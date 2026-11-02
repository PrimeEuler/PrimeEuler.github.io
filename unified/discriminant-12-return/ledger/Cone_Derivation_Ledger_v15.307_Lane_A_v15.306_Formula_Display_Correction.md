# Cone Derivation Ledger v15.307 — additive correction to v15.306 formula display

**Date (America/New_York):** 2026-11-02  
**Lane:** A — frozen chosen counting-measure K_full  
**Parent:** v15.306  
**Fresh pre-write master:** ed811bac5c023649e9ffdb5b721fdea36a08533d  
**Status:** FORMULA_DISPLAY_CORRECTION_ONLY__NUMERICAL_CERTIFICATE_UNCHANGED

Post-write verification found that the repository write path stripped Markdown backslashes from the displayed formulas in v15.306. The executable witness, its hashes, its evaluated output, and the mathematical conclusions were not changed. This additive entry supplies the authoritative plain-text formulas and scope.

The certified constant is:

```text
A = 8 * sum over q in {2,3,4,5,7} of
        w_q^2 * sin^2(pi * log(q) / 2)

w_2 = log(2)/sqrt(2)
w_3 = log(3)/sqrt(3)
w_4 = log(2)/2
w_5 = log(5)/sqrt(5)
w_7 = log(7)/sqrt(7)
```

The evaluated exact-rational enclosure is:

```text
6.70411705806156354127349965482182532075007943089580178227170
<= A <=
6.70411705806156354127349965482182532075032159432278195525699
```

The exact assertions checked by the frozen witness are:

```text
A > 838/125 = 6.704
sqrt(A) > 2589/1000 = 2.589
sqrt(A)/(2*pi) > 103/250 = 0.412
```

Because c = 2/pi, the authoritative scoped operator consequences are:

```text
inf_N ||Q_N B Q_N|| > 0.412
limsup_(N -> infinity) ||Q_N B P_N|| > 0.412
```

The first statement applies to admissible sharp parity-prefix cutoffs. The second is subsequential and is not a uniform lower bound for every N.

Frozen witness:

```text
path: unified/discriminant-12-return/research-notes/lane_a_v15_306_five_frequency_A_certificate.py
commit: da74ffa34000101bb1fc1d458f8d9082afbb6610
git_blob_sha: 9ae0cb02607521018822a10c2d9d6714f65543b6
sha256: ee9f189479466243ac2c3849e4d0fd292b138a4c1674d996d0b1d38adff5331d
```

The upper-bound scope fence from v15.306 is unchanged: adjacent-entry asymptotics alone do not upper-bound ||Q_N B Q_N||. A complete all-offset kernel row/block majorant with certified remainders is still required. Therefore v15.304's M = 15 stopping rule is not improved and FULL_K_TRANSFER remains INCONCLUSIVE.

No v14.405/v14.406 replay occurred. The v14.814 finite-far failure, C_S_32000, thresholds 3e-5 and 0.002, frozen hashes, and exactly-once accounting remain unchanged.

```yaml
HANDOFF:
  target:
    - external-audit
  type: five-frequency-A-exact-rational-certificate
  parent: v15.307
  supersedes_display_formulas: v15.306
  witness_commit: da74ffa34000101bb1fc1d458f8d9082afbb6610
  witness_sha256: ee9f189479466243ac2c3849e4d0fd292b138a4c1674d996d0b1d38adff5331d
  status: open
  action:
    - replay the executable witness byte-for-byte
    - audit the corrected plain-text formulas and scope
```
