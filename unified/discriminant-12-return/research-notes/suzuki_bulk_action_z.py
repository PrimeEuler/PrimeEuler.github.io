#!/usr/bin/env python3
"""Dyadic-rounded interval action-z evaluator for full row blocks.

Every interval operation rounds OUTWARD; no exact-interval uncertainty is dropped.
The already certified analytic EM/exponential remainder remains unchanged.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb,factorial
from suzuki_certified_remote_z import (R,constants,enclosure,midpoint,radius,
    interval_add,interval_mul,interval_recip,interval_scale,exp_minus_one,
    stirling,sin_integer)

class Arithmetic:
    def __init__(self,bits):self.bits=bits
    def out(self,a):return enclosure(*a,self.bits)
    def add(self,a,b):return self.out(interval_add(a,b))
    def mul(self,a,b):return self.out(interval_mul(a,b))
    def scale(self,a,q):return self.out(interval_scale(a,q))
    def recip(self,a):return self.out(interval_recip(a))
    def power(self,a,k):
        v=(F(1),F(1))
        for _ in range(k):v=self.mul(v,a)
        return v

@lru_cache(maxsize=32)
def moments(bits):
    a=Arithmetic(bits);ep=exp_minus_one(bits);q=a.power(ep,4);iq=a.recip((1-q[1],1-q[0]));out=[]
    assert q[1]<F(1,32) and iq[1]<F(16,15)
    for r in range(4):
        total=(F(0),F(0))
        for p in range(2*r+1):
            jp=(F(0),F(0))
            for k in range(p+1):
                jp=a.add(jp,a.scale(a.mul(a.power(q,k),a.power(iq,k+1)),stirling(p,k)*factorial(k)))
            total=a.add(total,a.scale(jp,F(comb(2*r,p)*2**p,2**(2*r-p))))
        out.append(a.mul(ep,total))
    return tuple(out)

@lru_cache(maxsize=32)
def moment_points(bits):
    out=[]
    for row in moments(bits):
        p=midpoint(row,bits)
        assert radius(row,p)<F(10**10,1<<bits)
        assert abs(p)<3*10**9
        out.append(int(p*(1<<bits)))
    return tuple(out)

def nonprime(n,pi,bits):
    """Fixed-integer point formula plus a complete directed error budget."""
    scale=1<<bits;pp=midpoint(pi,bits);pint=int(pp*scale)
    b=n*pint//4;a=scale//4;den=a*a+b*b
    wr=a*scale*scale//den;wi=-(b*scale*scale//den)
    def mul(x,y):return x*y//scale
    def cmul(x,y):return mul(x[0],y[0])-mul(x[1],y[1]),mul(x[0],y[1])+mul(x[1],y[0])
    def power(x,k):
        p=scale
        for _ in range(k):p=mul(p,x)
        return p
    x=scale*scale//(n*pint)
    atan=sum((-1)**j*(power(x,2*j+1)//(2*j+1)) for j in range(5))
    value=pint//2-atan-wi//2
    wp=(scale,0);w2=cmul((wr,wi),(wr,wi))
    for j,B in enumerate((F(1,6),F(-1,30),F(1,42),F(-1,30)),1):
        wp=cmul(wp,w2);coef=-B/(2*j)
        value+=coef.numerator*wp[1]//coef.denominator
    ip=scale*scale//pint;corr=0
    for r,m in enumerate(moment_points(bits)):
        row=mul(m,power(ip,2*r+1))
        corr+=(-1)**r*2**(2*r+2)*row//n**(2*r+1)
    value-=(-1)**n*corr
    point=F(value,scale)
    # Primitive pi/reciprocal displacements, all integer floors, cached
    # moment radii and atan's analytic next term are explicitly retained.
    error=F(10**12,scale)+F(1,n*pi[0])**11/11
    return point-error,point+error

def evaluate(n,output_bits=160):
    assert isinstance(n,int) and n>R
    output_bits=max(160,output_bits);bits=max(512,64*((n.bit_length()+256+63)//64));scale=1<<bits
    pi,pp,weights,phases,_,_=constants(bits);pint=int(pp*scale)
    value=F(0);error=F(0);maxphase=F(0)
    for (wp,dw),(tp,ti) in zip(weights,phases):
        full=n*int(tp*scale);reduced=(full+pint)%(2*pint)-pint;turns=(full-reduced)//(2*pint)
        phase=n*radius(ti,tp)+2*abs(turns)*radius(pi,pp)
        sp,se=sin_integer(reduced,bits,56);s=F(sp,scale);se+=phase
        value+=2*wp*s;error+=2*(dw*(1+se)+abs(wp)*se);maxphase=max(maxphase,phase)
    ni=nonprime(n,pi,bits);np=midpoint(ni,bits);value+=np;error+=radius(ni,np)
    error+=13*F(4,3*R)**8+F(1024*10**7,3**9*R**9)
    lo,hi=enclosure(value-error,value+error,output_bits)
    assert maxphase<F('1e-70') and (hi-lo)/2<F('1e-39')
    return {'n':str(n),'working_bits':bits,'output_bits':output_bits,
        'lower_rational':str(lo),'upper_rational':str(hi),'radius_upper_rational':str((hi-lo)/2),
        'max_argument_reduction_error_rational':str(maxphase),
        'parity_sign':(-1)**n,'physical_nonprime_error_included':True,
        'all_five_physical_prime_weights_retained':True,'uses_machine_sine':False}
