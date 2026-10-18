# Cone Derivation Ledger v14.552 — Sandbox return: v14.544 changed direct-middle compact action certified and exactly replayed, both sectors

**Timestamp:** 2026-10-17 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.544 (Lane A ACK of fresh lifts + changed direct-middle compact-action HANDOFF), v14.543 (sandbox fresh-lift return), v14.541 (Lane A fresh-lift producer), v14.539 (sandbox complete-RHS return), v14.510/v14.511 (RHS producer + ratification), v14.500/v14.502 (delta candidate + clarification), v14.471/v14.473 (direct-middle compact freeze + sandbox replay), v14.448 (direct-middle execution gate), v14.405 (gap-extended compact action), v14.403 (gap RHS + lift freeze), v14.442 (finite-plus-gap residual gate; v14.354 and source/v14.403 transport charged exactly once there).
**Status:** scoped production return under Jeremy's 2026-10-17 authorization ("Start the compact-action build"). The v14.544 HANDOFF is closed for the changed compact-action gate: both sector changed direct-middle compact-action buffers were produced under the frozen contract and exactly replayed, byte-identically. **Compact action only:** no direct-middle residual was composed or evaluated, no seed action was combined, no far work was opened, and no whole-action, whole-residual, stationary, or infinite-capacity claim is made. Nothing was fed into the 912,383-row v14.406 consumer.

## The frozen contract as executed

Support-aware compact action on output rows U..2U−1, U = 1,040,383, of the five current compact components (support [0, 2U)):

| # | component | offset | count | formed from |
|---|---|---|---|---|
| 1 | front | 0 | 128,000 | whole source Z − v14.543 fresh lift (no v14.403 lift reused) |
| 2 | near | 128,000 | 128,000 | refined Near trial (v14.300) |
| 3 | patch1 | 256,000 | 264,192 | v14.341 wider correction candidate |
| 4 | patch2 | 520,192 | 520,191 | v14.399 gap correction candidate |
| 5 | delta | 1,040,383 | 1,040,383 | v14.500 δ_DM, on exactly the output rows |

Every input byte was hash-pinned in the producer and asserted before use: snapshot (PINS), full-stationary source certificates, the v14.543 lift certificates and buffers, near certificates/buffers, the v14.349 old-finite certificates and patch z, the v14.403 gap RHS certificates and correction-input z, both raw candidates (reassembled from their repo payloads and pin-verified), the v14.500 delta buffers (even `c5b68453…`, odd `e9efaf91…`), and their paired v14.539 correction-input-z buffers (even `0e9e889c…`, odd `4ba2d312…`). Output-row z is the delta component's stored correction-input z (bits 160), per the support-owner convention of the audited gap-extended producer: every output row is owned by component 5.

Self-interaction (component 5, exactly once each): the rectangular channels include the artificial Hankel self term; it is removed exactly once by the owner compensation of `suzuki_gap_extended_compact_action.py` (the identity isolated in `suzuki_compact_action_self_diagonal.compensate_self`: on owner rows z_out = z_in, so the compensation is integer-exact), and the raw physical diagonal from the certified diagonal enclosure is added exactly once, its interval half-width charged. Components 1–4 have no diagonal on these rows. C_S_32000, the 2^256 kernel scale, all certified tolerances, and the compact-action physical-error threshold 3e-11 are retained unchanged.

**Charge accounting (verbatim from both certificates):** "Charge accounting: the v14.354 Hankel self-diagonal correction charge and the global source + v14.403 lift transport charge were each charged exactly once in ledger v14.442 and are not charged again in this composition. No term in this certificate's error budget is, contains, or repeats either charge. The Hankel self-interaction removal and raw-diagonal insertion applied to the delta component are evaluation procedures of this compact action under the v14.544 frozen contract, not repetitions of the v14.354 error charge."

## Run record

Producer: `suzuki_direct_middle_changed_compact_action.py` (sandbox, this return) — the v14.471 direct-middle shard skeleton (`seq_producer_dm.py` lineage) carrying the v14.405 on-support assembly, built on Lane A's audited modules unmodified: `suzuki_gap_extended_compact_action.py` (research-notes commit 7f7f11f6, SHA-256 `e6be6ccb…`), `suzuki_compact_component_rectangle.py` (SHA-256 `362c1742…`), `suzuki_compact_action_self_diagonal.py` (SHA-256 `e9db14bf…`), `suzuki_wider_correction_rhs.py` (floor; SHA-256 `543d31fe…`), `suzuki_wider_correction_finite_lift.py` (writebuffer; SHA-256 `0134f6dd…`); changed producer SHA-256 `7784532512ea8a9e6c5bdb3728bb52ca7af281b6da97f076b17057f39885eeb2`. Producer self-checks executed and recorded in both sector certificates: component rectangle rows 486, mixed-scale split rows 30, self-diagonal rows 54 — all exact. Per shard per component, three sampled output rows were recomputed by direct integer channel sums and matched exactly (15/15 per shard, including delta rows inside their own support).

Run shape: 4 shards per sector (DM partition of U), sectors and shards serial under systemd (`ca544.service`, workspace launcher `ca544/run_ca544.sh`), skip-if-done per artifact with re-hash validation. Production tree launched 2026-10-17T20:30:19Z, completed (both stitches) 22:16Z; the exact-replay tree completed 2026-10-18T00:16:47Z (`CA544_DONE`). Incidents, disclosed in full: a VM replacement at ~20:23Z killed a foreground smoke attempt before production began (no artifact lost; the supervised run was launched after the replacement, on the fresh boot); a second VM replacement at ~23:21Z killed replay odd-v shard 0 mid-loop (no completed artifact lost; the /etc unit was recreated from the workspace copy, the launcher resumed at 23:22:33Z re-validating and skipping every completed artifact, and the interrupted shard was recomputed from row 0). Exact replay: an independent second production of both complete trees (prep, shards, stitch) into a separate root; all 22 compared file pairs (prep artifacts, shard certificates, shard buffers, sector certificates, stitched buffers) byte-identical — replay verdict PASS. All certification arithmetic is exact integer/Fraction arithmetic; convolutions are exact (GMP integer multiplication inside `suzuki_exact_integer_source_action.convolution`).

## Results (independently re-verified after completion)

Certificate schema `cone.direct-middle-changed-compact-action.v1`; per-sector stitched buffer bits 256, count 1,040,383, complete contiguous coverage of [1040383, 2080765] with 3 seams checked per sector.

| sector | stitched buffer SHA-256 | width | bytes | complete physical-error upper (cap 3e-11) | diagonal interval charge | parameter charge |
|---|---|---|---:|---:|---:|
| even-v | `807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec` | 30 | 31,211,490 | 9.252926241952067e-18 | 9.248852494394221e-18 | 4.073747557845216e-21 |
| odd-v | `1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1` | 30 | 31,211,490 | 9.231899594035513e-18 | 9.231813984081294e-18 | 8.560995421832813e-23 |

Both complete uppers are exact-rational certified < 3e-11 (verified as Fractions, not only in display floats), ~7 orders of magnitude inside the gate. Sector certificate files: even `direct-middle-changed-compact-action-even-v.json` SHA-256 `2013799b36b5810ec90e9f815822634c7da518e8e18dda401b9f1c72dc0d7a6a`; odd `direct-middle-changed-compact-action-odd-v.json` SHA-256 `ebe5cc360f1daceb90de47c12ae98ec90836941213b595f2b234340ae92fe4c1`. Represented five-component compact ℓ¹ / norm upper (display): even 39939027848.08218 / 24614556761.144974; odd 839320133.8689237 / 486622035.539643. The ℓ¹ values reproduce the v14.471 frozen error scale exactly through the shared parameter-charge term (1e-34 · ℓ¹ · √count): the v14.471 maximum shard error 9.1027e-22 is this producer's even-sector per-shard parameter term — an independent cross-check that the component loading, including the new-lift front, is the frozen one.

Shard coverage (buffer SHA-256 / certificate file SHA-256):

| sector | shard | rows | output indices | buffer SHA-256 | certificate SHA-256 |
|---|---|---:|---|---|---|
| even-v | 0 | 260,096 | 1040383–1300478 | `a0e44079d7cbff283b82e5a80d1515a06f909c84ab0d6f6d6cd5a764a5e887ae` | `47c9a26b16a8dd82d8be7cea4ec9c2cf4ebfd2d1fa27f6d949475993e12e51de` |
| even-v | 1 | 260,096 | 1300479–1560574 | `0a964fa474dedbf6a7686b7091d76b4b016dbccb566329023f0aea921c0cd889` | `6b684d9d1da77359a4e9c5c468bcf041e684a871a30f9a857b677624ae42846d` |
| even-v | 2 | 260,096 | 1560575–1820670 | `4b3facafe64423bb678f386701214b750ce9a6fdfb7747ebfe971a5e8019aa33` | `01f9b4adace7716853a21693dd6686389cd735c5d1850a591b77dddf4467a78f` |
| even-v | 3 | 260,095 | 1820671–2080765 | `cd8a836b40d67725e55a58d283d52bb542efd1071c3e6528af5b8a038518837d` | `9efffe4adf6cfc8c7726161e378d103e497050ffb9eef2ec56924c0ba5623681` |
| odd-v | 0 | 260,096 | 1040383–1300478 | `388f0fe34003d1554f185e9c34887a51fdf231b2271e84508a4b6f9450658478` | `9594a751918a6ba1d935eed47607fc5de9fd7263b14a8704df4c98f0b2c20274` |
| odd-v | 1 | 260,096 | 1300479–1560574 | `a3d28140e0d140bc8dc8a0d2a2cb50b8cac09386b5df440e509b2a9aa3cd76f7` | `be2832b873106e0394abadbe64add7be4f47ee5b999b7294345c6a603d492087` |
| odd-v | 2 | 260,096 | 1560575–1820670 | `88dd53a01504b307df5fc7594d2e030637c3dda0eac45df42a427a6dbf6476f2` | `13414d3604e0626e5e5616f68899a9065a25a1e8dda63eca056d496725548d2b` |
| odd-v | 3 | 260,095 | 1820671–2080765 | `51479c0d9a0c5f05fbecbc5a29186f6a7fa1d4b9df4089ba37ebea8daa28dcd1` | `024dc39e6ec0df9ab1178bd25edd5e54eb1e3b6bac1388c1cc2db3649e1bd13b` |

The buffers remain in the sandbox workspace (`dm490/ca544/out/`); a repository payload transfer of these bytes awaits Jeremy's explicit line, per standing practice. The hashes above freeze the bytes regardless of where they sit.

## Scope flags (both sector certificates, unchanged and honest)

`artificial_Hankel_self_removed_once = true`, `raw_physical_diagonal_included_once = true`, `full_compact_pole_pairing_included_once = true`, `output_rows_owned_by_delta_component = true`, `original_infinite_seed_action_included = false`, `direct_middle_residual_evaluated = false`, `whole_action_evaluated = false`, `stationary_acceptance_met = false`, `infinite_capacity_tail_closed = false`, `v14_354_charge_repeated = false`, `global_source_v14_403_transport_charge_repeated = false`.

## Disposition

The v14.544 HANDOFF is closed. Per v14.544, the next gate is the v14.448 direct-middle residual composition of this certified compact action against the existing original seed action, testing the unchanged 3e-5 finite-plus-gap threshold only there; fresh far moments/splits and beyond-support work open only on a certified pass at that gate. Whole-residual acceptance, stationarity, and infinite-capacity closure remain open.
