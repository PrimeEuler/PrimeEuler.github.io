#!/usr/bin/env python3
"""Physical K10 far residual for the exact represented finite trial.

Preserves pole/Z cancellation in every retained even inverse power. Exact
finite inverse uncertainty is deliberately separate; this is not a capacity
certificate. All inequalities and constants use integer/Fraction arithmetic.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_trace_congruence_replay import display

if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)


def enclose(x,bits=384):
    scale=1<<bits
    lo=x[0].numerator*scale//x[0].denominator
    hi=-((-x[1].numerator*scale)//x[1].denominator)
    return F(lo,scale),F(hi,scale)


def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def times(x,y):
    v=[a*b for a in x for b in y];return min(v),max(v)
def recip(x):
    assert x[0]>0;return F(1)/x[1],F(1)/x[0]
def constant(x):return F(x),F(x)
def magnitude(x):return max(abs(x[0]),abs(x[1]))
def power(x,n):
    out=constant(1)
    for i in range(n):out=times(out,x)
    return out


def atan_recip(q,terms=180):
    total=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))
    next_term=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(total,total+next_term),max(total,total+next_term)


def hyperbolic(odd,terms=80):
    # Terms for cosh/sinh(1/2), all positive; successive omitted ratios
    # decrease, so the first omitted term/(1-ratio) bounds the whole tail.
    import math
    offset=int(odd)
    total=sum((F(1,2**(2*k+offset)*math.factorial(2*k+offset)) for k in range(terms)),F(0))
    e=2*terms+offset
    first=F(1,2**e*math.factorial(e));ratio=F(1,4*(e+1)*(e+2))
    return total,total+first/(1-ratio)


def sigma(q,n):return F(1,n**q)+F(1,2*(q-1)*n**(q-1))


def root_upper(q):
    # Keep >=128 relative guard bits even for powers as small as n^-48.
    # A fixed 2^-128 absolute square-root ceiling would destroy K10 scaling.
    bits=128+max(0,(q.denominator.bit_length()-q.numerator.bit_length()+1)//2)
    return sqrt_upper(q,bits=bits)


def root_lower(q):
    from math import isqrt
    bits=128+max(0,(q.denominator.bit_length()-q.numerator.bit_length()+1)//2)
    r=isqrt((q.numerator<<(2*bits))//q.denominator)
    out=F(r,1<<bits);assert out*out<=q
    return out


def expansion_self_test():
    # Independent direct-kernel evaluation checks all pole/Z signs and powers.
    pi=F(22,7);c=2/pi;modes=[1,3,5,7];xx=[F(3,7),F(-2,11),F(5,13),F(-7,17)]
    zz=[F(-4,5),F(5,7),F(2,3),F(-3,11)]
    for odd in (False,True):
        alpha=-2 if odd else 2;h=F(6,11) if odd else F(7,6)
        k=4*h/pi
        pole=lambda n:k/(n*(1+1/(pi*pi*n*n)))
        P=sum((pole(m)*x for m,x in zip(modes,xx)),F(0));d=alpha*k*P
        S22=sum((abs(z*x)*m**22 for z,x,m in zip(zz,xx,modes)),F(0))
        S23=sum((abs(x)*m**23 for x,m in zip(xx,modes)),F(0))
        for n in (15,32,127):
            zn=F(-13,7);u=F(1,n-1 if odd else n)
            direct=u-c*sum(((zn*m-n*z)*x/F(n*n-m*m) for m,z,x in zip(modes,zz,xx)),F(0))-alpha*pole(n)*P
            expanded=F(1,n)+ (F(1,n*(n-1)) if odd else 0)
            for j in range(11):
                Z=sum((z*m**(2*j)*x for z,m,x in zip(zz,modes,xx)),F(0))
                M=sum((m**(2*j+1)*x for m,x in zip(modes,xx)),F(0))
                expanded+=(c*Z-d*(-1)**j/pi**(2*j))/n**(2*j+1)-c*zn*M/n**(2*j+2)
            charge=c*F(4,3)*(S22/F(n**23)+8*S23/F(n**24))+abs(d)/pi**22/n**23
            assert abs(direct-expanded)<=charge
    return {'both_parities':True,'independent_direct_kernel_cases':6,'exact_rational_remainder_checks_pass':True}


def analyze(path):
    raw=Path(path).read_bytes();o=json.loads(raw)
    odd=o['sector']=='odd-v';R=o['cutoff'];n0=2*R+(2 if odd else 1)
    pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
    c=times(constant(2),recip(pi));h=enclose(hyperbolic(odd))
    k=times(times(constant(-8 if odd else 8),h),recip(pi))
    ez=F('1e-38');ep=F('1e-39');l1=F(o['trial_l1_rational'])
    pp=F(o['pole_moment_rational']);p=(pp-ep*l1,pp+ep*l1)
    d=times(k,p);pinv2=power(recip(pi),2)
    coeff=[];norm_z=F(0);norm_m=F(0)
    for row in o['moments']:
        j=row['j'];z=F(row['Z_even_rational']);err=ez*F(row['X_even_abs_rational'])
        zz=(z-err,z+err)
        pole=times(d,times(constant((-1)**j),power(pinv2,j)))
        # rho = u + c*Z/n - d/[n*(1+1/(pi*n)^2)] - c*z_n*M/n^2.
        a=add(times(c,zz),neg(pole))
        if j==0:a=add(a,constant(1))
        b=magnitude(a)*root_upper(sigma(4*j+2,n0))
        norm_z+=b
        norm_m+=8*magnitude(c)*abs(F(row['M_odd_rational']))*root_upper(sigma(4*j+4,n0))
        coeff.append({'j':j,'combined_Z_pole_interval_rational':[str(x) for x in a],
                      'combined_Z_pole_interval_display_approximate':[display(x) for x in a],
                      'norm_charge_rational':str(b),'norm_charge_display':display(b)})
    source_extra=F(0) if not odd else F(n0,n0-1)*root_upper(sigma(4,n0))
    az=F(o['S22_z_point_rational'])
    # |z_phys|<=|z_point|+ez; X22 <= S23/minimum positive mode.
    # S23 also bounds X22 because all physical integer modes >=1.
    ax=F(o['S23_point_rational']);az+=ez*ax
    geom_z=magnitude(c)*F(4,3)*az
    geom_m=magnitude(c)*F(4,3)*8*ax
    kernel_rem=root_upper(2*geom_z**2*sigma(46,n0)+2*geom_m**2*sigma(48,n0))
    # Exact pole geometric remainder, j=11, with denominator 1+t>=1.
    pole_rem=magnitude(d)*magnitude(power(recip(pi),22))*root_upper(sigma(46,n0))
    total=norm_z+norm_m+source_extra+kernel_rem+pole_rem
    leading=tuple(F(x) for x in coeff[0]['combined_Z_pole_interval_rational'])
    leading_min=F(0) if leading[0]<=0<=leading[1] else min(abs(x) for x in leading)
    nonleading=(norm_z-F(coeff[0]['norm_charge_rational']))+norm_m+source_extra+kernel_rem+pole_rem
    lower=max(F(0),leading_min*root_lower(F(1,2*n0))-nonleading)
    out={'schema':'cone.frozen-trial-physical-far-outward.v1','sector':o['sector'],
         'cutoff':R,'first_far_mode':n0,'moments_input_sha256':hashlib.sha256(raw).hexdigest(),
         'pi_interval_rational':[str(x) for x in pi],
         'hyperbolic_interval_rational':[str(x) for x in h],
         'finite_z_source_cap_rational':str(ez),'finite_pole_source_cap_rational':str(ep),
         'combined_even_inverse_power_channels':coeff,
         'norm_charges_rational':{'combined_Z_pole':str(norm_z),'oscillatory_M':str(norm_m),
                                 'odd_source':str(source_extra),'kernel_geometric':str(kernel_rem),
                                 'pole_geometric':str(pole_rem)},
         'far_norm_upper_rational':str(total),'far_norm_upper_display':display(total),
         'far_energy_upper_rational':str(total**2),'far_energy_upper_display':display(total**2),
         'far_norm_lower_rational':str(lower),'far_energy_lower_rational':str(lower**2),
         'far_energy_lower_display':display(lower**2),
         'represented_trial_far_energy_exceeds_4_96e_minus9_exact':lower**2>F('4.96e-9'),
         'far_energy_bound_le_4_96e_minus9_exact':total**2<=F('4.96e-9'),
         'physical_source_scalar_uncertainty_included':True,
         'independent_expansion_self_test':expansion_self_test(),
         'exact_finite_inverse_uncertainty_included':False,'infinite_capacity_tail_closed':False,
         'guardrail':'Physical residual of represented rounded finite Galerkin trial on n>2R only. Near octave and transport to the exact finite physical inverse remain required. This is not an inverse-weighted parity capacity difference.'}
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('--moments',required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    a=p.parse_args();o=analyze(a.moments);raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'sector':o['sector'],'far_energy_upper':o['far_energy_upper_display'],
                      'leading_channel':o['combined_even_inverse_power_channels'][0]['combined_Z_pole_interval_display_approximate'],
                      'infinite_capacity_tail_closed':False},indent=2))


if __name__=='__main__':main()
