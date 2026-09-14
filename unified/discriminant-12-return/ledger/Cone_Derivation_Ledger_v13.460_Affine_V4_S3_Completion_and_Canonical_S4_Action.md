# Cone Derivation Ledger v13.460 — Affine V4-S3 Completion and Canonical S4 Action

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this write. The newest numbered entry was `v13.459`, so `v13.460` was free.

Relevant predecessors:

- `v13.442`: prime-2 tangent Klein four `T_2=1+eta F_4` and `Aut(T_2)≅S_3`;
- `v13.444`: canonical self-duality of every Klein four group and canonical Hadamard/Fourier structure;
- `v13.454`: intrinsic discriminant-12 `S_3` quotient from the two ramified primes;
- `v13.457`: associated-graded ramified tower `S_3` phases;
- `v13.458`: recovery of the full mod-4 `V_4` character data from quotient plus first-order derivation bit.

The present checkpoint tests whether the intrinsic `V_4` and intrinsic `S_3` structures combine into a canonical four-state affine symmetry.

## 1. Tangent Klein four as an affine plane [D]

Let

\[
T_2=1+\eta\mathbf F_4
\]

inside

\[
R_2=\mathbf F_4[\eta]/(\eta^2).
\]

Multiplication in the tangent subgroup is

\[
(1+\eta s)(1+\eta t)=1+\eta(s+t),
\]

so

\[
\boxed{T_2\cong(\mathbf F_4,+)\cong\mathbf F_2^2\cong V_4.}
\]

Use the additive coefficient coordinate

\[
1+\eta t\longleftrightarrow t\in\mathbf F_4.
\]

Thus the four tangent states are

\[
\boxed{\{0,1,w,w^2\}}
\]

in coefficient form, where

\[
w^2+w+1=0.
\]

## 2. Translation subgroup [D]

For every `a∈F_4`, define

\[
T_a(t)=t+a.
\]

Then

\[
T_aT_b=T_{a+b},
\]

so

\[
\boxed{\mathcal T:=\{T_a:a\in\mathbf F_4\}\cong(\mathbf F_4,+)\cong V_4.}
\]

This action is regular on the four tangent points.

The three nontrivial translations have permutation form

\[
T_1=(0\ 1)(w\ w^2),
\]

\[
T_w=(0\ w)(1\ w^2),
\]

\[
T_{w^2}=(0\ w^2)(1\ w).
\]

Thus the normal Klein four inside the four-point permutation group is realized exactly by the tangent translations.

## 3. Linear `S_3` from the discriminant-12 local phase [D]

From `v13.442`, the `F_2`-algebra automorphisms of `R_2` act on tangent coefficients as

\[
t\mapsto a\,\sigma(t),
\]

with

\[
a\in\mathbf F_4^\times,
\qquad
\sigma\in\operatorname{Gal}(\mathbf F_4/\mathbf F_2).
\]

Hence

\[
\operatorname{Aut}_{\mathbf F_2}(R_2)
\cong
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong
C_3\rtimes C_2
\cong S_3.
\]

Define the standard generators

\[
A(t)=wt,
\]

and

\[
F(t)=t^2.
\]

Then

\[
A^3=F^2=1,
\qquad
FAF=A^{-1}.
\]

Their permutation action on the four tangent points is

\[
\boxed{A=(1\ w\ w^2),\quad 0\text{ fixed},}
\]

and

\[
\boxed{F=(w\ w^2),\quad 0,1\text{ fixed}.}
\]

Therefore

\[
\boxed{\langle A,F\rangle\cong S_3=\operatorname{Aut}(T_2).}
\]

This is the same intrinsic `S_3` phase symmetry forced by discriminant 12 in `v13.454`, realized here as the full automorphism group of the tangent Klein four.

## 4. Affine completion [D]

The linear action conjugates translations by

\[
L T_a L^{-1}=T_{L(a)}
\]

for every

\[
L\in\langle A,F\rangle.
\]

Hence the translations are normal, and the generated affine group is

\[
\boxed{
\mathcal A
=
\mathcal T\rtimes\langle A,F\rangle
\cong
V_4\rtimes S_3.
}
\]

Since

\[
|\mathcal A|=4\cdot6=24,
\]

and it acts faithfully on four points,

\[
\mathcal A\hookrightarrow S_4.
\]

Both groups have order 24, so

\[
\boxed{
\mathcal A
\cong
AGL_2(\mathbf F_2)
\cong
S_4.
}
\]

Thus the four-state tangent carrier has the full affine symmetry group

\[
\boxed{V_4\rtimes\operatorname{Aut}(V_4)\cong S_4.}
\]

## 5. Explicit four-state permutation model [D]

In the ordered point set

\[
\Omega=\{0,1,w,w^2\},
\]

the generators are

\[
\boxed{
T_1=(0\ 1)(w\ w^2),
}
\]

\[
\boxed{
T_w=(0\ w)(1\ w^2),
}
\]

\[
\boxed{
T_{w^2}=(0\ w^2)(1\ w),
}
\]

\[
\boxed{
A=(1\ w\ w^2),
}
\]

\[
\boxed{
F=(w\ w^2).
}
\]

The first three form the normal Klein four. The last two generate the stabilizer of `0`, which is exactly `S_3`.

Hence

\[
\boxed{
S_4=V_4\rtimes S_3
}
\]

appears in its standard four-point affine realization.

## 6. Stabilizer interpretation [D]

The affine group acts transitively on the four tangent states. The stabilizer of the identity state `0` is precisely

\[
\boxed{\operatorname{Stab}(0)=\operatorname{Aut}(T_2)\cong S_3.}
\]

Thus the intrinsic discriminant-12 `S_3` phase can be interpreted as the point stabilizer inside the completed four-state symmetry.

Equivalently,

\[
\boxed{S_4/V_4\cong S_3.}
\]

The quotient by translations remembers only the linear phase symmetry.

## 7. Relation to the three-state phase [D/I]

The three nonzero tangent states

\[
T_2\setminus\{1\}
\leftrightarrow
\mathbf F_4^\times
\]

form the three-state `S_3` carrier from `v13.442` and `v13.454`.

The affine completion adds the distinguished zero/identity state and then permits translations that move that distinguished point.

Therefore the hierarchy is

\[
\boxed{
\text{three nonzero states with }S_3
\quad\subset\quad
\text{four affine states with }S_4.
}
\]

The `S_3` is exactly the stabilizer of the zero state in the `S_4` action.

## 8. Canonical versus noncanonical aspects [Audit]

There are two different statements that must not be conflated.

### 8.1 Canonical tangent completion

The prime-2 tangent group

\[
T_2=1+\eta\mathbf F_4
\]

is an intrinsic arithmetic object, and its full automorphism group is intrinsically

\[
\operatorname{Aut}(T_2)\cong S_3.
\]

Therefore its holomorph/affine completion

\[
\boxed{T_2\rtimes\operatorname{Aut}(T_2)\cong S_4}
\]

is canonical as an abstract permutation group on the underlying four-element set.

### 8.2 No canonical pointwise identification with `U(12)`

Although

\[
U(12)\cong V_4
\]

and

\[
T_2\cong V_4,
\]

there is still no previously established canonical pointwise isomorphism

\[
U(12)\to T_2.
\]

The canonical self-duality of `v13.444` fixes the Fourier structure of each Klein four, but does not by itself choose which of the three nonidentity elements of `U(12)` is which tangent state.

The distinguished `chi_-3` axis reduces this ambiguity to a `C_2` at mod two, while mod four recovers the full character labels through extension data. A direct arithmetic identification of the *Galois V4 itself* with the tangent translation V4 is not asserted here.

Therefore the exact safe statement is

\[
\boxed{
\text{the tangent four-state carrier has canonical affine symmetry }S_4,
}
\]

not

\[
\text{“the mod-12 residue labels themselves canonically form this exact four-point affine set.”}
\]

## 9. Character/Fourier compatibility [D/I]

Every Klein four group carries the canonical alternating pairing from `v13.444`, hence canonical self-duality

\[
V_4\cong\widehat V_4.
\]

The automorphism group `S_3` preserves this pairing. Therefore the affine `S_4` completion acts compatibly with the canonical Fourier/Hadamard structure in the following sense:

- translations act in the regular basis;
- the point stabilizer `S_3=Aut(V_4)` permutes the three nontrivial translation directions;
- under canonical self-duality, the same `S_3` permutes the three nontrivial character directions.

Thus the four-state regular basis and the four-character Hadamard basis carry the same `S_3` permutation symmetry on their three nontrivial sectors.

**[Audit]** This compatibility does not imply that the Hadamard transform itself is an element of the permutation group `S_4`.

## 10. Compact synthesis [D/I]

The discriminant-12 local arithmetic now contains the exact hierarchy

\[
\boxed{
V_4
\triangleleft
S_4
\twoheadrightarrow
S_3,
}
\]

with

\[
\boxed{
S_4
\cong
V_4\rtimes S_3
\cong
AGL_2(\mathbf F_2).
}
\]

On the canonical prime-2 tangent carrier:

\[
\boxed{
\text{translations}=V_4,
\qquad
\text{linear phase}=S_3,
\qquad
\text{full affine symmetry}=S_4.
}
\]

The three-state `S_3` phase is therefore exactly the point stabilizer inside a natural four-state affine completion.

---

**Checkpoint conclusion.** The proposed `V_4\rtimes S_3` completion is exact on the prime-2 ramification tangent carrier. Writing `T_2≅(F_4,+)`, translations by `F_4` form the normal Klein four and the intrinsic semilinear `S_3` acts as its full automorphism group. Together they generate `AGL_2(F_2)`, a faithful order-24 action on four points, hence `S_4`. This gives a precise four-state symmetry completion of the discriminant-12 local phase structure, while preserving the guardrail that no canonical pointwise identification of the tangent translation `V_4` with the separately labeled mod-12 Galois `U(12)` has yet been proved.