#!/usr/bin/env python3
"""Precision budget for rational-only certificate primitives.

This file records deliberately over-resolved truncation choices.  The finite
matrix only needs scalar entry control around 1e-11, while these primitives are
designed to land many orders smaller.

Recommended proof settings:

  pi via Machin:
      atan(1/5): 24 alternating terms
      atan(1/239): 8 alternating terms

  logs via atanh series:
      32 terms after power-of-two scaling, |z|<=1/3

  Euler gamma:
      Euler-Maclaurin at N=64 with Bernoulli terms through at least B_12

  small Si/Ci modes n=1,3,5,7:
      50 terms of the entire series

  large Si/Ci modes n>=9:
      Laplace asymptotic expansion truncated near its least term with the exact
      first-omitted integral remainder.

Representative scales (ordinary decimal diagnostics, not certificate values):
  n=9 asymptotic Si/Ci remainder ~2.6e-13 at optimal modest truncation;
  n=11 ~4.3e-16;
  n=7 convergent 50-term remainder <4e-27;
  n=5 convergent 40-term remainder <2e-26.

Hence a uniform 1e-11 cusp-scalar enclosure is available with substantial
slack.  Prime base constants can be targeted at 1e-24 or better, so multiplying
angles by n<=153 still leaves harmonic uncertainty far below 1e-20.
"""

PI_ATAN5_TERMS=24
PI_ATAN239_TERMS=8
LOG_TERMS=32
GAMMA_N=64
SMALL_SICI_TERMS=50
UNIFORM_CUSP_SCALAR_TARGET=1e-11
PRIME_BASE_TARGET=1e-24

if __name__=='__main__':
    print('rational primitive precision budget loaded')
