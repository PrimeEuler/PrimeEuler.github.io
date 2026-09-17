# Cone Derivation Ledger v13.565 — Expanded Label-Blind Suzuki Ray Geometry

**Renumbering note:** originally filed as v13.556, which collided with the already-pushed `Cone_Derivation_Ledger_v13.556_Three_Pair_Quotient_S4_to_S3.md`. Renumbered to v13.565 during External Audit Round 50. Mathematical content is unchanged.

**Status:** first sample-expansion gate in the new 5/13 Suzuki ray-alignment exploratory lane. Finite binary64 diagnostic; no explanatory arithmetic labels consulted; no theorem promotion.

## 1. Predeclared expansion

Following v13.564, the question is no longer whether χ12 organizes the Suzuki response. That lane is closed. The new neutral question is whether the observed q=5,13 shared-ray proximity persists when the q sample is enlarged.

Before computing new ray geometry, freeze the sample as the first twelve primes >=5:

`Q={5,7,11,13,17,19,23,29,31,37,41,43}`.

Use exactly the Level-1 source formula and the same canonical fixed baseline whitening

`B0=C_arch+C_2+C_3+C_4+C_5+C_7`.

For every q, retain the existing twelve-component directional fingerprint F_q and normalize it to the ray

`U_q=F_q/||F_q||`.

Define the pairwise ray angle

`theta(q,r)=acos(U_q·U_r)`.

No χ12 value, residue label, candidate character, Pell datum, log-frequency hypothesis, or other explanatory variable enters this construction.

Reproducer:

`research-notes/suzuki_ray_alignment_expanded_blind.py`

## 2. Predeclared seed-persistence gate

The q=5,13 observation from v13.555 is treated only as a seed.

**PASS-SEED:** q=5 and q=13 remain mutual nearest neighbors under ray angle in the enlarged sample.

**FAIL-SEED:** either q=5 or q=13 acquires a closer ray neighbor.

This gate tests persistence only. It cannot explain the source-side cause of any alignment.

## 3. M=499 screening result

The smallest angles are

| pair | angle (degrees) |
|---|---:|
| 13,31 | 1.165022174 |
| 5,37 | 3.016228306 |
| 5,13 | 8.460726552 |
| 5,31 | 8.737815691 |
| 31,37 | 9.373496630 |
| 13,37 | 9.438255282 |

Thus q=5 and q=13 are not mutual nearest neighbors after sample expansion.

`nearest(5)=37`, with angle `3.016228306 degrees`.

`nearest(13)=31`, with angle `1.165022174 degrees`.

The original seed angle remains small, `theta(5,13)=8.460726552 degrees`, but two newly admitted rays are substantially closer to its endpoints.

**[OBS] M=499 seed-persistence gate: FAIL-SEED.**

## 4. Frozen confirmation at M=999

Without changing the sample, observable, metric, or gate, repeat at M=999.

| pair | M=499 angle | M=999 angle |
|---|---:|---:|
| 13,31 | 1.165022174 | 1.166774267 |
| 5,37 | 3.016228306 | 3.022757404 |
| 5,13 | 8.460726552 | 8.479191857 |
| 5,31 | 8.737815691 | 8.754907167 |
| 31,37 | 9.373496630 | 9.384973872 |
| 13,37 | 9.438255282 | 9.452091662 |

At M=999,

`nearest(5)=37`, angle `3.022757404 degrees`,

`nearest(13)=31`, angle `1.166774267 degrees`.

Both remain well below

`theta(5,13)=8.479191857 degrees`.

**[OBS] The expanded-sample FAIL-SEED result is confirmed at M=999.**

## 5. Interpretation

The original q=5,13 alignment is real within the four-q Level-1 sample but is not an isolated mutual-nearest-neighbor pair in the enlarged label-blind ray geometry.

The expanded geometry instead reveals at least two tighter alignments:

`13 <-> 31` and `5 <-> 37`.

This changes the exploratory question. The target is no longer to explain one exceptional 5/13 pair. The data now suggest a broader response-ray geometry in which 5 and 13 lie in a region containing still closer rays.

No arithmetic interpretation is attached at this stage.

## 6. Evidence status and guardrails

**Legend:** `[EXACT]` exact recomputation/algebra; `[B64]` finite binary64 checkpoint output; `[OBS]` empirical pattern from frozen outputs; `[UNSUPPORTED]` conclusion not established by present evidence.

- **[B64]** All angles above are finite binary64 outputs from the fixed construction.
- **[OBS]** q=5,13 cease to be mutual nearest neighbors when the predeclared sample is expanded.
- **[OBS]** q=13,31 and q=5,37 are substantially tighter ray alignments at both M=499 and M=999.
- **[UNSUPPORTED]** No source-side invariant has yet been shown to organize these alignments.
- **[UNSUPPORTED]** The new pairs are not evidence for a congruence, character, Pell, cyclotomic, or other arithmetic law until such a variable is independently predeclared and tested.
- **[UNSUPPORTED]** The observed finite-sample geometry does not establish an infinite family or asymptotic structure.

## 7. Next gate

Do not select an arithmetic explanation from the newly visible q labels and then retrofit a metric.

The next safe step is geometric: analyze the complete frozen angular-distance matrix itself, identify whether it contains a stable low-dimensional ray manifold / chain / cluster structure, and predeclare a geometry-only statistic before consulting any candidate source-side labels.

Only after that geometry is characterized should candidate explanatory invariants be tested against the frozen structure.
