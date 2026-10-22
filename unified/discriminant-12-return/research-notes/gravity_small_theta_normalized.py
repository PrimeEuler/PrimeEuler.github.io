#!/usr/bin/env python3
"""Gravity finite-temperature Maxwellian cross-covariance: normalized quadrature and hot expansion.
Units mu=T=K=1. For fixed eccentricity e<1 and Theta=mu/(2T sigma^2).
Requires numpy, scipy. No interaction with Suzuki sandbox."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf

def d_parallel(v,theta):
    chi=v*math.sqrt(theta)
    if chi < .2:
        moment=sum((-chi*chi)**k/(math.factorial(k)*(2*k+3)) for k in range(16))
        return 2*math.sqrt(theta)/math.sqrt(math.pi)*moment
    psi=erf(chi)-2*chi/math.sqrt(math.pi)*math.exp(-chi*chi)
    return psi/(2*chi*chi*v)

def mixed_cov(e,theta):
    def integrand(E):
        c=math.cos(E)
        v=math.sqrt((1+e*c)/(1-e*c))
        return 2*e*c*d_parallel(v,theta)
    mean=quad(integrand,0,2*math.pi,epsabs=1e-13,limit=500)[0]/(2*math.pi)
    return 8*(1-e*e)*mean

def leading(e,theta):
    q=math.sqrt(1-e*e)
    Dstar=2*math.sqrt(theta)/(3*math.sqrt(math.pi))
    return -96*Dstar*theta*q*(1-q)/5

for e in (.2,.6,math.sqrt(2/3),.95):
    for theta in (.001,.01,.04):
        exact=mixed_cov(e,theta)
        asym=leading(e,theta)
        assert exact<0
        print(f'e={e:.8f}, Theta={theta:.4f}, exact={exact:.12g}, leading={asym:.12g}, ratio={exact/asym:.8f}')
