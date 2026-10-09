#!/usr/bin/env python3
"""Adaptive, outward physical remote-z evaluator using integer arithmetic."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial,isqrt
import argparse,json,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
QS=(2,3,4,5,7)
R=256000
TERMS=24

def enclosure(lo,hi,bits):
    scale=1<<bits
    return F(lo.numerator*scale//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)
def interval_add(a,b):return a[0]+b[0],a[1]+b[1]
def interval_mul(a,b):
    v=[x*y for x in a for y in b];return min(v),max(v)
def interval_recip(a):
    assert a[0]>0;return 1/a[1],1/a[0]
def midpoint(a,bits):
    q=(a[0]+a[1])/2;return F(q.numerator*(1<<bits)//q.denominator,1<<bits)
def radius(a,p):return max(abs(a[0]-p),abs(a[1]-p))
def atan_recip(q,bits):
    K=bits//4+12
    total=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(K)),F(0))
    nxt=F((-1)**K,(2*K+1)*q**(2*K+1))
    return min(total,total+nxt),max(total,total+nxt)
def log_interval(q,bits):
    r=F(q-1,q+1);K=2*bits+12
    total=2*sum((r**(2*k+1)/(2*k+1) for k in range(K)),F(0))
    tail=2*r**(2*K+1)/((2*K+1)*(1-r*r))
    return enclosure(total,total+tail,bits)

@lru_cache(maxsize=32)
def constants(bits):
    a=atan_recip(5,bits);b=atan_recip(239,bits)
    pi=enclosure(16*a[0]-4*b[1],16*a[1]-4*b[0],bits)
    assert 3<pi[0]<pi[1]<4
    pp=midpoint(pi,bits);logs={q:log_interval(q,bits) for q in QS}
    weights=[];phases=[]
    for q in QS:
        if q==4:wi=(logs[2][0]/2,logs[2][1]/2)
        else:
            root=isqrt(q<<(2*bits));si=(F(root,1<<bits),F(root+1,1<<bits))
            wi=interval_mul(logs[q],interval_recip(si))
        wi=enclosure(*wi,bits);wp=midpoint(wi,bits)
        assert 0<wi[0]<=wi[1]<1
        th=interval_mul(pi,logs[q]);th=enclosure(th[0]/2,th[1]/2,bits)
        weights.append((wp,radius(wi,wp)));phases.append((midpoint(th,bits),th))
    # Alternating e^-1 series, with a rigorous next-term remainder.
    K=1
    while F(1,factorial(K+1))>F(1,1<<(bits+12)):K+=1
    ep=sum((F((-1)**j,factorial(j)) for j in range(K+1)),F(0))
    nxt=F((-1)**(K+1),factorial(K+1))
    ei=(min(ep,ep+nxt),max(ep,ep+nxt))
    s0=enclosure(ei[0]/(1-ei[0]**4),ei[1]/(1-ei[1]**4),bits)
    return pi,pp,weights,phases,s0,midpoint(s0,bits)

def sin_integer(x,bits):
    scale=1<<bits;assert abs(x)<4*scale
    term=x;total=x
    for k in range(1,TERMS):
        term=-(term*x*x//(scale*scale*(2*k)*(2*k+1)))
        total+=term
    # Each recurrence multiplier <=16, each floor costs <2^-bits.
    rounding=F(TERMS*16**TERMS,scale)
    remainder=F(4**(2*TERMS+1),factorial(2*TERMS+1))
    return total,rounding+remainder

def evaluate(n,output_bits=64):
    assert isinstance(n,int) and n>R
    bits=max(192,((n.bit_length()+128+63)//64)*64)
    scale=1<<bits;pi,pp,weights,phases,s0,sp=constants(bits)
    pint=int(pp*scale);value=F(0);error=F(0);largest_phase_error=F(0)
    for (wp,dw),(tp,ti) in zip(weights,phases):
        full=n*int(tp*scale)
        reduced=(full+pint)%(2*pint)-pint
        k=(full-reduced)//(2*pint)
        phase_error=n*radius(ti,tp)+2*abs(k)*radius(pi,pp)
        sinp,ds=sin_integer(reduced,bits);s=F(sinp,scale)
        ds+=phase_error
        value+=2*wp*s
        error+=2*(dw*(1+ds)+abs(wp)*ds)
        largest_phase_error=max(largest_phase_error,phase_error)
    sign=1 if n%2==0 else -1
    coeff=(1-4*s0[1],1-4*s0[0]) if sign==1 else (1+4*s0[0],1+4*s0[1])
    ni=interval_add((pi[0]/2,pi[1]/2),interval_mul(coeff,(1/(n*pi[1]),1/(n*pi[0]))))
    np=pp/2+(1-4*sign*sp)/(n*pp)
    value+=np;error+=radius(ni,np)
    nonprime=F(4,9*R*R)+F(55,81*R**3)
    error+=nonprime
    assert largest_phase_error<F('1e-30') and error<F('1e-10')
    lo,hi=enclosure(value-error,value+error,output_bits)
    assert (hi-lo)/2<F('1e-10')
    return {'n':str(n),'working_bits':bits,'output_bits':output_bits,
      'lower_rational':str(lo),'upper_rational':str(hi),
      'radius_upper_rational':str((hi-lo)/2),
      'max_argument_reduction_error_rational':str(largest_phase_error),
      'parity_sign':sign,'physical_nonprime_error_included':True,
      'all_five_physical_prime_weights_retained':True,'uses_machine_sine':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('modes',type=int,nargs='+');a=p.parse_args()
    print(json.dumps([evaluate(n) for n in a.modes],indent=2,sort_keys=True))
