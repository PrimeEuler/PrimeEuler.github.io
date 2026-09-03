# Cone Derivation Ledger v13.179 — Return Boost and Tangent Rays

Status labels: [S] source-established, [D] exact derived, [I] interpretation, [O] open, [Audit] limitation.

## 1. Setup

Paper A Cone coordinates are

\[
X=\frac{x-y}{2},\qquad T=\frac{x+y}{2},\qquad Y=\sqrt{xy},
\]

so

\[
T^2-X^2=Y^2=xy.
\]

The discriminant-12 return

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}
\]

is conjugate over \(\mathbb R\) to the Lorentz boost

\[
B_{12}=\begin{pmatrix}2&\sqrt3\\ \sqrt3&2\end{pmatrix}.
\]

Let

\[
\varepsilon=2+\sqrt3,\qquad \varepsilon^{-1}=2-\sqrt3,
\]

and

\[
R_{12}=\log\varepsilon.
\]

Then

\[
B_{12}=\begin{pmatrix}\cosh R_{12}&\sinh R_{12}\\ \sinh R_{12}&\cosh R_{12}\end{pmatrix}
\]

because \(\cosh R_{12}=2\) and \(\sinh R_{12}=\sqrt3\).

## 2. [D] The Paper-A factor coordinates are null coordinates for the return boost

Use the ordering \((T,X)\). Then

\[
\binom{T'}{X'}=
B_{12}\binom{T}{X}
=
\begin{pmatrix}2&\sqrt3\\ \sqrt3&2\end{pmatrix}
\binom{T}{X}.
\]

Since

\[
x=T+X,\qquad y=T-X,
\]

we obtain

\[
\begin{aligned}
x'&=T'+X'=(2+\sqrt3)(T+X)=\varepsilon x,\\
y'&=T'-X'=(2-\sqrt3)(T-X)=\varepsilon^{-1}y.
\end{aligned}
\]

Therefore

\[
\boxed{x'=(2+\sqrt3)x,\qquad y'=(2-\sqrt3)y.}
\]

This immediately preserves the shell product:

\[
\boxed{x'y'=xy.}
\]

Hence every Paper-A shell \(xy=n\) is invariant under the real discriminant-12 boost.

This is an exact real-geometric bridge. It does **not** identify the Paper-A integer factor lattice with the integral lattice preserved by \(g_{12}\); the diagonal scaling above is irrational in the \((x,y)\) coordinates.

## 3. [D] Tangent-circle endpoints are exactly the null eigenrays

For fixed row level \(y=u\), the flat parabola is

\[
Y^2=u^2+2uX.
\]

Its Euclidean vertex is

\[
(X,Y)=\left(-\frac u2,0\right).
\]

At that point

\[
T=\frac u2,
\]

so in the \((T,X)\) side view the vertex is

\[
\boxed{v_-(u)=\left(\frac u2,-\frac u2\right).}
\]

The mirror column parabola has vertex

\[
\boxed{v_+(u)=\left(\frac u2,+\frac u2\right).}
\]

These are null vectors:

\[
T^2-X^2=0.
\]

They are also eigenvectors of \(B_{12}\):

\[
\boxed{B_{12}v_+(u)=\varepsilon\,v_+(u),}
\]

\[
\boxed{B_{12}v_-(u)=\varepsilon^{-1}v_-(u).}
\]

Thus the two exact tangent points from v13.177 lie on the expanding and contracting null eigendirections of the discriminant-12 return.

Equivalently, in factor coordinates:

- \(v_+(u)\) corresponds to \((x,y)=(u,0)\),
- \(v_-(u)\) corresponds to \((x,y)=(0,u)\).

The return scales these axes reciprocally:

\[
(u,0)\mapsto(\varepsilon u,0),
\qquad
(0,u)\mapsto(0,\varepsilon^{-1}u).
\]

Hence

\[
\boxed{
\text{Paper-A parabola tangent endpoints}
=
\text{null eigenrays of the discriminant-12 boost}.
}
\]

This is stronger than the earlier statement that the two constructions merely share a Lorentz form.

## 4. [D] The tangent-circle family is scaled by the Pell unit

The row-parabola tangent circle has radius

\[
t_-(u)=\frac u2.
\]

Under the contracting null ray,

\[
\boxed{t_-(u)\mapsto \varepsilon^{-1}t_-(u).}
\]

The mirror column endpoint scales by

\[
\boxed{t_+(u)\mapsto \varepsilon t_+(u).}
\]

Thus the real return does not permute the finite integer/half-integer tangent-circle family

\[
\frac12,1,\frac32,2,\ldots
\]

but instead generates a multiplicative Pell-unit orbit.

[Audit] This rules out the naive idea that the twelve circles \(u=1,\ldots,12\) form a finite orbit of \(g_{12}\) in ordinary real Cone geometry.

Projectively, however, the two null rays are fixed points of the return.

## 5. [D] Return as exact translation in Paper-A rapidity

On a fixed shell \(xy=n\), write

\[
x=\sqrt n\,e^s,\qquad y=\sqrt n\,e^{-s}.
\]

The boost law

\[
x'=\varepsilon x,\qquad y'=\varepsilon^{-1}y
\]

gives

\[
\boxed{s'=s+R_{12},}
\]

where

\[
\boxed{R_{12}=\log(2+\sqrt3).}
\]

Therefore the discriminant-12 return is literally a constant translation in the Paper-A shell rapidity coordinate.

For the \(k\)-th iterate,

\[
\boxed{s_k=s_0+kR_{12}.}
\]

and

\[
\boxed{x_k=\varepsilon^k x_0,\qquad y_k=\varepsilon^{-k}y_0.}
\]

This gives a precise bridge between the Pell-unit return scale and the Cone's hyperbolic shell parameterization.

## 6. [D] Factor exchange reverses the return

Paper-A factor exchange is

\[
P:(x,y)\mapsto(y,x).
\]

In \((T,X)\), this is

\[
\boxed{J:(T,X)\mapsto(T,-X).}
\]

Since

\[
B_{12}^{-1}
=
\begin{pmatrix}2&-\sqrt3\\-\sqrt3&2\end{pmatrix},
\]

we have

\[
\boxed{J B_{12} J=B_{12}^{-1}.}
\]

Equivalently, in rapidity,

\[
s\mapsto -s
\]

conjugates

\[
s\mapsto s+R_{12}
\]

to

\[
s\mapsto s-R_{12}.
\]

So the exact Cone factor-exchange involution is a reversing symmetry of the real discriminant-12 boost.

This matches the same abstract dihedral relation present in the arithmetic return problem:

\[
\text{involution}\cdot\text{return}\cdot\text{involution}
=
\text{return}^{-1}.
\]

[Audit] The simple Cone factor exchange \(J\) should not automatically be identified with the specific integral reversing matrix \(C\) used for \(g_{12}\). Under the Lorentz conjugacy \(L\), the integral reversor becomes a different real Lorentz involution. What is exact here is the shared reversing relation, not equality of the involutions.

## 7. [D] n=11 shell under the return

The integer endpoint

\[
(x,y)=(11,1)
\]

has

\[
(T,X)=\left(6,5\right),
\qquad
T^2-X^2=11.
\]

Under one real return,

\[
\boxed{(11,1)\mapsto(11\varepsilon,\varepsilon^{-1}),}
\]

still satisfying

\[
(11\varepsilon)(\varepsilon^{-1})=11.
\]

Its rapidity increases by exactly \(R_{12}\).

The mirror endpoint \((1,11)\) is obtained by factor exchange, and the reversing relation sends forward iteration on one orientation to backward iteration on the other.

Thus the exact \(n=11\), \(x+y=12\) boundary point is not fixed by the return; it is one point on the invariant \(n=11\) hyperbolic orbit.

## 8. [D] Row/column parabola families transform covariantly

A fixed row \(y=u\) is sent to

\[
y'=\varepsilon^{-1}u.
\]

Therefore the row-parabola family transforms as

\[
\boxed{P_u^{\rm row}\mapsto P_{\varepsilon^{-1}u}^{\rm row}.}
\]

Likewise a fixed column \(x=u\) transforms as

\[
\boxed{P_u^{\rm col}\mapsto P_{\varepsilon u}^{\rm col}.}
\]

The corresponding tangent-circle radii transform with the same factors.

So the discriminant-12 return acts naturally on the **continuous** Paper-A parabola/circle foliation, even though it does not preserve the integer-indexed subfamily.

## 9. Interpretation

[I] The new exact picture is:

\[
\boxed{
\text{integer factor mesh}
\subset
\text{continuous Cone foliation}
\xrightarrow{\;g_{12}\text{ over }\mathbb R\;}
\text{Pell-unit scaling flow}.
}
\]

The arithmetic return preserves an integral lattice in its native discriminant-12 coordinates, while the same return in Paper-A null coordinates becomes irrational reciprocal scaling.

This suggests that the two papers are best connected not by trying to identify their integer grids, but by viewing them as **different arithmetic sections of one real Lorentz dynamical system**.

That statement is currently an interpretation, but all algebraic ingredients above are exact.

## 10. Strongest new bridge

The strongest theorem from this ledger is the combined identity

\[
\boxed{
(x,y)
\xrightarrow{\text{Cone}}
(T,X)
\xrightarrow{B_{12}}
(T',X')
\Longleftrightarrow
(x,y)\mapsto
\bigl((2+\sqrt3)x,(2-\sqrt3)y\bigr),
}
\]

with

\[
\boxed{s\mapsto s+\log(2+\sqrt3).}
\]

and with the v13.177 tangent endpoints precisely equal to the two null eigenrays.

This provides an exact, non-numerological bridge from the new tangent-circle geometry into the core discriminant-12 return map.

## 11. Next open calculation

[O] Push the continuous-resolution mesh through this return. If

\[
\Lambda_m=1+\frac1m\mathbb Z_{\ge0},
\]

then determine exactly how \(m\), tangent phase \(\theta_m(n)\), and terminal arm phase transform under

\[
(x,y)\mapsto(\varepsilon x,\varepsilon^{-1}y).
\]

The key question is whether there is a natural renormalized resolution parameter for which the discriminant-12 return acts by a simple shift or scale on the v13.172--v13.176 phase system.
