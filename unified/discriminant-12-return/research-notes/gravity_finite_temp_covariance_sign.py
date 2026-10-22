#!/usr/bin/env python3
"""Finite-temperature scale/eccentricity cross-covariance sign probe.
The proof is analytic (paired eccentric anomaly + decreasing D_parallel).
This file checks dimensionless quadratures for representative parameters.
"""
import numpy as np
from scipy.special import erf
from scipy.integrate import quad
from math import sqrt, exp, pi

def psi(x):
    if x < 0.02:
        return 4/sqrt(pi)*(x**3/3-x**5/5+x**7/14-x**9/54)
    return erf(x)-2*x/sqrt(pi)*exp(-x*x)

def Dpar(v, sigma=1.0):
    if v < 1e-10:
        return 4/(3*sqrt(pi)*(sqrt(2)*sigma)**3)
    chi=v/(sqrt(2)*sigma)
    return psi(chi)/v**3

def signed_integral(e, sigma):
    # <D(v)(v^2-1)>_Kepler for mu=T=1, reduced via exact cancellation
    def f(E):
        c=np.cos(E)
        v=sqrt((1+e*c)/(1-e*c))
        return 2*e*c*Dpar(v,sigma)
    return quad(f,0,2*pi,epsabs=1e-12,limit=300)[0]/(2*pi)

for e in (0.1,0.5,sqrt(2/3),0.95):
    for sigma in (0.5,1.0,5.0):
        val=signed_integral(e,sigma)
        assert val < 0,(e,sigma,val)
        print(f'e={e:.7f} sigma={sigma:.3f} integral={val:.12e}')
print('The exact sign proof is in Gravity_Finite_Temperature_Covariance_Sign_Theorem.md')
