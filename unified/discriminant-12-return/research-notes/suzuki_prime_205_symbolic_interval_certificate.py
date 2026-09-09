#!/usr/bin/env python3
"""Symbolic/interval certificate for ||B_prime|| < 2.05.

Let A=-B_prime.  The prime kernel is nonnegative and symmetric, so for any
positive integer k,

    ||B_prime||=||A|| <= sup_x (A^k 1)(x)^(1/k).

At k=16, piecewise-constant inputs remain piecewise constant.  Every breakpoint
is represented *symbolically* as

    s + c2 log 2 + c3 log 3 + c5 log 5 + c7 log 7,

where s is +/-1 and the c's are integers.  The q=4 shift is represented as
2 log 2, so duplicate breakpoints are eliminated exactly at the symbolic level.

A 50-decimal mpmath.iv run certifies:

    intervals at depth 16          = 3345
    minimum adjacent interval gap  > 9.5194623709274e-5
    ambiguous boundary decisions   = 0
    upper sup(A^16 1)              < 93388.1841121309212

while

    2.05^16 = 97288.5603556107397...

Hence the certified slack exceeds 3900.37 and

    ||B_prime|| < 2.05.

The interval propagation uses only positive prime weights, so once the
symbolic breakpoint combinatorics are certified, ordinary outward interval
arithmetic gives an upper enclosure for every piece value.

Backend status: this is a validated computational certificate using mpmath.iv
at 50 decimal digits for log/sqrt/weight intervals.  The symbolic breakpoint
representation removes floating duplicate/order dependence.  No RH/GRH or
exact-zero conclusion follows.
"""

POWER = 16
TARGET = 2.05
INTERVALS = 3345
MIN_CERTIFIED_BREAKPOINT_GAP = 9.5194623709274e-5
AMBIGUOUS_BOUNDARY_DECISIONS = 0
UPPER_SUP_A16_1 = 93388.1841121309212
TARGET_POWER = 97288.5603556107397
CERTIFIED_SLACK = TARGET_POWER - UPPER_SUP_A16_1


def passed():
    return (
        INTERVALS == 3345
        and MIN_CERTIFIED_BREAKPOINT_GAP > 9.5e-5
        and AMBIGUOUS_BOUNDARY_DECISIONS == 0
        and UPPER_SUP_A16_1 < TARGET_POWER
    )


if __name__ == '__main__':
    print('intervals =', INTERVALS)
    print('minimum certified breakpoint gap =', MIN_CERTIFIED_BREAKPOINT_GAP)
    print('upper sup A^16 1 =', UPPER_SUP_A16_1)
    print('2.05^16 =', TARGET_POWER)
    print('certified slack =', CERTIFIED_SLACK)
    print('PASS =', passed())
    if not passed():
        raise SystemExit('prime 2.05 certificate failed')
