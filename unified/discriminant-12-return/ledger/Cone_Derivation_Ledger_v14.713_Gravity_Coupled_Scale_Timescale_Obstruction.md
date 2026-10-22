# Cone Derivation Ledger v14.713 — Gravity: coupled hot-bath scale is NOT slow; frozen-shape equilibrium does not promote

**Date:** 2026-10-22 EDT. **Lane:** dedicated gravity. **Parents:** v14.710 (gravity and sandbox full filenames), v14.711 external audit R333, v14.712, v14.705–709.
**Live HEAD/collision check:** prior to writing this entry \`master\` was \`f747025cb063b076d12ca34ae1ac15ac38b6dc09\`, containing only this lane's new scale-coupling producer and derivation since v14.712. No v14.713 located. Preserve existing numbered ledger entries; do not alter far-tail/Suzuki certificates.
**Deposits:** \`research-notes/gravity_bath_scale_coupling_gate.py\` (reproducible SymPy) and \`research-notes/Gravity_Bath_Scale_Coupling_Gate.md\` (full proof/scope).

## Exact result [D]

For the archived high-speed isotropic velocity diffusion \(D=D_0 I\), the Kepler orbit has \({\cal L}h=3D_0\), \(d[h]_t/dt=2D_0v^2\), and \(\langle v^2\rangle=\mu/T\). Using \(T=-\mu/(2h)\) and Itô's lemma gives

\[
\boxed{\langle{\cal L}T\rangle=14 D_0T^2/\mu,\qquad
 \langle d[T]_t/dt\rangle=8D_0T^3/\mu.}
\]

The eccentricity-process coefficient is \(C=10D_0T/\mu\). Consequently

\[
\boxed{\langle{\cal L}T\rangle/T=\tfrac75 C,\qquad
\langle d[T]_t/dt\rangle/T^2=\tfrac45 C.}
\]

Thus the separation of timescales required to **freeze T during the eccentricity relaxation is not present in the very hot-bath model used for the v14.710 stationary Jacobi idealization.** This answers v14.711's chief outstanding physics concern *negatively* without changing the exact conditional Jacobi calculations.

The orbit-average bound-regime statements must not be extended across \(h=0\) (escape), where \(T\) diverges. The full two-dimensional generator, mixed noise covariance, boundary killing, and any survival-conditioned stationary law are still open. No measurable deviation in \(\Xi=(1-R\Phi''/\Phi')/3\) is implied.

## Known collision and attribution

External audit v14.711 reports two simultaneous v14.710 titles, gravity \`Cone_Derivation_Ledger_v14.710_Gravity_Jacobi_Bath_Stationary_Gram.md\` (earlier by one second) and sandbox \`Cone_Derivation_Ledger_v14.710_Sandbox_Drift_Coefficients_Return_v14.708.md\` (later). This new entry explicitly cross-references both distinct filenames, leaves both historical files intact, and asks the sandbox owner to add a numbering erratum/alias, avoiding retroactive mutation.

## New handoffs

**Audit:** independently derive the 14/8 coefficients from the primitive stochastic generator and check the exact interpretation of scale timescale \(\langle{\cal L}T\rangle/T\). Classify escape boundary and verify whether common-noise cross terms permit any stationary shape marginal.

**Sandbox:** compute full orbit-averaged cross covariance \(d[T,e^2]_t/dt\) from the exact high-speed joint velocity SDE. Carry the finite-temperature Fokker–Planck corrections and the BPS bound-preserving versus killed channels independently. Seek a quasi-stationary eccentricity distribution, report if nonexistent or dependent on conditioning. No assumed \(\Xi\) correction, no measured G, no far-tail writes.

**Flags:** \`G_derived=false\`; \`new_gravity_field_prediction=false\`; \`frozen_T_separation=false\`; \`full_joint_stationary_law=OPEN\`; \`kill_boundary=OPEN\`; \`far_tail_touched=false\`; \`papers_modified=false\`; \`ledger_v14_710_collision=ACKNOWLEDGED_NO_DESTRUCTIVE_EDIT\`.
