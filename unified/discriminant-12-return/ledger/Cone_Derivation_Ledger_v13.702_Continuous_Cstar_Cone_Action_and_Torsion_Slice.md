# Cone Derivation Ledger v13.702 — Continuous C* Cone Action and the Cyclotomic Torsion Slice

Date: 2026-09-23

Status: exact construction of a continuous \(\mathbb C^\times\) action on the complexified cone/spinor model. This follows v13.701's exact identification \(\mathcal Z^3=iI\).

## 0. Synchronization

Immediately before this write the live head was v13.701, commit \`0eca70249d9820088427db887e21727610690306\`; no v13.702 collision was present.

## 1. Start from the null-spinor factorization

Use the split-matrix cone model
\[
Q(X,Y,T)
=
\begin{pmatrix}
T+X&Y\\
Y&T-X
\end{pmatrix}
=
\begin{pmatrix}x&Y\\Y&y\end{pmatrix},
\]
with
\[
\det Q=xy-Y^2=T^2-X^2-Y^2.
\]

On the null cone, choose a spinor
\[
\psi=\binom{\alpha}{\beta},
\qquad
Q=\psi\psi^T,
\]
so
\[
x=\alpha^2,\qquad
y=\beta^2,\qquad
Y=\alpha\beta.
\]

For the positive real cone,
\[
\alpha=\sqrt G\,e^{s/2},
\qquad
\beta=\sqrt G\,e^{-s/2},
\]
which gives
\[
x=Ge^s,\quad y=Ge^{-s},\quad Y=G,
\]
and hence
\[
T=G\cosh s,\qquad X=G\sinh s.
\]

## 2. A genuine C* action on the spinor

For any
\[
w\in\mathbb C^\times,
\]
define
\[
\boxed{
D(w)=
\begin{pmatrix}
w^{1/2}&0\\
0&w^{-1/2}
\end{pmatrix}
}
\]
locally on the double cover, or equivalently define the action directly on cone coordinates by
\[
\boxed{
x\mapsto wx,\qquad
y\mapsto w^{-1}y,\qquad
Y\mapsto Y.
}
\]

The latter is globally single-valued in \(w\) and avoids a square-root branch.

The group law is exact:
\[
D(w_1w_2)\sim D(w_1)D(w_2)
\]
on spinors, while on cone coordinates
\[
\boxed{
\rho(w_1w_2)=\rho(w_1)\rho(w_2).
}
\]

In \((T,X,Y)\) coordinates,
\[
T'=\frac{wx+w^{-1}y}{2},
\qquad
X'=\frac{wx-w^{-1}y}{2},
\qquad
Y'=Y.
\]

Using \(x=T+X,y=T-X\),
\[
\boxed{
\begin{pmatrix}T'\\X'\end{pmatrix}
=
\begin{pmatrix}
a(w)&b(w)\\
b(w)&a(w)
\end{pmatrix}
\begin{pmatrix}T\\X\end{pmatrix},
\qquad
Y'=Y,
}
\]
where
\[
a(w)=\frac{w+w^{-1}}2,
\qquad
b(w)=\frac{w-w^{-1}}2.
\]

Since
\[
a(w)^2-b(w)^2=1,
\]
this is a complex Lorentz boost.

## 3. Null-cone and determinant preservation

Directly,
\[
x'y'=(wx)(w^{-1}y)=xy.
\]
Therefore
\[
x'y'-Y'^2=xy-Y^2.
\]

Hence
\[
\boxed{
\det Q'=\det Q
}
\]
for every \(w\in\mathbb C^\times\).

Equivalently,
\[
\boxed{
T'^2-X'^2-Y'^2=T^2-X^2-Y^2.
}
\]

Thus \(\rho(\mathbb C^\times)\) preserves the full complexified quadratic form, not merely its null locus.

This closes the primary existence gate:
\[
\boxed{
\rho:\mathbb C^\times\longrightarrow SO(2,1;\mathbb C)
}
\]
is a genuine one-complex-parameter subgroup (in this coordinate ordering, the boost acts in the \(T,X\) plane and fixes \(Y\)).

## 4. Logarithmic coordinate

Write
\[
w=e^\ell,\qquad
\ell=s+i\phi.
\]
Then
\[
a(w)=\cosh\ell,\qquad
b(w)=\sinh\ell,
\]
so
\[
\boxed{
\begin{pmatrix}T'\\X'\end{pmatrix}
=
\begin{pmatrix}
\cosh\ell&\sinh\ell\\
\sinh\ell&\cosh\ell
\end{pmatrix}
\begin{pmatrix}T\\X\end{pmatrix}.
}
\]

The infinitesimal generator is
\[
K_X=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&0
\end{pmatrix}
\]
in \((T,X,Y)\) ordering, and
\[
\boxed{
\rho(e^\ell)=e^{\ell K_X}.
}
\]

Thus \(\log w=\ell\) is literally the additive Lie-algebra coordinate of the complexified boost.

## 5. Real positive slice recovers rapidity

For
\[
w=e^s>0,
\]
\[
\ell=s\in\mathbb R,
\]
and
\[
\rho(e^s)=
\begin{pmatrix}
\cosh s&\sinh s&0\\
\sinh s&\cosh s&0\\
0&0&1
\end{pmatrix}.
\]

Acting on the cone waist point \((T,X,Y)=(G,0,G)\) gives
\[
\boxed{
(T,X,Y)=(G\cosh s,G\sinh s,G),
}
\]
exactly the project's rapidity parametrization.

Therefore
\[
\boxed{
\mathbb R_{>0}\subset\mathbb C^\times
}
\]
is not merely analogous to the rapidity flow: it **is** the rapidity boost subgroup.

## 6. Unit-circle slice is an imaginary boost, not the fixed-T XY rotation

For
\[
w=e^{i\phi},
\]
\[
\ell=i\phi,
\]
so
\[
\cosh(i\phi)=\cos\phi,\qquad
\sinh(i\phi)=i\sin\phi.
\]
Hence
\[
\boxed{
T'=T\cos\phi+iX\sin\phi,
\qquad
X'=iT\sin\phi+X\cos\phi,
\qquad
Y'=Y.
}
\]

This is a compact \(U(1)\) subgroup inside the **complexified \(TX\)-boost plane**.

[G] It is not the intrinsic fixed-\(T\) cone-circle rotation
\[
J:(X,Y,T)\mapsto(-Y,X,T).
\]

Thus the project contains at least two distinct \(U(1)\)-type phase structures:

1. \(U(1)_{\rm boost}\): imaginary rapidity, rotating the complexified \(T/X\) boost plane;
2. \(U(1)_{XY}\): ordinary fixed-\(T\) rotations in the \(X/Y\) plane.

They must not be identified without an explicit conjugacy in a larger group.

## 7. The fourth-root torsion of the boost C* action

At
\[
w=i=e^{i\pi/2},
\]
\[
a(i)=0,\qquad b(i)=i,
\]
so
\[
\boxed{
\rho(i):(T,X,Y)\mapsto(iX,iT,Y).
}
\]

Its square is
\[
\boxed{
\rho(i)^2:(T,X,Y)\mapsto(-T,-X,Y).
}
\]

Its fourth power is identity.

Therefore the \(\mu_4\) torsion inside this \(\mathbb C^\times\) boost action is an order-four coordinate-mixing subgroup, but it is **not** the scalar subgroup
\[
\{I,iI,-I,-iI\}
\]
identified in v13.701.

This is a crucial negative result:
\[
\boxed{
\rho(i)\ne iI.
}
\]

So the exact cyclotomic scalar torsion \(\mathcal Z^3=iI\) belongs to a different central phase action than the \(\mu_4\) torsion of the complexified rapidity boost.

## 8. Two commuting C* candidates, not one collapsed C*

The scalar action
\[
S(\lambda):v\mapsto\lambda v,
\qquad \lambda\in\mathbb C^\times,
\]
commutes with the boost action \(\rho(w)\).

However,
\[
q(S(\lambda)v)=\lambda^2q(v),
\]
so scalar \(\mathbb C^\times\) preserves the null cone projectively/setwise but not the quadratic form level-by-level.

By contrast,
\[
q(\rho(w)v)=q(v).
\]

Therefore the natural larger action is
\[
\boxed{
(\lambda,w)\in\mathbb C^\times_{\rm scale}\times\mathbb C^\times_{\rm boost}
}
\]
with
\[
v\mapsto\lambda\,\rho(w)v.
\]

It satisfies
\[
q(\lambda\rho(w)v)=\lambda^2q(v).
\]

On the null cone \(q=0\), both factors preserve the cone.

This is a stronger and more accurate ambient candidate than a single undifferentiated \(\mathbb C^\times\).

## 9. Placement of the established cyclotomic C4

v13.701 proved
\[
\mathcal Z^3=iI.
\]

Therefore
\[
\boxed{
\langle\mathcal Z^3\rangle=\mu_4
\subset
\mathbb C^\times_{\rm scale}.
}
\]

It is **not** the fourth-root torsion of
\[
\mathbb C^\times_{\rm boost}.
\]

This resolves an important ambiguity:

\[
\boxed{
\begin{array}{c|c|c}
&\mathbb C^\times_{\rm scale}&\mathbb C^\times_{\rm boost}\\ \hline
\text{action}&v\mapsto\lambda v&x\mapsto wx,\ y\mapsto w^{-1}y\\
q&\lambda^2q&q\\
\text{real positive part}&\text{dilation}&\text{rapidity boost}\\
i\text{ torsion}&iI=\mathcal Z^3&(T,X,Y)\mapsto(iX,iT,Y)\\
\text{central}&\text{yes}&\text{within boost torus; not globally scalar}
\end{array}
}
\]

## 10. Combined logarithmic coordinates

The natural continuous coordinates are therefore two complex logarithms:
\[
\lambda=e^\tau,\qquad
w=e^\ell.
\]

The combined action is
\[
\boxed{
v\mapsto e^\tau e^{\ell K_X}v.
}
\]

At minimum this gives a commuting complex two-torus
\[
\boxed{
(\mathbb C^\times)^2
}
\]
acting on the complexified null cone, one factor by scale and one by Lorentz boost.

On the positive real cone, the real subgroups are:

- \(e^{\Re\tau}\): overall scale/product-shell change;
- \(e^{\Re\ell}=e^s\): rapidity/factor-ratio change.

Thus the two most elementary continuous cone variables are already the two real logarithms expected from
\[
(x,y)\in\mathbb R_{>0}^2:
\quad
\frac12\log(xy),\qquad
\frac12\log(x/y).
\]

Indeed, if
\[
\tau=\frac12\log(xy),\qquad
s=\frac12\log(x/y),
\]
then
\[
\boxed{
\log x=\tau+s,\qquad
\log y=\tau-s.
}
\]

This is a particularly clean non-D12 coordinate system.

## 11. Export significance

### Suzuki / operator lane

The cone now has two additive logarithmic generators:
\[
\tau=\tfrac12\log(xy),\qquad
s=\tfrac12\log(x/y).
\]

Any Suzuki Cayley/log bridge should therefore be tested against **both**:

- scale/spectral-radius log \(\tau\);
- ratio/rapidity log \(s\).

A one-variable match could otherwise conflate distinct generators.

### Hilbert–Pólya lane

This gives an exact Lie-group scaffold, not an HP operator:
\[
(\mathbb C^\times)^2
\leftrightarrow
\text{two commuting logarithmic generators}.
\]
The self-adjointness/positivity/spectral-determinant requirements remain wholly open.

### Cyclotomic lane

The cyclotomic \(C_4\) sits in the scale-phase factor, not the rapidity-boost torsion:
\[
\boxed{
\mathcal Z^3=iI\in\mathbb C^\times_{\rm scale}.
}
\]

This is a sharper placement than was available before v13.701.

## 12. Result

\[
\boxed{
\textbf{PASS: a genuine }\mathbb C^\times_{\rm boost}\textbf{ action preserves the complexified quadratic form.}
}
\]

\[
\boxed{
\textbf{PASS: its positive-real subgroup is exactly the rapidity flow.}
}
\]

\[
\boxed{
\textbf{FAIL: its }\mu_4\textbf{ torsion is not the scalar cyclotomic }\mu_4.
}
\]

\[
\boxed{
\textbf{PASS: the natural broader continuous action is at least }
\mathbb C^\times_{\rm scale}\times\mathbb C^\times_{\rm boost}.
}
\]

\[
\boxed{
\log x=\tau+s,\qquad
\log y=\tau-s
}
\]
is the corresponding additive coordinate decomposition.

## 13. Next gate

Before exporting to Suzuki, test whether the split-matrix congruence model realizes the combined \((\mathbb C^\times)^2\) action naturally and determine the semidirect extension obtained by adjoining factor exchange and complex conjugation. In particular, compute how
\[
R_X,\quad C
\]
act on
\[
(\tau,\ell)
\]
and whether the resulting group is a Weyl/dihedral extension of the complex torus.
