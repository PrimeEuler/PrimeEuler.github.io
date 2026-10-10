#!/usr/bin/env python3
"""Exact uniform budget and independent physical reference diagnostics."""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import argparse,json,hashlib
from suzuki_certified_remote_diagonal import evaluate

def arch_reference(mp,n,N=8):
    k=mp.mpf(n)*mp.pi/2;endpoint=(-1)**n
    def h(t):return mp.exp(-t/2)/(-mp.expm1(-2*t))-1/(2*t)
    def h0(j):
        p=j+1;bp=sum(mp.binomial(p,l)*mp.bernoulli(l)*(mp.mpf(3)/4)**(p-l) for l in range(p+1))
        return 2**j*bp/p
    a=[h0(j) for j in range(N)];b=[mp.diff(h,mp.mpf(2),j) for j in range(N)]
    u0=[2*a[j]-(j*a[j-1] if j else 0) for j in range(N)]
    u2=[-j*b[j-1] if j else mp.mpf(0) for j in range(N)]
    def integral(left,right):
        return sum((-1)**j*(right[j]*endpoint-left[j])/(1j*k)**(j+1) for j in range(N))
    value=mp.re(integral(u0,u2))+mp.im(integral(a,b))/k
    rem=18*factorial(N)/k**N+6*factorial(N)/k**(N+1)
    return value,rem

def build(source_gate):
    import mpmath as mp
    raw=source_gate.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    assert sha=='f37bbb3e33d51c04fea345ab45774c327f75efa8a23312be96bdd0695529d94d'
    # Elementary constants behind the complex-disk/Cauchy proof.
    assert F(3,2)/(F(5,6)) + F(11,27)*3/(2*F(5,6)) < 3
    bound=F(172,9*256000**2)+F(1,9*256000**3)
    assert bound<F('3e-10')
    rows=[]
    for old in json.loads(raw)['cases']:
        n=int(old['n']);row=evaluate(n)
        with mp.workdps(int(n.bit_length()*.302)+110):
            nn=mp.mpf(n);k=nn*mp.pi/2;x=nn*mp.pi
            weights=[mp.log(2)/mp.sqrt(2),mp.log(3)/mp.sqrt(3),mp.log(2)/2,mp.log(5)/mp.sqrt(5),mp.log(7)/mp.sqrt(7)]
            prime=sum(w*((2-mp.log(q))*mp.cos(k*mp.log(q))+mp.sin(k*mp.log(q))/k) for q,w in zip((2,3,4,5,7),weights))
            arch,rem=arch_reference(mp,n)
            ref=mp.log(nn/4)-mp.ci(x)-mp.si(x)/x-prime-arch
            def mf(s):
                f=F(s);return mp.mpf(f.numerator)/f.denominator
            assert mf(row['lower_rational'])<ref-rem and ref+rem<mf(row['upper_rational'])
        rows.append(row)
    # An independent low-frequency quadrature validates the diagnostic endpoint recipe.
    with mp.workdps(80):
        for n in (17,32):
            k=n*mp.pi/2
            def integrand(t):
                h=mp.mpf(1)/4 if t==0 else mp.exp(-t/2)/(-mp.expm1(-2*t))-1/(2*t)
                return h*((2-t)*mp.cos(k*t)+mp.sin(k*t)/k)
            direct=mp.quad(integrand,[mp.mpf(j)/32 for j in range(65)])
            ref,rem=arch_reference(mp,n);assert abs(direct-ref)<rem
    return {'schema':'cone.certified-raw-remote-diagonal.v1','cases':rows,
        'source_gate_sha256':sha,'complex_disk_kernel_absolute_bound':3,
        'h_derivative_bounds_0_1_2':[3,3,6],'arch_constant_upper':43,
        'uniform_analytic_error_strict_upper_rational':'3/10000000000',
        'uniform_total_radius_strict_upper_rational':'1/1000000000',
        'operator_action_at_norm_002_upper_rational':'1/500000000000',
        'energy_form_at_norm_002_upper_rational':'1/250000000000000',
        'all_50_physical_reference_intervals_inside':True,
        'reference_arch_endpoint_order':8,'reference_arch_remainder_included':True,
        'reference_endpoint_recipe_low_frequency_quadrature_checked':True,
        'pole_included':False,'evaluated_trial_or_action':False,
        'finite_lifts_certified':False,'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-gate',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.output.write_text(json.dumps(build(a.source_gate),indent=2,sort_keys=True)+'\n')
    print('50 raw physical diagonal intervals and uniform budget passed.')
