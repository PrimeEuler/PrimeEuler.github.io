# Cone Derivation Ledger v14.772 — Local boundary-response model and calibration obstruction

Date: 2026-10-23. Lane: gravity only. Parents: v13.770, v14.768–771. Research note: research-notes/Gravity_Common_Wall_Local_Response_Model.md, committed at 2cd420d26cb541a31f61e4179b30008c2bc33202. Prewrite master HEAD: 2cd420d26cb541a31f61e4179b30008c2bc33202. No Suzuki/far-tail payload modified.

## Explicit local detector [D]

For positive factor-pair shell ab=n at uniform spacing h, r_h(n)=log(h²n). With a fixed nonnegative compactly supported C¹ profile w normalized by integral w=1, define w_ε(t)=w(t/ε)/ε and
\[
\mathcal R_h(L,\varepsilon)=\sum_{n\ge1}d(n)w_\varepsilon(r_h(n)-L).
\]
The sum is finite for each wall L and positive width ε.

## Exact calibration covariance [D]

For h_EM=1 and h_G=1/2,
\[
\boxed{\mathcal R_{\rm G}(L,\varepsilon)
=\mathcal R_{\rm EM}(L+\log4,\varepsilon)}.
\]
If the two walls can be calibrated independently,
\[
\boxed{\mathcal R_{\rm G}(L-\log4,\varepsilon)
=\mathcal R_{\rm EM}(L,\varepsilon)}.
\]
A simultaneous passive shift of r and L changes nothing. Thus a measurable distinction requires an operationally common wall, not merely equal numerical values for L.

## Fixed-width large-wall theorem [D]

Write \(A_\varepsilon=\int e^t w_\varepsilon(t)dt>0\) and \(B_\varepsilon=\int t e^t w_\varepsilon(t)dt\). Using \(D(x)=x\log x+(2\gamma-1)x+O(\sqrt x)\) and Stieltjes partial summation:
\[
\mathcal R_h(L,\varepsilon)
=h^{-2}e^L[(L-2\log h+2\gamma)A_\varepsilon+B_\varepsilon]
+O_{h,\varepsilon,w}(e^{L/2}).
\]
Therefore for any fixed ε>0 and admissible profile w,
\[
\boxed{\lim_{L\to\infty}
\mathcal R_{\rm G}(L,\varepsilon)/
\mathcal R_{\rm EM}(L,\varepsilon)=4}.
\]
The result is profile-independent at leading order for fixed resolution, but makes no claim of uniformity when ε tends to zero. The fourfold ratio is normalized factor-pair density, *not* gravitational versus electromagnetic coupling.

## Physical closure contract [O]

Prove that both sectors share one invariant operational radial wall and that the measured physical states are actually described by these shell measures. Supply a gauge/diffeomorphism-invariant action response whose coefficient is independently normalized and not preloaded with Newton's G or alpha. Test wall, probe and regulator stability. The divisor count is not the Suzuki/Weil spectral current (v13.770).

Flags: local_response=DEFINED; exact_shift_covariance=PROVED; fixed_width_density_asymptotic=PROVED; physical_wall=OPEN; EM_G_physical_carriers=OPEN; G_derived=false; Suzuki_reserved=true.

HANDOFF
target: external-audit
type: gravity-only-derivation-check
parent: v14.772
status: open
action: Verify partial summation and the fixed-epsilon error term; check independent-wall cancellation and the nonuniform epsilon caveat; ensure no unsupported claim of physical G or Suzuki/Weil carrier equivalence.
deliverable: scoped audit verdict; do not modify Suzuki or far-tail files.
