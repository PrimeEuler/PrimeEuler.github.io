# Cone Derivation Ledger v14.863 — Exact seat-to-bicone Larmor-angle map

Date 2026-10-25. Parents v14.366–367, v14.767, v14.856, v14.862. Research note research-notes/AMGM_Seat_to_Bicone_Larmor_Angle_Map.md, commit f7b56d115cd37424ce5f1a9b1957acc7352ad46e. Live prewrite HEAD f7b56d115cd37424ce5f1a9b1957acc7352ad46e. Additive only; Suzuki/far-tail untouched.

[D] On fixed-T AM–GM slice T=u,X=δ,Y=sqrt(u²-δ²), the reflected upper-circle points \(z_\pm=\pm δ/u+i\sqrt{1-(δ/u)²}\) have exact relative angle \(θ=2\arcsin(|δ|/u)\) and \(\cos θ=1-2δ²/u²\). This is geometry, not yet dynamics, and the fixed-T path differs from either parabola row/column.

[I/D] Explicitly ASSUME Larmor vectors of equal classical length j (or prepared spin-j coherent product states) oriented along the two reflected circle directions. Explicitly ASSUME ferromagnetic exchange \(H_{\rm ex}=-λJ_1\cdot J_2,\ λ>0\). Then the energy/expectation increase from balanced state is EXACTLY \(ΔE=2λj²(δ/u)²\) and raw-coordinate stiffness \(k_\delta=4λj²/u²\). For equal λ,j, u=1/2 versus u=1 gives ratio 4; normalized ξ=δ/u curvature is 4λj² for both. The orientation locking and exchange are independent dynamical input, not selected by arithmetic or bicone operator algebra. Exchange eigenmultiplet spectrum by itself is independent of δ; prepared coherent products need not be eigenstates.

[D] Countermodel: choose both vectors parallel for every δ, preserving total and exchange coupling; the exchange seat curvature vanishes. Hence pure geometry does not prove positive restoring stiffness. No contradiction with earlier negative ground-state response from a DIFFERENT linear differential-field coupling in v14.862.

[O] Derive an orientation map from the actual resonant rotating magnetic drive and state preparation, then calculate physical susceptibility; quantify possible contact-weighted corrections only after deriving spin/state/carrier multiplicity and normalization. No Newton G/alpha inference.

Flags: seat_circle_angle=EXACT; exchange_seat_curvature=EXACT_CONDITIONAL_LOCK; orientation_lock_derived=NO; raw_u_half_ratio=4_CONDITIONAL; normalized_u_distinction=NONE; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: amgm-bicone-angle-lock-review
parent: v14.863
status: open
action: Verify mirrored-circle angle, cos identity and exchange energy, compare raw and normalized stiffness, explicitly check that angular lock is independent of magnetic drive and that constant-vector countermodel gives zero seat stiffness. Preserve Suzuki/far-tail.
deliverable: scoped verdict.
