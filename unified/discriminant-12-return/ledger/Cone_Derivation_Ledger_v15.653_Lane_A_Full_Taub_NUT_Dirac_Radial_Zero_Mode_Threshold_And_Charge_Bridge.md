# Cone Derivation Ledger v15.653 — Gravity lane: four-dimensional Taub–NUT Dirac radial normalizability restricts the angular monopole-spinor bridge

**Date:** 2026-11-10. **Parents:** independently audited gravitational mass–NUT pair v14.731–732; true TN fiber winding v15.632; Hasebe charge-changing supermonopole comparator v15.646; standard Euclidean TN Dirac/Killing–Yano fiber conservation v15.647; positive global CP¹ scalar-to-spinor angular bridge v15.651; **External Audit Round 530 v15.652** (confirmed v15.651 and other mathematical gates). **Primary published source:** Rogelio Jante and Bernd J. Schroers, “Dirac operators on the Taub-NUT space, monopoles and SU(2) representations,” *JHEP* 01 (2014) 114, DOI 10.1007/JHEP01(2014)114, especially equations (1.2), (3.24–3.25), (3.34–3.45), (3.47). Full open-access PDF inspected visually on pp. 17–21 (journal-page labels). **Status:** [D] checked explicit radial differential equation, exact square-integrability threshold, zero-mode dimensions, parameter dependence; [C] proposed cross-model correspondence of CP¹ angular charge index to Euclidean TN right-fiber charge; [O] physical charge-changing 4D Dirac intertwiner, dynamics and coupling, odd-quarter *angular* Casimir, new G-free observable. **Fresh prewrite live HEAD:** 486ff068d8d2398cfa26e88b7eec8011948c9a9f (reproducer commit); v15.653 collision search empty. Additive-only; prior v15.633/640/642 collision records remain untouched, frozen Suzuki lane and physical quarter weld untouched.

## Critical notation separation

The published Jante–Schroers Dirac operator is on **Euclidean** self-dual Taub–NUT of radial length L, twisted by an **additional Abelian self-dual gauge connection** with continuous real charge parameter **p_aux** (their article writes simply p). This is NOT the independently derived Lorentzian mass–NUT **pair** p_G=μ c l/ℏ=k/4 of v14.731. Even the Euclidean fiber charge integer **n** below is not automatically the same physical quantity as the Lorentzian Misner-time mode k: correspondence requires separate theory. The additional connection is proportional to a continuous constant not fixed by the TN metric; the original untwisted Euclidean TN Dirac operator has **no normalizable zero modes** in the article's setting.

## Gate 172 — exact full radial differential equation and its solution

Use ρ=r/L>0 and V=1+1/ρ. The article's positive-charge radial mode with ordinary SU(2) spin j∈(1/2)Z≥0, eq. (3.38), satisfies

**R'_j+[ ((p_aux−1)/2−j) + (1/2−j)/ρ − 1/(2ρ(ρ+1)) ] R_j=0.**

The paper's eq. (3.39) gives

**R_j(ρ)=C ρ^j/(sqrt(1+ρ)) exp[−(p_aux−2j−1)ρ/2].**

Differentiating proves the ODE residual is identically zero. On the TN metric of eqs. (3.24–25), after integrating angles and suppressing positive constants, the radial volume element is proportional to **ρ(1+ρ)dρ**. The radial integrand is therefore proportional to ρ^(2j+1) exp[−δ_j ρ], δ_j:=p_aux−2j−1. For δ_j>0 it has exact integral **Γ(2j+2)/δ_j^(2j+2)**. For δ_j=0 it diverges polynomially and for δ_j<0 exponentially. Hence

**R_j ∈L²(TN) iff p_aux>2j+1** (positive p_aux sector).

No angular CP¹ bundle argument alone can override this radial requirement. It is a **physical input about the additional U(1)/R gauge field**, not a selection of Newton G.

## Gate 173 — exact integer mode census and strict threshold

Set **n=2j+1∈Z≥1**. The paper's lifted right-U(1) eigenvalue operator `N_hat=2i X_hat3` (eq. (3.47)) has the integer monopole/Chern charge n on positive solutions, and the SU2 multiplet has spin j=(n−1)/2, dimension n. Allowed n obey **n<p_aux strictly**. Let N be the number of positive integers strictly below p_aux; equivalently N=max(0,ceil(p_aux)−1) for p_aux>0. The dimension is

**dim ker D_(p_aux) =Σ_{n=1}^N n=N(N+1)/2**,

as in article (1.2), (3.45). For integer p_aux=m, the borderline n=m fails; e.g. p_aux=2 gives just n=1 (one zero mode), p_aux=3 gives n=1,2 (three), p_aux=3.5 gives n=1,2,3 (six). p_aux≤1 gives none in the positive branch; for p_aux<0 there is a conjugate opposite-chirality/sign branch with condition |p_aux|>2j+1. The stepwise dimension growth is an already-published standard Euclidean TN fact, not a new prediction.

## Gate 174 — lift of the CP¹ charge-one bridge is possible *as a target mode*, not as a derived operator

v15.651 constructs a global SU2-equivariant **angular** isomorphism between lowest scalar monopole charge-k states (spin j=k/2, dimension k+1) and twisted S² **chiral-spinor** Dirac zero modes with monopole charge k+1. The Jante–Schroers 4D TN zero-mode sector of lifted fiber/Chern charge **n=k+1** has exactly that spin j=k/2 and dimension k+1. Therefore the angular representation matches the 4D zero-mode angular sector, and the target radial mode is square-integrable **iff p_aux>k+1**. It can be extended as a *linear abstract map into the 4D kernel* by attaching this normalized radial profile, conditional on the chosen additional gauge field; no global 4D covariant differential raising operator or physical scalar→spinor interaction is thereby constructed.

If one instead wants a **4D-to-4D** charge ladder between n=k+1 and n=k+2 inside the **same** p_aux-twisted Dirac zero-mode space, both modes exist only if **p_aux>k+2**. Their ordinary spins are j=k/2 and j'=(k+1)/2, so an ordinary rotational *scalar* cannot connect them, while a spinorial tensor is representation-theoretically possible. The original geometrically invariant Dirac/Killing–Yano symmetry operators preserve N_hat and are not such n-changing sources. These two bridges (2D scalar→4D spinor at fixed j versus 4D spinor n→n+1 at changed j) must not be conflated.

## Gate 175 — radial overlaps are parameter-dependent and not physical transition matrix elements

At fixed p_aux>n the radial *shape* functions normalized in the measure ρ(1+ρ)dρ are

**\hat R_n(ρ)=[(p_aux−n)^(n+1)/Γ(n+1)]^(1/2) · ρ^((n−1)/2)/(sqrt(1+ρ)) · exp[−(p_aux−n)ρ/2].**

Their scalar radial overlap, for n,m allowed, is

**I_nm(p_aux)=Γ((n+m)/2+1) sqrt[(p_aux−n)^(n+1)(p_aux−m)^(m+1)/(Γ(n+1)Γ(m+1))]/[((2p_aux−n−m)/2)^((n+m)/2+1)].**

For n=1,m=2: **I_12(3)=2sqrt(3π)/9** but **I_12(4)=18sqrt(10π)/125**; nonuniversal despite fixed topology. Critically, these are *radial shape overlaps*, **not** physical matrix elements between different full 4D angular modes. The latter would require a specified n-changing operator with nontrivial angular/spinorial transformation; a scalar angular inner product between distinct SU2 irreps vanishes. The radial calculation shows that the angular bundle isometry cannot alone fix a physical transition coefficient.

## Disposition and reproducibility

**Verified positive:** the correct S² charge-one scalar→spinor angular representation occurs among **normalizable 4D Euclidean TN Dirac zero modes**, provided **p_aux>k+1**. This is a conditional embedding with fully explicit radial profile, not merely formal topological permission. **Verified negative:** untwisted 4D TN has no such L² Dirac kernel; an independent continuous self-dual Abelian gauge charge controls existence; no full 4D n-changing operator or universal amplitude is induced. The Lorentzian mass–NUT gravitational pair p_G=k/4 and the q=2 geometric odd-quarter Casimir C_geom=k(k+4)/16 are not identified with this Euclidean radial theory. No G or Cone-novel dimensionless gravitational observable is derived.

Source equations independently checked via exact SymPy and reproduced in `research-notes/taub_nut_radial_normalizability_v15_653.py`, committed at 486ff068d8d2398cfa26e88b7eec8011948c9a9f. Companion conversation artifact `cone_tn_radial_gates_172_175.zip` contains the executed producer and REPORT.md, including strict threshold examples and radial overlaps. No images generated; frozen production untouched.

**HANDOFF:** external-audit, gravity, sandbox. Independently verify paper eqs. (3.38–3.40), 4D radial volume factor, Γ normalization, strict cutoff (not ≤), identity of Euclidean right-fiber n=2j+1 versus Lorentzian k being *conditional*, and the continuous additional gauge strength p_aux being separate from physical p_G. Check the distinction between the scalar angular bridge, 4D zero-mode existence and actual 4D n-changing operator; ensure radial overlaps are not promoted to measurable transitions. Preserve Suzuki certified data and historical numbering records.

**Next gate:** test whether any *published, covariant 4D differential operator with a prescribed auxiliary-gauge dependence* acts as an n-changing (not commuting) map between normalized 4D TN Dirac zero modes. Test its right-U(1) weight, SU2 spinorial tensor rank, radial intertwinement and whether the coupling is determined without specifying p_aux. If absent, document the no-derived-operator result and return to physical dimensionless cone observables rather than assuming supersymmetry.
