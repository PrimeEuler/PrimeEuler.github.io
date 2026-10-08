# Cone Derivation Ledger v14.163 — Sandbox: v14.162 Actual-Cutoff Trace Witnesses Independently Replayed

**Date:** 2026-10-08
**Track:** Sandbox / v14.162 handoff response
**Status:** [V] All four frozen actual-cutoff trace witnesses independently decoded and replayed; byte-identical to committed; all ρ≤1e-20 confirmed exactly.
**Parents:** v14.159, v14.160, v14.162.
**Collision check:** live ledger max v14.162 at write time; v14.163 is next-free. No collision.

---

## 1. Independent replay: method

Fetched the frozen namespace
`research-notes/payloads/normalized_joint_trace_run_37720158340/` read-only:
all five JSON files, all four `.json.gz.b64` witnesses, the manifest, and the
three replay scripts (`suzuki_frozen_trace_witness_replay.py`,
`suzuki_exact_represented_trace_certificate.py`,
`suzuki_trace_congruence_replay.py`). Ran the standard-library wrapper with
`--compare-reference` in an isolated directory. No repo writes; no payload
mutation.

## 2. Results [V]

- **Manifest integrity:** all four `.b64` witnesses decode (base64, validated)
  to gzip bytes whose SHA-256 matches the manifest; byte lengths match.
- **All four targets met exactly:** `all_four_targets_met_exactly: true` —
  each witness's `relative_defect_target_met_exact` passes by exact Fraction
  comparison against $10^{-20}$.
- **Byte-identical output:** the replay's JSON is SHA-256-identical to the
  committed `actual_cutoff_trace_replay.json` (`reference_byte_identical: true`).
- **ρ values confirmed** (exact rational, displayed prefix):

| Parity | Cutoff | ρ (replayed) | v14.162 table | Margin |
|---|---|---|---|---|
| even | 64000 | 2.41239843979921…e-28 | 2.41239843979921e-28 ✓ | 4.15e7× |
| odd | 64000 | 2.32359013823200…e-28 | 2.32359013823200e-28 ✓ | 4.30e7× |
| even | 128000 | 3.09873870640385…e-28 | 3.09873870640385e-28 ✓ | 3.23e7× |
| odd | 128000 | 3.01332135049361…e-28 | 3.01332135049361e-28 ✓ | 3.32e7× |

All match to every displayed digit; margins ≥32 million× as claimed.

## 3. Scope check [V]

- The replay output carries `overall_certificate_ready: false`, consistent
  with v14.162 §5: assembly (1e-4/1e-9/1e-14) and residual (1e-11/1e-15)
  ceilings remain open. Only the represented-vector trace target is closed.
- The v14.153 frozen payload was not touched; the new run uses its own
  namespace, as required.
- No source-faithful paired bound, infinite-tail result, or final Cone
  theorem is promoted by this replay — matching v14.162's stated scope.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Four actual-cutoff witnesses independently replayed;}\\
&\qquad\text{byte-identical to committed; all }\rho\leq10^{-20}\text{ exact.}\\
&\text{[V] Scope correct: trace target closed, assembly/residual still open.}\\
&\text{No obstruction. First v14.157 numerical ceiling achieved on real data.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.162
target: sandbox
status: closed
result: Four frozen actual-cutoff trace witnesses independently decoded and replayed with the committed standard-library wrapper. Manifest hashes verified; all rho<=1e-20 decisions confirmed by exact rational comparison; output byte-identical to committed replay JSON. Scope check passes: only the represented-vector trace target is closed.
constraints: None.
