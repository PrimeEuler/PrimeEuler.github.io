# Cone Derivation Ledger v13.189 — Principal Paper v0.3 Line Audit

**Date:** 2026-09-03  
**Target:** `papers/Discriminant_12_Return_v0.3.tex`  
**Purpose:** line-by-line mathematical, logical-scope, notation, and LaTeX audit after the v13.188 dependency rewrite.

Labels: [D] exact, [Audit] correction/clarification, [I] interpretation, [O] open.

---

## 1. Executive verdict

The v0.3 rewrite is mathematically much stronger than v0.2 and the central algebraic chain survives this audit. No failure was found in the centered-Cayley identities, the explicit return matrix, the ramified ideal action, the Lorentz form, the Cone boost, the tangent-eigenray theorem, the cyclotomic companion matrix, the index-4 calculation, the mod-2 transvection, the `F_4` order-3/order-2 actions, or the `n=11` narrow-class calculation.

The main repairs are **logical-scope and basis-compatibility repairs**, not changes to the core structure. One theorem-level quantifier should be rewritten before publication; one finite-field basis should be chosen compatibly with the integral basis change; and the Artin/`T_11` paragraph should make its restriction from the full cyclotomic Galois group to `Gal(K_12/F)` explicit.

---

## 2. Preamble and abstract

### [D] Centered-Cayley formulas

The abstract formulas

\[
K=\frac{2}{\tau+2}H,
\qquad
KH=\frac{\tau-2}{2}I
\]

are correct, as is the selection `sigma=2`, `tau=4`, `Delta=12`.

### [Audit] "selected return" language

The abstract correctly includes the phrase "with the period-[1,2] positive integral normalization." Retain that qualifier everywhere. The Cayley condition selects the trace, not by itself the literal matrix `g_12`.

### [Audit] `T_11`/`J` wording

The abstract says the Artin action is `T_11`, complex conjugation, "corresponding to" `J`. This is publication-safe provided the body continues to state that this is a representation correspondence and not literal equality of a field automorphism with an operator.

---

## 3. Main theorem: quantifier/scope issue

### [Audit — important]

The theorem begins:

> Let `g in SL_2(Q)` ... Then the following statements hold.

Clause (i) is genuinely a theorem about that arbitrary `g`. Clauses (ii)–(vi), however, are statements about the **newly selected and normalized object** `g_12`, not consequences that hold for the originally quantified `g` as written.

The mathematics is correct, but the theorem's logical grammar should be changed.

### Recommended theorem opening

Use a two-stage statement:

> Let `g in SL_2(Q)` have trace `tau`, assume `g+I` is invertible, and define `H`, `K`, `tau=sigma+2`. Then the universal centered-Cayley identities hold, and in the hyperbolic range `K=H^{-1}` iff `sigma=2`. At the selected trace `tau=4`, choose the period-[1,2] primitive positive integral normalization `g_12`. For this normalized return, statements (ii)–(vi) hold.

This removes any implication that an arbitrary trace-4 rational matrix is literally equal to `g_12`.

---

## 4. Centered Cayley section

### [D] Centered square

\[
H^2=(\tau^2/4-1)I
\]

is exact.

### [D] Cayley inverse

\[
(g+I)^{-1}=\frac{(\tau+1)I-g}{\tau+2}
\]

is exact whenever `g+I` is invertible. For `det g=1`, invertibility is equivalent to `tau != -2`, consistent with the denominator.

### [D] Self-reciprocal trace

Hyperbolicity makes `H` invertible and gives

\[
K=H^{-1}\iff\tau=4\iff\sigma=2.
\]

No repair required.

---

## 5. Primitive return and ideal lattice

### [D] Continued-fraction product

For

\[
A_a=\begin{pmatrix}a&1\\1&0\end{pmatrix},
\]

\[
A_1A_2=\begin{pmatrix}3&1\\2&1\end{pmatrix}.
\]

Correct.

### [D] Ramified ideal

\[
\mathfrak p_2=(2,\sqrt3-1)=(1+\sqrt3)
\]

is correct as an ideal of `O_F=Z[sqrt3]`.

### [D] Multiplication matrices

In `f=(2,sqrt3-1)`:

\[
[\times\sqrt3]_f=H_{12},
\qquad
[\times(2+\sqrt3)]_f=g_{12}.
\]

Correct.

### [D] Principal/Pell basis and conjugacy

For

\[
e_1=1+\sqrt3,
\qquad
e_2=3+\sqrt3,
\]

\[
C_{\rm basis}=\begin{pmatrix}1&2\\1&1\end{pmatrix},
\]

and

\[
C_{\rm basis}^{-1}g_{12}C_{\rm basis}
=\begin{pmatrix}2&3\\1&2\end{pmatrix}
\]

are exact.

No conflict with the distinct arithmetic reversor `C_rev`; v0.3 currently uses only `C_basis`, so no notation collision occurs in the paper.

---

## 6. Pell-Lorentz and Cone sections

### [D] Norm form

\[
N((2x-y)+y\sqrt3)=2q_{12}(x,y),
\quad
q_{12}=2x^2-2xy-y^2
\]

is correct and has discriminant 12.

### [D] Lorentz boost

In `(U,V)=(2x-y,sqrt3 y)`, multiplication by `2+sqrt3` is

\[
B_{12}=\begin{pmatrix}2&\sqrt3\\\sqrt3&2\end{pmatrix}.
\]

Correct.

### [D] Factor-cone null action

With Paper-A coordinates

\[
x=T+X,
\qquad y=T-X,
\]

the same real Lorentz boost acts as

\[
x'=\lambda x,
\qquad y'=\lambda^{-1}y.
\]

Thus `xy=n` is invariant and rapidity translates by `log lambda`. Correct.

### [D] Tangency theorem

The row parabola

\[
Y^2=u^2+2uX
\]

has vertex `(-u/2,0)`, the mirror column has `(u/2,0)`, and the origin-centered fixed-`T` circle is tangent there exactly at `T=u/2`. The side-view points `(T,X)=(u/2,+-u/2)` are exactly the null eigenrays of `B_12`.

Correct.

### [Audit] Terminology

Retain "factor-parabola tangent endpoints" or "parabola/fixed-T-circle tangent endpoints." Avoid shortening this later to "cell-centered circles," because the source audit showed that circular product-label boxes are a separate annotation layer.

---

## 7. Mod-12 shell

### [D]

\[
U(12)=\{1,5,7,11\}\cong V_4
\]

and

\[
T_r=(r+1)/2,
\quad
X_r=\pm(r-1)/2,
\quad
Y_r=\sqrt r
\]

are correct.

### [D] Galois action typo fixed

v0.3 correctly uses

\[
T_r:\zeta_{12}\mapsto\zeta_{12}^r,
\]

repairing the v0.2 typo.

### [Audit] Figure dependency

The source references `mod12_v4_cone_triple.png`. Before release, confirm that the image exists in the TeX compilation directory or add an explicit relative graphics path. This is a build/deployment issue, not a mathematical issue.

---

## 8. Cyclotomic completion

### [D] Operator identity

\[
\mathcal Z=(H_{12}+iI)/2=\times\zeta_{12}
\]

is exact after scalar extension, and the extended ideal

\[
\mathfrak P_2=\mathfrak p_2\OO_{K_{12}}
\]

is an integral carrier.

### [D] Integral rank-4 matrix

The companion matrix displayed for multiplication by `zeta` follows from

\[
\zeta^4=\zeta^2-1
\]

and is correct.

### [D] Index 4

\[
[\OO_{K_{12}}:\Z[\sqrt3,i]]=4
\]

is correct. Both the determinant calculation and the independent discriminant check support it.

### [Audit] Quotient language

The sentence

\[
\OO_{K_{12}}/\OO_0\cong(\F_2)^2
\]

should continue to say **additive quotient**. It is not being asserted as a quotient field or as the same ring as the later `F_4` residue field. v0.3 currently handles this correctly.

---

## 9. Ramified quotient and `F_4`

### [D] Ramified reduction

\[
\bar g_{12}=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

and

\[
\bar q_{12}(x,y)=y
\]

are correct in the `f` basis.

### [D] Integral origin of Boolean relabeling

\[
C_{\rm basis}\bmod2
=\Phi
=\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]

and

\[
\Phi\bar g\Phi^{-1}=P
\]

are exact.

### [Audit — basis compatibility refinement]

v0.3 then identifies Frobenius with the same transvection in the `F_4` basis `(1,omega)`. The matrix calculation is correct, but a still cleaner presentation is available that makes the **integral basis change and the field basis change commute exactly**.

Choose the `F_2`-linear identification

\[
\psi_f(f_1)=1,
\qquad
\psi_f(f_2)=\omega^2.
\]

Then because

\[
e_1=f_1+f_2,
\qquad
e_2=f_2\pmod2,
\]

we obtain

\[
\psi_e(e_1)=\omega,
\qquad
\psi_e(e_2)=\omega^2.
\]

In the ramified basis `(1,omega^2)`, Frobenius has matrix

\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}=\bar g,
\]

while in the principal/Boolean basis `(omega,omega^2)` Frobenius swaps the two basis elements and has matrix `P`.

This is the basis-compatible version of the bridge and should replace the looser phrase "in a suitable additive basis" in the theorem/body.

### [D / recommended promotion] XOR as field trace

The compatible basis above also gives an exact strengthening not yet stated in v0.3:

\[
\operatorname{Tr}_{\F_4/\F_2}(a+b\omega^2)=b.
\]

Hence in the ramified basis

\[
\boxed{\bar q_{12}=\operatorname{Tr}_{\F_4/\F_2}.}
\]

In the principal/Boolean basis `(omega,omega^2)`,

\[
\operatorname{Tr}(\epsilon_1\omega+\epsilon_2\omega^2)
=\epsilon_1+\epsilon_2
=\epsilon_1\oplus\epsilon_2.
\]

Therefore the existing XOR statement can be sharpened to

\[
\boxed{\text{XOR parity}=\operatorname{Tr}_{\F_4/\F_2}}
\]

under the explicitly stated compatible additive identification.

**Guardrail:** this does not identify the ramified dual-number quotient with `F_4` as rings. It is an `F_2`-linear carrier/action identification.

### [D] Finite groups

`<times omega,Fr>=GL_2(F_2) ~= S_3`, `AGL(1,4) ~= A_4`, and `A Gamma L(1,4) ~= S_4` are correct. Keep the `D_8` Boolean affine layer separate.

---

## 10. The `n=11` specialization

### [D] Geometry

\[
(11,1),(1,11)\mapsto(X,Y,T)=(\pm5,\sqrt{11},6)
\]

is exact.

### [D] Narrow class computation

\[
N(1+2\sqrt3)=-11
\]

and

\[
(1+\sqrt3)(1+2\sqrt3)=7+3\sqrt3
\]

with both real embeddings of `7+3sqrt3` positive imply

\[
[\mathfrak p_{11}]=[\mathfrak p_2]
\]

in the narrow class group.

### [Audit] Artin/Galois layer should be stated more explicitly

The paper writes

\[
\Art_{K_{12}/F}(\mathfrak p_{11})=T_{11}.
\]

This is compatible with the established project convention, but `T_11` was introduced just above as an element of the full cyclotomic group

\[
\Gal(K_{12}/\Q)\cong U(12).
\]

For publication clarity, explicitly say that the nontrivial element of the quadratic subgroup

\[
\Gal(K_{12}/F)\subset\Gal(K_{12}/\Q)
\]

is the restriction/identification of the cyclotomic automorphism `T_11`. Since `11=-1 mod 12`, this automorphism is complex conjugation and fixes `sqrt3`, hence indeed lies in `Gal(K_12/F)`.

This removes any apparent category jump in the Artin equation.

### [D] `T_11 <-> J`

The paper correctly labels this a representation correspondence and explicitly denies literal equality across categories. Retain this wording.

---

## 11. LaTeX/build audit

No obvious unmatched environment or displayed-math delimiter was found in the fetched source.

Items to verify in an actual TeX build:

1. `mod12_v4_cone_triple.png` resolves from the paper's compilation working directory.
2. `\mathbin{\mathrm{xor}}` is typographically acceptable. It compiles as text in math mode only if `\mathrm{xor}` exists; standard LaTeX/amsmath does **not** define `\xor` by default. The current source uses `\mathrm{xor}` without defining it. This is a likely compile error.

### [Audit — likely LaTeX error]

Replace

```tex
\epsilon_1\mathbin{\mathrm{xor}}\epsilon_2
```

with either

```tex
\epsilon_1\oplus\epsilon_2
```

or define a command explicitly, e.g.

```tex
\newcommand{\xor}{\mathbin{\mathrm{XOR}}}
```

The mathematical paper already uses `oplus` elsewhere, so `\epsilon_1\oplus\epsilon_2` is preferable.

---

## 12. Recommended v0.3.1 repair set

Before adding new material, make a narrow repair revision with exactly these changes:

1. rewrite the main theorem's opening so clause (i) applies to arbitrary `g` and clauses (ii)–(vi) apply to the selected normalized `g_12`;
2. replace the undefined `\mathrm{xor}` expression by `\oplus`;
3. use the basis-compatible `F_4` identification `f_1->1`, `f_2->omega^2`, hence `e_1->omega`, `e_2->omega^2`;
4. promote the resulting exact identity `bar q_12 = Tr_{F_4/F_2}`, equivalently XOR = field trace in the Boolean basis;
5. clarify that `T_11` lies in `Gal(K_12/F)` because it is complex conjugation and fixes `sqrt3`;
6. verify the figure path in an actual TeX build.

After those repairs, the draft is ready for a second independent audit rather than further structural expansion.

---

## 13. Final status

**Core theorem chain:** survives.  
**New mathematical failure found:** none.  
**Logical theorem-scope repair:** required.  
**Likely LaTeX compile repair:** required (`\\mathrm{xor}`).  
**Finite-field basis refinement:** strongly recommended.  
**New exact promotion:** XOR parity equals the `F_4/F_2` field trace under the compatible additive identification.  
**`T_11 <-> J`:** survives, with a recommended explicit subgroup sentence.

---

**End of v13.189 audit.**