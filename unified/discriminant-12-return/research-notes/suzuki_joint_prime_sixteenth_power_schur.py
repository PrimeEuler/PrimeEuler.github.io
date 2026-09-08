#!/usr/bin/env python3
"""Sixteenth-power Schur audit for Suzuki's joint prime operator at a=1.

Let A=-B_prime=sum_q a_q S_log(q), q in {2,3,4,5,7}.  A has a nonnegative
symmetric kernel, hence ||B_prime||=||A|| <= sup_x(A^k 1)(x)^(1/k).
Piecewise-constant inputs remain piecewise constant, so each iterate is an
exact finite breakpoint sweep.

At k=16 the ordinary floating-point evaluation gives
    intervals = 3345
    sup_x(A^16 1)(x) = 93388.18411213082
    ||B_prime|| <= 2.044764260347282.
The finite-breakpoint reduction is exact; displayed decimals are not interval
certified.

Combined with the existing analytic archimedean bound and localized cusp/pole
bounds, the first sufficient odd cutoff is N=1165.

No RH/GRH, kernel, or lambda_1=0 conclusion follows.
"""
from __future__ import annotations
import math
import numpy as np

SHIFTS=np.array([math.log(2.0),math.log(3.0),math.log(4.0),math.log(5.0),math.log(7.0)])
WEIGHTS=np.array([math.log(2.0)/math.sqrt(2.0),math.log(3.0)/math.sqrt(3.0),math.log(2.0)/2.0,math.log(5.0)/math.sqrt(5.0),math.log(7.0)/math.sqrt(7.0)])
EULER_GAMMA=0.5772156649015328606

def eval_piecewise(bps,vals,x):
    if x < -1.0 or x > 1.0: return 0.0
    if x == 1.0: return float(vals[-1])
    j=int(np.searchsorted(bps,x,side='right')-1)
    return float(vals[max(0,min(j,len(vals)-1))])

def apply_A(bps,vals):
    new={-1.0,1.0}
    for b in bps:
        for ell in SHIFTS:
            for z in (b-ell,b+ell):
                if -1.0 < z < 1.0: new.add(float(z))
    nb=np.array(sorted(new),dtype=float); nv=[]
    for lo,hi in zip(nb[:-1],nb[1:]):
        x=0.5*(lo+hi)
        nv.append(sum(a*(eval_piecewise(bps,vals,x+ell)+eval_piecewise(bps,vals,x-ell)) for ell,a in zip(SHIFTS,WEIGHTS)))
    return nb,np.array(nv,dtype=float)

def power_schur(power=16):
    bps=np.array([-1.0,1.0]); vals=np.array([1.0]); seq=[]
    for k in range(1,power+1):
        bps,vals=apply_A(bps,vals); supv=float(np.max(vals))
        seq.append({'power':k,'intervals':len(vals),'sup_Ak1':supv,'root_bound':supv**(1.0/k)})
    return {'sequence':seq,'prime_bound':seq[-1]['root_bound']}

def s2(N): return 1.0/N**2+1.0/(2.0*N)
def s4(N): return 1.0/N**4+1.0/(6.0*N**3)
def s6(N): return 1.0/N**6+1.0/(10.0*N**5)
def cusp_tail_bound(N):
    rank=(2.0/math.pi**2)*s2(N); c=2.0/math.pi**3+6.0/math.pi**4; alpha=2.0*c/math.pi
    off=2.0*alpha*math.sqrt((math.pi**2/12.0)*s6(N)); C=2.0/math.pi**2+2.0/math.pi**3+2.0/math.pi**4+6.0/math.pi**5
    return rank+off+C*math.sqrt(s4(N))
def pole_tail_bound(N): return 32.0*math.cosh(0.5)**2/math.pi**2*s2(N)
def arch_bound():
    q=2.0/math.pi
    return 2.0*(0.5+math.lgamma(1.0-q)-EULER_GAMMA*q)
def cutoff():
    prime=power_schur(16)['prime_bound']
    for N in range(1,100000,2):
        total=math.pi/2.0+prime+arch_bound()+cusp_tail_bound(N)+pole_tail_bound(N)
        margin=math.log(N/4.0)-total
        if margin>0: return {'N':N,'prime_bound':prime,'arch_bound':arch_bound(),'cusp_tail':cusp_tail_bound(N),'pole_tail':pole_tail_bound(N),'total':total,'margin':margin}
    raise RuntimeError('cutoff not found')

if __name__=='__main__':
    for row in power_schur(16)['sequence']: print(row)
    print('coercive cutoff',cutoff())
