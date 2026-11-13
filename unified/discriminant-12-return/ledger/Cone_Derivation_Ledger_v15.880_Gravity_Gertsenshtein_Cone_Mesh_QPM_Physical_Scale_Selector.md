# Cone Derivation Ledger v15.880 — Gravity: Can the EM-half / G-quarter mesh fix physical Gertsenshtein quasi-phase-matching length?

**Date:** 2026-11-13 US Eastern. **Parents:** Muse/Sandbox v15.866 (sector q=h/2, EM q=1/2, G q=1/4, squared corrections 1/4 vs 1/16) and v15.867–869 (node and turn-rate dictionary); Gravity v15.877/878 standard Einstein–Maxwell photon–graviton polarization conversion; v15.879 unitary no-attractor theorem and externally specified spatial magnetic-field-reversal quasi-phase-matching positive control. **Live HEAD immediately prewrite:** 9f2d47157813aaad9a2fd8de6fead2789d6e6575. Target file checked absent. This is an additive-only research gate; no certified, Sandbox or Suzuki artifacts touched.

**Classification:** [D] exact Fourier harmonics of a sign-reversing transverse physical magnetic field; [N] numerical unitary two-state solution agrees with weak-mixing Born Fourier prediction, and both exhibit mismatch-sensitive QPM; [N] no independent physical length selector from the Cone h/2 versus h/4 bookkeeping; [O] original action-derived medium/field source and a discrete mesh-to-length dynamical law.

## Gate 522 — separate normalized mesh position from measurable magnetic reversal spacing

For an externally given sinusoidal/square-wave magnetic-field profile with spatial period **Lambda** and photon–graviton refractive wavenumber mismatch **Delta**,

**B_T(z)=B_0 sign[cos(2 pi z/Lambda)]**.

In the first-order (small mixing, undepleted incident graviton) Einstein–Maxwell wave-conversion model, the outgoing photon amplitude is proportional to

**A_gamma(L) = -i mu_0 ∫_0^L sign[cos(2 pi z/Lambda)] exp(i Delta z) dz**,

up to a convention-dependent overall propagation phase. The physically relevant dimensionless detuning parameter is **r=Delta Lambda/(2 pi)**. A mesh coordinate q=1/2 or q=1/4, by itself, does not determine either Lambda in metres or Delta in inverse metres. The exact half-step identity

**[h(j+1/2)]²−(h/2)² = h²j(j+1)**

gives squared offsets **1/4** for h_EM=1 and **1/16** for h_G=1/2, but is independent of Delta or Lambda. The relative mesh factor of two therefore cannot set a new physical photon–graviton phase-matching length without an independent dimensionful calibration/dispersion relation.

## Gate 523 — exact selection harmonics for a four-period sign-reversing field

Choose Lambda=2pi in arbitrary spatial units; the external B field is sign(cos z), and integrate it over **L=4 Lambda=8pi**. For mismatch Delta=r (in those chosen units) define the dimensionless Fourier amplitude

**a(r) = (1/L) ∫_0^L sign(cos z) exp(i r z) dz**.

At integer odd r=2n+1, its exact value is

**a(2n+1) = [2/(pi(2n+1))] (-1)^n**,

and at positive even integer r it is zero. The maximum fundamental occurs at r=1, which is precisely **Delta Lambda=2pi**. This is the familiar odd-harmonic Fourier series of a square-wave magnetic profile, *not* a universal resonance of the Cone quarter-grid.

| mismatch / pattern fundamental r | |a(r)|² |
| ---: | ---: |
| 1/2 | <1e-30 (numerical zero for four whole periods) |
| 1 | 0.405284734569351 |
| 3/2 | <1e-30 |
| 2 | <1e-30 |
| 3 | 0.0450316371743724 |
| 5 | 0.0162113893827740 |

The half-integer null entries depend on the chosen observation length of four complete periods, rather than being generally zero at arbitrary finite length. Likewise odd-harmonic selectivity is a property of the *assumed B shape*. Changing the reversal profile changes the Fourier spectrum. All tabulated values are *normalized Born amplitudes*, not physical conversion probabilities or an amplification beyond unitarity.

## Gate 524 — preserve physical length covariance and validate full two-state propagation

The normalized Fourier amplitude depends on physical Delta and Lambda only via **Delta Lambda/(2pi)**, assuming the number of profile periods remains fixed. Thus replacing **(Delta,Lambda) -> (2Delta,Lambda/2)** preserves the normalized transfer. It follows directly that an invariant integer mesh ratio does not select an absolute Lambda: infinitely many physical pairs have the same conversion response.

The exact **lossless 2×2 mixed-wave propagation** solves

**i d/dz (A_gamma,h)^T = [[Delta,mu(z)],[mu(z),0]] (A_gamma,h)^T**

with piecewise constant signed mu(z) from the real sign(cos z) B field, multiplying each domain's matrix exponential. This unitary calculation agrees with the first-order Born predictions for **mu=10^-4**:

| Delta | full exact P | leading Born P |
| ---: | ---: | ---: |
| 1 | 2.55999780565e-6 | 2.56000000000e-6 |
| 3 | 2.84444409411e-7 | 2.84444444444e-7 |

The exact propagation norm U†U=I is verified numerically better than 1e-12. The weak-mixing relative discrepancy is O(mu²), consistent with the undepleted-field approximation. This validates that the Fourier response arises from real, physically reversed mixing signs, not conventionally relabeling a polarization axis.

**Reproducer:** research-notes/k4_gertsenshtein_mesh_qpm_selector_v15_880.py, commit **9f2d47157813aaad9a2fd8de6fead2789d6e6575**. Independently run before commit from the local working file, with analytic harmonic assertions, fixed-length nulls, scale-covariance test and exact 2×2 piecewise exponential comparison; all PASS. Committed-byte external audit pending.

## Gate 525 — answer and principled next step

**Positive:** real magnetic-field sign reversals can quasi-phase-match conventional Gertsenshtein conversion, and the mismatch determines the needed reversal period. The Cone half/quarter node/antinode language offers a consistent *coordinate description* of such periodic signs.

**Negative:** Cone's h_EM=1 versus h_G=1/2, or q_EM=1/2 versus q_G=1/4, fixes no physical wave mismatch, field reversal period, external magnetic field, supporting current, or coupling amplitude. On the original K4 EH+isotropic-solid + Maxwell action, the result remains conventional Einstein–Maxwell + identical solid: no new force, no independent G and no distinct dimensionless prediction. Numerical peaks at chosen r=1,3,5 are supplied by the B modulation's Fourier harmonics, not an emergent phase-locking rule.

**Open:** to turn the proposal into a physical novelty gate, derive from a covariant action or a predictive microscopic selector a *real B/current spatial pattern* B(z), its preferred Lambda, the photon–graviton dispersion Delta, and a source/energy budget, without setting Lambda=2pi/Delta by hand. Then compare its polarization-resolved conversion with ordinary Gertsenshtein/QED/plasma/elasticity. A separate complete K4+Maxwell constrained finite-source/receiver simulation remains unperformed.

**HANDOFF — Audit and Muse:** independently reexecute v15.880, confirm four-period square-wave harmonics, control dependence on observation length, unitary 2×2 propagation/Born match, and the no-new-scale verdict. Explicitly distinguish a **physical magnetic-field reversal** from a **basis convention sign**. Do not repurpose the independent Suzuki automation.
