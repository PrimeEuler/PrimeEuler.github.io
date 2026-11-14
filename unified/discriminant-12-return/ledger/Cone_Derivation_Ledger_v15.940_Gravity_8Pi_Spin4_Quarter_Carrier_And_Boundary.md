# Cone Derivation Ledger v15.940 — The 8π quarter-phase carrier tensored with the Spin(4) bicone

**Date:** 2026-11-13 US Eastern. **Gravity lane.** **Parents and redundancy:** v15.625 (distinct quarter geometric Casimir residues); v15.628 (odd-rung two-sector shift, amplitude freedom); v15.630 (odd quarters not ordinary SU2 spins); v15.631 (four U1 twisted holonomy sectors); v15.632–633 (bundle patch and fourth-root obstruction); v15.639 (bicone swap grading is not quarter Casimir parity); v15.642 (headless-bicone quotient); v15.701 (Hopf carrier source obstruction); v15.938 (original ladder quadrupole boundary obstruction); External Audit Round 575 **v15.939** independently passed Gravity v15.930–938. **Live HEAD immediately before ledger write:** 62591d88c470f0f604d6050dffa1c5be8bc93544. Target path checked absent. Additive only; certified frozen Suzuki, Audit, Sandbox and staged manuscripts untouched.

**Question:** Is the candidate odd-quarter algebra a “double cover” of SU2, or can one package it as a natural 8π-periodic phase degree of freedom next to the already-established two ordinary SU2 bicone factors? Test exact Casimir spectrum, grading, shift, adjoint/boundaries, Spin4 covariance, and constraints on physical normalization.

**Status:** [D] explicit 8π Fourier realization and exact finite-dimensional algebraic checks; [R] repackaging of already known holonomy and odd-rung results, not new Casimir spectrum; [N] a genuine new connected double cover of SU2 does not exist; [N] no physical field interaction, unique source coupling, or repaired quarter J tensor.

## Gate 702 — one 8π axial circle produces the complete formal quarter Casimir tower

Choose *an auxiliary* circle θ ∈ R/(8πZ) and Hilbert space L²(S¹_(8π)) with Fourier functions **|k>=exp(i kθ/4)/sqrt(8π)** for k∈Z. Define **K=−i∂θ**, so **K|k>=(k/4)|k>**. Choose **C=K(K+1)**. Its eigenvalues are exactly the established formal q=2 geometric spectrum **C_k=k(k+4)/16**. Restrict to k≥0 (Hardy/positive-frequency projection) to reproduce the nonnegative shell tower; this restriction is an **additional structural choice** not selected by the parabola geometry. This is unitarily equivalent to repackaging the four θ mod 2π twist sectors β=0,1/4,1/2,3/4 from v15.631 into a single 8π circle. Thus it improves compactness of the representation but **does not discover a new spectrum or quantum field**.

The conventional 2π translation **U_2π=e^{i2πK}** has eigenvalues i^k, is order four, and its square **χ=U_2π²=e^{i4πK}=(-1)^k**. The earlier quarter Casimir grading obeys **exp(16πi C)=(-1)^k** exactly (because k(k+4)≡k mod2). Thus χ=exp(16π i C) on this tower, and the known even-k EM subset versus odd-k candidate gravity subset is automatic. At odd k, a *phase-only* 4π translation acts by −1, and 8π translation acts trivially. This is **not** a physical 4π spatial rotation of an odd-quarter spin irrep: the angular geometry here is auxiliary U1, and SU2 is itself simply connected, with no nontrivial connected double cover. The source-faithful bicone instead has **Spin4=SU2×SU2**, double-covering SO4.

## Gate 703 — a canonical unit-modulus shift and its source-charge obstruction

On the complete two-sided Fourier tower k∈Z, choose the unitary multiplication **W=e^{iθ/4}**, W|k>=|k+1>. The exact identities are

**[K,W]=(1/4)W**,
**{χ,W}=0**,
**U_2π W=i W U_2π**,
**[C,W]=W(K/2+5/16)**.

The last identity follows from C_(k+1)−C_k=(2k+5)/16, and emphasizes that W changes geometric Casimir labels. This is a concrete **charge-one** sector-crossing operator with unit-modulus normalization as a *choice of Fourier multiplication*. That does **not** fix any coefficient λ multiplying W in a physical Hamiltonian. An arbitrary phase-valued function of K can alter W's channel phases; more general weighted shifts change strengths. A parity-even source built only from K/C and the Spin4 generators cannot change k; an interaction λW+λ*W† requires a separately provided charged source/field or a specified symmetry-breaking mechanism. Earlier v15.628/v15.695–701 already established this essential physical source/amplitude freedom.

On the **positive k≥0** Hardy tower, W is a unilateral isometry and **W†W=I, WW†=I−|0><0|**. Consequently **[W,W†]=−|0><0|**: the lower boundary is real. The finite N×N reproducer additionally has an artificial top cutoff so **W†W=I−|N−1><N−1|**, **WW†=I−|0><0|**. These must not be confused with the infinite bilateral unitary. The lower end is an ordinary Hardy-shift boundary, not automatically the original q=2 physical gravitational boundary.

## Gate 704 — tensoring with Spin4 is algebraically consistent but does not fix the defects

For any ordinary bicone representation `V_{j1}⊗V_{j2}`, define

**H_ext=(V_{j1}⊗V_{j2})⊗H_phase**,

with J_i and K_i on bicone factors, phase K and W on the last factor. Then **[J_i,K]=[K_i,K]=[J_i,W]=[K_i,W]=0** (commuting independent tensor factors). The phase W is a **rotational scalar**; a graviton-like rank-two tensor or position-like vector must be built separately and cannot be obtained by simply renaming W. The bicone **exchange parity** from v15.639 remains a distinct operator from χ acting on the Fourier factor.

This new tensor product is mathematically consistent, but it does not create an intertwined identification between the phase-label Casimir and physical total SU2 Casimir, nor repair the **original defective step-one quarter ladder**. In particular, on odd-quarter L=7 the known intrinsic boundary Casimir defect E_L has rank two; tensoring with a four-state spin-half×spin-half bicone makes E_L⊗I4 rank eight, not zero. Thus the extra phase factor cannot be used to declare v15.938's tidal tensor covariant. If someone defines a separate connection, a nontrivial mixed generator or a central extension, its Jacobi/adjoint and physical patching must be verified independently.

## Gate 705 — verification, negative physical selector and next route

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_spin4_8pi_quarter_carrier_v15_940.py`, additive commit **62591d88c470f0f604d6050dffa1c5be8bc93544**. Independent local Python/SymPy run PASS on finite Fourier cuts N=4,8,16,32: K/C spectra, U2π order-four character, χ parity, Casimir-shift commutator and correct operator order, Fourier shift adjoints and lower/top finite-cut projectors, Spin4 tensor commutation, and persistence of rank-two defect at odd-quarter L=7. **External Audit pending.**

**Outcome:** **Positive mathematical carrier**—the bicone Spin4 and an 8π U1 Fourier phase can coexist; the phase recovers all formal q=2 Casimir values, a Z4 character and a natural parity-changing isometry in a unified realization. **Negative novelty/physical gate**—this is a reformulation of existing v15.631/v15.628 holonomy and shift, not a new double cover of SU2, and it fixes no unique gravitational tensor, physical winding/connection, SI clock, source coupling or experiment. The original boundary-defective q=2 algebra remains distinct.

**NEXT:** Test whether a physical field-derived connection can identify the phase circle with an actual bicone or Lorentzian spacetime bundle globally, respecting v15.632–633's monopole Chern/fourth-root obstruction. Alternatively derive an explicitly sourced off-diagonal physical action including its charge-one compensator, then compare its dimensionless response to ordinary U1 hopping/interferometry. Unless a nontrivial source or global bundle datum emerges, stop recasting the same character algebra.

**HANDOFF Audit:** verify the exact 8π Fourier/β-sector equivalence, `[C,W]=W(K/2+5/16)` ordering, the 4π sign vs physical SU2 rotation distinction, Hardy lower-end commutator, and Spin4 tensor-product persistence of the E defect.
