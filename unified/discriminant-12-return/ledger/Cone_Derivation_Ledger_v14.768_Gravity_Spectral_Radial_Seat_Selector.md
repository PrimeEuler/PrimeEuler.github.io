# Cone Derivation Ledger v14.768 — Suzuki spectral denominator and half-grid Cone radial seat

**Date:** 2026-10-23 EDT. **Lane:** gravity radial-scale selector. **Parents:** v13.177, v13.301, v13.748, v13.770, v14.367, v14.550, v14.766–767. **Research note:** \`research-notes/Gravity_Spectral_Diagonal_Radial_Seat_Bridge.md\` (original commit \`60a8b298\`). **Audit correction:** v14.769 independently verified the mathematics but identified LaTeX backslashes stripped by the original publication; this is a formatting-only reconstruction, with the same scope and claims. Neither Suzuki payloads nor far-tail files modified.

## Radial versus boost coordinates [D]

The Cone coordinates are
\[
r=\log(xy),\qquad \beta=\frac12\log\frac{x}{y}.
\]
On a uniform factor grid \(x=ha,y=hb\) with \(ab=n\),
\[
\boxed{r_h(n)=\log(h^2n)},\qquad X_{\rm vertex}=\pm\frac h2.
\]
A common dilation shifts \(r\) but preserves \(\beta\). Thus \(h_{\rm EM}=1\) gives \(r_{\rm EM}(n)=\log n\) and vertices \(\pm1/2\), while \(h_{\rm G}=1/2\) gives
\[
\boxed{r_{\rm G}(n)=\log(n/4)},\qquad \boxed{X_{\rm vertex}=\pm1/4}.
\]

## Old pair hyperbola and independently established spectral diagonal [D]

For \(\psi_{n,k}=\frac12\log(n/k)\) and \(c=h^{-2}\),
\[
\boxed{r_h(n)=2\psi_{n,h^{-2}}}.
\]
Consequently \(r_{\rm G}(n)=2\psi_{n,4}=\log(n/4)\). This is a *radial scale comparison*, not the intrinsic boost of the common-rescaled pair \((hn,h)\).

The established Suzuki cusp diagonal from v13.301 is
\[
C_{nn}=\log(n/4)-\operatorname{Ci}(n\pi)-\frac{\operatorname{Si}(n\pi)}{n\pi}.
\]
Its reference diagonal is
\[
\boxed{(D_{\log})_{nn}=\log(n/4)=r_{1/2}(n)=2\psi_{n,4}}.
\]

## Spectral-denominator / vertex-seat theorem [D]

If \(\Lambda_c(n)=\log(n/c)\) equals \(r_h(n)=\log(h^2n)\) for all \(n>0\), then uniquely
\[
\boxed{h=c^{-1/2}},\qquad \boxed{X_{\rm vertex}=\pm\frac1{2\sqrt c}}.
\]
At \(c=4\), this gives \(h=1/2\) and vertices \(\pm1/4\), *conditional on the shared normalization of the spectral and factor-shell indices*.

## Normalized power-map cocycle [D]

The unit-preserving power map of v14.767 sends \(n\mapsto n^k\). The radial coordinate obeys
\[
\boxed{r_h(n^k)=k r_h(n)+(k-1)\log(h^{-2})}.
\]
For EM (\(h=1\)) the affine term vanishes. For \(h=1/2\),
\[
\boxed{r_{\rm G}(n^k)=k r_{\rm G}(n)+(k-1)\log4}.
\]
Equivalently \(\Lambda(n^k)=k\Lambda(n)+(k-1)\log4\), for \(\Lambda(n)=\log(n/4)\).

## Radial cutoff and global factor counts [D]

For a fixed radial cutoff \(r_h(ab)\le L\),
\[
ab\le h^{-2}e^L,\qquad
\boxed{D_h(L)=D(\lfloor h^{-2}e^L\rfloor)}.
\]
Thus
\[
D_{\rm EM}(L)=D(\lfloor e^L\rfloor),\qquad
\boxed{D_{\rm G}(L)=D(\lfloor4e^L\rfloor)}.
\]
The factor-four count is mathematically exact, but the *physical* identification of this spectral normalization with a gravitational sector remains conditional.

## Outcome and boundaries

The old EM-to-G scale hyperbola matches the half-grid radial seat exactly **as a coordinate identity**. The same \(4\) occurs in the independently established Suzuki logarithmic diagonal. This does not identify divisor arithmetic with the Suzuki/Weil current: the v13.770 carrier mismatch remains controlling. It does not derive \(G\), \(\alpha_G\), or the physical coupling hierarchy.

**Next gate:** compare independently normalized action/spectral boundary observables at \(r_{\rm EM}=\log n\) and \(r_{\rm G}=\log(n/4)\), at the same boost \(\beta\). Identify what detects an absolute radial shift and what is invariant.

**Flags:** \`radial_boost_separation=EXACT\`; \`spectral_diagonal_matching=COORDINATE_IDENTITY\`; \`physical_sector_identification=OPEN\`; \`G_derived=false\`; \`Suzuki_payloads_touched=false\`; \`far_tail_touched=false\`.
