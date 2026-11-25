# Cone Derivation Ledger v15.1451 — Exact curved-H² sigma Noether stress identity, and why nonlinear wave corrections are required by Einstein Bianchi consistency

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [D EXACT PASS] independently derived and symbolically verified the identity between covariant sigma stress divergence and the target sigma Euler residual; [NEGATIVE] crossed leading sigma wave fields (v15.1409) produce nonzero fifth-order sigma residual and thus a nonzero stress divergence, so cannot be inserted as an exactly conserved stress in a complete Einstein solution without corrections; [OPEN] full Einstein–Maxwell–Weyl–H² stress and order-reduced EOM, exact coupled constraints/evolution, physical quarter selector. Strict additive. Parents v15.1409–1412 (crossed sigma leading and fifth-order corrections), v15.1450 (3+1 ADM constraints), Audit Round 638 independently verified full Weyl and external-work gates v15.1420–1422.

## Gate 1371 — exact Noether/Bianchi identity

The real curved H² sigma model has target coordinates `phi^A=(u,v)`, `G_AB(phi)=δ_AB−phi_A phi_B/(1+phi²)`, target Christoffels `Γ^A_BC=−phi^A G_BC` and kinetic Lagrangian `L_sigma=−f²r²/2 G_AB g^{μν}∂mu phi^A∂nu phi^B`. Its Euler operator `E^A=Box phi^A+Γ^A_BC ∂phi^B·∂phi^C=Box phi^A−phi^A G_BC∂phi^B·∂phi^C`. The stress tensor is `T_{μν}=f²r²[G_AB ∂mu phi^A∂nu phi^B−(g_{μν}/2)G_AB ∂phi^A·∂phi^B]`. Diffeomorphism/Noether covariance yields the **exact off-shell identity**

`∇mu T^mu_nu=f²r² G_AB E^A ∂nu phi^B`.

Thus stress-energy is separately conserved *on shell* E=0; off shell its divergence is an explicit residual, not automatically zero. The full Weyl–F–area coupled theory modifies both matter EOM and stress through curvature variations; this identity applies here only to **the uncoupled sigma action**. Full metric source must include EM and C F B contributions, with a full covariant Noether identity across all fields.

## Gate 1372 — independent exact symbolic verification on crossed null wave histories

Use 2+1 slice of flat 3+1 Minkowski (−++) with `A=t−x, B=t−y`, `u=a sin A, v=b sin B`. In null phase variables, `Box f=−2∂A∂B f` and `∂f·∂g=−(f_Ag_B+f_Bg_A)`. Independently form the exact stress T^mu_nu, its full spacetime divergence, and compare it for ν=t,x,y against `G_AB E^A ∂nu phi^B`. All three identities hold symbolically **without series expansion or numerical tolerance**.

The exact displayed divergences for kinetic f*r=1 and `D=1+a²sin²A+b²sin²B` are

`div T^mu_t=−2a²b² sinA sinB cosA cosB [a² sinA cosA+b² sinB cosB]/D²`,

`div T^mu_x=+2a⁴b² sin²A sinB cos²A cosB/D²`,

`div T^mu_y=+2a²b⁴ sinA sin²B cosA cos²B/D²`.

Nonzero terms start at total amplitude degree six in the stress divergence, because E starts at fifth order and is multiplied by a first-order scalar gradient. The earlier v15.1410 fifth-order sigma correction removes the E degree-five terms, suppressing divT accordingly; this exact code checks the uncorrected waves as a nonzero-counterexample and does not falsely claim to evolve a full corrected Einstein metric.

**Actually executed local SymPy** `/mnt/data/cone_gate/k4_h2_stress_bianchi_identity.py` all three exact identities PASS. **Additive canonical GitHub reproducer** `research-notes/k4_h2_sigma_stress_noether_v15_1451.py`, SHA **27a3db6cb251a0598a89e36c7a0d6ad6d5fd8304**, awaiting independent exact committed-byte replay.

**AUDIT:** independently verify stress signs using signature (−++), correct mixed-index position, exact target Christoffels and Noether formula, three rational trigonometric outputs, orders 5 vs 6, and avoid conflating uncoupled sigma conservation with the full C F B interacting Bianchi identity.

**NEXT:** derive the complete covariant metric variation of Weyl–F–area and associated matter Euler operators, check `∇ T_total=0` on coupled equations and Bianchi constraints, perform controlled EFT order reduction below cutoff, and only then test fully coupled 3+1 evolutions. No physical G-free interaction or quarter radius normalization emerges from these standard Noether identities.
