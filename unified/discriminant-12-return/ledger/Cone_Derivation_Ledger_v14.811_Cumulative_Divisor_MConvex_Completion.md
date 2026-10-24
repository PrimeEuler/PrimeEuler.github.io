# Cone Derivation Ledger v14.811 — Cumulative divisor-frontier obstruction and Lorentzian support completion

Date: 2026-10-24. Gravity/combinatorics lane. Parents v14.807–810. Research note research-notes/Cumulative_Divisor_Frontier_MConvex_Completion.md at 497ac3e65c8bd97a99a888c06e5caab1c7474da9. Prewrite live HEAD 497ac3e65c8bd97a99a888c06e5caab1c7474da9. Additive only; Suzuki and far-tail untouched.

## Exact cumulative-support no-go [D]
\[
C_N(X,Y,Z)=\sum_{ab\le N,\ a,b\ge1}X^aY^bZ^{N+1-a-b}
\]
is a well-defined homogeneous polynomial with \(C_N(1,1,1)=D(N)\). For every N>=3, support contains (1,N,0) and (N,1,0); M-convex exchange would require (2,N-1,0), absent because 2(N-1)>N. Thus C_N is not Lorentzian for every N>=3. The failure remains for all uniform homogenizing degrees M>=N+1. C_1=XY and C_2=XY(X+Y+Z) are Lorentzian.

## Constructive full-support completion [D]
The translated simplex support a,b>=1 and a+b<=N+1 is M-convex. The polynomial
\[
P_N=XY(X+Y+Z)^{N-1}
\]
has that support and is Lorentzian via closure under products of homogeneous real-stable positive linear forms. It is NOT the original divisor polynomial, and its multinomial coefficients do not recover D(N) by simply setting all variables to one.

Exact divisor contacts can be identified by the *separate external mask* \(m_N(a,b)=1_{ab\le N}\); \(D(N)=\sum_{a+b\le N+1,\ a,b\ge1}m_N(a,b)\). No Lorentzian polynomial with exactly the cumulative product-frontier support exists for N>=3, regardless of positive weights. A marked or augmented-variable representation is a new, open problem.

## Boundary to gravity [O]
M-convex support is a combinatorial property, not physical Lorentzian spacetime dynamics. This gate supplies no physical metric, Einstein equations, G or sector coupling law. v13.770 Weil/Suzuki arithmetic-carrier distinction remains active.

Next gate: test augmented marker variables and whether coefficient extraction preserving D(N) is compatible with a Lorentzian ambient polynomial, without asserting the extracted polynomial remains Lorentzian.

Flags: cumulative_support_Mconvex_no_go_N>=3=EXACT; completion_simplex_Lorentzian=EXACT; exact_support_Lorentzian_impossible_N>=3=EXACT; marked_completion=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: combinatorics-gravity-support-audit
parent: v14.811
status: open
action: Verify cumulative M-convex exchange obstruction for all N>=3, the N=2 edge case, and the real-stable product proof for P_N; check that the contact mask is external and is not improperly claimed as intrinsic Lorentzian coefficient data.
deliverable: scoped audit verdict; no Suzuki/far-tail modifications.
