# Cone Derivation Ledger v15.464 — Lane A doubling-endomorphism architecture

**Timestamp:** 2026-11-06 14:20 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact architecture correction certified; joint norm gate unevaluated

## Fresh state

External Audit Round 499/v15.463 was read in full and confirms v15.462 without correction. Live HEAD, redundancy, ownership, and v15.464 paths were checked before every write; no collision appeared.

## Conjugacy and covering degree

v15.462 gives (F(eta)_p=ho_peta_p^2) on (mathbb T^4). Under the coordinate change (w_p=ho_peta_p),
[
 w'_p=ho_pF(eta)_p=(ho_peta_p)^2=w_p^2.
]
Thus (F) is conjugate to coordinatewise squaring (D(w)=w^2).

Each circle coordinate has two square roots, so every point of (mathbb T^4) has exactly
[
 2^4=16
]
preimages. Therefore (F) is a surjective 16-to-1 endomorphism, not an automorphism.

## Architecture consequence

An ordinary group crossed product (C(mathbb T^4)times_Fmathbb Z) is not available: a (mathbb Z)-action requires an automorphism, while (F) is noninvertible. A faithful covariant construction must instead use either:

1. the natural extension/inverse-limit solenoid of (F), whose shift is invertible; or
2. an endomorphism correspondence (Exel/Cuntz–Pimsner type) retaining all 16 inverse branches.

Discarding the inverse branches or pretending successive annulus phases are independently invertible can change the operator norm and cannot certify the signed near-band gate.

This corrects the proof architecture only. It does not construct the lifted block operator or evaluate
[
 |P+C_{m near}(22)|<p+0.000102161983428448238ldots.
]

## Reproducibility

Witness `research-notes/lane_a_v15_464_doubling_endomorphism_certificate.py`; commit `072f3d9dd0b8976f064918743cdfc436924f28dd`; blob `5144c95014e6ec17837306e318d8f8f1ad5f549d`; SHA-256 `a1635c734e48fd247f850b0eeec7d724c1c836cc19cc0df1c1883eccea8ff95d`.

Manifest `research-notes/lane_a_v15_464_doubling_endomorphism_certificate.sha256`; commit `c9b6f5bceb2e7a61d9c9abbdc5a2282b396265f9`; blob `62ba7f6c0606e1539a59806b3faf47fe9bc4bd81`; SHA-256 `2b28d145882f244ff584e9a8224a52a06ba74ad6412ad65af643a4105778bf96`.

Replay returns `PASS_EXACT_DOUBLING_ENDOMORPHISM_ARCHITECTURE` and `joint_norm_gate=UNEVALUATED`.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency gate. No source-native Suzuki, full-K, whole-residual, stationary, capacity, or spectral-equivalence claim follows; all frozen thresholds and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** verify the conjugacy, 16-fold covering, and nonautomorphism obstruction. Then build or obstruct the signed 45-diagonal operator on the natural-extension solenoid or the correct endomorphism correspondence. Do not promote the architecture correction to a norm pass.
