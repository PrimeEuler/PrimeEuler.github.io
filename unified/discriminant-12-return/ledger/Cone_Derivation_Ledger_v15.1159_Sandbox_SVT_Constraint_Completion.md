# Cone Derivation Ledger v15.1159 — Sandbox: the nonlinear K4 corner (2) — scalar/vector ADM constraints solved for v15.1085's mode; the scalar tide survives where the TT jet vanishes

**Deposit type:** Sandbox exploration, independently checkable.
Item 3 of Jeremy's 2026-11-18 gravity-thread tasking, second
half: the scalar/vector ADM constraint completion v15.1085
Gate 911 left open (its TT-only Weyl jet "cannot simply be
called the full electric tidal field"). Producer re-executed
at staging, exit 0 (11 checks, all PASS).

Solve, on the initial slice, for v15.1085's filed
longitudinal mode (q parallel z; T00 = R, T0i = 0,
Tij = diag(P, -P, R)), in longitudinal gauge with standard
linearized ADM constraints (imported GR; conventions stated
in the payload; structural results convention-free). SVT
split verified: Tij = (R/3) I + diag(-R/3, -R/3, 2R/3) +
diag(P, -P, 0), scalar STF S_L = 2R/3, anisotropic
amplitude Pi^S = (3/2) S_L = R. Momentum constraint at
eta = 0 (T0i = 0) gives Psi' + H Phi = 0, reducing the
Hamiltonian constraint to Psi(q,0) = -kappa a0^-2 R/(2 q^2)
— forced by the energy density R, not the anisotropy P.
Traceless ij: Phi - Psi = -kappa a0^-2 R/q^2, so Phi = 3 Psi
and Phi + Psi = -2 kappa a0^-2 R/q^2. Vector sector: the
transverse momentum constraint is homogeneous with zero
source for this data at eta = 0 (v15.1085's filed caveat:
initial slice, this orientation), so vector potential and
vector Weyl vanish at eta = 0. Gate 910's Ward jet
re-verified (R'(0) = 0, S_z'(0) = -i q R, R''(0) = -q^2 R).

Completed initial electric Weyl: the scalar sector gives
E^S = (kappa R/(3 a0^4)) diag(1, 1, -2) — traceless,
q-independent at eta = 0 (the constraints' 1/q^2 is
cancelled by the tidal q^2), proportional to R. Against
v15.1083's TT jet W_+(q,0) = kappa P/(2 a0^4): at
a:b = 1:2 the completed E_xx is (19/30) kappa R/a0^4 vs
the TT-only (3/10) — the scalar sector more than doubles
the xx tide; at a = b (P = 0) the TT jet vanishes while
the completed field is (kappa R/(3 a0^4)) diag(1, 1, -2),
nonzero — Gate 911's warning is quantitatively maximal at
the symmetric point, where the true initial tide is set
entirely by the energy density.

Scope: initial-slice solve for one filed mode; gauge,
boundary and zero-mode choices stated, not derived; no
time evolution of the scalar sector, no position-space
detector reconstruction. The completed field is standard
Einstein gravity sourced by the standard Maxwell stress —
no cone-specific operator appears, nothing is selected.
Together with v15.1158 this closes item 3's corner: the
veto is all-orders, and the tidal field's SVT bookkeeping
is now complete at the initial slice. G_derived = false.
Lane A files untouched.

**Payload:** `payloads/svt_constraint_completion_v15_1159/` — SVT_Constraint_Completion.md `3bc382f369aa0c0612a7428e3fffff0bf11fbd4f9aaee2ec0866db56b6d92bbd`, svt_constraint_completion.py `b5ad30d27aba9c16452d710bbf7ca25d2cb67c1047940cc15b8f076f38372d5f`.
