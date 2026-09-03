# Cone Derivation Ledger v13.188 — Principal Paper Dependency Audit

**Status:** Draft-level dependency and theorem-architecture audit of `papers/Discriminant_12_Return_v0.2.tex` against the verified ledger through v13.187 and the independent external audit v13.186.  
**Date:** 2026-09-03  
**Scope:** Determine which claims in the principal paper are proved in-document, which are now proved elsewhere in the ledger and should be promoted into the paper, which statements require correction, and what theorem architecture should replace the current v0.2 structure.

Audit labels: [S] source-established, [D] exact derived, [N-cert] certified numerical, [I] interpretation, [O] open, [Audit] correction/limitation.

---

## 1. Executive verdict

The principal paper has the correct mathematical spine, but `v0.2` now materially understates the proof status of the project.

At the time of that draft, Theorem 2.1 included six clauses while the body proved only the first four packages and relegated the cyclotomic and ramified-Boolean packages to a roadmap. That was the presentation gap identified independently in v13.186. Since then, ledger v13.182–v13.185 have supplied exact proofs that substantially strengthen clauses (iv)–(vi), including:

1. the exact ideal-basis realization of the return;
2. the exact interpretation of the centered generator as multiplication by `sqrt(3)`;
3. the integral cyclotomic carrier `p_2 O_K` for `Z`;
4. resolution of the old index-4 lattice issue;
5. the residue field `F_4` and order-3 reduction of the cyclotomic operator;
6. the exact identification of the ramified transvection with Frobenius on `F_4`;
7. the resulting `A_4` / `S_4` finite symmetry completion.

Accordingly, the next paper revision should not merely patch v0.2. It should reorganize the theorem into a dependency chain whose later clauses are actually proved in the body.

---

## 2. Current theorem audit

### 2.1 Clauses (i)–(ii): centered Cayley selection

**[D — clean and complete.]**

The paper proves

\[
K=\frac{2}{\tau+2}H,
\qquad
KH=\frac{\tau-2}{2}I,
\]

and therefore, with `tau=sigma+2`,

\[
\boxed{K=H^{-1}\iff\sigma=2}
\]

in the hyperbolic range.

This remains the correct theorem entrance. It is independent of Pell arithmetic, the Cone, cyclotomy, Suzuki theory, and RH-adjacent material.

**Recommendation:** retain essentially unchanged.

### 2.2 Clause (iii): the selected integral return

**[D — correct, but uniqueness language needs care.]**

The draft introduces

\[
g_{12}=A_1A_2=\begin{pmatrix}3&1\\2&1\end{pmatrix},
\]

with trace `4`, determinant `1`, discriminant `12`, and eigenvalues `2+-sqrt(3)`.

This is correct. However, the strongest project statement is conjugacy-class based: the centered-Cayley condition selects the trace-4 hyperbolic class, while `[1,2]` supplies a distinguished primitive positive integral representative. The paper should avoid wording that sounds as though the Cayley condition alone uniquely derives this exact matrix without the positivity/continued-fraction normalization.

**Recommendation:** state explicitly:

> The self-reciprocity condition selects the trace-4 hyperbolic class; the period `[1,2]` normalization selects the primitive positive integral representative `g_12` used below.

### 2.3 Clause (iv): ideal action and Lorentz norm

**[Audit — current theorem contains a basis error.]**

The current theorem states that in the ordered ramified basis

\[
(2,\sqrt3-1),
\]

both `H_12` and `g_12` are multiplication by `sqrt(3)` and `2+sqrt(3)`, respectively. This is correct and is proved in the body.

However, later ledger work discovered a second natural basis

\[
e_1=1+\sqrt3,
\qquad
e_2=3+\sqrt3=\sqrt3 e_1,
\]

in which

\[
[\times(2+\sqrt3)]_e
=
\begin{pmatrix}2&3\\1&2\end{pmatrix},
\qquad
[\times\sqrt3]_e
=
\begin{pmatrix}0&3\\1&0\end{pmatrix}.
\]

The exact integral basis change

\[
C_{\rm basis}=\begin{pmatrix}1&2\\1&1\end{pmatrix}
\]

satisfies

\[
C_{\rm basis}^{-1}g_{12}C_{\rm basis}
=
\begin{pmatrix}2&3\\1&2\end{pmatrix}.
\]

This basis is mathematically important because modulo `2`, `C_basis` becomes exactly the Boolean relabeling matrix `Phi`, and the return becomes factor exchange.

**Recommendation:** retain the ramified basis for the integral form `q_12`, then add a proposition introducing the principal/Pell basis and the exact basis conjugacy. This turns what v0.2 presents as a later mod-2 relabeling into an integral arithmetic construction.

### 2.4 Clause (v): cyclotomic completion

**[D — now fully provable, but v0.2 is obsolete.]**

The identities

\[
\mathcal Z=\frac{H+iI}{2},
\qquad
\Phi_{12}(\mathcal Z)=0,
\qquad
\mathcal Z^{12}=I,
\]

and

\[
g_{12}=-i(I+\mathcal Z)(I-\mathcal Z)^{-1}
\]

are exact.

The important later refinement is that the apparent half-integrality of `Z` is not an operator defect. Let

\[
K=\Q(\zeta_{12}),
\qquad
\mathfrak P_2=\mathfrak p_2\OO_K,
\qquad
\alpha=1+\sqrt3.
\]

Then

\[
\{\alpha,\alpha\zeta,\alpha\zeta^2,\alpha\zeta^3\}
\]

is a natural integral ideal basis and multiplication by `zeta=zeta_12` is represented by

\[
\boxed{
M_\zeta=
\begin{pmatrix}
0&0&0&-1\\
1&0&0&0\\
0&1&0&1\\
0&0&1&0
\end{pmatrix}.
}
\]

Thus

\[
\boxed{\mathcal Z=\times\zeta_{12}}
\]

on the integral carrier `P_2`.

The old order

\[
\OO_0=\Z[\sqrt3,i]
\]

has exact index

\[
\boxed{[\OO_K:\OO_0]=4}.
\]

This has now been verified by two independent methods: the project's basis determinant and the external audit's discriminant calculation

\[
\disc(\OO_0)=2304,
\qquad
\disc(\OO_K)=144.
\]

**Recommendation:** replace the roadmap treatment with a full cyclotomic-integrality section. The index-4 calculation belongs there as an explanation of why the earlier 2-by-2 complex presentation looks half-integral.

### 2.5 Clause (vi): ramified Boolean reduction

**[D — correct but substantially superseded by stronger structure.]**

The paper's reduction

\[
\bar g(x,y)=(x+y,y)
\]

and Boolean coordinate change

\[
\Phi(x,y)=(x,x+y)
\]

give

\[
\Phi\bar g\Phi^{-1}=P,
\]

where `P` is factor exchange. The reduced form becomes XOR. These statements remain exact.

The later ideal-basis theorem strengthens this:

\[
\boxed{\bar C_{\rm basis}=\Phi.}
\]

Therefore `Phi` is not an ad hoc Boolean relabeling. It is the mod-2 reduction of the integral basis change between two natural bases of `p_2`.

Even more strongly, with

\[
\F_4=\F_2(\omega),
\qquad
\omega^2+\omega+1=0,
\]

Frobenius in the basis `(1,omega)` is

\[
\boxed{
\mathrm{Fr}=
\begin{pmatrix}1&1\\0&1\end{pmatrix}
=\bar g.
}
\]

Multiplication by `omega` is

\[
M_\omega=
\begin{pmatrix}0&1\\1&1\end{pmatrix},
\]

of order `3`, and

\[
\mathrm{Fr}M_\omega\mathrm{Fr}^{-1}=M_\omega^{-1}.
\]

This supplies the exact finite-field completion:

\[
\F_4^+\cong V_4,
\qquad
\F_4^\times\cong C_3,
\]

\[
\operatorname{AGL}(1,4)\cong A_4,
\qquad
\operatorname{A\Gamma L}(1,4)\cong S_4.
\]

**Guardrail:** `p_2/2p_2` is a nonreduced ramified ring, while `O_K/P_2` is the field `F_4`. They are not the same quotient ring. The exact bridge established so far is at the level of the common `F_2^2` carrier/action, with the transvection matrix becoming Frobenius in the field model.

---

## 3. Paper A / Cone material

The current v0.2 geometric mod-12 section is useful, but the ledger now contains a much stronger exact real-geometric bridge than the paper states.

Paper A coordinates are

\[
X=\frac{x-y}{2},
\qquad
Y=\sqrt{xy},
\qquad
T=\frac{x+y}{2},
\]

with null-cone equation

\[
T^2-X^2-Y^2=0.
\]

For fixed factor shell `xy=n`, rapidity `s` gives

\[
x=\sqrt n e^s,
\qquad
y=\sqrt n e^{-s},
\]

and the discriminant-12 return acts exactly as

\[
\boxed{x'=(2+\sqrt3)x,
\qquad
y'=(2-\sqrt3)y,}
\]

so

\[
\boxed{s'=s+\log(2+\sqrt3).}
\]

Thus every real Paper-A shell is invariant under the same Pell-unit Lorentz return.

The row/column parabola at factor level `u` is tangent to the fixed-`T` circle at

\[
\boxed{T=u/2,\qquad (X,Y)=(\pm u/2,0).}
\]

These tangent endpoints are exactly the expanding and contracting null eigenrays of the discriminant-12 boost.

**Recommendation:** add one concise geometric section before the arithmetic mod-12 shell. It should prove the Lorentz action on Paper-A null coordinates and identify the tangent endpoints with the boost eigenrays. This supplies the real geometric carrier that the current introduction gestures toward but does not actually use in the theorem chain.

The existing `U(12)={1,5,7,11}` figure should remain as a finite arithmetic section of that continuous real geometry, not as the source of the Lorentz action.

---

## 4. The `n=11` role

The current mod-12 shell correctly places

\[
(11,1),(1,11)
\]

on

\[
x+y=12,
\qquad
(T,X)=(6,\pm5).
\]

Later ledger work supplies a separate arithmetic reason that `11` is distinguished:

\[
N(1+2\sqrt3)=-11,
\]

and in the narrow class group

\[
[\mathfrak p_{11}]=[\mathfrak p_2].
\]

For the narrow Hilbert class field

\[
K=\Q(\zeta_{12}),
\]

this yields

\[
\operatorname{Art}_{K/F}(\mathfrak p_{11})=T_{11}.
\]

Since `11=-1 mod 12`, the corresponding cyclotomic automorphism is complex conjugation in the compatible labeling.

**Recommendation:** keep this as a corollary/example after the cyclotomic and ideal sections, not as a premise of the main theorem. It is a distinguished arithmetic section of the discriminant-12 structure, not what selects the structure.

---

## 5. Proposed theorem architecture for v0.3

The principal theorem should be decomposed into a short main theorem plus dependency propositions.

### Main theorem: Discriminant-12 return package

A suitable final statement is:

1. **Centered selection.** `K=H^{-1}` selects `tau=4` (`sigma=2`).
2. **Integral return.** The normalized primitive positive representative is `g_12`, with discriminant `12` and Pell unit `2+sqrt(3)`.
3. **Ideal realization.** `g_12` is multiplication by `2+sqrt(3)` on `p_2`; its centered generator is multiplication by `sqrt(3)`.
4. **Lorentz realization.** The return preserves `q_12` and acts on Paper-A null coordinates by `(x,y)->(lambda x,lambda^{-1}y)`.
5. **Cyclotomic realization.** `Z=(H+iI)/2` is multiplication by `zeta_12` on `P_2=p_2 O_K`, with an integral rank-4 matrix.
6. **Finite reduction.** The ramified return is a transvection/factor exchange and, in the `F_4` model, the same matrix is Frobenius; multiplication by reduced `zeta` supplies the order-3 action.

Then state the symmetry consequences as corollaries:

\[
V_4^{\rm tr}\rtimes C_2\cong D_8,
\]

for the Boolean translation-plus-reflection layer, and

\[
\operatorname{AGL}(1,4)\cong A_4,
\qquad
\operatorname{A\Gamma L}(1,4)\cong S_4
\]

for the finite-field affine/semilinear layer.

These groups must remain distinct.

---

## 6. Specific corrections required before v0.3

### [Audit] Typo in cyclotomic Galois action

The current mod-12 proposition contains

`zeta_12 -> zeta_12^{,r}`.

This should be

\[
\boxed{\zeta_{12}\mapsto\zeta_{12}^r.}
\]

### [Audit] Theorem proof-status mismatch

Current Theorem 2.1 includes clauses (v)–(vi), but the body says only clauses (i)–(iv) are proved and treats (v)–(vi) as a roadmap. This should no longer be patched with a forward reference; the later ledger now supplies the missing proofs. The next draft should include those proofs.

### [Audit] Outdated description of the four-state cyclotomic layer

The statement

\[
\OO_K/\Z[\sqrt3,i]\cong(\F_2)^2
\]

is correct as an additive quotient and useful for the index-4 gluing calculation, but it is no longer the most natural finite carrier for the operator. The natural operator reduction is

\[
\OO_K/\mathfrak P_2\cong\F_4,
\]

with reduced `zeta` of order `3`.

Both should appear, with their roles explicitly separated:

- `O_K/O_0`: index-4 integral-closure/gluing quotient;
- `O_K/P_2`: residue field carrying the reduced cyclotomic operator.

### [Audit] Do not conflate basis matrices

Use

\[
C_{\rm basis}=\begin{pmatrix}1&2\\1&1\end{pmatrix}
\]

for the ideal basis change and reserve

\[
C_{\rm rev}=\begin{pmatrix}1&0\\-2&-1\end{pmatrix}
\]

for the arithmetic reversor satisfying

\[
C_{\rm rev}gC_{\rm rev}^{-1}=g^{-1}.
\]

---

## 7. Material that should remain outside the principal theorem

The following are valuable but should not be dependencies of the algebraic theorem:

- the certified Suzuki determinant crossing `m_2(t_*)=2+sqrt(3)`;
- Clark/Cauchy/Fisher/Berry constructions;
- RH-sensitive analytic claims;
- continuous-resolution divisor-count asymptotics beyond the minimum geometry needed for the Cone bridge;
- speculative identification of finite phase data with physical quantum structure.

The principal paper can mention the Suzuki crossing in a final outlook paragraph as an independent analytic realization of the same selected Pell unit, but it should not be used in the proof.

---

## 8. Current dependency diagram

The strongest audited chain is now

\[
\boxed{
\begin{gathered}
K=H^{-1}
\Longleftrightarrow
\sigma=2
\Longrightarrow
\tau=4
\Longrightarrow
\Delta=12\\[2mm]
\Longrightarrow
\lambda=2+\sqrt3
\Longrightarrow
g_{12}=\times\lambda\text{ on }\mathfrak p_2\\[2mm]
\Longrightarrow
H=\times\sqrt3
\Longrightarrow
\mathcal Z=\times\zeta_{12}\text{ on }\mathfrak P_2\\[2mm]
\Longrightarrow
\bar\zeta\in\F_4^\times\cong C_3,
\qquad
\bar g=\mathrm{Frob}_{\F_4/\F_2}\\[2mm]
\Longrightarrow
A_4\subset S_4
\text{ finite affine/semilinear completion.}
\end{gathered}}
\]

In parallel, the same Pell unit acts on the real Cone as

\[
\boxed{
(x,y)\mapsto(\lambda x,\lambda^{-1}y),
\qquad
s\mapsto s+\log\lambda,
}
\]

with the Paper-A parabola/circle tangent endpoints equal to its null eigenrays.

This is the correct unifying architecture for the next principal-paper draft.

---

## 9. Audit status

**[D] Independently supported core:** centered-Cayley identities; trace selection; discriminant-12 return; Pell ideal action; Lorentz norm; basis conjugacy; cyclotomic polynomial; index-4 order inclusion; integral cyclotomic ideal carrier; ramified transvection; `F_4` Frobenius identification.

**[Audit] Required editorial repair:** theorem proof-status mismatch, cyclotomic Galois typo, separation of the two four-state quotients, explicit distinction between `C_basis` and `C_rev`.

**[I/O] Still outside the algebraic theorem:** analytic Suzuki realization and any RH-adjacent consequences.

**Conclusion:** the mathematical content now supports a substantially stronger and cleaner `Discriminant_12_Return_v0.3.tex`. The next action should be to draft that revision from this dependency architecture rather than incrementally patching v0.2.

---

**End of v13.188 principal-paper dependency audit.**