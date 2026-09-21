# Cone Derivation Ledger v13.604 — Full-Precision 207900-Assignment Null Reproducibility

## Status

Compact reproducibility checkpoint for the preregistered five-candidate comparison of the frozen M=3999 12-prime Suzuki response-ray geometry. This is a finite binary64/randomization diagnostic, not a theorem or an explanatory bridge.

## 1. Frozen geometry and null

Source population:
`Q={5,7,11,13,17,19,23,29,31,37,41,43}`.

Residue multiplicities mod 12 are
`(n_1,n_5,n_7,n_11)=(2,4,4,2)`.

The null holds the 12 full-precision fingerprint rays, hence all 66 pair angles, fixed and exhaustively reassigns only these residue labels with the observed multiplicities. The assignment count has two independent exact forms:

```
12!/(2!4!4!2!) = 207900
C(12,2) C(10,4) C(6,4) = 207900.
```

Every distinct assignment occurs once.

## 2. Frozen candidates

On `{1,5,7,11}`:

- `sigma_A=(7 11)`, fixing 1 and 5.
- `sigma_B=(5 11 7)`, fixing 1.
- `T5=(1 5)(7 11)`.
- `T7=(1 7)(5 11)`.
- `T11=(1 11)(5 7)`.

The sigma candidates were fixed by the J-compatible V4 classification before this comparison. The three T candidates were independently fixed by the cone-incidence dictionary and explicitly preregistered before unblinding.

For a candidate g, pair (i,j) is selected iff
`r_j=g(r_i)` or `r_i=g(r_j)`.

## 3. Frozen score

For the selected and complementary angle sets,

```
S_g = mean(theta_other) - mean(theta_selected).
```

Positive S means the candidate-selected pairs are closer than the complement.

Full-precision observed thresholds:

| candidate | selected pairs | S_g (deg) |
|---|---:|---:|
| sigma_A | 15 | +1.9165982669856696 |
| sigma_B | 33 | -2.940076504734453 |
| T5 | 16 | +5.586570730028399 |
| T7 | 16 | -2.099438906466993 |
| T11 | 20 | -3.4257423157818536 |

The family statistic is `max_g S_g`, observed at T5:
`S_max=+5.586570730028399 deg`.

## 4. Exhaustive tail audit

Tie convention is conservative and fixed:
`p = Pr_null(S_null >= S_obs)`.
For the family statistic the same inclusive rule is applied to `max_g S_g`.
No Monte-Carlo +1 correction is used because the null is completely enumerated.

| statistic | N_> | N_= | N_>= | exact p=N_>=/207900 |
|---|---:|---:|---:|---:|
| sigma_A | 59181 | 1 | 59182 | 0.2846657046657047 |
| sigma_B | 160388 | 2 | 160390 | 0.7714766714766714 |
| T5 | 9808 | 2 | 9810 | 0.047186147186147186 |
| T7 | 155836 | 2 | 155838 | 0.7495815295815296 |
| T11 | 179808 | 4 | 179812 | 0.8648965848965849 |
| max of five | 55335 | 4 | 55339 | 0.2661808561808562 |

All rows satisfy `N_>+N_=N_>=` exactly.

The five-candidate null also gives
`E[max_g S_g]=4.540334051441723 deg`
and 95th percentile
`Q_0.95=9.57579997972845 deg`.

Therefore T5 has a nominal inclusive tail of 9810/207900, but the preregistered five-candidate familywise tail is 55339/207900. The familywise gate remains FAIL/null-consistent.

## 5. Numerical-stability and reproducibility checks

1. **Full-precision versus displayed rounded angles.** Repeating the exhaustive test after rounding each angle to 1e-4 degree changed no inclusive tail numerator and no p-value.
2. **Score perturbations from rounding.** Full-minus-rounded score changes were:
   - sigma_A: -1.3408574695e-6 deg
   - sigma_B: -7.4715869403e-7 deg
   - T5: +6.7300283924e-6 deg
   - T7: -5.9064669919e-6 deg
   - T11: +1.3798703087e-6 deg.
3. **Independent 9-decimal angle-matrix replay.** Re-enumerating all 207900 assignments from the frozen M=3999 angle matrix printed to 9 decimal places reproduced every strict-tail count, tie count, and inclusive-tail count in the table above.
4. **Combinatorial cardinality.** Multinomial and sequential-combination constructions independently give 207900 assignments.
5. **Integer-tail reconstruction.** Every reported p-value is exactly the corresponding integer inclusive numerator divided by 207900.
6. **Tie handling.** Equality is not assumed absent: the replay explicitly finds tie multiplicities 1,2,2,2,4 and 4 for the five individual candidates and family maximum respectively. Inclusive tails are therefore retained.
7. **Rounded/full family stability.** Both full-precision and rounded-angle enumerations give the identical familywise numerator 55339 and p=0.2661808561808562.

## 6. Guardrails

- T5 is the only candidate with nominal p<0.05, but it does not survive the frozen five-candidate familywise null.
- No explanatory Suzuki/cone correspondence is promoted.
- No failed chi12 phase-law result is reopened.
- This checkpoint certifies reproducibility of the finite randomization calculation only; it does not establish an asymptotic law, exact V4 symmetry of the Suzuki operator, Pell bridge, or RH/GRH consequence.
