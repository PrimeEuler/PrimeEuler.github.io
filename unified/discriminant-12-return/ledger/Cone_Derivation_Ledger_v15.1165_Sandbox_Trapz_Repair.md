# Cone Derivation Ledger v15.1165 — Sandbox: additive repair — v15.857's producer made NumPy-2.0-portable (np.trapz shim), outputs byte-identical

**Deposit type:** Sandbox additive repair, independently
checkable. Origin: Audit's handoff from the 2026-11-16
review — v15.857's filed producer `hj_inversion.py` calls
`np.trapz` at three sites; `np.trapz` was removed in
NumPy 2.0, so the filed producer runs only on NumPy < 2.0.
Filed at Jeremy's direction 2026-11-18.

The repair is additive: the filed v15.857 payload is
untouched. The repaired producer in this payload differs
from the filed copy by exactly two items: a five-line
shim after the imports (`_trapz = np.trapezoid if
hasattr(np, "trapezoid") else np.trapz` — the NumPy 2.0
name preferred, the old name as fallback; the rename is
the only change NumPy made to the algorithm), and the
three call sites renamed to `_trapz(`. The full diff
against the filed copy contains no other hunks.

Verification, both regimes: in this environment (NumPy
1.26.4: has `trapz`, lacks `trapezoid`) the repaired
producer's full stdout is byte-identical to the original
filed producer's, run from the staged v15.857 payload
copy; and under a simulated NumPy 2.0 (subprocess with
`np.trapz` deleted and `np.trapezoid` installed before
the run) the stdout is again byte-identical to the same
reference. The staged copy was re-executed before this
deposit with the same byte-identical result.

v15.857's results, verdict and entry stand unchanged —
no number moves; only the producer's portability is
repaired. The Audit-flagged debt is discharged.

**Payload:** `payloads/trapz_repair_v15_1165/` — Trapz_Repair_Note.md `34a4e05b531b38fd0c71343f95af0e99d2985e30e9db2bfda81ea042ce1f2108`, hj_inversion.py `102047ec2d20632786b870651bdb69b34c1e1f384b949f9de00207c4e9073cdb`.
