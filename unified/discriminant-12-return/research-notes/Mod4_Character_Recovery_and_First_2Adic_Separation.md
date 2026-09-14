# Mod-4 Character Recovery and First 2-Adic Separation

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 1. Starting point

Let

\[
K=\mathbf Q(\zeta_{12})=\mathbf Q(\sqrt3,i),
\qquad
\mathcal O_K=\mathbf Z[\zeta_{12}],
\]

and set

\[
R_4:=\mathcal O_K/4\mathcal O_K,
\qquad
R_2:=\mathcal O_K/2\mathcal O_K.
\]

Write

\[
u:=\bar\zeta_{12}\in R_4.
\]

The preceding mod-2 analysis proved

\[
\bar i=\overline{\sqrt3}
\]

in \(R_2\), so the characteristic-zero character lines \(\chi_{-4}\) and \(\chi_{12}\) cannot be separated on the full mod-2 carrier. The residual labeling symmetry there is a genuine \(C_2\).

This note checks the first deeper 2-adic layer.

## 2. Exact first-order separation [D]

The characteristic-zero identities

\[
\boxed{\sqrt3+i=2\zeta_{12}}
\]

and

\[
\boxed{\sqrt3-i=2\zeta_{12}^{-1}}
\]

are integral identities in \(\mathcal O_K\).

Modulo 2 both right-hand sides vanish, giving

\[
i\equiv\sqrt3\pmod2.
\]

Modulo 4, however, \(2u\) and \(2u^{-1}\) are nonzero because \(u\) is a unit and \(2\neq0\) in \(R_4\). Hence

\[
\boxed{i\not\equiv\sqrt3\pmod4.}
\]

Thus the collapse

\[
\chi_{-4}\leftrightarrow\chi_{12}
\]

is specific to the mod-2 quotient. It is already resolved at the next 2-adic layer.

## 3. Exact order of the cyclotomic generator modulo 4 [D]

Because \(\zeta_{12}^{12}=1\), the order of \(u\) divides 12.

But

\[
u^6=-1,
\]

and

\[
-1\neq1\pmod4.
\]

So the order does not divide 6. Therefore

\[
\boxed{\operatorname{ord}_{R_4}(u)=12.}
\]

This contrasts with the already-audited order tower

\[
12\to6\to3
\]

for characteristic zero \(\to R_2\to\mathbf F_4\). The mod-4 carrier still retains the full order-12 cyclotomic clock.

## 4. Faithful recovery of the four Galois classes [D]

For

\[
r\in U(12)=\{1,5,7,11\},
\]

one has

\[
\sigma_r(u)=u^r.
\]

Since \(u\) has exact order 12 in \(R_4\), the exponents

\[
1,5,7,11\pmod{12}
\]

produce four distinct powers. Hence the reduction of the cyclotomic Galois action to \(R_4\) is faithful:

\[
\boxed{
U(12)\hookrightarrow\operatorname{Aut}(R_4).
}
\]

So the Galois-information chain is

\[
\boxed{
V_4\text{ in characteristic zero}
\longrightarrow
V_4\text{ mod }4
\longrightarrow
C_2\text{ mod }2
\longrightarrow
C_2\text{ on }\mathbf F_4.
}
\]

The loss of the \(\chi_{-4}\) / \(\chi_{12}\) distinction occurs precisely when passing from mod 4 to mod 2.

## 5. The first 2-adic correction module [D]

The reduction map

\[
R_4\twoheadrightarrow R_2
\]

has kernel

\[
2R_4.
\]

Multiplication by 2 induces a natural additive isomorphism

\[
\boxed{
R_2\xrightarrow{\sim}2R_4,
\qquad
\bar x\longmapsto2x\pmod4.
}
\]

Indeed, changing a lift by \(2y\) changes \(2x\) by \(4y=0\), and the kernel is exactly reduction modulo 2.

Under this identification, the two first-order differences are

\[
\boxed{
\sqrt3+i\longleftrightarrow u,
\qquad
\sqrt3-i\longleftrightarrow u^{-1}
}
\]

inside the mod-2 ramified ring.

Thus the first 2-adic correction remembers the oriented pair

\[
\boxed{u\quad\text{vs.}\quad u^{-1}}
\]

that the raw mod-2 equality \(i=\sqrt3\) had erased.

## 6. Surviving action on the correction pair [D]

Modulo 4, for the Galois elements one has

\[
\sigma_r(2u)=2u^r.
\]

Inside the kernel \(2R_4\), signs disappear because

\[
-2\equiv2\pmod4.
\]

Hence:

- \(r=1,7\) preserve the oriented class of \(2u\);
- \(r=5,11\) exchange \(2u\) and \(2u^{-1}\).

Equivalently, the action on the two-element correction pair is again controlled by

\[
\boxed{\chi_{-3}.}
\]

This is compatible with the earlier result that \(\chi_{-3}\) is the surviving mod-2 Galois/Frobenius quotient. The difference is that the ambient mod-4 ring still retains all four Galois automorphisms faithfully.

## 7. Canonical lift of the distinguished tangent half-turn [D/I]

In the mod-2 ring, the distinguished tangent involution is

\[
h=u^3=\bar i=\overline{\sqrt3}.
\]

At mod 4, the cyclotomic generator gives a canonical lift

\[
\boxed{i=u^3.}
\]

The real generator is separately

\[
\boxed{\sqrt3=u+u^{-1}.}
\]

These are unequal mod 4, with

\[
\sqrt3-i=2u^{-1}.
\]

Thus once the fixed primitive root \(\zeta_{12}\) is retained, the deeper 2-adic carrier canonically distinguishes the characteristic-zero \(i\)-direction from the \(\sqrt3\)-direction.

Interpretively, the residual \(C_2\) ambiguity of the pointed mod-2 \(V_4\) bridge is not intrinsic to the full 2-adic tower; it is forced only by truncation at depth one.

## 8. Guardrails [Audit]

1. The equality \(i=\sqrt3\) remains valid in \(R_2\); the present result says only that their chosen lifts separate in \(R_4\).
2. Faithful mod-4 Galois action does not identify the mod-4 ring with the characteristic-zero field.
3. The additive identification \(R_2\cong2R_4\) is a first-order correction-module statement, not a ring isomorphism.
4. The action on the two-element correction pair is still the \(\chi_{-3}\) quotient, even though the ambient mod-4 Galois action is faithful \(V_4\).
5. No geometric Cone-shell or Suzuki-operator identification is inferred.

## 9. Compact synthesis

The character-information filtration at the ramified prime 2 is now

\[
\boxed{
\text{char. 0}: V_4
\quad\to\quad
\text{mod }4: V_4
\quad\to\quad
\text{mod }2: C_2
\quad\to\quad
\mathbf F_4: C_2.
}
\]

The exact obstruction at mod 2 is

\[
\boxed{i\equiv\sqrt3\pmod2,}
\]

while the first deeper correction is

\[
\boxed{
\sqrt3+i=2u,
\qquad
\sqrt3-i=2u^{-1}\pmod4.
}
\]

Hence the unresolved \(\chi_{-4}\leftrightarrow\chi_{12}\) swap of the mod-2 tangent bridge is resolved by the first nontrivial 2-adic lift.