# Cone Derivation Ledger v13.299

## Archimedean Remainder Regularity and Bounded-Operator Reduction

**Status:** SOURCE-SERIES REGULARITY REDUCTION + EXPLICIT BOUNDED-OPERATOR FORM + NUMERICAL CONVERGENT-SERIES MAJORANT — SMOOTH REMAINDER CONTROL ADVANCED, BUT CUSP OFF-DIAGONAL CONTROL STILL OPEN — RH/GRH NOT PROVED

### 1. Purpose

v13.298 separated the a=1 even-v high-mode matrix into a local archimedean cusp, a bounded finite prime-ramp operator, and smoother terms.  The next task was to turn the smooth archimedean remainder into an actual bounded L2 operator rather than merely observe diagonal decay.

The local singular model is

\[
s(t)=\frac12 t\log t + A t,
\qquad
A=\frac12(\log(2\pi)+\gamma-1),
\]

and we write

\[
g_{\rm arch}(t)=s(t)+r(t),\qquad 0\le t\le2.
\]

### 2. Exact source-series remainder

Using the same convergent pre-(2.2) expansion already used in the v13.290--v13.298 audits,

\[
\boxed{
r(t)=\frac14\sum_{m\ge2}
\frac{\zeta(2-m,\tfrac14)(-2)^m}{m!}\,t^m.
}
\]

The series starts at m=2. Therefore

\[
\boxed{r(0)=0,\qquad r'(0)=0.}
\]

This is the decisive regularity fact for the derivative-form kernel.

### 3. Two integrations by parts

For \(v\in H_0^1(-1,1)\), define

\[
Q_r(v)=\int_{-1}^1\int_{-1}^1
v'(x)r(|x-y|)v'(y)\,dy\,dx.
\]

Because v vanishes at the endpoints and because r'(0)=0, two integrations by parts introduce no boundary term and no delta contribution at x=y. Thus

\[
\boxed{
Q_r(v)
=-\int_{-1}^1\int_{-1}^1
v(x)r''(|x-y|)v(y)\,dy\,dx.
}
\]

Hence the archimedean remainder is represented by the ordinary symmetric integral kernel

\[
K_r(x,y)=-r''(|x-y|).
\]

This establishes the correct bounded-operator framework for the smooth remainder.

### 4. Convergent-series L1 majorant

If

\[
r(t)=\sum_{m\ge2}a_m t^m,
\qquad
a_m=\frac14\frac{\zeta(2-m,\tfrac14)(-2)^m}{m!},
\]

then on 0<=t<=2,

\[
\int_0^2|r''(t)|\,dt
\le
\sum_{m\ge2}|a_m|m2^{m-1}.
\]

The numerical convergent-series evaluation through m=90 gives

\[
\sum_{m=2}^{90}|a_m|m2^{m-1}
\approx0.6573779527509354.
\]

Selected majorant terms are approximately

| m | term |
|---:|---:|
| 10 | 1.91e-3 |
| 20 | 9.88e-6 |
| 30 | 7.08e-8 |
| 40 | 5.76e-10 |
| 50 | 5.01e-12 |
| 60 | 4.55e-14 |
| 70 | 4.25e-16 |
| 80 | 4.06e-18 |
| 90 | 3.94e-20 |

Thus convergence is extremely rapid at the working cutoff.  This is still a numerical evaluation of the convergent majorant, not an interval-certified infinite-series constant.

A crude symmetric-interval Schur estimate gives

\[
\boxed{
\|K_r\|_{2\to2}
\lesssim 2(0.6573779527509354)
\approx1.3147559055.
}
\]

The factor 2 is deliberately conservative; sharper row-integral geometry is possible.

### 5. Smooth pole term

The pole kernel is

\[
p(t)=-8(\cosh(t/2)-1).
\]

After the same two integrations by parts,

\[
-p''(t)=2\cosh(t/2).
\]

The maximal Schur row integral on [-1,1] is

\[
\boxed{
\|K_{\rm pole}\|_{2\to2}
\le4\sinh(1)
\approx4.7008047746.
}
\]

Combining the crude archimedean-remainder majorant and the pole bound gives a smooth-term control of roughly

\[
\boxed{
\|K_{\rm smooth}\|\lesssim6.01556.
}
\]

Again, the archimedean part of this numerical constant is not interval-certified yet.

### 6. Relation to v13.298 prime bound

v13.298 established for the five a=1 prime-power ramps q=2,3,4,5,7 the operator bound

\[
\|B_{\rm prime}\|
\le2\sum_q\frac{\Lambda(q)}{\sqrt q}
\approx5.85247.
\]

Therefore every term except the singular cusp itself now has a concrete bounded-operator representation:

\[
A_{\rm even}
=
A_{\rm cusp}
+
B_{\rm prime}
+
K_{\rm smooth}.
\]

The prime and smooth terms are bounded on L2.  The remaining unbounded/high-mode growth must therefore come from \(A_{\rm cusp}\).

### 7. Important correction to the v13.298 shorthand

v13.298 observed numerically that

\[
(A_{\rm cusp})_{nn}=\log n-\log4+o(1)
\]

for odd n.  This diagonal asymptotic does **not** by itself establish the operator identity

\[
A_{\rm cusp}=\operatorname{diag}(\log n-\log4)+\text{bounded}.
\]

The off-diagonal cusp entries must still be controlled.

Therefore any v13.298 wording suggesting the full operator decomposition

\[
A_{\rm even}=D_{\log}+\text{bounded}
\]

should be read as an asymptotic target/model, not yet a theorem.

This distinction is essential before attempting an infinite-tail coercivity proof.

### 8. What is established at v13.299

The following are now on firm structural footing:

1. the archimedean remainder starts at order t^2;
2. r(0)=r'(0)=0;
3. two integrations by parts produce the ordinary kernel -r''(|x-y|) with no delta term;
4. the smooth pole term likewise becomes an ordinary bounded positive kernel;
5. the prime-ramp contribution is bounded by the shift-operator argument of v13.298;
6. hence the only unresolved source of unbounded high-mode growth is the singular cusp operator.

The numerical series majorant strongly supports a modest norm for the archimedean remainder, but its infinite-series numerical constant has not yet been interval-certified.

### 9. What this does not establish

This checkpoint does **not** prove:

- an infinite-tail coercivity constant;
- the full operator decomposition \(A_{\rm cusp}=D_{\log}+\text{bounded}\);
- strong H1 convergence of the Ritz candidates;
- \(\ker G_1\ne\{0\}\);
- \(\lambda_1=0\);
- RH or GRH;
- admissibility of the earlier lambda=-5 Fredholm experiment.

### 10. v13.300 next target

The correct next target is now the singular cusp operator itself.

For

\[
s(t)=\frac12t\log t+At,
\]

compute or estimate the odd-mode matrix

\[
C_{mn}=\int_0^2 s(t)S_{mn}(t)\,dt.
\]

The key questions are:

1. can \(C_{mn}\) be written explicitly in terms of \(m\pm n\)?
2. does the diagonal equal \(\log n-\log4+O(n^{-1})\) analytically?
3. are the off-diagonal entries a bounded convolution/Hankel perturbation of that diagonal?
4. can one prove
   \[
   A_{\rm cusp}=D_{\log}+B_{\rm cusp},\qquad \|B_{\rm cusp}\|<\infty?
   \]

That is now the decisive bridge to an actual infinite-tail coercivity theorem framework.

### 11. Files

Research script:

`research-notes/suzuki_arch_remainder_bound.py`

This ledger:

`ledger/Cone_Derivation_Ledger_v13.299_Archimedean_Remainder_Regularity_and_Bounded_Operator_Reduction.md`
