# Cone Derivation Ledger v14.877 — Larmor quasistatic magnetic seat energy
Date 2026-10-25. Parents v14.871–876. Research note research-notes/Larmor_Quasistatic_Magnetic_Energy_Seat_Correction.md, commit a6dd90658600ec941db26b095a98d4920bee9be6. Live prewrite HEAD a6dd90658600ec941db26b095a98d4920bee9be6. Additive bicone lane; Suzuki/far-tail untouched.

[D conditional Gaussian model] For conserved rotating dipole source at first order δ, Fourier J1=g f_a e^-ikc[δdot e_x−iδ kx v], v=ΩR tangent perpendicular ex. Instantaneous magnetostatic transverse energy EB=μ0/2∫J*P_T J/k² has no δ δdot cross term (pure imaginary with real projector), and splits as
EB=(M_T/2)δdot²+(kB,Ω/2)δ²,
M_T=μ0g²/(6π^(3/2)a),
kB,Ω=μ0g²(ΩR)²/(30π^(3/2)a³).
Here g=2qR/u, and kB,Ω/kE=4(ΩR/c)²/5 using electrostatic kE from v14.873. The angular average for the convective term is <khat_x²[1−khat_v²]>=4/15. This is a checked positive FIELD-ENERGY correction, NOT yet a dynamical restoring force because prescribed rotation requires work/constraints. Valid only quasistatically for Ωa/c, ωa/c, ΩR/c small.

[O] Full causal rotating kernel and physical source mechanism still needed; no mass/G/Higgs derived.

Flags: magnetostatic_rotation_energy=POSITIVE; correction_ratio=(4_over_5)_v2_over_c2; restoring_force=NOT_DERIVED; genuine_pole=OPEN; source_from_bicone=POSTULATED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: rotating-magnetostatic-seat
parent: v14.877
status: open
action: Independently verify angular 4/15 moment, Gaussian coefficient, cross-term cancellation and difference between magnetostatic energy and dynamical seat force.
deliverable: scoped independent verdict.
