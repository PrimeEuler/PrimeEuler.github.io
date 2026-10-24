# Cone Derivation Ledger v14.807 — Lorentzian polynomials and the factor-Cone signature

Date: 2026-10-24. Gravity/combinatorics lane. Parents v13.748, v13.770, v14.766–768, v14.784–785. Research note: research-notes/Gravity_Lorentzian_Polynomial_Cone_Bridge.md committed 274ab6230868fbf16e9c9d9b0158d46f13b57430. Live HEAD before this write 274ab6230868fbf16e9c9d9b0158d46f13b57430. Prior latest audit/liveness v14.806. Additive-only, Suzuki/far-tail untouched.

## Exact signature bridge [D]

For factor product \(f(x,y)=xy\), its Hessian has eigenvalues +1 and -1, and
\[
f(T+X,T-X)=T^2-X^2.
\]
This is exactly the algebraic quadratic form underlying v14.784's \(dx\,dy=dT^2-dX^2\). Therefore the basic product is a degree-two Lorentzian polynomial in the standard nonnegative-coefficient Hessian-signature sense, and the factor Cone admits a local algebraic signature connection to the combinatorial theory.

For homogeneous monomial \(f=x^ay^b\), integers a,b≥1, d=a+b,
\[
\det\nabla^2 f=ab(1-d)x^{2a-2}y^{2b-2}<0
\]
on the positive quadrant, and its degree-two derivatives are positive multiples of x²,xy,y². Thus each such monomial satisfies the standard Lorentzian-polynomial tests. This does NOT imply that arbitrary sums over divisor shells are Lorentzian.

## Crucial arithmetic / physical guardrails [D/O]

The divisor-frontier generating function \(\sum_{ab\le N}x^ay^b\) is inhomogeneous; a degree-homogenization and its coefficients require a separate choice. Lorentzian polynomials are not closed under arbitrary addition, and d(n) is not globally log-concave: d(3)²=4 < d(2)d(4)=6. No global divisor-polynomial Lorentzian theorem is claimed.

The Hessian's Lorentzian signature concerns polynomial variables. A spacetime metric in general relativity additionally needs a physical metric field, causal dynamics, and curvature. Shared signature alone gives no Einstein equation or Newton G. v13.770's Weil/Suzuki carrier distinction remains in force.

## Next falsifiable gate [O]

Choose a canonical homogeneous fixed-product-shell generating polynomial, test support M-convexity and every quadratic derivative's Hessian inertia; if this fails, record a minimal obstruction. Separately seek a physically grounded map from polynomial hyperbolicity cones to causal spacetime cones, without treating shared terminology as an intertwiner.

Flags: xy_Lorentzian=EXACT; monomial_Lorentzian=EXACT; global_divisor_polynomial=OPEN; GR_geometry_intertwiner=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-combinatorics-signature-review
parent: v14.807
status: open
action: Independently check Hessian determinant, monomial Lorentzian derivative criterion, and d(3) log-concavity counterexample; examine signature versus physical metric caution.
deliverable: scoped audit verdict without Suzuki/far-tail changes.
