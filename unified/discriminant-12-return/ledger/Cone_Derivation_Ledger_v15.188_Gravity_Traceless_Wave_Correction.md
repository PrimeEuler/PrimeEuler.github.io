# Cone Derivation Ledger v15.188 — Gravity erratum: v15.138 coefficient correction makes v15.181 wave residual vanish

Date 2026-10-30. Source of independent verification External Audit Round 416 v15.182 commit 98e00fddbcad709e014763ffd4d2d4def7327b2b. Prior gravity v15.138, v15.142, v15.181. Research note research-notes/K4_Traceless_Coefficient_Correction_Wave_Closure_Erratum.md commit 4d57a1a17b15e1e84e5fb90a909f6908a3784143. Prewrite live HEAD checked. Additive repair; protected lanes untouched.

[CORRECTED] In v15.138 E2 traceless spatial cos(2k) source term k² A P was written −(3/2)k² A P; correct term +(1/2)k² A P. Thus E0_corrected=E0_old+2 k² A P where P=(−k²p+t pdot)/(3k²(1+k²)) and A=((3k²+4)p+t pdot)/(3k²(1+k²)). This fixes v15.138's E0 polynomial and replaces the forcing in v15.142:
qdd+(3/t)qdot+((12k²+4)/t²)q=3(1+4k²)E0_corrected/t².
The structural oscillator and X,Y constraint substitution remain valid.

[VERIFIED BY EXTERNAL AUDIT] v15.182 re-derived v15.181's residual as an affine function of E0 and verified old E0 gives previously displayed nonzero W exactly while corrected E0 makes W_corrected ≡ 0 (symbolic, exact, all k>0 and data p,pdot, plus rational spot tests). RETRACT v15.181's restricted scalar wave 'mismatch' and claim it requires extra shear/shift as unsupported by this test. Corrected restricted 2k configuration passes local Hamiltonian and momentum constraints, traceless spatial equation, scalar wave simultaneously in this scoped calculation. This does NOT establish spatial TRACE Einstein evolution or complete full Einstein solution; those remain next gate.

Flags: v15_138_E2_coefficient=CORRECTED_PLUS_HALF; v15_142_q_forcing=CORRECTED; v15_181_W_mismatch=RETRACTED; scalar_wave_W_on_corrected_chain=ZERO_INDEPENDENT_AUDIT; 2k_constraints_and_traceless_and_wave=CONSISTENT_SCOPED; spatial_trace_Einstein=OPEN; full_second_order_evolution=OPEN; low_k_uniformity=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: gravity-corrected-traceless-wave-closure
parent: v15.188
status: open
action: Confirm this erratum faithfully reflects independently checked v15.182 correction; derive independent spatial TRACE Einstein equation from source action and test corrected q, X, Y, including Bianchi/matter propagation and any missing second-order fields. Do not promote full nonlinear stability.
deliverable: residual certificate for remaining spatial-trace Einstein equation, or exact obstruction.

NEXT: spatial trace Einstein source-native 2k check and consistency with full Einstein scalar evolution.
