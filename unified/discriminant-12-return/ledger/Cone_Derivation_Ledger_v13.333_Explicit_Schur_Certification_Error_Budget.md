# Cone Derivation Ledger v13.333 — Explicit Schur Certification Error Budget

## Purpose

This checkpoint converts the qualitative two-precision strategy of v13.332 into explicit operator- and entrywise-error targets.

Let

\[
F=A_{CC}-C B^{-1}C^T,
\]

where \(B\) is the finite buffer block on odd modes \(21,23,\ldots,153\).

Assume

\[
B\succeq \gamma I,
\qquad
\|\Delta A\|\le\delta_A,
\quad
\|\Delta B\|\le\delta_B,
\quad
\|\Delta C\|\le\delta_C,
\]

with \(\delta_B<\gamma\).  Then the perturbed Schur complement obeys

\[
\boxed{
\|\widetilde F-F\|
\le
\delta_A
+
\frac{2\|C\|\delta_C+\delta_C^2}{\gamma-\delta_B}
+
\frac{\|C\|^2\delta_B}{\gamma(\gamma-\delta_B)}.
}
\]

The inverse term follows from

\[
\widetilde B^{-1}-B^{-1}
=-B^{-1}(\widetilde B-B)\widetilde B^{-1}.
\]

## Buffer entry tolerance

Using the pole-free numerical buffer gap target

\[
\gamma\approx0.23848
\]

and dimension \(d_B=67\), an entrywise enclosure radius \(\varepsilon_B\) gives the crude norm bound

\[
\|E_B\|_2\le 67\varepsilon_B.
\]

A half-gap design target is therefore

\[
\boxed{
\varepsilon_B
<\frac{0.23848}{2\cdot67}
\approx1.78\times10^{-3}.
}
\]

Thus the finite 67-dimensional buffer can in principle be certified with only millesimal entrywise accuracy.

## Stiff six-dimensional tolerance

The first resolvable stiff effective level from v13.332 is approximately

\[
\gamma_S\approx4.33\times10^{-8}.
\]

For a \(6\times6\) symmetric enclosure,

\[
\|E_S\|_2\le6\varepsilon_S.
\]

A half-gap design target becomes

\[
\boxed{
\varepsilon_S
<\frac{4.33\times10^{-8}}{12}
\approx3.61\times10^{-9}.
}
\]

This quantifies the two-precision architecture:

- buffer entries: roughly \(10^{-3}\) is enough for positivity;
- stiff effective block: roughly \(10^{-9}\) entrywise control;
- terminal 4D block: substantially finer control, potentially \(10^{-12}\)–\(10^{-17}\), depending on the final pivot geometry.

## Schur-error consequence

The buffer itself can be enclosed coarsely for positivity, but a coarse \(\delta_B\) cannot simply be propagated through the inverse if the target is a \(10^{-9}\)-accurate effective core.  The resolvent term

\[
\frac{\|C\|^2\delta_B}{\gamma(\gamma-\delta_B)}
\]

makes this explicit.

Therefore certification should use two separate notions of precision:

1. a coarse enclosure proving \(B>0\);
2. a much sharper verified linear solve / inverse action for the particular columns \(B^{-1}C^T\).

There is no need to enclose every entry of \(B^{-1}\) at extreme precision.

## Structural improvement

The finite proof target is now a finite set of inequalities rather than an undefined high-precision computation:

1. certify a buffer lower bound \(\gamma>0\);
2. certify the solve residual for \(BX=C^T\);
3. propagate the solve error into a \(10\times10\) Schur enclosure;
4. certify the six-dimensional stiff complement;
5. leave only the terminal \(4\times4\) interval block unresolved.

## Guardrails

All numerical constants above are design targets inherited from non-interval numerical audits.  They are not yet certified enclosures.  No exact zero, positivity theorem, \(\lambda_1=0\), RH, or GRH conclusion follows.
