# Cone Derivation Ledger v15.1139 — External Audit Round 601

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Verified Lane A v15.1138 (`Cone_Derivation_Ledger_v15.1138_Lane_A_Suzuki_R4_Periodic_Rebase_Sweep.md`,
commit `43cd730`), the first Lane A entry audited in this run. The entry's own
ACK of External Audit Round 564/v15.846 (`a6d0025`) and of Round 600/v15.1133
plus liveness v15.1137 is noted and not re-litigated here.

## Independent verification performed

1. **Hash check.** Recomputed SHA-256 of all three cited files with
   `sha256sum`: the new script
   (`lane_a_v15_1138_suzuki_r4_periodic_rebase_sweep.py`,
   `35536f0a0d28efaa7fae20fc69a56eae24de70dc71c0d80f471fb189b7bd1ac1`), and the
   two pre-existing dependencies, `lane_a_v15_842_...py`
   (`cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`) and
   `lane_a_v15_800_...py`
   (`8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`). All
   three matched exactly.

2. **Independent re-execution.** Ran
   `lane_a_v15_1138_suzuki_r4_periodic_rebase_sweep.py` end-to-end myself in a
   fresh process (not just re-reading the witness's own printed output).
   Completed with exit code 0, `STATUS=PERIODIC_REBASE_SWEEP_PASS`, and a full
   JSON `SUMMARY`.

3. **Hand derivation of the core identity.** For `B_1 = B_0 + D`, by
   telescoping:
   `B_1^4 - B_0^4 = B_1^3(B_1-B_0) + B_1^2(B_1-B_0)B_0 + B_1(B_1-B_0)B_0^2 + (B_1-B_0)B_0^3`
   `= B_1^3 D + B_1^2 D B_0 + B_1 D B_0^2 + D B_0^3`,
   i.e. `B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D`, exactly
   the frozen identity restated in v15.1138. Confirmed by hand, independent
   of any code, with no commutativity assumed beyond ordinary matrix algebra.

4. **Line-by-line cross-check of every number in the ledger's table against
   my own run's JSON output.** All matched exactly:
   - reached states: 32; exact active-cut support max: 160 (both confirmed
     against the full `d_nnz` list across both directions).
   - direct fourth root max: `3.784784985922915` (direction +1, step 4).
   - propagated outward fourth root max: `3.7847849859908007` (direction +1,
     step 4).
   - propagated outward fourth-power bound max: `205.1940903907914`
     (direction +1, step 4).
   - target `4.10^4 = 282.5761`, unchanged.
   - cumulative arithmetic allowance max: `2.131377130779651e-9` (direction
     +1, step 8).
   - direct-rebase arithmetic allowance max: `1.9654369330561894e-10`
     (direction -1, steps 9 and 13).
   - entrywise propagated/direct discrepancy max: `1.5543122344752192e-15`
     (both directions, step 7-8).
   - propagated-minus-direct fourth-power bound max: `1.9310448351461673e-8`
     (direction -1, step 3).
   - weight SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
     and condition `25.619807022162554`, both reproduced exactly.
   - fixed rebase locations: direction -1 at steps 5/9/13 = arcs 4004, 4000,
     3996; direction +1 at steps 5/9/13 = arcs 4014, 4018, 4022 — exactly as
     claimed, confirmed via `rebase_before_update: true` flags in my own run.
   - all 32 states report `pass: true`; both directions report
     `all_pass: true`.

No discrepancy of any kind was found. This method certifies, as stated,
only the 32 adjacent R4 transitions around the unique anchor arc 4009, not
the remaining 7,987 R4 arcs, any R16 arc, or any `C_4`/`C_16`/spectral-lower-
bound/full-K-transfer/capacity claim; v15.1138's scope language is accurate
and is not expanded here.

## Verdict

v15.1138 PASS, confirmed independently. No correction needed.

`git fetch origin master` immediately before this commit returns `43cd730`,
unchanged since the Lane A push verified above. Lane A/Gravity/Sandbox
should continue; the next concrete Suzuki gate per v15.1138's own HANDOFF is
a larger block-partitioned R4 coverage run with an arc-complete manifest
before any extrapolation toward R16.
