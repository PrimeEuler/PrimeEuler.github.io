# Cone Derivation Ledger v13.354

## Exact generator LDL and large pivot margin for the N=16001 high block

### Purpose

The corrected global route requires a rigorous proof that the pole-free finite
high block

\[
A_{0,[21,16001]}\succeq 0.22 I.
\]

The previous checkpoint v13.353 established the midpoint target

\[
\lambda_{\min}(A_{0,[21,16001]})\approx 0.227114802018,
\]

but this was only a matrix-free Lanczos diagnostic.  A direct dense interval
factorization of the resulting 7991x7991 matrix would be unnecessarily large.

This checkpoint replaces that plan by an exact displacement-generator LDL
recurrence.

---

## 1. Unified pole-free off-diagonal sequence

Let

\[
Z_n:=2A_n+\operatorname{Si}(n\pi)+2H_n.
\]

Then for odd \(m\ne n\),

\[
(A_0)_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

With

\[
X=\operatorname{diag}(n^2),\qquad u=(Z_n),\qquad v=(n),
\]

this is equivalent to the exact displacement identity

\[
\boxed{
XA_0-A_0X=\frac2\pi(uv^T-vu^T).
}
\]

The diagonal shift \(-0.22I\) commutes with \(X\), so the same identity holds
for

\[
B:=A_{0,[21,16001]}-0.22I.
\]

---

## 2. Scalar Schur complements preserve displacement rank two

Partition the current symmetric matrix as

\[
M=\begin{pmatrix}a&b^T\\ b&C\end{pmatrix}.
\]

Its scalar Schur complement is

\[
S=C-\frac{bb^T}{a}.
\]

If the current generators are \((u_1,v_1)\) for the pivot row and
\((u_2,v_2)\) for the remainder, then direct substitution gives

\[
\boxed{
u_2'=u_2-\frac{b}{a}u_1,
\qquad
v_2'=v_2-\frac{b}{a}v_1.
}
\]

The current off-diagonal pivot column is reconstructed exactly from the
generators:

\[
\boxed{
b_i=\frac2\pi\frac{u_1v_i-v_1u_i}{x_1-x_i},
\qquad x_i=n_i^2.
}
\]

Therefore every LDL step can be performed using only:

- the current diagonal;
- two generator vectors;
- the fixed nodes \(x_i=n_i^2\).

No dense matrix needs to be formed.

Complexity is \(O(N^2)\) arithmetic and \(O(N)\) storage.

---

## 3. Midpoint full-block audit

For the 7991 odd modes

\[
21,23,\ldots,16001,
\]

using the quadrature-free finite archimedean reconstruction and the exact
unified Cauchy off-diagonal formula, the no-pivot structured LDL recurrence gives

\[
\boxed{
\min_j d_j^{LDL}\approx0.25429962365.
}
\]

The minimum pivot occurs at

\[
\boxed{n=29}.
\]

The late pivots rise to values of order 8.  No midpoint pivot approaches zero.

This is a much larger numerical margin than the raw spectral slack

\[
0.227114802018-0.22\approx7.11\times10^{-3}.
\]

The factorization coordinates are therefore substantially better conditioned
for positivity certification than a direct smallest-eigenvalue enclosure.

---

## 4. Dense recurrence cross-check

On the smaller block \(n=21,23,\ldots,199\), construct the dense matrix from
exactly the same diagonal and Cauchy off-diagonal data and perform ordinary
no-pivot dense LDL elimination.

The generator recurrence and dense pivots agree to approximately

\[
\boxed{1.3\times10^{-15}}
\]

in double arithmetic.

This verifies the implementation of the Schur-generator update at midpoint
precision.

---

## 5. Perturbation diagnostic

Random perturbations of the diagonal and \(Z_n\) data show strong numerical
stability.  Even perturbations at the \(10^{-6}\) scale move the minimum pivot
only at roughly the \(10^{-6}\) scale in the tested midpoint runs.

This is diagnostic only.  It is not substituted for an interval proof.

---

## 6. Revised certification target

The finite high-block positivity proof is now reduced to one explicit task:

1. outward-enclose every initial diagonal entry;
2. outward-enclose every \(Z_n\);
3. run the exact generator LDL recurrence in interval/ball arithmetic;
4. verify every pivot interval has positive lower endpoint.

Because the midpoint minimum pivot is about 0.2543, the interval implementation
has a very large positivity margin compared with the already-achieved
\(10^{-10}\)-scale finite-entry enclosure targets.

If this closes, then together with the existing v13.351-v13.353 targets

\[
\|G\|<1,
\qquad
\alpha_{16003}>4.67326749,
\]

one obtains

\[
A_0|_{\mathcal D}>0,
\]

for the full infinite high complement \(\mathcal D\) of odd modes \(n\ge21\).
Only after that global positivity step may the infinite inertia problem be
reduced rigorously to the ten low modes.

---

## Guardrails

- The 0.25429962365 pivot is midpoint numerical data, not yet interval certified.
- No full high-complement positivity theorem is claimed in this checkpoint.
- No exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.
- The new result supersedes the need for a dense 7991x7991 interval Cholesky,
  but not the need for outward-rounded arithmetic.
