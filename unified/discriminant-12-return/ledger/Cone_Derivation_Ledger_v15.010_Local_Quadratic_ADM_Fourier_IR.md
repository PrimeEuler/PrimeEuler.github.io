# Cone Derivation Ledger v15.010 — Local quadratic ADM momentum and Fourier IR source

Date 2026-10-27. Parent gravity v15.003/005/007. Parallel Muse v15.008/009 on means-conics left untouched. Research note research-notes/K4_Local_Second_Order_ADM_Fourier_Momentum_Constraint.md at commit 766c467b9dac0f4460a89639265acb3edac6c452. HEAD immediately before write 766c467b9dac0f4460a89639265acb3edac6c452. No protected lanes touched; Suzuki physical quarter weld parked.

[D] Exact canonical H_i=−2∂k(hijΠjk)+Πjk∂i hjk+pI∂iφI=0. For homogeneous h0,Π0 and φ0I=zi, p0=0, expand fields X=X0+X1+X2 with no 1/2 factor. Local second-order equation:
 H_i2=−2∂k(h0ijΠ2jk+h1ijΠ1jk+h2ijΠ0jk)+Π0jk∂i h2jk+Π1jk∂i h1jk+p_i2+pI1∂iπ1I=0.
The quadratic matter p_i2 includes *both* genuine second-order mode terms (2C/3)a³(dotπ_i2−β_i2) and first-order products (2C/3)a³[(trε/2−α)(dotπ_i1−β_i1)−β1j∂jπ_i1]. Splitting p_i2 correctly gives an explicit Fourier bilinear source and second-order linear constraint operator. The divergence products carry output iK, but Π1∂h1,p1∂π1 and bilinear p2 contain internal input momenta and are not automatically O(K) or O(K²). Under periodic or vanishing-flux boundaries spatial integration reproduces v15.007 exact zero-mode global condition.

[SCOPE] Exact second-order local MOMENTUM equation, not complete lapse/shift elimination: one must also include Hamiltonian constraint, fixing gauges and zero modes. K=0 global solvability does not guarantee uniform inverse-operator estimates for arbitrarily small nonzero K. No IR divergence, nonlinear future stability or charge selection proven.

Flags: full_local_second_order_momentum_identity=DERIVED; quadratic_p2_products=INCLUDED; Fourier_output_K_divisibility=NOT_AUTOMATIC; global_K_zero_balance=RECOVERED; coupled_hamiltonian_and_momentum_inversion=OPEN; nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: local-quadratic-ADM-Fourier-IR
parent: v15.010
status: open
action: Verify index-density and Fourier split including bilinear p2, check global zero-mode reduction, and require full Hamiltonian+momentum gauge-fixed inversion before any uniform IR bound.
deliverable: scoped verdict.

NEXT: construct full second-order Hamiltonian constraint and coupled regular-gauge linear constraint operator acting on degree-two modes; test actual invertibility and low-K estimates. Preserve v14.996 full-metric action lessons.
