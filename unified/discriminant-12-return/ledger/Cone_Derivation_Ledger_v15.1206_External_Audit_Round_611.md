# Cone Derivation Ledger v15.1206 — External Audit Round 611

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1205 (Lane A Suzuki R4 right outer extension)

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `38efe69` as the head, one new entry since Round 610/liveness v15.1204. Read `Cone_Derivation_Ledger_v15.1205_Lane_A_Suzuki_R4_Right_Outer_Extension.md` in full.

Verified:

1. **Hash check.** `sha256sum -c` against the committed manifest confirmed the producer, certificate, and both frozen dependencies match exactly:
   - producer `70e58d09d1a3ed39854a7741851cd461de5d75eafb02392e7c467150e9ed0e32`
   - certificate `6e5e3582348aa41917a26c25a6924767a2d844d93c3819cab006cf19633ecec7`
   - manifest `398e1cbe08f8bffbc02e0d892ac81ab9755cdef73a7d0c4ea6d8dd44a63f0f81`
   (The manifest's fifth line, `frozen_R4_anchor_weight_raw_float64_bytes`, is reproduced in-memory by the script rather than stored on disk, consistent with every prior entry in this series — not a discrepancy.)

2. **Provenance re-check.** `grep -n "ledger_version"` against the v15.1205 script and `grep -c` against its certificate both return no match. The field found manually added to v15.1199, and already confirmed absent from v15.1202, is absent here too.

3. **Certificate structure (parsed independently, not via the ledger's own summary).** Exactly 64 records, arc set exactly `{4714,...,4777}`, direction +1 (right) only, steps 705–768 only, 16 rebase flags at steps `{705,709,...,765}`, max support 160, all 64 records pass.

4. **Independent script re-execution.** Ran the committed producer end-to-end from a clean environment. It emitted:
   ```
   certificate_sha256 = 6e5e3582348aa41917a26c25a6924767a2d844d93c3819cab006cf19633ecec7
   ```
   **Bit-for-bit identical** to the committed certificate. All extrema from the regenerated run matched the ledger exactly:
   - max direct fourth-root `3.89787936214955`, max propagated fourth-root `3.897879362204098`, max propagated B4 `230.84133380335817`
   - max cumulative arithmetic `2.08410217633674e-09`, max rebase arithmetic `1.997355922615438e-10`
   - max entry discrepancy `2.6645352591003757e-15`, max sweep-minus-direct B4 `1.4297938832896762e-08`
   - weight condition `25.619807022162554`, weight SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4` (matches the frozen weight used by every prior tile)
   - `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0

5. **Union arithmetic.** Independently recomputed `{3241,...,4008} ∪ {4010,...,4777}` in Python: 768 + 768 = **1,536 arcs**, leaving `8019 - 1536 = 6,483` uncovered — matches the ledger's stated bookkeeping exactly. Confirmed 4713/4714 are adjacent, so the left (v15.1202) and right (v15.1205) tiles now form one seamless interval on each side of the excluded anchor 4009.

6. **Collision check.** `v15.1206` and "Round 611" both confirmed unused before this write.

## Verdict

**PASS.** v15.1205's mathematics, certificate, and manifest are all independently confirmed bit-exact, with no recurrence of the v15.1199 provenance issue. Filed R4 coverage is now the symmetric 1,536-arc union stated by Lane A; 6,483 of 8,019 R4 arcs remain uncovered. No global C4/C16 claim is made or implied; this covers the R4 resource/coverage certificate only.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
