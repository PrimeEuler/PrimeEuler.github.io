# Cone Derivation Ledger v15.1386 — Nonlinear H² sigma-model kinetic geometry and sourced Euler–Lagrange equations

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Parents:** v15.1380–1382 geometry, v15.1384 Audit sign correction, v15.1385 Maxwell source+transverse response. **Status:** [D/PASS] two independent positive kinetic modes for the continuous positive-sheet H² target and exact Levi-Civita sigma model; [D] formally coupled Maxwell/sigma Euler–Lagrange field equations from the specified chosen EFT interaction; [NEGATIVE] positive uncoupled sigma kinetic does not guarantee no ghosts/ill-posedness of curvature-coupled full metric system; [OPEN] total stress tensor and its covariant Bianchi conservation, cutoff analysis, nonlinear initial value evolution, unique quarter-grid selector and calibrated detector. **Preledger source commit** da13201fc30d7cff9ab1352c2f0508dde66f2f03. Additive-only.

## Gate 1297 — exact induced target metric and positive kinetic eigenvalues

Let `n(u,v)=r(sqrt(1+u²+v²),u,v)` with `r=1/4` on `T²−X²−Y²=r²`. The normalized induced metric `G_AB(u,v)=r^(−2) (partial_A n)·(partial_B n)` is

`G_AB=δ_AB−phi_A phi_B/(1+u²+v²)`, `phi=(u,v)`.

Its exact determinant is `det G=1/(1+u²+v²)>0`, inverse `G^AB=δ^AB+phi^A phi^B`, and eigenvalues **1** (angular) and **1/(1+u²+v²)** (radial), positive for finite real u,v. The Christoffel symbols simplify EXACTLY to `Gamma^A_BC=−phi^A G_BC`. Consequently the isolated sigma kinetic action

`S_sigma=−(f²/2)∫ sqrt(−g) G_AB g^{mu nu} ∂mu phi^A ∂nu phi^B`

with f²>0 has the positive free/background Hamiltonian energy density

`rho_sigma=f²/2 G_AB(dot phi^A dot phi^B+sum_i∂i phi^A∂i phi^B)`.

Its exact curved-spacetime Euler–Lagrange equations, with no Weyl coupling, are

`Box phi^A−phi^A G_BC ∇mu phi^B ∇^mu phi^C=0`.

The two traveling null target waves of v15.1382/1385 satisfy the **linear** part `Box u=Box v=0`, while their nonlinear sigma corrections begin at cubic order in small u,v. The background sigma stress enters Einstein's equation at O(f²a²), O(f²b²); the previously used vacuum TT background plus prescribed sigma waves is therefore an explicitly **perturbative fixed-background probe**, not the full sourced Einstein solution.

## Gate 1298 — exact formal coupled sigma/Maxwell equations and their scope

Denote the normalized target area form `Omega_AB=epsilon_AB/sqrt(1+u²+v²)` and `B_mu nu=Omega_AB ∇mu phi^A ∇nu phi^B`. Define the curved-spacetime Weyl-coupled action addition

`L_int=−(g/2) C_mu nu rho sigma F^{mu nu} B^{rho sigma}`, `g=zeta/Lambda²`.

Maxwell variation yields

`∇mu[F^{mu nu}+g C^{mu nu rho sigma}B_rho sigma]=J_external^nu`.

Define `W^{rho sigma}=C_mu nu{}^{rho sigma}F^{mu nu}`. Since Omega is the closed target area form, a variation of its pullback obeys exactly `δB=d(i_{δphi} B)`. After integrating by parts, variation with respect to each internal scalar gives

`f² G_AB [Box phi^B+Gamma^B_CD ∇phi^C·∇phi^D] +g Omega_AB (∇nu phi^B) ∇mu W^{mu nu}=0`.

This is the **formal Euler–Lagrange equation of the chosen action** for independent continuous target fields; it does not derive the action from the discrete quarter mesh. Its interacting principal symbol depends on F, Weyl curvature and their derivatives, which have not been analyzed for hyperbolicity/extra degrees of freedom. The interaction contains spacetime Weyl curvature (second metric derivatives), so the *full metric variation*, background constraints and EFT cutoff must be included before claiming stability or a consistent nonlinear four-metric initial value problem.

In the v15.1385 leading test, the initial electromagnetic perturbation is zero and is induced at O(g epsilon a b); the new sigma-field forcing proportional to `g W` arises at higher order in g once this EM field is generated. However the two sigma waves' ordinary stress-energy remains present at O(f²a²,f²b²) and must be incorporated or made consistently negligible in any physical full metric calculation.

## Gate 1299 — reproducibility, Audit and next physical gate

**Actually executed local exact SymPy check:** `/mnt/data/cone_gate/quarter_h2_sigma_kinetic_v15_1386.py`, determinant, inverse, all eight connection components and eigenvalue characterization PASS. **GitHub additive reproducer:** `research-notes/k4_quarter_h2_sigma_kinetic_v15_1386.py`, commit **da13201fc30d7cff9ab1352c2f0508dde66f2f03**; awaiting external committed-byte replay.

**Audit handoff:** independently vary the sigma kinetic and curvature-dependent target area term, especially the sign and antisymmetric 1/2 normalizations of `Omega_AB ∂phi ∇W`; check positive kinetic eigenvalues and that the traveling-wave backgrounds are only *leading-order* solutions. Review whether the chosen curvature operator is redundant under more general EFT field redefinitions, the possible higher-time-derivative metric equation, ghost/characteristic bounds for small g/Lambda² and under what controlled approximation the fixed-background v15.1385 EM response is valid.

**NEXT:** perturbatively integrate the two coupled Maxwell/sigma equations on the already-Audited Maxwell–K4 tidal background with a genuinely localized finite-energy sigma Cauchy packet and its stress tensor; derive the metric variation of the Weyl interaction, verify the complete covariant Ward/Bianchi identities, and calculate a gauge-controlled optical detector response. Always compare both to original Einstein+same K4 AND a **matched identical enlarged EFT**. A nonzero effect from a freely chosen extra field and coupling is not a unique quarter-grid gravitational prediction; radius r=1/4 still cancels from normalized Omega.
