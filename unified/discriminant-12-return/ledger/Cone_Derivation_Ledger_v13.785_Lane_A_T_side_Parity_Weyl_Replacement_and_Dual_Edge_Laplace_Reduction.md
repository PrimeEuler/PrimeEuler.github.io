# Cone Derivation Ledger v13.785 — Lane A T-side Parity/Weyl Replacement and Dual Edge-Laplace Reduction of the Affine Ratios

Date: 2026-09-25

Lane: A.

Status: [D] exact source-level parity reduction using \(T_a^{-1}\); [D] exact finite Weyl Möbius formula without ordinary-\(\bar D\) assumptions; [D] exact dual-resolvent representation of \(r_{0,a},r_{1,a}\); [D] exact right-edge Laplace reduction; [G] supersedes the operator realization used in v13.777 while retaining its Möbius algebra.

Parents: v13.675, v13.777, v13.782–784.

## 0. Synchronization

Immediately before this write the live ledger head is v13.784. No collision is present.

This entry continues after the v13.784 source correction. All constructions are performed first on the rigorous source-level operator
\[
T_a=A_a-\lambda I,
\]
avoiding any identification of \(\bar D\) with an ordinary endpoint derivative.

## 1. Exact reflection-compatible deficiency pair [D]

Suzuki Section 6 gives
\[
T_av_{+i}=e^x,\qquad T_av_{-i}=e^{-x},
\]
for the canonical resolvent vectors with unit source normalization.

Since \(T_a\) commutes with reflection \(R\),
\[
v_{-i}=Rv_{+i}.
\]

Choose the deficiency basis with a common reflection-compatible scalar \(C_a\):
\[
v_+=C_av_{+i},\qquad
v_-=C_av_{-i}=Rv_+.
\]

Define
\[
w_e:=\frac{v_{+i}+v_{-i}}{2},
\qquad
w_o:=\frac{v_{+i}-v_{-i}}{2}.
\]
Then
\[
\boxed{
w_e=(T_a^{(+)})^{-1}\cosh x,
}
\tag{1E}
\]
\[
\boxed{
w_o=(T_a^{(-)})^{-1}\sinh x.
}
\tag{1O}
\]

Thus
\[
v_+=C_a(w_e+w_o),
\qquad
v_-=C_a(w_e-w_o).
\]

## 2. T-side parity transforms [D]

Using Suzuki's Fourier convention
\[
\widehat f(z)=\int_{-a}^{a}f(x)e^{izx}\,dx,
\]
define
\[
\boxed{
E_a(z):=\widehat{w_e}(z),
\qquad
O_a(z):=\widehat{w_o}(z).
}
\tag{2}
\]

Because \(w_e\) is even and \(w_o\) odd,
\[
\boxed{
E_a(-z)=E_a(z),
\qquad
O_a(-z)=-O_a(z).
}
\tag{3}
\]

Since \(T_a\) is real and the sources \(\cosh,\sinh\) are real, \(w_e,w_o\) may be chosen real. Hence on the real axis,
\[
E_a(x)\in\mathbb R,
\qquad
O_a(x)\in i\mathbb R.
\]

The deficiency transforms are simply
\[
\widehat v_+=C_a(E_a+O_a),
\qquad
\widehat v_-=C_a(E_a-O_a).
\]

## 3. Exact finite characteristic and Weyl formula [D]

Suzuki's finite characteristic is
\[
W(a,\theta;z)
=
(z-i)\widehat v_+(z)
+
e^{i\theta}(z+i)\widehat v_-(z).
\]

Therefore
\[
\boxed{
W_0(a;z)=2C_a\,[zE_a(z)-iO_a(z)],
}
\tag{4}
\]
\[
\boxed{
W_\pi(a;z)=2C_a\,[-iE_a(z)+zO_a(z)].
}
\tag{5}
\]

Using the audited boundary-triple convention
\[
\frac{W_0}{W_\pi}=i\,m_a,
\]
we obtain
\[
\boxed{
m_a(z)
=
-i\,
\frac{zE_a(z)-iO_a(z)}
{-iE_a(z)+zO_a(z)}.
}
\tag{6}
\]

Where \(E_a\neq0\), set
\[
\eta_a(z):=\frac{O_a(z)}{E_a(z)}.
\]
Then
\[
\boxed{
m_a(z)
=
-i\frac{z-i\eta_a(z)}{-i+z\eta_a(z)}.
}
\tag{7}
\]

This recovers the Möbius algebra of v13.777, but now its response functions are the rigorous \(T_a^{-1}\) parity responses (1E)–(1O), not ordinary-function images of \(\bar D\).

## 4. Immediate parity consistency checks [D]

From (3),
\[
\boxed{\eta_a(-z)=-\eta_a(z)}
\]
where defined.

For real \(x\), \(\eta_a(x)\in i\mathbb R\). Substitution into (7) gives the expected real boundary values of the finite Weyl function wherever the reference denominator is nonzero.

If \(E_a(0)\neq0\), then \(O_a(0)=0\) and
\[
m_a(0)=0.
\]

Moreover,
\[
O_a'(0)=i\int_{-a}^{a}x\,w_o(x)\,dx,
\qquad
E_a(0)=\int_{-a}^{a}w_e(x)\,dx.
\]
Differentiating (7) at zero gives the exact scalar diagnostic
\[
\boxed{
m_a'(0)
=
1+
\frac{\displaystyle\int_{-a}^{a}x\,w_o(x)\,dx}
{\displaystyle\int_{-a}^{a}w_e(x)\,dx},
}
\tag{8}
\]
provided the denominator is nonzero.

Thus even the local Weyl slope is a ratio of two source-level \(T_a^{-1}\) moments.

## 5. Dual-resolvent representation of the affine ratios [D]

Return to the raw first-kind kernel
\[
k_a(x,y)=g(x-y)-\lambda N_a(x,y).
\]

Define the exact trace representers
\[
\boxed{
q_{0,a}(y):=k_a(0,y),
\qquad
q_{1,a}(y):=\partial_xk_a(0,y).
}
\tag{9}
\]

Then \(q_{0,a}\) is even and \(q_{1,a}\) odd. The v13.782 affine ratios are
\[
r_{0,a}
=
\langle q_{0,a},w_e\rangle,
\qquad
r_{1,a}
=
\langle q_{1,a},w_o\rangle.
\]

By self-adjointness of \(T_a^{-1}\), define the **dual responses**
\[
\boxed{
\psi_{0,a}:=(T_a^{(+)})^{-1}q_{0,a},
\qquad
\psi_{1,a}:=(T_a^{(-)})^{-1}q_{1,a}.
}
\tag{10}
\]

Then
\[
r_{0,a}
=
\langle \psi_{0,a},\cosh\rangle,
\qquad
r_{1,a}
=
\langle \psi_{1,a},\sinh\rangle.
\tag{11}
\]

Parity eliminates the complementary exponential pieces:
\[
\int\psi_{0,a}\sinh=0,
\qquad
\int\psi_{1,a}\cosh=0.
\]

Hence both ratios have the unified one-sided Laplace form
\[
\boxed{
r_{0,a}
=
\int_{-a}^{a}e^x\psi_{0,a}(x)\,dx,
}
\tag{12}
\]
\[
\boxed{
r_{1,a}
=
\int_{-a}^{a}e^x\psi_{1,a}(x)\,dx.
}
\tag{13}
\]

## 6. Exact right-edge localization [D]

Introduce the inward edge coordinate
\[
x=a-\xi.
\]

Then (12)–(13) give
\[
\boxed{
e^{-a}r_{j,a}
=
\int_{0}^{2a}e^{-\xi}\,
\psi_{j,a}(a-\xi)\,d\xi,
\qquad j=0,1.
}
\tag{14}
\]

This is exact.

Therefore the primitive affine-edge problem is not controlled by the full \(L^2\)-norm of the exponentially growing sources \(\cosh,\sinh\). It is controlled by a **Laplace-weighted right-edge profile of the dual resolvent responses**.

Recall
\[
\alpha_a=-e^{-a}(1+r_{1,a}),
\]
\[
\beta_a
=
-e^{-a}\{a(1+r_{1,a})+1+r_{0,a}\}.
\]

Define
\[
L_{j,a}
:=
\int_{0}^{2a}e^{-\xi}\psi_{j,a}(a-\xi)\,d\xi
=
e^{-a}r_{j,a}.
\]

Then
\[
\boxed{
\alpha_a=-e^{-a}-L_{1,a},
}
\tag{15}
\]
\[
\boxed{
\beta_a
=
-(a+1)e^{-a}-aL_{1,a}-L_{0,a}.
}
\tag{16}
\]

Consequently the pure compensated edge limit follows if
\[
\boxed{
L_{0,a}\to0,
\qquad
aL_{1,a}\to0.
}
\tag{17}
\]

This is strictly sharper than the crude global resolvent estimate of v13.782's continuation.

## 7. Explicit trace representers [D]

Using
\[
N_a(0,y)
=
\frac{y^2}{4a}-\frac{|y|}{2}+\frac a6,
\]
we have
\[
\boxed{
q_{0,a}(y)
=
g(y)
-\lambda\left(
\frac{y^2}{4a}-\frac{|y|}{2}+\frac a6
\right).
}
\tag{18}
\]

For \(y\neq0\),
\[
\boxed{
q_{1,a}(y)
=
-g'(y)-\frac{\lambda}{2}\operatorname{sgn}(y).
}
\tag{19}
\]

Differentiating (18) gives the exact relation
\[
\boxed{
q_{1,a}(y)+q_{0,a}'(y)
=
-\frac{\lambda}{2a}y
}
\tag{20}
\]
away from the origin, with the natural distributional interpretation across \(y=0\).

Equation (20) may be useful for coupling the two dual edge responses, although \(T_a^{-1}\) does not commute with differentiation and no such coupling theorem is claimed here.

## 8. Spectral representation and the true quantitative bottleneck [D/N]

Let
\[
T_a^{(\pm)}\phi_{n,a}^{\pm}
=
\mu_{n,a}^{\pm}\phi_{n,a}^{\pm},
\qquad
\mu_{n,a}^{\pm}>0,
\]
with parity-adapted orthonormal bases.

Then
\[
\boxed{
r_{0,a}
=
\sum_n
\frac{
\langle q_{0,a},\phi_{n,a}^{+}\rangle
\langle\phi_{n,a}^{+},\cosh\rangle
}{
\mu_{n,a}^{+}
},
}
\tag{21}
\]
\[
\boxed{
r_{1,a}
=
\sum_n
\frac{
\langle q_{1,a},\phi_{n,a}^{-}\rangle
\langle\phi_{n,a}^{-},\sinh\rangle
}{
\mu_{n,a}^{-}
}.
}
\tag{22}
\]

A bound using only
\[
\|T_a^{-1}\|
\le(\lambda_a-\lambda)^{-1}
\]
and
\[
\|\cosh\|,\|\sinh\|\asymp e^a
\]
cannot prove (17). The decisive issue is cancellation/localization in the **matrix elements** or, equivalently, decay of the edge profiles \(\psi_{j,a}(a-\xi)\).

Thus the quantitative gate is now precisely:
\[
\boxed{
\int_0^{2a}e^{-\xi}\psi_{0,a}(a-\xi)\,d\xi\to0,
}
\]
\[
\boxed{
a\int_0^{2a}e^{-\xi}\psi_{1,a}(a-\xi)\,d\xi\to0.
}
\]

## 9. Dependency cleanup relative to v13.777 [G]

Retain from v13.777:

- the two-channel Möbius algebra;
- the reduction to one meromorphic ratio;
- the projective cancellation of the common deficiency normalization.

Supersede from v13.777:

- treating \(\bar D e_{\pm i}\) as ordinary scalar multiples of \(e^{\pm x}\);
- assigning ordinary-function parity directly to those transported sources;
- defining the parity responses through an \(L^2\)-style \(S_a^{(\pm)}\) inverse without specifying the energy-space realization.

The rigorous replacement is (1E)–(7) on the \(T_a\) side.

## Result

The finite Weyl problem and the primitive affine-edge problem now have two clean, source-faithful scalar reductions built from the same operator \(T_a^{-1}\):

\[
\boxed{
\eta_a(z)
=
\frac{
\widehat{(T_a^{(-)})^{-1}\sinh}(z)
}{
\widehat{(T_a^{(+)})^{-1}\cosh}(z)
}
\longrightarrow
m_a(z)\ \text{by (7)},
}
\]

and
\[
\boxed{
e^{-a}r_{j,a}
=
\int_0^{2a}e^{-\xi}\psi_{j,a}(a-\xi)\,d\xi,
\qquad
\psi_{j,a}=T_{a,\mathrm{parity}(j)}^{-1}q_{j,a}.
}
\]

The next analytic gate is therefore an **edge-local resolvent estimate**, not a global operator-norm estimate.
