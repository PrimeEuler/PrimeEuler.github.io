# Cone Derivation Ledger v15.1203 — External Audit Round 610

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1202 (Lane A Suzuki R4 left outer extension)

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `04661d8` as the head, one new entry since Round 609/liveness v15.1201. Read `Cone_Derivation_Ledger_v15.1202_Lane_A_Suzuki_R4_Left_Outer_Extension.md` in full.

Verified:

1. **Hash check.** `sha256sum` on all four frozen artifacts — `lane_a_v15_1202_suzuki_r4_left_outer_extension.py`, its certificate, its SHA-256 manifest, and the two frozen dependencies (`lane_a_v15_842_...py`, `lane_a_v15_800_...py`) — matched the committed values exactly:
   - producer `b1838460e97f214ad2bc2d9a2b434060a703971bd2a93dd2f2de338887cc3939`
   - certificate `2b549c84f5dbf199e905a30725501e6645483f9293de3b8a30b304810dbe1e71`
   - manifest `af14e8f5906de7d111d96c59b366b1cc1fb9b8dba0eb6cdff5007be442213ca8`

2. **Provenance re-check (the technique introduced after the v15.1199 finding).** `grep -n "ledger_version"` against the v15.1202 script returns no match, and the same grep against the committed certificate JSON returns no match. The manually added field found in v15.1199 does not recur here. This confirms Lane A's stated correction was applied correctly, not just claimed.

3. **Independent script re-execution.** Ran the committed producer end-to-end from a clean environment (no cached state). It completed and emitted:
   ```
   certificate_sha256 = 2b549c84f5dbf199e905a30725501e6645483f9293de3b8a30b304810dbe1e71
   ```
   This is **bit-for-bit identical** to the committed certificate's hash — the re-run reproduces the exact committed file, with no field added, removed, or changed. All stated extrema matched the regenerated run exactly:
   - 64 states, arcs 3241–3304, direction −1 only, steps 705–768
   - 16 rebase flags, at arcs `{3304,3300,...,3244}` (i.e. steps 705,709,...,765 from the other end — consistent with the ledger's 16 flags "including the exact extension anchor")
   - max direct fourth-root `3.8978793621495758`, max propagated fourth-root `3.897879362203492`, max propagated B4 `230.8413338032147`
   - max cumulative arithmetic `2.0469823756692857e-09`, max rebase arithmetic `1.997355922615438e-10`
   - max entry discrepancy `3.9968028886505635e-15`, max sweep-minus-direct B4 `1.4265395975598949e-08`
   - weight condition `25.619807022162554`, weight SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
   - `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0

   All 64 propagated fourth-moment bounds pass the `B4 < 282.5761` target, confirmed independently from the regenerated run, not merely re-read from the ledger.

4. **Certificate structure.** An independent parse of the committed certificate (not the producer's own summary) confirmed exactly 64 unique records, arcs 3241–3304 only, direction −1 only, steps 705–768 only, 16 rebase flags, max support 160 — matching the ledger's claims exactly.

5. **Collision check.** `ls` of the ledger directory confirmed `v15.1203` and "Round 610" are both unused before this write.

## Verdict

**PASS.** v15.1202's mathematics, certificate, and manifest are all independently confirmed bit-exact. The v15.1199 certificate-provenance correction (removal of the unproduced `ledger_version` field) reported in Round 609 was correctly applied: no such field appears anywhere in v15.1202's producer or certificate.

Filed R4 coverage after this round: `{3241,...,4008} union {4010,...,4713}`, 1,472 of 8,019 R4 arcs, as stated in v15.1202. No global C4/C16 claim is made or implied by this audit; this verification covers the R4 resource/coverage certificate only, per the strict boundary Lane A itself states.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check (`git fetch origin master`) performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
