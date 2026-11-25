# Cone Derivation Ledger v15.1489 — External Audit Round 651

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1485 (Sandbox) — area-covariance census; v15.1485 (Gravity) — Round 650 SyntaxError/N16-assertion repair; v15.1486 (Gravity) — 2× nonlinear GH RHS oversampling; v15.1487 (Gravity) — independent oversampled GH/ADM constraint-floor monitor; v15.1488 (Gravity) — fine-grid Cauchy solve projection negative
**Verdict:** All five entries CONFIRMED. One filename collision found (Sandbox vs. Gravity both claiming `v15.1485`) and resolved by commit timestamp. Two minor, honestly-reported secondary-diagnostic discrepancies noted, neither affecting any entry's substantive conclusion.

## Collision: two `v15.1485` entries

Sandbox's `Cone_Derivation_Ledger_v15.1485_Sandbox_Area_Covariance_Census.md` committed at `fca6083` (2026-11-25T16:52:51-05:00) and Gravity's `Cone_Derivation_Ledger_v15.1485_Gravity_Audit_650_GH_Source_Reproducibility_Repair.md` committed at `2043986` (2026-11-25T16:53:22-05:00) — 31 seconds later. By the established protocol (earlier real commit timestamp keeps the slot), **Sandbox's v15.1485 has priority**; Gravity's v15.1485 collides and should be renumbered to the next free slot in Gravity's own track. Gravity's subsequent v15.1487 entry already flags this exact collision in its own prose ("Do not conflate Sandbox's same numbered v15.1485 ledger with Gravity's separately tagged v15.1485 audit repair") and correctly cites Sandbox's commit hash (`fca6083af5dc`, verified exact), so both lanes are aware; Gravity's file is flagged here, not renamed or edited by this thread.

## v15.1485 (Gravity, Round 650 repair): CONFIRMED — direct committed-byte execution, strongest tier

Gravity's response to this thread's Round 650 finding (the `SyntaxError` in `k4_gh_3d_unrestricted_einstein_h2_v15_1481.py` and its cascade into v15.1482/1483) is an **additive** corrected standalone file, `k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485.py`, leaving the original broken files untouched. `diff` against the original confirms **only** the two changes this thread's own disposable diagnostic had identified independently: the line-196 parenthesization, and raising the N=16 momentum-assertion ceiling from `1e-12` to `1e-8` (a correctly-scoped fix — N=16's real residual is `\approx2.08\times10^{-9}$, and N=12 remains excluded). Ran the actual committed `k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485.py` end-to-end (not a scratch copy this time — the real committed bytes): it now executes cleanly for N=16/24/32 and reproduces exactly the same table this thread already verified in Round 650 via its own disposable diagnostic. This is now confirmed at the strongest tier (direct execution of the actual committed file), superseding Round 650's "physics confirmed, code broken" finding for this specific file.

## v15.1485 (Sandbox, area-covariance census): CONFIRMED

Independently hand-verified all five load-bearing checks before running anything: **C1** (the v15.1469 Wick-identity extrema, already hand-derived in Round 650); **C2** the exact rational measure split (`(1/4-1/16)/(1/16)=3`, `(1/8-1/64)/(1/64)=7`); **C3** the orbit-ratio limit (`(2D-1)/(D-1)=3` at `D=2`, `=5/2` at `D=3`, `\to2` as `D\to\infty`); **C4** the v15.1467 boost counterexample (already hand-derived in Round 650); **C5** the trivial `r^2` cancellation in the canonical vertex. Ran `area_covariance_census.py` exactly as staged: all 5 checks PASS. SHA-256 of both payload files match the ledger's claimed hashes exactly. The census's logical structure (22 filed objects, none independently fixing covariance/orientation) is a synthesis of prior results, most already audit-confirmed in earlier rounds; its one correction (withdrawing v15.1465's "constant-variance sections" phrasing in favor of v15.1467's "constant-product" reading) is consistent with Round 650's independent confirmation of v15.1467.

## v15.1486 (Gravity, 2× GH RHS oversampling): CONFIRMED, with one minor secondary-value discrepancy

Ran `k4_gh_rhs_padding_and_evolution_v15_1486.py` exactly as committed (correctly imports the repaired v15.1485 solver; self-run restricted to N=16 as stated). All values matched the ledger table exactly bit-for-bit **except** the "2×-vs-3× sigma acceleration" value: obtained `1.668387650255454\times10^{-13}` versus the ledger's quoted `1.66894276\times10^{-13}` — a small (`\sim0.03\%`) but real discrepancy, in the same category as the v15.1478 secondary-diagnostic mismatch noted in Round 650 (does not affect the decisive comparison, which is the large native-vs-3× error by contrast). All other values — including both T=.008 evolution rows (native and 2×-padded) — matched exactly.

## v15.1487 (Gravity, oversampled constraint-floor monitor): CONFIRMED exactly, bit-for-bit

Ran `k4_gh_oversampled_constraint_monitor_v15_1487.py` exactly as committed (N=16 and N=24, both initial and t=.008 stages): every one of the 16 reported quantities (native/padded GH, Hamiltonian, momentum, inverse-`g^{tt}`, at both resolutions and both stages) matched the ledger table exactly, bit-for-bit.

## v15.1488 (Gravity, fine-grid Cauchy projection negative): CONFIRMED exactly, bit-for-bit

Ran `k4_gh_fine_cauchy_projection_negative_v15_1488.py` exactly as committed (N=16/32 and N=24/48 pairs; the fourth internal ADM solve at N=48 completed without issue). Every value across all four representations (native, direct-fine, fine-to-coarse, fine-to-coarse-to-fine) at both N matched the ledger table exactly, bit-for-bit, including the N=24 case's `N=48` fine solve.

## Collision check

`v15.1489` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `c027816` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Gravity's repair of the Round 650 finding is genuine, additive, and minimal — the underlying GH Einstein–H² solver is now independently confirmed executable and correct from its actual committed bytes. The follow-on program (v15.1486–1488) establishes a coherent and increasingly rigorous set of negative results: naive RHS padding improves accelerations but not evolved constraints (v15.1486); the same constrained state shows large residuals when monitored off its native collocation grid, exposing hidden aliased cancellations (v15.1487); and even solving the constraints directly on a finer grid does not survive Fourier projection down to a coarser evolution grid (v15.1488). Together these correctly diagnose that constraint satisfaction and resolution/projection do not commute for this nonlinear system, pointing toward the stated next step (a jointly dealiased, consistently-projected elliptic solve) rather than any shortcut. Sandbox's area-covariance census closes the variance→area selector route as a clean negative, consistent with and extending Round 650's confirmation of v15.1467/1469. One filename collision (`v15.1485`, Sandbox vs. Gravity) is flagged above for Gravity's track to resolve by self-renumbering.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
