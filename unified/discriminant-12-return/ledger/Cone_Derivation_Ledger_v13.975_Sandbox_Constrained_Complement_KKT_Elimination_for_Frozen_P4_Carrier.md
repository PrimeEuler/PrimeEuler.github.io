# Cone Derivation Ledger v13.975 — Sandbox: Constrained-Complement KKT Elimination for the Frozen P4 Carrier

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact algebraic constrained-complement identity for any B-orthonormal four-carrier; [D] three-solve reconstruction of the numerical Q4 background, source correction, and all Fourier backgrounds; [I] reduces the remaining payload to two core-coupling solves plus one source solve per parity; [G] exact-P4 error remains separate and is controlled by the existing projector-angle certificates  
**Authorization:** Jeremy, 2026-10-03 ("lets certify it!" / parallel sandbox payload completed)  
**Parents:** v13.971, v13.974  
**Collision check:** v13.975 was absent immediately before this write.

---

## 0. Purpose

v13.974 freezes the residual-certified numerical four-carriers

\[
Z_\pm\in\mathbb R^{7999\times4},
\qquad
Z_\pm^TB_\pm Z_\pm=I_4+E_B,
\]

with tiny B-orthogonality defect, together with

\[
Z_\pm^Tf_{T,\pm}.
\]

v13.971 shows that the exact Xi phase transform requires the nonresonant complement terms

\[
C_Q^*J_Q^{-1}C_Q,\qquad
C_Q^*J_Q^{-1}g_Q,\qquad
h_Q(t)^*J_Q^{-1}g_Q.
\]

The present entry shows that, for the frozen numerical carrier, all of these can be reconstructed from only **three constrained solves per parity**.  No explicit \(B^{\pm1/2}\), no full orthogonal-complement basis, and no t-dependent linear solves are needed.

---

## 1. Numerical transformed carrier [D]

Let

\[
A=A_T,\qquad B=B_T>0
\]

on the parity tail, and let

\[
Z\in\mathbb R^{N\times4}
\]

be the frozen numerical generalized-Ritz basis with

\[
Z^TBZ=I_4
\]

at the exact algebraic level; the finite payload defect is handled separately.

Define

\[
Y=B^{1/2}Z.
\]

Then

\[
Y^TY=I_4,
\]

and the numerical transformed projector is

\[
\widehat P_4=YY^T,
\qquad
\widehat Q_4=I-\widehat P_4.
\]

The transformed tail operator is

\[
J=B^{-1/2}AB^{-1/2}.
\]

---

## 2. Constrained numerical-Q inverse [D]

For any original-coordinate right-hand side

\[
b\in\mathbb R^N,
\]

define \(x_b\) and multiplier \(\lambda_b\) by the saddle system

\[
\boxed{
\begin{pmatrix}
A&BZ\\
Z^TB&0
\end{pmatrix}
\binom{x_b}{\lambda_b}
=
\binom{b}{0}.
}
\tag{1}
\]

Set

\[
y_b=B^{1/2}x_b,
\qquad
g_b=B^{-1/2}b.
\]

Multiplying the first block equation by \(B^{-1/2}\) gives

\[
Jy_b+Y\lambda_b=g_b,
\]

while the constraint gives

\[
Y^Ty_b=0.
\]

Therefore \(y_b\in\operatorname{Ran}\widehat Q_4\), and projection of the first equation onto \(\operatorname{Ran}\widehat Q_4\) gives

\[
\widehat Q_4J\widehat Q_4\,y_b
=
\widehat Q_4g_b.
\]

Hence, whenever the numerical complement compression is invertible,

\[
\boxed{
y_b
=
\widehat Q_4
(\widehat Q_4J\widehat Q_4)^{-1}
\widehat Q_4g_b.
}
\tag{2}
\]

Equation (1) is therefore an exact original-coordinate realization of the numerical nonresonant inverse.

---

## 3. Two core-coupling solves [D]

Let

\[
R:=A_{TC}(0)\in\mathbb R^{N\times2}.
\]

Solve (1) with the two columns

\[
b=R_{:1},\qquad b=R_{:2}.
\]

Collect the solutions in

\[
X_C=
\begin{pmatrix}
x_{R_1}&x_{R_2}
\end{pmatrix}.
\]

Then the numerical nonresonant self-energy is

\[
\boxed{
\widehat\Sigma_C
=
R^TX_C.
}
\tag{3}
\]

Thus the numerical renormalized core at \(\delta=0\) is

\[
\boxed{
\widehat H_C(0)
=
A_{CC}(0)-R^TX_C.
}
\tag{4}
\]

The resonant four-channel coupling is independently

\[
\boxed{
\widehat C_P(0)
=
Z^TR
=
K_0,
}
\tag{5}
\]

whose values were already frozen numerically in v13.828.

Hence the complete numerical six-dimensional matrix is

\[
\boxed{
\widehat{\mathcal M}_6(0)
=
\begin{pmatrix}
\widehat H_C(0)&K_0^T\\
K_0&\widehat J_P
\end{pmatrix}.
}
\tag{6}
\]

With the frozen Ritz basis one may take

\[
\widehat J_P=Z^TAZ
\]

rather than assuming it is exactly diagonal.

---

## 4. One source solve [D]

Let the tail source be

\[
f_T.
\]

Solve (1) once with

\[
b=f_T,
\]

and denote the solution by

\[
x_f.
\]

Then the numerical nonresonant source correction is

\[
\boxed{
\widehat s_C^{\,Q}
=
R^Tx_f.
}
\tag{7}
\]

Therefore the numerical six-dimensional source vector is

\[
\boxed{
\widehat f_6
=
\binom{
f_C-R^Tx_f
}{
Z^Tf_T
}.
}
\tag{8}
\]

The lower four coordinates are exactly the source payload frozen in v13.974 up to the explicitly separated source-arithmetic and subspace errors.

The regular tail-source background is

\[
\boxed{
\widehat h_{\rm reg}
=
f_T^Tx_f.
}
\tag{9}
\]

---

## 5. No t-dependent complement solve is required [D]

Let

\[
p_C(t),\qquad p_T(t)
\]

be the original-coordinate Fourier-evaluation vectors on the core and tail.

The numerical regular Fourier-source background is

\[
\boxed{
\widehat r(t)
=
p_T(t)^Tx_f.
}
\tag{10}
\]

For the reduced core Fourier functional, symmetry of the constrained complement inverse gives

\[
C_Q^*\widehat J_Q^{-1}h_Q(t)
=
X_C^Tp_T(t).
\]

Therefore

\[
\boxed{
\widehat h_{C,\rm red}(t)
=
p_C(t)-X_C^Tp_T(t).
}
\tag{11}
\]

The four resonant Fourier coordinates are simply

\[
\boxed{
\widehat h_P(t)
=
Z^Tp_T(t).
}
\tag{12}
\]

Thus

\[
\boxed{
\widehat h_6(t)
=
\binom{
p_C(t)-X_C^Tp_T(t)
}{
Z^Tp_T(t)
}.
}
\tag{13}
\]

After the three constrained solves have been performed, every \(t\)-dependent quantity is obtained by dot products only.

---

## 6. Numerical Xi transform [D]

The frozen-carrier numerical transform is therefore

\[
\boxed{
\widehat F_a(t)
=
p_T(t)^Tx_f
+
\widehat h_6(t)^*
\widehat{\mathcal M}_6(0)^{-1}
\widehat f_6.
}
\tag{14}
\]

This is the finite-payload counterpart of the exact v13.971 formula

\[
F_a(t)
=
r_a(t)
+
h_6(t)^*
\mathcal M_6(0)^{-1}
f_6.
\]

The only differences between (14) and the exact physical transform are now explicit certificate items:

1. numerical-carrier vs. exact-\(P_4\) projector error;
2. finite/operator arithmetic enclosures;
3. residuals of the three constrained solves;
4. exact nonresonant-tail continuation beyond the finite payload.

No hidden t-dependent solve remains.

---

## 7. B-orthogonality defect [D/G]

The frozen payloads have

\[
\|Z^TBZ-I\|
\ll10^{-12}.
\]

If exact orthonormality is desired before solving (1), define

\[
G_B=Z^TBZ
\]

and replace

\[
Z
\mapsto
Z\,G_B^{-1/2}.
\]

Because the defect is \(O(10^{-13})\), this is a tiny deterministic correction.

The payload's canonical column signs are retained by using the positive-definite principal \(G_B^{-1/2}\); no arbitrary four-space rotation is introduced.

---

## 8. Exact-P4 error remains separate [G]

Equations (1)–(14) are exact for the frozen numerical carrier.

They do **not** identify

\[
\widehat P_4=P_4.
\]

The exact-projector replacement is controlled separately by the existing subspace-angle certificates.

Because the v13.974 carrier is unchanged, the later sharpened public bounds apply to the same columns, in particular the refined block-energy/subspace estimates from the v13.824–836 lineage.

No projector error is silently absorbed into source arithmetic.

---

## 9. Minimal second payload [O]

A second sandbox run no longer needs to freeze a new spectrum.

For each parity it only needs to freeze:

1. \(G_B=Z^TBZ\);
2. \(K_0=Z^TR\) as a replay check against v13.828;
3. the two-column constrained solution \(X_C\);
4. the source constrained solution \(x_f\);
5. \(\widehat H_C(0)\);
6. \(\widehat f_6\);
7. \(\widehat h_{\rm reg}\);
8. outward residuals of the three saddle solves.

Once \(X_C\) and \(x_f\) are frozen, Lane A can evaluate all Fourier coordinates and phase intervals without another large solve.

---

## 10. Result

The missing nonresonant background does not require an explicit \(Q_4\) basis.

It is generated by the single saddle operator

\[
\boxed{
\mathscr K_Z
=
\begin{pmatrix}
A_T&B_TZ\\
Z^TB_T&0
\end{pmatrix}.
}
\]

Two core-coupling right-hand sides and one source right-hand side determine all static and t-dependent background terms needed for the Xi phase certificate.

The remaining computational payload is therefore only **three constrained tail solves per parity**.
