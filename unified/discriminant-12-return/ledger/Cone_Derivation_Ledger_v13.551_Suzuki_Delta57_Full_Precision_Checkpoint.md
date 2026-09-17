# Cone Derivation Ledger v13.551 — Suzuki Δ57 full-precision checkpoint

**Status:** reproducible finite numerical diagnostic; no theorem promotion.

This checkpoint records the full-binary64 `M=3999` fixed-full-`D` character-space exchange coordinate for the two dominant source-pair strata `(2,3)` and `(3,5)`.  The reproducer is

`research-notes/suzuki_unit_core_delta57_checkpoint.py`.

It rebuilds the source-faithful pole-free finite-high Suzuki matrix, freezes the full block-diagonal Cholesky whitening metric, computes each star's leading pair-response singular vectors, resolves the response over unit cores `(1,5,7,11)`, and applies `H4/2` to obtain the three nonprincipal coordinates

`x=(a,b,c)=(x_{chi_-4},x_{chi_-3},x_{chi_12})`.

## Exact algebraic reduction

With projective Hadamard overlaps

`C(x,v)=|x·v|/(||x|| sqrt(3))`, `v5=(1,-1,-1)`, `v7=(-1,1,-1)`, define

`Delta57(x)=C(x,v7)^2-C(x,v5)^2`.

Direct expansion gives the exact identity

`Delta57 = 4 (a-b) c / [3 (a^2+b^2+c^2)]`.

This identity is algebraic; the `a,b,c` supplied by the Suzuki computation below are numerical binary64 midpoint data.

## Reproduced M=3999 values

| pair | star | Delta57 |
|---|---:|---:|
| (2,3) | 1 | -0.9029267235997576 |
| (2,3) | **5** | **+0.5359576668827004** |
| (2,3) | 7 | -0.7250522420661470 |
| (2,3) | 11 | -0.6151381598919492 |
| (3,5) | 1 | -0.9408356856671705 |
| (3,5) | **5** | **-0.02861044046328676** |
| (3,5) | 7 | -0.8192276598694792 |
| (3,5) | 11 | +0.1146480703384783 |

The `(2,3)` class-5 response is uniquely and strongly on the `v7` side of the `v5/v7` projective bisector among its four stars.  The `(3,5)` class-5 response is close to that bisector; stars 1 and 7 remain strongly on the `v5` side, while star 11 is modestly positive.

For orientation, the recomputed class-5 character vectors are approximately

`x_5^(2,3)=(-0.17249234..., +0.32730898..., -0.12207585...)`,

`x_5^(3,5)=(-0.13841193..., +0.16814523..., +0.00332074...)`.

The closed formula shows that `Delta57` couples the difference of the constituent-character amplitudes `(chi_-4 - chi_-3)` to the product-character amplitude `chi_12`.  In particular the near-bisector `(3,5)` class-5 value is consistent with its very small `chi_12` coordinate.

## Reproducibility gate

The script stores the eight checkpoint values and asserts a maximum replay discrepancy below `5e-15`.  It prints the residue responses, Hadamard character coordinates, singular values, `Delta57`, and the maximum expected-value error.

## Guardrails

1. These are **finite `M=3999`, binary64 midpoint** values, not outward-rounded certificates.
2. Whitening is the **fixed full Cholesky block metric** from the complete finite matrix; this is not a rewhitened source-subset statement.
3. The exact formula for `Delta57` is an identity in character coordinates, but the observed Suzuki response vectors are numerical.
4. No exact Suzuki `V4` symmetry, arithmetic vertex action, Pell-to-Suzuki intertwiner, asymptotic law, positivity improvement, or index-bound improvement is established here.
5. The official certified index bounds are unchanged by this checkpoint.

This checkpoint is therefore a reproducible numerical coordinate diagnostic for the class-5 `v5 <-> v7` exchange axis, and nothing stronger.
