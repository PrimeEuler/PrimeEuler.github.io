# M16001 remote Gram transcript contract

Status: audit specification only; fail closed; no theorem promotion.

The explicit remote range is the odd integers

`16003 <= n <= 1999999`,

which contains exactly **991999 rows**. This corrects the 992000 prose typo in ledger v13.510; the v13.511 external audit already verified the exact count.

The actual remote replay must emit enough data to reproduce the complete floating accumulation radius, not merely the final Gram midpoint.

For each chunk and each Gram entry `(i,j)`, emit:

- chunk row count `k_c`;
- chunk midpoint contribution;
- `S_c,ij = sum_rows abs(r_i*r_j)` from the actual row values entering the reduction;
- the local reduction structure if it is not a single sequential/BLAS dot whose error model has already been justified.

For aggregation of chunk Gram matrices, also emit the absolute magnitudes entering each rounded addition level (or an equivalent stronger majorant tied to the actual reduction tree). The checker must charge both:

1. within-chunk product/reduction rounding;
2. between-chunk accumulation rounding.

The final entrywise radius matrix is then converted to a Frobenius/operator majorant. No hard-coded QQ/QN/NN or remote-Gram radius is permitted.

If the implementation uses vectorized BLAS/matrix multiplication whose internal reduction order is unspecified, a plain `gamma_k` sequential-dot model must not be asserted without a justified implementation-level bound. In that case either use an explicitly controlled reduction for the certificate transcript or provide a stronger valid bound for the actual kernel.
