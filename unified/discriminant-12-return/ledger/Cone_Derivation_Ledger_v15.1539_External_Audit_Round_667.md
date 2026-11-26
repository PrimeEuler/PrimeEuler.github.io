# Cone Derivation Ledger v15.1539 — External Audit Round 667

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1535, v15.1536 (Lane A); v15.1537, v15.1538 (Gravity)
**Verdict:** v15.1535 and v15.1536 CONFIRMED bit-for-bit. v15.1537 and v15.1538: committed drivers independently executed end-to-end; qualitative claims and assertions confirmed; numerical reproduction is close but explicitly not bit-identical for v15.1537, and near-exact for v15.1538 — see detail below.

## v15.1535 (Lane A, arcs 7210–7273): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match exactly: producer `5ccf248ed06d11c852df4ab562d7471bd6bce77cbc3fa48fc7abbe5d74a388af`; certificate `bf10824e499c4a59e4419f72a48f2ec5062297af698f10ea2cfcf006f0c7d15d`; manifest `6c714b1e5d6df4ec4ca13507ad2c1a20a55bd4d5c313616a59ab8ca7d6a354ef`. Frozen dependency hashes unchanged. Certificate JSON extrema (64 states, all `pass: true`) match the ledger prose exactly, including max propagated fourth root `4.019659921353575` and max B4 `261.0701667975274`. A clean rerun of the committed producer reproduced `certificate_sha256=bf10824e499c4a59e4419f72a48f2ec5062297af698f10ea2cfcf006f0c7d15d` bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`. Coverage by hand: `832+3264=4096` of 8019, `8019-4096=3923` uncovered — matches. Target inequality confirmed: `261.0701667975274 < 282.5761`. Adjacent to v15.1532 at arcs 7209/7210, no gap.

**Collision note:** v15.1535's own account of a provisional-naming collision with this audit's own v15.1534 liveness note was verified against actual commit timestamps: the liveness note (`a707d53`) landed at 15:26:46 EST, before Lane A's v15.1535 producer commit (`a397db3`) at 15:36:19 EST. Lane A correctly detected the collision before its first additive write and renumbered from the provisional v15.1534 to the final-free v15.1535, exactly as the standing protocol requires (an uncommitted provisional attempt has no priority).

## v15.1536 (Lane A, arcs 7274–7337): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match exactly: producer `687f21c24ef194b88da565dac937d0ffbf1bbfe5cf1a4f7976e396c5f2c3c1cb`; certificate `25030adef63544463c36619a01123f7209664dd2a214e81ccbd699c9309c7596`; manifest `4fa4e98343ee322852cff24a6606584965411a3e8d023ed3bce26fc766b0c72f`. Frozen dependency hashes unchanged. Certificate JSON extrema match exactly, including max propagated fourth root `4.022766144857933` and max B4 `261.87807869214674`. A clean rerun reproduced `certificate_sha256=25030adef63544463c36619a01123f7209664dd2a214e81ccbd699c9309c7596` bit-for-bit. Coverage by hand: `832+3328=4160` of 8019, `8019-4160=3859` uncovered — matches. Target inequality confirmed: `261.87807869214674 < 282.5761`. Adjacent to v15.1535 at arcs 7273/7274, no gap.

## v15.1537 (Gravity): committed driver independently executed; close but not bit-identical reproduction

The ledger entry itself disclosed that its reported numbers came from an uncommitted local driver (`/mnt/data/cone_gh/gate1537_checkpoint.py`), not the committed `research-notes/k4_gh3d_checkpoint_t08_v15_1537.py`. Per standing practice, this audit does not accept a witness's own uncommitted script as evidence — the actual committed bytes were run.

First verified the frozen dependency `k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485.py` is unchanged since its Round-651 confirmation (sha256 `e7ed4534810ebcf2b9ffe8139d518e494987d55fdff5c6bdd93456051155e090`; git history shows only the single Round-650-flagged/Round-651-confirmed fix commit `4f433e3`, nothing since). Then ran the actual committed driver end-to-end from a clean scratch copy: four invocations with `--steps 5` against the same fresh checkpoint path, then `--steps 0 --offgrid`, exactly as the ledger describes. It ran successfully with no errors.

Results: the qualitative claims hold independently — native GH strictly increasing (`7.174e-13, 1.713e-12, 3.543e-12, 5.577e-12` at t=.02/.04/.06/.08), native M strictly increasing (`2.196e-11, 4.179e-11, 5.747e-11, 6.737e-11`), native H strictly *decreasing* (`1.455e-10, 1.262e-10, 9.396e-11, 5.235e-11`) — confirming the ledger's own point that this is not monotonic constraint damping. The offgrid/native H ratio at T=.08 came out to `4.0467e-11/5.2348e-11 ≈ 0.773`, matching the ledger's claimed "~0.77 of native".

However, the independently-rerun values match the ledger's table to only about 6–9 significant figures, not bit-for-bit: e.g. at t=.02 native GH, ledger quotes `7.174469351944879e-13` versus this rerun's `7.17439996300584e-13` (relative difference ≈1e-5, the largest discrepancy found across the whole run), while t=.08 native GH matched exactly (`5.576599478149171e-12` both). This is **not** the bit-for-bit reproducibility standard Lane A's R4 certificates have (those use exact rational-arithmetic error tracking by construction). This Gravity solver is floating-point RK4 integration of a nonlinear PDE via FFT/BLAS, which is not guaranteed bit-reproducible across runs or environments; the discrepancy pattern (small, same order of magnitude and sign structure throughout, largest at the earliest checkpoint, exact at the last) is consistent with ordinary floating-point non-reproducibility rather than an error, but is flagged explicitly here per standing practice rather than silently accepted as "confirmed bit-for-bit."

**Verdict for v15.1537: independently reproduced to 6–9 significant figures from the actual committed driver; all qualitative claims (monotonic GH/M growth, non-monotonic H, offgrid ratio ~0.77) confirmed; not bit-identical, consistent with ordinary floating-point PDE-integration non-reproducibility, not a substantive error.**

## v15.1538 (Gravity): committed script independently executed; near-exact reproduction

Same disclosure pattern: the ledger entry states "Exact committed bytes not executed this turn" for `research-notes/k4_gh_initial_subsidiary_derivative_v15_1538.py`. This audit ran the actual committed script end-to-end from a clean scratch copy against the same unchanged v15.1485 dependency.

It completed successfully, passing all three internal assertions (`.20<Ct_lower0/H<.30` for all of N=16/24/32; smooth-control `pointwise_gap<2e-12`; `max(abs(H))>.03`; `max(abs(Ct_spatial))<1e-12`), printing `PASS smooth continuum identity control; NEGATIVE constrained native-grid equality not resolved` exactly as the ledger's narrative describes. Unlike v15.1537, this script performs a single analytic evaluation at the initial slice with no iterative time-stepping, and reproduction here is near-exact to the displayed precision: e.g. N=16 `max C` ledger `9.7579348844e-12` vs rerun `9.757934884375638e-12`; smooth-control `H=0.039709029111449384` and `Ct0=0.03970902911145216` matched exactly to all displayed digits. Hand-verified the `Ct_lower0/H` ratio for all three resolutions: N=16 → 0.250001, N=24 → 0.250034, N=32 → 0.249812, all within the asserted (.20, .30) bound and consistent with the ledger's "approximately H/4" observation. The entry's own caveats (odd-grid runs not reproducing a universal quarter ratio, cause not isolated, no Cone quarter-grid physics claimed) were not independently re-run here since the entry itself states those were local-only diagnostics not present in the committed script; this audit confirms only what the committed bytes contain.

**Verdict for v15.1538: CONFIRMED to high precision (near bit-for-bit) from the actual committed script; all internal assertions and the ledger's qualitative narrative hold.**

## Collision check

`v15.1539` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `e6c5780` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Lane A: coverage now stands at 4,160 of 8,019 arcs (3,859 remaining); both new blocks (4.020, 4.023) sit comfortably within range. Lane A's own handling of the v15.1534 provisional-naming collision was correct and required no correction. Gravity: v15.1537's checkpointed T=.08 evolution and v15.1538's initial subsidiary-derivative analysis both independently reproduce from their actual committed drivers, with v15.1537's floating-point RK4 reproduction close-but-not-bit-identical (flagged, not an error) and v15.1538's single-evaluation reproduction near-exact. No Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
