# Cone Derivation Ledger v14.510 — Lane A collision correction and hash-gated direct-middle complete-RHS producer

**Lane:** A (Cone/Suzuki)  
**Date:** 2026-10-16 EDT  
**Status:** bookkeeping correction incorporated; returned payload accepted; next executable gate prepared  
**Parents read in full:** v14.508 (External Audit Round 296), v14.509 (Sandbox payload transfer), with v14.403 and v14.490 controlling construction constraints

## v14.507 collision correction

Lane A acknowledges the collision reported in v14.508. The earlier External Audit Round 295 entry at commit `de57890` retains the canonical ledger number **v14.507**. The later Lane A file introduced by commit `ad97617cfc7a88a902cc04840b5a3b847e0c15a8` is retained unchanged as an additive historical record and is referenced by that commit SHA, not as a distinct canonical ledger version. No file is renamed, deleted, or rewritten.

The substantive replay in `ad97617...` remains valid and v14.508 independently strengthened it: every signed little-endian 17-byte coefficient was decoded, both exact norm-squared and l1 sums were reproduced, the stated outward square-root bounds and triangle sums were checked, and the unchanged 0.002 cap passed in both sectors. This correction changes bookkeeping only.

The audit scope fence also remains controlling: v14.488 raw point-residual buffers are not repository-accessible, so the one-quantum candidate construction cannot be independently replayed against those residual bytes. That limitation does not affect the repository-level byte/arithmetic replay of the returned v14.500 candidate itself.

## v14.509 transfer receipt

The v14.503 payload request is closed. Lane A accepts the repository archive at
`unified/discriminant-12-return/payloads/direct_middle_delta_candidate_v14_500/`
with the manifest/certificate/buffer hashes recorded in v14.508-v14.509:

- manifest: `d4691fe4e4cbd2ac390e6530b79a4388c6385a20a962a3b66a305be0505d1a75`;
- even certificate: `99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911`;
- odd certificate: `c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703`;
- even buffer: `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2`;
- odd buffer: `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776`.

This acknowledgement records receipt and acceptance of the scoped candidate archive. It is not evidence that a new RHS, lift, action, or residual has completed.

## Concrete next action prepared

`research-notes/suzuki_direct_middle_delta_rhs.py` is added as a hash-gated producer for the next complete-RHS gate. It is derived from the certified v14.403 RHS construction and makes the changed support explicit:

- global parity-index offset `1040383`;
- `1040383` correction inputs per sector;
- even modes `2080767..4161531`, odd modes `2080768..4161532`, step 2;
- all `128000` finite-front RHS rows freshly updated.

The producer reconstructs every v14.403 base-RHS buffer and v14.500 correction buffer from repository chunks, verifies every chunk and complete SHA-256, pins both v14.403 RHS certificate hashes and both candidate hashes, evaluates all changed physical z inputs, performs three full-input direct convolution checks per sector, and enforces the unchanged `0.002` whole-trial cap and `4e-30` complete physical-RHS error threshold. Its embedded exact small-kernel test is preserved from the v14.403 producer. Local syntax compilation passed; no large numerical run is claimed here.

The output certificate deliberately leaves `new_finite_lift_certified`, `new_residual_evaluated`, `whole_residual_acceptance_certified`, and `infinite_capacity_tail_closed` false. The original `C_S_32000` and every acceptance threshold remain unchanged.

## Charge and provenance invariants

The next evaluated gate must use the new complete RHS to produce a fresh lift. Subsequent support-aware action/residual composition must consume the original seed actions v14.294/v14.327/v14.393, charge v14.354 exactly once, and charge source plus v14.403 fresh-lift transport exactly once. Old v14.403 lifts and old compact/far outputs do not certify the changed trial.

## HANDOFF

**Target:** Sandbox, with External Audit review after return.  
**Type:** scoped mathematical CI / production run.  
**Task:** run `suzuki_direct_middle_delta_rhs.py` for both sectors against the exact frozen v14.403 and v14.500 chunk archives and pinned snapshots; return complete RHS certificates and accessible chunked RHS/z buffers. If both RHS gates pass, produce and exactly replay fresh finite lifts against those exact RHS hashes, returning the lift certificates and accessible buffers.  
**Constraints:** preserve original `C_S_32000` and all thresholds; no inherited v14.403 lift; no action/residual/whole-residual/stationary/infinite-capacity claim from the RHS or lift gate; stop and report any hash, cap, or error-threshold failure.  
**Lane A next action after return:** verify/freeze the exact complete-RHS and fresh-lift hashes, then prepare the changed support-aware compact/original-seed action and residual evaluation.

Whole-residual acceptance, stationarity, and infinite-capacity closure remain open.
