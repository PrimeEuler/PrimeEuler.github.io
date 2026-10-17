# Cone Derivation Ledger v14.539 — Sandbox return: v14.510 direct-middle complete RHS certified, both sectors (RHS phase closed; fresh-lift phase open, blocked on Lane A producer)

**Timestamp:** 2026-10-17 (EDT, afternoon)
**Lane:** Sandbox (little Euler)
**Parents:** v14.510 (HANDOFF: complete-RHS producer + gate), v14.511 (Audit R297 ratification, self-check 72/72), v14.500/v14.502 (delta candidate + clarification), v14.403 (base RHS freeze), v14.488/v14.490 (gate that created the repair).
**Status:** scoped production return under Jeremy's 2026-10-17 authorization ("Run the RHS producer + fresh lifts"). The two-sector complete-RHS production is complete and independently re-verified in the sandbox. **RHS only:** no finite lift is certified by this entry, and no residual, whole-residual, stationary, or infinite-capacity claim is made. The original C_S,32000, the 0.002 whole-trial cap, and every threshold are unchanged.

## Run record (full, including the failures)

Producer: `suzuki_direct_middle_delta_rhs.py` (v14.510/v14.511, hash-gated; self-check 72/72 exact physical-kernel rows), run supervised under systemd (`rhs511.service`, workspace launcher `rhs511/run_rhs511.sh`, sectors sequential), consuming the frozen v14.403 base archive and the v14.500 candidate exactly as pinned in the producer (snapshot SHA-256 even `da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5`, odd `6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453`; candidate point SHA-256 even `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2`, odd `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776`; base v14.403 RHS certificate SHA-256 even `42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075`, odd `1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3`).

- Two initial launches (2026-10-17 15:30:00Z and 15:30:55Z) exited 1 within ~1 s, before any computation, on sandbox staging manifest-shape mismatches (the producer's candidate spec requires a top-level `bytes` field the frozen v14.500 manifest carries only in its files table). No hash pin ever failed and no producer gate assert was touched; staging was adapted sandbox-side only (the frozen repository manifest is untouched) and the third launch ran clean.
- Even sector: clean producer exit 0 at 2026-10-17T16:18:43Z.
- A VM replacement at ~16:42Z killed the odd sector at 560,000 / 1,040,383 z-rows (systemd units in /etc do not survive replacement). The monitor recreated the unit from the workspace copy and restarted the launcher at 17:06:58Z; the launcher re-verified and skipped the even sector and restarted the odd sector from row 0 (the producer is single-shot per sector).
- Odd sector: clean producer exit 0 at 2026-10-17T17:53:07Z; launcher wrote RHS511_DONE at 17:53:08Z only after both sectors passed the independent verifier.

## Certificates and gates (independently re-verified after completion)

Verifier `rhs511/verify_rhs511.py` was re-run independently for each sector after RHS511_DONE (exit 0 both): it re-hashes both buffers per sector against the certificate, checks row counts (128,000 front / 1,040,383 direct-middle), re-checks the rational gates as exact Fractions, confirms the 3/3 complete direct front checks, and confirms all closure flags remain false. Certificate schema `cone.direct-middle-delta-complete-finite-rhs.v1`; all 128,000 new RHS rows evaluated per sector; finite correction preserves domain; small exact physical-kernel checks 72/72.

| sector | whole-trial norm upper (< 0.002) | complete physical-RHS error upper (< 4e-30) | max correction-input z error (< 1e-39) | delta correction norm upper |
|---|---:|---:|---:|---:|
| even-v | 1.720328e-04 | 3.213e-30 | 7.15e-42 | 3.7520048128694792e-06 |
| odd-v | 1.719923e-04 | 3.210e-30 | 7.15e-42 | 3.7451276392601123e-06 |

The whole-trial uppers reproduce the v14.500 triangle sums exactly (base v14.403 upper + correction upper, per sector), as the construction requires.

## Output hashes (SHA-256)

Certificates (files in `rhs511/out/`):

- even-v `direct-middle-complete-RHS-even-v.json`: `d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad`
- odd-v `direct-middle-complete-RHS-odd-v.json`: `19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884`

Buffers (as recorded inside the certificates and re-hashed by the verifier):

- even-v complete lift-RHS, 3,840,000 bytes, 128,000 x 30, bits 256: `2fb4363ff1ad6a12fb6428eb80dd4aab90365662e79ff90f4ac0c826d7b5d658`
- even-v correction-input-z, 21,848,043 bytes, 1,040,383 x 21, bits 160: `0e9e889c915a55267bcf81f9c39d9aed0d768dc857e5bcbf0731f503e6a3ed7f`
- odd-v complete lift-RHS, 3,840,000 bytes, 128,000 x 30, bits 256: `e8d1e795c2df50c66bb9c972797c50af1581f31288c4550a3a1e307ef06d13a2`
- odd-v correction-input-z, 21,848,043 bytes, 1,040,383 x 21, bits 160: `4ba2d312191080a3d302704ef14e9479a7fab913401c508fb22cfe0dbab87c21`

Chunked staging (700,000-byte chunks, repository payload convention) is prepared and reassembly-verified in the sandbox at `rhs511/payload_staging/direct_middle_complete_rhs_v14_510/` (76 buffer chunks + both certificates; staging manifest SHA-256 `39c7205a0fa74c9b3c94874d8c69438b727ea48529f1094a658197b8d805feb6`). Per standing practice the payload transfer to `unified/discriminant-12-return/payloads/` itself awaits Jeremy's explicit line; the hashes above freeze the bytes regardless of where they sit.

## Scope flags (unchanged, honest)

Both certificates carry `new_finite_lift_certified = false`, `new_residual_evaluated = false`, `whole_residual_acceptance_certified = false`, `infinite_capacity_tail_closed = false`. Charge invariants preserved: original C_S,32000 untouched; no v14.403 lift is reused or inherited; no action/residual composition is claimed from this gate.

## Fresh-lift phase: OPEN — request to Lane A

The v14.510 HANDOFF's second half (produce and exactly replay fresh finite lifts against the exact RHS hashes above) is **not closed** by this entry. It is blocked on the lift producer, not on compute: v14.510 ships no lift producer, and no v14.403 finite-lift solver exists in the sandbox workspace (the only lift-named on-box module, `suzuki_near_trial_lift_rhs.py`, is a different probe-RHS tool). The v14.403 lift certificates use schema `cone.certified-gap-correction-finite-lift.v1`, emitted by a producer held in Lane A's repository/CI; its predecessor module `suzuki_wider_correction_finite_lift.py` is likewise not on this box. The sandbox did not improvise a lift.

**Request:** Lane A to deliver the direct-middle analogue of the v14.403 gap-correction finite-lift producer (the module emitting schema `cone.certified-gap-correction-finite-lift.v1`, or its successor for the v14.510 RHS), hash-gated to the new complete-RHS certificate/buffer SHA-256 values recorded above, with produce + exact-replay modes, in the same form as the RHS producer delivery (v14.510/v14.511, self-check included). On delivery the sandbox will produce and exactly replay both sector lifts and return them as a follow-on entry.

## Disposition

The v14.510 HANDOFF is closed for the RHS phase and remains open for the fresh-lift phase, for the reason stated. Lane A's next action per v14.510 stands: verify/freeze the exact complete-RHS hashes above (the fresh-lift freeze follows once lifts exist), then prepare the changed support-aware compact/original-seed action and residual evaluation. Whole-residual acceptance, stationarity, and infinite-capacity closure remain open.
