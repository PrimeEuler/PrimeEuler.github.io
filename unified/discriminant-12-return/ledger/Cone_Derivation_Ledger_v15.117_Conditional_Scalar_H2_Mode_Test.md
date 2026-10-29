# Cone Derivation Ledger v15.117 — Conditional constrained scalar single-mode Hamiltonian zero mode

Date 2026-10-29. Gravity parent v15.114; read External Audit Round 402 v15.112. Latest Lane A v15.116 protected. Research note research-notes/K4_Conditional_OnShell_Conjugate_Mode_Quadratic_Hamiltonian.md commit 4a6f3d30f62cd5ef7f909ea288787fe91ba80503.

[D, CONDITIONAL] For one real scalar mode in corrected source gauge, ψ_k=[−k²p+t pdot]/[3k²(1+k²)] and pdd+3pdot/t+(3k²+4)p/t²=0. Candidate translated-constraint b=0 and α_k=[(3k²+4)p+t pdot]/[3k²(1+k²)] satisfy directly checked source-sign linear Hamiltonian α=−(1+k²)ψ−tψdot−p/3 and corrected scalar-wave identity. Original v14.996 source EL_B/EL_Phi coefficients still NOT independently executed or certified; candidate b=0 NOT PROMOTED.

[D, CONDITIONAL] Substitution into complete quadratic Hamiltonian source v15.107 and spatially averaging a single conjugate ±k real mode gives
<H2>=−[t²pdot²(k^6+k^4+2k²−3)+tp pdot(4k^4+6k²−8)+p²(3k^8+7k^6+15k^4+16k²)]/[3k^4t²(1+k²)²].
For pdot=0 this grows −16p²/(3k²t²) as k→0, whereas p=0 yields +pdot²/k^4; only a mode-family diagnostic, not physical nonlinear instability or a statement on admissible function spaces. This result is dependent on the candidate auxiliaries, and must be retracted/updated if original source EL fails. Other second-order homogeneous fields H1[U2] are not included.

Flags: original_EL_B_EL_Phi=UNEXECUTED; candidate_B_zero=CONDITIONAL; candidate_alpha=CONDITIONAL; scalar_H2_single_mode=CONDITIONAL_SYMBOLIC; quadratic_IR_zero_mode=NOT_CERTIFIED_PHYSICAL; full_second_order_solvability=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: sandbox, external-audit
type: action-native-auxiliary-and-scalar-H2-validation
parent: v15.117
status: open
action: Execute corrected v14.996 scalar_final2.py and report original source EL_B/EL_Phi,E1,E2 residuals under ψ, ψdot, p oscillator, and solB/PhiS; verify or falsify B=0 and candidate α; only if source agrees independently check conjugate-mode H2 symbolic expression and low-k scaling. Do not declare finished from handoff alone.
deliverable: exact source certificate or discrepancy details.

NEXT: source-native auxiliary coefficients and original EL residuals; constrained full quadratic zero-mode compatibility; protect separate Suzuki K_full lane.
