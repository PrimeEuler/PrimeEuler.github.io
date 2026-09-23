# Cone Derivation Ledger v13.710 — Logarithmic Derivatives and the Two-Coordinate Independence Gate

Date: 2026-09-23

Status: exact local differential comparison following v13.709. The goal is to compare the canonical scale coordinate
\[
\tau_A^{Fred}(z)=\log\det_2(I-zS_A)
\]
with the canonical boundary/boost coordinate
\[
\ell_A^{Cayley}(z)=\log s_A(z),
\qquad
s_A(z)=\frac{m_A(z)-i}{m_A(z)+i},
\]
and determine what independence is actually proved.

## 0. Synchronization

Immediately before this write the live head was v13.709, commit \`52407b0877064edcd5ac7d50d69e6b6b049290b8\`. No v13.710 collision was present.

## 1. Fredholm scale logarithmic derivative

Let
\[
D_A(z)=\det_2(I-zS_A),
\qquad
\tau_A(z)=\log D_A(z).
\]

For \(z\) off the reciprocal nonzero spectrum of \(S_A\), the regularized determinant derivative is
\[
\boxed{
\tau_A'(z)
=
-\operatorname{Tr}\!\left[(I-zS_A)^{-1}S_A-S_A\right].
}
\]

Using
\[
(I-zS_A)^{-1}-I
=
z(I-zS_A)^{-1}S_A,
\]
this becomes
\[
\boxed{
\tau_A'(z)
=
-z\,\operatorname{Tr}\!\left[(I-zS_A)^{-1}S_A^2\right].
}
\]

This trace is well-defined because
\[
S_A^2\in\mathfrak S_1.
\]

Equivalently, if \(\{\mu_n\}\) are the eigenvalues of \(S_A\),
\[
\boxed{
\tau_A'(z)
=
-\sum_n\left(
\frac{\mu_n}{1-z\mu_n}-\mu_n
\right)
=
-z\sum_n\frac{\mu_n^2}{1-z\mu_n}.
}
\]

Near \(z=0\),
\[
\boxed{
\tau_A'(z)
=
-\sum_{m=2}^{\infty}
z^{m-1}\operatorname{Tr}(S_A^m).
}
\]

In particular,
\[
\boxed{
\tau_A'(0)=0,\qquad
\tau_A''(0)=-\operatorname{Tr}(S_A^2)=-\|S_A\|_{\mathfrak S_2}^2
}
\]
for self-adjoint \(S_A\).

Thus the scale derivative begins at second spectral moment.

## 2. Cayley/boost logarithmic derivative

For
\[
s_A(z)=\frac{m_A(z)-i}{m_A(z)+i},
\]
define
\[
\ell_A(z)=\log s_A(z).
\]

Direct differentiation gives
\[
\ell_A'
=
\frac{m_A'}{m_A-i}
-
\frac{m_A'}{m_A+i}.
\]

Hence
\[
\boxed{
\ell_A'(z)
=
\frac{2i\,m_A'(z)}
{m_A(z)^2+1}.
}
\]

This depends on the scalar Weyl function and its first derivative.

For an ordinary boundary triple,
\[
m_A'(z)
=
\gamma(\bar z)^*\gamma(z)
\]
in the standard scalar analytic convention (with the usual holomorphic continuation interpretation off the real axis). Thus
\[
\boxed{
\ell_A'(z)
=
\frac{2i\,\gamma(\bar z)^*\gamma(z)}
{m_A(z)^2+1}.
}
\]

So the boost derivative is rank-one boundary/defect data, whereas the Fredholm derivative is a full spectral trace.

## 3. Character separation of the derivatives

From v13.709:
\[
\tau_A:\quad
\Re\tau_A=(+,+),\qquad
\Im\tau_A=(+,-).
\]

From v13.706:
\[
\ell_A:\quad
\Re\ell_A=(-,+),\qquad
\Im\ell_A=(-,-).
\]

Differentiation with respect to the spectral variable does not alter deficiency-reflection parity. Therefore:
\[
\boxed{
\tau_A'\text{ is }F\text{-even},
\qquad
\ell_A'\text{ is }F\text{-odd}
}
\]
in the induced character action.

This immediately forbids any nonzero **F-equivariant scalar linear relation**
\[
a(z)\tau_A'(z)+b(z)\ell_A'(z)=0
\]
with \(F\)-even scalar coefficients \(a,b\), unless both character components vanish separately.

Thus the two derivatives occupy inequivalent \(C_2^2\) isotypic sectors.

## 4. No equivariant recovery of one coordinate from the other

Suppose there were a local holomorphic recovery
\[
\tau_A=H(\ell_A)
\]
compatible with deficiency reflection.

Because
\[
F:\tau_A\mapsto\tau_A,
\qquad
F:\ell_A\mapsto-\ell_A,
\]
equivariance forces
\[
\boxed{
H(-u)=H(u).
}
\]

Thus \(H\) must be even.

Conversely, if
\[
\ell_A=K(\tau_A),
\]
then \(F\)-equivariance would require
\[
K(u)=-K(u),
\]
so
\[
\boxed{K\equiv0.}
\]

Therefore a nontrivial F-odd boost coordinate cannot be recovered equivariantly from the F-even scale coordinate alone.

The reverse direction is not excluded algebraically: an F-even quantity can be an even function of an F-odd quantity. Hence character theory alone proves one-way nonrecoverability but not full functional independence.

## 5. Local differential independence criterion

A genuine local two-coordinate map requires a two-parameter deformation. Let \(p,q\) be independent deformation parameters of the operator/boundary data and consider
\[
\Phi(p,q)
=
(\tau_A(p,q),\ell_A(p,q)).
\]

Local independence is equivalent to
\[
\boxed{
J=
\det
\begin{pmatrix}
\partial_p\tau_A&\partial_q\tau_A\\
\partial_p\ell_A&\partial_q\ell_A
\end{pmatrix}
\ne0.
}
\]

A single spectral parameter \(z\) cannot prove two-dimensional functional independence: both \(\tau_A(z)\) and \(\ell_A(z)\) are functions on the same one-complex-dimensional spectral curve.

Therefore the phrase “two-coordinate operator torus” must be interpreted as a symmetry/character decomposition unless a second independent deformation is supplied.

This is an important dimensional guardrail.

## 6. Natural independent deformations

The project already supplies conceptually distinct deformation directions:

1. **bulk/kernel deformation:** vary the continuous kernel \(S_A\) (for example \(A\), arithmetic kernel data, or an admissible bulk coupling) while holding the boundary triple fixed;

2. **boundary extension deformation:** vary \(\theta\) or deficiency-channel coordinate while holding \(S_A\) fixed.

At fixed \(S_A\),
\[
\boxed{\partial_\theta\tau_A=0}
\]
because the Fredholm determinant depends only on \(S_A\).

The boundary factor
\[
b_\theta=1-e^{i\theta}s_A
\]
satisfies
\[
\boxed{
\partial_\theta\log b_\theta
=
-\frac{i e^{i\theta}s_A}
{1-e^{i\theta}s_A},
}
\]
which is generically nonzero.

Thus bulk Fredholm scale and extension phase are demonstrably independent under the \(\theta\)-deformation.

However \(\ell_A=\log s_A\) itself is a property of the boundary triple/Weyl function and does not depend on the extension parameter \(\theta\). Therefore \(\theta\) proves independence of the scale coordinate from the **extension phase**, but not by itself a nonzero Jacobian for \((\tau_A,\ell_A)\).

## 7. Rank-one boundary versus full trace obstruction

The formulas
\[
\boxed{
\tau_A'
=
-z\,\operatorname{Tr}[(I-zS_A)^{-1}S_A^2]
}
\]
and
\[
\boxed{
\ell_A'
=
\frac{2i\,m_A'}{m_A^2+1}
}
\]
show qualitatively different information content:

- \(\tau_A'\) samples all nonzero eigenvalues of the compact continuous-kernel operator through a regularized resolvent trace;
- \(\ell_A'\) samples the scalar Weyl function, equivalently a rank-one defect channel.

No identity in the current Suzuki/Kreĭn framework determines the full regularized trace from the single scalar Weyl function, or vice versa.

But absence of such an identity is not itself a theorem of functional independence. A cyclic rank-one Weyl function can, in suitable settings, encode a full operator spectral measure. Therefore:
\[
\boxed{
\text{full functional independence remains OPEN without a two-parameter Jacobian or an explicit obstruction theorem.}
}
\]

## 8. Strongest proved independence statement

The following is exact:

\[
\boxed{
\text{the Fredholm scale coordinate and Cayley boost coordinate lie in distinct }F\text{-character sectors.}
}
\]

\[
\boxed{
\ell_A\text{ cannot be recovered as a nonzero }F\text{-equivariant function of }\tau_A\text{ alone.}
}
\]

\[
\boxed{
\tau_A\text{ could only be recovered equivariantly from }\ell_A\text{ through an even function.}
}
\]

\[
\boxed{
\text{there is no proved even-function identity }\tau_A=H(\ell_A).
}
\]

Thus the proposed two-coordinate bridge passes the **equivariant independence** gate but not yet the stronger **functional independence** gate.

## 9. Relation to cone torus

For the cone,
\[
(\tau,\ell)\in\mathbb C^2
\]
are genuinely independent logarithmic coordinates because
\[
\log x=\tau+\ell,\qquad
\log y=\tau-\ell
\]
and \(x,y\) can vary independently.

For Suzuki, the canonical representatives
\[
\tau_A^{Fred}(z),\qquad
\ell_A^{Cayley}(z)
\]
have the same four-character decomposition, but along fixed operator data and varying \(z\) they trace only a one-complex-dimensional curve in the candidate \((\tau,\ell)\)-plane.

Therefore:
\[
\boxed{
\text{character-level }(\mathbb C^\times)^2\text{ structure: PROVED;}
}
\]
\[
\boxed{
\text{two-dimensional operator moduli/torus: NOT YET PROVED.}
}
\]

## 10. Result

\[
\boxed{
\frac{d}{dz}\log\det_2(I-zS_A)
=
-z\,\operatorname{Tr}[(I-zS_A)^{-1}S_A^2].
}
\]

\[
\boxed{
\frac{d}{dz}\log s_A(z)
=
\frac{2i\,m_A'(z)}{m_A(z)^2+1}.
}
\]

The first is a regularized full resolvent trace; the second is scalar Weyl/defect data.

\[
\boxed{
\textbf{PASS: equivariant independence.}
}
\]

\[
\boxed{
\textbf{OPEN: full functional independence / nonzero two-parameter Jacobian.}
}
\]

## 11. Next gate

The cleanest decisive test is to introduce a genuine bulk coupling \(\varepsilon\):
\[
S_A(\varepsilon)=S_A+\varepsilon V
\]
with \(V\) real, reflection-even, Hilbert--Schmidt, while keeping the boundary normalization fixed.

Then compute
\[
\partial_\varepsilon\tau_A^{Fred},
\qquad
\partial_\varepsilon\ell_A^{Cayley},
\]
and combine with a boundary deformation that is reflection-odd or changes the Weyl coordinate.

If one can choose two admissible deformations for which the \(2\times2\) Jacobian is nonzero, the operator-side two-coordinate structure becomes locally genuine rather than only representation-theoretic.
