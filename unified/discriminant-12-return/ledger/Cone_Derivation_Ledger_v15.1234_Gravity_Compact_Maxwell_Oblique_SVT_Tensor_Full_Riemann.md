# Cone Derivation Ledger v15.1234 — Oblique compact-Maxwell S/V/T stress and finite-time sourced K4 tensor-plus Fermi curvature

**Date:** 2026-11-19 Eastern. **Gravity/Cone lane.** **Status:** [D] real 3D Maxwell Cauchy evolution from the frozen v15.1078 compact source at an **oblique nonzero spatial Fourier wavevector**, scalar anisotropic stress and transverse vector momentum/tensor stress decomposed from the **same** Maxwell tensor, and finite-time physical-source tensor-plus response with the original K4 coasting tensor Euler equation; [D] numerical 32³/48³/64³ resolution and stress-conservation trends; [N] no independently derived quarter-grid gravity coupling, no full 3D constrained K4 metric and no gauge-complete finite optical detector; [O] vector and scalar sourced metric evolution at this oblique k, spatial zero mode/background, rest of 3D Fourier space and physical photon/mirror/emitter-clock readout. **Immediately prewrite live HEAD:** 94fa0ae67588361ea4fb7b6ed821dac9dbe60cb2. v15.1234 unique/collision checked. Strictly additive; untouched Lane A/Suzuki, Audit, Sandbox/Muse and archived v14.935 K4 payloads.

## Parent check, redundancy and collision correction
Gravity's previous finite-time **k=(0,0,1) scalar** result is in the historical file bearing v15.1229, committed as 6872dc8aca1f9544c31ff29a96ea951f1407f8b9, source 842f279fdbcd51a5c6652973958938ab4b48eae1. **External Audit Round 617, canonical v15.1230** (d1ef479c1de46dc1df654d0e4a59d424c33cb55e) independently executed that committed source across all 48³/64³/80³ grids and reproduced its numbers. It **also found a version-number collision**: Audit Round 616 owns v15.1229 by earlier commit time; Gravity's historical v15.1229 is substantively valid but numerically noncanonical. Preserve both immutable files; this v15.1234 uses the next free number after Audit v15.1232 and Lane A v15.1233, rather than attempting to rename past objects.

Physical precedent: v15.1078 specified the original compact, divergence-free Maxwell Cauchy source, v15.1081/1085 its Fourier stress and conservation jets; v15.750 demonstrated conventional S/V/T sourcing for a **different compact canonical scalar-matter packet**, and v15.787 derived the full electric Riemann including tensor curvature. This gate's addition is to apply the *same actual Maxwell 3D evolution* used in gravity's flagged v15.1229, now to **oblique K=(1,0,1) and its tensor-plus sourced metric**. The oblique scalar and transverse vector *metric modes* remain open, so the result is neither a completed full-SVT metric solution nor a physical optical signal.

## Gate 1181 — Maxwell packet source and nonparallel Fourier decomposition
Use flat conformal coordinates, spatial computational domain L_box=4pi per side, initial
**chi=f(x)f(y/2)f(z), E0=(∂y chi,−∂x chi,0), B0=0,**
where **f(u)=(1−u²)^3** on |u|<1 and zero elsewhere. This is the *original* v15.1078 compact 3D Maxwell Cauchy field. Its conformal-time Fourier evolution at each spatial wavevector q is **Ehat(q,xi)=cos(|q|xi) Ehat0(q)** and **Bhat(q,xi)=−i(q×Ehat0(q)) sin(|q|xi)/|q|**, with coasting conformal time xi=sqrt3 log tau.

At every time evaluate ordinary conformal Maxwell
**rho=(E²+B²)/2, S=E×B, Tij=rho δij−EiEj−BiBj**,
and extract Fourier coefficients at **K=(1,0,1)**, corresponding to FFT index (2,0,2) on L_box=4pi. Spatial mean FFT/N³ is the chosen normalization, with ±K pairing required for real fields. Let
**n=K/sqrt2=(1,0,1)/sqrt2, e=(1,0,−1)/sqrt2, b=(0,1,0)**.
The scalar spatial anisotropy, transverse vector momentum, and the two TT components are
**S_L=n_i Tij n_j−tr(T)/3**,
**V_1=e·S, V_2=b·S**,
**Pi_plus=[e_i Tij e_j−b_i Tij b_j]/2**,
**Pi_cross=e_i Tij b_j**.
These are standard 3D SVT projectors, not Cone-only operators. Maxwell tracelessness implies tr(T)=rho identically. This particular separable packet's y-reflection parity suppresses V_2 and Pi_cross throughout the sampled interval (numerical |Pi_cross| below ~6e-21 on the reported grids), but **V_1, S_L and Pi_plus are nonzero** after source evolution. At tau=1, B=0 and S=0, so both vector momentum polarizations vanish initially; the V_1 source is generated at positive time without an imposed pump.

Important numerical control: while the *analytic continuum* initial E is divergence-free, the compact C² bump sampled on a finite FFT grid does not have exact discrete q·Ehat=0 at every Nyquist/higher mode due to sampling/aliasing. The source reproducer checks the **selected nonparallel K bin** to tight relative tolerance and checks physical Maxwell stress conservation numerically. It does not falsely assert exact divergence closure at every discrete high-frequency bin. Periodic computational images cannot reach the source before tau=1.2 because the source supports |x|<1,|y|<2,|z|<1 and the maximum conformal travel is ~0.316, well within the half-box 2pi.

## Gate 1182 — finite-time stress projector results and conservation
Compute Maxwell at 17 source times tau=1..1.2, spatial grids N=32,48,64. Independent approximate conformal conservation controls use cubic-spline source-time derivatives of the projected stress, rather than directly copying derivatives from spectral Maxwell propagation:
**R_xi=−iK·S**, **S_i,xi=−iK_j Tij**.
The maximum mode-normalized energy Ward residuals improve ~3.20e-3 (32³), ~4.20e-4 (48³), ~2.29e-4 (64³); momentum Ward residuals improve ~3.03e-3, ~1.43e-3, ~4.24e-4. This is refinement, **not high-precision continuum certification**, with remaining source sampling, cubic interpolation and alias errors. Scalar anisotropy at tau=1:
32³ **0.0003032612**; 48³ **0.0003078812**; 64³ **0.0003083656**.
At tau=1.2, the three source channels are:
| N³ | S_L(1.2) | Im V_1(1.2) | Pi_plus(1.2) |
|---|---:|---:|---:|
| 32³ | −0.0000895689 | −0.0000059020 | −0.0001119104 |
| 48³ | −0.0000920718 | −0.0000065872 | −0.0001153726 |
| 64³ | −0.0000934051 | −0.0000075635 | −0.0001174942 |
The Fourier vector channel is imaginary in this real-space phase convention, with conjugate −K yielding a real physical field. Scalar/vector/tensor entries in this table are **matter stresses/momentum**, NOT all gravitational tidal components.

## Gate 1183 — ordinary K4 tensor-plus mode is genuinely sourced and evolved
Reuse the archived physical K4 tensor equation from **v15.750**, with cosmic tau and eta_s=3/4:
**gamma_plus''+3gamma_plus'/tau + beta_T gamma_plus/tau²=−2κ Pi_plus^physical(tau)**,
**beta_T=3|K|²+8eta_s/3=8** for |K|²=2; kappa=1.
For conformal Maxwell stress computed above,
**Pi_plus^physical(tau)=9 Pi_plus^conformal(tau)/tau⁴**, because a_FLRW=tau/sqrt3. Set zero *propagating* tensor Cauchy data gamma_plus(1)=gamma_plus'(1)=0, but retain the immediate source-driven tensor acceleration. Integrate using the same actual Maxwell time series interpolated in tau with a cubic spline and adaptive SciPy solve_ivp rtol 1e-11, atol 1e-14.

The historic v15.787 **full orthonormal electric Riemann**, not Weyl-only, for the tensor-plus metric gives the x-type plus coefficient
**E_plus^full=−[gamma_plus''+2gamma_plus'/tau]/2**,
where plus means the e/b polarization basis. This does not include any scalar/vector Ricci/tidal contribution in the same physical arm. At initial time, the zero gamma/gamma' data imply **E_plus^full(1)=9 Pi_plus^conformal(1)**, a sourced curvature contact, not a zero-past radiative field.

Empirical results:
| N³ | Pi_plus(1.2) | gamma_plus(1.2) | E_plus^full(1.2) |
|---|---:|---:|---:|
| 32³ | −0.00011191044 | −0.00007206708 | −0.00083014670 |
| 48³ | −0.00011537262 | −0.00007317270 | −0.00085034433 |
| 64³ | −0.00011749418 | −0.00007293224 | −0.00085751160 |
The 48³-to-64³ gamma difference is about 2.4e-7, and the full tensor electric curvature difference is ~7.2e-6. These are numerical *resolution comparisons*, not a proven continuum error bound.

## Gate 1184 — interpretation, Audit and continuation
**Positive:** the actual compact, source-free Maxwell packet now has nonzero longitudinal scalar anisotropic stress, a generated transverse momentum source, and nonzero tensor-plus anisotropic stress at the oblique nonzero mode K=(1,0,1). Its actual tensor-plus gravitational metric mode is evolved through finite time and one **full electric-Riemann tensor curvature component** is computed. The source satisfies ordinary 3D Maxwell energy and momentum conservation increasingly well with resolution; its parity-protected absent channels are appropriately reported as negative controls.

**Unclosed:** the oblique *scalar* and *vector* gravitational metric response must still be solved from all correct K4 source-first constraints, using Maxwell stress and signed ADM conventions as corrected v15.1226. We cannot use a nonzero source projector as a stand-in for those missing curvature sectors. Further, the full 3D source-to-metric reconstruction across all nonzero Fourier modes and k=0 cosmological background, finite detector spatial placement, free-mirror worldlines, photon null paths, emitter clock and physical emission-event identification (archived v15.811/v15.821) remain uncomputed. None of these quantities fixes the EM/G quarter-grid scale.

**Reproducer:** research-notes/k4_compact_maxwell_oblique_svt_tensor_v15_1234.py, source commit **94fa0ae67588361ea4fb7b6ed821dac9dbe60cb2**. A materially equivalent local NumPy/SciPy source+tensor implementation ran on N=32,48,64 and produced the displayed data, including generated Maxwell B, conventional SVT projector checks, transverse reflection nulls, Ward residuals and the sourced tensor electric-Riemann transfer. The committed standalone script includes explicit regression and resolution assertions, but has **not yet been independently post-commit re-executed by Audit**. As earlier Audit demonstrated, mathematical agreement should not be confused with proof that committed source bytes execute until checked.

**AUDIT HANDOFF:** re-execute the committed source cleanly and check the original stream function derivative signs and tensor-plus physical stress normalization under archived (+---), the exact k=(1,0,1) FFT (2,0,2) bin, 3D stress trace/projection and spatial reflection null, Maxwell Ward convergence, physical 9/tau⁴ source weight, beta_T=8, tensor gamma sign and full electric Riemann plus polarization tensor versus Weyl-only. Confirm that exact discrete Gauss for every FFT bin is *not* claimed. Keep the v15.1229 numbering collision disclosed and do not alter either old file.

**NEXT:** integrate the **same oblique mode's sourced K4 scalar and transverse vector** dynamical/constraint equations, reconstruct all nonzero full electric-Riemann scalar/vector/tensor contributions in a shared orthonormal polarization frame, then continue to full 3D Fourier reconstruction and gauge-controlled coasting photon/mirror/clock readout. The matched Einstein–Maxwell plus **identical relativistic solid** theory has the same tensor equation and source and therefore zero Cone-specific residual absent a new action-derived quarter-grid interaction.
