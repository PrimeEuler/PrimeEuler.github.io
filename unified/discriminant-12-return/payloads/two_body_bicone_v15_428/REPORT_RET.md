# Retarded EM two-charge run — sandbox report (2026-11-02)

Jeremy's pick: "fields carry the interaction." Two point charges (bicone axes
set aside for this step), q = ±1, m = 1, Gaussian units, c = 1, initial
separation 10, tangential speed 0.221 (γ ≈ 1.026, orbital period ≈ 142).
Particles still slide on their uv = m² shells exactly as in REPORT_REL.md;
what changed is ONLY where the force comes from: the Liénard–Wiechert field
of the other charge at the retarded time t_r = t − |r − r_src(t_r)|/c —
velocity field (∝1/R²) plus acceleration/radiation field (∝1/R), B = n̂×E.

## Method

Fixed-step RK4 delay integration (dt = 0.02). Retarded times trail the
present by ~10 time units, so source states at t_r are always in stored
history (cubic-Hermite in (r, v), linear in a). Pre-history (t < 0) is
prescribed uniform circular motion, making r, v, a continuous at t = 0.
Three runs from identical initial states:
A — instantaneous Coulomb control; B — retarded velocity fields only;
C — full Liénard–Wiechert.

## Results

1. **The field really does carry it away now.** Run C inspirals secularly:
   separation 10 → 9.27 (t=60) → 7.25 (t=100) → 5.71 (t=140) → plunge,
   stopped at r = 3.18, t = 166 (~1.3 initial periods — classical radiation
   at q²/(mc²r) = 0.1 is strong). Nothing in the force law was changed to
   add damping: the loss is entirely the retarded field doing it. This is
   the v15.275 antisymmetric channel as a *consequence* rather than an
   inserted term.
2. **Energy audit passes at the expected honesty level.** Bookkeeping
   orbital energy E_book = Σ(γ−1) − 1/r falls by 0.102 over run C; the
   time-integrated relativistic Larmor power predicts the fall with a ratio
   (Larmor ÷ bookkeeping loss) of 1.24–1.33 through the whole quasi-circular
   inspiral (t ≤ 140), degrading to 1.58 in the final plunge, where the
   instantaneous-potential bookkeeping and the coarse Larmor sampling both
   lose meaning. Order-unity, same-sign, stable-ratio agreement — the field
   is taking what Larmor says it should, to ~30%.
   Particle angular momentum falls by 0.99 (of 2.27) alongside — radiation
   carries L as well as E. (Total particle momentum is identically zero in
   this mirror-symmetric setup, so the momentum channel is uninformative
   here by symmetry, not by physics.)
3. **Run B is the cautionary tale:** retarded velocity fields WITHOUT the
   radiation term are not a consistent theory — the pair gains energy
   (+0.011) and drifts outward to r = 14.1. Delay alone does not give you
   dissipation; you need the 1/R field. (Stated as measured, not as a
   theorem about all truncations.)
4. **Force direction: retardation is much quieter than the naive guess.**
   The light-crossing delay is ~10 time units ≈ 0.44 rad of orbital phase
   (≈25°), yet body 1's force deviation from the instantaneous line of
   centres is only ~1.4° initially, growing smoothly to 5.5° in the plunge
   (RMS 2.3°, mean +2.1°). This is the standard LW cancellation made
   visible: the velocity field points at the source's *linearly
   extrapolated* present position, so the residual deviation is the
   curvature-over-the-delay plus the radiation-reaction tangential piece.
   A tiny 0.15° step at t ≈ 10 is the prescribed-history → self-consistent
   handover crossing the delay window (artifact, flagged, negligible).
5. **The snapshot field is visibly not a static dipole pattern:** at t = 166
   the E-field (reconstructed from stored history) is a twisted, swept
   structure anchored on retarded positions — the hollow markers (charges
   one initial light-crossing time earlier) sit far off the present
   positions in the plunge phase.

## Seams

- Point charges, classical: runaway/plunge is the classical theory being
  itself (no self-force regularization was needed because we never add a
  separate self-field; each charge feels only the other's LW field).
- Bicone dipoles are out of this run; the retarded *dipole* (oscillating /
  rotating source with its own retarded torque balance) is the obvious
  next layer and would reconnect to Reports 1–2.
- Quantization, field equations derived from the cone: untouched, as
  scoped in the preceding discussion. Maxwell here is solved in retarded
  Green-function form — used, not derived.

## Files

- `two_body_retarded.py`, `retarded_runs.npz`
- `fig_ret_separation_energy.png` — r(t) for A/B/C; E_book vs Larmor audit.
- `fig_ret_diagnostics.png` — force deviation; particle L loss.
- `fig_ret_field_snapshot.png` — E-field streamplot at t = 166 from history.

Status: sandbox only, not ledgered.
