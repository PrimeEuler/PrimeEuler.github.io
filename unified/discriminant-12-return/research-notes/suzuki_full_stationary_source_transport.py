#!/usr/bin/env python3
"""Stationarity-correct the full finite source and certify its energy defect."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_outward_certificate import read_snapshot,raw_source,subtract,support_dot,operator_radius
from suzuki_exact_integer_source_action import ExactSource,norm2,dot,sqrt_upper
from suzuki_trace_congruence_replay import inv,mul,tr
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
PINS={
'even-v':('da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5',
'87afab76d9b22e574b040e553623460456b0bcd819c2dde7985e6c783f92ba61'),
'odd-v':('6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453',
'4ead74028da43fbab4ae1f859c62e6d738113417d8cdc22cec9ac4903d022c3a')}
def display(q):return format(float(q),'.15g')
QBITS=512
def rounded(q,bits=QBITS):return F(q.numerator*(1<<bits)//q.denominator,1<<bits)
def combine(V,q):
    bits=max([V[6]['bits']]+[v['bits']+QBITS for v in V[:6]])
    out=[x<<(bits-V[6]['bits']) for x in V[6]['values']]
    for v,a in zip(V[:6],q):
        av=int(a*(1<<QBITS));shift=bits-v['bits']-QBITS
        out=[x+((av*y)<<shift) for x,y in zip(out,v['values'])]
    return {'bits':bits,'values':out}
def run(root,sector):
    stem=f'joint-256000-{sector}.trace-256000.full'
    sp=root/(stem+'.zip');cp=root/(stem+'.certificate.json')
    assert hashlib.sha256(sp.read_bytes()).hexdigest()==PINS[sector][0]
    raw=cp.read_bytes();assert hashlib.sha256(raw).hexdigest()==PINS[sector][1]
    d=json.loads(raw);meta,source,V,P=read_snapshot(sp)
    assert meta['remote_start']==32000 and meta['sector']==sector
    assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
    M=[[F(x) for x in row] for row in d['M_point_decimal']]
    J=[row[:6] for row in M[:6]];beta=[[-M[i][6]] for i in range(6)]
    pointq=mul(inv(J),beta);q=[rounded(x[0]) for x in pointq]
    assert any(q)
    Z=combine(V,q);g=raw_source(source['modes'],sector,32000)
    print(sector,'combined vector constructed; exact action begins',flush=True)
    mompath=root/('frozen256-'+('even' if sector=='even-v' else 'odd')+'-moments.json')
    mr=mompath.read_bytes();mom=json.loads(mr)
    assert mom['snapshot_sha256']==PINS[sector][0] and mom['certificate_sha256']==PINS[sector][1]
    assert [str(x) for x in q]==mom['stationary_coefficients_rounded_down_rational']
    assert norm2(Z)==F(mom['trial_l2_squared_rational'])
    n=source['modes'];power=[1]*len(n);checked=0
    for old in mom['moments']:
        zz=F(sum(a*b*t for a,b,t in zip(source['z']['values'],Z['values'],power)),1<<(source['z']['bits']+Z['bits']))
        mm=F(sum(a*b*t for a,b,t in zip(n,Z['values'],power)),1<<Z['bits'])
        xx=F(sum(abs(b)*t for b,t in zip(Z['values'],power)),1<<Z['bits'])
        assert zz==F(old['Z_even_rational']) and mm==F(old['M_odd_rational']) and xx==F(old['X_even_abs_rational'])
        checked+=3;power=[t*k*k for t,k in zip(power,n)]
    assert F(sum(abs(a*b)*t for a,b,t in zip(source['z']['values'],Z['values'],power)),1<<(source['z']['bits']+Z['bits']))==F(mom['S22_z_point_rational'])
    assert F(sum(abs(a)*k*t for a,k,t in zip(Z['values'],n,power)),1<<Z['bits'])==F(mom['S23_point_rational'])
    assert F(sum(abs(a) for a in Z['values']),1<<Z['bits'])==F(mom['trial_l1_rational'])
    assert dot(source['pole'],Z)==F(mom['pole_moment_rational'])
    AZ=ExactSource(source,meta['kernel_bits']).action(Z)
    s0=subtract(AZ,g);gram=[[dot(a,b) for b in P] for a in P]
    projected=[[support_dot(p,s0)] for p in P]
    qpoint2=norm2(s0)-mul(tr(projected),mul(inv(gram),projected))[0][0]
    assert qpoint2>=0
    graph_dots=[dot(w,s0) for w in V[:6]]
    gradient=[M[i][6]+sum(J[i][k]*q[k] for k in range(6)) for i in range(6)]
    serialization=F(1,10**100)*(1+sum(abs(x) for x in q))
    assert all(abs(x-y)<=serialization for x,y in zip(graph_dots,gradient))
    wn=sqrt_upper(F(d['graph_vector_norm2_rational']),192)
    zn=sqrt_upper(norm2(Z),192);da,_,_=operator_radius(source,meta['kernel_bits'])
    assert da==F(d['operator_radius_rational'])
    dg=F(len(source['modes']),1<<g['bits']);input_error=da*zn+dg
    qs=sqrt_upper(qpoint2,192)+input_error
    ds=sqrt_upper(sum(x*x for x in graph_dots),192)+wn*input_error
    gamma=F('2.37e-13' if sector=='even-v' else '4.15e-12')
    rho=F(d['relative_trace_fro_upper_rational']);nu=rho/(1-rho)
    b={k:F(x) for k,x in d['bounds_rational'].items()}
    f=b['graph_residual_fro']/(1-rho)
    j=min(J[i][i]-sum(abs(J[i][k]) for k in range(6) if k!=i) for i in range(6))
    mn=max(sum(abs(x) for x in row) for row in M)
    alpha=b['assembly_J']+2*b['assembly_beta']+b['assembly_eta']
    a=b['assembly_J']+nu*(2+nu)*(mn+alpha)+f*f/gamma
    h=j-a;assert h>0
    energy=qs*qs/gamma+(ds/(1-rho)+f*qs/gamma)**2/h
    eta=21*sqrt_upper(energy,192)
    # Quantify the omitted protected stationarity in the old fixed-trace source.
    beta_norm=sqrt_upper(sum(x[0]**2 for x in beta),192)
    cross=b['assembly_beta']+nu*(2+nu)*(mn+alpha)
    corrected_s=b['source_residual_l2']+b['graph_residual_fro']*nu
    cross+=f*corrected_s/gamma
    protected_point=mul(tr(beta),pointq)[0][0]
    protected_error=cross*(2*beta_norm+cross)/h+a*beta_norm**2/(j*h)
    assert protected_point>protected_error
    width=max(1,(max(abs(x).bit_length() for x in Z['values'])+8)//8)
    packed=b''.join(x.to_bytes(width,'little',signed=True) for x in Z['values'])
    values={'represented_full_stationary_vector_norm2':norm2(Z),
      'projected_point_residual_norm2':qpoint2,'physical_projected_full_residual_upper':qs,
      'point_graph_dot_norm2':sum(x*x for x in graph_dots),
      'physical_graph_dot_full_residual_upper':ds,'operator_radius':da,
      'finite_stationary_graph_floor':h,'full_finite_inverse_energy_error_upper':energy,
      'whole_remote_source_transport_upper':eta,
      'omitted_protected_stationary_energy_point':protected_point,
      'omitted_protected_stationary_energy_lower':protected_point-protected_error,
      'omitted_protected_stationary_energy_upper':protected_point+protected_error}
    return {'sector':sector,'source_snapshot_sha256':PINS[sector][0],
      'source_certificate_sha256':PINS[sector][1],
      'full_source_vector_recipe':'Z=V6+sum(q[j]*Vj), all coordinates exact dyadic',
      'q_dyadic_bits':QBITS,'q_rational':[str(x) for x in q],
      'full_vector_bits':Z['bits'],'full_vector_width':width,
      'full_vector_count':len(Z['values']),'full_vector_binary_sha256':hashlib.sha256(packed).hexdigest(),
      'point_gradient_serialization_identity_checked':True,
      'far_moments_input_sha256':hashlib.sha256(mr).hexdigest(),
      'all_existing_far_moments_match_corrected_vector':True,
      'exact_replayed_far_moment_values':checked,
      'rational':{k:str(v) for k,v in values.items()},
      'display_approximate':{k:display(v) for k,v in values.items()},
      'transport_below_2e_minus10':eta<F('2e-10'),
      'transport_below_revised_1e_minus9':eta<F('1e-9'),
      'source_assembly_certified':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True)
    p.add_argument('--sector',choices=list(PINS),required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=run(a.root,a.sector)
    a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps(o['display_approximate'],indent=2))
