# Cone Derivation Ledger v13.836 — Exact \(2+4\) Six-Dimensional Full-Pencil Feshbach Reduction

Date: 2026-09-28.

Lane: A finite/resonance branch.

Status: [T] exact six-dimensional analytic reduction of the full generalized pencil in the certified low-energy disk; [C] all infinite nonresonant tail degrees eliminated through the exact rank-four tail projector and its \(0.08\) moat; [G] the final ordinary six-root multiplicity claim remains a winding/Riesz-count problem.

Parents: v13.823–835.

Research artifact:

- research-notes/suzuki_exact_six_dimensional_feshbach_reduction.md
  - commit 20cfa288331cf44421ec0f4c23b3950275181b6c

No GitHub workflow/status run is attached.

## 1. Exact spectral splitting

On the certified positive tail,

\[
J_T=B_T^{-1/2}A_TB_T^{-1/2}.
\]

The spectral projector

\[
P_4=\mathbf 1_{(-0.02,0.02)}(J_T)
\]

has exact rank four.

Let

\[
Q_4=I-P_4.
\]

The nested \(\rho=0.02/0.10\) theorem gives

\[
\sigma(J_T|_{\operatorname{Ran}Q_4})
\cap[-0.10,0.10]
=
\varnothing.
\]

Therefore the complementary resolvent

\[
Q_4(J_T-z)^{-1}Q_4
\]

is analytic throughout the open disk

\[
|z|<0.10.
\]

## 2. Restore the two low-core modes

Write the full parity space as

\[
\mathcal H
=
\mathcal H_C\oplus\mathcal H_T,
\qquad
\dim\mathcal H_C=2.
\]

After the positive tail congruence \(y=B_T^{1/2}v\), the full pencil

\[
F(z)=A-zB_{\rm sm}
\]

is congruent to

\[
\mathcal F(z)
=
\begin{pmatrix}
F_{CC}(z)&C(z)^*\\
C(z)&J_T-z
\end{pmatrix},
\]

where

\[
C(z)=B_T^{-1/2}F_{TC}(z).
\]

Split the tail further into

\[
\operatorname{Ran}P_4
\oplus
\operatorname{Ran}Q_4.
\]

Because \(P_4\) is an exact spectral projector,

\[
P_4J_TQ_4=0.
\]

Thus

\[
\mathcal F(z)
=
\begin{pmatrix}
F_{CC}(z)&C_P(z)^*&C_Q(z)^*\\
C_P(z)&J_P-z&0\\
C_Q(z)&0&J_Q-z
\end{pmatrix}.
\]

## 3. Exact elimination of the infinite nonresonant tail

Inside

\[
|z|<0.10,
\]

the operator

\[
J_Q-z
\]

is invertible.

Its Schur elimination gives the exact analytic six-dimensional matrix function

\[
\boxed{
\mathcal M_6(z)
=
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

The eliminated infinite complement contributes only through the analytic \(2\times2\) background \(H_C\).

## 4. Exact equivalence

Block Gaussian elimination gives, for every

\[
|z|<0.10,
\]

\[
\boxed{
F(z)\text{ singular}
\iff
\mathcal M_6(z)\text{ singular}.
}
\]

Moreover,

\[
\boxed{
\dim\ker F(z)
=
\dim\ker\mathcal M_6(z).
}
\]

Thus ordinary algebraic/root multiplicity in the low-energy disk is an exactly six-dimensional problem.

The omitted infinite tail cannot create an additional singularity independently of \(\mathcal M_6\).

## 5. Quantitative regularity of the eliminated background

For real

\[
|\delta|\le0.02,
\]

the exact moat gives

\[
\|(J_Q-\delta)^{-1}\|<12.5.
\]

Therefore

\[
\|C_Q^*(J_Q-\delta)^{-1}C_Q\|
\le
12.5\|C_Q\|^2
\le
12.5\|C\|^2.
\]

Using the certified coupling-energy caps,

\[
\|C_e\|^2<0.0256,
\qquad
\|C_o\|^2<0.0416,
\]

gives the crude uniform bounds

\[
\boxed{
\|H_{C,e}-F_{CC,e}\|<0.32,
}
\]

\[
\boxed{
\|H_{C,o}-F_{CC,o}\|<0.52.
}
\]

These are not intended as final numerical enclosures; the analytic background should be evaluated directly for the contour proof.

## 6. Certified numerical four-channel carrier

The block-energy refinement of v13.835 gives

\[
\boxed{
\|P_{4,e}-\widehat P_{4,e}\|<0.0544,
}
\]

\[
\boxed{
\|P_{4,o}-\widehat P_{4,o}\|<0.0930.
}
\]

The unchanged numerical Ritz matrices satisfy

\[
\max|\widehat\delta_{j,e}|<0.00030,
\]

\[
\max|\widehat\delta_{j,o}|<0.01050.
\]

The grouped core-to-cluster error sharpens to

\[
\boxed{
\|C_e^*(P_{4,e}-\widehat P_{4,e})C_e\|<0.00140,
}
\]

\[
\boxed{
\|C_o^*(P_{4,o}-\widehat P_{4,o})C_o\|<0.00387.
}
\]

Hence the numerical carrier is now sufficiently close to the exact four-channel space to serve as a controlled center for the final \(6\times6\) contour calculation.

## 7. Relation to the exact endpoint theorem

The externally audited full endpoint theorem gives

\[
\operatorname{ind}_-F(-0.02)=2,
\]

\[
\operatorname{ind}_-F(+0.02)=4.
\]

Therefore the exact real spectral flow through the interval is

\[
+2.
\]

This guarantees at least two real roots, but it does not determine the total ordinary multiplicity because \(\mathcal M_6\) is a Pontryagin/Krein problem and may in principle possess neutral or non-real roots.

## 8. Final count as a winding number

Choose a positively oriented contour \(\Gamma\subset\{|z|<0.10\}\) surrounding the inner window and avoiding zeros of \(\det\mathcal M_6\).

The ordinary algebraic root count is exactly

\[
\boxed{
N_{\rm full}(\Gamma)
=
\frac{1}{2\pi i}
\oint_\Gamma
\operatorname{tr}
\left[
\mathcal M_6(z)^{-1}
\mathcal M_6'(z)
\right]dz.
}
\]

Equivalently,

\[
\boxed{
N_{\rm full}(\Gamma)
=
\operatorname{wind}_\Gamma
\det\mathcal M_6(z).
}
\]

A certified winding number six closes the ordinary full multiplicity question regardless of whether any enclosed roots are non-real.

A subsequent contour subdivision or Krein-type argument is needed if one additionally wants all six roots certified real.

## 9. What remains

All infinite-dimensional inertia and tail-multiplicity questions in this finite/resonance branch are closed.

The final unresolved ordinary-multiplicity gate is now:

1. evaluate the exact/numerical \(6\times6\) matrix \(\mathcal M_6(z)\) on a complex contour;
2. propagate the \(P_4\), grouped-coupling, and analytic-background errors to a determinant or smallest-singular-value enclosure;
3. certify the winding number;
4. if it equals six, subdivide the contour to determine whether all six zeros lie on the real axis.

## Guardrails

This entry does not claim:

- that the winding number is already six;
- six real roots;
- individual simplicity;
- any result on the separate Hilbert–Pólya boundary-normalization gate identified in v13.833.

## Result

The entire full low-energy root problem is exactly reduced to

\[
\boxed{
\det\mathcal M_6(z)=0,
\qquad
\dim\mathcal M_6=6,
}
\]

with the infinite nonresonant tail eliminated analytically.

The only remaining ordinary-multiplicity question in this finite/resonance branch is the certified \(6\times6\) Riesz/winding count.
