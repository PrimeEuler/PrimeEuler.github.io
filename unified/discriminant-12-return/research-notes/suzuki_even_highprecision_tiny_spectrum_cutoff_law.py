#!/usr/bin/env python3
"""Cutoff-law diagnostic for the first four tiny even-v Suzuki eigenvalues.

The high-precision finite matrices show an early rapid collapse of the first four
levels, followed by a much slower regime.  This helper records the current
M=29..119 ladder and computes local effective exponents under two deliberately
forced zero-limit models:

    lambda ~ M^{-p},
    lambda ~ exp(-c M).

The point is diagnostic: the local p and c values do not stabilize in the late
window, so neither simple model is promoted.  The data also do not yet
separate a tiny positive limiting level from slower decay to zero.

No exact-zero, infinite-operator sign, RH, or GRH conclusion follows.
"""
from __future__ import annotations
import math

DATA={
29:(3.43644597e-25,1.4112442e-19,1.155951e-14,1.8139834e-10),
39:(4.798499169636197e-28,6.112586643700622e-22,1.362339985676821e-16,6.612293158998051e-12),
49:(2.11014098e-29,5.1327702e-23,2.730166e-17,2.6427501e-12),
59:(1.0813726e-29,3.8993034e-23,2.2248169e-17,2.1312665e-12),
69:(8.6421607e-30,3.5032592e-23,1.9246842e-17,1.95358e-12),
79:(8.081065357e-30,3.343042341e-23,1.854669666e-17,1.896334934e-12),
89:(7.894433029e-30,3.069718115e-23,1.802990865e-17,1.844343305e-12),
99:(7.662203524e-30,2.820247787e-23,1.787327172e-17,1.750303244e-12),
109:(7.12753787141e-30,2.74394414108e-23,1.74262194311e-17,1.62910467195e-12),
119:(6.92050652436e-30,2.72737259564e-23,1.69915892537e-17,1.57381187469e-12),
}


def local_power(a,b,ya,yb):
    return -math.log(yb/ya)/math.log(b/a)


def local_exp(a,b,ya,yb):
    return -math.log(yb/ya)/(b-a)


def report():
    Ms=sorted(DATA)
    for j in range(4):
        print('level',j+1)
        for a,b in zip(Ms[-6:-1],Ms[-5:]):
            ya,yb=DATA[a][j],DATA[b][j]
            print(' ',a,'->',b,
                  'ratio=',yb/ya,
                  'p_zero=',local_power(a,b,ya,yb),
                  'c_zero=',local_exp(a,b,ya,yb))

    assert all(DATA[M][j] > 0 for M in Ms for j in range(4))
    # Late ratios are close to one: the early rapid-collapse regime has ended.
    assert DATA[119][0]/DATA[69][0] > 0.75
    assert DATA[119][2]/DATA[69][2] > 0.85
    print('CONCLUSION: early rapid collapse crosses over to a much slower regime')
    print('GUARDRAIL: no simple zero-limit power/exponential law is promoted')
    print('GUARDRAIL: positive plateau vs slow decay to zero remains unresolved')


if __name__=='__main__':
    report()
