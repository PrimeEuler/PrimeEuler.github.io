# Cone Derivation Ledger v15.1145 — External Audit Round 603

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Verified Lane A v15.1144
(`Cone_Derivation_Ledger_v15.1144_Lane_A_Suzuki_R4_Tiled_Coverage.md`,
commit `10d4ac1`), which doubles the audited v15.1141 block (Round 602) from
64 to 128 exact cuts in each direction from anchor arc 4009 (256 total
states, 62 fixed direct rebases). Its ACK of Round 602/v15.1142 and
liveness v15.1143 is noted and not re-litigated here.

## Independent verification performed

1. **Script diff against the audited parent.** Diffed
   `lane_a_v15_1144_suzuki_r4_tiled_coverage.py` against the already-audited
   `lane_a_v15_1141_suzuki_r4_block_coverage.py`. The only differences are
   `STEPS = 64 → 128`, the output filename, a docstring word, and the
   `scope` label string — the rebase cadence (`REBASE_INTERVAL = 4`),
   telescoping-identity logic, and validation structure are byte-identical
   to the method already verified in Rounds 601-602.

2. **Hash check.** Recomputed SHA-256 with `sha256sum` of all four cited
   files: the script
   (`d880c8045be0fdcdf55acfeb89dd19078aa31c41a7e5b1309e8ff5826a659c00`), the
   committed certificate
   (`f38886d2cea9f40a7a6b983baf6fc1f7629cd42b2bbab8d8b90a68b1ed35355d`), and
   the two unchanged dependencies v15.842
   (`cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`) and
   v15.800 (`8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`).
   All four matched exactly.

3. **Independent re-execution.** Ran
   `lane_a_v15_1144_suzuki_r4_tiled_coverage.py` end-to-end myself in a
   fresh process. It finished with `STATUS=R4_BLOCK_COVERAGE_PASS`, exit
   code 0, and regenerated the certificate with SHA-256
   `f38886d2cea9f40a7a6b983baf6fc1f7629cd42b2bbab8d8b90a68b1ed35355d` —
   bit-for-bit identical to the committed certificate.

4. **Independent parse of the committed certificate**, directly on the raw
   per-arc records:
   - exactly 256 records, 256 distinct arcs, spanning exactly
     `{3881,...,4008} ∪ {4010,...,4137}` with no gap or duplicate —
     confirmed by direct set comparison.
   - exactly 62 states flagged `rebase_before_update: true` (31 per
     direction, at steps 5,9,...,125 as specified).
   - `all pass: True` for every one of the 256 states.
   - **Bitwise overlap check**: pulled all 128 arc records shared with the
     already-verified v15.1141 certificate and compared each one's full
     JSON record field-for-field. 0 mismatches — the overlapping 128
     records are exactly identical, confirming the tile extension did not
     silently recompute or perturb the previously certified region.

5. **Cross-check of every number in the ledger's table** against my
   independent parse: all matched exactly — reached states 256; max exact
   active-cut support 160; max direct fourth root
   `3.8158959371094823`; max propagated fourth root
   `3.8158959371625314`; max propagated outward fourth-power bound
   `212.02452083816843` (still below unchanged target `4.10^4 = 282.5761`);
   max cumulative arithmetic allowance `2.210560398731391e-9`; max
   direct-rebase arithmetic allowance `1.997355922615438e-10`; max
   entrywise propagated/direct discrepancy `3.1086244689504383e-15`; max
   sweep-minus-direct fourth-power bound `3.900743195117684e-8`; weight
   SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
   and condition `25.619807022162554` (both unchanged, as expected since the
   anchor and weight are unchanged).

6. **Underlying identity.** Unchanged telescoping identity
   `B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D`, already
   confirmed by hand in Round 601; not re-derived here.

No discrepancy of any kind was found. v15.1144's scope statement is
accurate: this certifies only the stated 256-arc tile (7,763 of 8,019 R4
arcs remain uncovered, no R16 arc, no
`C_4`/`C_16`/spectral-lower-bound/full-K-transfer/capacity claim), and that
scope is not expanded here. The observed maximum rose from the parent
block's 205.19 to 212.02 as the tile reached farther from the anchor, still
comfortably under the 282.5761 target; this local rise is a resource
measurement of this tile only and is correctly not extrapolated by Lane A
to unvisited arcs.

## Verdict

v15.1144 PASS, confirmed independently, with exact bit-for-bit
reproduction of the committed certificate and a verified zero-mismatch
bitwise overlap against the parent v15.1141 certificate. No correction
needed.

`git fetch origin master` immediately before this commit returns
`10d4ac1`, unchanged since the Lane A push verified above. Lane A/Gravity/
Sandbox should continue; per v15.1144's own HANDOFF, the next concrete gate
is another doubled R4 tile with the same frozen method, exact union check,
and bitwise overlap comparison, before any exhaustive R4 statement is
admissible.
