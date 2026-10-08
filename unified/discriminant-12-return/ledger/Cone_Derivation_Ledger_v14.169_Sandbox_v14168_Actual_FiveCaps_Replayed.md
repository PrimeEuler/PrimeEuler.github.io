# Cone Derivation Ledger v14.169 — Sandbox: v14.168 Actual 64k/128k Five Caps Independently Replayed

**Date:** 2026-10-08
**Track:** Sandbox / v14.168 handoff response
**Status:** [V] Full independent replay of all four actual full-vector witnesses and the paired interval; byte-identical to committed; all six numerical targets pass on all four rows; paired interval strictly negative within 9e-10.
**Parents:** v14.155–v14.168.
**Collision check:** live ledger max v14.168 at write time; v14.169 is next-free. No collision.

---

## 1. Full independent replay: method

Fetched the complete frozen namespace
`research-notes/payloads/exact_outward_run_37791856005/` read-only: manifest,
CI provenance, all four parent JSONs, all four full certificates, the paired
JSON, the committed replay reference, and all 64 base64 ZIP parts (~64MB).
Downloaded the five replay scripts
(`suzuki_frozen_outward_witness_replay.py`,
`suzuki_exact_outward_certificate.py`,
`suzuki_exact_outward_pair_certificate.py`,
`suzuki_exact_integer_source_action.py`,
`suzuki_trace_congruence_replay.py`). Ran the standard-library wrapper with
`--compare-reference` in an isolated directory. No repo writes.

## 2. Results [V]

- **Manifest integrity:** all file hashes and byte lengths verified; all four
  ZIP snapshots decode and hash-match.
- **All six numerical targets pass on all four rows:**
  `all_rows_meet_all_six_numerical_targets_exactly: true`
  (five caps + trace, even/odd × 64k/128k).
- **Byte-identical certificates:** `all_certificates_byte_identical: true` —
  all four certificate files reproduce exactly from the decoded snapshots.
- **Byte-identical reference:** this thread's output is SHA-256-identical to
  the committed `outward_replay.json`.
- **Scope flag correct:** `overall_certificate_ready: false`, matching the
  entry's stated independent-audit gate.

## 3. Cap values: independently confirmed [V]

All 20 cap values (5 caps × 4 rows) extracted from this thread's own run
match v14.168 §3's table to every displayed digit and pass their targets:

| Target | 1e-4 | 1e-9 | 1e-14 | 1e-11 | 1e-15 |
|---|---|---|---|---|---|
| even/64k | 3.59e-7 ✓ | 1.05e-11 ✓ | 3.07e-16 ✓ | 6.19e-14 ✓ | 1.81e-18 ✓ |
| even/128k | 4.66e-7 ✓ | 1.36e-11 ✓ | 3.97e-16 ✓ | 1.02e-13 ✓ | 2.97e-18 ✓ |
| odd/64k | 1.43e-10 ✓ | 4.14e-15 ✓ | 1.20e-19 ✓ | 4.74e-15 ✓ | 1.37e-19 ✓ |
| odd/128k | 1.85e-10 ✓ | 5.36e-15 ✓ | 1.56e-19 ✓ | 1.43e-14 ✓ | 4.13e-19 ✓ |

## 4. Paired interval: independently confirmed [V]

From this thread's own run, exact rational comparison:

- Interval: $[-7.0867924675989616\times10^{-10},
  -7.0866618557091350\times10^{-10}]$ — matches v14.168 §4.
- Strictly negative: **True** (upper endpoint $<0$).
- Absolute bound $7.0867924675989616\times10^{-10}\leq9\times10^{-10}$:
  **True by exact rational comparison.**
- Point odd-minus-even increment $-7.0867271616540483\times10^{-10}$:
  matches v14.168.
- Endpoint error sum $6.5305944913\times10^{-15}$: matches v14.168.

## 5. Symmetry flag: resolved and confirmed [V]

v14.167 flagged that exact $A_0$ symmetry needs antisymmetric $T_0$.
v14.168 §1 resolves it: the implementation constructs
$T_0(k)={\rm sign}(k)\cdot{\rm floor}(2^{256}/(2|k|))$ — signed-magnitude
truncation toward zero, not floor toward $-\infty$. Verified:
$T_0(-k)=-T_0(k)$ holds exactly for all $k$, hence $A_0$ is exactly
symmetric. The v14.167 flag is closed; no producer change was needed.

## 6. Scope

This replay confirms the finite 64k-to-128k octave: all six v14.157
numerical ceilings now have actual endpoint evidence, and the paired
interval is strictly negative within the 9e-10 budget. The independent
audit gate (`overall_certificate_ready`) remains for External Audit.
No infinite-tail conclusion or final Cone theorem is promoted.

## 7. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Four actual full-vector witnesses fully replayed from snapshots;}\\
&\qquad\text{byte-identical certificates and reference output.}\\
&\text{[V] All 20 caps match v14.168's table; all six targets pass on all rows.}\\
&\text{[V] Paired interval strictly negative, }|\cdot|\leq9\times10^{-10}
\text{ exact.}\\
&\text{[V] v14.167 symmetry flag resolved: }T_0\text{ exactly antisymmetric.}\\
&\text{No obstruction. Finite-octave numerical closure achieved on real data.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.168
target: sandbox
status: closed
result: Four frozen actual full-vector witnesses independently decoded and replayed from the committed snapshots with the standard-library wrapper. All manifest hashes verified; all six numerical targets pass on all four rows; all certificates and the reference output reproduce byte-identically; the paired interval is confirmed strictly negative within 9e-10 by exact rational comparison; the v14.167 symmetry flag is confirmed resolved by the signed-magnitude T0 construction. No obstruction.
constraints: None.
