# Cone Derivation Ledger v13.766 — Lane A Coupling-Homotopy Collapse and Explicit Kernel Sign Obstruction

Date: 2026-09-24

Lane: A — Screw/Helix–Weil–Hermite–Biehler Program.

Status: [D] exact coupling-homotopy reduction; [D] explicit basepoint kernel formulas from Suzuki's finite kernel; [N] pointwise sign/monotonicity route obstructed; [C] precise remaining positivity criterion.

Parents: v13.743, v13.749, v13.761–765.

## 0. Synchronization

Live ledger checked immediately before write: v13.765 is current head; no numbering collision.

## 1. Coupling homotopy is exactly affine [D]

From v13.765 define
\[
\mathcal F_{+,A}=(R_A^{(+)}1)\otimes\ell_{0,A},
\qquad
\mathcal F_{-,A}=(R_A^{(-)}x)\otimes\ell_{1,A}.
\]

Introduce \(t\in[0,1]\):
\[
D_{+,A}(t):=\det_F(I+t\mathcal F_{+,A}),
\]
\[
D_{-,A}(t):=\det_F(I+t\mathcal F_{-,A}).
\]

Because each perturbation is rank one,
\[
\boxed{D_{+,A}(t)=1+tM_{00},}
\qquad
\boxed{D_{-,A}(t)=1+tM_{1x}.}
\]

Thus
\[
D'_{+,A}(t)=M_{00},\qquad
D'_{-,A}(t)=M_{1x}.
\]

There is no hidden nonlinear determinant flow. The proposed coupling-monotonicity route collapses exactly to the sign/location of the two scalar moments.

For real \(M\), \(1+tM\) is nonzero on \(0\le t\le1\) iff \(M>-1\). If \(M=-1\), the physical endpoint is singular; if \(M<-1\), a zero occurs at \(t=-1/M\in(0,1)\).

Hence:
\[
\boxed{
\text{coupling homotopy adds no leverage beyond proving }
M_{00}>-1,\ M_{1x}>-1.
}
\]

## 2. Reality of the two moments [D/C]

Suzuki's finite kernel and the source functions \(1,x\) are real. On a real, invertible realization of the corrected response operator \(\mathcal L_A\), the responses
\[
R_A^{(+)}1,\qquad R_A^{(-)}x
\]
are real, and the basepoint functionals are real. Therefore
\[
\boxed{M_{00},M_{1x}\in\mathbb R}
\]
on that real realization.

This is the natural source-faithful setting of the corrected Section-8 moment system. If a different complexified realization is used, the corresponding reality structure must be stated explicitly rather than assumed.

## 3. Suzuki's explicit finite kernel at the basepoint [D]

The audit in v13.749 independently source-checked Suzuki's formula
\[
k(x,y)=g(x-y)-\lambda N(x,y),
\]
with
\[
\boxed{
N(x,y)=\frac{x^2+y^2}{4A}-\frac{|x-y|}{2}+\frac{A}{6}.
}
\]

At \(x=0\),
\[
\boxed{
N(0,y)
=
\frac{y^2}{4A}-\frac{|y|}{2}+\frac{A}{6}.
}
\]

Hence
\[
\boxed{
k(0,y)
=
g(y)
-\lambda\left(
\frac{y^2}{4A}-\frac{|y|}{2}+\frac{A}{6}
\right).
}
\]

For \(y\ne0\),
\[
\partial_xN(0,y)=\frac12\operatorname{sgn}(y),
\]
while evenness of \(g\) gives
\[
g'(-y)=-g'(y).
\]
Therefore
\[
\boxed{
k_x(0,y)
=
-g'(y)-\frac{\lambda}{2}\operatorname{sgn}(y),
\qquad y\ne0.
}
\]

These formulas recover exactly the even/odd parities already audited in v13.749.

## 4. The geometric Green term changes sign [D]

Set
\[
t=\frac{|y|}{A}\in[0,1].
\]
Then
\[
N(0,y)
=
A\left(
\frac{t^2}{4}-\frac t2+\frac16
\right)
=
A\left[
\frac{(t-1)^2}{4}-\frac1{12}
\right].
\]

Its zero in \(0\le t\le1\) is
\[
\boxed{
t_*=1-\frac1{\sqrt3}.
}
\]

Thus
\[
N(0,y)>0
\quad\text{for}\quad
0\le |y|<A\left(1-\frac1{\sqrt3}\right),
\]
and
\[
N(0,y)<0
\quad\text{for}\quad
A\left(1-\frac1{\sqrt3}\right)<|y|\le A.
\]

In particular,
\[
N(0,0)=A/6>0,\qquad
N(0,\pm A)=-A/12<0.
\]

Therefore the Green correction in \(k(0,y)\) has no fixed pointwise sign even before combining it with \(g(y)\).

## 5. The derivative trace kernel also has no source-forced fixed sign [N]

For \(y>0\),
\[
k_x(0,y)=-g'(y)-\lambda/2,
\]
and for \(y<0\) oddness supplies the reflected value.

The established screw positivity controls the quadratic increment kernel/form; it does not supply a pointwise inequality forcing
\[
-g'(y)-\lambda/2
\]
to have one sign on \(0<y<A\).

Likewise, even where screw positivity yields information about \(g\), the sign-changing \(N(0,y)\) term prevents a pointwise sign theorem for \(k(0,y)\) from following automatically.

Hence:
\[
\boxed{
\text{neither }\ell_{0,A}\text{ nor }\ell_{1,A}
\text{ is presently a positive functional on its parity channel.}
}
\]

No pointwise-kernel argument presently implies
\[
M_{00}\ge0
\quad\text{or}\quad
M_{1x}\ge0.
\]

## 6. Why resolvent positivity would still be insufficient without compatibility [N]

Even if \(R_A^{(\pm)}\) is positive as an operator in some Hilbert realization, the moments are
\[
M_{00}=\ell_{0,A}(R_A^{(+)}1),
\]
\[
M_{1x}=\ell_{1,A}(R_A^{(-)}x).
\]

Operator positivity controls quantities of the form
\[
\langle f,R_Af\rangle,
\]
not arbitrary mixed boundary evaluations \(\ell(R_Af)\).

Therefore positivity of \(R_A\) alone does not determine the sign of \(M_{00}\) or \(M_{1x}\). One still needs a positive-compatible Riesz identity, e.g.
\[
\ell_{0,A}(v)=\langle q_{0,A},v\rangle,\qquad q_{0,A}\ \text{appropriately aligned with }1,
\]
and analogously in the odd channel.

This is the same functional mismatch first exposed abstractly in v13.758, now seen directly in Suzuki's explicit basepoint kernels.

## 7. Exact remaining sign criterion [C]

The homotopy/Fredholm route closes if one can prove
\[
\boxed{M_{00}>-1,\qquad M_{1x}>-1.}
\]

A stronger sufficient condition is
\[
M_{00}\ge0,\qquad M_{1x}\ge0,
\]
but the explicit kernel formulas do not presently imply it.

The norm route from v13.761 remains valid:
\[
|M_{00}|
\le
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|,
\]
\[
|M_{1x}|
\le
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|.
\]
Thus
\[
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|<1,
\qquad
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|<1
\]
still gives nonresonance, but this is a magnitude theorem, not a sign theorem.

## 8. Consequence for Lane A strategy [N/D]

The following routes have now been exhausted to their exact stopping points:

1. bulk coercivity alone — insufficient (v13.761);
2. direct HB/boundary characteristic identification — category mismatch (v13.765);
3. coupling homotopy — exactly affine, so equivalent to the original \(M>-1\) problem (this entry);
4. pointwise sign of Suzuki's basepoint kernels — blocked by the explicit sign-changing Green term and uncontrolled derivative combination (this entry).

Therefore further formal rearrangement of the same scalar system is unlikely to close nonresonance.

The next genuinely new information must come from one of:
- quantitative norm/coercivity estimates strong enough to put \(|M|<1\);
- a positive-compatible energy-space Riesz representation of the trace functionals;
- a direct numerical/rigorous finite-\(A\) evaluation of \(M_{00},M_{1x}\) followed by an analytic asymptotic argument;
- an as-yet-unproved intertwiner identifying the feedback operator with a protected extension determinant.

## 9. Cross-lane guardrail

Lane B's audit-PASSed centered prime-orbit trace remains an exact bulk decomposition tool:
\[
\mathscr W_{S,\rm fin}=-\mu_{\rm Weil}^{\rm fin}.
\]
It does not alter the sign-changing finite-\(A\) Green trace kernels above. No Schur nonresonance conclusion is imported from Lane B.

## Result

The coupling/monotonicity gate is completely resolved:
\[
\boxed{
D_{\pm,A}(t)=1+tM_{\pm,A}.
}
\]
It is safe on \(0\le t\le1\) exactly when the corresponding real scalar moment exceeds \(-1\).

Suzuki's explicit basepoint kernels are
\[
\boxed{
k(0,y)=
g(y)-\lambda\left(
\frac{y^2}{4A}-\frac{|y|}{2}+\frac A6
\right),
}
\]
\[
\boxed{
k_x(0,y)
=
-g'(y)-\frac{\lambda}{2}\operatorname{sgn}(y).
}
\]

The geometric term \(N(0,y)\) changes sign at
\[
\boxed{|y|=A(1-1/\sqrt3),}
\]
so the hoped-for pointwise positivity route does not close.

The smallest remaining analytic target is no longer "prove monotonicity"; it is directly:
\[
\boxed{M_{00}>-1,\qquad M_{1x}>-1}
\]
or, quantitatively, \(|M_{00}|,|M_{1x}|<1\).
