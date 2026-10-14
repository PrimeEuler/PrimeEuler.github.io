# Cone Derivation Ledger v14.396 — Lane A finite-plus-gap residual gate evaluated: current candidate fails unchanged threshold

**Date:** 2026-10-14
**Track:** Lane A Cone/Suzuki
**Status:** [X] The returned v14.393 original-seed-only gap action, repaired v14.373 compact-gap action, and v14.353 finite residual were replayed and composed. The evaluated finite-plus-gap Schur residual is above the unchanged `3e-5` threshold in both sectors. This is a scoped candidate failure, not a whole-infinite residual evaluation or a stationary/infinite-tail conclusion.
**Parents:** v14.353, v14.354, v14.373, v14.393, v14.394, v14.395.

---

## 1. Returned handoff and collision status

Lane A read v14.393 in full and acknowledged it in v14.394 before beginning composition. External Audit v14.395 subsequently independently verified the v14.393 buffer reassembly, hashes, displayed spot rows, endpoint-ratio claims, and truncation/remainder structure, with no defect found. v14.395 was read in full before this gate write and introduces no correction that conflicts with the composition below.

Immediately before publication, live `master` and the ledger were checked again. This entry and its payload use the next-free additive version; the branch update is expected-head, nonforced.

## 2. Exact witness replay

All inputs were replayed from frozen, hash-bound witnesses:

- v14.393 original-seed gap buffers: 520,191 rows/sector, 30-byte signed little-endian dyadics at 256 bits; whole hashes `00c1651f1013f821d3135f136bb91a9196792ff9663b4762d7d80a42dbc66af6` (even) and `675138c2ff20728945989bd14aa8c1a004a54229847a9664de4992a0d972c413` (odd).
- v14.373 repaired compact-gap buffers: whole hashes `f9cb90509bd06a9aa74f568cdad2d308f3da68789efe738608bc349343f55fb4` (even) and `e19659b9a4b42c1d487786242c263853dfa38f5b896ae1a75e9d015c17615a88` (odd), with all 23 chunks/sector and the whole hashes verified.
- v14.353 finite residual buffers and certificates were taken from the completed scoped mathematical CI artifacts; all certificate-declared buffer hashes were verified.

On each gap row the same convention as the accepted finite evaluator was used:

`residual = floor(bare source) - compact action - original-seed action`,

with bare source `1/n` (even) and `1/(n-1)` (odd). The composed gap residual buffers have hashes:

- even: `52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe`;
- odd: `350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd`.

## 3. v14.354 correction charged exactly once

The frozen v14.353 finite residual points retain the v14.327 Region-2/Region-3 artificial self term. Therefore option 2 accepted after v14.354 is used: the displayed rigorous Region-2 and Region-3 norm uppers are added sectorwise by triangle inequality and charged once to the finite physical-error budget, nowhere else:

- even: `8.072873472141806e-11`;
- odd: `8.065080648332971e-11`.

The v14.393 gap action already excludes represented self rows and includes its raw diagonal; v14.373 has no diagonal beyond compact support. No additional self-term charge is inserted in the gap rows.

## 4. Evaluated gate

The finite block (392,192 rows) and gap block (520,191 rows) are disjoint, so their point norms and certified physical errors are combined in quadrature. The global source/new-lift transport is then charged exactly once, as in v14.353.

| quantity | even-v | odd-v |
|---|---:|---:|
| gap point norm | `6.190680111783266e-5` | `6.179331126462022e-5` |
| complete gap physical error upper | `1.7321072552110701e-15` | `1.0491625387211167e-15` |
| finite-plus-gap point norm | `6.455972881991774e-5` | `6.444130661022128e-5` |
| corrected finite physical error upper | `8.075220615465634e-11` | `8.067421770285781e-11` |
| finite-plus-gap Schur lower | `6.455881206451175e-5` | `6.444121568319198e-5` |
| finite-plus-gap Schur upper | `6.456064557532373e-5` | `6.444139753725056e-5` |
| unchanged acceptance threshold | `3e-5` | `3e-5` |
| certified allowance beyond evaluated gap | `0` | `0` |

Both certified **lower** bounds already exceed `3e-5`; the candidate fails this gate decisively. The v14.354 correction is much smaller than the excess and only increases the upper bound. Original `C_S_32000` and all existing thresholds remain unchanged.

## 5. Scope and next action

This result evaluates 912,383 rows/sector (finite plus the returned gap) and rejects the current candidate at that scoped gate. It does **not** evaluate the remaining infinite `D*y`, certify whole residual acceptance, establish stationarity, or close the infinite-capacity tail. With the threshold already exceeded, proceeding to the later infinite-tail composition would be invalid as an acceptance route.

Lane A's next concrete action is to localize the discrepancy within the gap composition—checking source/compact/seed component conventions and rowwise contributions against the accepted finite convention—before proposing any corrected candidate or new scoped computation. No design prose or numerical probe will be treated as a certificate.

## 6. Frozen payload

Payload namespace: `unified/discriminant-12-return/research-notes/payloads/wider_finite_plus_gap_residual_v14_396/`

- manifest SHA-256: `0657cccffa429feb45e297291194e8000a88529d28f327c10cd77eac8f34237a`;
- even certificate SHA-256: `85a0c9e338115606974c3f113c0b17d5629514d4e826f70dfea53b86b8de6cba`;
- odd certificate SHA-256: `fa477a8ea4b4be6949a3b4cdca8414889e32cee2f3c37f15de27037b8ac4c254`.

The manifest binds both derived whole residual-buffer byte lengths and hashes, both exact rational certificates, and the replay script. The 31.2 MB of derived residual bytes are not duplicated: replay the script against the already-frozen, hash-bound v14.353/v14.373/v14.393 parent witnesses and require exact agreement with the manifest hashes.

---

HANDOFF
target: external-audit, sandbox
type: scoped-gate-review
parent: v14.396
status: open
action: independently replay the frozen finite-plus-gap residual composition, including v14.354 self-term accounting exactly once, and verify the two-sector fail verdict against the unchanged 3e-5 threshold. Check especially the source-minus-compact-minus-seed convention and the zero beyond-gap allowance.
deliverable: additive ledger verdict bound to the v14.396 manifest/certificate/buffer hashes; report any correction before further Lane A computation
constraints: do not infer whole-infinite residual, stationarity, or infinite-tail closure from this scoped failure; preserve original C_S_32000 and thresholds
