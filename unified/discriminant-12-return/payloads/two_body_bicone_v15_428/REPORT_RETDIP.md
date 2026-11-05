# Retarded bicone dipoles — sandbox report (2026-11-02)

The merge Jeremy asked for: bicone dipoles (Reports 1–2) as *retarded*
sources (Report 3). Each body = centre charge (±1) + rigid dipole pair
(∓/± QD at ∓/± (S/2)·n(θ) on the bicone axis; moment p = QD·S). Every force
is a Liénard–Wiechert point-charge field, cross-body only; net force drives
the centre (still shell-sliding, dp/dt = F), net torque about the centre
drives I·θ''. Intra-body interactions are carried by the rigid constraint
and excluded (seam — see negative result 4 for what happens if you naively
include them). Same orbit as the monopole LW baseline: separation 10,
v = 0.221, period ≈ 142. Production parameters QD = 1, S = 1 (p = 1), I = 2.

## What the runs did

**Attempt 0 (QD = 3, I = 0.5) — runaway, diagnosed not hidden.** Axes spun
up to circulation (ω ~ 1.3) within 20 time units and the run blew up. Cause:
strong coupling (dipole field ~50% of monopole field at the partner) with a
libration period (~22) only ~2× the light-crossing delay (~10), and — the
load-bearing absence — no intra-dipole radiation-reaction torque in a
cross-only model to brake delay-pumped spin. Led directly to the gentler
production parameters and to test 4 below.

**Main run (QD = 1, S = 1, I = 2, cross-only): plunge at t = 58** vs the
monopole baseline's t = 166, at separation 3.08. Findings:

1. **The retarded torque does not lock the axes.** Both axes librate with
   large amplitude and stay nearly inertial while the line of centres
   rotates beneath them: axis 1 swings +34° → −50° → +23° relative to the
   line of centres; axis 2 swings +126° → −122° → −67° (near the
   libration/circulation separatrix). Spin rates stay small (|ω| ≤ 0.17,
   0.37) until the plunge, when strengthening fields spin axis 2 up.
   Contrast the instantaneous Newtonian run of Report 1, where the axes
   *tumbled* through full circulation: retardation + the monopole-anchored
   geometry here gives libration, not tumbling — in this window and regime.
2. **Finite-size retarded drag — the headline.** Body 1's net-force
   deviation from the line of centres starts at −6.9° (initial dipole
   geometry), crosses zero at t ≈ 17, then grows *with a sustained drag
   sign* to +21° (RMS 12.4°): a tangential braking component reaching
   ~sin(21°) ≈ 36% of the total force. That, not extra radiation, is what
   triples the inspiral speed. Origin: the constituents sit ±0.5 off-centre
   and sample the partner's retarded field at displaced points with
   displaced velocities — an extended body feels retardation *across
   itself*.
3. **Size scan proves it is a model effect, not a code artifact.** Same run
   at S = 0.2 (p = 0.2): deviation collapses to ≤ 4.5° (RMS 3.1°, vs
   baseline 2.3°) and the inspiral returns to near-baseline (r = 7.39 at
   t = 80 vs baseline ≈ 8.3). The drag vanishes smoothly toward the point
   limit. Whether *nature's* rigid dipoles do this is a separate question
   (rigid constraint + cross-only fields remain idealizations); that the
   equations as posed do it, with the right limit, is established.
4. **Negative result — naive intra-body retardation is ill-posed.** Adding
   the dipole pair's mutual LW interaction (INTRA run) runs away within
   10 time units: the mutual retarded force across the arm (~QD²/S² ≈ 100×
   the orbital forces) cancels only imperfectly between retarded samples,
   and the residual feeds back positively. This is the classical extended-
   body self-interaction problem arriving on schedule, and it points at
   the program's own v15.275 split: the *symmetric* (ret+adv)/2 channel is
   the well-posed intra-body piece and the *antisymmetric* (ret−adv)/2
   piece is the radiation reaction; the full retarded self-field alone is
   neither. Building that version is a next step, not a patch.

**Diagnostic caveat (self-caught):** the constituent-wise Larmor sum used
in earlier reports overcounts radiation for composite bodies — it adds
q_i² incoherently (per body Σq² = 3) where a tight cluster radiates
coherently (~(Σq)² = 1). For these runs the separation curve, not the
Larmor sum, is the energy-loss ground truth. Numbers quoted accordingly.

## Files

- `two_body_retarded_dipole.py` (argv: TMAX QD I INTRA S),
  `retarded_dipole_runs_*.npz` per parameter set.
- `fig_retdip_axes.png` — main run: inspiral, axis libration, spin rates.
- `fig_retdip_compare.png` — size scan: separation + force deviation,
  baseline / S=0.2 / S=1.
- `fig_retdip_deviation.png`, `fig_retdip_field.png` — main run deviation
  and L-totals; E-field snapshot at t = 58 with bicone axes drawn (local
  dipole lobes + retarded sweep visible).

Status: sandbox only, not ledgered.
