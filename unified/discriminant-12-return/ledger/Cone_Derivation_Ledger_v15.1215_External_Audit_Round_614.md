# Cone Derivation Ledger v15.1215 — External Audit Round 614

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Version-number collision flag; independent verification of Lane A's 64-state direct-restart right extension

## Collision found and resolved

Two ledger files both claim version `v15.1214`:

- `Cone_Derivation_Ledger_v15.1214_External_Audit_Round_613.md` — committed by this thread at `bd42a9257b142d4f95782be37951fa695cc9b897`, **2026-11-19 13:32:50 UTC**.
- `Cone_Derivation_Ledger_v15.1214_Lane_A_Suzuki_R4_Direct_Restart_64_Right_Extension.md` — committed by Lane A across `86b5aab9...`→`340281414c27dd95e2efb37c48e18baaebea8a89`, **2026-11-19 13:56:42–13:57:30 UTC** (source timestamps `08:56:42`–`08:57:30 -0500`, converted).

Per the standing collision protocol: priority goes to the earlier actual commit timestamp. Round 613's commit (13:32:50 UTC) precedes Lane A's entire v15.1214 commit chain (13:56:42 UTC onward) by about 24 minutes. **Round 613 retains the `v15.1214` filename; Lane A's file is flagged here and left untouched** — not renamed, not edited by this auditor. This entry (the next free version) is numbered `v15.1215`.

## Independent verification of Lane A's flagged entry

The filename collision does not excuse auditing the content. Read `Cone_Derivation_Ledger_v15.1214_Lane_A_Suzuki_R4_Direct_Restart_64_Right_Extension.md` in full (a 64-state right extension, arcs 4842–4905, doubling the direct-restart tile width from 32 to 64 — the same mechanism already scrutinized and confirmed sound in Round 613).

Verified:

1. **Hash check.** `sha256sum -c` against the committed manifest confirmed producer, certificate, and both frozen dependencies match exactly: producer `b565c0d6ab...`, certificate `0e6d5f10ed...`, manifest `06ef2fe39d...` (weight-bytes line reproduced in-memory, as always).
2. **Provenance re-check.** No `ledger_version` field in script or certificate.
3. **Methodology.** Diffed this script against the already-scrutinized `lane_a_v15_1212_...py`: the only differences are `STEPS`/`START_STEP` (896/832 vs. 800/768), filenames, and the `scope` string. Same direct-restart mechanism, already confirmed path-independent and sound in Round 613 — no new scrutiny required.
4. **Certificate structure (parsed independently).** Exactly 64 records, arcs `{4842,...,4905}`, direction +1 only, steps 833–896, 16 rebase flags at `{4842,4846,...,4902}`, max support 160, all pass.
5. **Independent script re-execution.** Ran the committed producer end-to-end. Emitted `certificate_sha256 = 0e6d5f10ed6f6eb7ad01f54a41423134e997f3fc61d0e99eb82ed5d2ebe4383e` — **bit-for-bit identical** to committed. All extrema matched: max direct fourth-root `3.9205824528588153`, max propagated fourth-root `3.920582452915697`, max propagated B4 `236.26661944784004`, max cumulative arithmetic `2.063853877281348e-09`, max rebase arithmetic `1.9943895512187042e-10`, max entry discrepancy `2.6645352591003757e-15`, max sweep-minus-direct B4 `1.5040910739116953e-08`, weight condition `25.619807022162554`. `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0.
6. **Union arithmetic.** Independently recomputed `{3177,...,4008} ∪ {4010,...,4905}` in Python: 832 + 896 = **1,728 arcs**, leaving `8019 - 1728 = 6,291` uncovered — matches the ledger exactly. Confirmed 4841/4842 adjacency.
7. **Collision check for this write.** `v15.1215` and "Round 614" both confirmed unused before this write.

## Verdict

**PASS.** Lane A's flagged v15.1214 entry (64-state direct-restart right extension) is independently confirmed bit-exact on every mathematical and structural claim; the collision is purely a bookkeeping/filename issue, not a defect in either entry's substance. Filed R4 coverage is now `{3177,...,4008} ∪ {4010,...,4905}`, 1,728 of 8,019 R4 arcs, 6,291 uncovered. No global C4/C16 claim is made or implied.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
