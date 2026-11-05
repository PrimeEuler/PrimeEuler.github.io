# Two-body bicone-dipole simulation — sandbox report (2026-11-02)

Jeremy's prompt: push on seam #2 of the v15.270–v15.282 dynamics chain (no
interaction yet — everything was single-particle). Idea, in his words: do a
2-body simulation with our bicone dipoles and watch how their acceleration
parabolas change orientation over time.

## Model (dimensionless, planar, deliberately minimal)

- Two equal masses (m = 1), each carrying a rigid dipole along its bicone
  axis n_i = (cos θ_i, sin θ_i), moment of inertia I = 0.2.
- Interaction energy depends only on r = r2 − r1 and the two axis angles:
  U = −K/r + (Cdd/r³)·[ n1·n2 − 3 (n1·ê)(n2·ê) ], ê = r/r, K = 1.
  First term = central monopole baseline (keeps the pair bound).
  Second term = textbook dipole–dipole interaction. Torques τ_i = −∂U/∂θ_i
  rotate the bicone axes; forces F1 = −F2 translate the bodies.
- HONEST SCOPE: the force law is classical dipole physics *imported* into the
  pair language, not derived from the cone. The test is narrower: once a is
  *sourced by the other body*, how does each body's osculating acceleration
  parabola r + vτ + ½aτ² reorient, and does the dipole term bend a measurably
  off the line of centres (which the monopole alone can never do)?

## Runs and verification

Integrator solve_ivp, rtol 1e-10, t ∈ [0, 40], initial separation 2.0,
circular-orbit speed for the monopole baseline, axes θ = (0.6, 2.2), spins 0.

- **Control (Cdd = 0):** circular orbit; total energy drift ~3e-11, ΔL ~5e-11;
  deviation of a1 from the line of centres = 0.0000° at all sampled times
  (exactly as required — any nonzero value would be a code bug).
- **Dipole (Cdd = 0.6):** energy spread ~3e-11, ΔP = 0, ΔL ~4e-12
  (orbital + spin angular momentum together conserved). Bound throughout:
  separation breathes 2.00 → 3.49 and back, orbit precesses into a rosette.

Bugs caught en route (both mine): (1) first version used half the correct
circular speed (√2 low), giving an eccentric plunging orbit — fixed to
v = √(K/2r); with that bug plus Cdd = 0.6 the pair made a close approach and
the dipole 1/r⁴ force blew the integration up; the fixed version is stable.
(2) First figure drew the osculating parabolas in lab coordinates, where they
lie on top of the trajectory (they osculate it — true but unreadable); replaced
with acceleration arrows in the lab plot plus a separate velocity-frame
parabola figure.

## Results

1. **The parabola axis does NOT just track the line of centres once dipoles
   interact.** Deviation δ(t) oscillates quasi-periodically, RMS 10.3°,
   typical peaks ±10–16°, extremes −30° (at t≈0) / −25° / +22°. Zero in the
   control by construction — so δ is a clean, single-number observable for
   "is there a non-central, orientation-dependent interaction."
2. **No tidal locking in this regime:** both bicone axes tumble through the
   full angle relative to the line of centres; the dipole factor
   f = n1·n2 − 3(n1·ê)(n2·ê) sweeps its full range [−2, +2]. The deviation
   oscillation is driven by that tumbling.
3. **Velocity-frame parabolas change shape, not just direction:** at t = 2 the
   dipole parabola bends noticeably harder than the monopole control; at
   t = 12 and t = 34 it bends less and is shorter (slower passage). Curvature
   (= |a|) and tilt (= a⊥/a∥) both become time-dependent through the partner's
   position *and* axis orientation — the two-body feedback loop the
   single-particle chain lacked: state of 2 → force on 1 → new parabola of 1 →
   new state of 2 → torque on both axes → repeat.

## What this does NOT show

- No cone-derived force law; the 1/r³ dipole form is assumed.
- Planar, classical, equal masses, one (K, Cdd, I) point — no parameter scan,
  no locking/chaos boundary mapped, no relativistic/shell (uv = m²) version:
  accelerations here are Newtonian, parabolas are the γ→1 shadows of v15.270.
- The bicone axis is treated as a headed dipole vector; the true bicone is
  headless (n ~ −n for the shape), with the sign carried by the dipole phase —
  not modelled here.

## Files

- `two_body_bicone.py` — full simulation + figures (Python/matplotlib).
- `fig_trajectories_parabolas.png` — orbits + acceleration (parabola-axis) arrows.
- `fig_local_parabolas.png` — body-1 osculating parabola in its velocity frame, 4 times.
- `fig_orientation_diagnostics.png` — δ(t), axis angles vs line of centres, r(t) and f(t).

Status: sandbox only, not ledgered.
