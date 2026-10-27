# Full non-diagonal `K_full` provenance obstruction

## Claim

The presently frozen two-sector channel formula and algebraic moment-class domain do not determine a canonical closed, self-adjoint, or normal Hilbert-space realization of the full non-diagonal operator. Consequently they do not determine a unique spectral measure from which a canonical projection or intertwiner could be formed.

This is an obstruction from missing provenance, not a universal nonexistence theorem.

## Frozen algebraic data

Write the frozen linear channel action on finitely supported inputs as

`(K y)_N = sum_m K[N,m] y_m`,

sector by sector. The frozen moment class contains all finitely supported sequences, but no positive lattice measure `w_N`, Hilbert completion, graph norm, or boundary condition is part of the frozen data.

For a candidate weighted completion

`H_w = l2(w)`,  `||y||_w^2 = sum_N w_N |y_N|^2`,  `w_N>0`,

the formal adjoint matrix is

`(K_w^*)[m,N] = (w_N/w_m) conjugate(K[N,m])`.

Thus the adjoint relation, symmetry equations, normality equations, closure, and spectral measure depend on `w`. The algebraic matrix alone does not select them.

## Exact tail witness from the repaired v14.967/v14.969 floor regime

Fix the certified spike mode `m1`. The repaired exact-floor argument gives, for all sufficiently large live output rows `N`,

`K[N,m1] = c (m1 z_N - N z_m1)/(N^2-m1^2)`,

where `z_N` is uniformly bounded and the frozen exact witness certifies `z_m1 != 0`. Hence

`N K[N,m1] -> -c z_m1 != 0`.

Therefore there are constants `C1,C2>0` and an index `N0` such that

`C1/N <= |K[N,m1]| <= C2/N` for all live `N>=N0`.

Consider the two admissible completions of the same algebraic sequence space:

- `H_0 = l2`, with `w_N=1`;
- `H_1/2 = l2(N)`, with `w_N=N` (sector offsets only change finitely many terms).

The spike basis vector `e_m1` has finite norm in both spaces. But its image has tail norm comparable to

- `sum_N N^0/N^2`, which converges in `H_0`;
- `sum_N N^1/N^2 = sum_N 1/N`, which diverges in `H_1/2`.

So the same frozen algebraic rule maps `e_m1` into `H_0` but not into `H_1/2`. The frozen moment-class domain therefore does not even determine a Hilbert completion on which its advertised finitely supported core is an operator domain, before closability or self-adjointness is considered.

More generally, for `H_a=l2(N^(2a))`, the certified spike column is square summable exactly on the tail side `a<1/2` and is excluded for `a>=1/2`.

## Consequence for the v14.972 gate

The requested canonical spectral route cannot be supplied from the frozen data alone:

1. no actual Hilbert inner product is frozen;
2. the formal adjoint changes with the unfrozen weights;
3. even membership of a frozen column in the target Hilbert space changes with those weights;
4. therefore no unique closure, self-adjoint/normal realization, or spectral measure is determined;
5. hence a spectral projector or intertwiner would necessarily import new, non-frozen Hilbert-space or boundary data.

This proves the negative branch requested by v14.972 only in the provenance sense: the current frozen package is insufficient to canonically define `K_full` spectrally.

## Scope and reopening condition

Not proved: that no realization exists after additional data are supplied; that every weighted realization is nonclosable; that no self-adjoint extension exists; or that a future Suzuki finite-interval/Friedrichs construction cannot canonically select a norm and boundary condition.

The gate may be reopened after an additive return freezes all of:

- the Hilbert space and measure/weights;
- a dense operator domain and graph closure;
- the adjoint/boundary relation and sector normalization;
- a proof of self-adjointness or normality (or a uniquely specified extension);
- the resulting spectral measure and any convergence mechanism used.

Finite diagonalizations, fitted zeros, support switches, and prescribed-zero families remain excluded.

