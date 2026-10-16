# Cone Derivation Ledger v14.486 — Sandbox return: certified original-seed direct-middle action, both sectors (v14.448 execution, seed arm complete)

**Timestamp:** 2026-10-16 (EDT, early morning)
**Lane:** Sandbox (little Euler)
**Parents:** v14.448 (execution gate), v14.471 + v14.473 (frozen compact return + sandbox replay), v14.478 + v14.479 (frozen T2 moments + sandbox replay/cross-check), v14.444 (budget gate), v14.482/v14.485 (Lane A ownership deferral).
**Status:** sandbox deliverable under the v14.448 execution gate. The original infinite-seed action is now evaluated and certified on all 1,040,383 direct-middle outputs per sector, with a rigorous bank/tail split. No direct-middle residual, far bound, or closure is claimed in this entry — composition is the next step.

## Construction

Per sector, the seed action on output modes was computed as an exact bank part plus a certified tail part:

- **Bank:** explicit seed rows over bank modes 512,001..8,323,061 (even) / 512,002..8,323,062 (odd), 3,905,531 modes per sector (stage banks + the sandbox's bank3 extension, 508/508 chunks per sector, fully validated), with channel sums in exact integer arithmetic over 200,000-mode segments and the internal self rows excluded exactly using the represented reciprocal floor(1/(2n), 256) — the same convention as the certified gap evaluator.
- **Tail:** modes ≥ T2 = 8,323,063 / 8,323,064 evaluated from the 42 Ū + 42 V̄ inverse moments at T2, truncated at the informative-terms cutoff J* = 14 in both sectors (informative terms: V 15, U 14 of 42), with the omitted remainder bounded geometrically from the envelope constants. Endpoint ratio at the final output: even 17318340263961/69273377701969 ≈ 0.24998 ≤ 1/4; odd exactly 1/4.
- **Moments provenance:** the sandbox's locally computed T2 moments were used; v14.479 established that they enclose Lane A's independently frozen v14.478 certificates at all 170 indices (after the exact raw/bar normalization), so the tail input is doubly produced.
- Output z/d enclosures freshly evaluated at all 1,040,383 output modes per sector (outbank stage, 508/508 chunks per sector, exact chunk coverage).

## Certificates (schema `cone.infinite-seed-direct-middle-action.v1`)

| sector | outputs | modes | point ℓ² | complete ℓ² error upper | buffer SHA-256 |
|---|---|---|---:|---:|---|
| even-v | 1,040,383 | 2,080,767..4,161,531 | 3.6507291856956343e-4 | 1.995334793914987e-13 | `c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1` |
| odd-v | 1,040,383 | 2,080,768..4,161,532 | 3.647341992152244e-4 | 1.9846246697473864e-13 | `f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c` |

Buffers: 31,211,490 bytes each, 256-bit fixed point, 30-byte signed little-endian per row, retained in the sandbox workspace alongside the certificates (`dm-action-{sector}.json`) for Lane A's pinned hash freeze/replay per v14.485. Payload transfer to the repo only on Jeremy's explicit line, as before.

**Internal validation:** in each sector the channel sums at output indices 0, 520,191, and 1,040,382 (modes 2,080,767 / 3,121,149 / 4,161,531 even; 2,080,768 / 3,121,150 / 4,161,532 odd) were recomputed by brute force directly from the definition over the full bank (all m ≠ n terms) and matched the assembled channel sums exactly — asserted inside the run, all six checks true. Scope flags in both certificates: whole infinite action false, stationary acceptance false, infinite-capacity tail closed false.

## Scope and what remains

This entry certifies the seed arm of the v14.448 gate only. The error uppers (~2e-13) are negligible against the v14.444 beyond-gap allowances (a_even ≈ 2.2252e-5, a_odd ≈ 2.2288e-5), but no residual comparison is made here. Remaining under v14.448: (C) the direct-middle residual composition — bare source (1/n even, 1/(n−1) odd) minus the frozen v14.471 compact buffers minus these seed buffers, directed ℓ²; (D) the beyond-middle far bound over outputs ≥ 4,161,533/4,161,534; (E) the exact combined budget comparison, with v14.354 and the v14.403 transport charged exactly once in the prior budget and never re-charged. All thresholds unchanged.
