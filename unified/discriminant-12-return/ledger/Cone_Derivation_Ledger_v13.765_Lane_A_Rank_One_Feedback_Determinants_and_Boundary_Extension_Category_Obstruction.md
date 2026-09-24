# Cone Derivation Ledger v13.765 — Lane A Rank-One Feedback Determinants and Boundary-Extension Category Obstruction

Date: 2026-09-24

Lane: A — Screw/Helix–Weil–Hermite–Biehler Program.

Status: [D] exact Fredholm determinant realization of the two corrected Suzuki feedback denominators; [N] exact obstruction to identifying them with Suzuki's rank-one boundary-extension/Hermite–Biehler determinant from presently established data; [X] incorporates the audit-PASSed Lane-B finite-prime bulk trace without overreach.

Parents: v13.661, v13.673, v13.742, v13.745, v13.758, v13.761–764.

## 0. Synchronization

The live ledger was checked immediately before this write. Current head is v13.764 (External Audit Round 94); no v13.765 exists and there is no numbering collision.

Round 94 PASSes Lane B v13.763 and explicitly confirms that its exact centered prime-orbit trace does not solve Lane A's finite-A Schur nonresonance. Round 93 PASSes v13.761's trace/Riesz reduction and nonresonance obstruction.

## 1. Corrected parity feedback system [D]

From v13.745, reflection gives
\[
M_{0x}=M_{10}=0,
\]
and the affine-moment closure is
\[
(1+M_{00})I_{0,A}=M_{0e}C_A,
\]
\[
(1+M_{1x})I_{1,A}=M_{1e}C_A.
\]

Let
\[
R_A=\mathcal L_A^{-1},
\]
and retain v13.761's exact trace functionals
\[
\ell_{0,A}=\operatorname{ev}_0\circ K_A,\qquad
\ell_{1,A}=\operatorname{ev}_0\circ\partial_xK_A.
\]

Then
\[
M_{00}=\ell_{0,A}(R_A^{(+)}1),
\qquad
M_{1x}=\ell_{1,A}(R_A^{(-)}x).
\]

## 2. Each Schur denominator is an exact rank-one Fredholm determinant [D]

On the even response space define
\[
\mathcal F_{+,A}
:=
(R_A^{(+)}1)\otimes\ell_{0,A},
\]
i.e.
\[
\mathcal F_{+,A}f
=
R_A^{(+)}1\,\ell_{0,A}(f).
\]

For a rank-one operator \(u\otimes\ell\),
\[
\det_F(I+u\otimes\ell)=1+\ell(u).
\]
Therefore
\[
\boxed{
1+M_{00}
=
\det_F(I+\mathcal F_{+,A}).
}
\]

Similarly, on the odd response space,
\[
\mathcal F_{-,A}
:=
(R_A^{(-)}x)\otimes\ell_{1,A},
\]
and
\[
\boxed{
1+M_{1x}
=
\det_F(I+\mathcal F_{-,A}).
}
\]

Thus the two previously algebraic Schur factors are genuine finite-rank Fredholm determinants.

## 3. Product determinant [D]

On the parity direct sum \(X_A=X_{A,+}\oplus X_{A,-}\), define
\[
\mathcal F_A
=
\mathcal F_{+,A}\oplus\mathcal F_{-,A}.
\]

Then
\[
\boxed{
D_A
:=
(1+M_{00})(1+M_{1x})
=
\det_F(I+\mathcal F_A).
}
\]

Equivalently, before parity diagonalization,
\[
D_A
=
\det_{\mathbb C^2}
\begin{pmatrix}
1+M_{00}&M_{0x}\\
M_{10}&1+M_{1x}
\end{pmatrix},
\]
and the finite-rank determinant identity \(\det(I+UV)=\det(I+VU)\) identifies this with the corresponding rank-two response-space Fredholm determinant.

## 4. Exact zero-mode interpretation [D]

The even determinant vanishes iff
\[
I+\mathcal F_{+,A}
\]
has a nonzero kernel. Thus
\[
1+M_{00}=0
\]
iff there exists \(f_+\ne0\) such that
\[
f_+
+
R_A^{(+)}1\,\ell_{0,A}(f_+)=0.
\]

Multiplying by \(\mathcal L_A\),
\[
\boxed{
\mathcal L_A f_+
+
1\,\ell_{0,A}(f_+)=0.
}
\]

Likewise,
\[
1+M_{1x}=0
\]
iff there exists \(f_-\ne0\) satisfying
\[
\boxed{
\mathcal L_A f_-
+
x\,\ell_{1,A}(f_-)=0.
}
\]

Therefore the two dangerous scalar resonances are exactly zero modes of two parity-resolved rank-one feedback perturbations of the corrected finite integral operator.

## 5. Compare with Suzuki's genuine boundary-extension determinant [D/N]

v13.661 proves the exact finite Suzuki boundary determinant
\[
\Delta^{\rm bdry}_{A,\theta/\pi}(z;z_*)
=
\frac{\tau_\theta-m_A(z)}
{\tau_\theta-m_A(z_*)},
\qquad
\tau_\theta=\tan(\theta/2).
\]

This determinant compares two domains/extensions of the fixed deficiency-\((1,1)\) symmetric operator. Its rank-one resolvent correction is
\[
\gamma_A(z)[\tau_\theta-m_A(z)]^{-1}\gamma_A(\bar z)^*.
\]

By contrast, the new feedback determinants are
\[
\det_F\!\left[I+
(R_A^{(+)}1)\otimes\ell_{0,A}\right],
\]
\[
\det_F\!\left[I+
(R_A^{(-)}x)\otimes\ell_{1,A}\right],
\]
which perturb the corrected Section-8 response equation itself by source/trace feedback.

No established unitary, form, or boundary-triple intertwiner identifies
\[
\mathcal L_A+1\otimes\ell_{0,A}
\]
or
\[
\mathcal L_A+x\otimes\ell_{1,A}
\]
with a Suzuki extension
\[
H_{A,\theta}:\quad \Gamma_1=\tau_\theta\Gamma_0.
\]

Therefore:
\[
\boxed{
\text{rank-one feedback determinant}
\neq_{\rm established}
\text{rank-one boundary-extension determinant}.
}
\]

The shared rank-one algebra is not enough to identify the determinant categories.

## 6. Why Hermite–Biehler nonvanishing does not transfer [N]

v13.673 gives the finite HB function
\[
E_A^{HB}=W_\pi-c_\infty W_0,
\]
with Schur function
\[
S_A(z)=
\frac{1+i c_\infty m_A(z)}
{1-i c_\infty m_A(z)},
\qquad |S_A(z)|<1
\quad(z\in\mathbb C_+).
\]

Hence
\[
\boxed{
1-i c_\infty m_A(z)\ne0
\qquad(z\in\mathbb C_+).
}
\]

More generally, for real \(\tau\),
\[
|\tau-m_A(z)|\ge\Im m_A(z)>0.
\]

But these estimates apply to the genuine boundary-extension denominators. Without an identity
\[
1+M_{00}
=
C_{+,A}(z)[\tau_+-m_A(z)]
\]
or
\[
1+M_{1x}
=
C_{-,A}(z)[\tau_--m_A(z)]
\]
with known nonzero factors, HB/Nevanlinna theory cannot be transferred to the feedback determinants.

No such identity follows from v13.661, v13.673, or the corrected Section-8 equation.

## 7. Structural mismatch sharpened [N]

There are two independent parity feedback determinants:
\[
D_{+,A}=1+M_{00},
\qquad
D_{-,A}=1+M_{1x}.
\]

Suzuki's finite symmetric operator has scalar deficiency indices \((1,1)\), hence one scalar Weyl function \(m_A(z)\) and one scalar boundary parameter at a fixed spectral point.

This does not logically forbid some special relation, but it means that identifying both parity feedback factors with independent Suzuki boundary-extension denominators requires additional structure not present in the established scalar boundary triple.

Accordingly, the correct next question is not "are both rank one?" but "is there an explicit intertwiner/domain identity taking either feedback zero-mode equation to \(\Gamma_1=\tau\Gamma_0\)?" At present the answer is: none established.

## 8. Lane-B cross-lane relevance [X]

v13.763/764 establishes exactly
\[
\left\langle\mathscr W_{S,\rm fin},\phi\right\rangle
=
-\operatorname{Tr}\!\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right].
\]

Together with v13.746, this decomposes the full-line bulk current into:
\[
\boxed{
\text{archimedean/origin package}
-
\text{centered prime-orbit trace}.
}
\]

This gives an exact operator carrier for the finite-prime part of the bulk entering Lane A's screw/Weil picture.

However the feedback corrections
\[
1\otimes\ell_{0,A},
\qquad
x\otimes\ell_{1,A}
\]
remain finite-A basepoint/domain data. Thus the cross-lane architecture is:
\[
\boxed{
\underbrace{\text{archimedean/origin current}
-\text{prime-orbit trace}}_{\text{bulk}}
+
\underbrace{\text{parity rank-one basepoint feedback}}_{\text{boundary}}.
}
\]

The Lane-B result strengthens the bulk side but does not alter the boundary determinant obstruction.

## 9. Strongest nonresonance statement presently available [D/C]

Unconditionally:
\[
\boxed{
1+M_{00}
=
\det_F(I+\mathcal F_{+,A}),
\qquad
1+M_{1x}
=
\det_F(I+\mathcal F_{-,A}).
}
\]

Hence nonresonance is exactly equivalent to invertibility of the two feedback operators:
\[
\boxed{
1+M_{00}\ne0
\iff
I+\mathcal F_{+,A}\text{ invertible},
}
\]
\[
\boxed{
1+M_{1x}\ne0
\iff
I+\mathcal F_{-,A}\text{ invertible}.
}
\]

The v13.761 norm criterion remains sufficient:
\[
\|\mathcal F_{+,A}\|<1,
\qquad
\|\mathcal F_{-,A}\|<1.
\]

Conditionally, if an explicit boundary-triple intertwiner is later proved so that either determinant equals a nonzero scalar multiple of \(\tau-m_A(z)\) at \(z\in\mathbb C_+\), then Nevanlinna/HB theory immediately gives nonvanishing and the quantitative lower bound
\[
|\tau-m_A(z)|\ge\Im m_A(z).
\]

No unconditional HB proof of feedback nonresonance is currently justified.

## 10. Consequence for the edge/HB convergence program [D]

The corrected deficiency ratios remain
\[
r_{0,A}=\frac{M_{0e}}{D_{+,A}},
\qquad
r_{1,A}=\frac{M_{1e}}{D_{-,A}}.
\]

Thus the finite-to-edge and finite-to-HB gates depend on:
1. numerator response bounds;
2. invertibility/lower bounds for the two explicit feedback Fredholm determinants.

The determinant realization is valuable because analytic Fredholm methods can now be applied if an auxiliary parameter is introduced, but the value at the physical parameter still requires a zero-exclusion argument.

## 11. Next Lane-A gates

1. Introduce a coupling parameter \(t\):
\[
D_{+,A}(t)=\det_F(I+t\mathcal F_{+,A})=1+tM_{00},
\]
\[
D_{-,A}(t)=\det_F(I+t\mathcal F_{-,A})=1+tM_{1x}.
\]
Determine whether positivity/monotonicity along \(0\le t\le1\) can exclude a zero at \(t=1\).

2. Derive the kernels
\[
k(0,y),\qquad k_x(0,y)
\]
from Suzuki's explicit finite kernel and estimate their signs/norms separately on the parity channels.

3. Preserve the Lane-B bulk trace as an exact decomposition tool, but do not use it to infer the finite-A boundary sign.

## Result

The characteristic/Hermite–Biehler route has been pursued to its exact stopping point.

The corrected Suzuki feedback denominators are genuine Fredholm determinants:
\[
\boxed{
1+M_{00}
=
\det_F\!\left[I+
(R_A^{(+)}1)\otimes\ell_{0,A}\right],
}
\]
\[
\boxed{
1+M_{1x}
=
\det_F\!\left[I+
(R_A^{(-)}x)\otimes\ell_{1,A}\right].
}
\]

Their zeros are exactly parity-resolved feedback zero modes.

But they are not presently identified with Suzuki's boundary-extension/HB determinants, so the strict HB nonvanishing theorem cannot be transferred.

The next viable nonresonance route is therefore sign/monotonicity of these explicit rank-one feedback determinants, not further formal characteristic matching.
