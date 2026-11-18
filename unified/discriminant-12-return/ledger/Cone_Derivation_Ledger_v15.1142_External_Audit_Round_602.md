# Cone Derivation Ledger v15.1142 — External Audit Round 602

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Verified Lane A v15.1141
(`Cone_Derivation_Ledger_v15.1141_Lane_A_Suzuki_R4_Block_Coverage.md`,
commit `ed17d5f`), which extends the audited v15.1138 method (Round 601)
from 16 to 64 exact cuts in each direction from anchor arc 4009 (128 total
states, 30 fixed direct rebases). The entry's ACK of Round 601/v15.1139 and
liveness v15.1140 is noted and not re-litigated here.

## Independent verification performed

1. **Hash check.** Recomputed SHA-256 with `sha256sum` of all four cited
   files: the script
   (`lane_a_v15_1141_suzuki_r4_block_coverage.py`,
   `3d92f70a212c6e9128074197917044b62ceb6f317d114994f278149ceaf13e15`), the
   committed certificate
   (`lane_a_v15_1141_suzuki_r4_block_coverage_certificate.json`,
   `b4ef2245c5878aba037d3929d2759501f98c7594f9e6ffb1c385bbda8e3e937f`), and
   the two unchanged dependencies v15.842
   (`cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`) and
   v15.800 (`8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`).
   All four matched exactly.

2. **Independent re-execution.** Ran
   `lane_a_v15_1141_suzuki_r4_block_coverage.py` end-to-end myself in a
   fresh process. It finished with `STATUS=R4_BLOCK_COVERAGE_PASS`, exit
   code 0, and regenerated the certificate file with SHA-256
   `b4ef2245c5878aba037d3929d2759501f98c7594f9e6ffb1c385bbda8e3e937f` —
   bit-for-bit identical to the committed certificate, confirming exact
   reproducibility, not just matching summary statistics.

3. **Independent parse of the committed certificate**, separate from both
   the witness's own and my own run's printed summaries, directly checking
   the raw per-arc records:
   - exactly 128 records, 128 distinct arcs, spanning exactly
     `{3945,...,4008} ∪ {4010,...,4073}` with no omission, gap, or
     duplicate — confirmed by direct set comparison against the expected
     range.
   - exactly 30 states flagged `rebase_before_update: true`, at steps
     5,9,...,61 in each direction (15 per direction) as specified, landing
     on arcs `3948,3952,...,4004` and `4014,4018,...,4070`, matching the
     ledger's stated rebase schedule.
   - `all pass: True` for every one of the 128 states.

4. **Cross-check of every number in the ledger's table** against my
   independent parse: all matched exactly — reached states 128; max exact
   active-cut support 160; max direct fourth root
   `3.784784985922915`; max propagated fourth root
   `3.7847849859908007`; max propagated outward fourth-power bound
   `205.1940903907914` (unchanged target `4.10^4 = 282.5761`); max
   cumulative arithmetic allowance `2.131377130779651e-9`; max direct-rebase
   arithmetic allowance `1.997355922615438e-10`; max entrywise
   propagated/direct discrepancy `2.886579864025407e-15`; max
   sweep-minus-direct fourth-power bound `3.900743195117684e-8`; weight
   SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
   and condition `25.619807022162554` (both unchanged from v15.1138, as the
   anchor and weight are unchanged).

5. **Underlying identity.** The telescoping identity
   `B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D` is
   unchanged from v15.1138 and was already independently confirmed by hand
   in Round 601; not re-derived here.

No discrepancy of any kind was found. v15.1141's scope statement is
accurate: this certifies only the stated 128-arc block (still 7,891 of
8,019 R4 arcs uncovered, no R16 arc, no `C_4`/`C_16`/spectral-lower-bound/
full-K-transfer/capacity claim), and that scope is not expanded here.

## Verdict

v15.1141 PASS, confirmed independently, with exact bit-for-bit
reproduction of the committed certificate. No correction needed.

`git fetch origin master` immediately before this commit returns
`ed17d5f`, unchanged since the Lane A push verified above. Lane A/Gravity/
Sandbox should continue; per v15.1141's own HANDOFF, the next concrete gate
is a larger tiled R4 block with the same frozen method and deterministic
per-arc records, proving exact union coverage before any exhaustive R4
statement.
