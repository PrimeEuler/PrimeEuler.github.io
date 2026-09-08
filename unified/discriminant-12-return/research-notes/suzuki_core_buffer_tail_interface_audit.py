#!/usr/bin/env python3
"""Core-buffer-tail interface audit for Suzuki's a=1 even-v sector.

This checkpoint follows the v13.312 certified tail cutoff N=151 and asks how
best to use that positivity in a finite-to-infinite reduction.

The key distinction is between:

1. a fixed low near-null core, taken here as odd Dirichlet modes n<=19;
2. a finite buffer of higher modes below a chosen tail cutoff N;
3. the certified coercive tail n>=N.

The whole low/tail interface is not small merely because N is large: the prime
shift operator is bounded but noncompact, so modes immediately below and above
an interface can remain O(1)-coupled.  By contrast, a fixed finite core does
decouple from a remote tail, with individual prime-shift matrix entries
decaying like O(1/n) for fixed core mode m and n->infinity.

For the normalized even-v odd Dirichlet basis

    psi_n(x)=(-1)^((n-1)/2) cos(n*pi*x/2),   n odd,

the truncated two-sided shift

    (S_l f)(x)=f(x-l)+f(x+l),

with f=0 outside [-1,1], has matrix elements that can be evaluated exactly by
integrating products of cosines over the two overlap intervals.  The joint
prime operator is

    B_prime = -sum_q a_q S_log(q),

q in {2,3,4,5,7}, a_q=Lambda(q)/sqrt(q).

The script reports numerical Hilbert-Schmidt norms of the fixed core-to-tail
prime block, truncated at a large maximum mode.  These are diagnostic, not
rigorous infinite-tail enclosures.  Their purpose is to identify the correct
block architecture before a certified Schur/Feshbach reduction is attempted.

No RH/GRH, kernel, lambda_1=0, or global positivity conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np

SHIFTS = [math.log(2.0), math.log(3.0), math.log(4.0),
          math.log(5.0), math.log(7.0)]
WEIGHTS = [
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
]


def phase(n: int) -> float:
    if n % 2 != 1:
        raise ValueError('use odd n in the even-v sector')
    return -1.0 if ((n-1)//2) % 2 else 1.0


def _int_coscos(a: float, b: float, theta: float,
                left: float, right: float) -> float:
    """Integral cos(a x) cos(b x + theta) dx over [left,right]."""
    def F(x: float) -> float:
        if abs(a-b) < 1e-14:
            first = 0.5*x*math.cos(theta)
        else:
            first = 0.5*math.sin((a-b)*x-theta)/(a-b)
        second = 0.5*math.sin((a+b)*x+theta)/(a+b)
        return first + second
    return F(right)-F(left)


def shift_entry(m: int, n: int, ell: float) -> float:
    """Return <psi_m,S_ell psi_n> exactly up to floating evaluation."""
    a = m*math.pi/2.0
    b = n*math.pi/2.0
    # psi_n(x-ell), x in [-1+ell,1]
    i_minus = _int_coscos(a,b,-b*ell,-1.0+ell,1.0)
    # psi_n(x+ell), x in [-1,1-ell]
    i_plus = _int_coscos(a,b,b*ell,-1.0,1.0-ell)
    return phase(m)*phase(n)*(i_minus+i_plus)


def prime_entry(m: int, n: int) -> float:
    return -sum(w*shift_entry(m,n,ell) for w,ell in zip(WEIGHTS,SHIFTS))


def core_modes(max_core: int = 19) -> list[int]:
    return list(range(1,max_core+1,2))


def core_tail_prime_hs(cutoff: int, max_tail: int = 3001,
                       max_core: int = 19) -> float:
    if cutoff % 2 == 0:
        cutoff += 1
    total = 0.0
    for m in core_modes(max_core):
        for n in range(cutoff,max_tail+1,2):
            z = prime_entry(m,n)
            total += z*z
    return math.sqrt(total)


def interface_samples(cutoff: int) -> dict:
    """Show that adjacent buffer/tail modes need not have small prime coupling."""
    if cutoff % 2 == 0:
        cutoff += 1
    m = cutoff-2
    n = cutoff
    return {
        'm': m,
        'n': n,
        'prime_entry': prime_entry(m,n),
        'abs_prime_entry': abs(prime_entry(m,n)),
    }


def report(cutoffs=(151,201,237,301,401,501), max_tail=3001) -> dict:
    return {
        'core_max_n': 19,
        'tail_truncation_max_n': max_tail,
        'core_tail_prime_hs': [
            {'cutoff':N,
             'hs_truncated':core_tail_prime_hs(N,max_tail=max_tail)}
            for N in cutoffs
        ],
        'interface_samples': [interface_samples(N) for N in cutoffs],
        'status': 'numerical interface audit; not an infinite-tail certificate',
    }


if __name__ == '__main__':
    r=report()
    print('Suzuki core-buffer-tail interface audit')
    print('fixed near-null core: odd n<=',r['core_max_n'])
    print('core-to-tail prime HS, tail truncated at n<=',r['tail_truncation_max_n'])
    for row in r['core_tail_prime_hs']:
        print(row)
    print('adjacent interface samples')
    for row in r['interface_samples']:
        print(row)
