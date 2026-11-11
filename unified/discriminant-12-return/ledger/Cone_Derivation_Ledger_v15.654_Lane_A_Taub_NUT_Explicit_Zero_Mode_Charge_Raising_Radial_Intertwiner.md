# Cone Derivation Ledger v15.654 — Gravity lane: explicit 4D Taub–NUT Dirac zero-mode charge generator, radial intertwining, and exact upper-domain obstruction

**Date:** 2026-11-10 (local US Eastern). **Parents:** v14.731–732 (mass–NUT pair independently quarter-quantized, separate Lorentzian model); v15.632 (Misner-periodic monopole winding), v15.646 (Hasebe supersphere half-charge ladder comparison); v15.647 (Euclidean TN Killing–Yano operators preserve fiber momentum); v15.651 (global S² spinor-twisted charge-one bridge); v15.653 (Euclidean 4D Jante–Schroers exact radial normalizability); **External Audit Round 531**, most recent, verifies v15.653 at HEAD df9f185f. **Status:** [D] exact radial first-order intertwiner and 4D zero-mode mapping for admissible charge sectors; [C] proposed unbounded multiplication operator extracted from the published zero modes, not claimed as a published dynamical symmetry; [O] full Dirac operator intertwining, conserved/physical transition, coupling, odd-quarter geometric Casimir and Lorentzian observable. **Fresh prewrite HEAD:** 787ef092c35f79fea6a8a00e27897258760a8e3f (exact reproducibility script just committed); duplicate v15.654 ledger search negative. All writes additive, no frozen Suzuki edits and no attempt to identify Suzuki physical-quarter sectors.

**Primary source:** R. Jante and B. J. Schroers, *Dirac operators on the Taub-NUT space, monopoles and SU(2) representations*, JHEP **01** (2014) 114, DOI 10.1007/JHEP01(2014)114, especially (3.35)–(3.47) and (A.22)–(A.35). The published PDF's pages 19–21 (journal labels) were read, including its full four-spinor mode formula and radial equation. These new intertwining conclusions are derived from its explicit modes, not claimed verbatim from the paper.

## Gate 176 — construct a 4D charge-raising zero-mode solution generator

In the **Euclidean** TN metric with radial coordinate ρ=r/L, and a separately introduced self-dual auxiliary Abelian gauge field of free continuous strength p_aux>0, the published zero modes of charge n=2j+1 have
Ψ_(n,P)(ρ,z₁,z₂)=R_n(ρ) P_(n−1)(z₁,z₂) e_top,
where e_top=(1,0,0,0)^T in the paper's spin frame; P_(n−1) is holomorphic and homogeneous of degree n−1, and
R_n(ρ)=ρ^((n−1)/2)/√(1+ρ) · exp[−(p_aux−n)ρ/2] (suppressing normalisation).
They exist in L² **iff n<p_aux**.

Set **B_α=√ρ exp(ρ/2) z_α** as a *multiplication* operator on spinor-valued functions (α=1,2, a spin-1/2 SU2 doublet). Then, by direct identity,
**B_α Ψ_(n,P)=Ψ_(n+1,z_α P)**,
provided **n+1<p_aux** so that the target is an L² zero mode. The fiber quantum number n increases by one because z_α has one Hopf-fiber character unit relative to polynomial degree, and the published lifted right-fiber number operator Nhat differs by a fixed spin-frame shift (the modes have n=degree+1). Thus **[Nhat,B_α]=B_α on the mode tower**. In the chosen coordinate framing, B_α is an explicit *global scalar multiplication function on the 4D total space*, unlike a nowhere-nonzero scalar map on the **base S²** bundles L_k→L_(k+1): the latter obstruction is respected, not contradicted. Near the TN nut, where √ρ is proportional to the smooth R⁴ radial coordinate, √ρ z_α extends as a complex Cartesian coordinate (modulo a smooth nonzero radial factor); exp(ρ/2) is smooth. This is a nonvanishing *pair* of coordinate components away from the nut, but each component has zeros; the map is not invertible and cannot be a scalar line-bundle isomorphism over S².

This construction **uses an already postulated auxiliary gauge field**; it does not derive that field from TN, nor does it identify n with the Lorentzian mass–NUT k without further physical work. Hasebe's supermonopole charge-changing ladder remains a separate supergroup operator with distinct coefficients.

## Gate 177 — full first-order radial intertwining identity, beyond a solution coincidence

Define the first-order radial differential expression
**D_n := ∂_ρ + (p_aux−n)/2 − (n−1)/(2ρ) + 1/[2(1+ρ)].**
The published radial equation (3.38) is D_n R_n=0. For b(ρ)=√ρ exp(ρ/2), the exact differential identity **D_(n+1) b = b D_n** holds on every differentiable radial test function on ρ>0, because b'/b=(1+1/ρ)/2 cancels the difference of their zeroth-order coefficients. This is a bona fide intertwining of the **separated first-order radial equations**, not a claim that B_α intertwines the *full* 4-component Dirac operator off the special holomorphic zero-mode subspaces. In particular [Dirac_p,B_α] need not vanish on arbitrary spinors, and B_α is not one of the conserved KY/Runge–Lenz symmetries.

## Gate 178 — explicit normalized spinorial ladder coefficients and non-universality

The normalized radial norm in measure ρ(1+ρ)dρ is
**I_n(p_aux)=Γ(n+1)/(p_aux−n)^(n+1)**.
In the normalized Haar S³ angular polynomial basis with monomials z₁^a z₂^b, a+b=n−1, multiplication by z₁ or z₂ has squared norm (a+1)/(n+1) or (b+1)/(n+1), respectively. Therefore the coefficients of B_α between **normalized** 4D zero modes are
**C_(n,a;1)=sqrt[(a+1)(p_aux−n)^(n+1)/(p_aux−n−1)^(n+2)]**,
**C_(n,b;2)=sqrt[(b+1)(p_aux−n)^(n+1)/(p_aux−n−1)^(n+2)]**,
for p_aux>n+1. These are exact model amplitudes for the **chosen operator B**, *not* physical transition rates or gauge couplings. They depend on the freely chosen p_aux, choice of operator normalization, and representation label; topology and p_G=k/4 do not fix them. The angular z-doublet's Clebsch factors ensure SU2 spin j=(n−1)/2 changes by +1/2 (not geometric j_G=n/4). The choice of α (or a test spinor polarisation) is an additional selection.

## Gate 179 — highest-mode domain obstruction and lack of physical promotion

The full 4D normalizable kernel at fixed p_aux has finitely many charge sectors n=1,...,N, where N is the largest integer strictly below p_aux. On the **highest** sector n=N, application of B_α produces radial decay exp[−(p_aux−N−1)ρ/2] with nonpositive exponent, so the function is not L². Hence the raw multiplication B_α is an **unbounded operator on the 4D L² space whose natural domain does not include the full Dirac kernel**; it is not an endomorphism of the finite-dimensional zero-mode Hilbert space. One may define an algebraic truncated ladder that kills the top sector, but this is a *new spectral projector/nonlocal boundary choice*, not the unchanged local multiplication operator or a conserved Dirac symmetry. Existence of these B_α on the admissible subspace is nevertheless a constructive positive zero-mode mapping. This removes the previous practical uncertainty that no explicit 4D n-changing map was known, while retaining the distinction between a solution generator and a full Dirac symmetry.

No physical fermion source or force term was constructed; the auxiliary gauge field remains freely normalised on topologically R⁴ Taub–NUT, and the Lorentzian mass–NUT pair p_G=k/4 and Cone C_geom are distinct observables. **No Newton G, no parameter-free new tidal ratio, and no experimental gravitational prediction** follows.

## Reproducibility, audit, next gate

Executed exact SymPy script `research-notes/tn_dirac_zero_mode_charge_generator_v15_654.py` (commit 787ef092c35f79fea6a8a00e27897258760a8e3f); companion archive `cone_tn_ladder_gates_176_179.zip` contains `cone_tn_ladder/reproduce.py` and REPORT.md. Tests explicitly differentiate D_n, verify D_(n+1) b=b D_n for arbitrary test function, check homogeneous polynomial raising and right-fiber charge increase, and derive squared norm coefficient formula. Paper source PDF was visually inspected, with journal eqs (3.37)–(3.47). No image generation and no protected Suzuki modification.

**HANDOFF:** independent external-audit, gravity, sandbox; verify ratio R_(n+1)/R_n, operator charge normalisation (spin-frame offset), global smooth extension of √ρ z_α across nut with TN near-nut coordinates, radial intertwining off-shell, normalized Haar S³ coefficient factors, and failure of B_α to map highest multiplet into L². Special scrutiny of the claim that B_α is globally smooth on TN despite z_α not being scalar on S². Distinguish a new direct consequence of known explicit zero modes from a preexisting literature theorem; do not call it a physical conserved supercharge. Retain prior certified work and cross-lane collision avoidance.

**Next gate:** compute [Dirac_p,B_α] on unrestricted spinors (nonzero derivative Clifford multiplication), test whether B_α can be extended to a **bounded** physical transition/current with specified local source and without spoiling exact kernel invariance; compare with dynamical symmetry/Howe duality and derive whether any source-normalized G-free dimensionless observable survives. If no, record precise no-go and pivot back to source-based cone dynamics.
