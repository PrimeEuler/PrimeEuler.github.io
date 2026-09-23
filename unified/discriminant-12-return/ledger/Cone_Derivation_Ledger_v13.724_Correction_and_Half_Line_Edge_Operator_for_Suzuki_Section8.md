# Cone Derivation Ledger v13.724 — Correction and Half-Line Edge Operator for Suzuki Section 8

Date: 2026-09-23

Status: source-faithful correction to v13.721 plus exact edge-coordinate reduction at the \(L_0^2\) quadratic-form level. The actual deficiency-vector edge equation remains open because Suzuki's extended transport \(\bar D\) is not ordinary differentiation on the completed space.

## 0. Synchronization and audit relevance

Live head before this write is v13.723, External Audit Round 85, commit \`4e78c66a8470c33ada7ae5476e58615818541482\`. The audit verified v13.717--722 but did not resolve the domain issue below.

Suzuki Section 8 explicitly states
\[
H(S_A)\not\subset L^2(-A,A),
\]
and
\[
\bar D(1_{[-A,A]})\ne0.
\]
It also explicitly distinguishes
\[
S_Au_\pm=C_\pm\bar D e_{\pm i}
\]
from the formal twice-integrated first-kind equation (8.5).

This forces a correction to v13.721.

## 1. Correction: \(\bar D e_z=z e_z\) is not established

On the core \(C_c^\infty(-A,A)\),
\[
D=i\,d/dx.
\]
But Suzuki's \(\bar D\) is the continuous extension
\[
\bar D:H(T_A)\to H(S_A),
\]
and the exponential defect vectors are not core vectors with Dirichlet boundary values.

Therefore the step
\[
\bar D e_z=z e_z
\]
made in v13.721 is **not source-faithfully justified**.

Indeed Suzuki emphasizes that \(\bar D\) is not simply distributional differentiation on all of \(H(T_A)\), as witnessed by
\[
\bar D(1_{[-A,A]})\ne0.
\]

Hence the exact Section-8 defect equation remains
\[
\boxed{S_Au_z=\bar D e_z,}
\]
not \(S_Au_z=z e_z\).

Status correction:
\[
\boxed{\text{v13.721 Sections 1, 4--6 are conditional/model-level, not exact Suzuki identities.}}
\]

The mean-zero kernel algebra in v13.721 Section 2 remains valid as quadratic-form algebra.

## 2. Exact right-edge coordinate transform of the Neumann kernel

Set
\[
x=A-\xi,\qquad y=A-\eta,
\qquad 0\le\xi,\eta\le2A.
\]

Suzuki's Neumann inverse kernel is
\[
N_A(x,y)
=
\frac{x^2+y^2}{4A}
-\frac{|x-y|}{2}
+\frac A6.
\]

Substitution gives exactly
\[
\boxed{
N_A^{R}(\xi,\eta)
=
\frac{2A}{3}
-\max(\xi,\eta)
+\frac{\xi^2+\eta^2}{4A}.
}
\]

This expression itself has no pointwise finite \(A\to\infty\) limit because of \(2A/3\). That divergence is a gauge artifact of representing the inverse Neumann Laplacian before imposing the mean-zero quotient.

## 3. The quadratic-form equivalent Green kernel and its exact edge limit

Suzuki also derives the quadratic-form representative
\[
\widetilde K_A(x,y)=A-\max(x,y).
\]

For mean-zero inputs its quadratic form agrees exactly with \(K_A=(-\Delta_N)^{-1}\).

At the right edge,
\[
\widetilde K_A(A-\xi,A-\eta)
=
A-\max(A-\xi,A-\eta)
=
\boxed{\min(\xi,\eta)}.
\]

Thus the edge Green kernel is already independent of \(A\):
\[
\boxed{
K_{\rm edge}(\xi,\eta)=\min(\xi,\eta).
}
\]

It is the half-line Dirichlet Green kernel:
\[
-\partial_\xi^2K_{\rm edge}(\xi,\eta)=\delta(\xi-\eta),
\]
\[
K_{\rm edge}(0,\eta)=0,
\qquad
\partial_\xi K_{\rm edge}(\xi,\eta)\to0
\quad(\xi\to\infty)
\]
in the natural integrable-source class.

If
\[
h(\xi)=(K_{\rm edge}f)(\xi)
=\int_0^\infty\min(\xi,\eta)f(\eta)\,d\eta,
\]
then
\[
\boxed{-h''=f,\qquad h(0)=0,\qquad h'(\infty)=0.}
\]

This is an important refinement of v13.721: the correct right-edge Green representative is \(\min(\xi,\eta)\), not the full-line kernel \(-|\xi-\eta|/2\). They differ only by one-variable/affine gauge terms in the mean-zero bulk form, but those terms matter at an edge.

## 4. Edge reduction of the \(G_A\) term

Suzuki defines
\[
G_A=P_AGP_A
\]
on \(L_0^2(-A,A)\), where
\[
(P_Af)(x)
=
f(x)-\frac1{2A}\int_{-A}^Af(t)\,dt.
\]

For a mean-zero input \(u\), the inner projection is trivial and
\[
G_Au=P_A(Gu).
\]

Before the output projection, the right-edge difference kernel is exactly
\[
g((A-\xi)-(A-\eta))
=
\boxed{g(\eta-\xi)=g(\xi-\eta)}
\]
because \(g\) is even.

Thus the local edge convolution kernel is
\[
\boxed{G_{\rm edge}^{\rm loc}(\xi,\eta)=g(\xi-\eta).}
\]

However, \(P_A\) supplies a constant-output subtraction. Therefore the source-faithful limit is naturally an operator **modulo constants**, or equivalently a quadratic form on compensated edge profiles. One must not silently discard this projection when solving a non-mean-zero half-line forcing problem.

## 5. Candidate half-line Section-8 edge form

Combining the exact edge representatives gives the natural half-line quadratic-form kernel
\[
\boxed{
s_{\rm edge}(\xi,\eta)
=
g(\xi-\eta)-\lambda\min(\xi,\eta).
}
\]

Hence for sufficiently decaying compensated test profiles \(f,h\),
\[
\boxed{
\mathfrak s_{\rm edge}[f,h]
=
\int_0^\infty\!\!\int_0^\infty
\overline{f(\xi)}
\left[
g(\xi-\eta)-\lambda\min(\xi,\eta)
\right]
h(\eta)\,d\eta\,d\xi.
}
\]

This is the correct explicit edge object inherited from the finite Section-8 kernels at the quadratic-form/local-profile level.

It is **not yet proved** that the finite operators \(S_A\) converge in a resolvent sense to a self-adjoint operator represented by this kernel on ordinary \(L^2(0,\infty)\).

## 6. Formal edge operator and boundary conditions

If the form closes on a chosen half-line space and defines an operator, its formal action is
\[
\boxed{
(S_{\rm edge}q)(\xi)
=
\int_0^\infty g(\xi-\eta)q(\eta)\,d\eta
-\lambda\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta,
}
\]
understood modulo the constant-output projection inherited from \(P_A\).

Introduce
\[
h(\xi)
=
\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta.
\]
Then
\[
-h''=q,
\qquad
h(0)=0,
\qquad
h'(\infty)=0.
\]

Therefore the formal edge equation
\[
S_{\rm edge}q=f
\]
is equivalently
\[
\boxed{
\int_0^\infty g(\xi-\eta)q(\eta)\,d\eta
-\lambda h(\xi)
=
f(\xi)+c,
}
\]
\[
\boxed{
-h''(\xi)=q(\xi),\quad
h(0)=0,\quad h'(\infty)=0,
}
\]
where \(c\) represents the constant-output gauge/projection unless a normalization fixing it has been specified.

## 7. The requested \(q=S_{\rm edge}^{-1}e^{-\xi}\): precise model equation

The mathematically explicit **model** problem suggested by v13.721 is therefore
\[
\boxed{
\int_0^\infty
\left[
g(\xi-\eta)-\lambda\min(\xi,\eta)
\right]
q(\eta)\,d\eta
=
e^{-\xi}+c,
\qquad \xi>0,
}
\]
together with the Green-potential conditions
\[
\boxed{
h(\xi)=\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta,
\quad
-h''=q,
\quad h(0)=0,
\quad h'(\infty)=0.
}
\]

If a half-line normalization is chosen that kills the constant-output mode, set \(c=0\) and write
\[
\boxed{
q_{\rm model}(\xi)
=
S_{\rm edge}^{-1}e^{-\xi}.
}
\]

But this equation is **not yet the exact Suzuki deficiency equation**.

## 8. Why it is not yet the exact deficiency equation

Suzuki's actual finite-\(A\) equation is
\[
\boxed{
S_Au_\pm=C_\pm\bar D e_{\pm i}.
}
\]

The right-edge forcing in \(H(S_A)\) is therefore the edge limit of
\[
e^{-A}\bar D e_{+i},
\]
not automatically \(i e^{-\xi}\).

Suzuki explicitly warns that \(H(S_A)\not\subset L^2\) and that the formally integrated continuous-kernel equation (8.5) differs from \(S_Au_\pm=C_\pm\bar D e_{\pm i}\).

Thus the genuinely source-faithful edge problem has the form
\[
\boxed{
S_{\rm edge}q_+
=
F_+^{\rm edge},
\qquad
F_+^{\rm edge}
:=
\lim_{A\to\infty}e^{-A}\,\mathcal E_A(\bar D e_{+i}),
}
\]
provided this limit exists in the edge energy topology, where
\[
(\mathcal E_Af)(\xi)=f(A-\xi).
\]

Reflection gives the analogous left-edge channel.

The equality
\[
F_+^{\rm edge}=i e^{-\xi}
\]
is precisely an additional theorem that remains to be proved; it cannot be inferred merely from \(D=i\,d/dx\) on the core.

## 9. Consequence for the Suzuki--Xi bridge

The edge kernel itself is now explicit:
\[
\boxed{
s_{\rm edge}(\xi,\eta)
=
g(\xi-\eta)-\lambda\min(\xi,\eta).
}
\]

The remaining Suzuki--Xi obstruction has split into two sharply defined questions:

1. **transport-source gate**
\[
F_+^{\rm edge}\stackrel{?}=i e^{-\xi};
\]

2. **edge-resolvent gate**
\[
S_{\rm edge}^{-1}F_+^{\rm edge}
\stackrel{?}=c\,e^{-\xi}.
\]

Only if both hold does the scalar-channel normalization assumed in v13.721 follow.

Thus
\[
\boxed{\textbf{PASS: explicit half-line edge kernel/form derived}}
\]
\[
\boxed{\textbf{CORRECTION: }\bar D e_z=z e_z\textbf{ is not established}}
\]
\[
\boxed{\textbf{OPEN: exact deficiency forcing and scalar edge eigenprofile}}
\]

## 10. Next gate

Compute the edge forcing \(F_+^{\rm edge}\) directly from the definition of \(\bar D\) as the isometric extension \(H(T_A)\to H(S_A)\), rather than replacing it by ordinary differentiation. A workable route is to approximate \(e^x1_{[-A,A]}\) in the \(T_A\)-energy norm by core functions, differentiate those core approximants, and determine the limit after right-edge rescaling.

Only after this source term is fixed should the half-line integral equation be solved or Wiener--Hopf factorized.
