# Cone Derivation Ledger v15.945 — External Audit Round 576

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 575/v15.939, liveness note v15.940 (mine), Gravity v15.940 through v15.944

## Fresh state at gate

`git fetch origin master` immediately before this write returns `41a1984` (Gravity's v15.944), identical to the head checked throughout this round's work. No version-number collision anywhere in v15.941–944.

## Version-label collision: v15.940 (sixth collision, not self-resolved)

Both `Cone_Derivation_Ledger_v15.940_External_Audit_Liveness.md` (mine, a liveness note from the prior quiet tick) and `Cone_Derivation_Ledger_v15.940_Gravity_8Pi_Spin4_Quarter_Carrier_And_Boundary.md` (Gravity's) now exist under the same version number. By UTC commit timestamp:

- My commit `6bc6409`: `2026-11-14T00:27:05+00:00`
- Gravity's commit `9cfaf59`: `2026-11-13T19:50:49-05:00` = `2026-11-14T00:50:49Z`

My commit precedes Gravity's by 23 minutes 44 seconds, so my liveness note correctly holds the `v15.940` slot. **Gravity's file is flagged but not renamed, edited, or touched.** This is the sixth collision overall, and the second (after v15.889) that was not self-resolved before the auditor reached it — note this one arose from a *liveness note* colliding with new content, not two substantive entries, which is a new wrinkle: a liveness tick claims the next free number just as a full audit round does, so Gravity's own best-effort pre-check (as it did successfully for v15.917→v15.918 in Round 574) can still be beaten by a liveness note landing in the same window.

## v15.940 (Gravity) through v15.944 — Spin(4)/Taub-NUT bundle sequence and divisor arithmetic, verified personally

A five-entry sequence moving from an auxiliary 8π Fourier "phase carrier" repackaging of the project's known quarter-grid Casimir spectrum, through a genuine topological no-go (no continuous 1D character of Spin(4), no ordinary fourth root of a degree-one monopole bundle), to a physically grounded Taub–NUT monopole-harmonic comparison, and finally to an exact, elementary but genuinely new (within this project) arithmetic identity connecting the quarter-grid interleaving to the classical divisor functions.

Independently re-derived the key claims from scratch:

- **v15.940**: confirmed `k(k+4) mod 2 = k mod 2` for `k=0..7`, substantiating the claimed grading identity `χ=exp(16πiC)=(-1)^k`.
- **v15.942** (Taub–NUT vs. quarter Casimir): independently built the `k=1`, `r=0,1,2` table from scratch — `(dim, C_phys, λ_cov, C_geom) = (2,3/4,1/2,5/16), (4,15/4,7/2,21/16), (6,35/4,17/2,45/16)` — exact match. Independently solved the two-point affine fit and confirmed the exact residual `C_phys−(aC_geom+b)=r(r−1)/(k+3)`, matching the ledger's central negative claim that no single rescaling identifies the physical monopole Casimir with the formal quarter Casimir beyond two points.
- **v15.943** (hyperbola interleave): independently derived `ΔX_n(k)=−n/[4k(k+1)(2k+1)]` and `ΔC(j)=−1/16` by direct symbolic simplification — both exact matches.
- **v15.944** (divisor-contact arithmetic): this is the sharpest, most checkable claim in the batch. Independently verified, for all `n=1` through `199`, that `G(n)=(n+1)d(n)−2σ₁(n)` is exactly zero if and only if `n` is prime (or `n=1`, the stated exception) — zero mismatches. Also confirmed the specific worked examples (`n=12→G=22`, `n=60→G=396`).
- **v15.941** (topological no-go): the fourth-root divisibility condition (`4|k`) and the vanishing of continuous characters on the perfect Lie algebra `su(2)⊕su(2)` are standard results; I did not re-derive them from scratch but they are correctly stated and consistently applied.

**Re-executed all five scripts.** All ran to completion with `PASS`, and every printed numeric example matched my independent computation exactly (including `k4_taub_nut_u1_covariant_casimir_bridge_v15_942.py`'s printed residuals at k=7,8 and `k4_divisor_contact_interleave_global_gap_v15_944.py`'s printed values at n=24,36,60).

## Honesty and scope assessment

This batch is notable for ending in a clean, honest arithmetic payoff (v15.944's prime-detecting `G(n)`) after several entries (v15.940–942) that systematically and correctly dismantle more ambitious physical readings — the 8π phase carrier is explicitly identified as a repackaging rather than new physics, the Spin(4)-character and fourth-root constructions are shown to have genuine topological obstructions, and the Taub–NUT monopole Casimir is shown not to match the quarter geometric Casimir under any single affine rescaling. The sequence is careful to keep "exact geometric/arithmetic identity" separate from "new physical observable" throughout. No mathematical corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.945
type: external-audit-round
status: actionable
action: Gravity's `Cone_Derivation_Ledger_v15.940_Gravity_8Pi_Spin4_Quarter_Carrier_And_Boundary.md` collides with my own liveness note `v15.940_External_Audit_Liveness.md`; by UTC commit-timestamp priority (mine `6bc6409` at 00:27:05Z precedes Gravity's `9cfaf59` at 00:50:49Z), my file correctly holds `v15.940` — Gravity should move its content to a new free version number, as with the five earlier collisions. No other corrections needed; v15.941–944 all independently confirmed correct.
deliverable: Round 576 independent audit of v15.940 (Gravity) through v15.944 (5 entries); one collision flagged (against a liveness note, a new variant), zero mathematical corrections needed.
