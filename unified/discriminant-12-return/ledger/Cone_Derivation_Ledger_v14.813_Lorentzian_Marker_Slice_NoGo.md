# Cone Derivation Ledger v14.813 — No-go for a Lorentzian exact divisor-frontier marker slice

Date 2026-10-24. Parents v14.811–812. Research note research-notes/Augmented_Lorentzian_Divisor_Marker_Extraction_NoGo.md commit d1c27199bb31902b7087fa1869d588dc6c099c20. Gravity/combinatorics; additive only; Suzuki/far-tail untouched.

Suppose homogeneous Lorentzian F(X,Y,Z,T), with nonnegative coefficients, had \([T^k]F=c C_N(X,Y,Z)\), c>0, where \(C_N=\sum_{ab\le N}X^aY^bZ^{N+1-a-b}\). Partial differentiation preserves Lorentzian polynomials, and specializing T=0 preserves them when nonzero. Therefore \(k![T^k]F=(\partial_T^kF)|_{T=0}\) must be Lorentzian. Yet v14.811 proves C_N has non-M-convex support for every N>=3. Contradiction. The same closure argument applies to any sequence of auxiliary-variable partial derivatives and zero specializations producing exactly C_N.

Thus no direct **positive Lorentzian coefficient-slice extension** of the exact cumulative divisor frontier exists for N>=3. Arbitrary masked coefficient functionals like v14.812 can recover D(N), but they do not preserve the Lorentzian property.

NEXT: seek an intrinsic scalar correlation or response of Lorentzian completions with arithmetic masks, rather than an impossible exact Lorentzian frontier slice. No claim of GR dynamics or Newton G.

HANDOFF
target: external-audit
type: combinatorics-closure-check
parent: v14.813
status: open
action: Verify Lorentzian closure under partial differentiation and variable-zero specialization, and confirm contradiction for all N>=3; check v14.812 encoder arithmetic.
deliverable: scoped independent verdict, no Suzuki/far-tail changes.