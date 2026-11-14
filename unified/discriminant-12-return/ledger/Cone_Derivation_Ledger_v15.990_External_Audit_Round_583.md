# Cone Derivation Ledger v15.990 — External Audit Round 583

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 582/v15.987, Gravity v15.988 through v15.989

## Fresh state at gate

`git fetch origin master` immediately before this write returns `8e510f1` (Gravity's v15.989), identical to the head checked throughout this round's work. No version-number collision (`v15.990` confirmed free).

## v15.988 — driven tidal rotor numerical benchmark, verified personally

This entry fully resolves the Gate-796/v15.986 tension by simulating the actual driven two-degree-of-freedom Hamiltonian (the v15.900 rotor plus the real polar tidal potential) rather than reusing the frozen fixed-L formulas. Independently re-integrated the exact same Hamiltonian system from scratch using `scipy.integrate.solve_ivp` (not the committed script) at the stated tolerances:

- **Baseline (B=0)**: `r(2.2)=1.000677097175`, `L(2.2)=1.000000000000`, `W=0` — exact match.
- **Static tide (B=0.02)**: `r(2.2)=0.962644279631`, `L(2.2)=0.991629528224`, `W=0` — exact match.
- **Periodic tide (B(t)=0.02cos(1.7t))**: `r(2.2)=0.982471701105`, `L(2.2)=0.971154304299`, `W=-0.021055726566` — exact match.
- **First-order torque coefficient**: independently computed the linearized integral `-∫r₀²cos(2φ₀)dt` from 0 to 2.2 using the unforced trajectory and got `-0.36150220757`, matching the claimed `-0.361502210437` to the precision of my quadrature.
- **Finite-difference slopes** at `ε=0.01,0.02,0.04`: reproduced `-0.390219416800, -0.418523588810, -0.473890602455` exactly, matching and converging toward the first-order coefficient as claimed.

This is a genuinely careful numerical result, correctly and explicitly identified as a standard-GR+Maxwell benchmark (its "Cone-minus-GR residual is identically zero by Hamiltonian identity") rather than a novel prediction.

## v15.989 — quarter Casimir cannot drive tidal response, verified personally

Independently rebuilt the genuine closed `2D`-dimensional q2 Schwinger representation from scratch (not the committed script) and confirmed the core operator identities exactly: `[K_x,K_y]=iK_z/2`, the central Casimir `C_q=K²=J_q(J_q+1)/4·I` (diagonal and sector-scalar, confirmed numerically at `D=3`: `35/16` on every state), and the noncentral transverse quadratic `Q_q=K_x²+K_y²=[J_q(J_q+1)-J_z²]/4` (confirmed exactly against the diagonal `J_z²` construction). By direct hand calculation from the computed `Q_q` diagonal at `D=3` (`m=5/2,...,-5/2 → Q=5/8,13/8,17/8,17/8,13/8,5/8`), confirmed the adjacent-level energy-spacing formula `E_{m-1}-E_m=κ(2m-1)/4` holds exactly at every `m`.

This correctly establishes the entry's negative result: a central-Casimir "extra kinetic term" provably cannot affect any within-sector tidal dynamics (it commutes with everything), while the only operator that *could* matter (the transverse quadratic) is exactly the same kind of state-dependent one-axis-twisting anisotropy already flagged in v15.969 — not a new, independently-sourced gravitational kinetic energy.

**Re-executed both scripts.** Both ran to completion with `PASS`, matching every value derived above.

## Honesty and scope assessment

This pair closes out the rotor/tidal/quarter-Casimir investigation thread started in v15.984 with a genuinely rigorous numerical result (v15.988) and a clean operator-theoretic negative (v15.989), both explicitly and correctly scoped as reproducing or bounding standard physics rather than claiming new gravitational effects. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.990
type: external-audit-round
status: actionable
action: v15.988-989 both independently confirmed correct, including full reproduction of v15.988's numerical ODE integration (SciPy) to the stated precision. No corrections needed. No open items from this round.
deliverable: Round 583 independent audit of v15.988-989 (2 entries, 2 scripts); both confirmed correct, including numerical benchmark reproduction.
