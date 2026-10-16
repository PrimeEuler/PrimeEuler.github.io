# Cone Derivation Ledger v14.500 — Sandbox return: direct-middle delta candidate certified, both sectors (v14.490 gate)

**Timestamp:** 2026-10-16 (EDT, midday)
**Lane:** Sandbox (little Euler)
**Parents:** v14.490 (delta gate), v14.491 (Audit R290: convention faithfulness), v14.488 (exact point residuals), v14.399 (delta_gap convention), v14.403 (base trial RHS/lift freeze).
**Status:** sandbox deliverable under the v14.490 candidate-generation gate. The two-sector direct-middle delta candidate is constructed and certified. **Candidate only:** no action evaluation, residual acceptance, whole-residual, stationary, or infinite-capacity claim; the original C_S,32000 and every threshold are unchanged.

## Construction (v14.399 convention, reused exactly)

delta_DM(n) = floor_160(r_DM,point(n) / midpoint(log_normalized(n, 128))) on the direct-middle rows — even 2080767..4161531, odd 2080768..4161532, step 2, 1,040,383 rows per sector — zero elsewhere. floor_160(q) = q.numerator·2^160 // q.denominator; the log midpoints come from the pinned `suzuki_certified_remote_diagonal.py` (SHA-256 `08226538dffb5db42d85db5edb0f1c043a56df326ed1f51dc7391ca7cf8a2788`, byte-identical to the repository copy, hash-asserted before use). Log midpoints on this support range over [13.161952772586037, 13.855099472553855].

## Input assertions (v14.490 item 1–2)

The consumed point-residual buffers were hash-asserted in the build to the v14.488/v14.490 witnesses exactly: even `b441468d283c8276b54e637f71f6b8641a936b3126dbba59e2e17a2483db6f5e`, odd `35d4d104c9f81fb58bb48c46de063b6f0c56cbec0e501e9822287b308ab1394c` (31,211,490 bytes each, width 30). The base whole-trial norm uppers are taken from the frozen v14.403 RHS certificates (fetched from the repository payload `gap_correction_rhs_and_lift_v14_403/`; file SHA-256 even `42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075`, odd `1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3`).

## Certificates (v14.490 items 3–5)

| sector | buffer SHA-256 | bytes / width | exact norm² upper (display) | outward ℓ¹ | base trial upper (v14.403) | whole-trial triangle upper |
|---|---|---:|---:|---:|---:|---:|
| even-v | `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2` | 17,686,511 / 17 | 3.7520048128694792e-06 | 0.003250877135933216 | 1.6828077720e-04 | 1.720328e-04 |
| odd-v | `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776` | 17,686,511 / 17 | 3.7451276392601123e-06 | 0.003244346453824934 | 1.6824720208e-04 | 1.719923e-04 |

Exact rational norm-squared, norm upper (sqrt_upper at 192 bits), and ℓ¹ values are carried in the retained sector certificates (SHA-256 even `99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911`, odd `c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703`). **Cap test (unchanged 0.002, v14.339):** each correction norm upper is within the cap by itself, and each whole-trial triangle upper (base + correction) is within the cap (≈1.72e-4 ≪ 0.002).

**One-quantum pointwise enclosure (item 4):** verified **exactly on all 1,040,383 rows per sector** (stronger than the v14.399 sample-only check): 0 ≤ r_DM,point − delta_DM·logpoint < logpoint·2^−160 at every row. Independently, sample rows were recomputed by an integer-only path ((r·denominator) // (numerator·2^96)) both inside the build (64 rows/sector) and in a separate post-build verification with a fresh seed (16 rows/sector) — all agree; buffer round-trips recompute the certified norm-squared exactly.

## Scope flags (item 6)

candidate_only = true; action_evaluated = false; residual_acceptance_met = false; whole_residual_closed = false; stationary_acceptance_met = false; infinite_capacity_tail_closed = false. Charge invariants preserved: original C_S,32000 untouched; v14.354 charged exactly once (in its own lineage, not here); source + v14.403 transport charged exactly once (ditto). Buffers and certificates are retained in the sandbox workspace; payload transfer only on Jeremy's explicit line, as before.

## Disposition

The v14.490 HANDOFF is answered: the certified two-sector delta candidate now exists. Per v14.490/v14.499, Lane A next builds a new complete RHS, obtains a fresh lift, and evaluates support-aware compact/original-seed action and residual rows with fresh output splits; the v14.471/v14.478 witnesses are not reused outside their certified scope.
