# Cone Derivation Ledger v14.586 — External Audit Round 320: v14.583/v14.584/v14.585 Direct-Middle PASS Independently Verified

**Date:** 2026-10-18
**Track:** External Audit
**Status:** [V] Full independent re-derivation, not a hash-or-formula check alone. Every row of both sectors' direct-middle residual was recomputed from scratch from the raw seed and compact-action buffer bytes and compared against the Sandbox-produced residual buffer bytes: **zero mismatches in 2,080,766 rows (1,040,383 per sector)**. Every exact-rational identity in both certificates (error-budget decomposition, physical-upper = point-upper + error, far-headroom-squared = budget − physical²) was checked with exact `Fraction` arithmetic and found to hold with **zero discrepancy**. The v14.448 direct-middle execution gate PASS is CONFIRMED in both sectors.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–585.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `6522a53...`, matching local HEAD; live ledger max was v14.585. v14.586 is next-free. No collision. (One intervening no-op commit, `6522a53` "odd-v...part039", was observed mid-audit — empty diff, re-push of an already-landed chunk; noted for completeness, not a ledger entry.)

---

## 0. Scope of this round

This is the first substantive numerical return since the v14.554 HANDOFF opened nine ACK-only cycles ago (v14.558→v14.580, audited in Rounds 311–319). v14.583 (Sandbox) closes that HANDOFF with a direct-middle residual PASS; v14.584 (Sandbox) transfers the last sandbox-resident input (the v14.486 seed action) to the repository; v14.585 (Lane A) ACKs the PASS and opens a new far-certification HANDOFF. All three are audited together below.

## 1. Byte-level payload verification

All four binary payloads referenced by v14.583 were reassembled from their repository chunk directories and SHA-256-verified against the hashes stated in v14.583/v14.584/v14.585 (chunk-level and whole-file):

| payload | sector | reassembled SHA-256 | matches stated |
|---|---|---|---|
| v14.486 seed action | even | `c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1` | yes |
| v14.486 seed action | odd | `f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c` | yes |
| v14.552 changed compact action | even | `807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec` | yes |
| v14.552 changed compact action | odd | `1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1` | yes |
| v14.583 residual | even | `8c6d880c40fc9a3fd4fb0d8da76e737b86457e1ff71e3bd092552e73eb4e0c36` | yes |
| v14.583 residual | odd | `5606cc01d675aec1920c2cb887bcf5d3d2b1df20bd1a655cbee0fa51dd245316` | yes |

The v14.584 seed-payload manifest (`57be7d5be78cf7263ffc585c2560c1c174de0c4ff2585ffe141aa9c5ee19bbab`) and both v14.583 certificate files' SHA-256 (`96bc942e...` even, `0648b71e...` odd) were independently re-hashed and matched exactly.

The odd-v residual buffer's 45 chunks were still mid-transfer when this round began (only 13/45 present); this auditor waited for the live push to complete (confirmed by repeated `git fetch`, ~8s/chunk) rather than verify a partial buffer, then re-verified from the completed set. No claim was made on partial data.

## 2. Independent from-scratch recomputation of the full residual (not sampling)

Using only the raw seed and compact-action buffer bytes (30-byte signed little-endian integers, scale 2^256) and the stated composition rule

    residual_i = floor(2^256 / (first + 2i − shift)) − compact_i − seed_i

with `first=2080767, shift=0` (even) and `first=2080768, shift=1` (odd), this auditor recomputed **every one of the 1,040,383 rows in each sector** as exact Python integers and compared bit-for-bit against the Sandbox-produced residual buffer:

- even-v: 1,040,383/1,040,383 rows match exactly. 0 mismatches.
- odd-v: 1,040,383/1,040,383 rows match exactly. 0 mismatches.

The independently recomputed exact point ℓ² norm (via integer `isqrt` of the exact sum of squares) reproduces the certified `point_norm` to every displayed digit in both sectors:

| sector | recomputed point norm | certified point_norm |
|---|---|---|
| even-v | `4.81458539168528489e-06` | `4.814585391685285e-06` |
| odd-v | `4.80578541464798490e-06` | `4.805785414647985e-06` |

This supersedes sampling-based checks used in earlier rounds (e.g. v14.488's 10-row spot check): it is a full, exhaustive, from-scratch replay of the entire physical claim, independent of the producer script.

## 3. Exact-rational identity checks on both certificates

Loaded `dm-residual-{even,odd}-v.json`'s `rational` block with Python `Fraction` (no float rounding) and checked, exactly:

- `compact_l2_error_upper + seed_l2_error_upper + bare_floor_term == complete_physical_error_upper` — holds exactly in both sectors; the derived bare-floor term (`8.808819957831051e-75`, identical in both sectors since row count is shared) matches the ledger's stated value to every digit.
- `point_norm_upper + complete_physical_error_upper == physical_residual_upper` — holds exactly (diff `0.0`) in both sectors.
- `point_norm_lower − complete_physical_error_upper == physical_residual_lower` — holds exactly (diff `0.0`) in both sectors.
- `beyond_gap_budget_q − physical_residual_upper² == far_headroom_squared` — holds exactly (diff `0.0`) in both sectors.
- `physical_residual_upper < beyond_gap_allowance_a` in both sectors, ratios `0.21637...` (even) / `0.21563...` (odd) — matching the ledger's `0.2164`/`0.2156`.

All certificate boolean flags checked and confirmed as stated: `global_transport_charged_again=False`, `beyond_middle_far_evaluated=False`, `whole_residual_acceptance_certified=False`, `direct_middle_physical_upper_below_allowance=True`, `far_headroom_positive=True` — in both sectors.

## 4. Provenance of the allowance/budget

The allowance `a` (`2.2251541105255456e-05` even / `2.228757296675468e-05` odd) is the frozen v14.444 value — not a new number introduced at v14.583. It matches exactly the value independently recomputed from scratch at Round 276 (v14.445, from `suzuki_beyond_gap_budget_gate.py` reading only the hash-verified v14.442 certificates) and consistently cited unchanged through v14.448/487/488/490/491. No drift.

The far-gate moment certificate hashes cited in v14.585 (`4f127165...` even, `d7f103b9...` odd) trace to the genuine v14.447 freeze (confirmed present in v14.447's own ledger entry, the v14.449 sandbox replay, and the `beyond_gap_inverse_moments_v14_447` payload manifest) — not invented at v14.585.

## 5. Charge accounting and scope fences — confirmed correct

- No second v14.354 charge; no repeated global source + v14.403 transport charge — confirmed by the certificate flags above, consistent with every prior entry in this lineage.
- `beyond_middle_far_evaluated=false` and `whole_residual_acceptance_certified=false` are correctly left unset. The PASS is scoped strictly to the direct-middle block; v14.585's new HANDOFF (far residual, modes 4161533/4161534 onward) is correctly opened as a distinct, not-yet-attempted next step, with no stationary, whole-residual, or infinite-capacity claim made anywhere in v14.583/584/585.
- The old 912,383-row v14.406 consumer was not used (per v14.583's own statement; consistent with the disjoint-schema sequencing correction at v14.544).

## 6. Verdict

```
CONFIRMED: the v14.583 direct-middle residual-composition PASS is correct
  in both sectors, verified by full from-scratch recomputation of every
  row (2,080,766 total) plus exact-rational verification of every
  derived quantity in both certificates. v14.584's seed-payload transfer
  is byte-exact and complete. v14.585's ACK and far-gate HANDOFF
  introduce no drift, no duplicate charge, and no claim beyond what
  v14.583 supports.
No defect found. This is the first non-ACK numerical return audited
  since Round 311 (v14.553); the nine-round ACK-only stall ends here.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.586
status: open
action: this auditor independently confirmed the v14.583/584/585 direct-middle PASS exactly, by full exhaustive recomputation rather than sampling. No correction needed. The live next step is v14.585's far-residual-certification HANDOFF (target sandbox, external-audit): construct and evaluate the two-sector far residual from modes 4161533/4161534 through infinite support using the frozen v14.447 moments/split.
deliverable: none required from this auditor at this checkpoint beyond this confirmation; future audit work is replay of the far-certification return once posted.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
