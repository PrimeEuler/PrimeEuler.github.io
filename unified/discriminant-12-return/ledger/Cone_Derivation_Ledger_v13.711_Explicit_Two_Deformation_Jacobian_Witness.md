# Cone Derivation Ledger v13.711 — Explicit Two-Deformation Jacobian Witness

Date: 2026-09-23

Status: exact local deformation theorem following v13.710. This entry constructs one explicit admissible bulk deformation and one independent boundary-coordinate deformation, computes all four first derivatives of the canonical Fredholm/Cayley logarithms, and gives a nonzero Jacobian criterion with an explicit rank-one witness.

## 0. Synchronization

Immediately before this write the live head was v13.710, commit \`5a54ef2f82fe0895d3f439b33bbb8437a03beba1\`. No v13.711 collision was present.

Fix a nonreal spectral point \(z_0\) such that
\[
I-z_0S_A
\]
is invertible and
\[
m_A(z_0)\ne\pm i.
\]

Write
\[
\tau(z_0)=\log\det_2(I-z_0S_A),
\qquad
\ell(z_0)=\log\frac{m_A(z_0)-i}{m_A(z_0)+i}.
\]

We now introduce two independent real deformation parameters \((\varepsilon,\eta)\).

## 1. Bulk deformation

Choose a real reflection-even vector
\[
f\in L_0^2(-A,A),
\qquad
Rf=f,
\qquad
\|f\|=1,
\]
and define the rank-one self-adjoint operator
\[
\boxed{
V_f=|f\rangle\langle f|.
}
\]

Its kernel is
\[
v_f(x,y)=f(x)f(y),
\]
which is real, continuous if \(f\) is chosen continuous, reflection-even,
\[
v_f(-x,-y)=v_f(x,y),
\]
and trace class (hence Hilbert--Schmidt).

Define
\[
\boxed{
S_A(\varepsilon)=S_A+\varepsilon V_f.
}
\]

This preserves the real/reflection-even Section-8 operator class.

For this deformation we hold the chosen boundary triple/Weyl normalization fixed:
\[
\boxed{
m_{A,\varepsilon,\eta}(z)
\text{ has no }\varepsilon\text{-variation in this product deformation model.}
}
\]

This is an explicit local product deformation of the two operator coordinates, not a claim that perturbing Suzuki's arithmetic kernel physically leaves its Weyl function unchanged. The purpose is to test whether the two canonical coordinate sectors admit independent local directions in the enlarged admissible operator/boundary-data space.

## 2. Boundary/Weyl deformation

Use an admissible scalar boundary-coordinate translation
\[
\boxed{
m_\eta(z)=m_A(z)+\eta,
\qquad \eta\in\mathbb R.
}
\]

This is induced by the ordinary boundary-triple change
\[
\Gamma_0^\eta=\Gamma_0,
\qquad
\Gamma_1^\eta=\Gamma_1+\eta\Gamma_0,
\]
up to the sign convention for the Weyl function. It preserves the scalar Nevanlinna property for real \(\eta\).

It does not alter \(S_A\):
\[
\boxed{
\partial_\eta S_A=0.
}
\]

Thus \(\eta\) is a pure Weyl/boundary-coordinate deformation.

Define
\[
\boxed{
s_\eta(z)=
\frac{m_A(z)+\eta-i}
{m_A(z)+\eta+i},
\qquad
\ell_\eta(z)=\log s_\eta(z).
}
\]

## 3. First derivative: bulk response of Fredholm scale

Let
\[
\tau_{\varepsilon}(z_0)
=
\log\det_2(I-z_0(S_A+\varepsilon V_f)).
\]

For a differentiable Hilbert--Schmidt family \(S(\varepsilon)\),
\[
\partial_\varepsilon\log\det_2(I-zS)
=
-z\operatorname{Tr}\!\left[(I-zS)^{-1}S'-S'\right].
\]

At \(\varepsilon=0\), \(S'=V_f\), hence
\[
\boxed{
\partial_\varepsilon\tau\big|_0
=
-z_0\operatorname{Tr}
\left[
\bigl((I-z_0S_A)^{-1}-I\bigr)V_f
\right].
}
\]

For rank-one \(V_f\),
\[
\operatorname{Tr}(BV_f)=\langle f,Bf\rangle.
\]

Therefore
\[
\boxed{
\partial_\varepsilon\tau\big|_0
=
-z_0
\left\langle
f,\left[(I-z_0S_A)^{-1}-I\right]f
\right\rangle.
}
\]

Using
\[
(I-z_0S_A)^{-1}-I
=
z_0(I-z_0S_A)^{-1}S_A,
\]
also
\[
\boxed{
\partial_\varepsilon\tau\big|_0
=
-z_0^2
\langle f,(I-z_0S_A)^{-1}S_Af\rangle.
}
\]

## 4. Second derivative entry: boundary response of Fredholm scale

Since \(S_A\) is independent of \(\eta\),
\[
\boxed{
\partial_\eta\tau\big|_0=0.
}
\]

This is exact.

## 5. Third derivative entry: bulk response of Cayley boost

By construction of the product deformation, the Weyl datum is held fixed along \(\varepsilon\):
\[
\partial_\varepsilon m=0.
\]

Therefore
\[
\boxed{
\partial_\varepsilon\ell\big|_0=0.
}
\]

Again, this is exact for the explicitly defined product deformation.

## 6. Fourth derivative entry: boundary response of Cayley boost

For
\[
\ell_\eta
=
\log(m+\eta-i)-\log(m+\eta+i),
\]
differentiate:
\[
\partial_\eta\ell_\eta
=
\frac1{m+\eta-i}
-
\frac1{m+\eta+i}.
\]

At \(\eta=0\),
\[
\boxed{
\partial_\eta\ell\big|_0
=
\frac{2i}{m_A(z_0)^2+1}.
}
\]

Because \(m_A(z_0)\ne\pm i\), this is nonzero.

## 7. The four first derivatives

At \((\varepsilon,\eta)=(0,0)\):
\[
\boxed{
\begin{aligned}
\partial_\varepsilon\tau
&=
-z_0
\langle f,[(I-z_0S_A)^{-1}-I]f\rangle,\\[1mm]
\partial_\eta\tau
&=0,\\[1mm]
\partial_\varepsilon\ell
&=0,\\[1mm]
\partial_\eta\ell
&=
\frac{2i}{m_A(z_0)^2+1}.
\end{aligned}
}
\]

Hence the Jacobian is diagonal:
\[
\boxed{
J_f(z_0)
=
\det
\begin{pmatrix}
\partial_\varepsilon\tau&\partial_\eta\tau\\
\partial_\varepsilon\ell&\partial_\eta\ell
\end{pmatrix}
=
-z_0
\langle f,[(I-z_0S_A)^{-1}-I]f\rangle
\frac{2i}{m_A(z_0)^2+1}.
}
\]

Equivalently,
\[
\boxed{
J_f(z_0)
=
-\frac{2iz_0^2}
{m_A(z_0)^2+1}
\langle f,(I-z_0S_A)^{-1}S_Af\rangle.
}
\]

## 8. Explicit nonzero witness

Suppose the even reflection sector of \(S_A\) contains a nonzero eigenvalue
\[
S_Af=\mu f,
\qquad
Rf=f,
\qquad
\mu\ne0,
\qquad
\|f\|=1.
\]

Then
\[
(I-z_0S_A)^{-1}f
=
\frac1{1-z_0\mu}f.
\]

Therefore
\[
\partial_\varepsilon\tau
=
-z_0
\left(
\frac1{1-z_0\mu}-1
\right)
=
\boxed{
-\frac{z_0^2\mu}{1-z_0\mu}.
}
\]

The Jacobian becomes
\[
\boxed{
J_f(z_0)
=
-\frac{2iz_0^2\mu}
{(1-z_0\mu)(m_A(z_0)^2+1)}.
}
\]

Thus if
\[
z_0\ne0,\qquad
\mu\ne0,\qquad
1-z_0\mu\ne0,\qquad
m_A(z_0)\ne\pm i,
\]
then
\[
\boxed{J_f(z_0)\ne0.}
\]

This is an explicit local two-coordinate witness.

## 9. Existence caveat for the even eigenvalue

Because \(S_A\) commutes with reflection,
\[
L_0^2=L_{\rm even}\oplus L_{\rm odd}
\]
reduces \(S_A\).

If the even block is nonzero, compact self-adjointness gives a nonzero even eigenvalue and the witness above applies directly.

If the even block vanished identically but the odd block did not, one could choose an odd \(f\); the rank-one kernel
\[
f(x)f(y)
\]
is still simultaneously reflection-even:
\[
f(-x)f(-y)=f(x)f(y).
\]

Therefore any nonzero spectral block of \(S_A\) supplies a rank-one reflection-compatible eigenvector witness.

For \(S_A\ne0\), choose any normalized eigenvector \(f\) with nonzero eigenvalue. Since \(S_A\) commutes with \(R\), it may be chosen with definite parity. Then \(V_f=|f\rangle\langle f|\) commutes with \(R\).

Hence:
\[
\boxed{
S_A\ne0
\Longrightarrow
\text{an admissible rank-one witness exists.}
}
\]

## 10. Character interpretation

The bulk parameter \(\varepsilon\) changes only the F-even Fredholm scale coordinate in the product model:
\[
\partial_\varepsilon\tau\ne0,\qquad
\partial_\varepsilon\ell=0.
\]

The boundary-coordinate parameter \(\eta\) changes only the Cayley coordinate:
\[
\partial_\eta\tau=0,\qquad
\partial_\eta\ell\ne0.
\]

Therefore the tangent vectors are linearly independent:
\[
\boxed{
\partial_\varepsilon(\tau,\ell)
=
(\partial_\varepsilon\tau,0),
\qquad
\partial_\eta(\tau,\ell)
=
(0,\partial_\eta\ell).
}
\]

At a nonzero witness point:
\[
\boxed{
\operatorname{rank}d(\tau,\ell)=2.
}
\]

This upgrades the previous character-only separation to a genuine local two-complex-coordinate structure **on the product space of continuous-kernel operators and admissible boundary-coordinate data**.

## 11. Critical guardrail: product moduli versus physical Suzuki family

The deformation
\[
S_A\mapsto S_A+\varepsilon V_f
\]
while holding \(m_A\) fixed is an admissible deformation of the product data
\[
(S_A,\text{boundary triple/Weyl coordinate}),
\]
but it is not asserted to arise from Suzuki's one-parameter physical finite-\(A\) arithmetic family.

In the actual Suzuki construction, changing the kernel generally changes the induced Weyl function as well.

Therefore the exact theorem is:
\[
\boxed{
\text{the enlarged admissible operator/boundary-data space has local rank two.}
}
\]

It is **not yet**:
\[
\boxed{
\text{the physical Suzuki arithmetic family itself is two-dimensional.}
}
\]

That stronger statement would require differentiating the Weyl function induced by a genuine kernel perturbation.

## 12. Result

Explicit admissible pair:
\[
\boxed{
S_A(\varepsilon)=S_A+\varepsilon|f\rangle\langle f|,
\qquad
m_\eta=m_A+\eta.
}
\]

Four derivatives:
\[
\boxed{
\partial_\varepsilon\tau
=
-z_0\langle f,[(I-z_0S_A)^{-1}-I]f\rangle,
}
\]
\[
\boxed{\partial_\eta\tau=0,}
\]
\[
\boxed{\partial_\varepsilon\ell=0,}
\]
\[
\boxed{
\partial_\eta\ell
=
\frac{2i}{m_A(z_0)^2+1}.
}
\]

For an eigenvector \(S_Af=\mu f\):
\[
\boxed{
J_f(z_0)
=
-\frac{2iz_0^2\mu}
{(1-z_0\mu)(m_A(z_0)^2+1)}
\ne0
}
\]
under the stated nondegeneracy conditions.

Therefore:
\[
\boxed{
\textbf{PASS: local two-coordinate independence on the admissible product moduli space.}
}
\]

## 13. Next gate

The next stronger test should replace the artificial product deformation by a genuine kernel perturbation
\[
g_A\mapsto g_A+\varepsilon h
\]
inside Suzuki's continuous-kernel construction, derive the induced first variation
\[
\delta m_A(z)
\]
from the defect equation, and recompute the Jacobian.

If the determinant remains nonzero after allowing the physically induced cross-term
\[
\partial_\varepsilon\ell\ne0,
\]
then the local two-coordinate result will survive inside a coupled Suzuki-type operator family rather than only on the product moduli space.
