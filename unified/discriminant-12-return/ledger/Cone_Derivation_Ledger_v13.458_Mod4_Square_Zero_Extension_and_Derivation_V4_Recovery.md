# Cone Derivation Ledger v13.458 — Mod-4 Square-Zero Extension and Derivation Recovery of V4

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked before beginning and again immediately before this numbered write. The newest numbered entry remained `v13.457` (`Associated-Graded Ramified Tower S3 Phases`), so `v13.458` was free.

The present checkpoint answers the question left by `v13.457`: if every individual prime-2 associated-graded layer sees only the `chi_-3` quotient, where exactly does the full `V4` action recovered at mod four live?

## 1. Square-zero extension [D]

Let

\[
K=\mathbf Q(\zeta_{12}),\qquad
R_4=\mathcal O_K/4\mathcal O_K,\qquad
R_2=\mathcal O_K/2\mathcal O_K.
\]

Reduction gives

\[
\boxed{
0\to2R_4\to R_4\to R_2\to0.
}
\]

Because

\[
(2R_4)^2=0,
\]

this is a square-zero extension. Multiplication by two identifies

\[
\boxed{R_2\cong2R_4}
\]

additively.

The extension is not split as a unital ring extension because `R_2` has characteristic two while `R_4` has characteristic four.

## 2. Galois collapse mod two [D]

For

\[
G=U(12)=\{1,5,7,11\}\cong V_4,
\]

mod-two reduction gives

\[
\boxed{
\bar\sigma_1=\bar\sigma_7=\mathrm{id},
\qquad
\bar\sigma_5=\bar\sigma_{11}=:\tau.
}
\]

Thus the quotient action on `R_2` is controlled exactly by

\[
\boxed{\chi_{-3}.}
\]

The kernel is

\[
\ker\chi_{-3}=\{1,7\}.
\]

## 3. The invisible kernel element becomes a first-order derivation [D]

Since \(\sigma_7\equiv1\pmod2\), define

\[
\boxed{
D_7(\bar x)
=
\frac{\sigma_7(x)-x}{2}\pmod2.
}
\]

This is well-defined and satisfies

\[
\boxed{
D_7(xy)=xD_7(y)+D_7(x)y,
}
\]

so `D_7` is an `F2`-derivation of `R_2`.

Let

\[
\nu=\zeta_{12}\bmod4,
\qquad
u^6=-1,
\qquad
u^{12}=1,
\]

and write

\[
u\mapsto u\in R_2.
\]

Then

\[
\nu^7-\nu
=\nu(\nu^6-1)
=-2\nu,
\]

hence

\[
\boxed{D_7(u)=u.}
\]

Therefore the Galois bit that is completely invisible in the quotient ring is nonzero in the first-order lift.

## 4. The second collapsed pair [D]

Since

\[
11\equiv5\cdot7\pmod{12},
\]

we have

\[
\sigma_{11}=\sigma_5\sigma_7.
\]

Both reduce to `tau` on `R_2`, but their first-order difference is

\[
\boxed{
D_{11,5}(\bar x)
:=
\frac{\sigma_{11}(x)-\sigma_5(x)}{2}\pmod2
=
\tau(D_7(\bar x)).
}
\]

This is a `tau`-twisted derivation:

\[
D_{11,5}(xy)
=
\tau(x)D_{11,5}(y)+D_{11,5}(x)\tau(y).
\]

On the cyclotomic generator,

\[
\nu^{11}-\nu^5
=\nu^5(\nu^6-1)
=-2\nu^5,
\]

so

\[
\boxed{D_{11,5}(u)=u^5=\tau(u).}
\]

## 5. Exact two-bit reconstruction of V4 [D]

The mod-two action distinguishes

\[
\{1,7\}
\quad\text{from}\quad
\{5,11\},
\]

which is exactly the `chi_-3` bit.

The first-order derivation distinguishes

\[
1\text{ from }7,
\qquad
5\text{ from }11.
\]

That second bit is indexed exactly by `chi_-4`:

\[
\begin{array}{c|cccc}
r&1&5&7&11\\\hline
\chi_{-3}(r)&+&-&+&-\\
\chi_{-4}(r)&+&+&-&-
\end{array}
\]

Thus

\[
\boxed{
r\mapsto\bigl(\chi_{-3}(r),\chi_{-4}(r)\bigr)
}
\]

reconstructs the full `V4` label.

Since

\[
\chi_{12}=\chi_{-3}\chi_{-4},
\]

the third nontrivial character follows automatically.

Equivalently,

\[
\boxed{
\text{mod-two automorphism bit}=\chi_{-3},
}
\]

\[
\boxed{
\text{first-order derivation bit}=\chi_{-4},
}
\]

and

\[
\boxed{\chi_{12}=\chi_{-3}\chi_{-4}.}
\]

## 6. Character-line check [D]

In characteristic zero,

\[
\sigma_r(i)=\chi_{-4}(r)i,
\qquad
\sigma_r(\sqrt3)=\chi_{12}(r)\sqrt3.
\]

Modulo two,

\[
i\equiv\sqrt3,
\]

and the sign information disappears.

Modulo four,

\[
\sqrt3-i=2\zeta_{12}^{-1}\neq0,
\]

so the two lines separate again.

The exact Galois table is

\[
\begin{array}{c|cc}
r&\sigma_r(i)&\sigma_r(\sqrt3)\\\hline
1&i&\sqrt3\\
5&i&-\sqrt3\\
7&-i&-\sqrt3\\
11&-i&\sqrt3
\end{array}
\]

which agrees exactly with the two-bit reconstruction.

## 7. Why associated graded alone cannot see the second bit [D/I]

From `v13.457`, every prime-two graded layer

\[
\mathfrak P_2^n/\mathfrak P_2^{n+1}
\]

is one-dimensional over `F4`, and the Galois action on each individual layer factors only through `chi_-3`.

Therefore no single graded layer can recover the lost `chi_-4` information.

The second bit lives in how the action lifts across

\[
0\to2R_4\to R_4\to R_2\to0.
\]

Thus

\[
\boxed{
\chi_{-4}\text{ is encoded in first-order extension/lift data, not in a separate graded character.}
}
\]

This resolves the apparent tension between:

- `v13.457`: every associated-graded layer sees only `chi_-3`;
- `v13.447`: the full `V4` action is already faithful mod four.

Both are simultaneously true because the missing bit is extension data.

## 8. Group-extension guardrail [Audit]

The abstract Galois sequence

\[
1\to\langle\sigma_7\rangle\to V_4\to C_2\to1
\]

is split:

\[
V_4\cong C_2\times C_2.
\]

Therefore the new datum is **not** a nontrivial `H^2` class of the Galois group itself.

The nontrivial arithmetic object is the action on the non-split square-zero ring extension `R_4 -> R_2`, represented concretely by `D_7` and the corresponding `tau`-twisted derivation.

Hence

\[
\boxed{
\text{split group extension}\neq\text{trivial lift data on a ramified ring extension}.
}
\]

## 9. Compact synthesis [D/I]

The prime-two character filtration is now exact:

\[
\boxed{
V_4\text{ on }R_4
\longrightarrow
C_2\text{ on }R_2,
}
\]

with the lost kernel recovered by the first-order derivation `D_7`.

At the character level,

\[
\boxed{
V_4
\cong
\underbrace{C_2}_{\chi_{-3}\text{ quotient action}}
\times
\underbrace{C_2}_{\chi_{-4}\text{ lift/derivation bit}},
}
\]

and

\[
\boxed{\chi_{12}=\chi_{-3}\chi_{-4}.}
\]

So the exact location of the recovered character information is now identified: `chi_-3` lives on the associated graded, `chi_-4` lives in the first extension step, and `chi_12` is their product.

## 10. Relation to the current Suzuki frontier [Audit]

The concurrent Suzuki theorem thread is already closed at

\[
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

Recent terminal-direction diagnostics (`v13.455-v13.456`) show strong residue/character content plus one exceptional prime-3-dominated even direction, but no operator-level identification with the local derivation `D_7` is made here.

No Suzuki theorem strengthening follows from the present local arithmetic result.

---

**Checkpoint conclusion.** The full mod-four `V4` action is recovered from two distinct layers of local information. The mod-two quotient action is exactly the `chi_-3` bit. The kernel element invisible modulo two produces a nonzero first-order derivation, and the presence/absence of that correction is exactly the `chi_-4` bit. Their product is `chi_12`. Thus the character information absent from every individual associated-graded layer is recovered precisely in the square-zero extension data linking mod two to mod four.