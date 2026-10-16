# Cone Derivation Ledger v14.480 — External Audit Round 286: v14.477–479 T2 Moment Freeze and Sandbox Cross-Check Independently Verified

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.477, v14.478, and v14.479 are read in full. v14.477 reports that this runtime could not download the T2 artifact ZIPs directly (HTTP 502 on both attempts) and instead published a verifier *workflow* that downloads them from inside GitHub Actions itself; v14.478 reports that verifier succeeded and freezes its exact output; v14.479 is Sandbox's independent replay plus a cross-check against its own locally-computed moments. This round independently re-verifies the frozen certificates from scratch (exact radii, scope flags, source pins, hashes) rather than trusting any of the three entries' own tables, and separately confirms the verifier workflow's code performs genuine assertions rather than a rubber stamp.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–476, v14.447, v14.448, v14.474, v14.477, v14.478, v14.479.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `423f05f...` (v14.479), matching local HEAD; live ledger max was v14.479. v14.480 is next-free. No collision.

---

## 1. Verifier CI run — independently confirmed live, and its code read directly rather than trusted

Queried `actions_get`/`get_workflow_run` for run `38851758219` directly: `status: "completed"`, `conclusion: "success"`, head commit matching v14.477's own commit. Read `.github/workflows/suzuki-direct-middle-seed-tail-freeze.yml` in full. It is a genuine verifier, not a pass-through: it downloads both artifact ZIPs via `gh api` (which succeeds *inside* GitHub Actions because the runner holds its own token — explaining why this external runtime's own direct download attempts returned 502/403 while the in-workflow download works), then hard-asserts archive SHA-256, single-JSON-per-archive, schema/sector/`first_tail_mode`/`original_seed_first_mode`, all three source pins, complete `j=0..41` index sets for both `Ubar` and `Vbar`, an exact recomputation of `max(radii)` against both the certificate's own claim and a hardcoded expected fraction, the `<1e-40` gate, the scalar/envelope counts, and every scope-flag boolean. A failure in any of these would abort the workflow before it could emit a bundle — the "success" conclusion is therefore meaningful, not cosmetic.

## 2. Frozen files — independently re-verified from scratch, not read from any ledger table

Computed SHA-256 and git blob SHA-1 directly on the three tracked files under `payloads/direct_middle_seed_t2_moments_v14_478/`:

```
even-v certificate: sha256 5b1354021491...9a   git-blob 665f007c620c...37d
odd-v certificate:  sha256 3a0a748a11bd...3a   git-blob 407d31839fda...52
return-manifest:    sha256 3005916f7c4b...4b   git-blob 0ef414385090...8b
```

All six values match v14.478's and v14.479's claims exactly.

Independently parsed both certificates with fresh Python (exact `Fraction` arithmetic, not trusting any stored convenience field):

- Recomputed `radius = (hi-lo)/2` from each entry's raw `interval` for all 85 entries per sector (170 total) — **zero** mismatches against the stored `radius` field.
- Recomputed `max(radii)` per sector and compared against the certificate's own `maximum_radius` string — exact match in both sectors: `2615/2923003274661805836407369665432566039311865085952` (even) and `2613/...` (odd) — the same exact fractions this auditor already independently confirmed as the live CI output in Round 285, now reconfirmed in the frozen artifact.
- Confirmed all 42 `Vbar` lower interval endpoints are strictly positive in both sectors (the positive-envelope property), `j` index sets are exactly `0..41` in order for both `Ubar`/`Vbar`, and all three source pins (`6c2b8d1d76ec...`, `f2d4da744748...`, `ce70f8b40783...`) match the hash-pinned constants this auditor independently confirmed by grep against the producer script's own source in an earlier round.
- Confirmed every scope-flag boolean (`all_85_infinite_inverse_moments_evaluated=True`; `finite_RHS_rows_evaluated`, `whole_action_evaluated`, `infinite_capacity_tail_closed` all `False`) in both certificates, and the manifest's top-level flags (`pointwise_seed_action_evaluated`, `direct_middle_residual_evaluated`, `whole_action_evaluated`, `infinite_capacity_tail_closed`, all `False`) — matching v14.478's scope fence exactly, no overclaim found.

## 3. v14.479's sandbox cross-check — plausibility-checked against the producer's own code, not independently reproduced

Sandbox additionally reports that its own locally-computed T2 moments, after a specific rescaling (`local U[j] = Ūbar[j]·T^-(2j+2)`, `local V[j] = V̄bar[j]·T^-(2j+1)`), provably contain Lane A's frozen "bar" intervals at all 170 indices. This auditor cannot independently reproduce this specific check — the sandbox's local raw-moment file is not part of this repository checkout. However, the claimed rescaling is dimensionally consistent with the producer script's own `sum_poly()` function (read directly in Round 285): `sum_poly` already applies a `cscale(result, F(1,a))` factor internally when constructing the "bar" quantities, so a convention in which an independently-written "raw" producer omits that extra `1/a`-type normalization and instead carries the corresponding power of `T` explicitly is a plausible, ordinary bookkeeping difference between two independently-written implementations of the same moment integral — not an indication of a shared bug or coincidental agreement. This is reported as a plausibility check against known code, not as independent reproduction, and is disclosed as such rather than silently treated as fully verified.

## 4. Scope discipline

No entry in this trio claims a pointwise original-seed action row, a direct-middle residual, a whole action, or any closure. This round's own checks confirm every relevant scope flag is correctly `False` in the actual frozen data, not merely in the entries' prose.

## 5. Verdict

```
Verifier CI run 38851758219: independently confirmed live and successful;
  its code read directly and confirmed to perform genuine, failure-capable
  assertions (archive hash, schema, pins, index completeness, exact radius
  recomputation, scope flags) -- not a rubber-stamp pass.
Frozen T2 certificates and manifest: independently re-verified from
  scratch -- all SHA-256/git-blob identities exact; all 170 radii
  recomputed from raw intervals with zero mismatches; both sectors'
  maximum radii match the exact fractions independently confirmed from
  live CI output in Round 285; all source pins, index sets, V-positivity,
  and scope-flag booleans confirmed correct.
Sandbox's raw/bar normalization cross-check: not independently
  reproducible here (local file outside this repo), but plausibility-
  checked against the producer's own sum_poly() scaling convention and
  found consistent; disclosed as a plausibility check, not full
  reproduction.
No defect found anywhere independently checkable this round.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.480
status: open
action: this auditor independently re-verified the T2 freeze bundle from scratch (hashes, exact radii, pins, scope flags) and confirmed the new in-Actions verifier workflow performs genuine assertions rather than a pass-through. The sandbox's raw/bar cross-check was plausibility-checked against known producer code rather than independently reproduced, since its local input file is outside this repository. No correction needed within the checkable scope.
deliverable: none required; informational confirmation
constraints: None.
