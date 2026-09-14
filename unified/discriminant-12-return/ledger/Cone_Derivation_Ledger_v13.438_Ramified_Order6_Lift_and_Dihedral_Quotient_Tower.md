# Cone Derivation Ledger v13.438 — Ramified Order-6 Lift and Dihedral Quotient Tower

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after checking the live repository head. `v13.437` had already landed and records the exact ramified residue-field semilinear reduction

\[
\times\zeta_{12}\mapsto \times\omega,
\qquad
\bar\sigma_r\,M_\omega\,\bar\sigma_r^{-1}
=M_{\omega^{\chi_{-3}(r)}},
\]

with

\[
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong C_3\rtimes C_2\cong S_3.
\]

The present entry asks what survives one level *before* passing to the residue field, namely in the full nonreduced mod-2 ring.

## 1. The full ramified mod-2 ring [D]

Let

\[
K=\mathbf Q(\zeta_{12}),
\qquad
\mathcal O_K=\mathbf Z[\zeta_{12}],
\]

and

\[
R:=\mathcal O_K/2\mathcal O_K.
\]

Since

\[
\Phi_{12}(x)=x^4-x^2+1
\equiv x^4+x^2+1=(x^2+x+1)^2\pmod2,
\]

we have

\[
\boxed{
R\cong \mathbf F_2[x]/\bigl((x^2+x+1)^2\bigr).
}
\]

Write

\[
u:=\bar\zeta_{12}\in R,
\qquad
f(x)=x^2+x+1,
\qquad
\eta:=f(u)=u^2+u+1.
\]

Then

\[
\boxed{\eta^2=0,}
\]

and \(\eta\neq0\), because the quotient is by \(f^2\), not by \(f\).

The residue-field quotient is

\[
R/(\eta)\cong\mathbf F_4,
\]

with \(u\mapsto\omega\).

## 2. Exact order of the cyclotomic generator in the nonreduced ring [D]

In characteristic two,

\[
x^3+1=(x+1)(x^2+x+1),
\]

hence in \(R\),

\[
\boxed{
u^3=1+(u+1)\eta.
}
\]

Define

\[
\varepsilon:=(u+1)\eta.
\]

Because \(u+1\) is a unit modulo the local ring with maximal ideal \((\eta)\), one has \(\varepsilon\neq0\). Also

\[
\boxed{\varepsilon^2=0.}
\]

Therefore

\[
\boxed{
u^3=1+\varepsilon\neq1.
}
\]

But

\[
\nu^6=(1+\varepsilon)^2=1
\]

because the characteristic is two and \(\varepsilon^2=0\). Hence

\[
\boxed{\operatorname{ord}_R(u)=6.}
\]

Thus multiplication by the cyclotomic generator has the exact order tower

\[
\boxed{
12\quad\longrightarrow\quad6\quad\longrightarrow\quad3,
}
\]

namely

\[
\times\zeta_{12}\text{ on }\mathcal O_K,
\qquad
\times u\text{ on }R,
\qquad
\times\omega\text{ on }\mathbf F_4.
\]

The first quotient kills the characteristic-zero sign \(-1=\zeta_{12}^6\), while the second kills the nontrivial nilpotent half-turn \(u^3=1+\varepsilon\).

## 3. The missing factor two is a ramification-tangent unipotent [D/I]

The map

\[
\langle u\rangle\cong C_6
\longrightarrow
\langle\omega\rangle\cong C_3
\]

has kernel

\[
\boxed{
\{1,u^3\}=\{1,1+\varepsilon\}\cong C_2.
}
\]

Since

\[
(1+\varepsilon)^2=1,
\qquad
\varepsilon^2=0,
\]

this kernel is represented by a nontrivial unipotent element supported entirely in the square-zero ramification ideal.

**[I]** The extra factor two retained by the full mod-2 ring, but lost in the residue field, is therefore literally carried by the first-order ramification tangent.

**[Audit]** This is an algebraic tangent/nilpotent statement only. No identification is made with Cone shell displacement, geometric tangent bundles, or Suzuki fluctuation spaces.

## 4. Explicit coefficient-field splitting [D]

Set

\[
w:=u+\eta.
\]

Then, using \(\eta^2=0\),

\[
\boxed{w^2+w+1=0.}
\]

Hence \(w\) generates an embedded coefficient field

\[
\mathbf F_4=\mathbf F_2(w)\subset R.
\]

Moreover

\[
u=w+\eta,
\]

and

\[
\boxed{
R\cong\mathbf F_4[\eta]/(\eta^2)
}
\]

as rings.

Relative to the \(\mathbf F_4\)-module decomposition

\[
R=\mathbf F_4\oplus\eta\mathbf F_4,
\]

multiplication by \(u=w+\eta\) acts as

\[
\boxed{
[M_u]_{\mathbf F_4}
=
\begin{pmatrix}
w&0\\
1&w
\end{pmatrix}.
}
\]

Thus the ramified lift of \(M_\omega\) is a size-two Jordan-type extension over \(\mathbf F_4\): its semisimple part is multiplication by \(w\), while the nilpotent off-diagonal term records the ramification layer.

Cubing gives a nontrivial unipotent operator, and sixth power gives identity, in agreement with the direct order calculation above.

## 5. Galois collapse already occurs on the full mod-2 ring [D]

For \(r\in U(12)=\{1,5,7,11\}\), the characteristic-zero Galois action is

\[
\sigma_r(\zeta_{12})=\zeta_{12}^r.
\]

Since \(u^6=1\) in \(R\), the exponent only survives modulo 6. Therefore

\[
1\equiv7\pmod6,
\qquad
5\equiv11\equiv-1\pmod6.
\]

Hence the four Galois automorphisms collapse in pairs:

\[
\boxed{
\bar\sigma_1=\bar\sigma_7,
\qquad
\bar\sigma_5=\bar\sigma_{11}
}
\]

as automorphisms of \(R\), with

\[
\boxed{
\bar\sigma_1(u)=u,
\qquad
\bar\sigma_5(u)=u^{-1}.
}
\]

Thus already on the nonreduced ring the surviving Galois quotient is

\[
\boxed{
U(12)\twoheadrightarrow C_2
}
\]

with kernel \(\{1,7\}\), i.e. the \(\chi_{-3}\) quotient.

So the nilpotent thickening restores an extra factor in the **multiplication order**, but it does **not** restore the lost \(\chi_{-4}\) or \(\chi_{12}\) Galois distinctions.

## 6. Exact semilinear relation on the ramified ring [D]

Let \(\tau\) denote the nontrivial surviving Galois involution on \(R\):

\[
\tau(u)=u^{-1}.
\]

Then

\[
\boxed{
\tau M_u\tau^{-1}=M_{u^{-1}}=M_u^{-1}.
}
\]

Since

\[
M_u^6=I,
\qquad
\tau^2=I,
\]

and \(\tau\notin\langle M_u\rangle\), the generated group is

\[
\boxed{
\langle M_u,\tau\rangle
\cong C_6\rtimes C_2,
}
\]

where the nontrivial \(C_2\) acts by inversion. This is the dihedral group of order 12.

Reduction modulo \((\eta)\) sends

\[
M_u\mapsto M_\omega,
\qquad
\tau\mapsto\mathrm{Fr},
\]

and yields

\[
\boxed{
C_6\rtimes C_2
\twoheadrightarrow
C_3\rtimes C_2
\cong S_3.
}
\]

The kernel is the central involution

\[
\boxed{
\langle M_u^3\rangle
=
\langle M_{1+\varepsilon}\rangle
\cong C_2.
}
\]

## 7. Cyclotomic dihedral quotient tower [D/Audit]

In characteristic zero, complex conjugation \(\sigma_{11}\) satisfies

\[
\sigma_{11}M_{\zeta}\sigma_{11}^{-1}=M_{\zeta^{-1}}.
\]

Thus

\[
\langle M_\zeta,\sigma_{11}\rangle
\cong C_{12}\rtimes C_2,
\]

a dihedral group of order 24.

Combining characteristic-zero, full mod-2, and residue-field levels gives the exact quotient tower

\[
\boxed{
C_{12}\rtimes C_2
\twoheadrightarrow
C_6\rtimes C_2
\twoheadrightarrow
C_3\rtimes C_2\cong S_3.
}
\]

Equivalently, in group orders,

\[
\boxed{24\longrightarrow12\longrightarrow6.}
\]

The rotational kernels are successively

\[
\boxed{
\langle\zeta_{12}^6\rangle=\{\pm1\}
}
\]

and

\[
\boxed{
\langle u^3\rangle=\{1,1+\varepsilon\}.
}
\]

Both are central involutions in their respective dihedral groups.

**[Audit]** The characteristic-zero group here is the cyclotomic dihedral group generated by multiplication by \(\zeta_{12}\) and complex conjugation. It must not be identified with the Pell dihedral group from `v13.414`, even though both have order 24 and both admit inversion relations.

## 8. Relation to the prior character splitting [D/I]

The project now has three exact character/cyclotomic layers:

1. Over \(\mathbf Q\), the full \(V_4\) Galois representation splits into the four character lines
   \[
   1,\quad\chi_{-4},\quad\chi_{-3},\quad\chi_{12}.
   \]

2. In the full nonreduced mod-2 ring \(R\), the Galois action collapses to the \(\chi_{-3}\) quotient, but cyclotomic multiplication still has order 6 because of the square-zero ramification layer.

3. In the residue field \(\mathbf F_4\), the same \(\chi_{-3}\) Galois quotient survives, while cyclotomic multiplication drops further to order 3.

Thus

\[
\boxed{
\text{Galois information: }V_4\to C_2\to C_2,
}
\]

while independently

\[
\boxed{
\text{cyclotomic multiplication clock: }C_{12}\to C_6\to C_3.
}
\]

The square-zero ramification layer affects the second chain but not the first.

## 9. Structural conclusion [D/I]

The ramified reduction is therefore more informative than the residue field alone:

\[
\boxed{
\mathcal O_K
\longrightarrow
\mathcal O_K/2\mathcal O_K
\longrightarrow
\mathcal O_K/\mathfrak P_2
}
\]

carries the exact cyclotomic order sequence

\[
\boxed{12\to6\to3.}
\]

The intermediate factor two is represented by the nilpotent unipotent

\[
\boxed{u^3=1+\varepsilon,\qquad \varepsilon^2=0.}
\]

Adjoining the surviving inversion involution gives the exact semilinear/dihedral quotient tower

\[
\boxed{
C_{12}\rtimes C_2
\twoheadrightarrow
C_6\rtimes C_2
\twoheadrightarrow
C_3\rtimes C_2\cong S_3.
}
\]

This provides a precise algebraic meaning for the ramified tangent layer: it stores one otherwise-lost binary stage of the cyclotomic return while the Galois quotient has already collapsed to the \(\chi_{-3}\) orientation channel.

---

**Checkpoint conclusion.** The full mod-2 cyclotomic ring is not merely a technical precursor to \(\mathbf F_4\). Its square-zero ramification layer carries an exact order-two unipotent half-turn, lifting the residue-field order-3 multiplication to order 6. Consequently the cyclotomic return descends through the exact clock tower \(12\to6\to3\), and the corresponding inversion extensions descend through dihedral groups of orders \(24\to12\to6\). The Galois information, by contrast, has already collapsed to the \(\chi_{-3}\) quotient at the full mod-2 stage.