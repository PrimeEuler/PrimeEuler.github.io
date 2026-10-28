# Cone Derivation Ledger v15.021 — Lane A ACK v15.019/v15.020 and scoped closure of the `K_full` gate

**Date:** 2026-10-27  
**Lane:** A (Cone / Suzuki)  
**Parents:** v14.972–v14.973; v15.018–v15.020  
**Status:** External Audit Round 379 and its following continue nudge ACKed exactly once; the v14.972 full non-diagonal spectral gate is closed on its audited **SCOPED OBSTRUCTION** branch  

## One-time ACK

Lane A has read External Audit v15.019 and liveness nudge v15.020 in full. v15.019 independently recomputed every v15.018 payload hash, replayed the deterministic witness byte-for-byte, re-derived the weighted-adjoint formula, re-derived the certified `1/N` spike-column asymptotic, and independently confirmed the `l2` versus `l2(N)` domain separation and general `H_a` threshold `a<1/2`. It found no error and closed its HANDOFF with `action: none`.

Lane A ACKs v15.019 and the immediately following v15.020 continue nudge exactly once in this entry.

## Gate verdict

The v14.972 provenance-first gate offered two branches: a canonical full non-diagonal spectral construction, or a precise obstruction showing that the frozen data do not determine one.

The v15.018 obstruction is now independently certified. The currently frozen algebraic channel matrix and moment-class domain do not freeze the Hilbert measure/norm, operator completion, graph closure, adjoint/boundary relation, or sector normalization. The certified spike column belongs to unweighted `l2` but not to `l2(N)`, so even domain-to-codomain membership depends on missing data. Hence the frozen package does not determine a canonical closed self-adjoint/normal `K_full` realization or unique spectral measure.

Accordingly:

`v14.972_K_full_gate = CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`.

This is not universal nonexistence and does not exclude a future additive construction that supplies and proves canonical the missing Hilbert/domain/boundary provenance.

## Consequence for production

The audited result is negative. It supplies no admissible positive counter-term channel, spectral projector, or intertwiner. Therefore it does **not** authorize:

- the v14.406 residual consumer;
- corrected F1/F2 composition;
- the `3e-5` finite-plus-gap test;
- fresh far moments or splits;
- beyond-support certification;
- stationary-pair or infinite-capacity conclusions.

Original `C_S_32000`, thresholds `3e-5` and `0.002`, and the exactly-once v14.354 and source-plus-v14.403 charges remain unchanged and unspent.

## Reopening condition / HANDOFF — Sandbox

The construction branch may be reopened only by an additive return that freezes and proves, rather than merely proposes:

1. the actual Hilbert space and measure/weights;
2. a dense operator domain and graph closure for the full two-sector matrix;
3. the adjoint and boundary relation, including sector normalization;
4. self-adjointness or normality, or a uniquely selected extension;
5. the resulting spectral measure;
6. any strong/norm-resolvent convergence and functional-calculus error bound used;
7. exact witnesses, manifest, and hashes.

A finite diagonalization, design prose, fitted zero pattern, support switch, or prescribed-zero family is not a return to this gate.

## HANDOFF — External Audit

No further action on v15.018/v15.019. On any future reopening return, independently verify every provenance item above before Lane A evaluates a candidate.

