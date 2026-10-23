# Gravity radial-shift observable test (after v14.769)

Date: 2026-10-23 EDT. Lane: independent gravity. Parents: v13.301, v13.770, v14.760–762, v14.768–769. Suzuki certified computation reserved. [D] = exact conditional statement; [O] = physical input missing.

## Shared-coordinate radial shift [D]

With the common index n and independently agreed radial reference:
\[
r_{\mathrm{EM}}(n)=\log n,\qquad
r_{\mathrm{G}}(n)=\log(n/4)
=r_{\mathrm{EM}}(n)-\log4.
\]
For a same-index finite dimensional comparison, define diagonal matrices
\[
L_{\mathrm{EM}}=\operatorname{diag}(\log n_j),\qquad
L_{\mathrm{G}}=\operatorname{diag}(\log(n_j/4)),
\]
hence
\[
\boxed{L_{\mathrm{G}}=L_{\mathrm{EM}}-(\log4)I}.
\]

## No-go for shift-invariant spectral data [D, conditional]

If the *same* finite Hermitian interaction K is used in both sectors, \(H_{\mathrm{EM}}=L_{\mathrm{EM}}+K\), \(H_{\mathrm{G}}=L_{\mathrm{G}}+K\), then
\[
H_{\mathrm{G}}=H_{\mathrm{EM}}-(\log4)I,
\quad
\lambda_j(H_{\mathrm{G}})=\lambda_j(H_{\mathrm{EM}})-\log4.
\]
Consequently all eigenvalue differences, their degeneracies, and any function exclusively of spectral gaps are identical. Off-diagonal transition matrix elements between common normalized eigenvectors are identical for a fixed common observable. No gap-based experiment alone can determine a coupling asymmetry from the constant shift.

This does *not* claim the real EM and gravitational operators share K, domain, Hilbert-space realization, physical units, or boundary conditions. Those are indispensable dynamical hypotheses.

## What does change, but does not automatically fix G [D/O]

The trace and suitably finite spectral functions do detect a fixed energy/radial origin:
\[
\operatorname{tr}H_{\mathrm{G}}
=\operatorname{tr}H_{\mathrm{EM}}-N\log4.
\]
For finite N and real t,
\[
\boxed{\operatorname{tr}(e^{-tH_{\mathrm{G}}})
=4^t\operatorname{tr}(e^{-tH_{\mathrm{EM}}})}.
\]
But normalized Gibbs probabilities and thermal expectation values of fixed observables are unchanged, because the common factor \(4^t\) cancels in the partition-function ratio. Absolute free energies shift by the chosen origin, and the shift is not measurable without a shared energy standard or boundary.

Likewise a homogeneous radial functional \(A_p(r)=C e^{pr}\), with a **common externally fixed** C and p, gives
\[
A_p(r_{\mathrm{G}})/A_p(r_{\mathrm{EM}})=4^{-p}.
\]
This ratio is a mathematical scaling identity, not a prediction of electromagnetic or gravitational couplings, because p, C, the action's physical meaning and sector matching remain unspecified.

## Comparison with prior physical-selector no-go [D/O]

v14.760 exhibits a tunable conditional minimum \(U(\psi)=q_n^2(ae^{2\psi}+be^{-2\psi})\). v14.761 shows classical Maxwell and Einstein–Hilbert normalizations cannot provide a,b non-circularly merely by copying coefficients from the actions. A fixed radial shift of \(-\log4\) adds no missing independent Hessian/field normalization, cannot by itself fix the very large hierarchy, and cannot replace the physical inputs in the CFS proposal.

## Gate decision / next falsifiable contract [O]

Supply a single admissible, sector-resolved physical response observable \(\mathcal O\), with an explicit common unit and boundary, and derive
\[
\mathcal O_{\mathrm{G}}[r-\log4,\beta]/
\mathcal O_{\mathrm{EM}}[r,\beta]
\]
directly from its action, with no measured coupling inserted as a coefficient. Test whether it is invariant under independent shifts of zero points and changes of regulator. If it is invariant, the radial bridge is a coordinate match only. If non-invariant and physically normalized, evaluate it and compare with independent data.

No G, alpha or hierarchy derived. No Suzuki far-tail / certificate / code touched.
