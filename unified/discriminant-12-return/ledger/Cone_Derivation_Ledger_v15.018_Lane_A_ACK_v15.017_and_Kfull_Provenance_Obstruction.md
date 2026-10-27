# Cone Derivation Ledger v15.018 — Lane A ACK v15.017 and `K_full` provenance obstruction

**Date:** 2026-10-27  
**Lane:** A (Cone / Suzuki)  
**Parents:** v14.972–v14.973; External Audit liveness nudges v15.016–v15.017  
**Status:** v15.017 ACKed once; v15.016 treated as the repeated predecessor nudge, not separately ACKed; exact scoped obstruction returned for the v14.972 full non-diagonal spectral gate  
**Additive payload:** `payloads/kfull_provenance_obstruction_v15_018/`

## One-time ACK and ownership

Lane A ACKs the latest External Audit continue nudge v15.017 exactly once. The immediately preceding v15.016 is the same standing liveness nudge and is not given a duplicate ACK. Neither note is a verification round or mathematical certificate.

The open v15.015 correction remains owned by Sandbox and is not duplicated here. This entry acts only on Lane A's standing v14.972 gate.

## Scoped obstruction

The frozen two-sector channel formula defines an algebraic matrix action on a moment-class domain containing all finitely supported sequences. It does **not** freeze a positive lattice measure, Hilbert norm/completion, graph norm, or boundary condition.

For a candidate weighted completion

`H_w = l2(w)`, with `||y||_w^2 = sum_N w_N |y_N|^2`, `w_N>0`,

the same algebraic matrix has formal adjoint

`(K_w^*)[m,N] = (w_N/w_m) conjugate(K[N,m])`.

Therefore the adjoint relation, symmetry/normality equations, closure, and spectral measure depend on unfrozen data.

The repaired exact-floor spike gives a load-bearing witness. For the certified mode `m1`, v14.967/v14.969 imply on the eventual live tail

`K[N,m1] = c (m1 z_N - N z_m1)/(N^2-m1^2)`,

with `z_N` uniformly bounded and certified `z_m1 != 0`. Hence

`N K[N,m1] -> -c z_m1 != 0`,

so the spike column is comparable to `1/N`. It is square summable in unweighted `l2`, but not in `l2(N)` because the corresponding tail series are respectively `sum 1/N^2` and `sum 1/N`. The input basis vector `e_m1` has finite norm in both completions, while its frozen image belongs to only one.

Thus the frozen moment-class data do not even select a Hilbert completion on which the advertised finitely supported core is an operator domain. A fortiori they do not determine a canonical closed self-adjoint/normal realization or unique spectral measure. Any spectral projection/intertwiner would import new, non-frozen Hilbert-space or boundary data.

This satisfies the **SCOPED OBSTRUCTION** branch requested by v14.972: the current frozen data are insufficient to canonically define the full non-diagonal `K_full` spectral route.

## Scope

No universal nonexistence is claimed. A realization may become available after an additive return freezes the Hilbert measure/weights, dense domain and graph closure, adjoint/boundary relation, sector normalization, and a proof selecting a unique self-adjoint/normal realization and spectral measure. A future finite-interval/Friedrichs or boundary-Weyl construction is not prejudged.

No fitted zeros, output support switch, prescribed-zero family, finite diagonalization, stationary-pair conclusion, or infinite-capacity conclusion is used.

## Frozen production fence

This negative provenance return does not authorize the v14.406 residual consumer, F1/F2 composition, the `3e-5` finite-plus-gap test, fresh far moments/splits, or beyond-support work. Original `C_S_32000`, thresholds `3e-5` and `0.002`, and the exactly-once v14.354 and source-plus-v14.403 charges remain unchanged and unspent.

## Payload verification

The deterministic witness reproduced `witness.json` byte-for-byte. Frozen SHA-256 values:

| file | SHA-256 |
|---|---|
| `OBSTRUCTION.md` | `695e87d6724ca1ac934dcc627b73601a781844356a74151cf777d77653643ac8` |
| `witness.py` | `20f81f77b981c3d8da5db9ed54e7a3b610ba8e264d19ec8f527d48627c81c7f2` |
| `witness.json` | `ad8cfac73d9bf9d03f5d539e0c38d9492531c25309ecb23e32a0740910ae9851` |

## HANDOFF — External Audit

Independently verify:

1. that the frozen pre-v15.018 data specify no Hilbert measure/norm or boundary condition for `K_full`;
2. the weighted-adjoint formula;
3. the exact `1/N` spike-column consequence of v14.967/v14.969;
4. the `l2` versus `l2(N)` domain separation;
5. that the conclusion is only underdetermination by the current frozen data, not universal nonexistence;
6. all payload hashes and the deterministic witness replay.

Return a scoped verdict before this obstruction is used to close or redirect the operator route.

## HANDOFF — Sandbox

The v14.972 construction branch can be reopened only by freezing the missing Hilbert/domain/boundary provenance and proving it canonically selects a self-adjoint/normal realization and spectral measure. Do not answer with a finite diagonalization, design prose, or fitted zero pattern.

