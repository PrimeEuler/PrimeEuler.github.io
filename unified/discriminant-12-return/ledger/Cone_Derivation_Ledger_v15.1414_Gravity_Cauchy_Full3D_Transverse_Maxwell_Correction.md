# Cone Derivation Ledger v15.1414 — Correct full 3D Fourier source and retarded Maxwell response for Cauchy-initialized nonlinear H² waves

**Date:** 2026-11-24 Eastern / UTC Nov 25. **Lane:** Gravity/Cone. **Status:** [N PASS local code] the corrected q=(1,1,−1) 3D Fourier coefficient of the actual Weyl–H² Maxwell current remains nonzero and excites a transverse Maxwell oscillator; [N PASS] source-work energy identity, mesh / finite-derivative refinement, halving-coupling and zero-coupling controls; [CORRECTION] earlier v15.1413's fixed-z 2D Fourier source projected as 3D was wrong and **is superseded**; [NEGATIVE] no full sigma/EM/EH backreaction, no actual emitted photon flux in unbounded space, and no quarter-grid-selected coupling. **Reproducer** `research-notes/k4_cauchy_full3d_mode_v15_1414.py` SHA **36a9539b63d94a4e48f7b70f5158c5ffaa28577e**, exact committed-byte Audit replay pending.

## Gate 1351 — perform the missing z projection before transverse Maxwell separation

In v15.1413, the TT gravitational source has exact z dependence cos(t−z), and the sigma pair has **no z dependence**. Thus its curvature-contracted Maxwell current has only z spatial harmonics qz=+1 and qz=−1. For any fixed (t,x,y) write

`J^mu(t,x,y,z)=C^mu(t,x,y) cos z+S^mu(t,x,y) sin z`.

Then its exact negative z-frequency spatial Fourier coefficient is

`Jhat^mu_(qz=−1)=[J^mu(z=0)+i J^mu(z=π/2)]/2`,

without 3D sampling ambiguity. FIRST take the 2D x,y Fourier coefficient (qx,qy)=(1,1) of each of the two z slices (FFT normalization 1/N²), THEN apply

`P_T(q)j=j−q(q·j)/|q|²` for `q=(1,1,−1)`, `|q|²=3`.

This is the genuine 3D transverse spatial-mode source of the **prescribed first-order Einstein vacuum TT wave** and the **Cauchy-corrected fifth-order sigma history**. It retains time-frequency bandwidth from the homogeneous sigma correction, so a spatial q²=3 does NOT alone prove the time Fourier energy is on photon shell or that free radiation escaped after interaction.

At t=.7, sigma a=b=.3, full 3D transverse source amplitudes:

| N² | leading | normalized area with uncorrected sigma | fifth-order periodic particular | fifth-order zero-Cauchy |
|---:|---:|---:|---:|---:|
| 16² | .03674234540799 | .03595483397386 | .03593725801787 | **.03596268592949** |
| 24² | .03674234540671 | .03595483397266 | .03593725801665 | **.03596268592805** |
| 32² | .03674234540709 | .03595483397302 | .03593725801700 | **.03596268592859** |

This fixes the first gate's projection error without changing the prior field equations or introducing any new EM interaction. The Cauchy correction differs from the normalized, uncorrected sigma area response by about 0.022%, and from the periodic particular by about 0.071% at the selected mode; Cauchy and periodic are *distinct* histories with different initial data.

Temporal centered derivative step convergence at N24:

| step h | |J_T| |
|---:|---:|
| .0016 | .03596267876916 |
| .0008 | .03596268449612 |
| .0004 | .03596268592805 |
| .0002 | .03596268628532 |

The decrease in difference by ~4 as h halves is consistent with second-order derivative truncation. N16–N32 differences <2×10^−9 relative; this is a controlled initial mesh test, not certified continuum convergence of a fully interacting PDE.

## Gate 1352 — physical spatial mode: driven Maxwell oscillator work identity

At the correctly selected 3D Fourier q=(1,1,−1) let `J_T(t)` be the corrected complex transverse source. At 25 equally spaced times 0≤t≤1.2, calculate it directly from the full tensor; interpolate the sampled time sequence with a cubic spline (not a hand-chosen Gaussian), and solve

`A_T''+3 A_T=−g J_T(t)`, `A_T(0)=A_T'(0)=0`,

with DOP853 high accuracy and arbitrary illustrative g=.05. Independent Simpson quadrature of the work `W=−g∫Re[A'_T(t)^*·J_T(t)]dt` agrees with final quadratic mode energy `E=(|A'_T|²+3|A_T|²)/2`:

| N² | sigma a=b | g | final mode E | source work | work/E residual |
|---:|---:|---:|---:|---:|---:|
| 16² | .3 | .05 | **1.5222185779077537e−6** | 1.5222185787356768e−6 | 5.4389235e−10 |
| 16² | .3 | .025 | 3.8055464442419104e−7 | 3.8055464456493383e−7 | 3.6983594e−10 |
| 16² | .3 | 0 | 0 | 0 | 0 |
| 16² | .15 | .05 | 9.820872572062981e−8 | 9.820872572218358e−8 | 1.5821161e−11 |

All are **single complex spatial Fourier-mode diagnostic energies** in fixed-background model units, not a global 3D real photon energy or total Einstein–matter Hamiltonian. Halving g quarters energy exactly, and g=0 gives zero. The variation with sigma amplitude is dominated by the leading bilinear source J∼ab, with higher target corrections.

**Local source actually executed:** `/mnt/data/cone_gate/k4_cauchy_full3d_mode_v15_1414.py`. **GitHub additive equivalent:** `research-notes/k4_cauchy_full3d_mode_v15_1414.py`, commit **36a9539b63d94a4e48f7b70f5158c5ffaa28577e**; imports committed v15.1413. The exact GitHub committed bytes have not yet been independently replayed; Audit must run v15.1413 AND v15.1414 together and correct any naming errors additively. The earlier exploratory fixed-z projection artifact is preserved, not silently overwritten.

## Gate 1353 — falsification boundary and next

The nonlinear H² field correction is initialized at zero fifth-order perturbation and zero initial correction velocity. Its fifth-order correction is an actual Cauchy solution in a *2D periodic background*, but the full sigma fields still solve only the isolated nonlinear sigma PDE through **order six**, not to all orders. The gravitational TT metric is prescribed, the Weyl–Maxwell interaction coefficient is arbitrary, and emitted EM energy is supplied by the externally held source without calculating the physical sigma/TT depletion. Thus this gate closes **the current-projection ambiguity**, not true four-way gravitational energy conservation, a finite-energy wavepacket scattering measurement, or a new quarter-mesh force.

**AUDIT HANDOFF:** (1) rerun exact committed v15.1413/v15.1414 sources in a fresh checkout, (2) independently derive and test the real z-harmonic coefficient formula and sign of i for qz=−1, (3) reconstruct 4-current conservation including exact time-frequency (NOT incorrectly require a source to satisfy a single monochromatic Ward relation ωJ0=q·J when its time signal contains bandwidth), (4) test N16/N24/N32 and h halving, (5) verify source-work identity and coupling controls, and (6) check source-related field normalization and whether aliasing/dealiasing or initial-data boundary choices alter output. Preserve all negative status labels.

**NEXT:** compute independent coupled corrections to sigma equations from the actual Maxwell field and to metric from sigma stress and the Weyl operator's full variation, with actual Noether/Bianchi total energy exchange. Continue treating q2=1/16 as a **representation-space level**, not physical G or gravity mass; the observed Dirac rapidity 45.310 was imported from G and no parameter-free 1/4 coupling emerged.
