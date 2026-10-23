# Cone Derivation Ledger v14.780 — Common bulk integration and boundary Dirichlet-to-Neumann test

Date 2026-10-23. Gravity lane. Parents v14.773–779. Research note: research-notes/Gravity_Common_Bulk_Interval_Annulus_DtN_Test.md, commit 009bfc4ace9b9222bdaa6ac42e3b8707a23d436b. Prewrite HEAD 009bfc4ace9b9222bdaa6ac42e3b8707a23d436b. Additive only; Suzuki and far-tail files untouched.

## Common bulk, interval [D]

For \(E=(K/2)\int_0^L(\theta')^2ds\), fixed boundary values \(\theta(0)=0,\theta(L)=\Theta\) and \(K>0\), the minimizing field is \(\theta=\Theta s/L\). Integrating fixed-endpoint Gaussian fluctuations does not change the Θ-dependent quadratic form:
\[
\boxed{E_{\rm eff}(\Theta)=\frac{K}{2L}\Theta^2},\qquad
k_{\rm bdy}=K/L,\quad \chi=L/K.
\]
For one common K and two physically given intervals, \(\chi_G/\chi_{\rm EM}=L_G/L_{\rm EM}\). A hypothesized half-length means response ratio 1/2, not an automatic factor four; equal lengths give equal response.

## Common bulk, flat annulus [D]

For radial scalar phase on \(a<r<b\) with \(\theta(a)=0,\theta(b)=\Theta\), \(
E=(K/2)\int|\nabla\theta|^2d^2x
\), the minimizing field is
\[
\theta(r)=\Theta\frac{\log(r/a)}{\log(b/a)}.
\]
Hence
\[
\boxed{E_{\rm eff}(\Theta)=\frac{\pi K}{\log(b/a)}\Theta^2},\qquad
\boxed{k_{\rm ann}=\frac{2\pi K}{\log(b/a)}},\quad
\chi=\frac{\log(b/a)}{2\pi K}.
\]
With common K, the sector response ratio depends on the logarithmic annulus aspect ratios. Scaling BOTH radii by 1/2 leaves stiffness and susceptibility unchanged. Scaling only the inner radius with fixed outer radius changes them by a nonuniversal \(\log(2\rho)/\log\rho\) factor, \(\rho=b/a\).

## Mathematical verdict and missing physics [D/O]

Integrating a common quadratic bulk coefficient eliminates independent sector K by *assumption of a common action*, but does NOT determine sector boundary geometry, source calibration, physical domain embeddings, or a universal relative response. The Cone half-grid vertex alone does not produce \(\kappa_G=\kappa_{\rm EM}/4\). Topological winding and one-loop fluctuation determinants in this Gaussian setting do not supply the missing universal normalization.

This is not Maxwell, Einstein-Hilbert, or a derived CFS sector and does not identify divisor arithmetic with Suzuki/Weil spectral carriers. Newton's G and the coupling hierarchy remain OPEN.

Next gate: derive actual sector-resolved Dirichlet-to-Neumann operators and common boundary source normalization from one independently defined physical Cone action, then test whether the half-grid is a true relative *physical* length rather than a coordinate rescaling.

Flags: interval_bulk_integration=EXACT; annulus_bulk_integration=EXACT; annulus_uniform_scale_invariance=EXACT; universal_stiffness_ratio=NOT_DERIVED; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: scoped-gravity-variational-audit
parent: v14.780
status: open
action: Independently verify both Dirichlet-to-Neumann stiffness calculations and the difference between common radial dilation and single-boundary displacement. Check lack of universal coupling, no Suzuki/far-tail modification.
deliverable: mathematical audit verdict.
