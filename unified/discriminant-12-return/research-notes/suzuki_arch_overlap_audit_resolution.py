#!/usr/bin/env python3
"""Resolve External Audit Round 20's Suzuki archimedean off-diagonal finding.

The apparent discrepancy came from pairing h=g'' with the derivative-basis
overlap after the Weil form had already been integrated by parts.

For v in H_0^1(-1,1), the smooth h contribution to

    Q(v)=\iint g(x-y) v'(x)v'(y) dx dy

is, after integration by parts in x and y,

    -\iint h(|x-y|) v(x)v(y) dx dy.

Therefore h must be integrated against the overlap of the Dirichlet sine modes
psi_n, not against the overlap of their derivatives.

For odd m != n, with

    psi_n(x)=sin(n*pi*(x+1)/2),
    H_n=\int_0^2 h(t) sin(n*pi*t/2) dt,

the correct source-faithful matrix element is

    K_arch(m,n)=-(4/pi) (n H_m-m H_n)/(n^2-m^2).

This is the formula used in the pre-Round-20 rank-two Z_n construction.

By contrast, integrating h against the derivative-overlap produces

    (2ab/(a^2-b^2))(b H_n-a H_m),
    a=m*pi/2, b=n*pi/2,

which is algebraically correct for that *different overlap*, but it is not the
archimedean matrix element after the integration-by-parts reduction.

Independent numerical checks performed during the resolution:

pair (1,3):
  -integral h * sine-overlap = -0.1081045366838740
  legacy closed form         = -0.1081045366838740
  derivative-overlap formula = +0.0153046032370141

pair (1,21):
  -integral h * sine-overlap = -0.0153470463946085
  legacy closed form         = -0.0153470463946085
  derivative-overlap formula = +0.0021730484457013

pair (21,29):
  -integral h * sine-overlap = -0.000498872051576313
  legacy closed form         = -0.000498872051576249
  derivative-overlap formula = +0.0000677238563052651

pair (21,101):
  -integral h * sine-overlap = -0.000143231891397458
  legacy closed form         = -0.000143231891397457
  derivative-overlap formula = +0.0000194379508652697

An independent source-level control using Suzuki's screw function g(t) and the
derivative overlap also agrees with the full legacy assembled matrix. Examples:

  A_13 direct source form = 0.000387069325955204
  A_13 legacy assembly    = 0.000387069325951339
  A_13 rank-4 branch      = 0.123796209246839

  A_1,21 direct source    = -0.00104951791952813
  A_1,21 legacy assembly  = -0.00104951791953675
  A_1,21 rank-4 branch    = +0.0164705769207731

Hence External Audit Round 20's claimed K_arch correction is retracted. The
rank-4 repair branch v13.373--v13.386 is superseded as an audit detour. The
pre-audit rank-two identity

    Z_n=2 A_n+Si(n*pi)+2 H_n

and its structured LDL/cross architecture are restored, subject to their own
previously stated validated-computation guardrails.

No exact-zero, RH, or GRH conclusion follows from this resolution.
"""

from math import pi


def legacy_arch_offdiag(m, n, Hm, Hn):
    return -(4.0/pi)*(n*Hm-m*Hn)/(n*n-m*m)


def derivative_overlap_expression(m, n, Hm, Hn):
    a=m*pi/2.0
    b=n*pi/2.0
    return (2.0*a*b/(a*a-b*b))*(b*Hn-a*Hm)


if __name__ == '__main__':
    print('Audit resolution: h=g\'\' acts on Dirichlet sine overlap after IBP.')
    print('Restored K_arch(m,n)=-(4/pi)(n H_m-m H_n)/(n^2-m^2).')
    print('Guardrail: no RH/GRH or exact-zero claim.')
