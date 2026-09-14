# Cone Derivation Ledger v13.425 — Odd Finite-High Source Sensitivity and Even-Mode Cusp Reduction

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** numerical evaluation of an exact formula; **[Target]** deliberately loose enclosure target; **[Audit]** guardrail.

## 0. Synchronization

Repository head was checked immediately before assignment.  The latest numbered entry was v13.424, so v13.425 was free at creation time.

The active target remains

\[
A_{FF}^{(0)}\succeq0.53I,
\qquad F=\{22,24,\ldots,4000\},
\]

with the positive sinh-pole to be restored afterward by Loewner monotonicity.

v13.424 gave a deliberately weakened conditional factor floor

\[
\lambda_{\min}(LL^T)>0.0012755
\]

and reconstruction arithmetic below \(6\times10^{-11}\).  Therefore only a coarse exact-source enclosure is needed.

## 1. Off-diagonal source sensitivity [D]

For distinct even modes \(m,n\), the pole-free source-faithful matrix has

\[
A_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

If a nominal generator satisfies the uniform sequence enclosure

\[
|\Delta Z_j|\le \varepsilon_Z,
\]

then

\[
|\Delta A_{mn}|
\le
\frac{2}{\pi}\varepsilon_Z
\frac{n+m}{|n^2-m^2|}
=
\boxed{
\frac{2}{\pi}\frac{\varepsilon_Z}{|n-m|}
}.
\]

The finite-high modes have spacing two.  Number them \(n_i=22+2i\), \(0\le i<N-1\), with \(N=1990\).  Then the off-diagonal absolute row sum at row i is bounded by

\[
\frac{\varepsilon_Z}{\pi}
\left(H_i+H_{N-1-i}\right).
\]

Therefore, by the symmetric row-sum/operator-norm bound,

\[
\boxed{
\|\Delta A_{\rm off}\|_2
\le
C_{1990}\varepsilon_Z,
}
\]

where

\[
C_{1990}
:=
\frac1\pi\max_i(H_i+H_{1989-i}).
\]

Direct evaluation of this exact finite expression gives

\[
\boxed{C_{1990}=4.7618893616523295\ldots<4.762.}
\]

This is the important improvement over the crude \(N\max|E_{ij}|\) conversion: the Cauchy denominator leaves only a harmonic amplification.

## 2. Scalar-to-Z bookkeeping [D]

Recall

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

where \(A_n\) is the prime-source sequence.  Uniform scalar enclosures

\[
|\Delta A_n|\le\varepsilon_P,
\quad
|\Delta \operatorname{Si}(n\pi)|\le\varepsilon_{Si},
\quad
|\Delta H_n|\le\varepsilon_H
\]

give

\[
\boxed{
\varepsilon_Z
\le2\varepsilon_P+arepsilon_{Si}+2\varepsilon_H.
}
\]

A deliberately loose target package is

\[
\varepsilon_P=2\times10^{-6},
\qquad
\varepsilon_{Si}=10^{-8},
\qquad
\varepsilon_H=10^{-8},
\]

hence

\[
\varepsilon_Z=4.03\times10^{-6}.
\]

The resulting off-diagonal operator budget is only

\[
\boxed{
\|\Delta A_{\rm off}\|_2
<1.92\times10^{-5}.
}
\]

These are targets, not yet claimed enclosures of a concrete generator.

## 3. Diagonal perturbations [D/Target]

The diagonal is a sum of archimedean, prime, and cusp contributions.  Because these perturbations are diagonal, their operator norms are simply the largest absolute scalar errors; there is no factor of 1990.

Thus the deliberately loose nominal targets

\[
\varepsilon_{\rm arch,diag}=10^{-6},
\qquad
\varepsilon_{\rm prime,diag}=10^{-5},
\qquad
\varepsilon_{\rm cusp,diag}=10^{-6}
\]

cost only

\[
1.2\times10^{-5}
\]

in operator norm.

The analytic archimedean truncation is already separately bounded by v13.357:

\[
\boxed{
\|\Delta K_{\rm arch,trunc}\|_2\le1.22\times10^{-13}.
}
\]

Combining the illustrative scalar targets gives a total source budget below

\[
\boxed{3.2\times10^{-5}},
\]

well below both the inherited \(10^{-4}\) working target and the v13.424 factor floor \(0.0012755\).

## 4. Exact even-mode cusp simplification [D]

For every finite-high mode n, n is even.  Put

\[
x=n\pi.
\]

Then exactly

\[
\sin x=0,
\qquad
\cos x=1.
\]

The standard sine/cosine-integral inverse-power decomposition therefore reduces to

\[
\operatorname{Si}(x)=\frac\pi2-F(x),
\qquad
\operatorname{Ci}(x)=-G(x),
\]

with formal inverse-power expansions

\[
F(x)=\frac1x-\frac{2!}{x^3}+\frac{4!}{x^5}-\frac{6!}{x^7}+\cdots,
\]

\[
G(x)=\frac1{x^2}-\frac{3!}{x^4}+\frac{5!}{x^6}-\frac{7!}{x^8}+\cdots.
\]

Hence the cusp diagonal

\[
\log(n/4)-\operatorname{Ci}(n\pi)-\frac{\operatorname{Si}(n\pi)}{n\pi}
\]

becomes

\[
\boxed{
\log(n/4)+G(x)-\frac{\pi/2-F(x)}{x}.
}
\]

No general large-argument trigonometric evaluation is needed in the odd-sector finite-high block.

At the smallest argument \(x=22\pi\), the next inverse-power magnitudes after keeping F through \(4!/x^5\) and G through \(5!/x^6\) are

\[
\frac{6!}{(22\pi)^7}
\approx9.56\times10^{-11},
\]

and

\[
\frac{7!}{(22\pi)^8}
\approx9.68\times10^{-12}.
\]

They decrease rapidly with n.  The next proof step is to attach the standard integration-by-parts remainder inequalities to these truncations; the numerical scales show that the relaxed \(10^{-6}\) cusp target has enormous slack.

## 5. Prime-source consequence [D/I]

The only source component that still requires a nontrivial outward implementation is therefore the prime channel.  For n=2r,

\[
\sin\!\left(\frac{n\pi\log q}{2}\right)
=
\sin(r\pi\log q),
\]

and similarly for cosine.  Thus it is enough to enclose, for each q in \(\{2,3,4,5,7\}\), a single base rotation

\[
(\cos(\pi\log q),\sin(\pi\log q))
\]

and propagate it to r=11,...,2000 by a certified rotation/Chebyshev recurrence.

Because the admissible sequence error is at the \(10^{-6}\) scale, the recurrence does not require exceptionally tight base intervals.  This is much weaker than the historical 10^-30 scalar-radius implementation.

## 6. Proof-state update [Audit]

This checkpoint does not yet promote

\[
A_{FF}^{(0)}\succeq0.53I.
\]

It does remove two possible bottlenecks:

1. matrix conversion of Z-sequence errors is only harmonic, with exact coefficient <4.762;
2. the cusp channel collapses on even modes to short inverse-power series with very small omitted scales.

The remaining finite-high work is now sharply concentrated in:

- proof-grade remainder inequalities for the even-mode cusp series;
- a transparent outward prime base-angle/recurrence generator;
- parity-correct polynomial arch nominal rounding;
- final assembly against the v13.424 factor certificate.

Helper script:

`research-notes/suzuki_odd_M4000_source_sensitivity_budget.py`.

---

**Checkpoint conclusion.** A source-faithful finite-high enclosure below 10^-4 no longer requires entrywise 10^-8-level matrix control.  Uniform scalar control at only the low-micro scale already suffices, because the off-diagonal Cauchy structure converts sequence error with harmonic factor <4.762 and diagonal errors enter without dimension amplification.
