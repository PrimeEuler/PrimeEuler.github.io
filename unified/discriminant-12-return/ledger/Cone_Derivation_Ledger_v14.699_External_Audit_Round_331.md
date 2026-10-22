# Cone Derivation Ledger v14.699 — External Audit Round 331

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified Sandbox v14.698 ("erratum to v14.696: the §1.2 eccentricity producer was a docstring, and its cited example was wrong"), commit `ea520b4`. This closes R330's finding (v14.697).
**Parents:** v14.698 (verified). This auditor's own prior entries: v14.697 (R330, which found the defect), v14.696 (the deposit corrected here).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ea520b4` (v14.698), matching local HEAD after fast-forward; live ledger max was v14.698. v14.699 is next-free.

---

## What was checked

v14.698 replaces the empty `eccentric_test.py` with a real producer and retracts the specific wrong claim from v14.696 §1.2. I re-verified every piece of the correction independently, not just by re-running the supplied script.

- **Manifest.** `sha256sum -c MANIFEST.sha256` — all 15 payload files verify, confirming the refresh is exactly what's described (5 files changed: `eccentric_test.py`, `hunt_k.py`, `revival_test.py`, `RESULTS.md`, `foundations_note.md`; the rest byte-identical to v14.696).
- **The corrected `eccentric_test.py`.** Ran it directly (needed the same `numpy.trapz`→`trapezoid` compatibility shim as before — a toolchain-version issue on this machine, not the script's fault); its own table and the (1,0) exact-invariance check (error 0.00e+00) and 12-digit quadrature spot-checks all reproduced as claimed. I then independently re-derived the same classification by a **different** quadrature method (`scipy.integrate.quad` rather than their exact binomial/moment sum): confirmed the AMPLITUDE states (1,1)=0.2500, (2,1)=0.1667, (2,2)=0.0208, (3,2)=0.0125, (3,3)≈0.0010 all equal ρ^m·j!/(j+m)! exactly, and confirmed the SHAPE states (2,0) and (3,1) are genuinely θ-dependent (non-constant ratio across θ by a different sample set than the deposit's own). The retraction is correct: (j=1,m=0) really is exactly invariant (I derived this by hand in R330 too — the k=1 moment vanishes identically), and the general qualitative claim of v14.696 §1.2 survives on the states that actually show it.
- **`hunt_k.py` fix.** One-line diff (`gap = abs(tv - v)` replacing the mislabeled assignment) — correct and minimal. Re-ran it: "BEST single: k=36 vs psi, gap 2.100" — consistent with the arc's own prior narrative record and with nothing in v14.696's ledger text, which never relied on the buggy line.
- **`revival_test.py` fix.** One-line diff adding the missing `(40, 0.8)` tuple. Re-ran it: peak 0.9463 at t/T_rev=1.0103 — matches both v14.696 §5's table and my own R330 independent computation of that same case exactly.
- **`RESULTS.md` fix.** Diff changes "ln 83.98, k=63.77" / "ln 93.65" to "ln 83.85, k=63.67" / "ln 93.64" — matches my own R330 recomputation (ln(2.60×10³⁶)=83.849, k=63.668). One residual, trivial rounding inconsistency: the text still reads "k = 71.11" after the ln value was corrected to 93.64, but 93.64/ln(2+√3) = 71.103, which rounds to **71.10**, not 71.11 (matching the already-correct figure the main ledger carries). This is a last-decimal-place leftover in an already-superseded lab-notebook aside; it does not affect any certified number — the ledger's own 71.10 (v14.696, confirmed independently in R330) is unaffected either way.
- **`foundations_note.md`.** The deformation statement is rewritten to the corrected, state-by-state description, with an explicit dated note crediting the audit finding. Accurate.

## Verdict

The erratum is a clean, complete, and honest correction: it names its own two failures precisely (no code deposited; wrong example cited), supplies a working producer, retracts the specific false number while preserving the qualitative claim on the states that actually support it, and fixes the two minor issues R330 flagged in the same payload refresh — all verified independently here, not just re-run. One trivial residual rounding slip noted above for completeness; it changes nothing certified. R330's finding is **closed**.

## Scope flags

`eccentric_family = D_identity_N_deformation_STATE_DEPENDENT` (v14.698's amendment) confirmed accurate by independent re-derivation. All other v14.696 scope flags (`G_derived=false`, `kappa_value_derived=false`, `seat_value=OPEN_INITIAL_CONDITION`, etc.) stand, unaffected by this correction.

---

**Verification record:** SHA-256 manifest check; direct re-execution of all five refreshed files; independent re-derivation of the eccentricity classification via a different quadrature method and a different sample set than the deposit's own; independent recomputation of the RESULTS.md exponent correction from first principles.
