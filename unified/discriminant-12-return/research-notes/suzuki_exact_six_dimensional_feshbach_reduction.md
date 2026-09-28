# Exact \(2+4\) Feshbach/Riesz Reduction for the Full \(\rho=0.02\) Window

Lane A finite/resonance branch.

Status: exact operator reduction.  No ordinary six-root multiplicity claim is made here.

## 1. Tail spectral splitting

On the positive tail Hilbert space write

\[
J_T=B_T^{-1/2}A_TB_T^{-1/2}.
\]

The certified projector

\[
P_4=\mathbf 1_{(-0.02,0.02)}(J_T)
\]

has rank four, and with \(Q_4=I-P_4\),

\[
\sigma(J_T|_{\operatorname{Ran}Q_4})\cap[-0.10,0.10]=\varnothing.
\]

Hence for every complex \(z\) with \(|z|<0.10\),

\[
Q_4(J_T-z)^{-1}Q_4
\]

is analytic wherever \(z\) avoids the real complementary spectrum. In particular it is analytic throughout the open disk \(|z|<0.10\).

## 2. Full transformed block pencil

Restore the two low-core coordinates \(\mathcal H_C\), \(\dim\mathcal H_C=2\), and use the transformed tail coordinate \(y=B_T^{1/2}v\).

The full pencil

\[
F(z)=A-zB_{\rm sm}
\]

is congruent to the block operator

\[
\mathcal F(z)=
\begin{pmatrix}
F_{CC}(z)&C(z)^*\\
C(z)&J_T-z
\end{pmatrix},
\]

where

\[
C(z)=B_T^{-1/2}F_{TC}(z).
\]

Split the tail by \(P_4\oplus Q_4\).  Since \(P_4\) is a spectral projector of \(J_T\),

\[
P_4J_TQ_4=0.
\]

Thus

\[
\mathcal F(z)=
\begin{pmatrix}
F_{CC}(z)&C_P(z)^*&C_Q(z)^*\\
C_P(z)&J_P-z&0\\
C_Q(z)&0&J_Q-z
\end{pmatrix},
\]

with

\[
J_P=P_4J_TP_4,
\qquad
J_Q=Q_4J_TQ_4,
\]

and

\[
C_P=P_4C,\qquad C_Q=Q_4C.
\]

## 3. Eliminate the exact nonresonant complement

For \(|z|<0.10\), \(J_Q-z\) is invertible except at the real complementary spectrum, which is absent from this disk.

Therefore block Gaussian elimination gives an exact \(6\times6\) analytic Feshbach matrix on

\[
\mathcal H_C\oplus\operatorname{Ran}P_4:
\]

\[
\boxed{
\mathcal M_6(z)=
\begin{pmatrix}
H_C(z)&C_P(z)^*\\
C_P(z)&J_P-z
\end{pmatrix},
}
\]

where

\[
\boxed{
H_C(z)
=
F_{CC}(z)
-
C_Q(z)^*(J_Q-z)^{-1}C_Q(z).
}
\]

The eliminated block is analytic throughout \(|z|<0.10\).

Moreover,

\[
\boxed{
F(z)\text{ is singular}
\iff
\mathcal M_6(z)\text{ is singular},
\qquad |z|<0.10.
}
\]

Kernel dimensions agree:

\[
\boxed{
\dim\ker F(z)=\dim\ker\mathcal M_6(z).
}
\]

The full vector is recovered from a reduced vector \((u,p)\) by

\[
q=
-
(J_Q-z)^{-1}C_Q(z)u
\]

in the \(Q_4\)-component.

Thus the ordinary full root count in the certified window is exactly the zero count of a six-dimensional analytic matrix function.

## 4. Analytic background bound

For real \(|\delta|\le0.02\),

\[
\|(J_Q-\delta)^{-1}\|<12.5.
\]

Hence

\[
\boxed{
\|C_Q(\delta)^*(J_Q-\delta)^{-1}C_Q(\delta)\|
\le
12.5\,\|C_Q(\delta)\|^2
\le
12.5\,\|C(\delta)\|^2.
}
\]

Using the already-certified coupling caps gives the crude but rigorous bounds

\[
\|H_{C,e}(\delta)-F_{CC,e}(\delta)\|
<
12.5(0.0256)
=
0.32,
\]

\[
\|H_{C,o}(\delta)-F_{CC,o}(\delta)\|
<
12.5(0.0416)
=
0.52.
\]

These are intentionally crude; practical contour certification should evaluate the analytic background rather than use these worst-case bounds.

## 5. Numerical carrier

Let \(\widehat P_4\) be the unchanged residual-certified numerical four-space.

The sharpened block-energy bounds are

\[
\|P_{4,e}-\widehat P_{4,e}\|<0.0544,
\qquad
\|P_{4,o}-\widehat P_{4,o}\|<0.0930.
\]

Its Ritz matrices obey

\[
\max |\widehat\delta_{j,e}|<0.00030,
\qquad
\max |\widehat\delta_{j,o}|<0.01050.
\]

The numerical grouped core-to-cluster coupling satisfies

\[
\widehat G(\delta)
=
C(\delta)^*\widehat P_4C(\delta)
=
K(\delta)^TK(\delta),
\]

with the explicit quadratic polynomials recorded at v13.828.

The exact grouped coupling error sharpens to

\[
\|C_e^*(P_4-\widehat P_4)C_e\|<0.00140,
\]

\[
\|C_o^*(P_4-\widehat P_4)C_o\|<0.00387.
\]

Thus every ingredient of the \(2+4\) carrier is now quantitatively controlled at the grouped level.

## 6. Why a real-axis endpoint argument is insufficient

The externally audited full endpoint theorem gives

\[
\operatorname{ind}_-F(-0.02)=2,
\qquad
\operatorname{ind}_-F(+0.02)=4.
\]

Therefore the full real spectral flow is \(+2\), which proves at least two real crossing roots.

However the exact tail projector contributes four poles to the meromorphic two-mode Schur map, not four automatic full roots.

In an indefinite pencil, two real roots can collide and leave the real axis as a complex-conjugate pair.  Pontryagin index two limits such behavior but does not eliminate it from endpoint data alone.

Hence six ordinary roots require a genuine complex-plane/Riesz count for \(\mathcal M_6(z)\), or an equivalent Krein-aware real-axis theorem excluding neutral/nonreal collisions.

## 7. Final certificate target

Choose a contour \(\Gamma\) inside \(|z|<0.10\) enclosing the real interval \([-0.02,0.02]\), with no zeros on the contour.

Because \(J_Q-z\) is analytic and invertible there,

\[
N_{\rm full}(\Gamma)
=
\frac{1}{2\pi i}
\oint_\Gamma
\operatorname{tr}
\left[
\mathcal M_6(z)^{-1}
\mathcal M_6'(z)
\right]dz.
\]

Equivalently,

\[
N_{\rm full}(\Gamma)
=
\operatorname{wind}_\Gamma\det\mathcal M_6(z).
\]

A certified winding number of six would close the ordinary multiplicity question, including any non-real roots inside the contour.

To prove six **real** roots one then additionally excludes non-real zeros or certifies their absence by symmetry plus a contour subdivision.

## Result

The remaining full-pencil spectral problem in \(|z|<0.10\) is exactly finite-dimensional:

\[
\boxed{
F(z)\text{ singular}
\iff
\mathcal M_6(z)\text{ singular},
}
\]

where

\[
\boxed{
\dim\mathcal M_6=6.
}
\]

Thus the last ordinary-multiplicity gate is a certified six-dimensional Riesz/winding calculation, not another infinite-tail inertia problem.
