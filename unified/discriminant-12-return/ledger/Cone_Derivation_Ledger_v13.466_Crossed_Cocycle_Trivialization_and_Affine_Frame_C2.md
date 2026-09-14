# Cone Derivation Ledger v13.466 — Crossed Cocycle Trivialization and Affine-Frame C2

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this write. The newest numbered checkpoint was `v13.465` (External Audit Round 34), which independently verified the local arithmetic thread through `v13.462`. Hence `v13.466` was free.

This checkpoint formalizes the twisted mod-4 bridge from `v13.462` using crossed cocycles and determines whether the residual affine-frame ambiguity is represented by a nontrivial cohomology class.

## 1. The raw mod-4 correction table is not a V4 1-cocycle [D]

Let

\[
G=U(12)=\{1,5,7,11\}\cong V_4.
\]

The mod-two action factors through

\[
\chi_{-3}:G\to C_2=\langle\tau\rangle,
\]

where the induced action on the residue coefficient field is Frobenius

\[
\tau(t)=t^2
\qquad(t\in\mathbf F_4).
\]

From `v13.458-v13.462`, the first-order mod-four correction attached to the kernel element `7` appears as

\[
D_7(u)\equiv w,
\]

while in the other quotient coset

\[
D_{11,5}(u)\equiv w^2=\tau(w).
\]

Thus the tempting table

\[
1\mapsto0,\qquad
7\mapsto w,\qquad
5\mapsto0,\qquad
11\mapsto w^2
\]

is **not** a crossed 1-cocycle on the abelian group `G` with this action. Indeed, the cocycle law would give

\[
c(7\cdot5)=c(7)+7\cdot c(5)=w,
\]

but also, since `7*5=5*7`,

\[
c(5\cdot7)=c(5)+5\cdot c(7)=\tau(w)=w^2,
\]

and

\[
w\ne w^2.
\]

Hence the raw lift table is twisted extension data, not an ordinary `H^1(G,M)` cocycle.

## 2. The relative discrepancy is canonical [D]

The two coset corrections differ by

\[
\boxed{
\Delta:=w+w^2.
}
\]

Since

\[
w^2+w+1=0,
\]

we obtain

\[
\boxed{\Delta=1.}
\]

This is Frobenius-fixed:

\[
\tau(1)=1.
\]

Therefore the relative discrepancy descends to the quotient

\[
C_2=G/\ker\chi_{-3}
\]

and defines a genuine crossed cocycle with values in the additive tangent module

\[
M=(\mathbf F_4,+),
\]

namely

\[
\boxed{
c(1)=0,\qquad c(\tau)=1.
}
\]

For `C2`, the only nontrivial cocycle condition is

\[
c(\tau^2)=c(\tau)+\tau c(\tau)=0.
\]

Here

\[
1+\tau(1)=1+1=0,
\]

so the condition is satisfied exactly.

## 3. Computation of H^1(C2,F4) [D]

For the Frobenius action of `C2` on the additive group of `F4`, a 1-cocycle is determined by an element `a=c(tau)` satisfying

\[
a+\tau(a)=0.
\]

Thus

\[
Z^1(C_2,M)=M^{\tau}=\mathbf F_2=\{0,1\}.
\]

A coboundary has the form

\[
\delta b(\tau)=\tau(b)+b.
\]

But the trace map

\[
\operatorname{Tr}_{\mathbf F_4/\mathbf F_2}(b)=b+b^2
\]

is surjective onto `F2`. In particular,

\[
\delta w(\tau)=w^2+w=1,
\]

and likewise

\[
\delta w^2(\tau)=w+w^2=1.
\]

Hence

\[
\boxed{
B^1(C_2,M)=Z^1(C_2,M)=\mathbf F_2
}
\]

and therefore

\[
\boxed{
H^1(C_2,\mathbf F_4)=0.
}
\]

So the crossed cocycle detected by the mod-four relative correction is nonzero as a representative but cohomologically trivial.

## 4. Affine interpretation [D]

The nonzero cocycle representative gives the affine involution

\[
\boxed{
F'(t)=t^2+1.
}
\]

The untwisted Frobenius is

\[
F(t)=t^2.
\]

Let `T_b` denote translation by `b`:

\[
T_b(t)=t+b.
\]

Then, because every translation is its own inverse in characteristic two,

\[
T_wFT_w^{-1}(t)
=t^2+w^2+w
=t^2+1.
\]

Thus

\[
\boxed{
F'=T_wFT_w^{-1}.
}
\]

Equally,

\[
\boxed{
F'=T_{w^2}FT_{w^2}^{-1}.
}
\]

Therefore the mod-four twist changes the affine origin but not the conjugacy class of the intrinsic involution.

## 5. Explicit S4 permutation form [D]

On the four affine points

\[
\mathbf F_4=\{0,1,w,w^2\},
\]

ordinary Frobenius acts as

\[
\boxed{F=(w\;w^2)}
\]

with `0` and `1` fixed.

The twisted affine involution

\[
F'(t)=t^2+1
\]

acts as

\[
\boxed{F'=(0\;1)}
\]

with `w` and `w^2` fixed.

They are conjugate in

\[
AGL_2(\mathbf F_2)\cong S_4
\]

by `T_w` (or by `T_{w^2}`).

Thus the mod-four correction does not leave the canonical affine `S4`; it selects a different affine frame inside the same `S4`.

## 6. Why there are exactly two trivializations [D]

The equation

\[
\delta b(\tau)=1
\]

is

\[
b+b^2=1.
\]

Its solutions are precisely

\[
\boxed{b=w,\quad b=w^2.}
\]

Their difference is

\[
w+w^2=1,
\]

which lies in the invariant subspace

\[
M^\tau=\mathbf F_2.
\]

Hence the two trivializations form a torsor under the nonzero invariant translation

\[
\boxed{T_1.}
\]

This is exactly the residual `C2` affine-frame ambiguity seen previously.

Therefore the residual `C2` is not a nontrivial cohomology class. It is the two-element set of choices that trivialize the unique nonzero cocycle representative.

## 7. Relation to the pointed V4 ambiguity [D/I]

Earlier checkpoints found that after fixing the distinguished axis

\[
7\leftrightarrow\chi_{-3}\leftrightarrow h,
\]

two pointed identifications remained between the Galois `V4` and the tangent `V4`.

The present calculation gives the cohomological meaning of that fact:

\[
\boxed{
\text{residual pointed }C_2
=
\text{two coboundary trivializations }b=w,w^2.
}
\]

Their difference is the invariant translation by `1`.

Thus the ambiguity is an affine-origin choice internal to the canonical `S4` carrier.

## 8. Structural synthesis [I]

The exact hierarchy is now:

1. the mod-two quotient remembers the `chi_-3` semilinear action;
2. the mod-four lift produces two coset-dependent first-order corrections `w` and `w^2`;
3. their canonical relative discrepancy is the fixed element `1`;
4. that discrepancy is a genuine crossed cocycle on the quotient `C2`;
5. the cocycle class vanishes in `H^1(C2,F4)`;
6. its two trivializations are exactly the two residual affine frames;
7. both frames lie inside the same canonical affine group

\[
\boxed{AGL_2(\mathbf F_2)\cong S_4.}
\]

So the right invariant object is not a new nontrivial cohomology class. The invariant arithmetic datum is the **trivializable crossed cocycle together with its two-point trivialization torsor**.

## 9. Guardrails [Audit]

- The raw four-element correction table on `U(12)` is not a 1-cocycle; only the relative discrepancy descends to the quotient `C2` as a crossed cocycle.
- `H^1(C2,F4)=0` does not mean the mod-four correction is zero; it means it can be removed by changing affine origin.
- The two choices `w` and `w^2` are not canonically identified individually by the current arithmetic data.
- No canonical pointwise isomorphism `U(12) -> T2` is promoted here.
- The canonical `S4` affine symmetry from `v13.460` remains exact and unchanged.
- No implication for the Suzuki operator theorem is claimed.

---

**Checkpoint conclusion.** The mod-four twisted bridge has a precise cohomological description. The raw Galois correction is not a `V4` 1-cocycle, but its relative coset discrepancy is the canonical cocycle `c(tau)=1` for Frobenius acting on the additive tangent module `F4`. This cocycle is the coboundary of either `w` or `w^2`, so `H^1(C2,F4)=0`. The two coboundary trivializations differ by the invariant translation `1` and are exactly the residual `C2` of affine-frame choices. Thus the final ambiguity is not a hidden arithmetic obstruction; it is an origin-choice torsor internal to the already canonical affine `S4` symmetry.