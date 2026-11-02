# Cone Derivation Ledger v15.305 — Lane A: persistent high-tail coupling and boundary leakage

**Date:** 2026-11-02. **Track:** Lane A, frozen K_full in chosen counting-measure ell2. **Parents:** v15.106, v15.129, v15.139, v15.227, v15.303–304. **Status:** [D] asymptotic nonvanishing of high-tail operator norm; [D] nonvanishing of cross-boundary coupling along a subsequence; [O] quantitative inexpensive full-K transfer.

## Ledger collision check

Live master HEAD immediately before preparation: cfb5a0410a45131587a81e2b9a9382c78c5d0b4e (v15.304). No Sandbox return used. Additive only.

## Gate 1. The tail norm cannot be made small by moving the cutoff

Let P_N contain the physical parity modes through index N, Q_N=I-P_N, and B=K-D. Let c=2/pi and, for distinct parity modes, B_(n+2,n)=c/4*(z_(n+2)-z_n)+O(1/n), as derived in v15.139. The pole coupling is O(n^-2). Within either fixed parity class the exact source physical signal has

z_n=pi/2+sum_(q in {2,3,4,5,7})2w_q sin(theta_q n)+O(1/n),
theta_q=pi log(q)/2,
w_2=log(2)/sqrt(2), w_3=log(3)/sqrt(3), w_4=log(2)/2, w_5=log(5)/sqrt(5), w_7=log(7)/sqrt(7).

Let Delta_n=z_(n+2)-z_n. Along either parity n=b+2j, the Cesaro mean satisfies the exact identity

lim_(J->infty) (1/J) sum_(j=0)^(J-1) |Delta_(b+2j)|²
=8 sum_q w_q² sin²(theta_q)=:A>0.

Pairwise frequency nonresonance modulo the parity-lattice period follows because collisions would give log(q/r) or log(qr) an even integer (and the self-frequency condition similarly forces an impossible integer exponential identity). Each sine factor is nonzero. Thus limsup_(n->infty, fixed parity)|Delta_n|>=sqrt(A).

For any fixed N, sufficiently large n and n+2 both belong to Ran(Q_N), and
||Q_N B Q_N||>=|<e_(n+2),B e_n>|.
Therefore

**inf_N ||Q_N B Q_N|| >= (|c|/4)*sqrt(A)>0**,

where the inf is over admissible prefix cutoffs N. More explicitly liminf_(N->infty) ||Q_N B Q_N|| >= (|c|/4)*sqrt(A). Since the choice of arbitrarily large near-diagonal n is available for every N, the same bound holds for each N.

This does not exclude a sharper *constant* M_N much less than global M=15; it rules out M_N->0 purely by raising N. Nor does it claim the high-tail spectral edge remains low: physical d_n~log(n/4) still grows and ultimately dominates any uniformly bounded B.

## Gate 2. Offblock norm need not decay along prefixes

Let N be the largest mode in P_N; N+2 lies in Q_N. Then
||Q_N B P_N|| >= |B_(N+2,N)|=|c|/4*|Delta_N|+O(1/N).

Since limsup |Delta_N|>=sqrt(A), it follows that

limsup_(N->infty)||Q_N B P_N|| >= (|c|/4)*sqrt(A)>0.

This obstruction applies specifically to *sharp coordinate prefixes*, not smooth localization, multi-block preconditioners or alternative nonlocal projections. A uniform positive lower bound for every N is not claimed.

## Gate 3. Implication for v15.304's stopping rule

The sufficient positive-tail inequality
log((N+2)/4)-C-b-M_N>0
cannot be made inexpensive merely by assuming M_N->0, since such decay is false. On the other hand, the scalar diagonal logarithm grows unboundedly and the tail will eventually be positive; that existence result is unchanged. To improve resource requirements without modifying the physical kernel, use one of:
(a) a rigorously smaller nonvanishing tail norm constant grounded in five-frequency structure;
(b) an energy-dependent operator/block comparison sharper than ||B||;
(c) an interval-certified resonant-mode block complemented by a coupled-tail resolvent bound.

Nothing in this entry certifies a full-K gap or demonstrates a practical cutoff. No canonical Suzuki source synthesis, no new seed, and no F1/F2 production or v14.406 replay. v14.405/v14.406 PASS and v14.814 far FAIL remain unchanged, as do C_S_32000, thresholds 3e-5/.002, and charge-once accounting.

**NEXT DIRECT GATE:** derive a rigorous numerical lower bound on A, and explore a smaller sharp analytic upper bound on Q_N B Q_N. No Sandbox handoff issued.
