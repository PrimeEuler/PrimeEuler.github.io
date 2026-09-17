# M16001 remote Gram transcript contract

Status: audit specification; fail closed; no theorem promotion.

The explicit remote range is odd `16003 <= n <= 1999999`, exactly **991999 rows** (the 992000 prose count in v13.510 was corrected by the v13.511 audit).

For every actual chunk and Gram entry `(i,j)`, emit the chunk row count, midpoint contribution, and `S_c,ij=sum abs(r_i*r_j)`. Also emit the absolute magnitudes entering the actual chunk-aggregation tree. The certificate must charge both within-chunk reduction rounding and between-chunk accumulation rounding before converting the entrywise radius matrix to an operator majorant.

No hard-coded remote radius is permitted. If vectorized BLAS/matmul has unspecified internal reduction order, do not assert a sequential `gamma_k` model without justification; use a controlled certificate reduction or a valid stronger implementation-level bound.
