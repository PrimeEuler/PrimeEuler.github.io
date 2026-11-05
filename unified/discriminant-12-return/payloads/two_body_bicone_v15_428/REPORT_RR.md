# Split-channel intra-body build — sandbox report (2026-11-02)

Continuation Jeremy approved ("continue"): replace the ill-posed full-
retarded intra-dipole interaction (Report RETDIP, negative result 4) with
the v15.275 split — symmetric (ret+adv)/2 channel inside the body,
antisymmetric (ret−adv)/2 channel as the radiation reaction.

## The split, as implemented

- **Symmetric channel: exactly silent for a rigid dipole.** Its leading
  (instantaneous) form is a central force along the arm between equal and
  opposite charges: net force and net torque vanish identically. Verified
  numerically at t = 0 in the build: |net F| = 0.00e+00, torque = 0.00e+00
  for both bodies. So the symmetric intra channel carries *no* dynamics
  for a rigid pair — the constraint was already encoding all of it. All
  intra-body action lives in the antisymmetric channel.
- **Antisymmetric channel: Dirac reaction torque.** For a rigidly rotating
  dipole, τ_rr = (2/3c³)(p × p⃛)_z = (2/3)P²(α̇ − ω³), P = QD·S, c = 1.
  This is the (ret−adv)/2 self-field reduced to local form — no future
  states needed, unlike the symmetric/antisymmetric *field* combination.

## Implementation lesson (a failure, caught and fixed)

Version 1 estimated α̇ by finite differences of stage alphas inside the
RK step. It reproduced the Abraham–Lorentz–Dirac runaway in miniature:
68,458 cap hits, ω → 1e9, total blow-up. The jerk term fed on its own
noise at 1/dt gain. Fix = reduction of order (Landau–Lifshitz style):
α̇ is computed ONLY from the stored cross-torque alpha history on the
grid (smooth, orbital timescale), identical for all RK stages in a step.
After the fix: max |τ_rr| = 0.027 at production parameters, zero cap hits.

## Results

- **R1 (production: QD=1, I=2, S=1, RR on):** nearly the cross-only run —
  plunge at t = 56.5 vs 58; ω2 peak trimmed 0.368 → 0.345; force deviation
  RMS 12.3° vs 12.4°. The reaction torque is a few-percent correction here
  because the spins stay slow and the brake scales as ω³ (steady part).
  Honest reading: at these parameters the intra antisymmetric channel is
  *not* load-bearing for the orbital dynamics; the finite-size retarded
  drag of Report RETDIP remains the dominant dipole effect.
- **R2 (attempt-0 parameters: QD=3, I=0.5, RR on):** the brake does cap
  the spin that diverged without it (ω2 bounded ≈ 1.1 vs runaway; ω1 ≤
  0.29), but it saturates its safety cap 1,380 times doing so — outside
  the reduced-order term's perturbative validity — and the orbit still
  plunges by t = 24 (separation 2.70), driven by the translational
  finite-size drag (force deviation RMS 26.8°), not by spin. Verdict:
  in the strong-coupling regime the missing stabilizer was never mainly
  the spin brake; that regime is simply strongly coupled, and the
  reaction torque is one bounded piece of it.

## Net structural picture after Reports 1–5

Intra-body: symmetric channel silent (rigid), antisymmetric channel =
small ω³ spin brake, well-posed only in reduced-order form.
Inter-body: retarded LW fields carry energy/angular momentum off
(Larmor-audited), bend forces by aberration-cancellation residuals, and
— for extended bodies — produce a sustained-sign finite-size drag that
scales with body size and dominates the dipole phenomenology.
The cone-side dictionary is unchanged: symmetric = state/kinematics,
antisymmetric = irreversible dynamics (v15.275), now with a rigid-body
corollary — a rigid body's internal symmetric channel is identically
silent, so *all* of its internal dynamics is antisymmetric-channel.

## Files

- `two_body_retarded_dipole_rr.py` (argv: TMAX QD I S RR),
  `retarded_dipole_rr_runs_*.npz`, `fig_rr_compare.png` (R0/R1/R2),
  `fig_rr_axes.png` / `fig_rr_field.png` (last-run, R2).

Status: sandbox only, not ledgered.
