# Hbar unit-circle test for the gravity common-length selector

2026-10-23, gravity-only. Parents v14.620, v14.622, v14.773, and unit-circle pair-encoding notes. [D] exact algebra or dimensional statement; [O] requires independent physics.

## Phase is an action scale [D]

The geometric unit-circle point
\[
z_{n,k}=\frac{n-k+2i\sqrt{nk}}{n+k}
=\frac{\sqrt n+i\sqrt k}{\sqrt n-i\sqrt k}
\]
has modulus one and depends only on n/k. The equality
\[
z_{\lambda n,\lambda k}=z_{n,k}\quad(\lambda>0)
\]
shows that the unit circle cannot tell an absolute common scale from the pair direction. Likewise its integer AM–GM identities \((j+\tfrac12)^2-\tfrac14=j(j+1)\) fix dimensionless offsets, not a metric length.

For physical action S, quantum phase \(e^{iS/\hbar}\) is invariant under \(S\mapsto S+2\pi m\hbar\), not \(S\mapsto S+m\hbar\). One full winding gives \(h_{\rm Planck}=2\pi\hbar\), while \(\hbar\) is action per radian. This matches the interpretation of v14.620 but does not yield an absolute distance.

## Additional physical datum: a momentum or mass [D/O]

For a particle on a circular loop of proper circumference \(2\pi R\) and constant tangent mechanical momentum magnitude p, assume the canonical phase/action integral is \(S_{\rm loop}=\oint p\,ds=2\pi pR\), with no additional gauge holonomy or spin-connection term. Single-valuedness \(S_{\rm loop}/\hbar=2\pi m\) yields
\[
\boxed{pR=m\hbar,\qquad R_m=m\hbar/p}.
\]
The loop radius is fixed *conditionally* once a physical p is measured or dynamically selected. If p is independently set to \(\mu c\) as a model choice, \(R_m=m\hbar/(\mu c)\), a reduced-Compton-length ladder. This is not a universal gravitational length; setting p=μc is an extra assumption, not a general relativistic mass-shell consequence. In a real gauge background, the gauge-invariant loop quantization includes field holonomy and may shift m by an offset. Spin structure and boundary conditions can also give half-integer terms; the geometric quarter vertex does not itself require a quarter phase shift.

For a fixed measured p, the half-grid h=1/2 could be assigned radial loop radii \(R_m^{G}=m\hbar/(2p)\) while EM uses \(R_m^{EM}=m\hbar/p\), but that assignment is merely a postulate of different winding-to-radius maps, not forced by phase quantization. Both sectors may instead take the same quantum \(pR=m\hbar\). The common action quantum forbids neither choice.

## Dimensional identifiability [D]

The action dimension of ħ is M L² T⁻¹. Even with c of dimension L T⁻¹, ħ and c alone cannot produce a length by dimensional analysis. Introducing mass μ gives \(\ell_\mu=\hbar/(\mu c)\); introducing momentum p gives \(\ell_p=\hbar/p\). Selecting one common scale therefore needs an independently defined physical mass/momentum/spectral gap or boundary and a common dynamical relation to both sectors. Using \(\ell_{\rm P}=\sqrt{\hbar G/c^3}\) would presuppose G and is circular if the goal is to derive it.

## Key structural result [D/O]

The unit circle provides a common **action calibration** and discrete winding rule, a stronger constraint than arbitrary separate length labels. However it leaves a common scale freedom \((R,p)\mapsto(\lambda R,p/\lambda)\) at fixed pR/ħ. Likewise the radial shell gap is not fixed without an independently derived map from the action phase to the physical EM and G pair-grid spacings. A sector-linking dynamical boundary condition involving the same μ or p could break the free calibration, but no such condition has yet been derived.

**Next test:** derive the complete gauge-invariant loop phase \(\oint(p_{\rm mechanical}ds+qA)\) (and gravitational holonomy, if present) from a concrete common action and compare sector winding spectra. Avoid double-counting phases and distinguish an actual quarter offset from a vertex-coordinate quarter.

No G or physical coupling derived; no Suzuki, far residual or production modifications.
