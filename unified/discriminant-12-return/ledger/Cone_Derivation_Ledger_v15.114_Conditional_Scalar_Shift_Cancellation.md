# Cone Derivation Ledger v15.114 — Conditional on-shell scalar shift cancellation; original EL residuals pending

Date 2026-10-29. Gravity parent v15.111 and External Audit Round 402 v15.112 (verified previous quadratic ADM gates); Lane A v15.113 protected. Research note research-notes/K4_Conditional_OnShell_Scalar_Shift_Cancellation.md commit b2d09bf7c98a13e251f2f9471577afd36a0c3fab. Prewrite HEAD checked; add-only ledger.
[D, CONDITIONAL] Translate v15.038 linear ADM constraint convention ψ_old to source-faithful ψ_source=−ψ_old in conformal gauge h_ij=a²(1−2ψ_source)δij. With p=Δσ, k²>0, S=dotσ−b=−3Hψ_source−(pdot+Hp)/(1+k²) and α=−dotψ_source/H+S/(3H). Insert externally certified ψ_source=[−k²p+τpdot]/[3k²(1+k²)] and oscillator pdd+3pdot/τ+(3k²+4)p/τ²=0. Exact symbolic simplification yields S=−pdot/k², hence b=0 and α=[(3k²+4)p+τpdot]/[3k²(1+k²)]. Substitution into source-sign wave ∂τ[a³(dotσ−b)]−a(p+α−ψ_source)=0 yields 0 on oscillator.
[VERIFICATION BOUNDARY] This verifies INTERNAL algebra and wave compatibility conditional on transformed v15.038 constraints. It does not certify original v14.996 source-action Euler equations EL_B, EL_Phi; those outputs were not run this turn. Thus source-corrected auxiliary coefficients=OPEN, b=0=CANDIDATE, physical H2_on_shell=OPEN, second-order_solvability=OPEN. Potential IR 1/k² lapse and ψdot must be assessed within full constrained H2. No nonlinear future stability claim. k=0 excluded, Suzuki quarter weld PARKED, concurrent lanes untouched.
HANDOFF
target: sandbox, external-audit
type: source-faithful-auxiliary-crosscheck
parent: v15.114
status: open
action: Run v14.996 scalar_final2.py, extract solB and PhiS on solpsi and solpsid, original EL_B,EL_Phi,E1,E2 residuals; compare B=0 and alpha candidate exactly. If verified, evaluate exact quadratic source H2 on conjugate physical scalar modes incl infrared output zero.
deliverable: source-action coefficient certificate or exact mismatch.
