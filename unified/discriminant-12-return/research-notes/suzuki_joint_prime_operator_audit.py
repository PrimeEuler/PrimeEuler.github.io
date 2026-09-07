#!/usr/bin/env python3
"""Joint five-shift prime-operator audit for Suzuki a=1 even-v sector.

The prime contribution is

    B_prime = - sum_q a_q S_{log q},
    a_q = Lambda(q)/sqrt(q),
    q in {2,3,4,5,7},

with (S_l f)(x)=f(x-l)+f(x+l) under zero extension outside [-1,1].

This checkpoint gives a rigorous Schur bound for the *joint* operator by
counting which translated points remain inside the interval.  For

    R(x)=sum_q a_q [1_{|x-log q|<=1}+1_{|x+log q|<=1}],

symmetry gives ||B_prime|| <= sup_x R(x).  A breakpoint sweep shows

    sup_x R(x) = sum_q a_q = 2.9262341821764086...

which improves the v13.305 separate-shift bound 3.129252291....

A Galerkin finite-section calculation in odd Dirichlet modes is also included
as numerical evidence only; it suggests a true spectral radius near 1.94.
That numerical value is NOT used in the rigorous coercivity cutoff.

No RH/GRH, kernel, or lambda_1=0 conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.legendre import leggauss

SHIFTS = [math.log(2.0), math.log(3.0), math.log(4.0), math.log(5.0), math.log(7.0)]
WEIGHTS = [
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
]
EULER_GAMMA = 0.5772156649015328606


def row_sum(x: float) -> float:
    s = 0.0
    for ell,a in zip(SHIFTS,WEIGHTS):
        if abs(x-ell) <= 1.0:
            s += a
        if abs(x+ell) <= 1.0:
            s += a
    return s


def exact_joint_schur_bound() -> float:
    bps = {-1.0,1.0}
    for ell in SHIFTS:
        for z in (ell-1.0,ell+1.0,-ell-1.0,-ell+1.0):
            if -1.0 <= z <= 1.0:
                bps.add(z)
    bps = sorted(bps)
    tests = list(bps)
    tests += [(a+b)/2.0 for a,b in zip(bps[:-1],bps[1:])]
    return max(row_sum(x) for x in tests)


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0/math.pi**2) * odd_sum2_tail_bound(N)
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    C_diag = 2.0/math.pi**2 + 2.0/math.pi**3 + 2.0/math.pi**4 + 6.0/math.pi**5
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def pole_tail_bound(N: int) -> float:
    return 32.0*math.cosh(0.5)**2/math.pi**2 * odd_sum2_tail_bound(N)


def arch_remainder_analytic_bound() -> float:
    q = 2.0/math.pi
    return 2.0*(0.5 + math.lgamma(1.0-q) - EULER_GAMMA*q)


def coercive_cutoff(max_search: int = 100_000) -> dict:
    prime = exact_joint_schur_bound()
    for N in range(1,max_search+1,2):
        total = math.pi/2.0 + prime + arch_remainder_analytic_bound() + cusp_tail_bound(N) + pole_tail_bound(N)
        margin = math.log(N/4.0) - total
        if margin > 0:
            return {'N':N,'prime_bound':prime,'total_tail_bound':total,'margin':margin}
    raise RuntimeError('cutoff not found')


def galerkin_joint_norm(odd_modes: int = 120, quad_order: int = 1200) -> dict:
    # Numerical only: odd Dirichlet modes psi_n(x)=(-1)^((n-1)/2) cos(n pi x/2).
    ns = np.arange(1,2*odd_modes,2)
    x,w = leggauss(quad_order)
    Phi = np.empty((quad_order,odd_modes))
    for j,n in enumerate(ns):
        Phi[:,j] = ((-1)**((n-1)//2))*np.cos(n*math.pi*x/2.0)
    B = np.zeros((odd_modes,odd_modes))
    for ell,a in zip(SHIFTS,WEIGHTS):
        S = np.zeros_like(Phi)
        xp=x+ell; xm=x-ell
        mp=np.abs(xp)<=1.0; mm=np.abs(xm)<=1.0
        for j,n in enumerate(ns):
            sg = (-1)**((n-1)//2)
            if np.any(mp):
                S[mp,j] += sg*np.cos(n*math.pi*xp[mp]/2.0)
            if np.any(mm):
                S[mm,j] += sg*np.cos(n*math.pi*xm[mm]/2.0)
        B += -a*(Phi.T @ (w[:,None]*S))
    B=(B+B.T)/2.0
    ev=np.linalg.eigvalsh(B)
    return {'odd_modes':odd_modes,'lambda_min':float(ev[0]),'lambda_max':float(ev[-1]),'spectral_radius':float(max(abs(ev[0]),abs(ev[-1])))}


if __name__ == '__main__':
    print('joint Schur bound =', exact_joint_schur_bound())
    print('coercive cutoff =', coercive_cutoff())
    for M in (20,40,80,120):
        print('Galerkin numerical', galerkin_joint_norm(M,1200))
