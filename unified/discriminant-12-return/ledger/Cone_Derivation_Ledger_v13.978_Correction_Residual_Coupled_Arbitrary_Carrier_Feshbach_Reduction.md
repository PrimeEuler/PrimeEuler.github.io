# Cone Derivation Ledger v13.978 — Correction: Residual-Coupled Arbitrary-Carrier Feshbach Reduction

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] correction to the numerical-carrier reduction of v13.975; [D] exact arbitrary-carrier Feshbach formula including Ritz-residual cross coupling; [D] four additional KKT solves per parity suffice; [G] v13.975 complement KKT identities remain valid but its claimed complete numerical \(6\times6\) matrix omitted the noninvariant-carrier cross block; [G] v13.977 Part-I \(Q_4\) error theorem remains valid; [R] v13.977 numerical \(\kappa\approx0.792\) is reclassified as an incomplete-carrier diagnostic and must not be interpreted as the full high-cutoff scalar  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.824–836, v13.971, v13.974–977  
**Collision check:** v13.978 was absent immediately before this write.

---

## 0. Correction summary

The exact v13.971 \(2+4\) reduction uses the **exact spectral projector**

\[
P_4,
\]

so

\[
P_4J_TQ_4=0.
\]

The frozen numerical carrier

\[
Z
\]

of v13.974 is only a residual-certified approximation to \(\operatorname{Ran}P_4\).

Therefore its transformed projector

\[
\widehat P
\]

does **not** commute exactly with \(J_T\).

v13.975 correctly derived constrained-complement KKT formulas for:

- core-to-complement response;
- source-to-complement response;
- regular source background.

However, when it assembled the numerical \(6\times6\) matrix, it implicitly dropped the cross block

\[
\widehat QJ_T\widehat P.
\]

That omission is harmless only for an invariant carrier.

The present entry repairs the reduction exactly.

---

## 1. Numerical carrier and transformed operator [D]

Let

\[
B=B_T>0,
\qquad
A=A_T,
\]

and let the normalized frozen carrier satisfy

\[
Z^TBZ=I_4.
\]

Define

\[
Y=B^{1/2}Z,
\]

so

\[
Y^*Y=I_4.
\]

Let

\[
\widehat P=YY^*,
\qquad
\widehat Q=I-\widehat P,
\]

and

\[
J=B^{-1/2}AB^{-1/2}.
\]

The numerical Ritz matrix is

\[
\boxed{
\Theta=Y^*JY=Z^TAZ.
}
\tag{1}
\]

---

## 2. Ritz residual equals the missing \(P\)-\(Q\) cross block [D]

Define the original-coordinate Ritz residual

\[
\boxed{
S
=
AZ-BZ\Theta.
}
\tag{2}
\]

Because the Ritz carrier is Galerkin,

\[
Z^TS=0.
\]

Define the transformed residual

\[
\boxed{
K
=
B^{-1/2}S.
}
\tag{3}
\]

Then

\[
Y^*K=0,
\]

so

\[
K\in\operatorname{Ran}\widehat Q.
\]

Moreover

\[
JY
=
Y\Theta+K.
\]

Hence

\[
\boxed{
K
=
\widehat QJY
=
\widehat QJ\widehat P|_{\operatorname{Ran}\widehat P}.
}
\tag{4}
\]

Thus the Ritz residual is exactly the carrier-to-complement cross block that was absent from the v13.975 numerical matrix.

---

## 3. Full arbitrary-carrier three-block operator [D]

Let

\[
R=A_{TC}(0)
\]

be the original tail/core coupling.

Its transformed tail coupling is

\[
C=B^{-1/2}R.
\]

Split

\[
C_P=Y^*C=Z^TR,
\]

and

\[
C_Q=\widehat QC.
\]

Write

\[
D=\widehat QJ\widehat Q.
\]

Then the full transformed operator on

\[
\mathcal H_C
\oplus
\operatorname{Ran}\widehat P
\oplus
\operatorname{Ran}\widehat Q
\]

is

\[
\boxed{
\begin{pmatrix}
A_{CC} & C_P^* & C_Q^*
\\
C_P & \Theta & K^*
\\
C_Q & K & D
\end{pmatrix}.
}
\tag{5}
\]

For the exact spectral carrier, \(K=0\).

For the numerical carrier, \(K\neq0\) in general.

---

## 4. Existing three KKT solves [D]

The v13.975 saddle operator computes the constrained inverse

\[
D^{-1}
\]

on \(\operatorname{Ran}\widehat Q\).

The two existing core-coupling solves give

\[
X_C
\]

such that, in transformed coordinates,

\[
B^{1/2}X_C
=
D^{-1}C_Q.
\]

The existing source solve gives

\[
x_f
\]

such that

\[
B^{1/2}x_f
=
D^{-1}g_Q,
\]

where

\[
g=B^{-1/2}f_T.
\]

These identities remain correct.

---

## 5. Four residual KKT solves [D]

Run the same constrained saddle solver with the four columns of

\[
S=AZ-BZ\Theta.
\]

Collect the solutions into

\[
\boxed{
X_R
=
\begin{pmatrix}
x_{S_1}&\cdots&x_{S_4}
\end{pmatrix}.
}
\tag{6}
\]

Then

\[
\boxed{
B^{1/2}X_R
=
D^{-1}K.
}
\tag{7}
\]

These four solves are the only new numerical objects required.

---

## 6. Corrected arbitrary-carrier \(6\times6\) matrix [D]

Eliminate the \(\widehat Q\) block from (5).

The core/core block remains

\[
\boxed{
H_C
=
A_{CC}
-
R^TX_C.
}
\tag{8}
\]

The corrected core/\(\widehat P\) coupling is

\[
\boxed{
K_{\rm eff}
=
Z^TR
-
X_R^TR.
}
\tag{9}
\]

The corrected \(\widehat P/\widehat P\) block is

\[
\boxed{
J_{\rm eff}
=
\Theta
-
S^TX_R.
}
\tag{10}
\]

Therefore the exact finite numerical-carrier Feshbach matrix is

\[
\boxed{
\mathcal M_{6,\rm arb}
=
\begin{pmatrix}
H_C & K_{\rm eff}^T
\\
K_{\rm eff} & J_{\rm eff}
\end{pmatrix}.
}
\tag{11}
\]

This replaces the incomplete v13.975 numerical matrix

\[
\begin{pmatrix}
H_C & K_0^T\\
K_0 & \Theta
\end{pmatrix}.
\]

---

## 7. Corrected reduced source [D]

The raw numerical carrier source coordinate is

\[
s=Z^Tf_T.
\]

After eliminating \(\widehat Q\), the core source remains

\[
\boxed{
f_{C,\rm eff}
=
f_C-R^Tx_f.
}
\tag{12}
\]

The carrier source must also be corrected by the \(K\)-to-\(Q\) cross channel:

\[
\boxed{
s_{\rm eff}
=
Z^Tf_T
-
S^Tx_f.
}
\tag{13}
\]

Hence

\[
\boxed{
f_{6,\rm arb}
=
\binom{
f_C-R^Tx_f
}{
Z^Tf_T-S^Tx_f
}.
}
\tag{14}
\]

The regular source background remains

\[
\boxed{
h_{\rm reg}
=
f_T^Tx_f.
}
\tag{15}
\]

---

## 8. Corrected Fourier functional [D]

Let

\[
p_C(t),\qquad p_T(t)
\]

be the original-coordinate Fourier functional vectors.

The core reduced functional remains

\[
\boxed{
h_C(t)
=
p_C(t)-X_C^Tp_T(t).
}
\tag{16}
\]

The carrier functional receives the same residual-channel correction:

\[
\boxed{
h_P(t)
=
Z^Tp_T(t)-X_R^Tp_T(t).
}
\tag{17}
\]

The regular background remains

\[
\boxed{
r(t)=p_T(t)^Tx_f.
}
\tag{18}
\]

Thus

\[
\boxed{
h_{6,\rm arb}(t)
=
\binom{
p_C(t)-X_C^Tp_T(t)
}{
Z^Tp_T(t)-X_R^Tp_T(t)
}.
}
\tag{19}
\]

---

## 9. Corrected reconstructed coefficient vector [D]

Solve

\[
\mathcal M_{6,\rm arb}
\binom{w_C}{w_P}
=
f_{6,\rm arb}.
\]

Then

\[
F(t)
=
r(t)
+
h_{6,\rm arb}(t)^*
\binom{w_C}{w_P}.
\]

Collecting coefficients gives

\[
\boxed{
v_C=w_C,
}
\tag{20}
\]

and

\[
\boxed{
v_T
=
x_f
-
X_Cw_C
+
(Z-X_R)w_P.
}
\tag{21}
\]

Therefore

\[
\boxed{
F(t)
=
p_C(t)^Tv_C
+
p_T(t)^Tv_T.
}
\tag{22}
\]

The adaptive sign-box consumer of v13.985 remains unchanged after replacing the incomplete reconstructed vector by (20)–(21).

---

## 10. Why the omitted term is potentially decisive [D/G]

The transformed Ritz residual caps are approximately

\[
\|K_e\|
\lesssim
5.8\times10^{-3},
\]

\[
\|K_o\|
\lesssim
8.8\times10^{-3}
\]

in the later block-energy refinement.

With an inverse scale of order \(10\), the second-order carrier correction can be as large as

\[
\|K^*D^{-1}K\|
\lesssim
10\|K\|^2.
\]

Thus the crude scales are

even-v:

\[
\boxed{
\lesssim
3.4\times10^{-4},
}
\tag{23}
\]

odd-v:

\[
\boxed{
\lesssim
7.8\times10^{-4}.
}
\tag{24}
\]

These are vastly larger than the first numerical Ritz values and the tiny renormalized core entries.

Therefore the missing residual-channel correction cannot be dismissed a priori.

---

## 11. Status of v13.975 [G]

The following parts of v13.975 remain correct:

- the constrained KKT realization of the numerical complement inverse;
- the two core-complement solves;
- the source-complement solve;
- \(H_C=A_{CC}-R^TX_C\);
- \(f_C-R^Tx_f\);
- \(h_{\rm reg}=f_T^Tx_f\);
- the no-t-dependent-solve strategy.

The following claim is superseded:

\[
\text{“the complete numerical six-dimensional matrix is }
\begin{pmatrix}
H_C&K_0^T\\
K_0&\Theta
\end{pmatrix}
\text{.”}
\]

It is complete only when

\[
S=0,
\]

i.e. when the carrier is invariant.

For the residual-certified numerical carrier one must use (11).

---

## 12. Status of v13.977 numerical Part II [R]

The exact \(Q_4\) error theorem in v13.977 Part I remains valid.

The numerical values

\[
\kappa_{\rm energy}^{\rm nom}
\approx0.791891,
\]

and

\[
\kappa_{\rm phase}^{\rm nom}
\approx0.791879
\]

were computed from the incomplete matrix with \(X_R=0\).

Their agreement is an internal consistency check of that incomplete model only.

They are **not** evidence that the full high-cutoff finite model has scalar near \(0.792\).

Those numerical conclusions are reopened pending the four residual KKT solves.

---

## 13. Minimal next payload [O]

For each parity, freeze only:

1. the residual matrix
   \[
   S=AZ-BZ\Theta;
   \]
2. the four constrained solutions
   \[
   X_R;
   \]
3. four saddle multiplier vectors;
4. finite and remote residual diagnostics;
5. replay matrices
   \[
   S^TX_R,
   \qquad
   X_R^TR,
   \qquad
   S^Tx_f.
   \]

Then Lane A can assemble the corrected \(6\times6\) system immediately.

No new eigensolve is needed.

---

## 14. Result

For a residual-certified but noninvariant carrier, the exact finite Feshbach matrix is

\[
\boxed{
\mathcal M_{6,\rm arb}
=
\begin{pmatrix}
A_{CC}-R^TX_C
&
\left(Z^TR-X_R^TR\right)^T
\\
Z^TR-X_R^TR
&
\Theta-S^TX_R
\end{pmatrix}.
}
\]

The corrected source is

\[
\boxed{
f_{6,\rm arb}
=
\binom{
f_C-R^Tx_f
}{
Z^Tf_T-S^Tx_f
}.
}
\]

Only four additional constrained KKT solves per parity are required to repair the numerical carrier exactly.
