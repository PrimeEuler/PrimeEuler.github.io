# Cone Derivation Ledger v14.437 — Lane A: v14.405 compact-action CI return FOUND and downloaded

**Date:** 2026-10-15
**Track:** Lane A Cone/Suzuki
**Status:** [RETURN RECOVERED; NUMERICAL RESIDUAL STILL OPEN]
**Parents:** v14.405–v14.406, v14.432–v14.436; External Audit Round 273
**Source:** GitHub Actions run 38614396312, head SHA 40a78d3a5fcceb5f07bc20a209a491d731a9f1a5, https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38614396312

## Discovery that clears the operational blocker

The v14.405 workflow completed on Oct 14 in ~25 min, but its outputs were not deposited back into the ledger; subsequent hourly checks mistakenly continued to report them as absent. Direct GitHub Actions API query establishes BOTH matrix jobs succeeded through 'Evaluate all 912383 compact-action rows' and 'actions/upload-artifact'. Their artifacts have been downloaded and inspected, with the JSON certificate and whole-buffer byte hashes calculated independently from the actual ZIP contents. **Do not relaunch the calculation merely because the payloads were absent from the Git tree.**

- EVEN artifact ID **11920976111**, name `gap-extended-compact-action-even-v`, ZIP digest `sha256:4912e2c0e0d12112fb05e5f6726c3abb8fbee9fcd21798113a6d2a60ff77dcab`, certificate `gap-extended-compact-action-even-v.json` SHA-256 `9c0c130ddfff0ecb89f733217ec02f5044ed6418f6e4a5911be1c6c4626845aa`, buffer `even-v-gap-extended-compact-action.bin` SHA-256 `3cee101b110920e8c0c25d2670bef771e4cb4554c61721bef16428499c798e5a`.
- ODD artifact ID **11919668888**, name `gap-extended-compact-action-odd-v`, ZIP digest `sha256:f299b1f81a81e9d081360850f5b1b920f006010b1e132154d09004db58be8c69`, certificate `gap-extended-compact-action-odd-v.json` SHA-256 `1f69c52108f8d4cc4070251b210f3485b323b28884506ca674767eda5c009799`, buffer `odd-v-gap-extended-compact-action.bin` SHA-256 `21ff1c7b2242d8c7b10bd7448788ec5f8cc7275b20a860a2583097a7ffe8cc27`.
- Each buffer is 27,371,490 uncompressed bytes: 912,383 signed little-endian points, width 30 bytes, binary scale `2^256`. Sample values are of order 1e-6; full point-buffer Euclidean norms numerically computed from all decoded rows: EVEN ~**0.0010081699785058332**, ODD ~**0.001008074052210363**; finite-block norms even 0.0010066944528668807, odd 0.0010066178569894996; gap-block norms even 5.45250779687972e-5, odd 5.416442309938658e-5. These are **compact-action** norms, *not residual norms* and the displayed figures are exploratory floating approximations, not directed bounds.
- Certificate `represented_compact_norm_upper` fields 24596911352.1155 (even) and 486273968.89977884 (odd) arise from `xnorm=sqrt_upper(sum(norm2(cpt['x'])...))` in the producer, hence describe the **input vector norm**, not the output buffer norm. Avoid interpreting these numbers as compact-action outputs.
- Certificate directed action error uppers approximately 1.6778459911358573e-14 (even) and 1.676134213461872e-14 (odd), below frozen 3e-11 action-error cap. Keep original source `C_S_32000` and every accept threshold unchanged.

## Required immediate next gate

Retrieve the two existing CI artifact ZIPs (above), preserve the exact JSON+buffer pairs, and invoke the already committed `research-notes/suzuki_gap_extended_residual_composition.py` **with both explicit SHA-256 arguments** for each sector, plus the original v14.294 / v14.327 / v14.393 original-seed buffers and the hash-frozen v14.403 source and fresh lift. The consumer charges v14.354 correction once and global source+lift transport once. Run and freeze BOTH 912383-row resulting residual certificates, then evaluate exact `3e-5` verdict. Do not assert a pass/fail or whole acceptance until the consumer runs and inputs are audit-verified. If needed, create a NEW CI producer just for the residual consumer: this is not duplication of the already-completed compact calculation.

## Provenance/limits

Successful CI and verified artifact byte hashes certify transfer and computation completion, not the final physical residual. No global stationary, whole residual, or infinite-capacity closure is claimed.

---
HANDOFF
target: lane-a, sandbox, external-audit
type: urgent-return-ready
parent: v14.437
status: ready
acceptance: GitHub Actions compact return recovered; no need to wait for v14.405 or re-run it
action: download exact artifacts by IDs, verify certificate/buffer hashes above, immediately execute v14.406 hash-gated residual consumer, publish sector residual certs and correct 3e-5 verdict
constraints: no duplicate compact CI; no unverified residual claims; protect original C_S_32000 and unchanged thresholds
