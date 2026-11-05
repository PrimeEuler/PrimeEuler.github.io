# Two-body bicone-dipole, relativistic version — sandbox report (2026-11-02)

Continuation of REPORT.md (Newtonian version), at Jeremy's choice:
"parabolas sliding on uv = m² shells."

## Formulation

- Dynamical variables are now (r_i, p_i). The force law statement of v15.270
  becomes exact: **dp_i/dt = F_i** — force slides the momentum.
- Position follows from the shell: E_i = √(|p_i|²c² + m²c⁴),
  dr_i/dt = p_i c²/E_i. With u_i = E_i + |p_i|c, v_i = E_i − |p_i|c, each body
  lives on u_i·v_i = (mc²)² at rapidity ψ_i = ½ ln(u_i/v_i): the crossing
  slides *along* its hyperbola instead of being re-projected onto it.
- Same interaction as the Newtonian run: instantaneous lab-frame potential
  U = −K/r + (Cdd/r³)[n1·n2 − 3(n1·ê)(n2·ê)], torques −∂U/∂θ_i on rigid
  bicone axes. Same initial (r, p, θ) as the Newtonian run for an
  apples-to-apples comparison; c = 1, m = 1 (speeds 0.45–0.55 c, γ ≈ 1.07–1.20).

### Honest seams (unchanged or new)

- **Not covariant.** An instantaneous potential in one frame is the standard
  sandbox compromise; a genuinely relativistic interacting 2-body dynamics
  needs fields and retardation (no-interaction theorem). What is relativistic
  here is the single-particle kinematics — the shell sliding.
- Axis rotation is still a lab-frame rigid rotor; no Thomas precession or
  covariant spin transport. Force law still imported, not cone-derived.
- The shell identity uv = (mc²)² holds *by construction* (E is defined from
  p); its numerical check (below) validates the code, not the physics.

## Verification

- Shell: max |u·v − (mc²)²| = 4.4e-16 over both relativistic runs (machine
  precision — the crossing never leaves its hyperbola).
- Conservation: total-energy drift ≤ 1.1e-10, total momentum drift 0,
  total angular momentum (orbital, now r×p, + spin) drift ≤ 1.5e-10.
- R-control force deviation from the line of centres = 0.00° exactly
  (central force, as required).

## Results

1. **The trajectory picture changes qualitatively even before the dipole:**
   the relativistic monopole control is a precessing eccentric rosette, not
   the Newtonian closed circle. (With the same initial p, the relativistic
   speed is pc²/E = 0.447 rather than 0.5, so the control starts inside its
   circular radius and breathes: ψ₁ oscillates periodically 0.48 ↔ 0.62,
   three clean cycles in t = 40.) The dipole run's ψ₁ (0.37 ↔ 0.55) is
   visibly irregular by contrast — shell-sliding as a fingerprint: periodic
   for central force, modulated by the partner's tumbling axis with dipoles.

2. **Two distinct bendings of the parabola, now separated:**
   - The dipole bends the *force* off the line of centres: R-dipole RMS
     12.9°, max 30.3° (Newtonian run: RMS 10.3°, max 30.2° — same effect,
     slightly larger on the relativistic trajectory).
   - Relativity bends the *coordinate acceleration* a = dv/dt away from F
     even with no dipole at all: **R-control accel deviation RMS 1.16°,
     max 1.70°, while its force deviation is exactly 0.** Cause: longitudinal
     inertia γ³m vs transverse γm — when F has a component along v (eccentric
     phases), a tilts toward the transverse direction. In cone language:
     the thing that slides on the shell is p (driven by F); the worldline
     parabola is built from a; at γ > 1 they are no longer the same arrow.
     At this run's mild γ ≈ 1.1–1.2 the effect is ~1–2° — small but cleanly
     nonzero against an exactly-zero control force deviation, and it scales
     like γ² − 1, so it grows fast with speed.

3. **Peel-off at a snapshot (γ = 1.152, t ≈ 1.5), F frozen:** comparing the
   exact constant-F relativistic continuation against two parabolas —
   gap to the Newtonian force-parabola ½(F/m)τ² grows as τ^2.01 (it has the
   wrong acceleration from the first instant); gap to the worldline parabola
   ½a₀τ² (a₀ = dv/dt at the snapshot, carrying the local γ anisotropy) grows
   as τ^3.00 (right position, velocity *and* acceleration; departs only at
   jerk order). At τ = 1.6 the gaps are 0.078 vs 0.031. Note the contrast
   with the v15.233 rest case, where the gap opens at τ⁴: that was the
   special seat symmetry (v = 0 kills the lower orders); a generic moving
   snapshot peels at τ³ from its own worldline parabola.

## Files

- `two_body_bicone_rel.py` — simulation + figures (Python/matplotlib).
- `fig_rel_trajectories.png` — Newtonian vs relativistic orbits (controls dashed).
- `fig_rel_shell.png` — body-1 (u, v) track on uv = 1 (zoom) and ψ₁(t).
- `fig_rel_deviations.png` — force deviation vs accel deviation, both runs.
- `fig_rel_peeloff.png` — frozen-F peel-off gaps, log–log.

Status: sandbox only, not ledgered.
