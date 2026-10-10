#!/usr/bin/env python3
"""Outward raw physical diagonal; pole is deliberately separate."""
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
import argparse,json
from suzuki_certified_remote_z import (R,QS,constants,enclosure,midpoint,radius,
    interval_add,interval_mul,interval_recip,interval_scale,log_interval,sin_integer)

def cos_integer(x,bits,terms=24):
    scale=1<<bits
    assert abs(x)<4*scale
    term=scale;total=term
    for j in range(1,terms):
        term=-(term*x*x//(scale*scale*(2*j-1)*(2*j)))
        total+=term
    return total,F(terms*16**terms,scale)+F(4**(2*terms),factorial(2*terms))

@lru_cache(maxsize=160)
def fixed_log(q,bits):return log_interval(q,bits)

def log_normalized(n,bits):
    e=n.bit_length()-1;m=F(n,1<<e);r=(m-1)/(m+1)
    scale=1<<bits;rp=r.numerator*scale//r.denominator;K=bits+12
    term=rp;total=0
    for j in range(K):
        total+=term//(2*j+1)
        term=term*rp*rp//(scale*scale)
    value=F(2*total,scale)
    error=F(10*K+10,scale)+3*F(1,3)**(2*K+1)
    return interval_add(interval_scale(fixed_log(2,bits),e-2),(value-error,value+error))

def evaluate(n,output_bits=64):
    assert isinstance(n,int) and n>R
    bits=max(192,64*((n.bit_length()+128+63)//64));scale=1<<bits
    pi,pp,weights,phases,_,_=constants(bits);pint=int(pp*scale)
    result=log_normalized(n,bits);max_phase=F(0)
    # At x=n*pi: -Ci(x)-Si(x)/x = -1/(2n)+2*(-1)^n/x^2 +/- 3/x^3.
    ix=interval_scale(interval_recip(pi),F(1,n))
    cusp=interval_add((F(-1,2*n),F(-1,2*n)),interval_scale(interval_mul(ix,ix),2*(-1)**n))
    result=interval_add(result,cusp)
    invk=interval_scale(ix,2)
    for q,(wp,dw),(tp,ti) in zip(QS,weights,phases):
        full=n*int(tp*scale);reduced=(full+pint)%(2*pint)-pint
        turns=(full-reduced)//(2*pint)
        phase=n*radius(ti,tp)+2*abs(turns)*radius(pi,pp);max_phase=max(max_phase,phase)
        sp,se=sin_integer(reduced,bits);cp,ce=cos_integer(reduced,bits)
        si=(F(sp,scale)-se-phase,F(sp,scale)+se+phase)
        ci=(F(cp,scale)-ce-phase,F(cp,scale)+ce+phase)
        lq=fixed_log(q,bits);coef=(2-lq[1],2-lq[0])
        prime=interval_mul((wp-dw,wp+dw),interval_add(interval_mul(coef,ci),interval_mul(si,invk)))
        result=interval_add(result,(-prime[1],-prime[0]))
    arch=43*invk[1]**2;cusp_error=3*ix[1]**3
    lo,hi=enclosure(result[0]-arch-cusp_error,result[1]+arch+cusp_error,output_bits)
    assert max_phase<F('1e-30') and (hi-lo)/2<F('1e-9')
    return {'n':str(n),'working_bits':bits,'output_bits':output_bits,
        'lower_rational':str(lo),'upper_rational':str(hi),
        'radius_upper_rational':str((hi-lo)/2),
        'arch_error_upper_rational':str(arch),'cusp_error_upper_rational':str(cusp_error),
        'max_argument_reduction_error_rational':str(max_phase),
        'raw_physical_diagonal':True,'pole_included':False,
        'q4_weight_log2_over2':True,'uses_machine_trigonometry':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('modes',type=int,nargs='+');a=p.parse_args()
    print(json.dumps([evaluate(n) for n in a.modes],indent=2,sort_keys=True))
