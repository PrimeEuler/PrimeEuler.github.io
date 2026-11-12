# Cone Derivation Ledger v15.836 — Gravity: full-spectrum free K4 tensor mode has a causal front and nonzero tidal curvature at a separated receiver

**Date:** 2026-11-12 US Eastern. **Parents:** original K4 Einstein–Hilbert+isotropic solid v14.935, tensor/vector/scalar K4 mode equations v15.706/714/721–722, full electric tensor Riemann derivation v15.787–788, physical five-helicity optical mode calculation v15.818, single Fourier mode remote-source obstruction v15.835. **Live HEAD immediately prewrite:** c2742d18318b2d7dbd3c8dbfffc510929f759408; target checked absent. Additive-only; Suzuki/certified assets untouched.

**Status:** [D] exact log-time reduction of the K4 free tensor Euler equation to a massive one-dimensional hyperbolic master equation with finite propagation speed; [N] spectral numerical reconstruction of compact C7 initial tensor data and full electric tidal curvature at a separated receiver, initially zero until a causal front and then nonzero; [N] isolated Fourier modes display spurious apparent pre-arrival amplitudes; [O] physically sourced 3D compact canonical emitter, tensor/elastic scalar/vector full constraint propagators, optical detector and calibrated novelty.

## Gate 466 — tensor-mode PDE instead of a single Fourier coefficient

The original K4 tensor Euler operator on a coasting FLRW background with a(τ)=τ/sqrt3 has, for each spatial comoving wavevector k, the source-free equation

**γ̈_k+(3/τ)γ̇_k+[3|k|²+8η_s/3]γ_k/τ²=0**.

At **η_s=3/4**, define **s=lnτ**, **γ(τ,x)=τ^(−1)u(s,x)**. In a single spatial propagation direction x, the complete inverse-Fourier PDE is

**∂²_s u−3∂²_x u+u=0**.

This is an ordinary hyperbolic massive Klein–Gordon master equation with propagation speed **sqrt3 in logarithmic time**. With conformal time change **dη= sqrt3 ds**, the corresponding physical tensor front speed is exactly luminal (c=1 in the FLRW conformal metric), as already found in v15.752. The +u potential produces a *tail inside the light cone*; it does not imply a spatial signal beyond the characteristic front.

The associated full local tensor-plus electric Riemann curvature from v15.787, in a local comoving orthonormal frame, is

**R^x_(0x0)=−(γ̈+2γ̇/τ)/2=−τ^(−3)(u_ss−u_s)/2**.

Thus a sharp test of genuine remote tidal response requires the full set of Fourier k modes, not just one isolated mode.

## Gate 467 — compact C7 tensor initial data and distant receiver

Use a one-dimensional periodic computational interval **L=32** with smooth compact initial conditions at τ=1:

**u(0,x)= [1−((x−5)/2)²]^8** for |x−5|<2, zero outside, and **u_s(0,x)=0**.

The tensor data have compact x support [3,7]. A receiver is placed at x=0, completely outside that support. The nearest initial-data point is at comoving distance 3, so a causal front cannot reach it until

**s_front=3/sqrt3=sqrt3≈1.732050807568877**, equivalently **τ_front=exp(sqrt3)≈5.652233674034092**.

The 32-unit periodic box is large enough that wrapping paths do not contaminate the receiver over the stated time interval s≤2.35. Note explicitly that this is a **one-dimensionally localized plane-symmetric tensor perturbation** (transverse directions remain unbounded), not a fully three-dimensional compact gravitational-wave packet and not a canonical scalar matter emitter.

The exact Fourier mode evolution is

**u_k(s)=u_k(0)cos(sqrt[3k²+1]s)**,

because u_s(0)=0. The full spatial inverse FFT reconstructs u, u_s and u_ss and hence both γ and the full electric Riemann at receiver x=0.

## Gate 468 — numerical causal support and post-front full electric curvature

Independent N=1024 and N=2048 full-spectrum reconstructions agree closely. At N=2048, the receiver amplitudes are:

| s=lnτ | γ(receiver) | Full electric Riemann R^x_(0x0) |
| ---: | ---: | ---: |
| 0.0 | ≈−5.20×10^-18 | ≈+2.90×10^-13 |
| 0.5 | ≈+1.26×10^-17 | ≈+1.46×10^-13 |
| 1.0 | ≈+6.22×10^-18 | ≈−1.29×10^-14 |
| 1.5 | ≈−3.87×10^-18 | ≈−1.12×10^-14 |
| 2.0 | **+5.25247085×10^-5** | **−2.52644733×10^-4** |
| 2.35 | **+0.00607966679** | **−0.00082872076** |

The first four times precede s_front≈1.732; the physically reconstructed field and tidal curvature are zero up to spectral roundoff. After the expected front, both become nonzero. For reference, already at s=0.5 one *isolated* m=4 Fourier component of the receiver's tensor master amplitude is **≈−0.00999555+0.00999555i**, apparently nonzero before the front; it cannot be regarded as the real remote signal. Full-spectrum interference restores causality. The single-mode control at s=0 is similarly ≈−0.0248062+0.0248062i even though the compact initial field at receiver vanishes.

**Reproducer:** research-notes/k4_remote_tensor_causal_front_v15_836.py, additive commit **c11d157be1d91349d1d1b3d03b1587daf2e19d4f**. Tested locally with NumPy FFT at 1024 and 2048 spatial points. The prefront receiver |γ| <3×10^-8 and |R| <5×10^-7 assertions pass, full field/tidal refinement passes and both postfront signals are nonzero. All FFT and Pythagorean/cosmic-time factors can be independently rederived from the original K4 tensor ODE.

## Gate 469 — scientific interpretation and required next test

**Positive:** a separate receiver can be modeled *causally* by retaining the full spatial Fourier spectrum of a compact initial tensor disturbance, including its fully reconstructed local tidal curvature. This is a substantive bridge between the previously exact K4 mode equations and a real-space propagation check.

**Negative:** no canonical positive-energy matter *source* feeds this free tensor example; there is no localized three-dimensional source/detector geometry, no returning laser photon path, no autonomous physical source switch-on, and no new scale or dimensionless Cone-only gravitational coupling. This is a conventional hyperbolic wave result; the tensor characteristic and causal support are exactly those of standard relativistic GR+solid and do not distinguish theories. The background elastic solid and metric constraints for scalar/vector sectors require care: an elliptic Newtonian potential may be spatially nonzero outside matter on an initial slice, and its gauge-dependent instantaneous appearance must not be misreported as superluminal physical propagation.

**HANDOFF — external audit:** independently run both new committed numerical scripts v15.835/836 and the solid-action v15.833/834 proofs; verify source support location, correct logarithmic-time K4 tensor mass term, full electric Riemann derivative, front s=sqrt3 and no periodic wrap in the time window. Compare the emergent causal fronts with standard FLRW gravitational-wave Green functions (including possible curvature tails). Keep exact ordinary Einstein–Hilbert+relativistic solid matched-action null.

**NEXT:** replace the free plane-symmetric tensor initial packet by **the sourced, spatially three-dimensionally compact canonical four-wave matter packet** from v15.818; reconstruct all Fourier k modes and source the full K4 tensor (+/×) with properly normalized TT projectors, then compute receiver Riemann and two-way optical delays *outside the material support*. Only after that extend to full scalar/vector constraint evolution, full gauge-covariant source and detector event preparation, and a new independently selected Cone interaction candidate.
