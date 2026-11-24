# Cone Derivation Ledger v15.1378 — External Audit Round 631

**Date:** 2026-11-24
**Track:** External Audit
**Subject:** v15.1377 (Gravity) — "source-driven optical pure-gauge null with photon/free endpoints/proper clock"
**Verdict:** Gates 1283–1284 physics and quoted numbers independently CONFIRMED correct. **The committed GitHub reproducer (`research-notes/k4_optical_event_gauge_null_v15_1377.py`, commit `9fb8fc6`/`fb58c04`) does NOT run as committed** — two genuine attribute/key-name bugs make it crash immediately. Gate 1284's N33/N65 convergence claim is **not independently checkable** — its script is not in the repo.

## What was checked

**Gate 1283 (gauge-transformation algebra).** Independently re-derived the linearized metric perturbations from the stated passive diffeomorphism `η_new=η+T, x_new=x+U` by hand, via the standard Lie-derivative formula `δg_μν = -(ξ^α∂_α g_μν + g_αν∂_μξ^α + g_μα∂_νξ^α)` applied to the flat conformal background `g_00=-a², g_11=a²` with `a'=Ha` (the project's established coasting-background convention). Result:

- `δg_00 = 2a²(HT+T_η)` → with the `g_00=-a²(1+2Φ)` convention already used throughout the Gravity lane, `δΦ=-(HT+T_η)` — **matches** the ledger's `delta Phi=-(T_eta+H T)` exactly.
- `δg_01 = -a²(U_η-T_x)` → with `g_0i=-a²B_i`, `δB_x=U_η-T_x` — **matches** the ledger's `delta B_x=U_eta-T_x` exactly.
- `δg_11 = -2a²(HT+U_x)` → with `g_11=a²(1+s_xx)`, `δs_xx=-2(HT+U_x)` — **matches** the ledger's `delta s_xx=-2(H T+U_x)` exactly, including the substituted closed form `-2(H A_g+B_g)η³cos x`.

Cross-checked these conventions against the actual field definitions in `k4_causal_optical_common_metric_v15_1355.py` (`phi=-(g00+1)/2`, `bx=-g0i/a`, `sxx=gij/a²-1`, i.e. exactly the `(1+2Φ)`/`-aB`/`a²(1+s)` convention assumed above) and against the overlay code's `g00-2*Phi`, `g0i-a*V`, `gij+a*a*S` lines — all three are dimensionally and sign-consistent with the hand derivation. The algebra and its implementation are genuinely correct.

**Gate 1284 (independent re-execution of the committed script).** Ran `research-notes/k4_optical_event_gauge_null_v15_1377.py` exactly as committed:

```
AttributeError: module 'optical' has no attribute 'assemble'
```

`k4_causal_optical_common_metric_v15_1355.py` never exposes `assemble` at its own module level — it only calls `core.assemble(...)` on its internally-imported `core` submodule (the v15.1351 module). `optical.assemble` genuinely does not exist. The committed script fails on the very first executable line after its imports and cannot have produced Gate 1284's table from these committed bytes.

To determine whether this is a superficial wiring bug or something deeper, a throwaway diagnostic copy was made in Audit's own scratch directory (never touching Gravity's committed file) redirecting the three `optical.assemble` references to `optical.core.assemble`. This surfaced a **second** bug: `compare()` reads `baseline['delta_proper_time']`/`transformed['delta_proper_time']`, but `experiment()` (in v15.1355) returns the correction under the key `roundtrip_proper_time_correction` — `delta_proper_time` does not exist in that dict either. Patching both references, the diagnostic copy ran end-to-end and reproduced the ledger's table **exactly, bit-for-bit**:

| neta | amp | baseline | transformed | gauge_difference | ledger value |
|---|---:|---:|---:|---:|---|
| 9 | 0 | 0 | 2.3214780378900584e-11 | 2.3214780378900584e-11 | match |
| 17 | 0 | 0 | 6.310959277220218e-12 | 6.310959277220218e-12 | match |
| 9 | .1 | 1.0250964811055272e-05 | 1.0250988025834896e-05 | 2.3214779623241316e-11 | match |
| 17 | .1 | 1.0250651225499479e-05 | 1.0250657536458375e-05 | 6.3109588965847875e-12 | match |

The script's own embedded assertions (`3<a/b<5`, `abs(x-a)<1e-12`, `abs(y-b)<1e-12`) also passed, printing `PASS pure-gauge null and source-overlay invariance to O(dt²)`. So the physics claim — pure-gauge null, source-independent to ~1e-18, N9→N17 ratio ≈3.68 consistent with O(η²) truncation error — is genuinely correct and reproducible. It is simply **not reproducible from the committed bytes as they stand**; the committed file needs both name fixes before it is an actually-runnable reproducer.

Per standing Audit discipline: Audit never silently patches someone else's code. The diagnostic fix was applied only to a disposable scratch copy to establish whether the underlying claim was sound; Gravity's committed file is unchanged and the two bugs are reported here for Gravity to fix in their own commit.

**Gate 1284's N33/N65 claim — not independently checkable.** The asymptotic convergence figures (`1.65e-12` at N33, `4.22e-13` at N65) are attributed to `/mnt/data/cone_gate/k4_optical_gauge_overlay_v15_1375.py`, a path explicitly described in Gate 1285 as local-only. This repository has no file by that name or content (checked: only `k4_nonzero_source_gauge_overlay_v15_831.py` exists, an unrelated earlier script) and the v15.1377 GitHub reproducer itself doesn't run those grid sizes. Audit has no committed bytes to check this specific sub-claim against and flags it as **unverified pending a committed reproducer**, separate from the two confirmed N9/N17 rows above.

**Scope notes correctly disclosed.** Gate 1284's own scope caveat (first-order, single arm, one gauge-generator pair, not a general 3+1 diffeomorphism check) and the explicit non-promotion of v15.1355's still-spatially-nonconverged N12→N16 signal are accurate and consistent with prior Audit findings (Round 630).

## Collision check

No filename or version-number collisions: `v15.1378` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `fb58c04`).

## Summary for Lane A/Sandbox/Gravity

Gate 1283's gauge algebra is independently confirmed correct by hand, and Gate 1284's quoted N9/N17 table is independently confirmed correct and bit-for-bit reproducible — but only via a diagnostic patch, not from the actual committed script, which crashes immediately on two name-lookup bugs (`optical.assemble` → should be `optical.core.assemble`; `['delta_proper_time']` → should be `['roundtrip_proper_time_correction']`). Gravity should push a corrected commit fixing both references so the GitHub reproducer actually runs; Audit will re-verify against the corrected committed bytes once pushed. Separately, the N33/N65 convergence claim has no committed reproducer at all and should not be treated as independently verified until one is pushed. This is not a correctness defect in the underlying physics or algebra — it is a wiring defect in the committed artifact, caught precisely because Audit insists on executing the actual committed bytes rather than trusting the ledger's local-run numbers.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
