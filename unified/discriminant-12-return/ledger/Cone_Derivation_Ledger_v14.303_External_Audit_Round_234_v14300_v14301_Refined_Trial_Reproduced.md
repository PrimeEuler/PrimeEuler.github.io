# Cone Derivation Ledger v14.303 — External Audit Round 234: The Refined Near Trial's Correction, RHS, and Fresh Lift Independently Reproduced Byte-for-Byte

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.300's Near-seed correction and complete new finite RHS are independently re-executed from the rejected trial's own hash-verified residual points and reproduce every committed byte exactly, for both sectors, including all six archived binary witnesses. v14.301's fresh finite lift is independently replay-certified directly from the archived witness binaries, recomputing the entire exact-rational chain (Gram inverse, projected residual, inverse-energy bound) from scratch — the script's own byte-identical-serialization check passes for both sectors and matches v14.301's table exactly. v14.301's and v14.302's two newer, still-in-flight compact/residual producers were reviewed structurally and confirmed to correctly pin the new refined-trial/lift certificates (not the rejected trial's) while correctly reusing the unchanged infinite Far seed, v14.294 tail action, and source certificates — no committed payload exists yet for these two, so this is a structural check only. No correction found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–302.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0335a9f...` (v14.302), matching local HEAD; live ledger max was v14.302. v14.303 is next-free. No collision.

---

## 1. v14.300 — Near correction and new complete RHS, reproduced from scratch

Ran `suzuki_residual_near_seed_refinement.py` fresh for both sectors, starting from this auditor's own independently-reproduced v14.297 residual-point buffers (Round 233) rather than any committed binary — i.e. built the correction entirely from first principles using only hash-verified inputs. Output matched v14.300's table exactly: even-v correction norm `1.0855237322667139e-5`, whole-trial norm `0.00015685523732266715`, RHS error `3.213112412997428e-30`; odd-v correction norm `1.0841731273017624e-5`, whole-trial norm `0.00015684173127301763`, RHS error `3.210098216075485e-30`. Both JSON certificates and all six resulting binary buffers (near-correction, refined-near-trial, refined-lift-rhs — both sectors) are **byte-for-byte identical** to the committed/archived files.

Independently confirmed the whole-trial-norm safety margin: the reported new whole-trial norm upper (`0.000156...` both sectors) is well below the `0.002` domain-admissibility threshold, and the correction itself ($\approx1.08\times10^{-5}$) is below the producer's own `2e-5` cap — both assertions the producer itself enforces and that this auditor's independent run also satisfied.

## 2. v14.301 — fresh finite lift, independently replay-certified

Using the archived witness binaries (`even-v`/`odd-v-refined-near-finite-lift.bin`), ran `suzuki_refined_near_finite_lift.py` in `--mode replay` for both sectors — independently recomputing the entire exact-rational certification chain (Gram matrix and its inverse, projected-residual nonnegativity, all six protected graph components, operator-radius/RHS-error combination, graph-floor positivity, final `22*sqrt_upper(E)` charge) from scratch against the frozen binaries, not trusting the stored JSON. Both replays passed the script's own internal `assert certpath.read_text()==serialized` check silently, and the resulting numbers matched v14.301's table exactly: even-v action charge `9.591644978178165e-11` (lift norm `2969365111.8124943`), odd-v action charge `3.832992651090282e-14` (lift norm `58646754.83159147`).

## 3. v14.301/v14.302's in-flight producers — structural review only

`suzuki_refined_near_compact_region1_action.py` and `suzuki_refined_near_region1_residual.py` (v14.301) and `suzuki_refined_near_compact_far_action.py` (v14.302) have no committed numerical output yet — both entries explicitly state "no completed numerical value is asserted" / "no full-run new residual number or contraction is claimed." Read all three and confirmed their hard-coded certificate pins are correct: the compact producer's `LIFT` dict points to the new refined-lift SHAs (`8216f92d...`/`3549eaf8...`, matching v14.301's table) and its `NEAR` dict points to the new correction certificate SHAs (`cca920b7...`/`85a45f5f...`, matching v14.300's table) — not the rejected trial's originals. The residual producer correctly reuses `region1-close-plus-far-action-{sector}.json` (v14.294's unchanged infinite-tail action, since the Far seed did not change) and the same source certificate, while requiring the new compact and new lift certificates — confirming no double-counting and no silent reuse of the rejected trial's compact/lift, as claimed. This cannot be upgraded to a byte-for-byte check until a committed payload exists.

## 4. Verdict

```
v14.300: Near correction and new complete finite RHS INDEPENDENTLY
  REPRODUCED byte-for-byte for both sectors, built from this auditor's
  own independently-reproduced v14.297 residual points -- not a
  replay of Lane A's own residual buffer. All six binary witnesses
  match exactly.
v14.301: fresh finite lift INDEPENDENTLY REPLAY-CERTIFIED for both
  sectors directly from the archived witness binaries; the full
  exact-rational chain was recomputed from scratch and matches
  v14.301's table exactly.
v14.301/v14.302's newer compact/residual producers: STRUCTURALLY
  REVIEWED (correct new-trial/new-lift pins, correct reuse of the
  unchanged Far seed and v14.294 tail action) but not yet byte-checked
  since no committed payload exists.
No correction found. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.303
status: open
action: v14.300's Near correction/RHS and v14.301's fresh finite lift are both independently reproduced -- the former built from this auditor's own independently-reproduced residual points rather than any committed buffer, the latter replay-certified directly from the archived binaries. v14.301/v14.302's newer in-flight producers are structurally confirmed to pin the correct new-trial/new-lift certificates and correctly reuse the unchanged Far-seed components. No correction to report. Awaiting the frozen refined Region-1 residual to check whether this corrected trial actually improves on the rejection.
deliverable: none required; informational confirmation
constraints: None.
