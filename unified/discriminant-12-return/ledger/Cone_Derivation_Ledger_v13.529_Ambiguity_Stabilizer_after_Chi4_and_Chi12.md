# Cone Derivation Ledger v13.529 — Ambiguity Stabilizer after the chi_-4 and chi_12 Constraints

## Status

**Exact finite linear algebra.** This checkpoint computes the residual ambiguity in the explicit `U(24) <-> character dual <-> cone C_2^3` intertwiner.

A numbering note is necessary: an independent External Audit Round 43 had already used ledger number v13.528 before the exploratory v13.528 cone-intertwiner commit landed. This checkpoint therefore advances this branch to v13.529. The duplicate-numbered exploratory file should be treated as the immediate precursor by commit identity, not as a claim of globally unique numbering.

The main conclusion is:

\[
\boxed{\chi_{-3}\leftrightarrow R_X\text{ is forced once }\chi_{-4}\leftrightarrow R_Y\text{ and }\chi_{12}\leftrightarrow R_XR_Y\text{ are imposed},}
\]

but

\[
\boxed{\sigma\leftrightarrow S_T\text{ is not forced by those constraints alone}.}
\]

A residual Klein-four ambiguity remains:

\[
\boxed{\sigma\mapsto S_T,\ R_XS_T,\ R_YS_T,\ R_XR_YS_T.}
\]

It disappears only after one adds the extra geometric requirement that arithmetic sign act as **pure sheet reversal**, i.e. fix the complex coordinate `z` pointwise and reverse `T`.

---

## 1. Coordinates

Use the character basis

\[
e_1=\chi_{-3}=100,\qquad
e_2=\chi_{-4}=010,\qquad
e_3=\sigma=001.
\]

Then

\[
\chi_{12}=e_1+e_2=110.
\]

Use the cone-symmetry basis

\[
f_1=R_X,\qquad f_2=R_Y,\qquad f_3=S_T.
\]

Thus

\[
G_{\rm cone}=\langle f_1,f_2,f_3\rangle\cong\mathbf F_2^3.
\]

An isomorphism from the character group to the cone group is an invertible linear map

\[
L:\mathbf F_2^3\to\mathbf F_2^3,
\]

so the unrestricted ambiguity is

\[
GL_3(\mathbf F_2),\qquad |GL_3(\mathbf F_2)|=(8-1)(8-2)(8-4)=168.
\]

---

## 2. Fixing chi_-4 <-> R_Y

The compatible complex/cyclotomic identification gives the constraint

\[
L(e_2)=f_2.
\]

`GL_3(F_2)` acts transitively on the seven nonzero vectors, so the stabilizer of one nonzero vector has order

\[
\frac{168}{7}=24.
\]

Therefore fixing only

\[
\chi_{-4}\leftrightarrow R_Y
\]

leaves a 24-element ambiguity subgroup

\[
\boxed{\operatorname{Stab}_{GL_3(2)}(e_2)\text{ of order }24.}
\]

Abstractly this stabilizer is the affine group on the quotient/complement plane,

\[
\operatorname{Stab}(e_2)\cong \mathbf F_2^2\rtimes GL_2(\mathbf F_2)
\cong AGL_2(\mathbf F_2)\cong S_4.
\]

Thus the proven complex leg alone does not determine the full intertwiner.

---

## 3. Imposing the chi_12 / 11 half-turn compatibility

Independently established arithmetic facts single out

\[
\chi_{12}=\chi_{-3}\chi_{-4}=e_1+e_2
\]

as the Pell time-orientation character:

\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
\]

The tetrahedral/A3 representation independently associates the carrier element `11` and the `chi_12` axis with

\[
D_{11}=\operatorname{diag}(-1,-1,+1),
\]

a 180-degree rotation about the `chi_12` axis.

On each fixed-`T` cone circle the intrinsic 180-degree rotation is

\[
R_XR_Y:(z,T)\mapsto(-z,T).
\]

To compare the two representations we now impose the explicit cross-representation compatibility condition

\[
\boxed{L(\chi_{12})=L(e_1+e_2)=f_1+f_2=R_XR_Y.}
\]

This is the precise extra assumption being imposed. The Pell orientation and tetrahedral half-turn single out `chi_12/11` arithmetically; identifying that selected half-turn with the cone's fixed-sheet half-turn is the representation-matching condition. Neither the Pell law alone nor the A3 matrix alone is claimed to manufacture a cone action.

Since already

\[
L(e_2)=f_2,
\]

linearity immediately gives

\[
L(e_1)
=L(e_1+e_2)+L(e_2)
=(f_1+f_2)+f_2
=f_1.
\]

Hence

\[
\boxed{L(\chi_{-3})=R_X.}
\]

So **chi_-3 <-> R_X is forced** once the two displayed constraints are imposed.

---

## 4. Residual ambiguity after fixing the mod-12 plane

At this stage both basis vectors of the original mod-12 character plane are fixed pointwise:

\[
L(e_1)=f_1,\qquad L(e_2)=f_2.
\]

For `L` to remain invertible, the remaining vector `e_3=sigma` must map outside

\[
\operatorname{span}\{f_1,f_2\}.
\]

There are exactly four such vectors:

\[
f_3,\qquad f_1+f_3,\qquad f_2+f_3,\qquad f_1+f_2+f_3.
\]

Therefore

\[
\boxed{
L(\sigma)\in
\{S_T,\ R_XS_T,\ R_YS_T,\ R_XR_YS_T\}.
}
\]

The residual ambiguity group consists of the four automorphisms

\[
A_{\alpha,\beta}:
\begin{cases}
f_1\mapsto f_1,\\
f_2\mapsto f_2,\\
f_3\mapsto f_3+\alpha f_1+\beta f_2,
\end{cases}
\qquad \alpha,\beta\in\mathbf F_2.
\]

They satisfy

\[
A_{\alpha,\beta}A_{\alpha',\beta'}
=A_{\alpha+\alpha',\beta+\beta'},
\]

so

\[
\boxed{
\operatorname{Stab}_{GL_3(2)}(f_1,f_2)
\cong C_2^2=V_4.
}
\]

Counting agrees with the orbit calculation: fixing an ordered independent pair leaves four possible images for a third basis vector.

Thus the ambiguity reduction is

\[
\boxed{168\ \longrightarrow\ 24\ \longrightarrow\ 4.}
\]

The first reduction fixes `chi_-4 <-> R_Y`; the second additionally fixes `chi_12 <-> R_XR_Y` and consequently `chi_-3 <-> R_X`.

---

## 5. Why sigma <-> S_T is not yet forced

All four residual candidates reverse the sheet because each contains `S_T`:

\[
S_T,\quad R_XS_T,\quad R_YS_T,\quad R_XR_YS_T.
\]

But they differ by a fixed-sheet symmetry of the complex coordinate:

\[
\begin{array}{c|c}
L(\sigma)&(z,T)\mapsto\\ \hline
S_T&(z,-T)\\
R_XS_T&(-\bar z,-T)\\
R_YS_T&(\bar z,-T)\\
R_XR_YS_T&(-z,-T).
\end{array}
\]

Neither the `chi_-4` complex-conjugation constraint nor the `chi_12/11` fixed-sheet half-turn constraint distinguishes these four possibilities, because they already fix the entire mod-12 plane and differ only in how the extra signed direction is lifted over it.

Therefore

\[
\boxed{\sigma\leftrightarrow S_T\text{ is not forced by the stated arithmetic/Pell/A3 constraints alone}.}
\]

---

## 6. The extra condition that does force sigma -> S_T

There is, however, a natural geometric normalization available.

Define **pure sheet reversal** to mean the unique nontrivial cone symmetry in the displayed `C_2^3` that

1. reverses `T`, and
2. fixes the complex transverse coordinate `z=X+iY` pointwise.

Among the four residual candidates, only

\[
S_T:(z,T)\mapsto(z,-T)
\]

has this property.

Thus, if the arithmetic sign bit `sigma` is required by definition/convention to encode pure upper/lower sheet sign with no simultaneous factor-exchange or complex-conjugation action, then

\[
\boxed{L(\sigma)=S_T}
\]

is forced and the residual `V_4` ambiguity collapses to the identity.

Under that additional normalization the full intertwiner is uniquely

\[
\boxed{
\chi_{-3}\mapsto R_X,
\qquad
\chi_{-4}\mapsto R_Y,
\qquad
\sigma\mapsto S_T.
}
\]

Equivalently,

\[
\boxed{
5^a7^b(-1)^c\mapsto R_X^aR_Y^bS_T^c.
}
\]

The logical status must remain explicit: the first assignment is forced after the `chi_12/11` cone-half-turn compatibility is imposed; the third is forced only after the additional **pure-sheet-sign normalization** is imposed.

---

## 7. Relation to the QR deck direction

The QR deck vector is

\[
K=111=e_1+e_2+e_3=\chi_{12}+\sigma
\]

under the chosen carrier/dual coordinates.

Before pure-sheet normalization, if

\[
L(\sigma)=f_3+\alpha f_1+\beta f_2,
\]

then

\[
L(K)
=(f_1+f_2)+(f_3+\alpha f_1+\beta f_2)
=f_3+(1+\alpha)f_1+(1+\beta)f_2.
\]

Therefore the statement

\[
K\mapsto R_XR_YS_T
\]

is **equivalent**, once `chi_12 -> R_XR_Y` is fixed, to

\[
\sigma\mapsto S_T.
\]

So the earlier identification of the QR deck involution with the full cone antipode cannot be used as independent evidence to force pure sheet sign unless an independent QR-to-cone argument for the antipode is supplied. Otherwise the reasoning would be circular.

This is the exact guardrail.

---

## 8. Conclusion

The canonicity audit gives the exact hierarchy

\[
\boxed{
GL_3(2)\ (168)
\supset
\operatorname{Stab}(\chi_{-4})\ (24)
\supset
\operatorname{Stab}(\chi_{-4},\chi_{12})\ (4)
\supset
\{1\}
}
\]

where the last step requires pure-sheet normalization.

Thus:

\[
\boxed{\chi_{-4}\leftrightarrow R_Y}
\]

is fixed by the compatible cone/cyclotomic complex structure;

\[
\boxed{\chi_{12}\leftrightarrow R_XR_Y}
\]

is an imposed compatibility between the independently selected Pell/A3 `chi_12/11` half-turn and the intrinsic cone half-turn;

then

\[
\boxed{\chi_{-3}\leftrightarrow R_X}
\]

is forced algebraically;

but

\[
\boxed{\sigma\leftrightarrow S_T}
\]

still has a fourfold ambiguity until arithmetic sign is required to be pure sheet reversal.

This separates what is canonical, what is forced after a representation-matching condition, and what remains a normalization choice.