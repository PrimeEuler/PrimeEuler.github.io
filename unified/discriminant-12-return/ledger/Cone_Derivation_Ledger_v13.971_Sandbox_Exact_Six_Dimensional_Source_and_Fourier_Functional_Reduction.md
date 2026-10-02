# Cone Derivation Ledger v13.971 — Sandbox: Exact Six-Dimensional Source and Fourier-Functional Reduction for the Xi Phase Certificate

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact source reduction through the certified \(2+4\) Feshbach carrier; [D] exact Fourier-functional reduction; [D] explicit analytic-background bounds from the nonresonant tail moat; [I] identifies the final proof object as a \(6\times6\) solve plus bounded analytic backgrounds; [O] freeze the projected source/functionals in the residual-certified \(P_4\) basis and run outward interval evaluation on \([0,T]\)  
**Authorization:** Jeremy, 2026-10-02 ("awesome. eagerly awaiting :)")  
**Parents:** v13.823–836, v13.967–970  
**Collision check:** v13.970 is External Audit Round 148; v13.971 was absent immediately before this write.

---

## 0. Purpose

v13.967–969 reduce the Xi scalar certification to a bounded-window Weyl-sign problem with explicit phase uncertainty and stiff-complement control.

The remaining question is how to evaluate the exact source transform

\[
F_a(t)=\widehat{A_a^{-1}e^x}(t)
\]

without reconstructing the full infinite-dimensional inverse.

The certified low-energy tail structure from v13.823–836 already gives the answer.

The source and the Fourier functional can both be reduced exactly through the same \(2+4\) Feshbach carrier.

---

## 1. Certified transformed block operator [D]

At absolute shift

\[
\lambda=0,
\]

write the full parity operator in low-core/tail form and apply the positive tail congruence

\[
y=B_T^{1/2}v.
\]

With the exact rank-four spectral projector

\[
P_4=\mathbf 1_{(-0.02,0.02)}(J_T),
\qquad
Q_4=I-P_4,
\]

the transformed operator is

\[
\mathcal F(0)
=
\begin{pmatrix}
F_{CC}(0)&C_P(0)^*&C_Q(0)^*\\
C_P(0)&J_P&0\\
C_Q(0)&0&J_Q
\end{pmatrix}.
\]

The certified tail moat gives

\[
\boxed{
\|J_Q^{-1}\|<10.
}
\tag{1}
\]

The exact \(6\times6\) Feshbach matrix is

\[
\boxed{
\mathcal M_6(0)
=
\begin{pmatrix}
H_C(0)&C_P(0)^*\\
C_P(0)&J_P
\end{pmatrix},
}
\tag{2}
\]

with

\[
\boxed{
H_C(0)
=
F_{CC}(0)
-
C_Q(0)^*J_Q^{-1}C_Q(0).
}
\tag{3}
\]

---

## 2. Exact transformed source [D]

Let the original source coefficient vector be split as

\[
f=
\binom{f_C}{f_T}.
\]

After the tail congruence define

\[
\boxed{
g:=B_T^{-1/2}f_T.
}
\tag{4}
\]

Split

\[
g=g_P+g_Q,
\qquad
g_P=P_4g,
\qquad
g_Q=Q_4g.
\]

The full transformed source equation is

\[
\begin{pmatrix}
F_{CC}&C_P^*&C_Q^*\\
C_P&J_P&0\\
C_Q&0&J_Q
\end{pmatrix}
\begin{pmatrix}
u\\p\\q
\end{pmatrix}
=
\begin{pmatrix}
f_C\\g_P\\g_Q
\end{pmatrix}.
\]

The \(Q_4\) equation gives

\[
\boxed{
q
=
J_Q^{-1}
\left(
g_Q-C_Q u
\right).
}
\tag{5}
\]

Substitution into the core equation gives the exact reduced source

\[
\boxed{
f_6
=
\binom{
f_C-C_Q^*J_Q^{-1}g_Q
}{
g_P
}.
}
\tag{6}
\]

Therefore the reduced vector

\[
x_6=
\binom{u}{p}
\]

satisfies

\[
\boxed{
\mathcal M_6(0)x_6=f_6.
}
\tag{7}
\]

---

## 3. Exact source-resolvent scalar [D]

The full source quadratic form is

\[
\langle f,A^{-1}f\rangle.
\]

Using (5),

\[
\boxed{
\langle f,A^{-1}f\rangle
=
\langle g_Q,J_Q^{-1}g_Q\rangle
+
\langle
f_6,
\mathcal M_6(0)^{-1}f_6
\rangle.
}
\tag{8}
\]

Define the analytic-background scalar

\[
\boxed{
h_{\rm reg}
=
\langle g_Q,J_Q^{-1}g_Q\rangle.
}
\tag{9}
\]

Then the full source amplification is exactly

\[
\boxed{
h_{\rm reg}
+
f_6^*\mathcal M_6(0)^{-1}f_6.
}
\tag{10}
\]

Thus all singular/near-null source amplification is contained in the six-dimensional carrier.

---

## 4. Fourier evaluation functional [D]

For real \(t\), write the Fourier functional in the same transformed coordinates as

\[
h(t)
=
\begin{pmatrix}
h_C(t)\\
h_P(t)\\
h_Q(t)
\end{pmatrix}.
\]

Thus for a full transformed solution \((u,p,q)\),

\[
F_a(t)
=
h_C(t)^*u
+
h_P(t)^*p
+
h_Q(t)^*q.
\]

Insert (5):

\[
\begin{aligned}
F_a(t)
&=
h_C(t)^*u
+
h_P(t)^*p\\
&\quad+
h_Q(t)^*J_Q^{-1}
\left(
g_Q-C_Q u
\right).
\end{aligned}
\]

Collect the \(u\)-term.

Define

\[
\boxed{
h_{C,\rm red}(t)
=
h_C(t)
-
C_Q^*J_Q^{-1}h_Q(t),
}
\tag{11}
\]

and

\[
\boxed{
h_6(t)
=
\binom{
h_{C,\rm red}(t)
}{
h_P(t)
}.
}
\tag{12}
\]

Also define the analytic Fourier-background term

\[
\boxed{
r_a(t)
=
h_Q(t)^*J_Q^{-1}g_Q.
}
\tag{13}
\]

Then

\[
\boxed{
F_a(t)
=
r_a(t)
+
h_6(t)^*
\mathcal M_6(0)^{-1}
f_6.
}
\tag{14}
\]

This is the exact six-dimensional Fourier-transform formula needed by the phase certificate.

---

## 5. Uniform background bounds [D]

From

\[
\|J_Q^{-1}\|<10,
\]

we obtain

\[
\boxed{
|h_{\rm reg}|
\le
10\|g_Q\|^2,
}
\tag{15}
\]

\[
\boxed{
\|
f_C-
f_{6,C}
\|
\le
10\|C_Q\|\,\|g_Q\|,
}
\tag{16}
\]

\[
\boxed{
\|
h_C(t)-h_{6,C}(t)
\|
\le
10\|C_Q\|\,\|h_Q(t)\|,
}
\tag{17}
\]

and

\[
\boxed{
|r_a(t)|
\le
10\|h_Q(t)\|\,\|g_Q\|.
}
\tag{18}
\]

Using the certified coupling-energy caps,

\[
\|C_e\|^2<0.0256,
\qquad
\|C_o\|^2<0.0416,
\]

gives

\[
\boxed{
\|C_{Q,e}\|<0.16,
\qquad
\|C_{Q,o}\|<0.204.
}
\tag{19}
\]

Hence the analytic source and functional background corrections are quantitatively bounded before any six-dimensional solve is performed.

---

## 6. Projected source coordinates in a \(B_T\)-orthonormal numerical \(P_4\) basis [D]

Let

\[
\widehat Q
\]

be a \(B_T\)-orthonormal numerical generalized-Ritz basis approximating \(\operatorname{Ran}P_4\).

Its transformed orthonormal basis is

\[
\widehat Y
=
B_T^{1/2}\widehat Q.
\]

The transformed tail source is

\[
g=B_T^{-1/2}f_T.
\]

Therefore its numerical four-channel coordinates require no explicit square root:

\[
\boxed{
\widehat Y^*g
=
\widehat Q^*f_T.
}
\tag{20}
\]

Likewise, if \(p_T(t)\) is the original tail coefficient vector of the Fourier functional,

\[
\boxed{
\widehat Y^*B_T^{-1/2}p_T(t)
=
\widehat Q^*p_T(t).
}
\tag{21}
\]

Thus the source and Fourier projections can be reconstructed from the already-certified \(P_4\) Ritz basis using ordinary coefficient inner products.

No new \(B_T^{\pm1/2}\) computation is required.

---

## 7. Subspace-error propagation [D]

Let

\[
\widehat P_4
\]

denote the numerical transformed projector.

The certified block-energy refinements give

\[
\boxed{
\|P_{4,e}-\widehat P_{4,e}\|<0.0544,
}
\tag{22}
\]

\[
\boxed{
\|P_{4,o}-\widehat P_{4,o}\|<0.0930.
}
\tag{23}
\]

Therefore

\[
\boxed{
\|
(P_4-\widehat P_4)g
\|
\le
\varepsilon_P\|g\|,
}
\tag{24}
\]

and

\[
\boxed{
\|
(P_4-\widehat P_4)h(t)
\|
\le
\varepsilon_P\|h(t)\|,
}
\tag{25}
\]

with the sector-specific \(\varepsilon_P\) from (22)–(23).

This supplies a direct error budget for replacing exact four-channel source/functionals by the residual-certified numerical carrier.

---

## 8. Why the six-dimensional route is better than a raw source solve [D/I]

The direct \(A^{-1}e^x\) finite sections are dominated by huge near-null amplitudes.

The phase scalar, however, depends only on the real-axis sign of

\[
m_a(t)
=
-
\frac{\Re Z_a(t)}{\Im Z_a(t)},
\qquad
Z_a(t)=(t-i)F_a(t).
\]

Equation (14) shows that the exact \(F_a(t)\) is determined by:

1. one \(6\times6\) solve;
2. four projected source coordinates;
3. four projected Fourier coordinates;
4. bounded analytic \(Q_4\) backgrounds.

No full infinite inverse is needed.

Thus the phase-window theorem of v13.967 can be driven directly by the exact low-energy carrier already certified in v13.823–836.

---

## 9. Remaining finite dataset [O]

The architecture is now complete.

To instantiate the first proof-grade \(a=1\) scalar interval, freeze:

1. the residual-certified numerical basis
   \[
   \widehat Q_{4,\pm};
   \]
2. the projected source coordinates
   \[
   \widehat Q_{4,\pm}^*f_{T,\pm};
   \]
3. the projected Fourier coordinates
   \[
   \widehat Q_{4,\pm}^*p_{T,\pm}(t)
   \quad
   (0\le t\le T);
   \]
4. the \(2\times2\) low-core source/functionals;
5. the already-certified grouped coupling and analytic-background errors.

Then solve the outward interval \(6\times6\) systems and feed the resulting enclosure for

\[
F_a(t)
\]

into the v13.967 uncertain-window phase budget.

The only missing object is now a finite numerical payload, not a missing operator theorem.

---

## 10. R-statistic cross-lane note [I/G]

The new sieve-flow R-statistic reproducer independently detects low zeta frequencies in the logarithmic arithmetic coordinate.

This is qualitatively consistent with the low-height phase-window strategy.

However no R-statistic value enters equations (1)–(25).

The Xi scalar certificate remains entirely source-faithful to Suzuki's operator.

---

## 11. Result

At \(\lambda=0\), the exact infinite-dimensional source transform admits the representation

\[
\boxed{
F_a(t)
=
r_a(t)
+
h_6(t)^*
\mathcal M_6(0)^{-1}
f_6,
}
\]

with

\[
\boxed{
f_6
=
\binom{
f_C-C_Q^*J_Q^{-1}g_Q
}{
P_4B_T^{-1/2}f_T
},
}
\]

and

\[
\boxed{
h_6(t)
=
\binom{
h_C(t)-C_Q^*J_Q^{-1}h_Q(t)
}{
P_4B_T^{-1/2}p_T(t)
}.
}
\]

The infinite nonresonant tail contributes only through analytic backgrounds bounded by

\[
\|J_Q^{-1}\|<10.
\]

Therefore the first rigorous finite-\(a\) Xi-scalar enclosure is now exactly a **six-dimensional interval solve plus the phase-window error budget**.
