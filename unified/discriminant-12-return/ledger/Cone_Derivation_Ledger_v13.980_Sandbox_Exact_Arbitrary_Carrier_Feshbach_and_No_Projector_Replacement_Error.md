# Cone Derivation Ledger v13.980 — Sandbox: Exact Arbitrary-Carrier Feshbach Certification and Elimination of Projector-Replacement Error

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact full-operator Feshbach reduction for any fixed numerical carrier whose complement is invertible; [D] exact complement-solve residual contract using the v13.979 numerical-complement gap; [D] exact-P4 replacement error is not part of the final scalar certificate; [I] P4 is now only a proof device for complement invertibility and carrier-quality diagnostics; [O] certify the infinite transformed residuals of the finite KKT solves  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.971, v13.974–979  
**Collision check:** v13.980 was absent immediately before this write.

---

## 0. Main simplification

The exact v13.971 reduction was written using the exact spectral projector

\[
P_4.
\]

The corrected v13.978 reduction shows how to work with a noninvariant numerical carrier.

There is a stronger conclusion.

Once an orthogonal numerical carrier

\[
\widehat P
\]

is fixed, the decomposition

\[
\mathcal H_T
=
\operatorname{Ran}\widehat P
\oplus
\operatorname{Ran}\widehat Q,
\qquad
\widehat Q=I-\widehat P,
\]

is an **exact Hilbert-space decomposition of the true tail operator**.

If

\[
\widehat D
=
\widehat QJ_T\widehat Q
\]

is invertible, eliminating \(\operatorname{Ran}\widehat Q\) is an exact Feshbach operation.

v13.979 proves precisely that invertibility.

Therefore the final finite-\(a\) Xi-scalar certificate does not require replacing the numerical carrier by exact \(P_4\).

---

## 1. Exact three-block decomposition [D]

Let

\[
Y=B_T^{1/2}Z,
\qquad
Y^*Y=I_4,
\]

and define

\[
\widehat P=YY^*,
\qquad
\widehat Q=I-\widehat P.
\]

Let

\[
J=B_T^{-1/2}A_TB_T^{-1/2}.
\]

For the two-dimensional low core, write the transformed full operator as

\[
\mathcal F=
\begin{pmatrix}
A_{CC}&C^*\\
C&J
\end{pmatrix}.
\]

Relative to

\[
\mathcal H_C
\oplus
\operatorname{Ran}\widehat P
\oplus
\operatorname{Ran}\widehat Q,
\]

this is exactly

\[
\boxed{
\mathcal F=
\begin{pmatrix}
A_{CC}&C_P^*&C_Q^*\\
C_P&\Theta&K^*\\
C_Q&K&\widehat D
\end{pmatrix},
}
\tag{1}
\]

where

\[
\Theta=Y^*JY,
\]

\[
K=\widehat QJY,
\]

\[
C_P=Y^*C,
\qquad
C_Q=\widehat QC,
\]

and

\[
\widehat D=\widehat QJ\widehat Q.
\]

No approximation has been made in (1).

---

## 2. Numerical complement is rigorously invertible [D]

v13.979 proves, from the exact \(P_4\) moat and the certified angle between \(P_4\) and \(\widehat P\), that

\[
\boxed{
\|\widehat D_e^{-1}\|<10.153,
}
\tag{2}
\]

and

\[
\boxed{
\|\widehat D_o^{-1}\|<10.303.
}
\tag{3}
\]

Thus \(\widehat D\) may be eliminated exactly in both parity sectors.

The exact spectral projector \(P_4\) has completed its essential role:

\[
\boxed{
P_4
\text{ certifies that }
\widehat D
\text{ is safely invertible.}
}
\]

It need not be substituted back into the final Feshbach system.

---

## 3. Exact arbitrary-carrier Feshbach matrix [D]

Eliminate \(\widehat D\) in (1).

The exact reduced matrix on

\[
\mathcal H_C
\oplus
\operatorname{Ran}\widehat P
\]

is

\[
\boxed{
\mathcal M_{\widehat P}
=
\begin{pmatrix}
A_{CC}-C_Q^*\widehat D^{-1}C_Q
&
C_P^*-C_Q^*\widehat D^{-1}K
\\
C_P-K^*\widehat D^{-1}C_Q
&
\Theta-K^*\widehat D^{-1}K
\end{pmatrix}.
}
\tag{4}
\]

This is exact for the true operator.

Using the original-coordinate KKT quantities of v13.975/v13.978,

\[
\boxed{
\mathcal M_{\widehat P}
=
\begin{pmatrix}
H_C&
K_{\rm eff}^T
\\
K_{\rm eff}&J_{\rm eff}
\end{pmatrix},
}
\tag{5}
\]

where

\[
H_C=A_{CC}-R^TX_C,
\]

\[
K_{\rm eff}=Z^TR-X_R^TR,
\]

\[
J_{\rm eff}=\Theta-S^TX_R.
\]

The only approximation in a numerical implementation of (5) comes from approximating the \(\widehat D^{-1}\) actions.

There is no separate \(P_4-\widehat P\) model error.

---

## 4. Exact arbitrary-carrier source [D]

Let the transformed tail source be

\[
g=B_T^{-1/2}f_T.
\]

Split

\[
g_P=Y^*g=Z^Tf_T,
\qquad
g_Q=\widehat Qg.
\]

Elimination of \(\widehat Q\) gives the exact reduced source

\[
\boxed{
f_{\widehat P}
=
\binom{
f_C-C_Q^*\widehat D^{-1}g_Q
}{
g_P-K^*\widehat D^{-1}g_Q
}.
}
\tag{6}
\]

In original-coordinate KKT notation,

\[
\boxed{
f_{\widehat P}
=
\binom{
f_C-R^Tx_f
}{
Z^Tf_T-S^Tx_f
}.
}
\tag{7}
\]

Again this is exact for the true operator if the constrained solves represent the exact \(\widehat D^{-1}\) actions.

---

## 5. Exact arbitrary-carrier Fourier functional [D]

Let \(h(t)\) be the transformed Fourier functional on the tail and split

\[
h_P(t)=Y^*h(t),
\qquad
h_Q(t)=\widehat Qh(t).
\]

After eliminating \(\widehat Q\),

\[
\boxed{
h_{\widehat P}(t)
=
\binom{
p_C(t)-C_Q^*\widehat D^{-1}h_Q(t)
}{
h_P(t)-K^*\widehat D^{-1}h_Q(t)
}.
}
\tag{8}
\]

By self-adjointness of \(\widehat D^{-1}\), the frozen KKT graph solves give

\[
\boxed{
h_{\widehat P}(t)
=
\binom{
p_C(t)-X_C^Tp_T(t)
}{
Z^Tp_T(t)-X_R^Tp_T(t)
}.
}
\tag{9}
\]

The regular background is

\[
\boxed{
r(t)
=
p_T(t)^Tx_f.
}
\tag{10}
\]

Thus the exact full Fourier transform is recovered from the arbitrary-carrier reduced solve.

---

## 6. Exact complement solve versus a numerical KKT solve [D]

For one transformed right-hand side \(g\), let

\[
y
=
\widehat D^{-1}\widehat Qg
\]

be the exact numerical-complement response.

Suppose a computed vector \(\widetilde y\) and multiplier \(\lambda\) satisfy

\[
J\widetilde y+Y\lambda=g-e.
\]

Let

\[
\eta=\|Y^*\widetilde y\|.
\]

Write

\[
\widetilde y
=
\widehat Q\widetilde y
+
Yc,
\qquad
\|c\|=\eta.
\]

Projecting onto \(\widehat Q\),

\[
\widehat D(\widehat Q\widetilde y)
+
Kc
=
\widehat Qg-\widehat Qe.
\]

Subtract

\[
\widehat Dy=\widehat Qg.
\]

Then

\[
\widehat D
(
\widehat Q\widetilde y-y
)
=
-\widehat Qe-Kc.
\]

Therefore, with

\[
M=\|\widehat D^{-1}\|,
\qquad
\rho=\|K\|,
\]

\[
\boxed{
\|
\widehat Q\widetilde y-y
\|
\le
M
\left(
\|e\|+\rho\eta
\right).
}
\tag{11}
\]

Since

\[
\|\widetilde y-\widehat Q\widetilde y\|=\eta,
\]

\[
\boxed{
\|y-\widetilde y\|
\le
M
\left(
\|e\|+\rho\eta
\right)
+\eta.
}
\tag{12}
\]

This is the correct final KKT error contract for the arbitrary-carrier Feshbach reduction.

---

## 7. Original-coordinate residual [D]

If the original-coordinate KKT residual is

\[
r
=
b-A_Tx-B_TZ\lambda,
\]

then

\[
e=B_T^{-1/2}r.
\]

Hence

\[
\boxed{
\|e\|
=
\|B_T^{-1/2}r\|.
}
\tag{13}
\]

A certified bulk floor

\[
B_T\succeq\beta I
\]

gives

\[
\boxed{
\|e\|
\le
\beta^{-1/2}\|r\|.
}
\tag{14}
\]

The source-faithful remote-tail machinery should preferably certify (13) directly or through the block-energy refinement used for the P4 residual.

---

## 8. Why the projector angle disappears from the final scalar error [D/I]

The exact-\(P_4\) comparison theorem of v13.977 contains terms proportional to

\[
\varepsilon_P.
\]

Those terms are needed only if one insists on replacing the numerical complement by the exact spectral complement.

The arbitrary-carrier reduction does not do that.

Instead:

1. choose \(\widehat P\);
2. prove \(\widehat D\) invertible using \(P_4\);
3. eliminate \(\widehat D\) exactly;
4. certify the finite KKT approximations to \(\widehat D^{-1}\).

Therefore

\[
\boxed{
\varepsilon_P
\text{ enters the final proof only through the bound on }
\|\widehat D^{-1}\|.
}
\tag{15}
\]

There is no additive projector-replacement uncertainty in the final scalar.

This removes what had been the dominant uncertainty in the v13.826/v13.828 grouped-residue formulation.

---

## 9. Role of the graph-corrected carrier [I]

v13.979 shows that

\[
Y_1=Y-X_R
\]

should be a much better approximation to the spectral four-space.

This improvement is still valuable because it:

- reduces \(K\);
- improves conditioning of the arbitrary-carrier Feshbach matrix;
- lowers the number and size of complement corrections;
- provides an independent cross-check against the exact \(P_4\) geometry.

But it is no longer logically required that

\[
Y_1\to P_4
\]

to arbitrary accuracy.

Any fixed carrier with an invertible complement supports an exact Feshbach reduction.

---

## 10. Final proof architecture [D/I]

The exact finite-\(a\) scalar can now be certified through the following chain:

\[
\boxed{
\text{fixed numerical carrier}
\to
\text{certified complement invertibility}
\to
\text{residual-certified KKT inverse actions}
}
\]

\[
\boxed{
\to
\text{exact arbitrary-carrier }6\times6\text{ Feshbach data}
\to
\text{reconstructed Fourier transform}
\to
\text{adaptive phase boxes}.
}
\]

No exact-\(P_4\) coordinate replacement is needed after the complement-gap theorem.

---

## 11. Remaining proof object [O]

For each KKT right-hand side required by v13.978, certify the **infinite transformed residual**

\[
\boxed{
\|B_T^{-1/2}r\|.
}
\]

The finite \(7999\)-mode saddle residuals already uploaded are tiny.

The only nontrivial component is the omitted remote tail beyond the frozen cutoff.

The existing P4 residual certificate provides the correct proof architecture:

1. direct remote rows;
2. Cauchy/moment expansion;
3. analytic far-tail envelope;
4. conversion to transformed residual using the certified \(B_T\) geometry.

Once those residuals are bounded, equations (11)–(14) certify the exact complement inverse actions.

---

## 12. Result

The final scalar certificate does **not** require an exact replacement of the frozen numerical carrier by \(P_4\).

For any fixed carrier \(\widehat P\) whose complement is invertible,

\[
\boxed{
\text{its Feshbach reduction is exact for the full operator.}
}
\]

The exact \(P_4\) theorem is needed only to guarantee

\[
\boxed{
\widehat D^{-1}
\text{ exists with a controlled norm.}
}
\]

The remaining analytic error is therefore reduced to the transformed residuals of a finite list of constrained complement solves.
