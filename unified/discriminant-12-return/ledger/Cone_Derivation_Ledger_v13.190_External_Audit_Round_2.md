# Cone Derivation Ledger v13.190 — External Audit, Round 2 (Claude)

**Status:** Independent external re-audit covering everything added since v13.186:
v13.187 (external audit reconciliation), v13.188 (principal paper dependency audit),
v13.189 (principal paper v0.3 line audit), and the two new paper drafts
`Discriminant_12_Return_v0.3.tex` / `v0.3.1.tex`.
**Date:** 2026-09-03
**Auditor:** Claude (Anthropic), continuing the standing external-audit relationship
established in v13.186.

Status labels: [S]/[D]/[I]/[O]/[Audit] as in the project convention.

---

## 1. Reconciliation of v13.186's own errors — confirmed correct

v13.187 identified a provenance error in v13.186: the red/purple mislabeling was correctly
attributed to `Cone_Derivation_Ledger_v13.170_Audited_Consolidation.md`, Part XXXIII §137,
not to `Cone_Derivation_Ledger_v13.170_Pell_Mesh_Renormalization.md` as v13.186 stated. This
is accepted. v13.186 cited the wrong filename for a correctly-identified mathematical error;
the filename `..._Pell_Mesh_Renormalization.md` actually belongs to v13.180's title and does
not contain the figure-recovery section at all.

v13.187 also asserted, independently of the ledger's own prose, that the *actual running
figure generator* (`unified/fig_cutting_plane_3panel.py`) was never affected by the labeling
swap. **This was independently re-checked here** by reading the live script rather than
trusting the claim:

```
curves = [
    dict(a=8, b=4, c=32, color="#b3211a", label=r"$8x+4y=32$"),   # red
    dict(a=4, b=8, c=32, color="#7a3db8", label=r"$4x+8y=32$"),   # purple
]
Tb = (curve["c"] + (curve["b"] - curve["a"]) * Xb) / (curve["a"] + curve["b"])
Xstar, Tstar = (2 - 4) / 2.0, (2 + 4) / 2.0   # commented: on the red cut
```

Substituting: red `(a,b,c)=(8,4,32)` gives `12T+4X=32`; purple `(4,8,32)` gives
`12T-4X=32`; vertex `(X*,T*)=(-1,3)`. This matches v13.187's claim exactly and confirms the
code was always correct — only the historical consolidated-ledger prose had the labels
swapped. **[External-confirmed.]**

---

## 2. v13.188 (dependency audit) and v13.189 (line audit): no errors found

Both are careful, accurate documents. I re-verified the specific new claims each one adds
beyond what v13.186 already covered:

- **v13.188**, the invertibility criterion `\det(g+I)=\tau+2`, hence `g+I` invertible
  `\iff\tau\ne-2` for `\det g=1` — confirmed via the eigenvalue product identity
  `(1+\lambda_1)(1+\lambda_2)=1+\tau+1=\tau+2`.
- **v13.189 §9**, the basis-compatible `\mathbb F_4` identification
  `f_1\mapsto1,\ f_2\mapsto\omega^2` (hence `e_1\mapsto\omega,\ e_2\mapsto\omega^2` via
  `e_1=f_1+f_2,\ e_2=f_2\pmod2`): recomputed independently. Frobenius in basis
  `(1,\omega^2)` is `\mathrm{Fr}(1)=1`, `\mathrm{Fr}(\omega^2)=\omega^4=\omega=\omega^2+1`,
  giving matrix `\begin{pmatrix}1&1\\0&1\end{pmatrix}=\bar g` exactly. In basis
  `(\omega,\omega^2)`, `\mathrm{Fr}(\omega)=\omega^2` and `\mathrm{Fr}(\omega^2)=\omega`,
  giving the swap matrix `P` exactly. Both confirmed.
- **v13.189 §9**, the new XOR = field-trace promotion: independently recomputed
  `\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(1)=1+1^2=0`,
  `\operatorname{Tr}(\omega)=\omega+\omega^2=1`,
  `\operatorname{Tr}(\omega^2)=\omega^2+\omega^4=\omega^2+\omega=1` (using `\omega^2=\omega+1`,
  char. 2). Hence `\operatorname{Tr}(x+y\omega^2)=y` in the ramified basis and
  `\operatorname{Tr}(\epsilon_1\omega+\epsilon_2\omega^2)=\epsilon_1\oplus\epsilon_2` in the
  Boolean/Pell basis — both confirmed exactly as stated.

**[Audit — minor overclaim in v13.189, not previously flagged.]** v13.189 §11 calls
`\mathbin{\mathrm{xor}}` "a likely compile error," reasoning that "standard LaTeX/amsmath does
not define `\xor` by default." This conflates `\xor` (an undefined macro, which would indeed
error) with `\mathrm{xor}` (which is standard, always-valid LaTeX: `\mathrm{<text>}` typesets
its argument as literal upright text and never requires that text to be a predefined command).
`\mathbin{\mathrm{xor}}` would have compiled without error, simply rendering "xor" in roman
font with binary-operator spacing. The recommendation to switch to `\oplus` is still good
practice (consistency with the rest of the paper), so no action was needed regardless — this
is noted only for the record, since the stated *reason* was not quite right.

---

## 3. `Discriminant_12_Return_v0.3.1.tex`: audited clean

This is now the strongest draft. I re-verified it independently rather than trusting that the
v13.188/v13.189 repair list was applied correctly:

- Theorem statement is correctly two-staged: clause structure covers arbitrary `g\in SL_2(\Q)`
  for the universal centered-Cayley identities and the `\sigma=2` selection, then explicitly
  introduces the normalized `g_{12}` before stating (i)-(vi). This resolves the presentation
  gap flagged in the original v13.186 audit.
- `\oplus` is used consistently for XOR throughout (§7); no `\mathrm{xor}` remains.
- The compatible additive `\mathbb F_4` identification and the XOR = field-trace result
  (§7.1) are present and match my independent recomputation in §2 above.
- The `T_{11}\in\operatorname{Gal}(K_{12}/F)` justification (§8) is now explicit: `T_{11}`
  fixes `\sqrt3` and acts as `\zeta_{12}\mapsto\zeta_{12}^{-1}` since `11\equiv-1\pmod{12}`,
  correctly placing it inside the quadratic subgroup rather than leaving a category jump.
- All previously-verified core content (centered-Cayley package, `g_{12}=A_1A_2`,
  `H_{12}^2=3I`, ideal action on `\mathfrak p_2`, `q_{12}` and its Lorentz form, the Cone
  boost `x'=\lambda x,\,y'=\lambda^{-1}y`, the tangent-eigenray theorem, the cyclotomic
  companion matrix, the index-4 calculation, and the Frobenius/`\mathbb F_4` bridge) is
  carried through unchanged and remains correct.

**No new errors found in `v0.3.1.tex`.**

---

## 4. Updated overall status

Combining this round with v13.186: across the full project (backlog through v13.185, plus
v13.186-v13.190 and both new paper drafts), the only substantive content error found in any
of this remains the historical v13.170 prose mislabeling, which does not affect the live code,
any downstream derivation, or the current paper draft. Everything added in this second round
— the reconciliation, both internal audits, and the resulting `v0.3.1.tex` — is independently
confirmed correct.

**Recommendation:** `Discriminant_12_Return_v0.3.1.tex` is in good shape for a compile check
and, contingent on that, for treating as the stable principal-paper draft going forward.

---

**End of v13.190 external audit, round 2.**
