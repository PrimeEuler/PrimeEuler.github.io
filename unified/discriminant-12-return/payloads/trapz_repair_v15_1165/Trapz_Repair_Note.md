# Additive repair — v15.857's producer made NumPy-2.0-portable

Sandbox note (little Euler), 2026-11-18. Origin: Audit's
handoff from the 2026-11-16 review cycle — v15.857's
producer `hj_inversion.py` calls `np.trapz` at three
sites (lines 82, 96, 102 of the filed copy); `np.trapz`
was removed in NumPy 2.0, so the filed producer runs
only on NumPy < 2.0. Jeremy directed the filing
2026-11-18 ("file it").

## The repair

Additive only: the filed v15.857 payload is untouched.
The repaired producer, `hj_inversion.py` in this
payload, differs from the filed copy by exactly:

1. a five-line shim after the imports —
   `_trapz = np.trapezoid if hasattr(np, "trapezoid")
   else np.trapz` — preferring the NumPy 2.0 name and
   falling back to the old one (same algorithm; the
   rename is the only change NumPy made); and
2. the three call sites renamed `np.trapz(` →
   `_trapz(`.

The full diff against the filed copy is those two
items and nothing else (reproduced by `diff` at build
time; the shim and call sites are the only hunks).

## Verification

- In this environment (NumPy 1.26.4, which has `trapz`
  and not `trapezoid`): the repaired producer's full
  stdout is **byte-identical** to the original filed
  producer's stdout, run the same day from the staged
  v15.857 payload copy.
- Under a simulated NumPy 2.0 (a subprocess in which
  `np.trapz` is deleted and `np.trapezoid` installed
  before the script runs): the repaired producer's
  full stdout is again **byte-identical** to the
  reference.

v15.857's results, verdict and entry stand unchanged;
this repair changes no number, only the producer's
portability. The debt Audit flagged is discharged.

Flags: repair = ADDITIVE (filed v15.857 untouched);
diff = shim + 3 call sites, nothing else;
output_identity = BYTE-IDENTICAL in both NumPy
regimes; results_changed = NONE.
