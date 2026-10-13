# Cone Derivation Ledger v14.308 — Sandbox independent reproduction of the v14.306 refined compact Far gate (byte-identical)

Sandbox track (our Lane B). Independent local execution of Lane A's published
v14.302 producer against its SHA-pinned payload inputs, carried out as
idle-time work while Lane A's run limit was pending reset (Jeremy-directed,
2026-10-12). The computation was launched locally at ~20:19 EDT on
2026-10-12, before v14.306 existed; the even sector completed at 20:21 EDT
and the odd sector at ~21:07 EDT. Inputs were exclusively the pinned repo
payloads below; Lane A's Far output artifacts were never downloaded. On
publication of v14.306, its recorded Far JSON SHA256 values were found to
match the local outputs exactly, in both sectors.

## Producer and pinned inputs (all SHA256 asserted by the producer itself)

Producer: `research-notes/suzuki_refined_near_compact_far_action.py`,
executed unmodified. Every internal pin passed.

- Snapshot root `payloads/exact_outward_run_37827949740/`: trace zips
  reassembled from the committed base64 parts and verified against the
  transport PINS — even zip `da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5`,
  odd zip `6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453`;
  certificates `87afab76d9b22e574b040e553623460456b0bcd819c2dde7985e6c783f92ba61` /
  `4ead74028da43fbab4ae1f859c62e6d738113417d8cdc22cec9ac4903d022c3a`.
- Source root `payloads/full_stationary_source_v14_213/`: full stationary
  source certificates `40fcbd9ba5745598...` (even) / `41fdeb3af0ab1d00...`
  (odd), matching the producer's pins.
- RHS/lift root `payloads/refined_near_trial_and_lift_v14_300/`: refined
  lift certificates `8216f92d69654953...` / `3549eaf804253468...` and
  near-seed-refinement certificates, matching the producer's pins; sibling
  witness `payloads/near_trial_rhs_witness_v14_238/` as the producer
  requires. The refined trial/lift inputs are the v14.300 archive —
  the original rejected seed's coefficients were not used.

## Reproduced results (identical to v14.306's frozen values)

All 42 compact Far moment pairs per sector for
x = (Z_full − refined lift, refined y_Near); three complete
256,000-input direct Far rows per sector verified against the exact
geometric omitted-piece identity (even n = 1024001, 1536001, 4096001;
odd n = 1024002, 1536002, 4096002; all `all_256000_terms_outward_identity`
true).

| Sector | Geometric action remainder upper | Physical compact Far parameter charge upper | Combined support norm upper |
|---|---:|---:|---:|
| even-v | 6.897170650247918e-16 | 8.670267808029947e-27 | 24523208672.860615 |
| odd-v | 1.36356291646682e-17 | 1.7141014026897978e-28 | 484821090.19425637 |

Output JSON SHA256 (local) — identical to the Far JSON SHA256 values frozen
in v14.306:

- even-v: `9eb263543a18c3fa2610e7d56ab83b8b94cc3292d2838b75fbe396b9f5e1c30b`
- odd-v: `ee1ea338b61c81aa13b303ea7eae0b868f607e8c5b9f0f8d3646cdd340f2f392`

Verdict [N-cert]: the v14.306 updated compact Far gate is independently
reproduced byte-for-byte. The physical parameter charge is recorded
separately from the geometric point-action remainder, per the v14.283
recipe; it is not an infinite-tail action or residual claim.

## Scope (unchanged, preserved from the producer's own flags)

Compact component only: `infinite_seed_tail_action_included = False`,
`whole_remote_residual_norm_evaluated = False`,
`stationary_acceptance_met = False`, `infinite_capacity_tail_closed =
False`. The refined Region-1 residual pass (upper bounds
1.5449327582703795e-5 even / 1.5421928748451216e-5 odd, below the unchanged
3e-5 target) is Lane A's v14.306 result, cited here, not claimed by the
sandbox. Whole-residual acceptance, signed stationary pairing, and capacity
closure remain open.

## HANDOFF-ACK

- To v14.302 (sandbox): acknowledged — the changed compact Far component
  stayed in Lane A's namespace; the sandbox tail-only Regions 2–3 work was
  not duplicated or mixed with these coefficients, and the unchanged
  infinite Far seed keeps that tail work reusable for the refined trial.
- To v14.306 (sandbox): acknowledged — the unchanged infinite-tail
  Regions 2–3 action is the next missing component for whole-residual
  evaluation. The sandbox evaluator is producing actual evaluated rows
  with directed error charges (not envelope bounds): sector banks [b, 2a)
  built and validated exactly against the v14.291 certificate; tail
  moments and the Region-3/Region-2 rectangle evaluation are in flight.
  The completion entry will report evaluated rows and charges only.

## Publication restriction (recorded explicitly, per v14.297's request)

The local output JSONs are held in the sandbox workspace only
(`~/workspace/d12/refined_far/out/`, SHA256 recorded above) and are NOT
committed to `research-notes/`; sandbox code and output publication to the
repository remains restricted pending Jeremy's explicit approval. This
ledger entry is the hash-bound public record of the reproduction.
