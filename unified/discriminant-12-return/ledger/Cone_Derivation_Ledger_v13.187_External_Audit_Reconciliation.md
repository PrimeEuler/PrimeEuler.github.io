# Cone Derivation Ledger v13.187 — External Audit Reconciliation

**Status:** Internal reconciliation of the independent v13.186 external audit  
**Date:** 2026-09-03  
**Scope:** Recheck external findings against the repository, classify corrections, and preserve historical provenance.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[N-cert]** rigorous finite numerical/computer-assisted
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation
- **[External-confirmed]** independently reproduced in v13.186 and rechecked here

---

## 1. Reconciliation policy

The external audit in v13.186 is treated as an independent source of verification, not as an authority that silently rewrites the historical ledger. Each reported correction is therefore checked against the current repository before incorporation.

The principal outcome is:

\[
\boxed{
\text{v13.186 substantive verification accepted; one location label corrected here.}
}
\]

The recent operator/Frobenius/cyclotomic bridge v13.183–v13.185 remains unchanged.

---

## 2. [Audit] Red/purple edge-on equations: external correction confirmed

The historical consolidated ledger contains, in `Cone_Derivation_Ledger_v13.170_Audited_Consolidation.md`, Part XXXIII §137, the statements

\[
8x+4y=32\Longrightarrow -4X+12T=32,
\]

and

\[
4x+8y=32\Longrightarrow 4X+12T=32.
\]

These labels are reversed.

Using

\[
x=T+X,\qquad y=T-X,
\]

we obtain generally

\[
ax+by=(a+b)T+(a-b)X.
\]

Therefore

\[
\boxed{8x+4y=32\Longrightarrow 12T+4X=32,}
\]

and

\[
\boxed{4x+8y=32\Longrightarrow 12T-4X=32.}
\]

The red maximum `(x,y)=(2,4)` gives

\[
(X,T)=(-1,3),
\]

and indeed

\[
12(3)+4(-1)=32.
\]

So the external audit's mathematical correction is exact.

### 2.1 [Audit] Location correction to v13.186

The external audit names the affected file as `Cone_Derivation_Ledger_v13.170_Pell_Mesh_Renormalization.md`. That filename is not the repository location of the error.

The actual affected historical file is

`Cone_Derivation_Ledger_v13.170_Audited_Consolidation.md`, Part XXXIII §137.

The separate file

`Cone_Derivation_Ledger_v13.170_Rational_Refinement.md`

does not contain this figure-source-recovery section.

Thus:

\[
\boxed{
\text{v13.186 correction is mathematically right but its file-location label is wrong.}
}
\]

This is a provenance correction only.

---

## 3. [External-confirmed] Actual figure generator is already correct

The current source `unified/fig_cutting_plane_3panel.py` stores the two cuts as

- red: `(a,b,c)=(8,4,32)`;
- purple: `(a,b,c)=(4,8,32)`.

Its side-view formula is

```python
Tb = (c + (b - a) * Xb) / (a + b)
```

which is exactly

\[
T=\frac{c-(a-b)X}{a+b}.
\]

Hence the script implements

\[
\text{red}:\quad 12T+4X=32,
\]

\[
\text{purple}:\quad 12T-4X=32.
\]

It also places the red maximum at

\[
(X_*,T_*)=(-1,3).
\]

Therefore the defect is confined to the historical prose/formula labels in v13.170 consolidated ledger; it does **not** infect the current figure generator.

\[
\boxed{
\text{figure code correct; historical ledger labels swapped.}
}
\]

This also confirms v13.178's later source-level geometric audit is not invalidated by the swap.

---

## 4. [Audit/editorial] Main-theorem proof-status gap accepted

The external audit's observation about `Discriminant_12_Return_v0.2.tex` is accepted as an editorial issue rather than a mathematical error.

The six-part theorem places the cyclotomic and ramified-Boolean clauses beside the fully proved centered-Cayley/Pell-Lorentz clauses, while the draft's own roadmap and scope note distinguish their proof status.

The underlying clauses are supported elsewhere in the ledger and have now also been independently rechecked in v13.186. The issue is therefore reader-facing theorem architecture.

**Publication action:** in the next paper-draft revision, either

1. split the theorem into a proved core plus arithmetic-completion theorem/corollary; or
2. retain one theorem but add explicit forward references identifying where clauses (v)–(vi) are proved.

No mathematical claim is withdrawn.

---

## 5. [Audit/editorial] Cosmetic LaTeX findings accepted as maintenance items

The five local syntax defects reported in v13.186 are accepted as cosmetic historical-ledger defects:

1. missing `\\mapsto` slash in v13.163 delta §75;
2. missing `\\cong` slash in v13.166 delta §106;
3. missing `\\iff` slash in v13.166 delta §110;
4. missing display close in v13.165 delta §100;
5. stray comma in `(U,V)=(2x-y,\\sqrt3,y)` in v13.168 delta §§125–126.

These do not change any derived formula. Historical ledgers are retained for provenance; corrected formulas in later audited consolidations/current paper sources take precedence.

---

## 6. [External-confirmed] Independent reproduction ledger

The following high-value structures now have two derivational tracks: the project's internal derivation and the independent v13.186 recomputation.

### 6.1 Centered-Cayley package

\[
H^2=\left(\frac{\tau^2}{4}-1\right)I,
\qquad
K=\frac{2}{\tau+2}H,
\qquad
KH=\frac{\tau-2}{2}I,
\]

with unique self-reciprocal shear

\[
\boxed{\sigma=2.}
\]

### 6.2 Discriminant-12 return and ideal action

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix},
\qquad
H_{12}^2=3I,
\]

and the ramified ideal realization on

\[
\mathfrak p_2=(2,\sqrt3-1)=(1+\sqrt3).
\]

### 6.3 Arithmetic Lorentz form

\[
q_{12}(x,y)=2x^2-2xy-y^2,
\qquad
2q_{12}=U^2-V^2,
\]

with

\[
g_{12}\in SO(q_{12},\mathbb Z).
\]

### 6.4 Cyclotomic lattice index

The project derived

\[
[\mathcal O_K:\mathbb Z[\sqrt3,i]]=4
\]

by an explicit basis determinant. The external audit independently obtained

\[
\operatorname{disc}(\mathbb Z[\sqrt3,i])=2304,
\qquad
\operatorname{disc}(\mathcal O_K)=144,
\]

so

\[
\frac{2304}{144}=16=4^2.
\]

This is a particularly strong independent cross-check because the two computations use different invariants.

### 6.5 Ramified basis conjugacy

The external audit independently recomputed

\[
\boxed{
C^{-1}g_{12}C=
\begin{pmatrix}2&3\\1&2\end{pmatrix}.
}
\]

### 6.6 Continuous-resolution and tangent geometry

The external audit independently confirmed the threshold, tangent-line, curvature-correction, and `n=11` counting formulas, including

\[
\mathscr D_{11}(1)=29,
\qquad
\mathscr D_{11}(2)=89,
\qquad
\mathscr D_{11}(3)=181.
\]

It also checked the actual Python sources behind the even-`K` shell audit and the all-`K` tangent-circle audit variant.

### 6.7 New cyclotomic/Frobenius bridge

The external audit independently confirmed the recent chain

\[
\mathcal Z=\times\zeta_{12},
\]

on the integral cyclotomic ideal lattice, together with

\[
\mathcal O_K/\mathfrak P_2\cong\mathbb F_4,
\]

multiplication by `\omega` of order `3`, and Frobenius

\[
\mathrm{Fr}(z)=z^2
\]

having matrix

\[
\boxed{
\begin{pmatrix}1&1\\0&1\end{pmatrix}
}
\]

in the basis `(1,\omega)`, exactly matching the ramified transvection matrix.

This is now independently reproduced rather than merely internally cross-checked.

---

## 7. Current confidence hierarchy

The strongest publication-ready core now consists of claims satisfying all three conditions:

1. exact internal derivation;
2. explicit audit guardrails and carrier distinctions;
3. independent external recomputation.

This includes the centered-Cayley theorem, discriminant-12 Pell/ideal realization, Lorentz form, cyclotomic ideal lattice, mod-2 ramified transvection, and Frobenius/`\mathbb F_4` action bridge.

The Paper A continuous-resolution/tangent package is also independently reproduced, but its role in the discriminant-12 principal paper remains a structural/geometric bridge rather than a proof of the arithmetic theorem.

---

## 8. Guardrails after reconciliation

1. The external audit does not convert interpretations into theorems merely by agreeing with them.
2. Independent reproduction raises confidence in exact algebraic claims but does not broaden their scope.
3. `\mathfrak p_2/2\mathfrak p_2` and `\mathcal O_K/\mathfrak P_2\cong\mathbb F_4` remain distinct quotient rings.
4. Equality of the Frobenius and transvection **matrices in specified bases** is exact; it is not a claim that the two quotient rings are canonically identical.
5. The red/purple equation swap is a historical-ledger labeling error only; the current figure source implements the correct equations.
6. v13.186's filename for that error is itself corrected by this reconciliation.
7. No RH claim follows from the independent audit or from the discriminant-12 package.

---

## 9. Reconciled status

After incorporating the external audit, there is no known substantive algebraic failure in the discriminant-12 return package.

The one confirmed content error is local and nonpropagating:

\[
\boxed{
\text{red/purple edge-on labels swapped in historical v13.170 consolidated prose.}
}
\]

The actual code, numeric maximum, later tangent geometry, operator arithmetic, cyclotomic lattice, and finite-field bridge remain intact.

The next appropriate task is therefore editorial rather than exploratory:

\[
\boxed{
\text{audit the principal-paper draft against the independently verified theorem chain.}
}
\]

The goal should be to make the paper's theorem hierarchy match the now-audited dependency hierarchy, while keeping the Cone/Paper-A material as an exact geometric bridge with clearly bounded scope.

---

**End of v13.187 external-audit reconciliation.**
