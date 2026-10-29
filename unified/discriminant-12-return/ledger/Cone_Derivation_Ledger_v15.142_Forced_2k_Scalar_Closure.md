# Cone Derivation Ledger v15.142 — Forced 2k scalar oscillator restores constrained traceless evolution

Date 2026-10-29. Gravity parents v15.137, v15.138. Existing Lane A v15.141 preserved (commit 33b8694). Muse v15.140 representation-boundary return read at commit 8cbf131. Research note research-notes/K4_Forced_Second_Order_Scalar_2k_Traceless_Closure.md at 89a074870881aa9a144516a47733d65aee7cb5b9. Prewrite HEAD checked, protected other lanes untouched.

[D, SCOPED] Add φ³ second-order q(t)sin2kz/(2k), retain conformal spatial metric ψ2=X cos2kz, lapse α2=Y cos2kz and zero shift. Let F2 and Q denote exact gravity v15.137 quadratic Hamiltonian and v15.131 momentum source; L=1+4k²; X0=(t²F2/12+tQ/(4k))/L, Y0=−t dotX0−tQ/(4k). Second-order Hamiltonian/momentum with q are (L X+t dotX+Y+q/3)=t²F2/12 and dotX+Y/t+dotq/(12k²)=−Q/(4k). Exact solution X=X0+[-q/3+t dotq/(12k²)]/L, Y=−t dotX−tQ/(4k)−t dotq/(12k²). Both constraints vanish identically.

[D] Traceless spatial equation first-order-source residual E0=gravity v15.138 formula, generally nonzero; including q modifies it by 4k²(δY−δX)−4q/3=−[t²qdd+3t dotq+(12k²+4)q]/[3L]. The identity was verified symbolically with zero residual. Thus choose q solving the forced oscillator qdd+3dotq/t+(12k²+4)q/t²=3L E0/t². For every fixed k>0 and t>0, this inhomogeneous linear ODE has solutions; substitution solves simultaneous 2k Hamiltonian and momentum constraints plus traceless spatial Einstein equation within restricted conformal/zero-shift ansatz. The oscillator's homogeneous operator matches scalar wavenumber 2k (3(2k)²+4).

[OPEN, IMPORTANT] Matter scalar wave equation and spatial trace Einstein evolution have NOT been tested; possible missing anisotropic metric/shear or shift required. Full Einstein–triplet second-order evolution, original full source variation, nonlinear future stability, and IR-uniform bounds remain OPEN. This is not a theorem that full second-order Einstein evolution closes. Muse sector-selection Casimir result remains separate and physical quarter weld PARKED.

Flags: gravity_2k_constraints=SOLVED_WITH_Q; gravity_2k_traceless=FORCED_OSCILLATOR_SOLVED; full_spatial_trace=OPEN; matter_wave_second_order=OPEN; full_order2_Einstein_evolution=OPEN; uniform_IR=OPEN; nonlinear_future_stability=OPEN; other_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: gravity-2k-forced-scalar-closure
parent: v15.142
status: open
action: Check source sign and q term in local Hamiltonian/momentum/traceless equations; independently verify eliminated forced oscillator and calculate missing spatial trace and scalar wave residuals. Determine if additional second-order shear or shift is necessary.
deliverable: scoped verdict and explicit missing evolution residual.

NEXT: independently derive second-order matter scalar wave and spatial trace Einstein equation, compare on forced q, distinguish Bianchi-redundant from genuinely independent equations.
