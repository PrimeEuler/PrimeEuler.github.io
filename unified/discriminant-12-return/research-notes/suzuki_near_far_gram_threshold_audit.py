#!/usr/bin/env python3
"""Near/far Gram threshold audit for global high-complement positivity.

For a main split at N=6003, write the cross block from finite high modes
21..6001 into the tail as

    G = [G_near  G_far],

with near columns 6003..16003 and far columns >=16005.

Because the column sets are disjoint,

    G G^T = G_near G_near^T + G_far G_far^T,

hence

    ||G||^2 <= ||G_near||^2 + ||G_far||^2.

Current midpoint targeting values:

    ||G_near|| ~= 0.883639329283,
    ||G_far||  ~= 0.45807,

where the far value comes from the combined pole-free Cauchy low-rank
factorization of v13.349.

This gives the coarse Gram upper target

    ||G|| <= sqrt(0.883639329283^2 + 0.45807^2)
          ~= 0.9953123.

The finite high-block minimum at 21..6001 is about

    gamma_F ~= 0.227336299782,

and the robust analytic tail gap at N=6003 is

    alpha_T ~= 3.6926350482594.

A sufficient Schur condition is

    ||G|| < sqrt(gamma_F * alpha_T) ~= 0.916226.

Therefore the N=6003 split does NOT close under this coarse near/far norm
combination.  This is a useful negative result: it prevents us from claiming
that the low-rank remote factorization alone finishes the high-complement proof.

At N~10003 the analytic tail gap is ~4.2034; if the finite high-block gap stays
near 0.227, the allowable cross norm rises to about 0.977.  This is much closer
to the observed moving-interface coupling, so N~10003 remains the preferred
working split.

The next certificate should therefore combine:
  * a finite high block through 10001;
  * a finite near-tail cross block;
  * a separated far block via the v13.349 Cauchy factorization;
  * Gram-level combination rather than triangle inequality.

No full high-complement positivity or RH/GRH conclusion is made here.
"""

NEAR=0.883639329283
FAR=0.45807
FINITE_GAP=0.227336299782
TAIL_GAP=3.6926350482594

if __name__=='__main__':
    import math
    combined=math.sqrt(NEAR*NEAR+FAR*FAR)
    threshold=math.sqrt(FINITE_GAP*TAIL_GAP)
    penalty=combined*combined/TAIL_GAP
    print('coarse combined cross =',combined)
    print('required threshold =',threshold)
    print('Schur penalty =',penalty)
    print('remaining margin =',FINITE_GAP-penalty)
    print('guardrail: N=6003 does not close under this coarse bound')
