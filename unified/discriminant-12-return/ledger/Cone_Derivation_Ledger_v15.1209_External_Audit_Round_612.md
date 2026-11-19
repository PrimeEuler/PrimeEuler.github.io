# Cone Derivation Ledger v15.1209 — External Audit Round 612

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1208 (Lane A Suzuki R4 left outer extension, steps 769–832)

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `472e78b` as the head, one new entry since Round 611/liveness v15.1207. Read `Cone_Derivation_Ledger_v15.1208_Lane_A_Suzuki_R4_Left_Outer_Extension.md` in full.

Verified:

1. **Hash check.** `sha256sum -c` against the committed manifest confirmed the producer, certificate, and both frozen dependencies match exactly:
   - producer `064b113743111011a497eaa4b4923527afb7996ad65c3dc149d468d554f0970c`
   - certificate `78a2d4bfdbc6496eb25750aaa72d742744b180a8207c087321ea30f7b238760c`
   - manifest `8eff9c4f77ddf677db51690bc2b9dbf9c8c1ee895d6d3d2712d92cae3e3e0d34`
   (weight-bytes line reproduced in-memory, as in every prior entry — not a discrepancy.)

2. **Provenance re-check.** `grep -n "ledger_version"` against the script and `grep -c` against the certificate both return no match. No recurrence of the v15.1199 issue.

3. **Certificate structure (parsed independently).** Exactly 64 records, arc set exactly `{3177,...,3240}`, direction −1 (left) only, steps 769–832 only, 16 rebase flags at `{769,773,...,829}`, max support 160, all 64 records pass.

4. **Independent script re-execution.** First attempt was killed at the background time limit with no output (same as the first v15.1202 attempt earlier this session); restarted with a longer timeout and completed cleanly. Emitted:
   ```
   certificate_sha256 = 78a2d4bfdbc6496eb25750aaa72d742744b180a8207c087321ea30f7b238760c
   ```
   **Bit-for-bit identical** to the committed certificate. All extrema matched the ledger exactly:
   - max direct fourth-root `3.9214348783882627`, max propagated fourth-root `3.9214348784363566`, max propagated B4 `236.47216583436088`
   - max cumulative arithmetic `1.9881963724764853e-09`, max rebase arithmetic `1.997355922615438e-10`
   - max entry discrepancy `3.1086244689504383e-15`, max sweep-minus-direct B4 `1.4155659755488159e-08`
   - weight condition `25.619807022162554`, weight SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
   - `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0

5. **Union arithmetic.** Independently recomputed `{3177,...,4008} ∪ {4010,...,4777}` in Python: 832 + 768 = **1,600 arcs**, leaving `8019 - 1600 = 6,419` uncovered — matches the ledger's stated bookkeeping exactly. Confirmed 3240/3241 adjacency, so this tile extends the existing left interval seamlessly.

6. **Collision check.** `v15.1209` and "Round 612" both confirmed unused before this write.

## Verdict

**PASS.** v15.1208's mathematics, certificate, and manifest are all independently confirmed bit-exact, with no recurrence of the v15.1199 provenance issue. Filed R4 coverage is now `{3177,...,4008} ∪ {4010,...,4777}`, 1,600 of 8,019 R4 arcs, 6,419 uncovered. No global C4/C16 claim is made or implied; this covers the R4 resource/coverage certificate only.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
