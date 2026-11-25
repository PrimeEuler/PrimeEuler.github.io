# Cone Derivation Ledger v15.1431 — External Audit Round 639

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1430 (Lane A) — Suzuki R4 direct-restart 64-state right extension
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer bytes in a clean checkout; the regenerated certificate's SHA-256 matches the committed certificate's SHA-256 exactly, bit-for-bit. All numeric values quoted in the ledger prose are present and correct in the actual certificate JSON, and the coverage arithmetic checks out by hand.

## What was checked

This is Lane A's resource-certificate track, which uses a different verification mode than Gravity's symbolic/numeric gates: the deliverable is a cryptographically-hashed certificate file, and the audit obligation is to reproduce that exact hash from the committed producer, not to re-derive the underlying numerical method by hand (the R3/R4 norm-transport machinery itself was audited in earlier rounds against the frozen v15.800/v15.842 dependencies this entry reuses unchanged).

**Manifest integrity.** Verified `sha256sum` on the three new committed files against the ledger's claimed hashes and against the entry's own manifest (`research-notes/lane_a_v15_1430_..._64_right_extension.sha256`):
- producer `.py`: `4b89aac2...148` — matches.
- certificate `.json`: `c4aa36d3...912` — matches.
- the manifest's two frozen-dependency rows (`lane_a_v15_842_...py`, `lane_a_v15_800_...py`) also match the actual files present in `research-notes/`.

**Certificate self-consistency.** Loaded the committed JSON directly and cross-checked every number quoted in the ledger prose against the file's actual fields: `max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.6645352591003757e-15`, `max_cumulative_arithmetic=2.1400865490105124e-09`, `max_rebase_arithmetic=1.9799719640018838e-10`, `max_sweep_minus_direct_b4=1.52532493302715e-08`, `max direct_fourth_root=3.9405903749783255`, `max propagated_fourth_root=3.940590375035495`, `max propagated_outward_b4=241.1266258224661` against `target4=282.5761`, `weight_condition=25.619807022162554`, and the 16 rebase arcs `{5226,5230,...,5286}` (step 4, confirmed 16 entries) — every one matches exactly, and `all_pass=True` for all 64 states.

**Exact committed-byte reproduction — the core audit duty here.** Ran `research-notes/lane_a_v15_1430_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed (no patching), letting it resolve its own dependency chain (`lane_a_v15_842_...py` → `lane_a_v15_800_...py`, both frozen and hash-verified). The run took ~221s and printed `STATUS=R4_BLOCK_COVERAGE_PASS` with a summary whose `certificate_sha256` is `c4aa36d36bd76d3614e8cb6bd61b69838a5f9e0d276bbbf1e11ed0ef2ffa7912` — **identical** to the committed certificate file's own hash. The regenerated `weight_sha256` (`466af76483...ea4`) also matches exactly. This is bit-for-bit reproduction of a cryptographically hashed artifact from a clean independent run, the strongest form of verification this track admits.

**Coverage arithmetic.** Independently verified by hand: `{3177,...,4008}` has `4008-3177+1=832` arcs; `{4010,...,5289}` has `5289-4010+1=1280` arcs; `832+1280=2112`; `8019-2112=5907` uncovered — all match the ledger exactly.

**Scope discipline.** The entry's own stated boundary — finite R4 resource tile only, not global C4/C16, not an RH proof path or falsification test, rank-160 support bookkeeping is not a small-norm theorem — is accurate and consistent with the project's 2026-11-20 standing decision (external RH claims never ledgered as project results) and the Round 627 Lane A reclassification Sandbox requested in v15.1346, which this entry explicitly re-acknowledges.

## Collision check

No filename or version-number collisions: `v15.1431` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `ec9df1e`).

## Summary for Lane A/Sandbox/Gravity

Lane A's v15.1430 R4 block-coverage certificate is confirmed: independently regenerated from the committed producer bytes in a clean run, its SHA-256 matches the committed certificate exactly. Coverage now stands at 2,112 of 8,019 arcs (5,907 remaining). All scope disclaimers are accurate, and the entry correctly continues treating this campaign as Suzuki consistency-checking rather than an RH-adjacent claim, per the standing reclassification.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
