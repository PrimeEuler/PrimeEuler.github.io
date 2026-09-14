# Cone Derivation Ledger v13.442 — Prime-2 Tangent V4 and S3 Automorphism Bridge

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before writing. The newest numbered entry was `v13.441` (`Pell Mod-3 Ramified Tangent Phase and F4 Unit Intertwiner`), so `v13.442` was free.

The relevant predecessors are:

- `v13.438`: \(\mathcal O_{K_{12}}/2\cong \mathbf F_4[\eta]/(\eta^2)\), with cyclotomic order collapse \(12\to6\to3\);
- `v13.439-v13.440`: common Pell/cyclotomic \(S_3\) quotient and the mod-3 radical/three-phase decomposition;
- `v13.441`: exact ramified prime-3 tangent phase and \(S_3\)-equivariant intertwiner to \(\mathbf F_4^\times\).

This entry identifies the full prime-2 tangent unit subgroup as a canonical Klein four group and shows that the same residue semilinear \(S_3\) is exactly its full automorphism group.

## 1. Full prime-2 unit group [D]

Let

\[
R_2:=\mathcal O_{K_{12}}/2\mathcal O_{K_{12}}
\cong \mathbf F_4[\eta]/(\eta^2),
\qquad \eta^2=0.
\]

Every unit has a unique factorization

\[
 a+b\eta
 =a\left(1+\frac ba\eta\right),
 \qquad a\in\mathbf F_4^\times,\ b\in\mathbf F_4.
\]

Hence

\[
\boxed{
R_2^\times
\cong
\mathbf F_4^\times\times(1+\eta\mathbf F_4).
}
\]

Because \(R_2\) is commutative, this is a direct product of groups.

The residue factor is

\[
\mathbf F_4^\times\cong C_3.
\]

For the tangent factor,

\[
(1+s\eta)(1+t\eta)
=1+(s+t)\eta
\]

because \(\eta^2=0\). Therefore

\[
\boxed{
1+\eta\mathbf F_4
\cong
(\mathbf F_4,+)
\cong
C_2\times C_2
\cong V_4.
}
\]

Thus

\[
\boxed{
R_2^\times\cong C_3\times V_4,
\qquad |R_2^\times|=12.
}
\]

This is an exact group decomposition internal to the ramified mod-2 cyclotomic ring.

## 2. Exact order-6 factorization of the reduced cyclotomic generator [D]

Use the coefficient-field generator from `v13.438`:

\[
 w:=u+\eta\in\mathbf F_4,
 \qquad
 w^2+w+1=0,
 \qquad
 w^3=1,
\]

where

\[
 u=\bar\zeta_{12}\in R_2.
\]

Since

\[
 u=w+\eta,
\]

we may factor

\[
 u=w\left(1+w^{-1}\eta\right)
 =w(1+w^2\eta).
\]

Define

\[
 h:=1+w^2\eta.
\]

Then

\[
 h^2=1
\]

and \(h\neq1\). Hence \(h\) has order two. Since the ring is commutative,

\[
 wh=hw.
\]

Therefore

\[
\boxed{
 u=wh,
 \qquad
 \operatorname{ord}(w)=3,
 \qquad
 \operatorname{ord}(h)=2,
 \qquad
 \operatorname{ord}(u)=6.
}
\]

Moreover,

\[
 u^3=w^3h^3=h,
\]

so

\[
\boxed{u^3=1+w^2\eta.}
\]

This is the same nontrivial tangent involution previously written as \(1+\varepsilon\). Indeed

\[
(u+1)\eta=(w+1)\eta=w^2\eta.
\]

Hence the mod-2 cyclotomic six-clock splits exactly into

\[
\boxed{
\text{residue }C_3\text{ phase}\times\text{one tangent }C_2\text{ half-turn}.
}
\]

## 3. The tangent Klein four group [D]

Write

\[
T_2:=1+\eta\mathbf F_4.
\]

Its four elements are

\[
\boxed{
T_2=
\{1,\ 1+\eta,\ 1+w\eta,\ 1+w^2\eta\}.
}
\]

Every nonidentity element has order two. Thus this is a canonical Klein four subgroup of \(R_2^\times\).

The three nontrivial tangent states are naturally indexed by \(\mathbf F_4^\times\):

\[
\boxed{
\tau_j:=1+\eta w^j,
\qquad j\in\mathbf F_3.
}
\]

These are the three nonidentity elements of \(T_2\).

## 4. Automorphisms of the ramified ring [D]

Every \(\mathbf F_2\)-algebra automorphism of

\[
R_2=\mathbf F_4[\eta]/(\eta^2)
\]

must preserve the unique maximal ideal

\[
(\eta)=\eta\mathbf F_4
\]

and induces an automorphism of the residue field \(\mathbf F_4\). Thus the residue action is either identity or Frobenius.

After choosing the canonical coefficient field \(\mathbf F_4\subset R_2\), an automorphism has the form

\[
\boxed{
\phi_{a,\sigma}(x+t\eta)
=
\sigma(x)+a\,\sigma(t)\eta,
}
\]

where

\[
 a\in\mathbf F_4^\times,
 \qquad
 \sigma\in\operatorname{Gal}(\mathbf F_4/\mathbf F_2)=\{1,\mathrm{Fr}\}.
\]

Composition gives

\[
(a,\sigma)(b,\tau)
=
(a\,\sigma(b),\sigma\tau).
\]

Therefore

\[
\boxed{
\operatorname{Aut}_{\mathbf F_2}(R_2)
\cong
\mathbf F_4^\times\rtimes
\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong
C_3\rtimes C_2
\cong S_3.
}
\]

The Frobenius acts on \(\mathbf F_4^\times\) by inversion, giving the nontrivial semidirect product.

## 5. The same S3 is Aut(V4) [D]

The tangent group

\[
T_2\cong(\mathbf F_4,+)
\]

is a two-dimensional vector space over \(\mathbf F_2\). The automorphism \(\phi_{a,\sigma}\) acts on tangent coefficients by

\[
\boxed{
t\longmapsto a\,\sigma(t).
}
\]

This realizes every invertible \(\mathbf F_2\)-linear map of \(\mathbf F_4\). Consequently

\[
\boxed{
\operatorname{Aut}_{\mathbf F_2}(R_2)
\xrightarrow{\sim}
GL_2(\mathbf F_2)
\cong
\operatorname{Aut}(T_2)
\cong
\operatorname{Aut}(V_4)
\cong S_3.
}
\]

Thus the residue semilinear \(S_3\) found in `v13.437` is simultaneously the full automorphism group of the prime-2 ramification tangent Klein four group.

This is an exact structural bridge:

\[
\boxed{
\text{prime-2 ramification tangent }V_4
\quad\text{has symmetry}\quad
S_3.
}
\]

## 6. Three nontrivial tangent states carry the same phase action [D]

Consider the two automorphisms

\[
A:=\phi_{w,1},
\qquad
F:=\phi_{1,\mathrm{Fr}}.
\]

On tangent coefficients,

\[
A:t\mapsto wt,
\]

while

\[
F:t\mapsto t^2.
\]

Therefore on

\[
\tau_j=1+\eta w^j
\]

we have

\[
\boxed{A:\tau_j\mapsto\tau_{j+1}}
\]

and

\[
\boxed{F:\tau_j\mapsto\tau_{-j}.}
\]

Hence the three nonidentity tangent states carry exactly the affine phase action

\[
\boxed{
 j\mapsto j+1,
 \qquad
 j\mapsto-j,
}
\]

already obtained for:

1. the Pell projectivized local units at the ramified prime 3;
2. the residue multiplicative shell \(\mathbf F_4^\times\).

Thus there are now three exact three-state realizations of the same \(S_3\)-phase:

\[
\boxed{
(\mathcal O_{\mathbf Q(\sqrt3)}/3)^\times/\mathbf F_3^\times
\ \longleftrightarrow\ 
\mathbf F_4^\times
\ \longleftrightarrow\ 
T_2\setminus\{1\}.
}
\]

## 7. Explicit second intertwiner [D]

Using the phase coordinate \(j\in\mathbf F_3\), define

\[
\boxed{
\Xi:\mathbf F_4^\times\longrightarrow T_2\setminus\{1\},
\qquad
\Xi(w^j)=1+\eta w^j.
}
\]

Then

\[
\boxed{
\Xi\circ M_w=A\circ\Xi,
}
\]

and

\[
\boxed{
\Xi\circ\mathrm{Fr}=F\circ\Xi.
}
\]

Combining with `v13.441` gives the explicit equivariant chain

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\xrightarrow{\ \Psi\ }
\mathbf F_4^\times
\xrightarrow{\ \Xi\ }
T_2\setminus\{1\}.
}
\]

All three carriers are three-element \(S_3\)-sets, and both arrows are exact equivariant bijections.

## 8. Relation to the project U(12) = V4 labels [D/I/Audit]

The project also carries the abstract unit group

\[
U(12)=\{1,5,7,11\}\cong V_4.
\]

Since

\[
T_2\cong V_4,
\]

there exist group isomorphisms

\[
U(12)\xrightarrow{\sim}T_2.
\]

However there is no canonical identification supplied by the current arithmetic data. In fact, the set of such identifications is acted on simply transitively by

\[
\operatorname{Aut}(V_4)\cong S_3.
\]

So the ambiguity of labeling the three nonidentity tangent states by \(5,7,11\) is itself controlled by the same \(S_3\) symmetry.

This gives a precise guardrail:

\[
\boxed{
U(12)\cong T_2\text{ abstractly, but no preferred }5/7/11\text{ assignment has been proved.}
}
\]

Any chosen identification differs from another by the canonical \(S_3=\operatorname{Aut}(V_4)\) action.

## 9. Two-prime synthesis [I]

The finite discriminant-12 structure can now be organized as follows.

At the ramified prime 3:

\[
\mathcal O_{\mathbf Q(\sqrt3)}/3
\cong
\mathbf F_3[\epsilon]/(\epsilon^2),
\]

and projectivized local units give

\[
C_3
\]

with inversion extension \(S_3\).

At the ramified prime 2:

\[
\mathcal O_{K_{12}}/2
\cong
\mathbf F_4[\eta]/(\eta^2),
\]

whose unit group splits as

\[
\boxed{C_3\times V_4.}
\]

The \(C_3\) residue factor carries the same three-phase identified with the prime-3 Pell tangent phase, while the \(V_4\) factor is the prime-2 nilpotent tangent subgroup. The full automorphism group of that tangent \(V_4\) is precisely the same

\[
\boxed{S_3}
\]

that acts on the three-phase carriers.

Thus the prime-2 ring packages both a three-state phase and a four-state tangent group in one exact local object:

\[
\boxed{
R_2^\times\cong C_3\times V_4,
\qquad
\operatorname{Aut}(V_4)\cong S_3.
}
\]

## 10. Guardrails [Audit]

- The tangent Klein four group \(T_2\) is an internal subgroup of the ramified mod-2 unit group; it is not automatically the same labeled object as \(U(12)\).
- No canonical assignment of \(5,7,11\) to \(1+\eta,1+w\eta,1+w^2\eta\) is asserted.
- The internal multiplication group \(R_2^\times\cong C_3\times V_4\) is abelian. The \(S_3\) appears as an automorphism/semilinear symmetry group, not as a subgroup produced by conjugation inside this abelian unit group.
- The automorphism \(A:\eta\mapsto w\eta\) is a ring automorphism of the ramified dual-number ring; it is distinct from multiplication by \(w\) on ring elements.
- The prime-3 nilpotent \(\epsilon\) and prime-2 nilpotent \(\eta\) remain different local objects.
- No identification is made here with geometric shell adjacency, Suzuki operator blocks, or a theorem-level positivity mechanism.

## 11. Structural conclusion [D/I]

The finite arithmetic architecture now contains an exact nested pattern:

\[
\boxed{
\begin{array}{c}
T_2=1+\eta\mathbf F_4\cong V_4\\[2mm]
\operatorname{Aut}(T_2)\cong S_3\\[2mm]
T_2\setminus\{1\}\cong \mathbf F_4^\times\cong C_3
\end{array}
}
\]

where the bottom three-element sets carry the standard \(S_3\cong\operatorname{AGL}_1(\mathbf F_3)\) action.

Combined with `v13.441`, the common phase chain is

\[
\boxed{
(\mathcal O_{\mathbf Q(\sqrt3)}/3)^\times/\mathbf F_3^\times
\cong_{S_3}
\mathbf F_4^\times
\cong_{S_3}
(1+\eta\mathbf F_4)\setminus\{1\}.
}
\]

This is exact. The prime-3 Pell tangent, the prime-2 residue phase, and the three nontrivial states of the prime-2 tangent Klein four group are three realizations of the same finite \(S_3\)-phase structure.
