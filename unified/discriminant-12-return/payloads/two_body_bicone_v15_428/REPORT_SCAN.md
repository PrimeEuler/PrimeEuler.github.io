# Drag scaling scan — sandbox report (2026-11-02)

Does the finite-size retarded drag (Report RETDIP) have a clean scaling
law? Scan on the rigid retarded-dipole code (`two_body_drag_scan.py`,
cross-only LW, QD=1, I=2), 10 runs, all completed. Sandbox, not ledgered.

## Scan A — size at fixed orbit (sep 10, v/c = 0.22 per body)

| S | plunge time | fdev RMS (t 5–40) | excess inspiral slope |
|---|------------|-------------------|-----------------------|
| 0.2 | 120 | 1.5° | 0.011 |
| 0.5 | 84 | 3.9° | 0.047 |
| 1.0 | 58 | 9.2° | 0.092 |
| 1.5 | 46.5 | 16.2° | 0.129 |
| 2.0 | 39 | 21.7° | 0.161 |

(Point-charge reference, S=0.05: plunge 163.5, slope −0.0219.)

- **Deviation angle: fdev_RMS = 9.57° · S^1.17**, log residuals ≤ 0.07 —
  a clean power law, near-linear in S as expected to leading order
  (deviation ≈ dipole/monopole field ratio ∝ S/r at fixed r, sampled
  across retardation).
- **Excess inspiral slope ∝ S^0.89** (S ≥ 0.5) — the drag *force* is
  linear in S to good accuracy.
- **Plunge time ≈ 56.7 · S^−0.49** (max err 5%), slightly better than
  the rational form t_point/(1 + 1.82 S) (max err 10%). The −1/2
  exponent mixes the S-independent radiation baseline with the linear
  drag, so read it as an effective law for this orbit, not a pure drag
  exponent.
- Caveat: eccentricity grows with S (quarter-orbit sep variation 4% at
  S=0.2 → 69% at S=2) — the large-S points are increasingly eccentric
  inspirals, not quasi-circular ones.

## Scan B — velocity (circular orbits, S=1 vs S=0.05 point reference)

Quarter-orbit-window fdev RMS (uniform early window, pre-plunge):

| sep | v_rel/c | dipole S=1 | point S=0.05 | ratio |
|-----|---------|-----------|--------------|-------|
| 5 | 0.63 | 21.7° | 3.3° | 6.5 |
| 10 | 0.44 | 9.4° | 1.3° | 7.3 |
| 20 | 0.32 | 3.9° | 0.45° | 8.6 |

- The dipole deviation exceeds the point-charge radiation-reaction
  deviation by **6.5–8.6× at every velocity**, and the ratio *grows* as
  v falls: the point deviation drops like ~v_rel^2.9 (consistent with a
  (v/c)³ radiation-reaction angle), the dipole deviation like ~v_rel^2.5.
  Finite-size drag is relatively *more* important at low velocity, not
  less — it is not a small correction riding on the point-charge effect.
- Caveats: sep=5 dipole run is violent (plunges at t=13.5, eccentricity
  0.42) — its window is early but the orbit is already strongly perturbed;
  sep=20 point run did not plunge inside its time cap (only its window
  statistics are used). The v-exponents rest on 3 separations with S/sep
  and delay covarying (unavoidable for circular orbits: ω·τ ∝ v_rel/c).

## Bottom line

The drag is a real, leading-order finite-size effect with a clean size
law (angle ∝ S^1.17, force ∝ S^~0.9) and a shallower velocity falloff
than point-charge radiation reaction. Combined with the spring run —
where the self-consistent size S_EQ = 0.867 weakened the drag and
delayed the plunge — the phenomenology is coherent: **the drag is
controlled by how much retarded-field structure the body spans,
∝ its size, and persists to low v/c.**

## Files

- `two_body_drag_scan.py`, `run_scan.sh`, `scan_log.txt`,
  `scan_runs_S*_sep*.npz`, `fig_scan.png`.

Status: sandbox only, not ledgered.
