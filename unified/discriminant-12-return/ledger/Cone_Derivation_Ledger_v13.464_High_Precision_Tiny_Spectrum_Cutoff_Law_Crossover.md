# Cone Derivation Ledger v13.464 — High-Precision Tiny-Spectrum Cutoff-Law Crossover

Date: 2026-09-14

Status labels: **[N]** numerical diagnostic, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this numbered write. The newest numbered entry remained `v13.463`, so `v13.464` was free.

This checkpoint continues the high-precision even-sector investigation of `v13.461` and `v13.463` by extending the first four tiny finite-cutoff eigenvalues through `M=119` and testing whether they obey a simple zero-limit asymptotic law.

## 1. High-precision ladder [N]

Use the source-faithful full even-v finite matrix with the same high-precision assembly as `v13.461`.

The first four eigenvalues were followed over

\[
M=29,39,49,59,69,79,89,99,109,119.
\]

The new reproducible helper is

`research-notes/suzuki_even_highprecision_tiny_spectrum_cutoff_law.py`.

Selected values are:

\[
\begin{array}{c|cccc}
M&\lambda_1&\lambda_2&\lambda_3&\lambda_4\\\hline
69&8.6422\!\times10^{-30}&3.5033\!\times10^{-23}&1.9247\!\times10^{-17}&1.9536\!\times10^{-12}\\
79&8.0811\!\times10^{-30}&3.3430\!\times10^{-23}&1.8547\!\times10^{-17}&1.8963\!\times10^{-12}\\
89&7.8944\!\times10^{-30}&3.0697\!\times10^{-23}&1.8030\!\times10^{-17}&1.8443\!\times10^{-12}\\
99&7.6622\!\times10^{-30}&2.8202\!\times10^{-23}&1.7873\!\times10^{-17}&1.7503\!\times10^{-12}\\
109&7.1275\!\times10^{-30}&2.7439\!\times10^{-23}&1.7426\!\times10^{-17}&1.6291\!\times10^{-12}\\
119&6.9205\!\times10^{-30}&2.7274\!\times10^{-23}&1.6992\!\times10^{-17}&1.5738\!\times10^{-12}
\end{array}
\]

All displayed values remain positive in the high-precision finite matrices.

## 2. Early rapid collapse does not persist [N]

Between `M=29` and roughly `M=50-70`, the first four levels fall by many orders of magnitude. If one inspects only that window, an exponential-to-zero interpretation is tempting.

The extended ladder shows that this rapid regime does not continue.

From `M=69` to `M=119`, for example,

\[
\frac{\lambda_1(119)}{\lambda_1(69)}\approx0.80,
\]

and

\[
\frac{\lambda_3(119)}{\lambda_3(69)}\approx0.88.
\]

Thus the late-window decay is dramatically slower than the early collapse.

The safe qualitative statement is

\[
\boxed{
\text{rapid early collapse}\quad\longrightarrow\quad\text{slow late-cutoff regime}.
}
\]

## 3. Forced zero-limit power-law test [N/Audit]

If one forces

\[
\lambda(M)\sim M^{-p},
\]

the local effective exponent between successive late cutoffs is

\[
p_{a,b}:=-\frac{\log(\lambda(b)/\lambda(a))}{\log(b/a)}.
\]

For the four levels over the late window, these effective exponents wander substantially rather than stabilizing. Typical values range from roughly

\[
0.07\text{ to }0.8.
\]

No common or level-specific stable power exponent is visible on the present range.

Therefore no simple power law is promoted.

## 4. Forced zero-limit exponential test [N/Audit]

Likewise, forcing

\[
\lambda(M)\sim e^{-cM}
\]

gives local rates

\[
c_{a,b}:=-\frac{\log(\lambda(b)/\lambda(a))}{b-a}.
\]

The late-window `c` values also fluctuate strongly and decrease relative to the early-cutoff regime.

Thus the data do not support one fixed exponential decay constant.

## 5. What the present data do and do not distinguish [I/Audit]

The flattening creates at least two plausible asymptotic possibilities:

1. the finite-cutoff levels approach tiny positive limits;
2. they continue to zero through a slower, possibly algebraic or more complicated, tail law.

The current range through `M=119` is insufficient to distinguish these responsibly.

In particular, a short nonlinear fit of the form

\[
\lambda(M)=\lambda_\infty+aM^{-p}
\]

is too underconstrained and unstable to promote a value of `lambda_infty`.

Therefore

\[
\boxed{
\text{positive plateau vs slow decay to zero remains open.}
}
\]

## 6. Relation to exact-kernel speculation [I/Audit]

`v13.461` already showed that the four finite-cutoff levels are genuine positive high-precision values, not binary64 sign noise.

The present crossover further weakens a naive interpretation in which the finite matrices rapidly converge exponentially to an exact four-dimensional kernel.

However it does **not** exclude an infinite-cutoff zero limit.

Hence the exact safe statement remains:

\[
\boxed{
\text{no exact-zero claim is justified from the finite-cutoff spectrum.}
}
\]

## 7. Next target [I]

The highest-value continuation is to avoid brute-force cutoff extension alone and instead inspect the tail correction analytically in the stabilized four-plane from `v13.463`.

Specifically, for each of the four stabilized terminal directions, compute the large-mode Schur/self-energy correction

\[
\Delta_j(M)
\]

using the same signed inverse-power expansion that made the six-plane tail certification tractable.

This can determine whether the observed slow regime is consistent with a nonzero limiting level or with a controlled decay to zero without requiring prohibitively large high-precision dense diagonalizations.

## 8. Guardrails [Audit]

- All finite-cutoff levels reported here are numerical high-precision values, not interval certificates.
- No limiting value is inferred.
- No exact kernel is asserted or excluded.
- No RH or GRH conclusion follows.

---

**Checkpoint conclusion.** Extending the high-precision even-sector tiny spectrum through `M=119` reveals a clear crossover: the spectacular early collapse of the first four levels gives way to a much slower late-cutoff regime. Neither a simple zero-limit power law nor a simple exponential law has stable local rates on the current window. The stabilized four-plane is therefore better studied through an analytic tail/self-energy correction than by extrapolating finite-cutoff eigenvalues.