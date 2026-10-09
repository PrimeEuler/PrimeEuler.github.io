#!/usr/bin/env python3
"""Adaptive, outward physical remote-z evaluator using integer arithmetic."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial,isqrt,comb
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

def sin_integer(x,bits,terms=TERMS):
    scale=1<<bits;assert abs(x)<4*scale
    term=x;total=x
    for k in range(1,terms):
        term=-(term*x*x//(scale*scale*(2*k)*(2*k+1)))
        total+=term
    # Each recurrence multiplier <=16, each floor costs <2^-bits.
    rounding=F(terms*16**terms,scale)
    remainder=F(4**(2*terms+1),factorial(2*terms+1))
    return total,rounding+remainder

@lru_cache(maxsize=32)
def exp_minus_one(bits):
    K=1
    while F(1,factorial(K+1))>F(1,1<<(bits+12)):K+=1
    total=sum((F((-1)**j,factorial(j)) for j in range(K+1)),F(0))
    nxt=F((-1)**(K+1),factorial(K+1))
    return enclosure(min(total,total+nxt),max(total,total+nxt),bits)

def interval_scale(a,q):return interval_mul(a,(F(q),F(q)))
def interval_power(a,k):
    r=(F(1),F(1))
    for _ in range(k):r=interval_mul(r,a)
    return r
def complex_interval_mul(a,b):
    ac=interval_mul(a[0],b[0]);bd=interval_mul(a[1],b[1])
    return interval_add(ac,(-bd[1],-bd[0])),interval_add(interval_mul(a[0],b[1]),interval_mul(a[1],b[0]))
def stirling(p,k):
    if p==0:return int(k==0)
    if k==0:return 0
    return k*stirling(p-1,k)+stirling(p-1,k-1)

def precise_nonprime(n,pi,bits):
    one=(F(1),F(1));b=interval_scale(pi,F(n,4));a=(F(1,4),F(1,4))
    den=interval_add(interval_power(a,2),interval_power(b,2));di=interval_recip(den)
    wi=(interval_mul(a,di),interval_scale(interval_mul(b,di),-1))
    x=(1/(n*pi[1]),1/(n*pi[0]));atan=(F(0),F(0))
    for j in range(5):atan=interval_add(atan,interval_scale(interval_power(x,2*j+1),F((-1)**j,2*j+1)))
    rem=x[1]**11/11;atan=(atan[0]-rem,atan[1]+rem)
    psi=interval_add(interval_scale(pi,F(1,2)),(-atan[1],-atan[0]))
    psi=interval_add(psi,interval_scale(wi[1],F(-1,2)))
    power=((F(1),F(1)),(F(0),F(0)));w2=complex_interval_mul(wi,wi)
    for j,B in enumerate((F(1,6),F(-1,30),F(1,42),F(-1,30)),1):
        power=complex_interval_mul(power,w2)
        psi=interval_add(psi,interval_scale(power[1],-B/(2*j)))
    ep=exp_minus_one(bits);q=interval_power(ep,4);iq=interval_recip((1-q[1],1-q[0]))
    moments=[]
    for r in range(4):
        total=(F(0),F(0))
        for p in range(2*r+1):
            jp=(F(0),F(0))
            for k in range(p+1):
                jp=interval_add(jp,interval_scale(interval_mul(interval_power(q,k),interval_power(iq,k+1)),stirling(p,k)*factorial(k)))
            total=interval_add(total,interval_scale(jp,F(comb(2*r,p)*2**p,2**(2*r-p))))
        moments.append(interval_mul(ep,total))
    # n*pi/k**(2r+2) = 2**(2r+2)/(n**(2r+1)*pi**(2r+1)).
    corr=(F(0),F(0));ip=interval_recip(pi)
    for r,m in enumerate(moments):
        row=interval_mul(m,interval_power(ip,2*r+1))
        corr=interval_add(corr,interval_scale(row,F((-1)**r*2**(2*r+2),n**(2*r+1))))
    sign=1 if n%2==0 else -1
    return interval_add(psi,interval_scale(corr,-sign))

def evaluate(n,output_bits=64,action_precision=False):
    assert isinstance(n,int) and n>R
    if action_precision:output_bits=max(output_bits,160)
    guard=256 if action_precision else 128
    bits=max(512 if action_precision else 192,((n.bit_length()+guard+63)//64)*64)
    scale=1<<bits;pi,pp,weights,phases,s0,sp=constants(bits)
    pint=int(pp*scale);value=F(0);error=F(0);largest_phase_error=F(0)
    for (wp,dw),(tp,ti) in zip(weights,phases):
        full=n*int(tp*scale)
        reduced=(full+pint)%(2*pint)-pint
        k=(full-reduced)//(2*pint)
        phase_error=n*radius(ti,tp)+2*abs(k)*radius(pi,pp)
        sinp,ds=sin_integer(reduced,bits,56 if action_precision else TERMS);s=F(sinp,scale)
        ds+=phase_error
        value+=2*wp*s
        error+=2*(dw*(1+ds)+abs(wp)*ds)
        largest_phase_error=max(largest_phase_error,phase_error)
    sign=1 if n%2==0 else -1
    if action_precision:
        ni=precise_nonprime(n,pi,bits);np=midpoint(ni,bits)
    else:
        coeff=(1-4*s0[1],1-4*s0[0]) if sign==1 else (1+4*s0[0],1+4*s0[1])
        ni=interval_add((pi[0]/2,pi[1]/2),interval_mul(coeff,(1/(n*pi[1]),1/(n*pi[0]))))
        np=pp/2+(1-4*sign*sp)/(n*pp)
    value+=np;error+=radius(ni,np)
    nonprime=13*F(4,3*R)**8+F(1024*10**7,3**9*R**9) if action_precision else F(4,9*R*R)+F(55,81*R**3)
    error+=nonprime
    cap=F('1e-39') if action_precision else F('1e-10')
    assert largest_phase_error<(F('1e-70') if action_precision else F('1e-30')) and error<cap
    lo,hi=enclosure(value-error,value+error,output_bits)
    assert (hi-lo)/2<cap
    return {'n':str(n),'working_bits':bits,'output_bits':output_bits,
      'lower_rational':str(lo),'upper_rational':str(hi),
      'radius_upper_rational':str((hi-lo)/2),
      'max_argument_reduction_error_rational':str(largest_phase_error),
      'parity_sign':sign,'physical_nonprime_error_included':True,
      'all_five_physical_prime_weights_retained':True,'uses_machine_sine':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('modes',type=int,nargs='+');p.add_argument('--action-precision',action='store_true');a=p.parse_args()
    print(json.dumps([evaluate(n,action_precision=a.action_precision) for n in a.modes],indent=2,sort_keys=True))
