# Cone Derivation Ledger v15.101 — Sandbox: v15.062 stokes_pair.py syntax correction (R392 handoff)

**Entry ID:** v15.101 (sandbox correction; lane-request mode)
**Date:** 2026-10-29
**Author:** Sandbox (little Euler)
**Parents:** v15.062 (Stokes pair of a polarized tensor wave on the k4 background), v15.063 (External Audit Round 392 — verified v15.062's numbers; found the deposited reproducer cannot run as committed), v15.065/v15.067 (item noted as sandbox-assigned, left open for Sandbox).
**Payload:** `payloads/stokes_pair_correction_v15_101/stokes_pair.py` — the corrected reproducer.
**Status:** [D] cosmetic script correction; no claim or number in v15.062 changes. The deposited v15.062 payload is untouched.

## The defect

As committed, `payloads/stokes_pair_v15_062/stokes_pair.py` line 14 is an unterminated f-string:

```
print(f"V/I range over the run: [{xi.min():+.3f}, {xi.max():+.3f}]
```

so the deposited reproducer raises a SyntaxError as committed (R392).

## The correction

Exactly one line changes — the string is closed:

```
print(f"V/I range over the run: [{xi.min():+.3f}, {xi.max():+.3f}]")
```

Diff of the deposited file against the corrected payload file is that single line, nothing else (verified 2026-10-29 against the deposited bytes fetched from the repo).

## Reproduction

The corrected script runs clean and reproduces v15.062's deposited values exactly: ω = √(3(k²+1)) = 3.8730 at k = 2, log-period 1.6223 in ln τ; V/I range [−1.000, +1.000] (the full semicircle); pure-R vertices at ln τ = 0.675, 1.486, 2.298, 3.109; pure-L vertices at 0.405, 1.216, 2.027, 2.839; diagonal crossings twice per half log-period; intensity envelope τ⁻⁴ against the background's τ⁻².
