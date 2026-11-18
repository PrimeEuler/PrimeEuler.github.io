# Cone Derivation Ledger v15.1173 — Lane A Suzuki R4 tiled coverage

**Date:** 2026-11-18 14:35 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS` for this 1,024-arc tile only

## Audit acknowledgements and collision discipline

- **ACK External Audit Round 604 exactly once:** the audit independently reproduced the prior 512-arc Lane A certificate and found it mathematically correct, while correcting its colliding ledger label: Gravity retains v15.1147. This entry does not reuse that number and treats the prior frozen files as content-valid but version-colliding.
- **ACK External Audit Round 605 “Lane A should continue” exactly once.** No Suzuki correction was issued.
- **ACK External Audit Round 606 “Lane A should continue” exactly once.** No Suzuki correction was issued.
- **ACK External Audit Round 607 “Lane A should continue” exactly once.** No Suzuki correction was issued.
- **ACK External Audit Round 608 “Lane A should continue” exactly once.** No Suzuki correction was issued.

The 1,024-transition computation completed under a provisional local label. Before every additive write, live `master`, competing writes, and the target path were checked again. Sandbox then occupied v15.1171 and v15.1172; the first attempted write was rejected by a concurrent-HEAD conflict and deposited nothing. The artifacts were therefore renumbered before publication to the then-next-free v15.1173. No frozen file was modified.

## Gate

The audited R4 periodic-rebase method was extended from 512 to 1,024 consecutive transitions about anchor arc 4009. The certified arc set is exactly

`{3497,...,4008} union {4010,...,4521}`.

The producer performs direct rebuilds every four steps and exact sparse support updates between rebuilds. It records direct and propagated fourth-moment bounds for every arc and checks the fixed threshold

`B4 < 4.10^4 = 282.5761`.

This is a resource-scaling and coverage certificate for an R4 tile. It is not a C4 certificate over all 8,019 R4 arcs and is not the requested R16 spectral certificate.

## Reproducible result

- distinct certified arcs: 1,024
- exact coverage: 512 arcs on each side of anchor 4009; anchor excluded
- periodic rebases: 254 total (127 per direction)
- maximum exact changed-entry support: 160 directed entries
- all 1,024 propagated bounds pass `B4 < 282.5761`
- maximum direct fourth-root bound: `3.9872057023124627`
- maximum propagated fourth-root bound: `3.9872057023367504`
- maximum propagated B4: `252.74034094445568`
- maximum cumulative arithmetic allowance: `2.2586198583801566e-09`
- maximum rebase arithmetic allowance: `1.997355922615438e-10`
- maximum entry discrepancy: `4.440892098500626e-15`
- maximum sweep-minus-direct B4: `4.256645524947089e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `1219.1614054539973 / 640.4065673119101 / 294.9173121449776 / 2300.7569898499996 / 1.1762964539999814`

Independent local validation found 1,024 unique records, the exact claimed union, 254 rebase flags, no anchor record, and no failed threshold. Every one of the 512 records overlapping the Round-604-verified parent certificate was bit-for-bit identical; zero parent records were missing or changed.

## Frozen inputs and artifacts

- producer commit: `3624d6dc38668678f0553f9d0eed4de6ce1db6ce`
- certificate commit: `f408db6deb95f0cf718b5efa5508329764429b6d`
- manifest commit: `a0e4d88a25fd613991445f8a2c47cdc1761d910a`
- producer SHA-256: `e358be5a2e07630c8b48c7b7ece03d255a14c2f617070df7a9a67bfbbcfc5c1e`
- certificate SHA-256: `08740b55b25281c22504f02706aba31c29fd5b69131d5c0be52276e225db13c6`
- manifest SHA-256: `2721751a83be51313970d82a4af9057897a5c1b09bdb2591d7a36eb85ec44ef6`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight hash reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Boundary and obstruction

This substantive gate demonstrates that the exact-support periodic-rebase mechanism remains numerically and arithmetically controlled over twice the audited coverage. It leaves 6,995 of the 8,019 R4 arcs uncovered, so no global C4 conclusion follows. A fortiori it provides no C16 upper bound and does not establish `C16 < 4.10`, `||X|| < 4.242`, the five-frequency joint cross budget, a two-sided spectral bound, full-K transfer, a source-native Suzuki Phi, or any whole-residual/stationary/capacity claim.

The original v14.405/v14.406 finite-plus-gap PASS, later v14.814 far FAIL, `C_S_32000`, thresholds `3e-5` and `.002`, source hashes, and once-only charges remain untouched.

## HANDOFF to External Audit

Please independently:

1. verify all SHA-256 values and re-execute the producer;
2. verify the exact 1,024-arc union, exclusion of anchor 4009, and all 254 periodic-rebase flags;
3. compare all 512 overlapping records bit-for-bit against the prior audited certificate;
4. reproduce the extrema, support cap, arithmetic allowances, and all 1,024 threshold passes;
5. preserve the strict R4-tile-only scope.

After audit, the independently feasible next resource gate is a further doubled R4 tile (2,048 transitions) if runtime permits. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from this R4 tile is permitted.
