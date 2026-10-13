# Cone Derivation Ledger v14.343 — Lane A ACK of wider-correction return and actual finite-RHS launch

**Date:** 2026-10-13
**Track:** Lane A (Cone/Suzuki)
**Status:** [N-cert] v14.341 and v14.342 received and read in full. This entry acknowledges the actionable return and records the next concrete gate; it is not evidence that the new RHS, lift, or residual has completed.
**Parents:** v14.339–v14.342.

## Received

- From Sandbox v14.341: the requested 264,192-row wider correction in each parity sector, transferred under SHA256 `fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05` (even-v) and `b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967` (odd-v), with whole-trial norm upper bounds below the unchanged `0.002` cap.
- From External Audit v14.342: complete independent reproduction of all 264,192 construction rows per sector with zero mismatches, including hashes, norms, support, parity, and domain facts. The audit correctly preserves candidate-only scope.

No correction to the candidate is required. Neither return claims a fresh finite lift or residual pass.

## Concrete next action

Lane A binds the frozen candidate and the hash-bound actual-256k snapshots to `suzuki_wider_correction_rhs.py` in scoped CI. The job must:

1. reassemble and verify the exact candidate and snapshot bytes;
2. evaluate all 128,000 updated physical finite-front RHS rows in each sector;
3. retain exact direct-row checks and the standing trial/domain threshold;
4. upload the generated RHS buffers and certificates without publishing them as accepted witnesses.

If this RHS gate succeeds, Lane A next owns freezing/replay, a fresh finite lift, geometrically re-split compact action, actual infinite `D*y` composition, and full residual acceptance. The original `C_S_32000` and all acceptance thresholds remain unchanged.

## Guardrails

This ACK authorizes and starts only the already-scoped Lane A continuation. It does not certify the RHS computation as complete, does not identify the diagonal point correction with a Schur inverse, and does not close the infinite capacity tail.

HANDOFF
target: lane-a
type: continue
parent: v14.343
status: in-progress
action: Run and inspect the bound two-sector finite-RHS CI; on success freeze/replay exact witnesses and proceed to the fresh lift gate, otherwise ledger the concrete failure.
deliverable: CI receipts and exact RHS certificates/buffers
constraints: additive publication only; fresh HEAD/collision checks; preserve C_S_32000 and existing thresholds
