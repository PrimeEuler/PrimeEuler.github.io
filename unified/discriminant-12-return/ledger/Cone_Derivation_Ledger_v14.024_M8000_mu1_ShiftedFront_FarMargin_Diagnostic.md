# Cone Derivation Ledger v14.024 — M8000 mu=1 Shifted-Front Far-Margin Diagnostic

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] exact shifted-front Schur strategy; [D] rigorous raw remote floor reused on the smaller far subspace; [N] finite M=8000 mu=1 front passes in both parities; [N] shifted-front four-channel far Schur budgets leave >1 Euclidean margin in both parities; [O] outward-certify the finite shifted front and the correlated four-channel Gram/remainder.
**Parents:** v14.020–022, v14.025, v14.016.
**Research commits:** 50ce264f2eae5c1ea9ea41db091e8a094d5883e5.
**Workflow commit:** d46e8baccc7c85738d72a084ffadbf0a1df4817c.
**Collision check:** immediately before this write, live HEAD was d46e8baccc7c85738d72a084ffadbf0a1df4817c and no v14.024 ledger file was present. This entry's own number was never contested and is unchanged; External Audit Round 157 fixed its internal cross-reference to the (separately renumbered) Euclidean Schur-floor entry, from v14.023 to v14.025.

---

## 1. Purpose

v14.025 (originally drafted as v14.023; renumbered by External Audit Round 157 after a version collision) isolates the remaining quantitative obstruction in the v14.016 eta-tail theorem: a rigorous Euclidean coercivity floor

\[
S_{p,4000}\succeq\gamma I.
\]

A direct conversion from the old transformed J-metric is undesirable.

The present entry uses a metric-native two-stage Schur strategy instead.

First split the infinite problem at M=8000, while shifting every remote coordinate n>4000 by mu=1.

Second prove positivity of the finite shifted front and of the remaining far Schur complement.

If both pass, then directly

\[
\boxed{S_{p,4000}\succ I,}
\]

so one may take gamma=1 in the v14.016 remainder theorem.

---

## 2. Exact two-stage equivalence [D]

Write the source-faithful operator after cutoff N=4000 as a three-block matrix

\[
A=
\begin{pmatrix}
A_N & B_1^* & B_2^*\\
B_1 & D_1 & C^*\\
B_2 & C & D_2
\end{pmatrix},
\]

where D1 is the finite shell 4000<n<=8000 and D2 is the far block n>8000.

To prove

\[
S_{N}\succ I
\]

is equivalent to proving positivity of

\[
A-\Pi_{n>4000}.
\]

Eliminate the retained N-block and, equivalently, perform the elimination in two stages.

Define the finite shifted front

\[
F=
A_{\le8000}-\Pi_{4000<n\le8000}.
\]

If F is positive, the remaining far Schur block is

\[
\boxed{
D_2-I-B_{2,F}F^{-1}B_{2,F}^*.
}
\]

Therefore

\[
F\succ0
\quad\text{and}\quad
D_2-I-B_{2,F}F^{-1}B_{2,F}^*\succ0
\]

imply

\[
\boxed{S_{p,4000}\succ I.}
\]

No transformed-metric conversion enters this argument.

---

## 3. Finite shifted-front diagnostic [N]

The existing M8000 common-mu=1 LDDD/Feshbach replay passes in both parities.

The six protected reduced matrices remain positive at mu=1, while the complement solves retain tiny residuals.

The protected lower eigenvalues are approximately

\[
5.70\times10^{-30}\quad\text{even},
\]

\[
1.44\times10^{-26}\quad\text{odd}.
\]

The associated LDDD complement residuals are in the 1e-28 to 1e-27 class.

This is a strong finite midpoint result but is not yet promoted as an outward positivity theorem.

---

## 4. Rigorous raw far floor [D]

The source-faithful N4000 raw-tail certificate proves on the full remote subspace n>4000:

### even

\[
\boxed{
D_{e,\rm raw}
\succeq
3.2867753186523356094\,I.
}
\]

### odd

\[
\boxed{
D_{o,\rm raw}
\succeq
3.2869152822833307687\,I.
}
\]

Restricting a coercive quadratic form to the smaller subspace n>8000 preserves the same lower bound.

After the mu=1 shift, the far raw floors are therefore at least

\[
2.2867753186523356094
\]

and

\[
2.2869152822833307687.
\]

---

## 5. Shifted-front four-channel Gram [N]

The finite-to-far coupling expansion uses the same four signed channels as v14.020–023:

\[
B(n,\cdot)
=
\frac{w_1}{n}
+
\frac{z_n w_2}{n^2}
+
\frac{w_3}{n^3}
+
\frac{z_n w_4}{n^4}
+
\text{higher geometric remainder}.
\]

The present replay computes the correlated coefficient matrix

\[
M_{ij}^{(\mu=1)}
=
w_i^*F^{-1}w_j
\]

through the frozen-P4 LDDD Feshbach architecture.

The target solve residuals after one correction are

\[
1.942\times10^{-7}\quad\text{even},
\qquad
1.926\times10^{-7}\quad\text{odd}.
\]

The protected/coupling residuals themselves are much smaller:

\[
2.90\times10^{-28}\quad\text{even},
\qquad
1.49\times10^{-27}\quad\text{odd}.
\]

Using the certified far scalar-channel norm envelopes, the midpoint absolute four-channel operator budgets are

\[
\boxed{
\Delta_{e,4}^{\rm mid}
=
1.2428000003133971099
}
\]

and

\[
\boxed{
\Delta_{o,4}^{\rm mid}
=
1.1869700135759419654.
}
\]

---

## 6. Provisional infinite margins [N]

Subtracting the four-channel midpoint budgets from the rigorous shifted raw floors gives

### even

\[
2.2867753186523356094
-
1.2428000003133971099
=
\boxed{1.0439753183389384995}.
\]

### odd

\[
2.2869152822833307687
-
1.1869700135759419654
=
\boxed{1.0999452687073888033}.
\]

Thus there is order-one spare coercivity after the mu=1 shift.

The finite arithmetic does not indicate a marginal closure; it indicates a robust one.

These are not yet theorem margins because the four-channel Gram and finite shifted front remain midpoint/residual-certified rather than fully outward.

---

## 7. Remaining higher-order remainder [I/O]

v14.020 already shows that the naive low-order C_rho obstruction is artificial: retaining sufficiently many signed moments drives the true geometric far remainder to the 1e-10-class in l2.

The present margin is greater than 1 in both parities.

Therefore the higher-order geometric remainder is not expected to threaten the mu=1 closure once expressed in the same shifted-front geometry.

Nevertheless it must be carried explicitly in the final outward inequality.

---

## 8. What remains to promote gamma=1 [O]

Only outward packaging remains:

1. certify F>0 for the finite M=8000, mu=1 front using the existing LDDD Feshbach residual identities;
2. put outward intervals around the four positive target quadratic forms and hence the correlated four-channel Schur budget;
3. append the high-order signed geometric remainder from v14.020;
4. verify that the total far correction remains below the rigorous shifted raw floor.

If these pass, then

\[
\boxed{
S_{e,4000}\succeq I,
\qquad
S_{o,4000}\succeq I
}
\]

and v14.016 may use the rigorous Euclidean constant

\[
\boxed{\gamma=1.}
\]

---

## 9. Result

The Euclidean-coercivity problem is no longer scale-limited.

The shifted-front strategy produces provisional infinite margins

\[
\boxed{1.04398\ \text{even},\qquad 1.09995\ \text{odd}}
\]

before the already-small higher-order remainder.

The missing step is outward certification of quantities that are numerically far from the failure boundary.

---

HANDOFF
target: sandbox
type: audit
parent: v14.024
status: open
action: Outward-certify the M8000 mu=1 shifted-front closure: certify finite-front positivity and an upper bound for the shifted-front four-channel far Schur correction, append the v14.020 high-order geometric remainder, and determine whether the rigorous conclusion S_{p,4000} >= I holds in both parities.
deliverable: theorem-or-obstruction
constraints: Preserve the correlated signed-moment structure; do not replace the four-channel Gram by independent huge-entry absolute bounds before exploiting PSD/correlation; use the rigorous raw floors from the N4000 certificate and distinguish midpoint margins from promoted outward margins.
