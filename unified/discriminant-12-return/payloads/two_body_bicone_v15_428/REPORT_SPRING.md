# Spring-arm dipoles — sandbox report (2026-11-02)

The rigid constraint was the last place the symmetric channel was frozen
out. Here the dipole arm length S(t) is a dynamical coordinate: spring +
intra-pair Coulomb (both symmetric, instantaneous — the leading symmetric
channel) set the internal structure; cross-body retarded LW fields drive
it tidally; the antisymmetric channel enters as a stretch reaction
(Q_S^rr = (QD²/3)·S_jerk, reduction-of-order from grid history) and the
variable-moment Dirac torque. Rotation uses I(S) = I0 + MD·S²/2.
Code: `two_body_spring_dipole.py`. Sandbox only, not ledgered.

## What the symmetric channel does when it wakes up

It sets the size. Spring (KS=10, rest length 1) vs the pair's own Coulomb
attraction (QD²/S²) balance at **S_EQ = 0.867** — the dipole is born
13% smaller than its spring's rest length, compressed by its own charges.
(The rigid runs' S=1 was, in this light, an externally imposed size.)
Started at S_EQ the arm is quiet: no ringing, adiabatic following with
peak-to-peak modulation ≤ 0.003 through the whole inspiral.

## Results

- **Slower inspiral.** Plunge at t = 60.5 vs 56.5 (rigid + reaction) and
  58 (rigid cross-only); at t=55 the separation is 5.34 vs the rigid
  3.96. Smaller moment (p = 0.867) and smaller constituent offsets weaken
  the finite-size retarded drag — a second, independent indication that
  the drag scales with body size.
- **Stretch stays adiabatic; no chirp resonance.** S leaves equilibrium
  only in the plunge, stretching to 0.882 (body 1) / 0.875 (body 2) as
  centrifugal and tidal terms grow (+1.5%). The stretch frequency
  ω_s = 6.3 stays ≥ 4.5× above every drive frequency even at separation
  3, so the hoped-for resonance crossing does not occur at these
  parameters — a clean negative: the arm rides its instantaneous
  equilibrium all the way down.
- Reaction terms remain small and well-behaved in the coupled system:
  max |τ_rr| = 0.016, zero cap hits; stretch reaction ≤ 0.046 (turn-on
  transient). Spin evolution tracks the rigid run (ω2 endpoint ≈ 0.33).

## Reading

With the arm free, the body's internal symmetric channel does exactly
one job — it selects the equilibrium size against the pair's own Coulomb
pull — and then goes quiet adiabatically, while everything irreversible
(orbital decay, drag, spin brake) remains antisymmetric-channel. The
v15.275 split survives unfreezing the constraint: symmetric = structure,
antisymmetric = dissipation.

## Files

- `two_body_spring_dipole.py`, `spring_dipole_runs.npz`,
  `fig_spring_main.png` (inspiral / S(t) / spins vs rigid runs),
  `fig_spring_zoom.png` (early S modulation).

Status: sandbox only, not ledgered.
