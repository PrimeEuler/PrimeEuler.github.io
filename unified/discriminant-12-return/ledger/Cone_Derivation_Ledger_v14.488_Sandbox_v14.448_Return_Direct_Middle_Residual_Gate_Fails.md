# Cone Derivation Ledger v14.488 — Sandbox v14.448 return: direct-middle residual composition — GATE FAILS on the direct-middle block alone in both sectors

**Timestamp:** 2026-10-16 (EDT, early morning)
**Lane:** Sandbox (little Euler)
**Parents:** v14.448 (execution gate), v14.444 (budget gate), v14.442 (finite-plus-gap certificates), v14.471/v14.473 (compact freeze + replay), v14.478/v14.479 (T2 moments + cross-check), v14.486 (sandbox seed action), v14.487 (Audit R288).
**Status:** sandbox deliverable under the v14.448 execution gate. The direct-middle residual is now evaluated exactly. **Verdict: the v14.444 sufficient condition FAILS already on the direct-middle block in both sectors** — the beyond-middle far block is therefore moot for this gate. No whole-residual, stationary, or capacity claim is made; all thresholds unchanged.

## Correction to v14.486 (per Audit R288, v14.487)

R288 verified v14.486's arithmetic exactly and flagged one display imprecision, accepted here: the even-sector endpoint ratio 17318340263961/69273377701969 equals **0.24999993992596597**, not "≈0.24998" as displayed in v14.486. The exact fraction and the ≤ 1/4 gate are unaffected. (The odd-sector ratio is exactly 1/4.)

## Composition (v14.448 step C), conventions

Residual rows were composed exactly as in the frozen consumer lineage (`suzuki_gap_extended_residual_composition.py`; directed norm primitives from `suzuki_returned_tail_residual_composition.py`): at S = 2^256, residual_i = S // (first + 2i − shift) − compact_i − seed_i, shift = 0 even / 1 odd (bare source 1/n even, 1/(n−1) odd), compact from the frozen v14.471 stitched buffers (hashes re-verified), seed from the v14.486 buffers (hashes re-verified). Physical error = compact ℓ² error (exact rational combination of the 40 shard errors: 4.07e-21 even / 8.55e-23 odd) + seed ℓ² error (1.995e-13 / 1.985e-13) + bare floor error upper (√count/S ≈ 8.8e-75) — negligible in total. The v14.403 transport and v14.354 charge were NOT re-charged (v14.448 §E); the comparison target is the frozen v14.444 budget: q = (3e-5 − t)² − p² from the v14.442 certificates, with allowance a, a² ≤ q.

## Result — FAIL, both sectors

| sector | DM point ℓ² | DM physical upper | allowance a | ratio | physical² vs q |
|---|---:|---:|---:|---:|---:|
| even-v | 5.05775126250299e-05 | 5.057751282456339e-05 | 2.2251541105255456e-05 | 2.273× | 2.5581e-09 vs q = 4.9513e-10 |
| odd-v | 5.048483094718929e-05 | 5.048483114565176e-05 | 2.228757296675468e-05 | 2.265× | 2.5487e-09 vs q = 4.9674e-10 |

Far headroom squared (q − physical²) is negative in both sectors (−2.063e-09 even, −2.052e-09 odd): since the beyond-gap ℓ² combines the disjoint direct-middle and far blocks in quadrature, the combined beyond-gap physical residual is ≥ the direct-middle block alone and cannot satisfy the v14.444 sufficient condition. The far block (v14.448 step D) was therefore not evaluated for this gate; evaluating it cannot change the verdict. Residual buffers retained in the sandbox workspace (31,211,490 bytes each; SHA-256 even `b441468d283c8276b54e637f71f6b8641a936b3126dbba59e2e17a2483db6f5e`, odd `35d4d104c9f81fb58bb48c46de063b6f0c56cbec0e501e9822287b308ab1394c`); payload transfer only on Jeremy's explicit line.

## Verification of the inputs before accepting the verdict

- **Sign conventions:** all sign combinations of the composition were evaluated; source − compact − seed is the smallest (alternatives: 7.7e-4, 8.2e-5) — not a sign error.
- **Independent seed recomputation:** ten sample rows (indices 0, 1, 520191, 777777, 1040382 per sector) were recomputed from scratch — direct extended-precision bank sums over all m ≠ n (not the channel machinery), tail series fed by Lane A's frozen v14.478 moments (not the sandbox's), streamed outbank enclosures — and reproduce the v14.486 buffer values with |difference| ≤ 7.2e-23 at every row. The seed action, including tail and pole terms, is correct as certified.
- **Residual profile:** per-eighth block norms decrease smoothly (even: 2.266e-5, 2.071e-5, 1.911e-5, 1.777e-5, 1.663e-5, 1.563e-5, 1.476e-5, 1.399e-5) — a distributed leftover, no seam/chunk/localized defect.

## Localization [N]/[I]

Component norms (even; odd is the same picture): ||source|| = 3.466238e-4, ||seed|| = 3.650729e-4, ||compact|| = 5.976768e-5. The seed alone leaves ||source − seed|| = 3.292492e-5 — already above the total allowance before the compact action enters — and the compact action anti-aligns with that leftover, raising it to 5.058e-5. [N] The seed's norm overshoots the source's by ≈5.3%. [I] This is the same global-coefficient-mismatch signature localized at v14.396 (≈6.9% overshoot): the changed trial absorbs the overshoot on its own support — which is why the finite-plus-gap gate passes at v14.442 — while off-support the trial's action (norm ≈5.9e-5 here) is too weak and wrongly aligned to compensate. The failure is a property of the current (trial, seed) pair beyond the gap, not of the evaluation machinery.

## Scope and disposition

The v14.448 execution gate's acceptance condition is NOT met: the direct-middle residual exceeds the v14.444 beyond-gap allowance in both sectors, so no beyond-gap, whole-residual, stationary, or infinite-capacity certification follows from the current pair. What stands certified: the finite-plus-gap gate (v14.442/v14.443), the frozen compact direct-middle return (v14.471, replayed v14.473, audited v14.472), the frozen T2 moments (v14.478, replayed v14.479, audited v14.480), and the sandbox seed action (v14.486, audited v14.487). The v14.448 HANDOFF is answered in full by this return — its deliverable was the composition and exact budget comparison, whose verdict is FAIL. Any next step (e.g. a δ-correction of the pair aimed at the direct-middle range, in the lineage of v14.399) is a new gate decision for Lane A / Jeremy, not a continuation of this one.
