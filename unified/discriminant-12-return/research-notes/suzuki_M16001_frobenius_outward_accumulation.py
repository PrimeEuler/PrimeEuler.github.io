#!/usr/bin/env python3
"""Outward arithmetic for the 79,910-term M16001 residual Frobenius norm.

This replaces the uncharged `sum((abs(R)+E)**2); sqrt` tail of v13.514.
For each nonnegative t_q=(|R_q|+E_q)^2 it charges formation, then charges
the complete sequential NTERM accumulation by gamma_NTERM*sum(t_q), and
finally gives a rigorous algebraic upper square-root endpoint using
sqrt(S_hi) <= sqrt(S_point)*(1+u)/(1-u) plus one final rounding allowance.

This script must be run together with the residual-entry producer; it accepts
R,E arrays rather than hardcoding their values.  It fails closed otherwise.
"""
import numpy as np
LD=np.longdouble; U=LD(2)**LD(-64); NTERM=79910

def gamma(k):
    ku=LD(k)*U
    if ku>=1: raise ArithmeticError
    return ku/(1-ku)

def outward_frobenius(R,E):
    R=np.asarray(R,dtype=LD); E=np.asarray(E,dtype=LD)
    if R.shape!=(7991,10) or E.shape!=R.shape: raise ValueError('need 7991x10 R,E')
    a=np.abs(R)+E
    # addition a=|R|+E
    ra=gamma(1)*(np.abs(R)+np.abs(E))
    # square a*a: propagate input radius and one multiplication rounding
    t=a*a
    rt=LD(2)*np.abs(a)*ra + ra*ra + gamma(1)*np.abs(t)
    # Exact target is <= sum(t+rt).  Charge the actual long-double reduction.
    terms=t+rt
    S=np.sum(terms,dtype=LD)
    sumabs=np.sum(np.abs(terms),dtype=LD) # nonnegative, retained explicitly
    rsum=gamma(NTERM)*sumabs
    Shi=S+rsum
    # np.sqrt point plus conservative relative one-op rounding.  The additional
    # division by (1-u) makes the printed endpoint algebraically outward even if
    # sqrt rounded downward.
    root=np.sqrt(Shi)
    root_hi=root*(LD(1)+U)/(LD(1)-U)
    print('NTERM =',NTERM)
    print('u =',U)
    print('gamma_NTERM =',gamma(NTERM))
    print('sum formed squared terms =',S)
    print('sum abs formed terms =',sumabs)
    print('gamma_NTERM accumulation charge =',rsum)
    print('charged squared-norm upper endpoint =',Shi)
    print('sqrt point =',root)
    print('OUTWARD Frobenius endpoint =',root_hi)
    return root_hi

if __name__=='__main__':
    raise RuntimeError('FAIL-CLOSED: import outward_frobenius and supply the actual 7991x10 R,E transcript arrays')
