#!/usr/bin/env python3
"""Full-cutoff source-faithful S10 / six-plane tail diagnostic.

This records the numerical checkpoint reached after restoring the correct
rank-two archimedean formula (v13.387-v13.390) and introducing the quadratic
six-plane tail criterion (v13.391).

Actual finite split
-------------------

    C = {1,3,...,19},
    F = {21,23,...,16001},
    T = {16003,16005,...}.

A source-faithful rank-two LDL solve on the full 7991-mode F block, with the
full even-sector pole included by a rank-one Woodbury update, gives the finite
Schur spectrum

    lambda_1..lambda_4 : numerical zero scale only,
    lambda_5 ~= 3.82590205e-8,
    lambda_6 ~= 2.14472468e-4,
    lambda_7 ~= 7.69095194e-1,
    lambda_8 ~= 1.70185089,
    lambda_9 ~= 2.01522883,
    lambda_10~= 2.34737759.

The first four values are NOT claimed exact zeros.

Six-plane residual
------------------
Let Q be the numerical eigenvectors 5..10 of S_F and

    R = A_TC - A_TF A_FF^{-1} A_FC.

On the first actual equal-width tail band 16003..31983, the singular values of
RQ are approximately

    5.94798074e-2,
    1.53298835e-6,
    3.45792126e-9,
    7.58e-14, ...

and the normalized quadratic threshold contribution is

    delta_crit(first band) ~= 0.02748277.

Cumulative ordinary-double diagnostics are

    through 31,983   : 0.02748277
    through 63,999   : 0.04170390
    through 127,999  : 0.04894821
    through 255,999  : 0.05260991
    through 511,999  : 0.05445132
    through 1,023,999: 0.05537475

versus the validated-computational effective-tail coercivity target

    delta >= 4.6732 - 0.994^2/0.22
          = 0.1821272727...

Signed far-tail reduction
-------------------------
For one of the six projected directions, collect its low+finite coefficients
w_j (Q on C, minus A_FF^{-1}A_FC Q on F), with j<=16001.  The source-faithful
pole-free off-diagonal formula gives for n>16001

  r_n^(0) = (2/pi) [
      Z_n/n^2 * sum_j j w_j/(1-j^2/n^2)
      - 1/n * sum_j Z_j w_j/(1-j^2/n^2)
  ].

The pole adds 2 c_n p, p=sum_j c_j w_j.  Extract the signed leading channel

  L/n,
  L = -(2/pi) sum_j Z_j w_j + (8 cosh(1/2)/pi) p.

With rho=16001/N and n>=N, the remainder obeys

  |r_n-L/n| <= B/n^2 + C/n^3,

where

  B = (16/pi)/(1-rho^2) * sum_j |j w_j|,

  C = (2/pi)/(1-rho^2) * sum_j |j^2 Z_j w_j|
      + (8 cosh(1/2)/pi^3)|p|.

The Z-envelope used here follows from

  Z_n = 2 A_n + Im psi(1/4+i n pi/4)
        + n pi sum_{k>=0} e^{-2a_k}/(a_k^2+(n pi/2)^2),

  |A_n| <= sum_q Lambda(q)/sqrt(q) = 2.9262341821...,

and, for y=n pi/4,

  0 < Im psi(1/4+i y)
    = sum_{k>=0} y/((k+1/4)^2+y^2)
    <= 1/y + pi/2.

Thus |Z_n|<8 is extremely loose but valid for the far-tail range used below.

Using the actual full-cutoff numerical six-plane coefficients, the resulting
Frobenius/operator upper diagnostic beyond N=128001 is

    Delta_far < 0.00866328.

Combining this with the directly accumulated numerical Gram through 127999
suggests

    delta_crit(full tail) <~ 0.05762,

well below 0.18212727, leaving a factor >3.1.

IMPORTANT STATUS
----------------
The 7991-mode solve and finite-band Gram accumulation in this file are
ordinary floating-point diagnostics.  The signed far-tail inequality is exact
structurally, but its displayed coefficient bound currently uses midpoint
six-plane/solve data.  Therefore 0.05762 is NOT yet a validated enclosure and
must not be promoted to a global inertia theorem.

Next certification step: outward-enclose the finite six-plane matrix and the
residual Gram through 127999, then interval-enclose the signed moments L,B,C.
The margin is large enough that this should not require delicate precision.

No exact-zero, RH, GRH, or lambda_1=0 claim follows.
"""

FINITE_SCHUR = [
    -1.27428815e-13,
    -1.26376777e-13,
    -1.25858716e-13,
     1.20541576e-12,
     3.825902051894257e-8,
     2.14472468e-4,
     7.69095194e-1,
     1.70185089,
     2.01522883,
     2.34737759,
]

DELTA = 4.6732 - 0.994**2/0.22
CUMULATIVE = {
    31983: 0.0274827713,
    63999: 0.0417039023,
    127999: 0.0489482115,
    255999: 0.0526099107,
    511999: 0.0544513194,
    1023999: 0.0553747546,
}
FAR_FROM_128001 = 0.00866327475

if __name__ == '__main__':
    print('lambda5(S_F) =', FINITE_SCHUR[4])
    print('lambda6(S_F) =', FINITE_SCHUR[5])
    print('effective-tail delta >=', DELTA)
    for stop, val in CUMULATIVE.items():
        print('cumulative through', stop, '=', val)
    print('midpoint-coefficient far-tail bound from 128001 <', FAR_FROM_128001)
    print('diagnostic total <', CUMULATIVE[127999] + FAR_FROM_128001)
    print('guardrail: diagnostic only; finite/moment interval enclosure remains open')
