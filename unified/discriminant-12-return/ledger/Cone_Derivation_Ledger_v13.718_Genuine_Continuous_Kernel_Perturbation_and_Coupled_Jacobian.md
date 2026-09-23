# Cone Derivation Ledger v13.718 — Genuine Continuous-Kernel Perturbation and Coupled Jacobian

Date: 2026-09-23

Status: exact coupled-deformation gate following v13.711, with relevance check against the new Xi/Zeta cone findings v13.713–717 and audits v13.714/v13.716.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization and relevance check

The live ledger advanced substantially after v13.711:

- v13.712 independently audited v13.708–711 and passed the Fredholm/Weyl four-character and product-Jacobian program;
- v13.713 opened the centered Xi/Zeta cone lane and found the exact four-character package
  \[
  \log|\xi|,\quad \Re(\xi'/\xi),\quad \Im(\xi'/\xi),\quad \arg\xi;
  \]
- v13.715 constructed the exact one-sided signed prime–archimedean radial current
  \[
  d\nu_\xi=W_\infty(r)\,dr-d\mu_\Lambda(r);
  \]
- v13.716 independently audited that current numerically and analytically;
- v13.717 constructed the globally convergent centered two-sided theta/Mellin current
  \[
  \Xi(w)=\frac12+\left(w^2-\frac14\right)\int_{\mathbb R}K_\theta(r)e^{wr}\,dr,
  \]
  with \(K_\theta\) real and even, making \(w\mapsto-w\) manifest.

These findings are directly relevant to the present Suzuki gate in one precise way: they supply canonical real/even logarithmic-radius kernels and currents that are natural **candidate perturbation directions** for a continuous-kernel operator. They do **not** yet identify the Xi theta kernel with Suzuki's Section-8 kernel, and v13.717 explicitly leaves that transform/intertwiner open.

Accordingly the present gate derives the genuine coupled first variation for an arbitrary admissible real reflection-even continuous kernel perturbation \(h\). The Xi theta current may later be inserted as a candidate \(h\) only after the variable/operator map is fixed.

Immediately before this write the live head was v13.717, commit \`70776f8528b6020b9cda80f7a88abf9369a13b7e\`. No v13.718 collision was present.

## 1. Genuine Section-8 kernel perturbation [D]

Let
\[
S=S_A
\]
be Suzuki's positive invertible Section-8 energy operator at the fixed lower-bound shift used to define the energy space.

Perturb its continuous kernel by a real reflection-compatible continuous kernel \(h\):
\[
\boxed{
S_\varepsilon=S+\varepsilon H,
}
\]
where
\[
(Hf)(x)=\int_{-A}^A h(x,y)f(y)\,dy,
\]
\[
h(x,y)=h(y,x)\in\mathbb R,
\qquad
h(-x,-y)=h(x,y).
\]

Then \(H\) is self-adjoint Hilbert--Schmidt and commutes with reflection \(R\). For sufficiently small real \(\varepsilon\), positivity/invertibility of \(S_\varepsilon\) persists.

This is now a genuine perturbation of the continuous-kernel energy operator; unlike v13.711, the induced defect vectors and Weyl data are allowed to vary.

## 2. Exact inverse variation [D]

For
\[
R_S=S^{-1},
\]
the standard resolvent identity gives
\[
\boxed{
\delta S^{-1}
:=
\left.\partial_\varepsilon S_\varepsilon^{-1}\right|_0
=
-S^{-1}HS^{-1}.
}
\]

In the v13.685 continuous-kernel notation define
\[
d_z:=\bar D e_z,
\qquad
d_\pm:=\bar D e_{\pm i}.
\]

The canonical defect solutions satisfy
\[
u_z=S^{-1}d_z,
\qquad
u_\pm=S^{-1}d_\pm.
\]

Hence
\[
\boxed{
\delta u_z=-S^{-1}Hu_z,
\qquad
\delta u_\pm=-S^{-1}Hu_\pm.
}
\]

This is the physically induced cross-response absent from the product model of v13.711.

## 3. Variation of the continuous-kernel characteristic coefficients [D]

v13.685 uses
\[
F_\pm(z)
=
\overline{
\langle d_{\bar z},S^{-1}d_\pm\rangle
}.
\]

Therefore
\[
\delta F_\pm(z)
=
-\overline{
\langle d_{\bar z},S^{-1}HS^{-1}d_\pm\rangle
}.
\]

Since \(u_{\bar z}=S^{-1}d_{\bar z}\) and \(u_\pm=S^{-1}d_\pm\), self-adjointness of \(S^{-1}\) gives
\[
\boxed{
\delta F_\pm(z)
=
-\overline{\langle u_{\bar z},Hu_\pm\rangle}.
}
\]

With
\[
A(z)=(z-i)F_+(z),
\qquad
B(z)=(z+i)F_-(z),
\]
we obtain
\[
\boxed{
\delta A=(z-i)\delta F_+,
\qquad
\delta B=(z+i)\delta F_-.
}
\]

## 4. Induced Weyl variation [D]

In the stabilized project convention,
\[
m(z)=-i\frac{A+B}{A-B}.
\]

Let
\[
N=A+B,\qquad D=A-B.
\]
Then
\[
m=-iN/D.
\]

Differentiate:
\[
\delta m
=
-i\frac{(\delta A+\delta B)(A-B)-(A+B)(\delta A-\delta B)}
{(A-B)^2}.
\]

The numerator simplifies exactly:
\[
(\delta A+\delta B)(A-B)-(A+B)(\delta A-\delta B)
=
2(A\,\delta B-B\,\delta A).
\]

Hence
\[
\boxed{
\delta m(z)
=
-\frac{2i\,[A(z)\delta B(z)-B(z)\delta A(z)]}
{[A(z)-B(z)]^2}.
}
\]

Substituting the kernel matrix elements:
\[
\boxed{
\delta m(z)
=
\frac{2i}
{(A-B)^2}
\left[
A(z)(z+i)\overline{\langle u_{\bar z},Hu_-\rangle}
-
B(z)(z-i)\overline{\langle u_{\bar z},Hu_+\rangle}
\right].
}
\]

This is the exact first variation of the project Weyl coordinate induced by a genuine Section-8 kernel perturbation.

## 5. Induced Cayley-log variation [D]

For
\[
s(z)=\frac{m(z)-i}{m(z)+i},
\qquad
\ell(z)=\log s(z),
\]
the differential is
\[
d\ell=\frac{2i}{m^2+1}\,dm.
\]

Therefore
\[
\boxed{
\partial_\varepsilon\ell
=
\frac{2i\,\delta m}{m^2+1}.
}
\]

Substituting the previous result gives
\[
\boxed{
\partial_\varepsilon\ell
=
-\frac{4}
{(m^2+1)(A-B)^2}
\left[
A(z)(z+i)\overline{\langle u_{\bar z},Hu_-\rangle}
-
B(z)(z-i)\overline{\langle u_{\bar z},Hu_+\rangle}
\right].
}
\]

Thus the genuine bulk perturbation generally moves the boost/Weyl coordinate as expected.

## 6. Fredholm-scale variation under the same kernel perturbation [D]

Let
\[
\tau(z)=\log\det_2(I-zS).
\]

For \(S_\varepsilon=S+\varepsilon H\),
\[
\boxed{
\partial_\varepsilon\tau
=
-z\,\operatorname{Tr}
\left(
[(I-zS)^{-1}-I]H
\right).
}
\]

Because
\[
(I-zS)^{-1}-I
=
z(I-zS)^{-1}S,
\]
equivalently
\[
\boxed{
\partial_\varepsilon\tau
=
-z^2\operatorname{Tr}
\left(
(I-zS)^{-1}SH
\right).
}
\]

The trace exists because the bracketed resolvent difference is Hilbert--Schmidt and \(H\) is Hilbert--Schmidt, so their product is trace class.

## 7. Independent boundary-coordinate deformation [D]

Retain the real ordinary-boundary-triple translation from v13.711:
\[
\boxed{
m_\eta(z)=m(z)+\eta,
\qquad \eta\in\mathbb R.
}
\]

This changes the boundary coordinate but not the continuous-kernel operator \(S\). Therefore
\[
\boxed{
\partial_\eta\tau=0.
}
\]

For the Cayley logarithm,
\[
\boxed{
\partial_\eta\ell
=
\frac{2i}{m(z)^2+1}.
}
\]

At a point where \(m(z)\ne\pm i\), this is nonzero.

## 8. The coupled four-derivative matrix [D]

At \((\varepsilon,\eta)=(0,0)\):
\[
\boxed{
\begin{pmatrix}
\partial_\varepsilon\tau&
\partial_\eta\tau\\[1mm]
\partial_\varepsilon\ell&
\partial_\eta\ell
\end{pmatrix}
=
\begin{pmatrix}
-z\,\operatorname{Tr}([(I-zS)^{-1}-I]H)&0\\[2mm]
\dfrac{2i\,\delta m_H(z)}{m(z)^2+1}&
\dfrac{2i}{m(z)^2+1}
\end{pmatrix}.
}
\]

This matrix is lower triangular.

Therefore the physically induced Weyl cross-term does **not** enter the determinant:
\[
\boxed{
J_H(z)
=
-\frac{2iz}
{m(z)^2+1}
\operatorname{Tr}
\left(
[(I-zS)^{-1}-I]H
\right).
}
\]

Equivalently,
\[
\boxed{
J_H(z)
=
-\frac{2iz^2}
{m(z)^2+1}
\operatorname{Tr}
\left(
(I-zS)^{-1}SH
\right).
}
\]

Thus:
\[
\boxed{
J_H(z)\ne0
}
\]
whenever
\[
m(z)\ne\pm i
\]
and the Fredholm scale responds nontrivially:
\[
\operatorname{Tr}
\left(
[(I-zS)^{-1}-I]H
\right)\ne0.
\]

## 9. Explicit genuine kernel witness [D]

Choose a normalized definite-parity eigenvector
\[
Sf=\mu f,\qquad \mu\ne0,
\]
and take the continuous rank-one kernel perturbation
\[
H=|f\rangle\langle f|
\]
when \(f\) is represented by a continuous eigenfunction of the continuous-kernel operator. Mercer/Fredholm regularity for a continuous kernel gives continuity of nonzero-eigenvalue eigenfunctions.

Then
\[
\partial_\varepsilon\tau
=
-\frac{z^2\mu}{1-z\mu}.
\]

The induced Weyl variation is no longer set to zero; it is the explicit defect-matrix expression from Sections 4–5.

Nevertheless
\[
\boxed{
J_f(z)
=
-\frac{2iz^2\mu}
{(1-z\mu)(m(z)^2+1)}.
}
\]

Therefore, under
\[
z\ne0,\qquad
\mu\ne0,\qquad
1-z\mu\ne0,\qquad
m(z)\ne\pm i,
\]
one has
\[
\boxed{
J_f(z)\ne0.
}
\]

This proves that the local rank-two result survives a genuine coupled continuous-kernel perturbation.

## 10. Relevance of the new Xi/Zeta cone current [D/G/O]

The new Xi lane changes the interpretation of the next perturbation to test.

v13.717 supplies a canonical real even radial kernel
\[
K_\theta(r)
=
e^{|r|/2}
\sum_{n\ge1}e^{-\pi n^2e^{2|r|}}.
\]

Its parity is exactly compatible with the admissibility conditions used above:
\[
K_\theta(-r)=K_\theta(r),
\qquad
K_\theta(r)\in\mathbb R.
\]

Similarly v13.715 supplies the signed prime–archimedean radial current
\[
d\nu_\xi(r)
=
W_\infty(r)\,dr-d\mu_\Lambda(r).
\]

These results make it natural to seek an operator perturbation \(H_\xi\) obtained from the Xi radial current and insert it into the exact formulas
\[
\delta\tau[H_\xi],
\qquad
\delta m[H_\xi],
\qquad
\delta\ell[H_\xi].
\]

But the variables are not yet identified:
- Suzuki's kernel acts on \(x,y\in[-A,A]\);
- the Xi kernels live on logarithmic radius \(r\in\mathbb R\).

Therefore:
\[
\boxed{
\text{no }H_\xi\text{ is promoted until an explicit map }r\leftrightarrow(x,y)
\text{ or a convolution/difference-coordinate transform is derived.}
}
\]

The obvious candidate is the translation-invariant difference coordinate
\[
r=x-y,
\]
because Suzuki's screw part already appears as \(g_A(x-y)\). This is now the highest-value cross-lane bridge to test.

## 11. Result [D]

For a genuine admissible continuous-kernel perturbation \(H\):
\[
\boxed{
\delta S^{-1}=-S^{-1}HS^{-1},
}
\]
\[
\boxed{
\delta F_\pm(z)
=
-\overline{\langle u_{\bar z},Hu_\pm\rangle},
}
\]
\[
\boxed{
\delta m(z)
=
-\frac{2i(A\delta B-B\delta A)}{(A-B)^2},
}
\]
\[
\boxed{
\delta\ell(z)
=
\frac{2i\,\delta m(z)}{m(z)^2+1},
}
\]
and
\[
\boxed{
\delta\tau(z)
=
-z\,\operatorname{Tr}([(I-zS)^{-1}-I]H).
}
\]

Together with the independent boundary translation \(m\mapsto m+\eta\),
\[
\boxed{
J_H(z)
=
-\frac{2iz}
{m(z)^2+1}
\operatorname{Tr}([(I-zS)^{-1}-I]H).
}
\]

Hence:
\[
\boxed{
\textbf{PASS: local rank-two independence survives genuine coupled kernel/Weyl variation.}
}
\]

## 12. Scope [G]

This is stronger than v13.711 because the Weyl function is now allowed to respond to the kernel perturbation.

It proves local rank two in a Suzuki-type continuous-kernel family plus an independent boundary-coordinate direction.

It does **not** yet identify the Xi/Zeta radial current with a Suzuki kernel deformation, and does not establish a determinant identity with \(\xi\).

## 13. Next gate [O]

Use the exact difference-coordinate structure
\[
g_A(x-y)
\]
of Suzuki's continuous screw kernel and test the candidate cross-lane map
\[
\boxed{r=x-y.}
\]

Specifically:

1. pull the even theta kernel \(K_\theta(r)\) back to
   \[
   h_\theta(x,y)=K_\theta(x-y);
   \]
2. verify Hilbert--Schmidt/reflection/self-adjoint admissibility on \([-A,A]^2\);
3. compute its Fredholm response
   \[
   \delta\tau[h_\theta];
   \]
4. compute its induced Weyl response
   \[
   \delta m[h_\theta];
   \]
5. compare the resulting exponential/Fourier matrix elements with the theta/Mellin transform in v13.717.

A nontrivial exact transform relation here would be the first genuine analytic bridge between the independently established Suzuki/operator and Xi/Zeta cone lanes.
