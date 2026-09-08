# Cone Derivation Ledger v13.332 — Four-Dimensional Terminal Core and Two-Precision Schur Strategy

## Finite effective hierarchy at the N=155 scale

A direct double-precision Feshbach assembly with buffer modes 21..153 exhibits the expected ~1e-11 numerical floor in the first four levels, so their displayed signs are meaningless.  However the next six scales are cleanly separated:

\[
\lambda_5\approx4.33\times10^{-8},\qquad
\lambda_6\approx2.55\times10^{-4},
\]

followed by approximately

\[
0.831,\ 1.706,\ 2.018,\ 2.352.
\]

This agrees structurally with the higher-cutoff hybrid audits: the unresolved cancellation is confined to the bottom few effective-core directions, while the remaining core is stiff.

## Certification architecture sharpened

Once the 67-dimensional buffer is certified positive, do **not** demand ultra-high precision uniformly on the resulting 10x10 effective core.

Instead split the effective core into

\[
E=U_4\oplus S_6,
\]

where S_6 is the numerically stiff six-dimensional complement and U_4 is the terminal near-null sector.

The certification can proceed in two stages:

1. certify S_6 positive with an operator enclosure comfortably below the ~4e-8 fifth-level gap;
2. eliminate S_6 rigorously and leave a terminal 4x4 Schur block for extreme precision.

A design target of order 1e-9 in operator norm for the first effective-core enclosure would give substantial room relative to the fifth level.  Only the terminal 4x4 block then needs precision near or below 1e-12--1e-17.

## Relation to the protected-tail construction

The v13.327--328 moment-protected lines use five or six effective directions because spending a small amount of stiff-core Rayleigh energy buys exact tail-moment cancellations.  This is compatible with a terminal 4x4 certification: the extra stiff directions are auxiliary cancellation directions, not evidence that the intrinsic unresolved finite inertia has dimension six.

Thus two different dimensions serve two different purposes:

- **4D terminal block:** finite sign/inertia certification;
- **5D/6D enlarged active spaces:** construction of remote-tail protected test directions.

Conflating these would obscure the reduction.

## Substantial current picture

The original infinite-dimensional question has now separated into three sharply different scales:

1. **remote tail n>=155:** analytically coercive and, on the v13.328 protected line, adverse Schur coupling already below the line scale;
2. **finite buffer 21..153:** numerically gap ~0.24 even after dropping the PSD pole, requiring only coarse interval entry control;
3. **terminal effective core:** all delicate cancellation concentrated in at most four numerical directions, with the other six separated by a fifth-level scale ~4e-8.

This is the main proof architecture going forward.

## Next target

Construct a verified/interval-friendly Schur pipeline whose first milestone is not full positivity but the rigorous statement:

> buffer positive + six-dimensional stiff effective complement positive, leaving a terminal 4x4 symmetric interval matrix.

That would turn the present numerical anatomy into a finite exact obstruction of dimension four.

## Guardrails

The 4D count is currently a numerically stable structural diagnosis, not a certified inertia theorem.  The first four double-precision signs are explicitly discarded.  No exact zero, positivity, lambda_1=0, RH, or GRH conclusion follows.