# Cone Derivation Ledger v15.995 — Exact K4 TT–Maxwell cavity mode projection: open q2 boundary source at graviton-exchange order

**Date:** 2026-11-14 US Eastern. **Gravity lane.** **Owner request:** continue v15.993's higher-order source search from the actual K4+Maxwell action, testing the open-quarter two-action-circle boundary operator rather than assuming a quartic interaction.

**Status:** [D] exact first-order TT metric–Maxwell vertex on the already used fixed-wall 1D y-polarized photon model; [D] exact spatial Fourier selection and zero of desired quartic term at single TT propagator exchange with diagonal spatial modes; [C] K4 tensor propagator from frozen local homogeneous quadratic action and formal single-exchange elimination; [N] no physically selected open-q2 T source, all-shell vertex weight, or G-independent observable; [O] fully nonlinear K4 graviton self-interaction, mode mixing/finite material boundaries, all polarizations and gauge-complete constraints.

**Parents / redundancy:** v15.602 original-unit projected q2 T†T=2E; v15.628 q2 grading; v15.695 true reduced curved Maxwell action L_EM=1/2 exp(2b)[(A_ydot)²−(∂z A_y)²] with metric ds²=−dt²+e^{2b}dx²+e^{−2b}dy²+dz² (historical script repaired v15.701); v14.928/935 physical Einstein–K4 elastic-solid quadratic tensor action; v15.679 propagating tensor metric source and Maxwell polarization; v15.991 open boundary bridge; v15.992 selection demands ΔN=2, Δm_phys=±2 on a chosen auxiliary two-mode carrier; v15.993 shows minimal O4=(a1†)^3 a3 requires shell-dependent coefficient 1/[2sqrt(L(L+2))]. **Audit Round 584**, canonical v15.994 commit f4294536e796d0a2e2424ca51c127f85ba94c521, independently verified v15.991–993, no corrections. **Live HEAD immediately prewrite:** fe20a4443ee7d2968046c7d6a65a046b301cdfb0 (new exact reproducer). Target path verified absent, additive-only; frozen Suzuki, prior certified entries, Audit, Muse and Sandbox unchanged.

## Gate 822 — derive physical cubic source rather than propose a bare A^4 interaction

Use exactly the v15.695 reduced curved Maxwell action, restricted to one y polarization of a perfect-wall 1D cavity z∈[0,π] and transversely unit area:

**L_EM=1/2 ∫_0^π dz exp(2b(t,z))[(∂t A_y)²−(∂z A_y)²].**

The linear metric term is **L_int=∫ b[(A_ydot)²−(A_y')²] dz**, derived by Taylor expansion, not a fitted coupling. Set b(t,z)=b_k(t) cos(kz), A_y(t,z)=q1(t) sqrt(2/π)sin z+q3(t)sqrt(2/π)sin(3z). In the units where photon modes have frequencies ω1=1 and ω3=3, the free Lagrangian is 1/2(pdot q)²−1/2(q1²+9q3²).

Define exact overlap matrices **C_(ij,k)=∫ cos(kz)e_i e_j dz**, **D_(ij,k)=∫ cos(kz)e_i' e_j' dz** for i,j∈{1,3}. The full first-order metric interaction is **L_int=b_k[dot q^T C_k dot q−q^T D_k q]**. After the Legendre transform, at linear order in b the canonical Hamiltonian interaction is **H_int=b_k V_k**, with **V_k=−p^T C_k p+q^T D_k q**. A kinetic-coordinate perturbation is not simply plus the Lagrangian source, and the sign is tracked explicitly.

Quantize the photon canonical oscillators in the standard way, q_m=(a_m+a_m†)/sqrt(2ω_m), p_m=−i sqrt(ω_m/2)(a_m−a_m†), ℏ=1 for these matrix elements. The exact projections include:

- k=0: C=diag(1,1), D=diag(1,9), and **V_0=a1²+(a1†)²+3a3²+3(a3†)²** (normal-ordered symbol), a squeezing vertex with no intermode conversion.
- k=2: **C=[[-1/2,1/2],[1/2,0]]**, **D=[[1/2,3/2],[3/2,0]]**; **V_2=(N1+1/2)+sqrt(3)[a1 a3+a1† a3†]** after proper normal-ordering. The reproduced commuting-symbol expression contains a1 a1†, differing only by the standard ordering constant. This vertex preserves **N1−N3** and hence cannot realize the target Δn1=+3, Δn3=−1, which changes that difference by four.
- k=4: **V_4=sqrt(3)[a1 a3†+a1† a3]**, genuine intermode conversion but no a1†² squeezing.
- k=6: **V_6=3(N3+1/2)**, number term of mode 3; its normal-order constant does not affect selection.

Other integer metric Fourier wavenumbers 0≤k≤10 give no new single-k pattern. These *sourced* quadratic vertices are nontrivial, but the one required quartic operator is absent at the level tested next.

## Gate 823 — a dynamical tensor can mediate four-photon interactions, but diagonal k-exchange cannot make this O4

For each k, the top-degree normal-ordered coefficient of **O4=(a1†)^3 a3** in the product V_k V_k is exactly

**coeff_O4(V_k²)=2 coeff_(a1†²)(V_k) coeff_(a1†a3)(V_k).**

The reproduced overlap integrals show: at k=0 the first factor is 1 but the second zero; at k=4 the second is sqrt(3) but the first zero; all other k yield at least one zero. Thus **coeff_O4(V_k²)=0**, for all spatial Fourier modes in this truncated cavity.

The *actual* frozen K4 TT quadratic action in homogeneous FLRW (v14.928/935) is proportional to

**S_T²=(M_Pl²/8)∫a³[dot γ_ij²−(∂γ_ij)²/a²−m_T²γ_ij²]**, with m_T²=(8η/3)H². For plus polarization γ_xx=2b, γ_yy=−2b, trγ²=8b², so the b quadratic action is proportional to **M_Pl²∫a³[dot b²−(∂b)²/a²−m_T² b²]**. On the spatially homogeneous background its *linear tensor propagator is diagonal in its spatial Fourier modes*. Integrating out a tensor mode at leading tree exchange produces terms of schematic form V_k D_k V_k (with time-dependent and normalization kernels). Since the target operator is absent in every such V_k product, **the leading Fourier-diagonal tensor-exchange contribution to O4 vanishes in this specified two-photon/one-polarization model**.

This is a stronger and more specific result than the earlier statement that Maxwell is quadratic at fixed metric. Dynamical metric exchange *does* create effective quartic photon interactions in general; our specific required quartic term vanishes after the real mode projection and tensor-momentum selection. It does NOT prove the full, nonlinear K4+Maxwell action has no such interaction at higher order, or that different geometries, 3D modes and boundary conditions cannot supply it. In particular, the approximation of a local instantaneous V_k²/Ω_k² is only a static/adiabatic illustration, not generally valid for a light or resonant tensor; the zero selection conclusion instead follows for arbitrary time-nonlocal diagonal D_k because the same per-k vertices lack the necessary operator composition.

## Gate 824 — an exact *possible* off-diagonal mechanism, not presently sourced

If one independently supplied a mixed propagator D_(0,4) or an inhomogeneous background connecting tensor spatial harmonics k=0 and k=4, the cross product V_0V_4+V_4V_0 has a nonzero top-degree **O4** coefficient **2sqrt(3)** before propagator/kinetic normalization. This is an algebraic witness that the desired occupation change is *not* universally forbidden; it is absent in the current Fourier-diagonal K4 tensor comparator. That mixed-k kernel cannot be silently added to the frozen homogeneous K4 action as an established physical interaction. A full nonlinear tensor self-interaction, spatially structured metric source or real material boundary could in principle alter mode mixing, but must be derived and constraint checked.

Even if such a mixing source is found, the original all-shell requirement persists: the bare O4 matrix element is sqrt[L(L+1)(L+2)], whereas the open q2 boundary T has sqrt[(L+1)/4]. Matching every shell would require an additional physical operator normalization proportional to 1/[2sqrt(L(L+2))], not a single constant coupling. Furthermore, M_Pl² tensor normalization contains Newton G, and the independently open K4 elastic parameter η/background H cannot simply be inserted as a parameter-free new gravitational prediction.

## Gate 825 — reproducibility, scope, next discriminant

**Reproducer:** `research-notes/k4_open_quarter_ttpair_source_v15_995.py`, additive commit **fe20a4443ee7d2968046c7d6a65a046b301cdfb0**. Verified locally with exact SymPy integrals/oscillator polynomial algebra: modes k=0..10, the explicit C,D and V matrices for k=0,2,4,6, missing O4 coefficient in V_k², nonzero 0–4 mixed-harmonic cross coefficient and all-shell T/O4 weight mismatch. **PASS.** Symbolic a and a† are treated as commuting solely when extracting highest-degree normal-ordered coefficients; quantum contractions lower operator degree and cannot manufacture the degree-four O4 coefficient. Independent Audit pending.

**Positive:** The actual physical Maxwell vertex and K4 tensor wave kinetic term together provide a controlled **nonlinear photon–tensor–photon exchange mechanism**, and spatial harmonics distinguish squeezing from number-conserving conversion. The zero in this mode selection is exact, not a numerical smallness. A mixed spatial harmonic source could give an O4 amplitude if it were physically present.

**Negative:** No sourced activation of the open quarter two-circle boundary T arises through the tested homogeneous quadratic-TT propagator and linear Maxwell vertex for these 1D modes. This is a scoped model restriction, not a no-go for all nonlinear K4. We have not selected a new frequency, coupling normalization, or G-independent gravitational observable; the geometrical boundary weight still requires a physical operator identification.

**Next:** inspect whether the *actual* K4 cubic TT self-interaction or constraint-reduced scalar/tensor mixing generates a physically justified off-diagonal spatial harmonic kernel in the same cavity, including gauge-invariant photon boundary conditions. Explicitly test tensor spatial selection and source conservation before calculating an induced O4. If translational homogeneity keeps the tensor kernel Fourier diagonal, investigate genuinely inhomogeneous localized matter or controlled boundaries rather than assuming a propagator defect.

**HANDOFF Audit/Muse:** independently derive standing-wave integrals, check Legendre transform signs and normal-order constant, [V2,N1−N3]=0, 0–4 mixed source coefficient, and TT normalization from γxx=2b. Confirm that the zero applies only to the specified leading single-tensor exchange, not all K4 orders or all photon geometries.
