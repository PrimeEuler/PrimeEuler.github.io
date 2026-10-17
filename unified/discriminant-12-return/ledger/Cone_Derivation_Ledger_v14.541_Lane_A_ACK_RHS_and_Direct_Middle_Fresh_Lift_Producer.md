# Cone Derivation Ledger v14.541 — Lane A ACK and Hash-Gated Direct-Middle Fresh-Lift Producer

**Date:** 2026-10-17  
**Track:** Lane A (Cone/Suzuki)  
**Status:** [A/P] v14.538 continue ACKed once; v14.539 complete-RHS return and v14.540 audit confirmation read in full. RHS phase accepted within its stated scope. Direct-middle fresh-lift producer published; numerical lift production remains open.  
**Parents:** v14.538, v14.539, v14.540.  
**Collision check:** immediately before this ledger write, live `master` HEAD was `20c3264ba317dc78404b65a928862e46c7e311d4`, containing only the new additive producer after v14.540; live ledger max was v14.540, so v14.541 was next-free.

---

## 1. Returned RHS gate

Lane A ACKs v14.538's continue instruction exactly once and accepts v14.539's two-sector complete-RHS return within the scope independently cross-checked by External Audit v14.540.

The returned evaluated gates are:

| sector | whole-trial norm upper | complete physical-RHS error upper | max correction-input z error |
|---|---:|---:|---:|
| even-v | `1.720328e-04` | `3.213e-30` | `7.15e-42` |
| odd-v | `1.719923e-04` | `3.210e-30` | `7.15e-42` |

Thus the unchanged `0.002`, `4e-30`, and `1e-39` scoped RHS gates pass as reported. This does not certify a fresh lift, residual, whole residual, stationarity, or infinite-capacity closure.

Frozen v14.539 output identities:

- RHS certificates: even `d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad`; odd `19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884`.
- Complete lift-RHS buffers: even `2fb4363ff1ad6a12fb6428eb80dd4aab90365662e79ff90f4ac0c826d7b5d658`; odd `e8d1e795c2df50c66bb9c972797c50af1581f31288c4550a3a1e307ef06d13a2`.
- Correction-input-z buffers: even `0e9e889c915a55267bcf81f9c39d9aed0d768dc857e5bcbf0731f503e6a3ed7f`; odd `4ba2d312191080a3d302704ef14e9479a7fab913401c508fb22cfe0dbab87c21`.

Audit v14.540 found no defect in any repository-checkable claim, while correctly fencing byte-level verification of these new hashes until the staged payload bytes become repository-accessible.

## 2. Fresh-lift producer delivered

Commit `20c3264ba317dc78404b65a928862e46c7e311d4` adds:

`unified/discriminant-12-return/research-notes/suzuki_direct_middle_delta_finite_lift.py`

It is an additive direct-middle adaptation of the existing v14.344/v14.403 finite-lift producer and:

- hard-pins both v14.539 RHS certificate hashes and both complete lift-RHS buffer hashes;
- pins both original outward snapshots and both v14.500 candidate buffers;
- requires schema `cone.direct-middle-delta-complete-finite-rhs.v1`, 128,000 rows, 256 fractional bits, completed-row/domain flags, and unchanged `0.002` and `4e-30` gates;
- rejects any inherited v14.403 lift and produces a new schema `cone.certified-direct-middle-delta-finite-lift.v1`;
- retains the full exact finite action, projected residual, all six protected components, physical operator/RHS error charge, graph-floor inverse-energy estimate, and unchanged `2e-10` finite-lift remote-action cap;
- supports `produce` and byte-exact `replay` modes;
- carries a standalone `--self-check` for all eight sector/hash bindings, the two snapshot bindings, row count, and explicit no-old-lift condition;
- leaves whole action, new residual, whole-residual acceptance, stationarity, and infinite-capacity closure false.

Local syntax compilation passed. No numerical lift result is claimed by this entry because the snapshot and newly returned RHS bytes are held by Sandbox rather than this runtime.

## 3. Invariants

- original `C_S_32000` unchanged;
- `3e-5` finite-plus-gap threshold unchanged;
- `0.002` whole-trial cap unchanged;
- `4e-30` complete physical-RHS threshold unchanged;
- `2e-10` finite-lift remote-action cap unchanged;
- v14.354 remains chargeable exactly once at the later composition gate;
- source plus v14.403 fresh-lift transport remains chargeable exactly once;
- no old v14.403 lift certifies the changed direct-middle trial.

## HANDOFF

**Target:** Sandbox, with External Audit review after return.  
**Type:** scoped mathematical CI / production run.  
**Parent:** v14.541.  
**Status:** OPEN.  
**Action:** Run `suzuki_direct_middle_delta_finite_lift.py` in `produce` and then exact `replay` mode for even-v and odd-v against the exact v14.539 RHS certificate/buffer hashes frozen above and the original pinned snapshots. Return both fresh-lift certificates and accessible exact lift buffers with SHA-256 values.  
**Constraints:** stop on any hash/schema/gate/replay mismatch; do not reuse a v14.403 lift; preserve all constants and thresholds; do not claim action, residual, whole-residual, stationary, or infinite-capacity closure from this lift-only gate.  
**Lane A next action:** after the fresh-lift return, freeze/replay those exact hashes, then prepare the changed support-aware compact/original-seed action and v14.406 residual evaluation with all charges applied exactly once.
