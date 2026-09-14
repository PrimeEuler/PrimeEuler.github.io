# Mod-4 Square-Zero Extension, Derivation Bit, and Recovery of the Full V4

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 1. Starting point

Let

\[
K=\mathbf Q(\zeta_{12}),\qquad \mathcal O_K=\mathbf Z[\zeta_{12}],
\]

and set

\[
R_4:=\mathcal O_K/4\mathcal O_K,\qquad R_2:=\mathcal O_K/2\mathcal O_K.
\]

From the preceding checkpoints:

- the full cyclotomic Galois group is
  \[
  G=U(12)=\{1,5,7,11\}\cong V_4;
  \]
- on `R_2`, the action collapses through the quotient controlled by \(\chi_{-3}\):
  \[
  \bar\sigma_1=\bar\sigma_7=\mathrm{id},\qquad
  \bar\sigma_5=\bar\sigma_{11}=:\tau;
  \]
- on `R_4`, all four Galois automorphisms are distinct again.

The question is: where, exactly, does the missing second bit live?

## 2. The mod-4 ring is a square-zero extension of the mod-2 ring [D]

Reduction gives the exact sequence of rings/additive groups

\[
\boxed{
0\longrightarrow 2R_4
\longrightarrow R_4
\longrightarrow R_2
\longrightarrow0.
}
\]

Because

\[
(2R_4)^2\subset4R_4=0,
\]

the kernel is square-zero:

\[
\boxed{(2R_4)^2=0.}
\]

Multiplication by two induces an additive identification

\[
\boxed{R_2\xrightarrow{\sim}2R_4,\qquad \bar x\mapsto2x.}
\]

This extension is not split as a unital ring extension: `R_2` has characteristic two whereas `R_4` has characteristic four.

Thus the first information beyond mod two is genuinely extension data.

## 3. The kernel Galois element is invisible on the quotient but nontrivial to first order [D]

The element \(7\in U(12)\) lies in

\[
\ker\chi_{-3}=\{1,7\}.
\]

Therefore

\[
\sigma_7(x)\equiv x\pmod2
\]

for every \(x\in R_4\).

Define

\[
\boxed{
D_7(\bar x)
:=
\frac{\sigma_7(x)-x}{2}\pmod2.
}
\]

This is well-defined: changing the lift `x` by `2y` changes the numerator by a multiple of four because \(\sigma_7\equiv1\pmod2\).

Since \(\sigma_7\) is multiplicative and congruent to the identity mod two,

\[
\begin{aligned}
D_7(\bar x\bar y)
&=
\frac{\sigma_7(xy)-xy}{2}\pmod2\\
&=
\bar x\,D_7(\bar y)+D_7(\bar x)\,\bar y.
\end{aligned}
\]

Hence

\[
\boxed{D_7:R_2\to R_2\text{ is an }\mathbf F_2\text{-derivation}.}
\]

## 4. Explicit value on the cyclotomic generator [D]

Let

\[
u:=\zeta_{12}\bmod4,\qquad u:=\zeta_{12}\bmod2.
\]

Then

\[
\sigma_7(\nu)=\nu^7.
\]

Using \(\nu^6=-1\),

\[
\nu^7-\nu
=\nu(\nu^6-1)
=-2\nu.
\]

Therefore

\[
\boxed{D_7(u)=u.}
\]

So the automorphism that disappears completely after reduction mod two leaves a nonzero first-order derivation in the square-zero correction layer.

## 5. The second collapsed pair differs by the corresponding twisted derivation [D]

Because

\[
11\equiv5\cdot7\pmod{12},
\]

we have

\[
\sigma_{11}=\sigma_5\sigma_7.
\]

Both \(\sigma_5\) and \(\sigma_{11}\) reduce to the same automorphism \(\tau\) of `R_2`.

Their first-order difference is

\[
\boxed{
D_{11,5}(\bar x)
:=
\frac{\sigma_{11}(x)-\sigma_5(x)}{2}\pmod2
=
\tau(D_7(\bar x)).
}
\]

It is a \(\tau\)-twisted derivation:

\[
D_{11,5}(xy)
=\tau(x)D_{11,5}(y)+D_{11,5}(x)\tau(y).
\]

On the generator,

\[
\nu^{11}-\nu^5
=\nu^5(\nu^6-1)
=-2\nu^5,
\]

so

\[
\boxed{
D_{11,5}(u)=u^5=\tau(u).
}
\]

## 6. Exact two-bit reconstruction of V4 [D]

The mod-two quotient distinguishes the two cosets

\[
\{1,7\},\qquad\{5,11\},
\]

which is exactly the \(\chi_{-3}\) bit.

Inside each coset, the presence or absence of the first-order derivation distinguishes

\[
1\text{ from }7,
\qquad
5\text{ from }11.
\]

That second bit is exactly \(\chi_{-4}\):

\[
\begin{array}{c|cccc}
r&1&5&7&11\\\hline
\chi_{-3}(r)&+&-&+&-\\
\chi_{-4}(r)&+&+&-&-
\end{array}
\]

Therefore the full mod-four Galois label is reconstructed by

\[
\boxed{
r\longmapsto\bigl(\chi_{-3}(r),\chi_{-4}(r)\bigr).}
\]

The first coordinate is visible on `R_2`; the second is recovered in the first-order square-zero correction.

Since

\[
\chi_{12}=\chi_{-4}\chi_{-3},
\]

the third nontrivial character is then recovered automatically.

Equivalently,

\[
\boxed{
\text{mod-2 automorphism bit}=\chi_{-3},
\qquad
\text{first-order derivation bit}=\chi_{-4},
\qquad
\chi_{12}=\chi_{-3}\chi_{-4}.
}
\]

## 7. Character-line check [D]

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

and signs disappear, so the two directions merge.

Modulo four,

\[
\sqrt3-i=2\zeta_{12}^{-1}\neq0,
\]

and the first-order correction separates them.

The Galois table is again fully distinct:

\[
\begin{array}{c|cc}
r&\sigma_r(i)&\sigma_r(\sqrt3)\\\hline
1&i&\sqrt3\\
5&i&-\sqrt3\\
7&-i&-\sqrt3\\
11&-i&\sqrt3
\end{array}
\]

Thus the derivation-bit reconstruction agrees exactly with the characteristic-zero character labeling.

## 8. Why this is extension data rather than associated-graded data [D/I]

The associated-graded prime-two layers are all one-dimensional over \(\mathbf F_4\), and the Galois action on every individual layer factors through \(\chi_{-3}\).

Therefore no single graded layer can recover the lost \(\chi_{-4}\) bit.

The missing bit appears only in how an automorphism lifts across

\[
0\to2R_4\to R_4\to R_2\to0.
\]

In particular,

\[
\boxed{
\chi_{-4}\text{ is encoded by first-order lift/derivation data, not by a separate graded character.}
}
\]

This explains precisely how the full `V4` can be faithful on `R_4` although every associated-graded layer still sees only the \(\chi_{-3}\) quotient.

## 9. Group-extension guardrail [Audit]

The Galois group extension

\[
1\to\langle\sigma_7\rangle\to V_4\to C_2\to1
\]

is split: abstractly \(V_4\cong C_2\times C_2\).

So the recovered information is **not** a nontrivial group-cohomology `H^2` class of `V4` itself.

The nontrivial datum is the action on the non-split square-zero ring extension `R_4 -> R_2`, concretely represented by the derivation `D_7` and its `tau`-twisted companion.

Thus:

\[
\boxed{
\text{split group extension}\neq\text{trivial arithmetic lift data}.
}
\]

## 10. Compact synthesis [D/I]

The prime-two character filtration can now be written

\[
\boxed{
\begin{array}{c}
V_4\text{ on }R_4\\[1mm]
\downarrow\\[-1mm]
C_2\text{ on }R_2
\end{array}
\qquad
\text{with kernel recovered by }D_7.
}
\]

More explicitly,

\[
\boxed{
V_4
\cong
\underbrace{C_2}_{\chi_{-3}\text{ quotient action}}
\times
\underbrace{C_2}_{\chi_{-4}\text{ first-order lift bit}}.
}
\]

and

\[
\boxed{\chi_{12}=\chi_{-3}\chi_{-4}.}
\]

So the exact location of the character recovery is now identified: the associated graded retains the finite-field/Frobenius character \(\chi_{-3}\), while the first nontrivial extension step restores the complex-orientation character \(\chi_{-4}\); their product restores the Pell/real character \(\chi_{12}\).

## Guardrails

- `D_7` is a derivation attached to the lift difference; it is not itself a Dirichlet character.
- The phrase “derivation bit = chi_-4” means the presence/absence of the canonical first-order correction is indexed by the `chi_-4` sign on the four Galois elements.
- No identification is made with Cone tangent vectors, shell displacement, or Suzuki terminal directions.
- The mod-four ring extension and the `V4` group extension are different mathematical objects.

---

**Conclusion.** The full discriminant-12 `V4` action at mod four is reconstructed from two exact bits of local data: the mod-two automorphism/Frobenius bit `chi_-3` and a first-order square-zero derivation bit indexed by `chi_-4`. The product gives `chi_12`. Thus the character information lost on every individual associated-graded layer is recovered precisely in the extension data linking the first two 2-adic layers.