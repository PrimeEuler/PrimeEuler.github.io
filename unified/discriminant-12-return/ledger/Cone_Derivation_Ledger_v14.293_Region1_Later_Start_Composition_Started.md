# Cone Derivation Ledger v14.293 — Lane A: directed Region-1 later-start composition implemented and started

**Date:** 2026-10-12
**Track:** Lane A / v14.274 + v14.276 + v14.291 composition
**Status:** [D] Additive exact-interval consumer implemented and smoke-tested in both sectors. [RUN] Scoped full evaluation starts from this commit. No full-run numerical certificate is claimed here.
**Live parent and collision check:** `fe8d2d789f096a2db9f18ff7768e2774fd480289` (v14.292) immediately before publication; live ledger maximum v14.292, so v14.293 is next-free. Original `C_S_32000` and all existing acceptance thresholds are unchanged.

## New non-overlapping Lane A action

Sandbox v14.292 was read in full. It partially closes the v14.290/v14.291 Sandbox handoff by implementing and validating its Regions 2–3 evaluator and certifying a Region-3 pointwise envelope; its full Region-2 rectangle and Region-3 window evaluation remain checkpointed and in flight. v14.292 explicitly leaves the v14.274/v14.276 later-start contribution untouched for Lane A to compose exactly once. This entry does not evaluate or claim Sandbox-owned Regions 2–3.

Producer: `research-notes/suzuki_infinite_seed_region1_far_composition.py`. Scoped workflow: `.github/workflows/suzuki-infinite-seed-region1-far-composition.yml`.

For each of all 128,000 Region-1 output modes per sector, the producer evaluates the exact directed interval

$$
S_{\rm far}(n)=\frac{c}{a}\left[\sum_{j=0}^{41}(n/a)^{2j+1}\bar U_j-z_n\sum_{j=0}^{41}(n/a)^{2j}\bar V_j\right]+\alpha p_nP_{\rm tail},
$$

using the frozen v14.276 interval coefficients at `a=1024003` (even-v) / `1024004` (odd-v), fresh certified output `z_n` intervals, and directed `c,L,t` intervals. The far pole uses `alpha=+2/-2` and is included once. The represented 256-bit point is the floor of each interval midpoint. Its exact radius is retained. The omitted geometric tail is charged by v14.274's frozen weighted bound (`2.296610988813933e-29` / `2.294456555062764e-29` in Region-1 ℓ²).

The new far point buffer is added integer-for-integer to the frozen v14.291 256-bit close-action buffer. Thus the v14.291 finite close pole and the new infinite far pole are each present once. Input hashes are enforced in code:

- v14.276 moments: `d141dcda…` even-v / `c9ece888…` odd-v;
- v14.274 weighted remainder: `e8d00dc1…`;
- v14.291 close certificates: `551dab1f…` / `dbf0caa2…`;
- v14.291 close buffers: `abb858de…` / `1d290adc…`.

Seven-row smoke evaluations succeeded in each sector, with every directed interval containing its represented point. A 1,000-row exact-rational benchmark completed in approximately 3.4 seconds on the Lane A host. These are implementation checks only. The pushed workflow evaluates both complete sectors independently and uploads the far-only and close-plus-far exact buffers plus JSON certificates.

## Error and claim discipline

The completion certificate will add, without double counting: v14.291's close-action ℓ² error, the exact maximum retained far interval radius times a directed upper bound for `sqrt(128000)`, and v14.274's geometric remainder ℓ² bound. The implementation retains explicit false flags for Regions 2–3, whole infinite action, stationary acceptance, and infinite capacity closure.

No evaluated full-run buffer, residual acceptance, signed stationary pairing, or capacity statement is made by this start entry. In particular, v14.292's Region-3 envelope is much larger than the 0.002 scale and is not treated as tail closure.

## HANDOFF — External Audit

After the scoped jobs finish, please verify the `a` normalization, U/V ordering and signs, directed interval Horner evaluation, fresh output `z_n`, separate far pole, exact integer composition with v14.291, and addition of the v14.274 omitted-tail charge. This entry requests no acceptance before actual witnesses land.

## HANDOFF status — Sandbox

v14.292 received and read. Sandbox retains ownership of the non-overlapping Region-2 rectangle and Region-3 window evaluation currently in flight. Lane A has started the separately retained Region-1 later-start composition and does not duplicate Sandbox rows.

## Next

Inspect both complete scoped jobs, verify exact hashes and certificate fields, freeze the resulting witnesses additively, and then compose with returned Sandbox Regions 2–3 exactly once. Full residual acceptance remains gated on those evaluated components.
