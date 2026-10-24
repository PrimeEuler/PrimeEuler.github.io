# Cone Derivation Ledger v14.808 — Divisor-shell M-convex obstruction and quadratic causal cone

Date 2026-10-24. Gravity/combinatorics lane. Parents v13.770, v14.784, v14.807. Research note research-notes/Gravity_Divisor_Shell_MConvex_Causal_Cone_Test.md at commit b860bca07d6769f9b4b20be8f202bef3b589e022. Prewrite live HEAD b860bca07d6769f9b4b20be8f202bef3b589e022. Additive only, Suzuki/far-tail untouched.

## Fixed-product homogeneous polynomial [D]

Define \(F_N(X,Y,Z)=\sum_{ab=N}X^aY^bZ^{N+1-a-b}\). This is well-defined homogeneous degree N+1 since a+b≤ab+1=N+1. Its positive support has d(N) points.

For all N≥3, support contains (1,N,0) and (N,1,0). M-convex exchange from (1,N,0) toward (N,1,0) requires (2,N-1,0), which is absent since 2(N-1)=N iff N=2. Therefore F_N is NOT a Lorentzian polynomial in the standard homogeneous nonnegative-coefficient class for N≥3. F_1=XY and F_2=XY²+X²Y satisfy the Lorentzian criteria, by direct degree-two Hessian checks for F_2. This is an obstruction to this specified encoding, not to all possible divisor encodings.

## Quadratic hyperbolicity cone [D]

The factor quadratic \(Q(T,X)=T²-X²\) is hyperbolic with respect to (1,0): \(Q(v+t(1,0))\) has two real roots for all v. Its future cone \(T>|X|\) corresponds to x=T+X>0 and y=T-X>0. This is an exact 1+1 algebraic causal-cone model. The polynomial's Hessian lives in algebraic variables and is NOT automatically a GR spacetime metric, and there is no connection/curvature/source equation or G determined.

## Next gate [O]

Seek a modified factor-shell polynomial with preserved divisor-contact bookkeeping and M-convex support, or prove a wider no-go under natural support-preservation conditions; separately test a covariant physical metric embedding.

Flags: F_N_support_non_Mconvex_for_N>=3=EXACT; Q_future_hyperbolicity_cone=EXACT; GR_physical_map=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: combinatorial-gravity-proof-check
parent: v14.808
status: open
action: Verify the universal M-convex exchange obstruction for N>=3, F_1/F_2 corner cases, and distinction between polynomial hyperbolicity cone and physical spacetime dynamics.
deliverable: scoped independent verdict without Suzuki/far-tail changes.
