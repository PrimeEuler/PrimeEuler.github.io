# Cone Derivation Ledger v15.839 — Gravity: complete spatial spectrum of compact canonical KG matter respects remote finite propagation

**Date:** 2026-11-12 US Eastern. **Parents:** frozen original coasting K4 Einstein–Hilbert/solid action v14.935; positive-energy canonical source and wave equation v15.727–730; compact four-wave K4 optical example v15.817–818; spatial single-Fourier obstruction v15.835; one-dimensional free tensor causal front v15.836/v15.837; TT projector nonlocality v15.838. **Immediately prewrite HEAD:** db830c9f52396b636e9f186e9fcab90500a22e30; ledger path absent. Strict additive-only, Suzuki and certified historical files unchanged.

**Classification:** [D] exact Fourier-mode propagation formula for physical real massless canonical matter on the coasting background, compact initial Cauchy data and strict continuum finite-domain-of-dependence theorem; [N] refined 3D numerical receiver field and positive local energy before/after expected arrival; [O] a physically sourced complete Einstein–solid remote tidal/optical response; [N] no experimental gravitational coupling or unique Cone effect.

## Gate 476 — use the actual canonical positive-energy field, not a single TT or Fourier mode

At τ0=1 and coasting **a(τ)=τ/sqrt3**, give the real minimally coupled massless canonical scalar initial data

**chi0(x,y,z)=w_R(r) cos(2x+y+1.4z)**,

**chidot0=−chi0**, **r²=(x−6)²+y²+z²**,

where **w_R(r)=(1−r²/R²)^8** for r<R=2.5 and zero outside. The cutoff is globally C7 and the initial source has compact support inside the radius-2.5 sphere about (6,0,0), with nonnegative local density **rho=(chidot²+|grad chi|²/a²)/2**.

The continuum Klein–Gordon Cauchy equation is

**chiddot+(3/τ)chidot−(3/τ²)Δchi=0**.

For logarithmic time **s=log τ**, the initial derivative choice gives the *exact* mode solution

**chi_k(τ)=τ^(−1)cos[s sqrt(3|k|²−1)] chi_k(1)**,

with imaginary frequencies correctly understood through cosine's analytic continuation. The first time derivative and all spatial gradients follow **analytically in Fourier space** before inverse FFT. Thus every field and density sample at the receiver derives from the **complete spatial spectrum of the same finite-energy real physical matter field**. No prescribed signed source profile is introduced.

## Gate 477 — finite domain of dependence and analytic front

Place the receiver at the spatial origin, distance 6 from the packet's center and distance **3.5** from its nearest initial support. The FLRW comoving radial null travel distance from cosmic τ=1 to τ is

**d_null(τ)=∫_1^τ dσ/a(σ)=sqrt3 logτ=sqrt3 s**.

Hence no local change in the canonical field from these compact data can reach the receiver before

**s_front=3.5/sqrt3≈2.02072594216369**,

**τ_front=exp(3.5/sqrt3)≈7.544**.

The continuum finite-propagation-speed theorem ensures **chi=0, grad chi=0 and rho=0 at the receiver for s<s_front** (for the compact-data perturbation against the zero-scalar background). The result is a mathematical consequence of the hyperbolic KG equation and coasting conformal light cone, not a claim of new gravity.

Use a periodic **numerical** box L=32 with 128³ and 160³ grids, which has no periodic-image arrival contaminating the receiver in the tested window through s=3.0. Numerical spectral differentiation of finite-C7 fields creates small, resolution-dependent prefront truncation tails; these are not physical field leakage.

## Gate 478 — actual remote receiver: quiet before arrival, nonzero afterwards

Compute the *full inverse Fourier reconstruction* of chi, chidot, three spatial derivatives and local nonnegative canonical rho at receiver (0,0,0). Representative results are:

| s=logτ | |chi(receiver)|, 128³ | |chi(receiver)|, 160³ | rho(receiver), 160³ |
| ---: | ---: | ---: | ---: |
| 0.5 | 3.9271×10^-8 | 3.5924×10^-9 | 4.28×10^-16 |
| 1.0 | 1.1970×10^-8 | 1.4282×10^-9 | 1.15×10^-14 |
| 1.5 | 7.6133×10^-8 | 5.6088×10^-9 | 6.49×10^-16 |
| 1.9 | 4.3136×10^-8 | 6.0429×10^-10 | 8.13×10^-16 |
| 2.5 | 7.4904×10^-5 | 7.4902×10^-5 | 8.06×10^-9 |
| 3.0 | 2.06059×10^-4 | 2.06052×10^-4 | 7.9243×10^-8 |

All four prefront receiver chi values decrease markedly with refinement; 160³ has prefront |chi|<1×10^-8 and rho<2×10^-13. Beyond the predicted front, both the field and local positive energy become nonzero, with 128³ and 160³ field amplitudes agreeing within 2×10^-8 and local rho within 5×10^-11.

The initial support is smooth and vanishes to high order at its boundary, so a tiny post-front response close to s_front is expected; the first explicitly tabulated post-front sample is s=2.5. The comparison does **not** use the nonlocal TT stress projection as a local energy or emission measurement.

## Gate 479 — why this complements rather than contradicts v15.838

The ordinary canonical matter **chi, its local derivatives and local rho** are genuinely local fields, and propagate with causal finite support (subject to the small spectral truncation errors shown). In contrast, the Fourier TT projection of their spatial anisotropic stress is a nonlocal decomposition of the same matter tensor and can be nonzero outside the packet's support already on the initial slice (v15.838). That does **not** imply the canonical matter or a truly physical complete gravitational detector response travels acausally.

For a *gravitational* separated receiver one must solve the fully constrained Einstein–solid system consistently: its background has nonzero solid stress, its scalar/vector metric constraints encode initial/exterior gravitational data, and the complete local Riemann and observer/geodesic/photon histories may exhibit cancellation of apparent instantaneous decomposition terms. Compare matched physical initial metric/constraint data and causal source changes before calling any new signal retarded.

**Reproducer:** research-notes/k4_compact_canonical_kg_remote_front_v15_839.py, additive commit **ec361401bbcc9459dd32a6e5c0a664dec33bf5fb**. Equivalent local NumPy 3D FFT program executed for 128³/160³ and PASS for expected front, prefront near-zero/refinement, postfront nonzero and cross-grid consistency. New committed-byte independent audit still pending. No image generation or previous source rewrites.

**HANDOFF — external audit:** independently run v15.838 and v15.839 at their published resolutions. Verify compact source support, TT Fourier projector transverse/trace identities and apparent remote projection, full KG mode transfer including imaginary low-k frequency continuation, coordinate light-front time and the numerical pre/postfront values. Keep v15.836/v15.837 historical version collision disclosed; original scientific results unchanged.

**NEXT:** Construct a *physical-source, fully constrained, multi-k* K4 metric and solid solution for this 3D compact canonical matter, with consistent initial gravitational constraint data. Compute **full local electric Riemann** and the finite-baseline gauge-covariant optical signal at a remote receiver; explicitly separate static exterior constraint fields from signal changes. Only then test conventional matched GR+solid subtraction, which remains identically zero until an independently derived Cone-specific operator or parameter-free selector exists.
