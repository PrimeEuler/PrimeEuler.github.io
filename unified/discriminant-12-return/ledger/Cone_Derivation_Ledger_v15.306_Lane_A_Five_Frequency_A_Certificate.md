# Cone Derivation Ledger v15.306 — Lane A: exact-rational five-frequency mean-square certificate

**Date (America/New_York):** 2026-11-02  
**Lane:** A — frozen chosen counting-measure `K_full`  
**Parents:** v15.139, v15.227, v15.303–v15.305  
**Fresh pre-write master:** `da74ffa34000101bb1fc1d458f8d9082afbb6610`  
**Status:** `SCOPED_EXACT_RATIONAL_CERTIFICATE__INDEPENDENT_AUDIT_OPEN`

## Frozen executable witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_306_five_frequency_A_certificate.py`  
Witness commit: `da74ffa34000101bb1fc1d458f8d9082afbb6610`  
Git blob SHA: `9ae0cb02607521018822a10c2d9d6714f65543b6`  
SHA-256: `ee9f189479466243ac2c3849e4d0fd292b138a4c1674d996d0b1d38adff5331d`

The witness uses exact `Fraction` arithmetic after enclosing `log(q)` and `sqrt(q)` with a conservative (10^{-110}) widening at Decimal precision 120. It constructs an independent exact-rational Machin enclosure for (pi), reduces every sine argument to ([0,pi/2]), and applies alternating Taylor lower/upper sums. The special source normalization (w_4=log 2/2) is retained.

For
[
A=8sum_{qin{2,3,4,5,7}} w_q^2sin^2!left(rac{pilog q}{2}ight),
]
the evaluated exact-rational enclosure prints
[
6.70411705806156354127349965482182532075007943089580178227170
le A le
6.70411705806156354127349965482182532075032159432278195525699.
]

The following deliberately coarser rational statements are asserted and checked exactly:
[
A>rac{838}{125}=6.704,qquad
sqrt A>rac{2589}{1000}=2.589,qquad
rac{sqrt A}{2pi}>rac{103}{250}=0.412.
]

Because (c=2/pi), v15.305's persistent adjacent-entry argument therefore has the explicit scoped consequence
[
inf_N|Q_NBQ_N|>0.412
]
for admissible sharp parity-prefix cutoffs, and
[
limsup_{N	oinfty}|Q_NBP_N|>0.412.
]
The first strict inequality follows by choosing arbitrarily large adjacent indices in every tail; the second remains a subsequential statement, exactly as in v15.305.

## Upper-bound exploration and scope fence

The five-frequency adjacent asymptotic alone cannot certify an upper bound for (|Q_NBQ_N|): it controls one moving near-diagonal entry, whereas an operator-norm upper bound requires the complete all-offset kernel plus certified remainder/row-sum or a block comparison. The triangle estimate only bounds the leading adjacent oscillatory amplitude and must not be promoted to a full tail-operator bound.

Accordingly, v15.304's global (M=15) stopping rule is not improved here. No practical full-(K) cutoff, full-(K) gap, source-native Suzuki identification, whole-residual, stationarity, or capacity conclusion is claimed.

`FULL_K_TRANSFER = INCONCLUSIVE`.

The v14.405/v14.406 pass, v14.814 finite-far failure, `C_S_32000`, thresholds (3	imes10^{-5}) and (0.002), frozen hashes, and exactly-once accounting remain unchanged.

```yaml
HANDOFF:
  target:
    - external-audit
  type: five-frequency-A-exact-rational-certificate
  parent: v15.306
  witness_commit: da74ffa34000101bb1fc1d458f8d9082afbb6610
  witness_sha256: ee9f189479466243ac2c3849e4d0fd292b138a4c1674d996d0b1d38adff5331d
  status: open
  action:
    - replay the executable witness byte-for-byte
    - verify Decimal correctly-rounded widening premise
    - verify Machin and sine alternating-series directions
    - verify the 0.412 operator-entry consequence and its scope
  next_lane_a_gate:
    - derive a complete all-offset certified row or block majorant for Q_N B Q_N
```
