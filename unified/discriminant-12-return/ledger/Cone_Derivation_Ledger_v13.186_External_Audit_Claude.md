# Cone Derivation Ledger v13.186 — External Audit (Claude)

**Status:** Independent external audit of `unified/discriminant-12-return`, covering the
ledger v13.162 through v13.185, the `STATUS_2026-09-03_Operator_Cone_Unification.md`
research note, both `Discriminant_12_Return` paper drafts, the `Casimir_Null_Diamond`
companion, and the two other research notes.
**Date:** 2026-09-03
**Auditor:** Claude (Anthropic), acting as an independent reviewer at the author's
request. Every claim below was checked by direct recomputation (symbolic/matrix
algebra, exact-fraction arithmetic, or independent trace-form computation), not by
re-reading the prose.

Status labels: [S] source-established, [D] exact derived, [N-cert] certified numerical,
[I] interpretation, [O] open, [Audit] correction/limitation — reusing this project's own
convention.

---

## 0. Scope and method

This entry is not a new derivation. It is a line-by-line independent re-verification of
everything already on record, run once against the full backlog (v13.162–v13.182, the two
main papers, the Casimir note, the two research notes) and once against the material added
after that pass (v13.183–v13.185, `STATUS_2026-09-03`). Where a claim involved a nontrivial
computation, I reproduced it independently — including one full symbolic Galois-conjugate
trace-form computation for `disc(O_K)` vs `disc(Z[sqrt(3),i])`, done before I had read the
project's own version of that index-4 argument, as a genuine cross-check rather than a
transcription check.

**Overall verdict:** the project is unusually rigorous. Across roughly 30 documents and
several hundred individually boxed claims I found **one genuine content error**, **one
presentation gap** (not a math error), and a handful of cosmetic LaTeX bugs. Every
substantial theorem, matrix computation, ideal-theoretic argument, and numeric example I
re-derived from scratch checked out exactly.

---

## 1. Findings — backlog (v13.162–v13.182 and companion papers)

### 1.1 [Audit] Genuine error: red/purple cut labels swapped

**Location:** `Cone_Derivation_Ledger_v13.170_Pell_Mesh_Renormalization.md` (the delta
introducing Part XXXIII, "Paper-A Figure Source Recovery"), §137 "Recovered v2
construction."

The text states:

> For the red cut `8x+4y=32`, the edge-on equation is `-4X+12T=32`, and for its purple
> reflection `4x+8y=32`, `4X+12T=32`.

Direct substitution `x=T+X, y=T-X` gives the opposite:

\[
8x+4y=32 \;\Longrightarrow\; 12T+4X=32,
\qquad
4x+8y=32 \;\Longrightarrow\; 12T-4X=32.
\]

This is confirmed by the note's own worked example: the stated red-cut vertex
`(X*,T*)=(-1,3)` satisfies `4X+12T=32` (`-4+36=32` ✓) but **not** the equation the text
labels "red" (`-4X+12T=32` gives `4+36=40≠32`). The final numeric outputs
`(X*,T*,Y*²)=(-1,3,8)` are correct for the red cut; only the two labeled boxed formulas
immediately above them are transposed. This propagates into the figure-audit framing in
v13.178 only by citation, not by recomputation, so v13.178's own claims are unaffected.

**Recommended fix:** swap the two labels in v13.170 §137 (and check whether the actual
`fig_cutting_plane_3panel.py`/`foundations` copy encodes the correct — not the mislabeled —
assignment; the script itself was not re-audited for this specific point).

### 1.2 [Audit] Presentation gap, not a math error: `Discriminant_12_Return_v0.2.tex`

Theorem 2.1 (the six-part main theorem) states parts (v) (cyclotomic completion) and (vi)
(ramified Boolean reduction) inside the same formal theorem environment as parts (i)–(iv),
which do have complete proofs in the body. But §6 ("Roadmap for the arithmetic completion")
and the closing "Scope note" both say, correctly, that only the centered-Cayley and
Pell–Lorentz packages are fully proved in this draft. Every individual claim inside (v) and
(vi) is independently correct — I verified `Phi_12(Z)=0`, `O_K/Z[sqrt3,i]≅(F_2)^2`, the
factor-exchange reduction, and the XOR norm claim all elsewhere in the ledger — but a reader
who only reads the boxed Theorem 2.1 has no signal that two of its six clauses are asserted
rather than demonstrated in that document. Recommend either splitting Theorem 2.1 into
"proved" and "stated, proved in §6/companion" parts, or adding an inline forward-reference.

### 1.3 Cosmetic LaTeX bugs (would break compilation, not the mathematics)

- v13.163 delta §75: `(\epsilon_1,\epsilon_2)mapsto(\epsilon_2,\epsilon_1)` — missing `\`
  before `mapsto`.
- v13.166 delta §106: `\mathbb Z[H_{12}]cong\mathcal O_{\mathbb Q(\sqrt3)}` — missing `\`
  before `cong`.
- v13.166 delta §110: `K=H^{-1}iff\sigma=2` — missing `\` before `iff`.
- v13.165 delta §100: a `\boxed{...}` block is opened but the closing `\]` for its
  surrounding `\[...\]` display is missing before `## 101` begins.
- v13.168 delta §125–126: `(U,V)=(2x-y,\sqrt3,y)` — stray comma, should be
  `(2x-y,\sqrt3\,y)`.

None of these affect the underlying claims; all are simple, local fixes.

### 1.4 Everything else in the backlog: verified correct

For the record, since this entry may be the only thing read before trusting the rest: I
independently reproduced and confirmed, among others —

- The full centered-Cayley package: `H^2=(\tau^2/4-1)I`, `K=\frac{2}{\tau+2}H`,
  `KH=\frac{\tau-2}2 I`, and the unique self-reciprocal class `\sigma=2`.
- `g_{12}=A_1A_2` via continuant matrices, `H_{12}^2=3I`, the ramified ideal action on
  `\mathfrak p_2=(2,\sqrt3-1)=(1+\sqrt3)` (including independently confirming
  `(\sqrt3-1)=(2-\sqrt3)(1+\sqrt3)` with `2-\sqrt3` a unit, so both generators really do
  give the same ideal).
- `q_{12}(x,y)=2x^2-2xy-y^2`, discriminant `12`, the Lorentz factorization
  `2q_{12}=U^2-V^2`, and `g_{12}\in SO(q_{12},\mathbb Z)`.
- The `\mathcal O_K/\mathbb Z[\sqrt3,i]\cong(\mathbb F_2)^2` index-4 claim, checked by a full
  independent symbolic Galois-trace-form computation
  (`disc(\mathbb Z[\sqrt3,i])=2304`, `disc(\mathcal O_K)=144`, ratio `16`, index `4`) —
  done before reading the project's own change-of-basis-determinant argument in v13.183, as
  a genuine cross-check, and the two methods agree exactly.
- v13.182's ramified-basis-conjugacy computation `C^{-1}g_{12}C=\begin{pmatrix}2&3\\1&2\end{pmatrix}`,
  recomputed by direct matrix multiplication.
- The cycle-type argument (v13.163) disproving the original hoped-for "Boolean translation"
  identification and replacing it with the correct factor-exchange/`D_8` result — I
  recomputed the two permutations and their cycle types independently.
- The entire continuous-resolution/mesh calculus (v13.171–v13.176): every threshold formula
  (`\theta_1(M)`, `\theta_2(M)` and their asymptotics), the tangent-line/curvature
  decomposition (`mg=2\theta+2m(T-r)`, verified via two independent derivations that agree),
  and the specific `n=11` numerics — I recomputed every fractional arm length by hand and
  confirmed `\mathscr D_{11}(1)=29`, `\mathscr D_{11}(2)=89`, `\mathscr D_{11}(3)=181` exactly.
- The parabola/anti-diagonal tangency theorem (v13.177), and its consistency against the
  *actual* Python source: `foundations/fig_cutting_plane_3panel.py` does loop
  `range(2,Kmax+1,2)` (even `K` only) exactly as v13.178 describes, and the newer
  `figures/fig_cutting_plane_tangent_circle_audit.py` does implement the fix v13.178 §5
  recommended (`range(1,Kmax+1)`, all `K`) — confirmed against the real files, not just the
  ledger's description of them.
- The Casimir/null-diamond paper's `SU(2)`/`SU(1,1)` completion theorems and the
  four-corner oscillator transition cell — all four vertex formulas
  (`Y_{J+}^2=\delta^2(p+1)q`, etc.) independently re-derived from `T_c,X_c` and confirmed
  exact.
- Headline arithmetic in the two research notes: `D(11)=29`, `T_{12}-D(12)=43` (matches
  OEIS A161664's defining count), `L(1,\chi_{12})\approx0.760` via the class-number formula,
  and the `\langle J_x^2\rangle+\langle J_y^2\rangle=(R_+^2-m^2)-\tfrac14` ladder-operator
  identity.

---

## 2. Findings — new material since the backlog pass (v13.183–v13.185, `STATUS_2026-09-03`)

This material resolves the "index-4 half-integral defect" that earlier entries (e.g.
v13.165 §97, v13.166) had repeatedly flagged as an open `[Audit]` concern, and adds a
genuinely new and well-verified result: **the same order-2 transvection that reduces the
Pell return mod 2 is exactly the Frobenius matrix on `\mathbb F_4` in the natural basis
`(1,\omega)`.**

I checked every nontrivial computation independently:

- **v13.183 §1** (change-of-basis matrix `\mathcal B_{\rm cyc}\to\mathcal B_0`): recomputed
  the full `4\times4` determinant by cofactor expansion and got `-1/4` exactly, matching
  the claim and matching my own independent trace-form index computation from the backlog
  pass (§1.4 above) — two unrelated methods, same answer.
- **v13.183 §3** (companion matrix for `\times\zeta_{12}` on the ideal basis
  `\{\alpha,\alpha\zeta,\alpha\zeta^2,\alpha\zeta^3\}`): recomputed from
  `\zeta_{12}^4=\zeta_{12}^2-1` (itself checked against `\Phi_{12}(x)=x^4-x^2+1`) and
  confirmed the exact matrix given.
- **v13.183 §6**: confirmed `N_{K/\mathbb Q}(1+\sqrt3)=4` via the tower-of-fields norm
  formula, confirmed `\Phi_{12}(x)\equiv(x^2+x+1)^2\pmod2` by direct expansion, and
  confirmed the resulting `\bar\zeta^3=1` claim.
- **v13.184 §3** (the headline new result): with `\omega^2+\omega+1=0`, computed
  `\mathrm{Fr}(1)=1`, `\mathrm{Fr}(\omega)=\omega^2=1+\omega` directly, giving matrix
  `\begin{pmatrix}1&1\\0&1\end{pmatrix}` — **exactly** the ramified transvection `\bar g`
  from v13.163/v13.170/v13.182. Independently confirmed.
- **v13.184 §4**: recomputed the multiplication-by-`\omega` matrix
  `\begin{pmatrix}0&1\\1&1\end{pmatrix}`, confirmed order 3, and confirmed
  `\mathrm{Fr}\,M_\omega\,\mathrm{Fr}^{-1}=M_\omega^{-1}` via the standard Frobenius-acts-by-
  squaring argument.
- The group-theoretic identifications `\mathrm{AGL}(1,4)\cong A_4`,
  `\mathrm{A\Gamma L}(1,4)\cong S_4`, and `GL(2,2)\cong S_3` are all standard, correct facts
  about small permutation groups; I did not find an error in how they were applied here.
- **v13.185** ("Post-Bridge Audit") and **`STATUS_2026-09-03`** are themselves careful
  self-audits of v13.177–v13.184; I re-checked their claims (including
  `H=\begin{pmatrix}0&3\\1&0\end{pmatrix}` in the Pell basis, which follows correctly from
  `g_{12}-2I` in that basis) and found no errors and no overclaiming — their own `[Audit]`
  guardrails (e.g. "`\mathfrak p_2/2\mathfrak p_2` and `\mathcal O_K/\mathfrak P_2` are not
  the same quotient ring") are accurate and appropriately conservative.

**No errors found in v13.183–v13.185 or `STATUS_2026-09-03`.**

---

## 3. Consolidated recommendation list

1. Fix the red/purple swap in v13.170 §137 (§1.1 above).
2. Either split Theorem 2.1 of `Discriminant_12_Return_v0.2.tex` so parts (v)–(vi) are
   visibly distinguished from the fully-proved (i)–(iv), or add an explicit forward
   reference at the theorem statement (§1.2 above).
3. Fix the five cosmetic LaTeX typos listed in §1.3 (all are one-character fixes).
4. No action needed on v13.183–v13.185 or `STATUS_2026-09-03` — audited clean.

---

## 4. Audit guardrails carried into this entry

- This entry does not re-derive anything; it only verifies. Where a boxed claim above says
  "confirmed" or "recomputed," that means an independent symbolic or exact-arithmetic
  computation was performed by the auditor, separate from reading the ledger's own working.
- This audit does not evaluate whether the project's broader Suzuki/RH-adjacent material
  (outside `discriminant-12-return`) is sound; that was out of scope for this pass.
- Absence of a finding in this entry for a given file section means that section was read
  and its stated computations were checked; it does not mean every English-language
  interpretive remark was independently re-derived from first principles.

---

**End of v13.186 external audit.**
