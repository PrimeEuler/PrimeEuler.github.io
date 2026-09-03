# Cone Derivation Ledger v13.182 — Ramified Ideal Basis Conjugacy

Status convention: [S] source-established, [D] exact derived, [I] interpretation, [O] open, [Audit] limitation.

## Goal

Identify the previously observed mod-2 conjugacy

\[
\Phi\,\bar g\,\Phi^{-1}=P
\]

as an actual change of integral basis on the ramified ideal

\[
\mathfrak p_2=(1+\sqrt3)=(2,\sqrt3-1)\subset \mathbf Z[\sqrt3].
\]

The discriminant-12 return is

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}.
\]

The Pell unit is

\[
\lambda=2+\sqrt3.
\]

---

## 1. Two natural \(\mathbf Z\)-bases of \(\mathfrak p_2\)

### Ramified basis

Use the standard ideal presentation

\[
\boxed{f_1=2,\qquad f_2=\sqrt3-1.}
\]

Since

\[
\mathfrak p_2=(2,\sqrt3-1),
\]

this is a natural integral basis of the norm-2 ideal.

### Principal/Pell basis

Since

\[
\mathfrak p_2=(1+\sqrt3),
\]

use

\[
\boxed{e_1=1+\sqrt3,\qquad e_2=\sqrt3(1+\sqrt3)=3+\sqrt3.}
\]

This is the principal-generator basis obtained by multiplying the ambient coefficient basis \(\{1,\sqrt3\}\) by \(1+\sqrt3\).

Both bases have determinant of absolute value \(2\) relative to \(\{1,\sqrt3\}\), hence both span the same index-2 ideal.

---

## 2. Multiplication by \(2+\sqrt3\) in the ramified basis

[D] Compute

\[
\lambda f_1=(2+\sqrt3)2=4+2\sqrt3.
\]

Write

\[
4+2\sqrt3=a(2)+b(\sqrt3-1).
\]

Matching coefficients gives

\[
b=2,\qquad 2a-b=4,
\]

so

\[
\boxed{\lambda f_1=3f_1+2f_2.}
\]

Next,

\[
\lambda f_2=(2+\sqrt3)(\sqrt3-1)=1+\sqrt3.
\]

But

\[
1+\sqrt3=f_1+f_2,
\]

so

\[
\boxed{\lambda f_2=f_1+f_2.}
\]

Therefore the multiplication matrix in the ramified ideal basis is

\[
\boxed{
[\times\lambda]_f
=\begin{pmatrix}3&1\\2&1\end{pmatrix}
=g_{12}.
}
\]

This is exact: the discriminant-12 return matrix is literally multiplication by the Pell unit on \(\mathfrak p_2\) when the ideal is written in the basis \(\{2,\sqrt3-1\}\).

---

## 3. Multiplication in the principal/Pell basis

[D] Since \(e_i=(1+\sqrt3)\times\{1,\sqrt3\}\), multiplication by \(\lambda\) has the same coefficient matrix as on the ambient basis \(\{1,\sqrt3\}\):

\[
\lambda(a+b\sqrt3)
=(2a+3b)+(a+2b)\sqrt3.
\]

Hence

\[
\boxed{
[\times\lambda]_e
=\begin{pmatrix}2&3\\1&2\end{pmatrix}.
}
\]

Modulo 2,

\[
\boxed{
[\times\lambda]_e\bmod2
=\begin{pmatrix}0&1\\1&0\end{pmatrix}
=P.
}
\]

Thus the Pell coefficient basis exhibits the return as the simple bit swap.

---

## 4. The basis-change matrix is exactly \(\Phi\) mod 2

[D] Express the principal basis in the ramified basis:

\[
e_1=1+\sqrt3=f_1+f_2,
\]

and

\[
e_2=3+\sqrt3=2f_1+f_2.
\]

Therefore

\[
(e_1\ e_2)=(f_1\ f_2)C,
\]

with

\[
\boxed{
C=\begin{pmatrix}1&2\\1&1\end{pmatrix}.
}
\]

Its determinant is

\[
\det C=-1,
\]

so this is an integral unimodular change of basis inside the same ideal.

The matrices satisfy

\[
\boxed{
C^{-1}g_{12}C
=\begin{pmatrix}2&3\\1&2\end{pmatrix}.
}
\]

Reducing \(C\) modulo 2 gives

\[
\boxed{
\bar C=
\begin{pmatrix}1&0\\1&1\end{pmatrix}.
}
\]

But the previously defined Boolean coordinate change

\[
\Phi(x,y)=(x,x+y)
\]

has exactly the matrix

\[
\boxed{
\Phi=
\begin{pmatrix}1&0\\1&1\end{pmatrix}
\in GL_2(\mathbf F_2).
}
\]

Therefore

\[
\boxed{\bar C=\Phi.}
\]

Because \(\Phi^2=I\) over \(\mathbf F_2\), either conjugacy orientation is equivalent, and we recover

\[
\boxed{
\Phi\,\bar g\,\Phi^{-1}=P.
}
\]

This is no longer merely an abstract coordinate trick: \(\Phi\) is the reduction modulo 2 of the actual integral change of basis between two natural bases of the ramified ideal \(\mathfrak p_2\).

---

## 5. Exact commutative picture

[D] The full integral and mod-2 relationship is

\[
\boxed{
\begin{array}{ccc}
\mathfrak p_2\text{ in }\{f_1,f_2\}
& \xrightarrow{\times(2+\sqrt3)} &
\mathfrak p_2\text{ in }\{f_1,f_2\}\\
\downarrow C^{-1} && \downarrow C^{-1}\\
\mathfrak p_2\text{ in }\{e_1,e_2\}
& \xrightarrow{\times(2+\sqrt3)} &
\mathfrak p_2\text{ in }\{e_1,e_2\}
\end{array}
}
\]

with matrices

\[
\boxed{
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}},
\qquad
\boxed{M=\begin{pmatrix}2&3\\1&2\end{pmatrix}},
\qquad
\boxed{M=C^{-1}g_{12}C}.
\]

Modulo 2 this becomes

\[
\boxed{
\begin{array}{ccc}
\mathbf F_2^2
& \xrightarrow{\bar g} &
\mathbf F_2^2\\
\downarrow \Phi && \downarrow \Phi\\
\mathbf F_2^2
& \xrightarrow{P} &
\mathbf F_2^2
\end{array}
}
\]

where

\[
\bar g=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

---

## 6. Consequence for the ramified quotient

[D] Since

\[
V_2=\mathfrak p_2/2\mathfrak p_2\cong\mathbf F_2^2,
\]

the two finite descriptions are now seen to come from the same ideal quotient expressed in two different natural bases:

- ramified basis \(\{2,\sqrt3-1\}\): return is the transvection \(\bar g\);
- principal/Pell basis \(\{1+\sqrt3,3+\sqrt3\}\): return is the factor swap \(P\).

Hence

\[
\boxed{
\text{ramified transvection}
\quad\text{and}\quad
\text{Boolean factor exchange}
}
\]

are not merely conjugate abstractly; they are the same multiplication-by-\(2+\sqrt3\) endomorphism of \(\mathfrak p_2/2\mathfrak p_2\), written in two integral bases inherited from the arithmetic of \(\mathfrak p_2\).

This strengthens the earlier bridge substantially.

---

## 7. Relation to the Cone boost

[D] From v13.179, the same Pell unit \(\lambda=2+\sqrt3\) is the expanding null eigenvalue of the real Cone Lorentz boost, with reciprocal eigenvalue \(\lambda^{-1}=2-\sqrt3\).

Thus there is now an exact chain

\[
\boxed{
\text{Cone null scaling by }2+\sqrt3
\longleftrightarrow
\times(2+\sqrt3)\text{ on }\mathfrak p_2
\longrightarrow
\mathfrak p_2/2\mathfrak p_2
\longleftrightarrow
\{\bar g,P\}\text{ in two bases}.
}
\]

The real Lorentz return, Pell ideal action, ramified transvection, and Boolean swap are therefore four presentations of one return mechanism, with the final finite identifications mediated by the explicit ideal-basis change \(C\).

[I] This provides a substantially more concrete unification of the continuous Cone geometry and the finite Boolean layer than direct reduction of continuous mesh phases.

---

## 8. Audit guardrails

[Audit] The equality \(\bar C=\Phi\) is basis-dependent but canonical relative to the two natural bases chosen above. Do not promote it to a basis-free equality of named matrices.

[Audit] The real Cone null coordinates are not literally elements of \(\mathfrak p_2\) in general. The exact bridge is via the common Pell-unit action, not an identification of every real Cone point with an ideal-lattice point.

[Audit] This result does not prove that arbitrary continuous mesh phases reduce canonically to the Boolean quotient. The stronger finite bridge instead passes through the integral ramified ideal lattice.

[Audit] The factor swap \(P\) here is the mod-2 action in the principal/Pell basis. Its interpretation as Paper-A factor exchange uses the previously established action correspondence and should not be confused with equality of the underlying coordinate spaces.

---

## 9. Exact synthesis

The main theorem of this entry is

\[
\boxed{
[\times(2+\sqrt3)]_{\{2,\sqrt3-1\}}
=\begin{pmatrix}3&1\\2&1\end{pmatrix}=g_{12},
}
\]

while

\[
\boxed{
[\times(2+\sqrt3)]_{\{1+\sqrt3,3+\sqrt3\}}
=\begin{pmatrix}2&3\\1&2\end{pmatrix}.
}
\]

The integral basis change is

\[
\boxed{
C=\begin{pmatrix}1&2\\1&1\end{pmatrix},
\qquad
C^{-1}g_{12}C=\begin{pmatrix}2&3\\1&2\end{pmatrix},
}
\]

and modulo 2,

\[
\boxed{
\bar C=\Phi,
\qquad
\Phi\bar g\Phi^{-1}=P.
}
\]

Therefore the previously observed ramified/Boolean conjugacy is the mod-2 shadow of an explicit unimodular change of basis inside the ramified ideal \(\mathfrak p_2\).
