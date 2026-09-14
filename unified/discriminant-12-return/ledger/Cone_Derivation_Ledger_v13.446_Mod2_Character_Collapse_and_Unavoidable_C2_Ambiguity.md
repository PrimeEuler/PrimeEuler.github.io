# Cone Derivation Ledger v13.446 — Mod-2 Character Collapse and Unavoidable C2 Ambiguity

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live head before this write was `v13.445` (External Audit Round 32), which independently verified the V4/cyclotomic/Pell/F4 thread through `v13.444`. Therefore `v13.446` is the next free ledger index.

The immediate question left by `v13.444` is whether the final residual swap

\[
\chi_{-4}\leftrightarrow\chi_{12}
\]

can be removed by using the characteristic-zero generators `i`, `sqrt(3)`, or the cyclotomic operator `Z = times zeta_12`, after passage to the full nonreduced mod-2 ring.

The answer is no: the two directions coincide exactly modulo `2`.

## 1. Full nonreduced mod-2 carrier [D]

Retain the notation from `v13.438` and `v13.442`:

\[
R_2:=\mathcal O_{K_{12}}/2\mathcal O_{K_{12}}
\cong \mathbf F_4[\eta]/(\eta^2),
\]

with

\[
u:=\bar\zeta_{12}\in R_2,
\qquad
u^6=1,
\qquad
h:=u^3=1+w^2\eta.
\]

Here `w` is the chosen embedded generator of `F4^x` with

\[
w^2+w+1=0.
\]

The element `h` is the unique nontrivial tangent involution fixed by the surviving mod-2 Galois involution.

## 2. Exact reductions of i and sqrt(3) [D]

In characteristic zero,

\[
i=\zeta_{12}^3.
\]

Therefore in `R_2`,

\[
\boxed{\bar i=u^3=h.}
\]

Also

\[
\sqrt3+i=2\zeta_{12}.
\]

Reducing modulo `2` gives

\[
\bar{\sqrt3}+\bar i=0.
\]

Since the ring has characteristic `2`, subtraction and addition agree, so

\[
\boxed{\bar{\sqrt3}=\bar i=h.}
\]

Thus the two characteristic-zero generators that span the `chi_-4` and `chi_12` character lines become exactly the same element in the full nonreduced mod-2 ring.

This is stronger than the residue-field statement `i -> 1` and `sqrt3 -> 1`: the equality already holds before killing the nilpotent tangent layer.

## 3. The four rational character lines collapse in pairs [D]

Recall the rational character-adapted basis

\[
B_\chi=(1,i,i\sqrt3,\sqrt3),
\]

corresponding to

\[
(\mathbf1,\chi_{-4},\chi_{-3},\chi_{12}).
\]

Using

\[
\bar i=\bar{\sqrt3}=h,
\qquad
h^2=1,
\]

we obtain

\[
\boxed{
1\mapsto1,
\qquad
i\mapsto h,
\qquad
i\sqrt3\mapsto1,
\qquad
\sqrt3\mapsto h.
}
\]

Therefore

\[
\boxed{
\{\mathbf1,\chi_{-3}\}\mapsto 1,
\qquad
\{\chi_{-4},\chi_{12}\}\mapsto h.
}
\]

So the full four-line rational decomposition does not survive modulo `2`; it collapses exactly according to the `chi_-3` parity splitting already visible in the zeta-intertwiner graph.

Equivalently, on the dual Klein four group of characters,

\[
\widehat{V_4}\longrightarrow
\widehat{V_4}/\langle\chi_{-3}\rangle\cong C_2
\]

is the surviving mod-2 character quotient.

## 4. Exact identification with the parity halves of Z [D]

From `v13.431` and `v13.436`, define

\[
K_+=L_{\mathbf1}\oplus L_{-3},
\qquad
K_-=L_{-4}\oplus L_{12}.
\]

The cyclotomic operator satisfies

\[
\mathcal Z:K_+\leftrightarrow K_-.
\]

The mod-2 reduction above sends the two basis generators of `K_+` to `1`, and the two basis generators of `K_-` to `h`:

\[
\boxed{K_+\rightsquigarrow1,
\qquad
K_-\rightsquigarrow h.}
\]

Hence the `chi_-3` parity decomposition is precisely the two-class information retained by the full mod-2 ramified ring.

This is not merely a residue-field collapse: the nontrivial tangent involution `h` retains the distinction between the two parity halves even though it cannot distinguish the two lines inside either half.

## 5. Why i, sqrt(3), and Z cannot remove the last C2 ambiguity mod 2 [D]

The residual ambiguity from `v13.444` was

\[
\chi_{-4}\leftrightarrow\chi_{12}.
\]

But their characteristic-zero spanning elements reduce to exactly the same element:

\[
\boxed{i\equiv\sqrt3\equiv h\pmod2.}
\]

Therefore every construction depending only on their images in `R_2` necessarily identifies the two channels.

In particular, multiplication by `u=bar(zeta_12)` cannot separate two inputs that are already equal in `R_2`.

Thus the full nonreduced mod-2 cyclotomic carrier does **not** canonically decide which of the two remaining tangent states should be labeled `chi_-4` and which should be labeled `chi_12`.

The residual transposition is therefore genuine at this reduction level.

## 6. The exact residual symmetry [D]

The canonical self-duality from `v13.444` fixes

\[
1\leftrightarrow\mathbf1,
\qquad
7\leftrightarrow\chi_{-3},
\]

and the arithmetic tangent involution fixes

\[
h=u^3.
\]

After those identifications, the only remaining freedom is the transposition

\[
\boxed{\chi_{-4}\leftrightarrow\chi_{12}.}
\]

On the `U(12)` side this is the automorphism

\[
5\leftrightarrow11,
\qquad
7\mapsto7.
\]

On the tangent `V_4` side it swaps the two nonidentity tangent elements other than `h` while fixing `h`.

Thus the stabilizer of the distinguished `chi_-3 / 7 / h` axis is exactly

\[
\boxed{C_2\subset S_3=\operatorname{Aut}(V_4).}
\]

This is the exact residual labeling symmetry.

## 7. A sharper mod-2 character diagram [D/I]

The characteristic-zero character decomposition

\[
\{\mathbf1,\chi_{-3},\chi_{-4},\chi_{12}\}
\]

passes through the full ramified mod-2 ring as

\[
\boxed{
\{\mathbf1,\chi_{-3}\}
\longmapsto1,
\qquad
\{\chi_{-4},\chi_{12}\}
\longmapsto h,
}
\]

and then through the residue map `R_2 -> F_4` as

\[
1\mapsto1,
\qquad
h\mapsto1.
\]

So there are two successive collapses:

\[
\boxed{4\ \text{character lines}\to2\ \text{ramified parity states}\to1\ \text{residue scalar state}.}
\]

Meanwhile, independently, cyclotomic multiplication itself follows

\[
C_{12}\to C_6\to C_3.
\]

These are distinct filtrations and should not be conflated.

## 8. Consequence for the tangent V4 / character V4 bridge [D/I]

The tangent Klein four group remains

\[
T_2=1+\eta\mathbf F_4\cong V_4,
\]

with distinguished nonidentity element

\[
h=1+w^2\eta.
\]

The canonical character self-duality gives a distinguished character axis `chi_-3`.

Thus there is a canonical **pointed** Klein-four comparison

\[
\boxed{(U(12),7)\quad\leftrightarrow\quad(T_2,h)}
\]

up to the unique residual `C2` automorphism fixing the distinguished point.

Equivalently, the arithmetic determines an isomorphism class of pointed `V4` objects, but not a unique fully labeled isomorphism.

This is the strongest canonical statement available from the mod-2 data alone.

## 9. What would be required to break the residual swap [Audit/I]

Because `i` and `sqrt3` coincide modulo `2`, any further separation must use information beyond `R_2` itself.

Natural candidates include:

1. a deeper `2`-adic lift, e.g. modulo `4`, where the identity
   \[
   \sqrt3+i=2\zeta_{12}
   \]
   is no longer annihilated;
2. characteristic-zero archimedean structure, where `i` and `sqrt3` are visibly distinct;
3. an additional operator or normalization not factoring through the mod-2 ring.

No such extra structure is promoted here.

## 10. Guardrails [Audit]

- The equality `i = sqrt3` is **only** in the full mod-2 quotient `R_2`; it is false in characteristic zero.
- The collapse of character lines is not a statement that the four Galois characters become equal as abstract characters.
- `chi_-3` remains the controlling residue Galois/Frobenius parity character, exactly as in `v13.416`.
- The residual `C2` ambiguity is a labeling symmetry of the pointed `V4` comparison, not a new physical or geometric symmetry of the Cone.
- No shell adjacency or Suzuki-sector identification is inferred.

## 11. Compact synthesis [D/I]

The prime-2 ramified ring retains exactly one bit of the four-character decomposition:

\[
\boxed{
\mathbf1\sim\chi_{-3},
\qquad
\chi_{-4}\sim\chi_{12}
\quad(\bmod 2).
}
\]

This surviving bit is represented by

\[
\boxed{1\leftrightarrow K_+,
\qquad h=u^3\leftrightarrow K_-.}
\]

The distinguished `chi_-3 / 7 / h` axis is canonical, while the swap

\[
\boxed{\chi_{-4}\leftrightarrow\chi_{12}}
\]

cannot be removed inside the full mod-2 carrier.

Hence the bridge constructed in `v13.442-v13.444` terminates naturally in a **pointed V4 object with residual C2 symmetry**.

That residual symmetry is not a defect of the construction; it is forced by the exact ramified congruence

\[
\boxed{i\equiv\sqrt3\pmod2.}
\]
