# Cone Derivation Ledger v15.713 — Gravity: sourced K4 scalar Ward-like constraint, exact forced mode, and archived state-space reproducibility alert

**Date:** 2026-11-11, US Eastern. **Parents:** v14.928 K4 EH+solid; **v14.935 original frozen SVT payload**, particularly matter_sector.py, eh_scalar.py, assemble.py and scalar_statespace.py; v15.706 homogeneous three-sector local dispersion; v15.711 exact scalar ADM auxiliary Hessian; v15.712 full source-first scalar mixed action reconstruction. **Status:** [D] exact time-dependent sourced scalar Euler–Lagrange equations in the archived K4 cos-Fourier convention; [D] original scalar mode frequency/friction remains correct when derived directly from the physical P equation; **[AUDIT ALERT]** original scalar_statespace.py's psi=alpha P reduction uses 0/0 for the reconstructed on-shell scalar EH/matter action; [C] independent physical covariant conservation meaning of formal source compatibility; [O] physical coasting FLRW source and detector transfer. **Immediately prewrite live HEAD:** e0d9621e6d77a8d17786aee4b4744543aa6a3c16; target v15.713 ledger path absent. Strictly additive, preserved all original v14.935 scripts and Suzuki/far-tail frozen objects.

## Gate 309 — DO NOT freeze background coefficients before Euler–Lagrange variation

From the actual archived scalar EH+solid quadratic actions regenerated in v15.712, add the formal ADM lapse/shift sources **J_Phi(tau) Phi+J_B(tau) B** before eliminating those nondynamical auxiliaries. Their algebraic Schur complement is

**L_red = L_0 - (1/2)[d(psi,P)+J]^T H^(-1)[d(psi,P)+J]**.

Substitute the exact coasting background **a(tau)=tau/sqrt(3), adot=1/sqrt(3), kappa C=1** into the *time-dependent reduced action*, then vary psi(tau) and P(tau) with all background time derivatives retained. This is the sequencing stipulated in v14.935 scalar_statespace.py, and is essential to reproduce its friction term. Work at **k>0**, because the k=0 scalar constraint block is singular.

A fully independent source-free run of the original assembly machinery also reproduces the original scalar kinetic coefficient. The source-free psi equation is examined below separately from the propagating P equation.

## Gate 310 — the sourced psi Euler equation is a source-compatibility identity, not psi=alpha P

The exact psi Euler–Lagrange expression simplifies to

**E_psi = -tau dJ_Phi/dtau - sqrt(3) J_B**.

Therefore consistent formal sources in this archived gauge/action convention satisfy

**tau J_Phi_dot + sqrt(3) J_B = 0**.

No psi or P appears in this equation. In the source-free system **E_psi=0 identically**. This is a Ward-like *source compatibility* relation of the constrained reduced action. It is NOT yet proved to equal the covariant FLRW equation nabla_mu T^(mu nu)=0 for an explicitly normalized physical stress perturbation, whose density/pressure/source action must still be supplied.

**Reproducibility alarm for v14.935:** the archived scalar_statespace.py attempts to infer **psi=alpha P**, setting **alpha=-C01/C00**, where C00 is the coefficient of psi and C01 of P in the psi Euler equation. The independently regenerated **source-free** scalar action gives **C00=C01=0** for all k at the exact coasting background. Re-running the original freeze/coefficient-extraction logic at sample eta=3/4 and k_phys/H=10 gives e1=0 and a Python **0/0 division**. This is an actual discrepancy between the original code's claimed elimination method and the mathematical source-free action, not a mere SymPy structural-equality issue.

This finding requires independent audit **of the actual original archived scripts and runtime** before formally revising the certified v14.935 method statement. No historical source or ledger file was altered. Crucially, it does not yet show the scalar *dispersion itself* wrong.

## Gate 311 — independent physical scalar P mode equation reproduces the archived frequency

After varying the *time-dependent* sourced reduced action, the P Euler equation has the exact form

**A_P P_ddot + B_P P_dot + C_P P + F_J=0**,

with

**A_P=2 sqrt(3) k^4 tau^3/[27(1+k²)]**,

**B_P/A_P=3/tau**,

**C_P/A_P=[8 eta(1+k²)-3k²]/[3 tau²]**,

and the source forcing (before applying compatibility)

**F_J=[k² tau J_Phi_dot+sqrt(3)k² J_B+sqrt(3)tau J_B_dot+sqrt(3)J_B]/[3(1+k²)]**.

The source-free equation is therefore

**P_ddot+(3/tau)P_dot + [8 eta(1+k²)-3k²]/(3 tau²) P=0**.

Rewrite using **H=1/tau, a=tau/sqrt(3), k_phys=k/a**:

**omega_S² = (8 eta/3)H² + (-1/3+8 eta/9)k_phys²**.

This EXACTLY reproduces the v14.935 reported scalar frequency and friction directly from the propagating physical P equation, without the unworkable psi=alpha P step. The existing scalar local stability/gradient threshold 3/8 is therefore not invalidated by this calculation. The finding concerns the archived derivation's *auxiliary elimination and claimed reproducibility*, not a refutation of this closed-form scalar mode equation.

## Gate 312 — source-compatible inhomogeneous scalar mode equation

Impose **J_Phi_dot=-sqrt(3) J_B/tau** on the forcing, as required by the psi Euler relation. Then

**F_J = sqrt(3)(tau J_B_dot+J_B)/[3(1+k²)]**.

Dividing by A_P gives the exact sourced scalar evolution equation

**P_ddot + (3/tau)P_dot
 + [8 eta(1+k²)-3k²]/(3 tau²) P
 = -9(tau J_B_dot+J_B)/(2 k⁴ tau³)**,

**for k>0**, on exact coasting K4 and in the formal ADM source/cos-Fourier normalization of the original archived action. This is the first **time-dependent sourced propagating scalar** equation in the gravity-lane return, obtained from the original EH+solid action rather than a chosen scalar oscillator.

A specified J_B(tau) is sufficient to express the forcing after source compatibility, but no physical source amplitude or measurable gravitational tidal transfer is selected. The strong k^-4 factor reflects the scalar constraint normalization at k>0 and cannot be extrapolated to k=0. A physical stress must solve the true covariant background conservation and have a definite tensor coupling before interpreting this right-hand side as a laboratory or astrophysical forcing.

## Gate 313 — precise update of the K4 frontier

**Positive:** exact single-source/vector constrained pole (v15.710), sourced scalar auxiliary response (v15.711), source-mixed action (v15.712), and now full time-dependent forced scalar P evolution (this gate).

**Important correction requiring audit:** v14.935's scalar_statespace.py psi-slaving coefficient is zero-over-zero in faithful EH+matter reconstruction. Independently derived P dynamics retain the reported scalar dispersion; audit should repair the *method and reproducer* additively without erasing the historical source.

**Still open:** reconstruct full gauge-invariant curvature response and the source-dependent lapse/shift with a **physically realized covariantly conserved external stress**, then compute tensor/vector/scalar pole residues and conditional triple-channel readout. The exact eta-independent squared-frequency-gap ratio 3 remains a conventional isotropic-relativistic-elasticity relation (v15.706), not uniquely Cone.

**Reproducibility:** research-notes/k4_sourced_scalar_ward_v15_713.py, additive commit e0d9621e6d77a8d17786aee4b4744543aa6a3c16, invokes the additive v15.712 full-archive reassembler and tests the exact time-dependent psi and P Euler–Lagrange identities, coefficient ratios, complete forcing, source consistency and zero-source psi identity using safe symbolic simplification. Locally run PASS. Independently recreated original v14.935 scalar_statespace.py coefficient extraction shows C00=C01=0 and a 0/0 at its alleged psi=alpha P line. No figures, no protected file edits.

**HANDOFF — priority external audit:** reproduce the original v14.935 matter_sector.py, eh_scalar.py, assemble.py, scalar_statespace.py chain **from original bytes**, establish whether the archived scalar_statespace.py really fails for the original source-free action (do not rely on the newly derived code alone), check the physical P ODE and the sourced compatibility condition, and state clearly which v14.935 claims stay valid and which method/reproducibility statements require an additive correction. Also check whether this constraint identity is the proper linearized FLRW stress-energy conservation Ward identity in the stated Fourier gauge. Do not touch frozen Suzuki artifacts.

**NEXT:** a true covariantly conserved stress source and metric Fermi readout, only after the scalar state-space audit; reject any premature unique gravitational signal inference from the mathematical source coefficients.
