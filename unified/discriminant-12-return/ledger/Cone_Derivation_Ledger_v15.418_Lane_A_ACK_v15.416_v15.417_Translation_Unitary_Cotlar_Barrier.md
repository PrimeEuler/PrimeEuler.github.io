# Cone Derivation Ledger v15.418 — Lane A ACK v15.416/v15.417 and translation-unitary Cotlar barrier

**Date:** 2026-11-05  
**Track:** Lane A / Suzuki five-frequency commutator  
**Status:** evaluated operator-representation structural barrier; frontier unchanged

## Nudge ACKs

- ACK exactly once: v15.416 (`b04019815ada1fdcfcc7a7af460abd27f54b5a72`), External Audit standing continue nudge.
- ACK exactly once: v15.417 (`ecd61f6d9c15bb54f47bc2112f75890c46d7719a`), External Audit standing continue nudge.

Both entries were read in full. Neither is a verification round or mathematical certificate, and neither introduced a correction. An initial attempt to publish this gate as v15.417 failed before any repository object or path was created; v15.417 was subsequently occupied by the second liveness note, so this publication uses the next-free additive number v15.418.

## Evaluated gate

Let `U_lambda` be translation by `lambda` on `L2(R/(2Z))`. For the 40 distinct signed pair labels from v15.414,

`U_lambda^* U_mu = U_(mu-lambda)`.

Every translation is unitary. Hence for every one of the `binom(40,2)=780` off-diagonal unordered pairs,

`||U_lambda^* U_mu|| = 1`,

even though exact Fraction enumeration confirms `mu-lambda` is nonzero modulo the label identity. Moreover the constant function is fixed by all 40 translations. Therefore distinctness of the translation labels alone supplies no operator-norm orthogonality and no Cotlar decay. Any admissible Cotlar/Gram improvement must use the signed multiplication coefficients and their translated overlap functions; it cannot replace those data by label separation.

This is an operator-representation statement, not the artificial scalar realization of v15.408/412. It nevertheless remains a structural no-go, not an estimate of the fully weighted physical cross sum.

## Frozen witness

- Path: `unified/discriminant-12-return/research-notes/lane_a_v15_418_translation_unitary_cotlar_barrier.py`
- Commit: `22bbd5d1cf142dfedc834c19f28dc574b9ad5005`
- Git blob: `492933f3b05fc3abd5c2b8305d80591e76a75679`
- SHA-256: `dba39a44138b55234885a48c59b352bf432fd33f8cc36e358cac05a954555f92`

The replay enumerates the 40 exact rational exponential labels, all 780 off-diagonal ratios, and asserts that every ratio is nonidentity. The norm-one conclusion follows exactly from unitarity, not numerical sampling.

## Next gate and scope

The next admissible gate is to construct the actual weighted terms `M_{c_lambda} U_lambda` and certify translated coefficient-overlap bounds in

`(M_{c_lambda}U_lambda)^*(M_{c_mu}U_mu)`.

Only such coefficient-aware products can yield a Cotlar matrix below the v15.405 joint-cross budget `4.249030150943723...`.

No physical cross-sum lower bound, source-canonical synthesis, full-K transfer, complete residual, stationarity, or infinite-capacity closure is asserted. The audited frontier remains `2.892017147262984` against target `2.535946`. Protected `C_S_32000`, `3e-5`, `.002`, and exactly-once transport accounting are unchanged.
