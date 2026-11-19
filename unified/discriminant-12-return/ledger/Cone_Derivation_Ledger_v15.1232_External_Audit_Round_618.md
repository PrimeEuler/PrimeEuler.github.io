# Cone Derivation Ledger v15.1232 — External Audit Round 618

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1231 (Lane A Suzuki R4 direct-restart right extension)

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `40a93da` as the head, one new entry since Round 617/v15.1230. Read `Cone_Derivation_Ledger_v15.1231_Lane_A_Suzuki_R4_Direct_Restart_64_Right_Extension.md` in full: a further 64-state right extension (arcs 5098–5161, steps 1089–1152), using the already-audited direct-restart mechanism, correctly filed under `research-notes/` from the outset this time.

Verified:

1. **Hash check.** `sha256sum -c` against the committed manifest confirmed the producer, certificate, and both frozen dependencies match exactly: producer `601374c443...`, certificate `ad9622ba24...`, manifest `051097b40f...` (weight-bytes line reproduced in-memory, as always).
2. **Provenance re-check.** No `ledger_version` field in script or certificate.
3. **Certificate structure (parsed independently).** Exactly 64 records, arc set exactly `{5098,...,5161}`, direction +1 only, steps 1089–1152 only, 16 rebase flags at `{5098,5102,...,5158}`, max support 160, all pass.
4. **Independent script re-execution.** Ran the committed producer end-to-end. Emitted `certificate_sha256 = ad9622ba245d6d8ee9136ccf92e3d124d187b76ac23dd928024e271e61e983e5` — **bit-for-bit identical** to the committed certificate. All extrema matched: max direct fourth-root `3.9204405126557003`, max propagated fourth-root `3.9204405127041904`, max propagated B4 `236.23240625304203`, max cumulative arithmetic `2.0593468226311633e-09`, max rebase arithmetic `1.9875619412558743e-10`, max entry discrepancy `3.1086244689504383e-15`, max sweep-minus-direct B4 `1.4794323988098768e-08`, weight condition `25.619807022162554`. `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0.
5. **Union arithmetic.** Independently recomputed `{3177,...,4008} ∪ {4010,...,5161}` in Python: 832+1152 = **1,984 arcs**, leaving `8019-1984=6,035` uncovered — matches the ledger exactly. Confirmed 5097/5098 adjacency.
6. **Collision check.** `v15.1232` and "Round 618" both confirmed unused before this write.

## Verdict

**PASS.** v15.1231's mathematics, certificate, and manifest are all independently confirmed bit-exact, correctly filed under `research-notes/` from the outset. Filed R4 coverage is now `{3177,...,4008} ∪ {4010,...,5161}`, 1,984 of 8,019 R4 arcs, 6,035 uncovered. No global C4/C16 claim is made or implied.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
