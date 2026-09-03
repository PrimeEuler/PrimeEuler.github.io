# Cone Derivation Ledger v13.181 — Pell Coefficient Parity and the Ramified Swap

Status labels: [S] source-established, [D] exact derived, [I] interpretation, [O] open, [Audit] limitation.

## 1. Purpose

This note tests whether the Pell-renormalized Cone mesh phases from v13.180 admit a canonical mod-2 reduction matching the ramified finite quotient in the discriminant-12 paper.

The answer is mixed:

- the transported mesh indices themselves are mod-2 invariant and therefore do **not** reproduce the nontrivial ramified transvection;
- however, the Pell unit multiplication on the coefficient lattice of `Q(sqrt(3))` reduces mod 2 to the factor-exchange swap `P`;
- that swap is exactly conjugate over `F_2` to the ramified transvection already established in the arithmetic paper.

So the bridge is not `continuous phase -> parity of transported mesh index`. The exact finite bridge passes through the **Pell coefficient lattice**.

---

## 2. Pell unit and coefficient lattice

Let

\[
\lambda=2+\sqrt3,
\qquad
\lambda^{-1}=2-\sqrt3.
\]

Write a general element of `Z[sqrt(3)]` as

\[
a+b\sqrt3.
\]

Multiplication by `lambda` gives

\[
(2+\sqrt3)(a+b\sqrt3)
=(2a+3b)+(a+2b)\sqrt3.
\]

Therefore, in the coefficient basis `(1,sqrt(3))`, multiplication by `lambda` is represented by

\[
M_\lambda=
\begin{pmatrix}
2&3\\
1&2
\end{pmatrix}.
\]

[D] Its determinant is

\[
\det M_\lambda=4-3=1,
\]

as expected from `N(lambda)=1`.

---

## 3. Exact mod-2 reduction

Reduce `M_lambda` modulo 2:

\[
\overline M_\lambda
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
=:P.
\]

Thus

\[
\boxed{\overline M_\lambda=P.}
\]

[D] The Pell return on the coefficient lattice reduces mod 2 to the coordinate swap

\[
\boxed{(a,b)\mapsto(b,a).}
\]

Since

\[
P^2=I,
\]

this reduction has order 2.

This is already the factor-exchange matrix used elsewhere in the project.

---

## 4. Comparison with the ramified transvection

The discriminant-12 return matrix is

\[
g_{12}=
\begin{pmatrix}
3&1\\
2&1
\end{pmatrix}.
\]

Its mod-2 reduction is

\[
\overline g=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

[S] This is the nontrivial transvection appearing in the ramified quotient.

Let

\[
\Phi=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix},
\qquad
\Phi(x,y)=(x,x+y).
\]

Over `F_2`, `Phi^{-1}=Phi`, and direct calculation gives

\[
\boxed{
\Phi\,\overline g\,\Phi^{-1}=P.
}
\]

Therefore

\[
\boxed{
\overline g
\sim_{GL_2(\mathbf F_2)}
P
=
\overline M_\lambda.
}
\]

[D] The ramified transvection and Pell coefficient swap are the same nontrivial unipotent conjugacy class in `GL_2(F_2)`.

This is an exact algebraic bridge.

---

## 5. Consequence for Pell powers

Write

\[
\lambda^k=a_k+b_k\sqrt3,
\qquad a_k,b_k\in\mathbf Z.
\]

Then

\[
\binom{a_{k+1}}{b_{k+1}}
=M_\lambda
\binom{a_k}{b_k}.
\]

Modulo 2,

\[
\binom{a_{k+1}}{b_{k+1}}
\equiv
P
\binom{a_k}{b_k}.
\]

Starting from

\[
(a_0,b_0)=(1,0),
\]

we obtain

\[
(a_k,b_k)\equiv
\begin{cases}
(1,0) & k\text{ even},\\
(0,1) & k\text{ odd},
\end{cases}
\pmod2.
\]

Hence

\[
\boxed{a_k\equiv k+1\pmod2,\qquad b_k\equiv k\pmod2.}
\]

For example,

\[
\begin{aligned}
\lambda^0&=1,\\
\lambda^1&=2+\sqrt3,\\
\lambda^2&=7+4\sqrt3,\\
\lambda^3&=26+15\sqrt3,\\
\lambda^4&=97+56\sqrt3,
\end{aligned}
\]

so the parity pairs are

\[
(1,0),(0,1),(1,0),(0,1),(1,0),\ldots
\]

exactly as predicted.

---

## 6. Reset phases after Pell transport

From v13.180, under the Pell scaling

\[
x\mapsto\lambda x,
\qquad
y\mapsto\lambda^{-1}y,
\]

an isotropic mesh density `m` is transported to

\[
m_{x,k}=m\lambda^{-k},
\qquad
m_{y,k}=m\lambda^k.
\]

If the natural transported anchors are also used, the corresponding local phases are invariant.

Now instead **reset the anchor to 1** after `k` iterates. Define

\[
\widehat\phi_{x,k}
=
\left\{m\lambda^{-k}(\lambda^k x-1)\right\},
\]

\[
\widehat\phi_{y,k}
=
\left\{m\lambda^k(\lambda^{-k}y-1)\right\}.
\]

Then

\[
\widehat\phi_{x,k}
=
\left\{m(x-1)+m(1-\lambda^{-k})\right\},
\]

\[
\widehat\phi_{y,k}
=
\left\{m(y-1)-m(\lambda^k-1)\right\}.
\]

Write

\[
\lambda^k=a_k+b_k\sqrt3,
\qquad
\lambda^{-k}=a_k-b_k\sqrt3.
\]

For integer `m`, all integer coefficient terms disappear modulo 1, giving

\[
\boxed{
\widehat\phi_{x,k}
=
\{\phi_{x,0}+m b_k\sqrt3\},
}
\]

\[
\boxed{
\widehat\phi_{y,k}
=
\{\phi_{y,0}-m b_k\sqrt3\}.
}
\]

So reset-to-unit-anchor phases undergo opposite irrational rotations controlled by the Pell coefficient `b_k`.

[D] Their sum is invariant modulo 1:

\[
\boxed{
\widehat\phi_{x,k}+\widehat\phi_{y,k}
\equiv
\phi_{x,0}+\phi_{y,0}
\pmod1.
}
\]

The phase difference changes by

\[
\boxed{
\widehat\phi_{x,k}-\widehat\phi_{y,k}
\equiv
\phi_{x,0}-\phi_{y,0}+2m b_k\sqrt3
\pmod1.
}
\]

---

## 7. Negative result: transported mesh parity is too trivial

Suppose a point lies exactly on a transported mesh:

\[
x=a_x+\frac{j_x}{m_x},
\qquad
y=a_y+\frac{j_y}{m_y}.
\]

Under the covariant transport rule

\[
x'=\lambda x,
\quad
a_x'=\lambda a_x,
\quad
m_x'=m_x/\lambda,
\]

we get

\[
m_x'(x'-a_x')=m_x(x-a_x)=j_x.
\]

Similarly

\[
j_y'=j_y.
\]

Therefore

\[
\boxed{
(j_x,j_y)\bmod2
\text{ is invariant under transported Pell flow.}
}
\]

[Audit] This parity action is the identity, whereas the ramified arithmetic quotient is the nontrivial transvection `gbar` (equivalently the swap `P`).

Hence:

\[
\boxed{
\text{naive parity of transported Cone mesh indices}
\neq
\text{ramified mod-2 action}.
}
\]

Any exact bridge must include additional arithmetic structure.

---

## 8. Where the exact bridge actually lives

The successful finite reduction is

\[
\boxed{
\text{Pell multiplication on }\mathbf Z[\sqrt3]
\longrightarrow
M_\lambda\bmod2=P.
}
\]

Together with the established ramified conjugacy

\[
\boxed{
\Phi\,\overline g\,\Phi^{-1}=P,
}
\]

we obtain the exact chain

\[
\boxed{
\text{real Cone boost}
\leftrightarrow
\lambda=2+\sqrt3
\longrightarrow
M_\lambda
\longrightarrow
P\ (\bmod2)
\longleftrightarrow
\overline g.
}
\]

The first equivalence is the Lorentz/Pell realization from v13.179.
The final equivalence is conjugacy over `F_2`.

This is substantially stronger than attempting to reduce arbitrary real phase values directly modulo 2.

---

## 9. Relation to the Boolean quotient

Earlier project work established the affine-coordinate map

\[
\Phi(x,y)=(x,x+y)
\]

that conjugates the ramified transvection to factor exchange:

\[
\Phi\overline g\Phi^{-1}=P.
\]

The reduced norm becomes XOR in the corresponding Boolean coordinates.

Therefore the new Pell calculation identifies the same swap `P` from a completely different direction:

\[
\boxed{
\text{Pell coefficient parity}
\xrightarrow{\lambda}
P
\xleftarrow{\Phi}
\text{ramified transvection}.
}
\]

[D] This is a common finite action, not merely a similarity of cycle types.

[I] It suggests that the Boolean factor-exchange picture is the mod-2 shadow of the same Pell unit that generates the real Cone boost.

[Audit] This does **not** mean that arbitrary Cone mesh phases themselves form `F_2^2`, nor that real phase reduction canonically defines the ramified ideal quotient.

---

## 10. A useful two-level picture

We now have two compatible dynamical descriptions of the discriminant-12 return.

### Real level

On null coordinates:

\[
(x,y)\mapsto(\lambda x,\lambda^{-1}y).
\]

On rapidity:

\[
s\mapsto s+\log\lambda.
\]

### Mod-2 coefficient level

On Pell coefficients:

\[
(a,b)\mapsto(2a+3b,a+2b)
\]

and hence

\[
\boxed{(a,b)\mapsto(b,a)\pmod2.}
\]

Thus the same unit `lambda` yields:

\[
\boxed{
\text{continuous hyperbolic translation over }\mathbf R
\quad\text{and}\quad
\text{order-2 swap over }\mathbf F_2.
}
\]

This is an exact local/global reduction statement for the Pell unit action.

---

## 11. Publication-safe claim

The strongest currently justified synthesis is:

\[
\boxed{
\begin{array}{c}
\text{The discriminant-12 return is multiplication by the Pell unit }2+\sqrt3\\[2mm]
\text{in its real Lorentz realization, while multiplication by the same unit}\\[2mm]
\text{on the coefficient lattice }\mathbf Z[\sqrt3]\text{ reduces modulo }2\\[2mm]
\text{to the coordinate swap }P,\text{ which is conjugate to the ramified transvection.}
\end{array}
}
\]

This gives a rigorous bridge between the real Cone return and the finite Boolean/ramified action.

It should **not** be strengthened to claim that the continuous fractional mesh phases themselves canonically reduce to the ramified quotient.

---

## 12. Next controlled question

The next useful calculation is to place the ideal

\[
\mathfrak p_2=(1+\sqrt3)
\]

explicitly inside the `(1,sqrt(3))` coefficient lattice and compare:

1. multiplication by `lambda` on `O_F`;
2. multiplication by `lambda` on the ideal basis of `p_2`;
3. the quotient `p_2/2p_2`;
4. the previously established transvection matrix `gbar`.

This should tell us whether the conjugating map `Phi` arises naturally from the change of basis between the ambient Pell coefficient lattice and the ramified ideal lattice, rather than being merely an abstract `GL_2(F_2)` conjugacy.
