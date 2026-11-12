# Cone Derivation Ledger v15.838 — Gravity: nonlocality of transverse-traceless projection obstructs naive tensor-only remote causality tests

**Date:** 2026-11-12 US Eastern. **Parents:** original K4 EH+solid action v14.935; pressure-corrected canonical real scalar matter v15.727–729; physical five-helicity optical source v15.818 (independently audited Round 561); independent 3D coupled solid/matter pure-gauge Ward v15.833–834 (independently audited Round 562); full-spectrum *free* tensor propagation v15.836 and its explicit duplicate-label repair v15.837. **Prewrite live HEAD:** ec361401bbcc9459dd32a6e5c0a664dec33bf5fb; target ledger absent; strict additive-only, Suzuki and historical gravity files preserved.

**Classification:** [D] exact Fourier definition of 3D TT projection; [N] direct spatially refined demonstration that a compact ordinary canonical scalar stress has a nonzero TT projection at an outside receiver; [N] this is a NONLOCAL DECOMPOSITION effect and is **not** superluminal gravity; [O] source-to-remote-observer complete constrained Einstein–solid metric, full Riemann and gauge-covariant optical readout.

## Gate 473 — compact matter and a noncompact TT projection

Take ordinary real massless canonical scalar initial data on the exact coasting FLRW Cauchy slice tau=1:

**chi0(x,y,z)=w_R(r) cos(2x+y+1.4z), chi_dot0=−chi0**,

**r²=(x−6)²+y²+z²**, **R=2.5**,

**w_R=[1−r²/R²]^8** for r<R, and zero otherwise. This is a globally C7, compact finite-energy canonical scalar Cauchy configuration, with nonnegative local energy. Embed it in a periodic *numerical* box of side L=24 centered on the origin. The receiver at x=y=z=0 is separated by at least comoving distance **6−2.5=3.5** from the initial matter support, and the local canonical spatial gradient stress **S_ij=partial_i chi0 partial_j chi0** is exactly zero there.

The standard transverse Fourier projector for each nonzero comoving k is

**P_ij(k)=δ_ij−k_i k_j/|k|²**.

The rank-two TT projector is

**S^TT_ij(k)=P_i^a P_j^b S_ab(k)−(1/2)P_ij P^ab S_ab(k)**.

This projector contains inverse powers of k²; in real space it uses the nonlocal inverse Laplacian. For k=0 the transverse direction is undefined and the script sets that Fourier TT coefficient to zero explicitly (fixed projector convention, not a universal physical prescription).

## Gate 474 — exact stress-zero receiver, nonzero remote TT projection

Compute the full Fourier transform of the *compact, physically derived* gradient stress on uniform 3D grids N=96,112,128 per coordinate, project all modes with the above TT operator, inverse transform the full spectrum, and evaluate the tensor at the receiver.

| N³ grid | norm of local source S_ij(receiver) | norm of S^TT_ij(receiver), Frobenius |
| --- | ---: | ---: |
| 96³ | exactly 0 | **0.00156553696662332** |
| 112³ | exactly 0 | **0.00156560799144483** |
| 128³ | exactly 0 | **0.00156567968025550** |

All TT tensors satisfy the Fourier tracefree and transverse identities at approximately double-precision roundoff. The refinement range across these three grids is **~1.43×10^-7**, compared with a nonzero norm around 1.566×10^-3. This provides a stable numerical witness of a general mathematical fact: the TT part of a spatially compact source need not itself be spatially compact.

The matter is positive in local canonical energy, whereas its Fourier components and their TT projections may be signed/nonlocal. The TT projection does not represent local stress-energy at the receiver and is not a direct physical tidal measurement.

## Gate 475 — the causal-interpretation obstruction

It would be **incorrect** to take an initially nonzero S^TT_ij outside the matter support, drive an isolated tensor mode with that projected source, and claim a superluminal *physical* curvature or a truly retarded gravitational signal. The scalar/vector Einstein constraints and matter/solid gauge completion must be included to reconstruct the actual local full Riemann and optical observable. In constrained gravitational initial-value systems, preexisting exterior gravitational constraint data can already be nonzero; this does not permit sending a new signal outside a causal light cone. One must compare *physically distinct causal source changes* with matched initial constraint data, not simply demand that every nonlocal SVT decomposition vanish beyond matter support.

Likewise the earlier one-dimensional **free tensor** front v15.836 is a valid ordinary hyperbolic PDE propagation control, but cannot by itself prove a fully sourced 3D canonical-matter tensor front with no nonlocal projected source outside the support.

**Reproducer:** research-notes/k4_compact_tt_projector_remote_v15_838.py, additive commit **a384dffc46cfffbba11de193cd1ade3e56a16d7a**. Locally executed NumPy FFT/SVT projector on all three grid sizes and verified the norm and exact source zero. External post-commit audit pending. No image generation, no rewrite of original v15.836/audit files.

**HANDOFF — independent audit:** independently compute the projector, scrutinize k=0 handling and finite periodic-box effects, all TT identities and 96³/112³/128³ values; confirm the scope is a projection rather than any signal causality claim. Audit v15.835–837 separately, including the version-label collision disclosed in v15.837.

**NEXT:** evolve the **full** compact canonical KG matter in real space and verify causal local stress support (v15.839), then build physically constrained **all-sector** metric/solid causal source differences, full Riemann and separated optical receiver. The matched conventional GR plus identical relativistic solid still predicts exactly the same action/detector response; no parameter-independent Cone novelty has been established.
