# Cone Derivation Ledger v15.835 — Gravity: isolated Fourier-mode detector output cannot establish remote-source locality or signal arrival

**Date:** 2026-11-12 US Eastern. **Parents:** v15.727–818 physical source-to-five-helicity K4 finite-arm detector; v15.830–832 complete 3D pure-gauge optical check; v15.833–834 coupled original K4 solid action gauge Ward and false-shear controls. **Immediately prewrite live HEAD:** c11d157be1d91349d1d1b3d03b1587daf2e19d4f. Target absent; additive only, original Suzuki/frozen physics payloads unchanged.

**Classification:** [D] exact discrete spatial Fourier translation identity and full-spectrum localization recovery; [N] one spatial Fourier-mode detector amplitude cannot prove source/receiver causal separation, arrival, distance attenuation or far-field wave character; [O] a spacetime-retarded full-spectrum K4 physical source-to-receiver solution.

## Gate 463 — the subtle limitation in our successful five-helicity optical calculation

The v15.818 source is a positive-energy canonical scalar compact on its initial Cauchy slice and is physically evolved. Its gravitational source tensors and detector metric histories, however, are computed and observed at **one fixed spatial Fourier mode K=(2,0,1)** in a periodic box, with Fourier-volume normalization. Each individual nonzero Fourier component is spatially extended, regardless of how localized the full initial source was. Its optical time series can verify the **source-to-mode-to-photon** algebra and the five polarization readout, but it is not a detector response to the *entire* localized packet at a separated receiver.

For any translated spatial source f(x−x0), the Fourier transform satisfies

**fhat_shift(k)=exp(−i k·x0) fhat(k)**,

so **|fhat_shift(k)|=|fhat(k)|** for every single mode. Translating the emitter farther away changes the mode phase without reducing its magnitude; therefore an isolated mode signal cannot by itself establish a proper distance, attenuation or a retarded reception time. The full inverse spatial Fourier transform, together with the spacetime-retarded field equations/constraints, is needed to reconstruct the physical localized result. This is a standard Fourier fact, not a new Cone theorem.

## Gate 464 — concrete compact/remote numerical demonstration

Use a one-dimensional periodic box L=16 with 512 uniform points and a globally C7 compact source bump **f(x)=[1−(x/R)²]^8** for |x|<R, R=1, and zero outside. Translate the source by x0=4 away from the receiver at x=0. The translated source is exactly zero at that receiver: **f_shift(0)=0**.

At Fourier mode m=3 its complex coefficient is nevertheless **≈0+0.03609712266605469i** in the stated normalized FFT convention; it is NONZERO at the receiver as a global single-mode contribution. Its magnitude is unchanged by translation to machine precision. The **complete** inverse FFT reconstructs the localized translated source and gives **f_shift(0)≈1.93×10^−34**, consistent with exact zero. Both the exact translation-phase theorem and the source/receiver comparison are reproduced at <2×10^-14 error.

**Reproducer:** research-notes/k4_single_fourier_remote_obstruction_v15_835.py, additive commit **c3bc4b0d398efa1d07469f343f49764a170eaf3c**. Locally executed PASS for the exact Fourier phase, modulus invariance, full inverse support and source/receiver null. This example is Fourier localization algebra, NOT itself a retarded Einstein–solid propagation experiment.

## Gate 465 — scientific verdict and genuine remote detector requirement

**Positive:** the already audited five-helicity near-source Fourier calculation remains valid for its claimed mode- and gauge-limited purpose. **Negative:** interpreting that result as an astrophysical emitter–detector delay or source-distance attenuation would be unjustified: a single Fourier coefficient is explicitly incapable of encoding spatial support.

**NEXT:** reconstruct the complete spatial Fourier spectrum under the original retarded K4 propagation dynamics and read full local Riemann and photon/mirror/clock at a receiver outside the emitter's support. In v15.836 we first test the simpler **free tensor hyperbolic propagation** as a controlled causality benchmark. Distinguish nonpropagating metric constraints and background curvature tails from the radiative front; compare with established GR/FLRW retarded Green-function theory. No measured Newton G or Cone-specific coupling has been inserted.

**HANDOFF — audit:** reproduce exact source translation FFT and the example; check that the scope does not falsely rule out a spatially nonzero gravitational constraint field outside matter. Audit v15.833–834 complete action/solid Ward separately.
