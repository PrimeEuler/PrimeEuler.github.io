# Drag scaling scan — first-pass analysis (proactive prep, 2026-11-02)

Source: `scan_log.txt` in this folder — batch launched 2026-11-02 18:02 UTC,
"ALL SCANS DONE" in the log; 10 SCANJSON lines. Note: Scan B's sep=10, S=1 case
is the same parameters as Scan A's S=1 run and appears once (as Scan A), so the
11 announced runs produce 10 distinct log lines.

## Scan A — size at fixed orbit (sep 10, V0 = 0.221)

| S | fdev RMS t=5–40 (°) | fdev mean (°) | plunge t | inspiral slope (half-orbit) |
|---|---|---|---|---|
| 0.2 | 1.52 | 1.18 | 120.0 | −0.0329 |
| 0.5 | 3.95 | 2.12 | 84.0 | −0.0689 |
| 1.0 | 9.25 | 5.34 | 58.0 | −0.1141 |
| 1.5 | 16.23 | 10.21 | 46.5 | −0.1510 |
| 2.0 | 21.71 | 13.95 | 39.0 | −0.1831 |

Log–log fits (5 points):
- **Force-deviation RMS ≈ 9.57 · S^1.17** — slightly superlinear in arm size,
  close to linear (RMS/S rises 7.6 → 10.9 across the range).
- **Plunge time ≈ 56.7 · S^−0.49** — essentially ∝ 1/√S.
- **|Inspiral slope| ≈ 0.112 · S^0.75.**

So the finite-size drag does have a clean-ish scaling in S: deviation roughly
linear in size, and the inspiral accelerates as a sublinear power of S.
Monotone in every metric, no thresholds or sign flips in 0.2 ≤ S ≤ 2.

## Scan B — velocity/separation (circular orbits; v and delay move together)

Dipole excess = quadrature difference between S=1 and the S=0.05 near-point
reference at the same separation (half-orbit RMS):

| sep | v/c per body (V0) | S=1 RMS (°) | S=0.05 RMS (°) | excess (°) | slope ratio S=1 / S=0.05 |
|---|---|---|---|---|---|
| 5 | 0.316 | 21.73 | 4.38 | 21.28 | 3.2× |
| 10 | 0.221 | 12.80 | 1.72 | 12.69 | 5.2× |
| 20 | 0.158 | 3.70 | 0.62 | 3.64 | 32.7× (see caveat) |

Caveats, keep them attached:
- By design, sep, v/c, and ω·τ all move together for circular orbits, so these
  three points cannot separate a velocity law from a separation/delay law.
  Fit formally: excess ∝ sep^−1.27, equivalently ∝ v^+2.53 — same data, two
  readings; do not quote either as *the* law.
- The sep=20, S=0.05 reference had not plunged when its run stopped
  (t_stop 515.5, sep_end 17.26) and the sep=20 slope ratio is inflated by its
  near-zero baseline slope (−0.00106); the excess-RMS column is the robust one.
- The S=0.05 baseline is not zero-deviation: pure point-charge retardation
  drag is present at every separation and grows at small sep (4.38° at sep 5),
  which is exactly why the excess subtraction matters.

## Bottom line
The drag is a genuine size effect with an orderly power-law in S
(deviation ~S^1.2, plunge ~S^−1/2), sitting on top of a smaller point-charge
retardation baseline. The v/c dependence is real but confounded with
separation in this design — separating them needs a non-circular or
forced-velocity run, not more circular points.
