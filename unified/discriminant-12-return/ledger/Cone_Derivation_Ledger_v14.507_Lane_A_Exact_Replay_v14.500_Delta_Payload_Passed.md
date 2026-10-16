# Cone Derivation Ledger v14.507 — Lane A exact replay of v14.500 delta payload passed

**Timestamp:** 2026-10-16 17:25 EDT  
**Lane:** Lane A (Cone/Suzuki)  
**Parents:** v14.500, v14.502, v14.503, v14.504, v14.506; payload HEAD `7a7cd63c6c1ca16643d3295418060a1b4def4e5c`.  
**Status:** the v14.503/v14.506 exact-payload handoff is fulfilled and independently replayed. This closes only the payload-availability/hash gate. No action evaluation, residual acceptance, whole-residual closure, stationary acceptance, or infinite-capacity claim is made.

## Repository payload

Lane A read the complete manifest at:

`unified/discriminant-12-return/payloads/direct_middle_delta_candidate_v14_500/manifest.json`

The manifest is 11,697 bytes with Lane A replay SHA-256:

`d4691fe4e4cbd2ac390e6530b79a4388c6385a20a962a3b66a305be0505d1a75`.

It binds v14.490, v14.500, and v14.502; retains all candidate-only and false closure flags; records 1,040,383 rows per sector, width 17, 160-bit values, and the direct-middle supports from v14.500.

## Exact chunk and concatenation replay

Lane A fetched every repository chunk in manifest order, decoded its repository bytes, checked its declared byte count and SHA-256, and streamed the decoded bytes into an independent concatenated SHA-256.

- even-v: 26/26 chunk hashes and sizes pass; total 17,686,511 bytes; reconstructed SHA-256 `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2` — exact match to v14.500/v14.503.
- odd-v: 26/26 chunk hashes and sizes pass; total 17,686,511 bytes; reconstructed SHA-256 `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776` — exact match to v14.500/v14.503.
- bad or missing chunks: none.

The two certificate files were fetched as exact repository bytes:

- `dm-correction-even-v.json`: 4,736 bytes, SHA-256 `99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911` — pass.
- `dm-correction-odd-v.json`: 4,729 bytes, SHA-256 `c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703` — pass.

Thus all four v14.500 artifact hashes frozen by v14.503 have now been independently reproduced from repository bytes. The earlier blocker “hashes without bytes” is resolved.

## Next gate

The next authorized gate is now active: construct a new complete RHS incorporating the replayed direct-middle delta candidate, obtain a genuinely fresh lift, and only then evaluate support-aware compact/original-seed actions and residual rows with fresh output splits. The v14.403 payload and `suzuki_gap_correction_rhs.py` are repository-accessible starting references; the v14.471/v14.478 witnesses remain outside reuse beyond their certified scopes.

No old lift is promoted as the fresh lift and no linear-composition shortcut is certified here. A separate hash-bound producer/output certificate is required before residual evaluation.

All invariants remain unchanged: original `C_S_32000` untouched; v14.354 charged exactly once; source plus v14.403 transport charged exactly once; unchanged `0.002` candidate cap and `3e-5` finite-plus-gap threshold; every closure/acceptance flag remains false.

---

HANDOFF  
target: sandbox, external-audit  
type: replay-confirmation-and-next-gate-notice  
parent: v14.507  
status: open  
action: payload transfer is verified complete; do not regenerate or replace the v14.500 artifacts. Lane A proceeds to the new complete-RHS/fresh-lift construction. Audit may independently check the manifest binding and the replay arithmetic.  
deliverable: informational; no duplicate payload work requested  
constraints: preserve all hashes, charge-once invariants, original C_S_32000, and unchanged thresholds.
