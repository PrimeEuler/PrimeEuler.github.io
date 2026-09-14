# Cone Derivation Ledger v13.462 — Mod-4 Twisted-Lift Obstruction to Canonical V4 Translation Identification

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this write. The newest numbered entry was `v13.461` (`High-Precision Small-Cutoff Even Spectrum`), so `v13.462` was free.

Relevant arithmetic predecessors:

- `v13.442`: prime-2 tangent Klein four `T_2=1+eta F_4` and its `S_3=Aut(T_2)` symmetry;
- `v13.444`: canonical V4 self-duality and the distinguished alignment `7 <-> chi_-3 <-> h=u^3`;
- `v13.458`: recovery of the full Galois `V4=U(12)` from the mod-2 `chi_-3` quotient plus first-order mod-4 derivation data;
- `v13.460`: affine completion `T_2 \rtimes Aut(T_2) = AGL_2(F_2) ~= S_4`.

The present checkpoint tests whether the mod-4 lift data canonically identifies the Galois Klein four `U(12)` itself with the tangent-translation Klein four `T_2`.

## 1. The two Klein fours [D]

Let

\[
G:=U(12)=\{1,5,7,11\}\cong V_4.
\]

On the prime-2 tangent side,

\[
T_2=1+\eta\mathbf F_4
\cong (\mathbf F_4,+)
\cong V_4.
\]

Writing

\[
\mathbf F_4=\mathbf F_2(w),\qquad w^2+w+1=0,
\]

the tangent states are

\[
1,\quad 1+\eta,\quad 1+w\eta,\quad 1+w^2\eta.
\]

The distinguished nonidentity tangent state from `v13.442-v13.444` is

\[
\boxed{h=u^3=1+w^2\eta.}
\]

Canonical V4 self-duality on `G` identifies

\[
\boxed{7\longleftrightarrow \chi_{-3}},
\]

and the arithmetic already singles out the pointed alignment

\[
\boxed{7\longleftrightarrow \chi_{-3}\longleftrightarrow h.}
\]

Thus any group isomorphism `G -> T_2` respecting the distinguished point has only two possibilities, differing by the unique nontrivial automorphism of `T_2` fixing `h`.

## 2. Mod-two quotient action [D]

From `v13.458`, reduction of the Galois action to

\[
R_2=\mathcal O_K/2\mathcal O_K
\]

gives

\[
\bar\sigma_1=\bar\sigma_7=\mathrm{id},
\qquad
\bar\sigma_5=\bar\sigma_{11}=:\tau.
\]

Hence

\[
G/\langle7\rangle\cong C_2,
\]

with quotient bit exactly `chi_-3`.

In the coefficient-field splitting

\[
R_2\cong\mathbf F_4[\eta]/(\eta^2),
\]

the surviving arithmetic involution acts on tangent coefficients as

\[
\boxed{\tau(t)=w t^2.}
\]

It fixes `w^2` and exchanges `1` with `w`.

## 3. First-order recovery of the invisible kernel element [D]

Let

\[
R_4=\mathcal O_K/4\mathcal O_K,
\]

and let `nu` be the image of `zeta_12` in `R_4`, with `u` its reduction in `R_2`.

Since `sigma_7` is identity modulo two, define

\[
D_7(\bar x)
:=
\frac{\sigma_7(x)-x}{2}\pmod2.
\]

From `v13.458`,

\[
\boxed{D_7(u)=u.}
\]

Reducing further to the coefficient field `F_4` gives

\[
\boxed{D_7(u)\bmod\eta=w.}
\]

Thus the kernel element `7`, invisible on `R_2`, has nonzero first-order lift coefficient `w`.

## 4. The same kernel displacement is twisted in the other quotient coset [D]

Because

\[
11=5\cdot7\quad\text{in }U(12),
\]

the first-order difference between the two lifts above the nontrivial quotient element is

\[
D_{11,5}(\bar x)
:=
\frac{\sigma_{11}(x)-\sigma_5(x)}{2}\pmod2.
\]

Exactly as in `v13.458`,

\[
\boxed{D_{11,5}=\tau\circ D_7.}
\]

On the cyclotomic generator,

\[
\boxed{D_{11,5}(u)=u^5.}
\]

Reducing to `F_4`,

\[
\boxed{D_{11,5}(u)\bmod\eta=w^2.}
\]

Since

\[
w\neq w^2,
\]

the first-order correction attached to multiplication by the same kernel element `7` depends on the quotient coset:

\[
\boxed{
1\leftrightarrow7:\ w,
\qquad
5\leftrightarrow11:\ w^2.
}
\]

This is the crucial obstruction.

## 5. Why this is not a tangent translation vector [D]

Suppose the mod-4 lift correction itself supplied a canonical translation realization

\[
\phi:G\to(\mathbf F_4,+)
\]

with the kernel element `7` represented by one fixed translation vector `a`.

Then group additivity would force

\[
\phi(7)-\phi(1)=a,
\qquad
\phi(11)-\phi(5)=a.
\]

In particular the displacement caused by multiplying by `7` would be the same in both quotient cosets.

But the actual first-order lift data give

\[
\boxed{w\quad\text{and}\quad w^2}
\]

for those two differences.

Therefore the natural mod-4 correction datum is not an ordinary translation cocycle with trivial coefficient action. It is twisted by the quotient involution `tau`:

\[
\boxed{
D_{11,5}=\tau(D_7).
}
\]

Equivalently, the lift datum belongs naturally to a semilinear/crossed setting rather than to a fixed additive translation coordinate.

## 6. Exact status of the two-bit reconstruction [D]

The full Galois label is nevertheless recovered canonically:

\[
\boxed{
r\longmapsto
\bigl(\chi_{-3}(r),\chi_{-4}(r)\bigr)
}
\]

is injective and reconstructs all four elements of `G`.

The roles are:

\[
\boxed{\chi_{-3}=\text{mod-two quotient-action bit},}
\]

\[
\boxed{\chi_{-4}=\text{first-order mod-four lift/derivation bit},}
\]

and

\[
\boxed{\chi_{12}=\chi_{-3}\chi_{-4}.}
\]

What fails is a stronger claim: these two recovered bits do not automatically constitute affine coordinates on the tangent translation group.

## 7. Residual C2 in the pointed V4 comparison [D/I]

The pointed arithmetic data still give

\[
(G,7)
\quad\text{and}\quad
(T_2,h).
\]

There are exactly two group isomorphisms

\[
\phi:(G,7)\xrightarrow{\sim}(T_2,h),
\]

because the stabilizer of a nonzero vector in

\[
Aut(V_4)\cong S_3
\]

has order two.

The mod-4 derivation data distinguish `5` from `11` inside `G`, but their natural correction terms are exchanged by the same semilinear involution that fixes `h`. Hence the derivation recovery does not itself canonically select one of the two pointed group isomorphisms as a translation identification.

**[I]** The residual `C2` has moved from "missing label information" to "choice of affine frame." Mod four removes the label ambiguity but not, by itself, the categorical distinction between Galois automorphisms and tangent translations.

## 8. Relation to the affine S4 completion [D/Audit]

From `v13.460`, the tangent affine group is canonically

\[
\boxed{
T_2\rtimes Aut(T_2)
\cong
V_4\rtimes S_3
\cong
AGL_2(\mathbf F_2)
\cong
S_4.
}
\]

This `S_4` action is exact on the four tangent states.

The present result shows that one must not strengthen this automatically to

\[
U(12)\rtimes S_3\quad\text{acting canonically on those same four points}
\]

by identifying `U(12)` with the translation subgroup through the mod-4 lift correction. The natural lift datum is twisted, not translational.

An abstract isomorphism certainly exists because both groups are Klein four, and pointed isomorphisms exist in exactly two ways. What is absent is a uniquely forced translation identification from the presently established arithmetic structures.

## 9. Guardrails [Audit]

- The full `U(12)` label is faithfully recovered modulo four; no Galois information remains lost there.
- The failure above is not failure of abstract group isomorphism. It is failure of the **natural first-order correction map** to be a fixed translation vector.
- `D_7` is a derivation and `D_{11,5}` is `tau`-twisted; they should not be silently treated as elements of one trivial `G`-module.
- The canonical tangent `S_4` from `v13.460` remains exact.
- No geometric mod-12 adjacency, Cone-shell symmetry, or Suzuki block action is inferred.

## 10. Compact conclusion

The mod-four lift resolves the missing Galois character bit but does **not** canonically identify the Galois Klein four with the tangent translation Klein four.

The obstruction is visible directly on the cyclotomic generator:

\[
\boxed{
D_7(u)\bmod\eta=w,
\qquad
D_{11,5}(u)\bmod\eta=w^2.
}
\]

Thus multiplication by the same kernel element `7` has a first-order correction twisted by the quotient involution in the other coset. A genuine translation vector would have to be coset-independent.

Therefore the strongest exact synthesis currently justified is

\[
\boxed{
\text{canonical tangent }S_4
\quad+\quad
\text{faithfully recovered Galois }V_4
\quad+\quad
\text{a semilinear mod-4 bridge between them},
}
\]

not yet a canonical identification of their two Klein-four subgroups.
