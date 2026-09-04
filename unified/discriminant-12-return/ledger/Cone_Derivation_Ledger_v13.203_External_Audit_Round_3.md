# Cone Derivation Ledger v13.203 — External Audit, Round 3 (Claude)

**Status:** Independent external audit of everything added since v13.190: v13.191–v13.202
(12 ledger entries), the new `Note_AreaDistortion_AMGM_Cone` branch, `PaperA_ConicTheorem`
v2.2/v2.3, `PaperB_EigenCoordinates`/`_v2`, and the principal-paper progression through
`Discriminant_12_Return_v0.3.3.tex`.
**Date:** 2026-09-04
**Auditor:** Claude (Anthropic), continuing the standing external-audit relationship from
v13.186/v13.190.

Status labels: [S]/[D]/[I]/[O]/[Audit] as in the project convention.

---

## 0. Scope of this pass

This round covers substantially more ground than v13.186/v13.190: a new "area distortion"
measure-theory branch (v13.196–v13.200), a discrete divisor-staircase push-forward theory
(v13.197), a canonical continuous divisor chamber (v13.200), and a serious audit-and-repair
cycle on the foundational `PaperB_EigenCoordinates.tex` (v13.201–v13.202). Verification
method: independent symbolic/numeric recomputation, not review of the prose. Several results
were checked by writing and running independent Python (including one `sympy` symbolic
check) rather than by hand, and are reported as such below.

**Overall verdict: exceptionally clean round.** Across 12 new ledger entries and several
thousand new lines of mathematics, **no new mathematical error was found**. One documentation
hygiene issue is flagged (a genuine numbering collision, twice). Separately, v13.201–v13.202
correctly identify and repair several *pre-existing* errors in the original
`PaperB_EigenCoordinates.tex` — those findings were independently re-verified here and are
sound.

---

## 1. [Audit] Numbering collisions (hygiene only, not a correctness issue)

Three independent pairs of ledger files share a version number:

- `Cone_Derivation_Ledger_v13.199_Exact_Angular_Inverse_Measure.md` and
  `Cone_Derivation_Ledger_v13.199_Weighted_Circle_Measure.md`;
- `Cone_Derivation_Ledger_v13.200_Area_Branch_Publication_Checkpoint.md` and
  `Cone_Derivation_Ledger_v13.200_Parabola_Secant_Divisor_Chamber.md`;
- `Cone_Derivation_Ledger_v13.201_Paper_B_Orbit_Power_Map_Audit.md` and
  `Cone_Derivation_Ledger_v13.201_Paper_A_Foundation_Closure.md` (the latter landed after
  this audit round was already underway; see §6 below).

In every case the two same-numbered files are mathematically consistent with each other and
do not contradict one another (the two `v13.199` files independently derive the identical
result `dx\,dy=2\cos\theta\,dX\,dY`; the two `v13.201` files cover disjoint topics, Paper A
versus Paper B), so this reads as parallel derivation/work threads landing under the same
next-available number rather than any actual conflict. Recommend renumbering members of each
pair (e.g. to v13.199b/v13.200b/v13.201b) so the sequence stays a clean total order, and
picking the *next unused* integer (currently v13.204, after this entry) for future entries
rather than reusing the most recent number.

---

## 2. Area-distortion branch (v13.196–v13.200): independently re-derived, all correct

This is a substantial new self-contained piece of geometry — the exact relationship between
factor-plane (Lebesgue) area and the flat/circle-view area under
`F(x,y)=((x-y)/2,\sqrt{xy})` — and it holds up completely under independent re-derivation.

- **Jacobian and surface element** (v13.196 §2): re-derived
  `\left|\partial(X,Y)/\partial(x,y)\right|=T/(2Y)` directly from the partial derivatives,
  and `dA_{\rm cone}=\sqrt2\,dX\,dY` from the standard graph-surface-element formula applied
  to `T=\sqrt{X^2+Y^2}` (using `1+f_X^2+f_Y^2=1+T^2/T^2=2` on the cone). Both match exactly.
- **Triangle/half-disk ratio `\pi/4`** (v13.196 §3): confirmed
  `\operatorname{Area}(\Delta_S)=S^2/2`, `\operatorname{Area}(F(\Delta_S))=\pi S^2/8` directly.
- **`\operatorname{Area}(B_n)=n\log n+n+1`** (v13.196 §4): re-derived from scratch by direct
  integration, splitting the shell triangle into the two linear "wing" pieces
  (`x\in[0,1]` and `x\in[n,n+1]`, contributing `n+1` total) plus the central hyperbolic piece
  (`x\in[1,n]`, contributing `n\log n`). Matches exactly, including via the internal
  consistency check `\operatorname{Area}(B_n)+\operatorname{Area}(C_n)=(n+1)^2/2`.
- **Circular cap formula** (v13.196 §5): confirmed against the standard circular-segment
  area formula `R^2\arccos(d/R)-d\sqrt{R^2-d^2}` with `R=(n+1)/2`, `d=\sqrt n`.
- **Rapidity/angle bridge** (v13.196 §7): re-derived `\sin\theta=\tanh s`,
  `\cos\theta=\operatorname{sech}s`, `d\theta=\operatorname{sech}s\,ds`, and confirmed
  `\int_0^\infty\operatorname{sech}t\,dt=\pi/2` (standard Gudermannian-function fact).
- **Reciprocal area/angle pairing** (v13.196 §8): re-derived `dx\,dy=2\rho\,d\rho\,ds` and
  `dX\,dY=\rho\cosh s\,d\rho\,ds` from the Jacobians of `x=\rho e^s,\,y=\rho e^{-s}` and
  `X=\rho\sinh s,\,Y=\rho,\,T=\rho\cosh s` respectively, giving
  `dX\,dY/dx\,dy=\cosh(s)/2` exactly as claimed.
- **Discrete staircase push-forward** (v13.197): independently re-derived the column-image
  formula
  `W_k(h)=\tfrac13\left[\sqrt h\,(k^{3/2}-(k-1)^{3/2})+h^{3/2}(\sqrt k-\sqrt{k-1})\right]`
  by direct double integration of the Jacobian over `[k-1,k]\times[0,h]`. Then, using this
  formula independently in a fresh Python script, recomputed
  `\mathcal W_T(11)`, `\mathcal W_H(11)`, `\mathcal W_D(11)`, `\mathcal W_A(11)` and their
  ratios to `T_{11},11H_{11},D(11),A_{11}` — **every value matched the ledger's reported
  figure to all displayed digits** (e.g. `\mathcal W_T(11)=51.26352005163986` against the
  claimed `51.2635200516399`).
- **v13.198's comparison table**: independently recomputed `D(n)` for
  `n\in\{10,11,20,50,100,1000,10000\}` together with `n\log n`,
  `\widetilde W_L(n)=\tfrac{8}{3\pi}(n-1)\sqrt n`, and `M(n)=n\log n+(2\gamma-1)n` — every
  table entry matched exactly, including
  `|D(11)-11\log11|\approx2.623152` and `|D(11)-\widetilde W_L(11)|\approx0.847614`. The
  asymptotic obstruction argument (`\widetilde W_L(n)=\Theta(n^{3/2})` versus
  `D(n)\sim n\log n`, hence the ratio diverges) is elementary and correct.
- **Exact angular inverse measure** (v13.199, both copies): re-derived
  `J=T/(2Y)=1/(2\cos\theta)` from `Y=T\cos\theta`, hence `dx\,dy=2\cos\theta\,dX\,dY`, and
  confirmed the whole-shell consistency check
  `\int_{-\pi/2}^{\pi/2}\int_0^R 2T\cos\theta\,dT\,d\theta=2R^2=S^2/2`. Everything downstream
  in these two files (the exact recovery statements for `n\log n`, `T_n`, `D(n)`, etc.) is a
  direct, automatic consequence of this one Jacobian identity via the ordinary
  change-of-variables theorem, not a separate claim requiring its own check.
- **Parabola–secant divisor chamber** (v13.200, second copy): re-derived the row/column-1
  parabola boundary `X_R-X_L=Y^2-1`, then by direct integration confirmed
  `P_n=\int_1^{\sqrt n}(Y^2-1)\,dY=\tfrac{n^{3/2}-3\sqrt n+2}{3}` and the factor-plane area
  `n\log n-n+1`, plus the `n=11` numerics (`P_{11}\approx9.510999441`,
  `11\log11-10\approx16.376848`).

No error, of any kind, was found anywhere in this branch. This is a solid, self-contained
addition and the branch's own decision to "freeze" it (v13.199/v13.200's stopping-rule
sections) after reaching the exact `2\cos\theta` result is the right call — it is a clean,
complete piece of work that does not need further speculative extension.

---

## 3. Paper A v2.2/v2.3 audit (v13.195): confirmed, plus one independent cross-check

The one new computational claim beyond what was already verified in earlier rounds — the
ellipse semi-axis formulas
`b_{\rm semi}=c/(2\sqrt{ab})`, `a_{\rm semi}=c\sqrt{2(a^2+b^2)}/(4ab)` — was independently
re-derived here by computing the literal 3D Euclidean distance between the two `Y=0`
endpoints `(X,Y,T)=(c/(2a),0,c/(2a))` and `(-c/(2b),0,c/(2b))` (the honest way to measure
the "true" semi-axis of an ellipse embedded in the ambient `(X,Y,T)` space, as opposed to a
flat-projection distance). This gives
`a_{\rm semi}=c\sqrt{2(a^2+b^2)}/(4ab)` exactly, matching the paper, and the resulting
eccentricity formula `e=|a-b|/\sqrt{a^2+b^2}` was likewise confirmed from
`e^2=1-b_{\rm semi}^2/a_{\rm semi}^2`.

---

## 4. Paper B audit and v2 repair (v13.201–v13.202): independently re-verified as sound

This is a genuinely important pass: it audits *pre-existing* content in the original
`foundations/PaperB_EigenCoordinates.tex` — the same file read earlier in this external-audit
relationship, before the discriminant-12 branch existed — and finds several real issues, all
of which were independently re-checked here rather than taken on trust:

- **`Gm=0` proof-text error**: recomputed `G_{a,b}m` symbolically for a general vector
  `m=(m_1,m_2,m_3)` with `\alpha=a+b,\gamma=a-b`, getting
  `Gm=(-\alpha m_2,\ \alpha m_1+\gamma m_3,\ \gamma m_2)`. This exactly matches v13.201's
  restated system, and confirms the *original* manuscript's stated intermediate equations
  (`\gamma m_3=0` and `\gamma m_1=0`, alongside `\alpha m_1+\gamma m_3=0`) do not correctly
  describe `Gm=0` for the general vector — while the paper's final kernel-vector *answer*,
  `m=(a-b,0,-(a+b))`, does independently check out (`Gm=0` verified directly by substitution).
  So the correction is right: the theorem survives, the written derivation did not.
- **Power-map normalization dependence**: this is the most substantive finding, and it is
  correct. Rescaling the cutting equation `(a,b,c)\mapsto(\kappa a,\kappa b,\kappa c)`
  represents the same geometric line, but reconstructing the "target" line from the
  `\kappa`-scaled representative and then dividing back by `\kappa` gives a target level of
  `(\kappa c)^n/\kappa=\kappa^{n-1}c^n`, versus `c^n` from the unscaled representative —
  confirmed symbolically here that the ratio between these two is exactly `\kappa^{n-1}`,
  which is `\ne1` for `\kappa\ne1,\,n\ne1`. The original "canonical power map" claim was
  therefore genuinely representative-dependent, not just an unstated convention.
- **"No power map exists at all" for rows/columns**: confirmed this is an overclaim as
  literally stated — the elementary map `(x,y)\mapsto(x^n,y^n)` trivially sends a row `x=c`
  to `x=c^n`. What actually fails at `ab=0` is specifically the diagonal eigen-coordinate
  construction (the generator is nilpotent, so it has no elliptic/hyperbolic eigen-coordinate
  to raise to a power), not every conceivable power map. The corrected wording is accurate.
- **v13.202's `v2` repair**: re-derived the factorizations
  `\zeta=(u+iv)^2` (with `u=\sqrt{ax}`, `v=\operatorname{sgn}(Y)\sqrt{by}`, `a,b>0`) and
  `\eta_\pm=(u\mp v)^2` (hyperbolic case) by direct expansion, confirming both exactly.
  Confirmed the future-cone-preservation arguments: elliptic case via
  `|P_n|=|\operatorname{Re}(\zeta^n)|\le|\zeta^n|=c^n`, giving
  `ax_n=(c^n+P_n)/2\ge0` and `by_n=(c^n-P_n)/2\ge0`; hyperbolic case via AM–GM,
  `P_n=(\eta_+^n+\eta_-^n)/2\ge\sqrt{(\eta_+\eta_-)^n}=|c|^n=|Q_n|`, giving
  `ax_n,\beta y_n\ge0`. Confirmed the projective normalizations `z=\zeta/c` (`|z|=1`) and
  `\xi_\pm=\eta_\pm/|c|` (`\xi_+\xi_-=1`) are invariant under positive rescaling of
  `(a,b,c)`, and confirmed the normalized generator `\widehat G_{a,b}=G_{a,b}/(2\sqrt{\pm ab})`
  has eigenvalues exactly `\pm i` (elliptic) or `\pm1` (hyperbolic), and is itself invariant
  under the same rescaling.

**No errors found in v13.202's repair.** The corrected `PaperB_EigenCoordinates_v2.tex` is
mathematically sound wherever checked.

---

## 5. Infrastructure entries (v13.191–v13.194): no math claims, correctly incorporate prior feedback

These four entries (compile check, publication build baseline, figure integration,
exposition/references) contain no new mathematical claims to verify. Worth noting: v13.191
explicitly and correctly restates the v13.190 correction about `\mathrm{xor}` not actually
being a LaTeX compile error — good, the record is now consistent on that point.

---

## 6. Late addition: Paper A foundation closure (second `v13.201`)

While this audit round was in progress, a further commit landed adding
`Cone_Derivation_Ledger_v13.201_Paper_A_Foundation_Closure.md`, a small correction to
`PaperA_ConicTheorem_v2.2.tex`, and a matching visual cleanup of
`fig_divisor_summatory_11_3panel.py`. Checked before finalizing this entry:

- **Degenerate `ab<0,c=0` case**: the entry adds the missing apex case to the conic
  classification theorem — at `c=0` with `ab<0`, `Y^2=xy=-(a/b)x^2` factors into two lines
  through the origin (since `-a/b>0` exactly when `ab<0`), of which only one ray survives on
  the positive-factor quadrant. This is straightforward, correct algebra and closes exactly
  the gap v13.195 (§5 in this round's earlier notes) had already flagged as needing attention.
- **`n=11` triangular-domain wording**: correctly fixes a real (if minor) error — the
  original text said the anti-diagonal *line* `x+y=12` "contains" `T_{11}=66` points, but the
  line itself contains only the 11 lattice points `(x,12-x)`; it is the *triangular region*
  `x+y\le12` that contains the 66-point count `T_{11}=1+\cdots+11`. The corrected wording
  ("bounds the triangular domain, which contains...") is accurate.
- **Figure script update**: cosmetic/visual refactor of the plotting code to display all
  integer `K` circles (not just even `K`), consistent with the same fix already applied
  elsewhere in the project (v13.178's recommendation, `fig_cutting_plane_tangent_circle_audit.py`);
  no numerical or geometric claim changed.

No error found in this addition either.

---

## 7. Updated overall status

Combining this round with v13.186/v13.190: across the full `discriminant-12-return`
directory plus the newly-touched `PaperA_ConicTheorem` and `PaperB_EigenCoordinates`
foundations, the only uncorrected issue on record remains the historical v13.170 prose
mislabeling (non-propagating, already reconciled in v13.187). Everything added in this
round — a substantial new area-distortion geometry branch, the Paper A degenerate-case and
wording fixes, and a real audit-and-repair cycle on Paper B — is independently confirmed
correct.

**Recommendation:** resolve the three numbering collisions (§1) when convenient; no other
action required from this pass.

---

**End of v13.203 external audit, round 3.**
