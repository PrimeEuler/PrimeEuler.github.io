# Cone Derivation Ledger v14.622 — External Audit Round 326: v14.620/v14.621 (ħ-as-unit-circle, Energy AM/GM + G Ingredients) Verified

**Date:** 2026-10-19
**Track:** External Audit
**Status:** [V] v14.620 (ħ as the unit circle; quantization pattern as AM/GM splits) and v14.621 (energy follows the AM/GM split; the G ingredients assembled) are Sandbox interpretive deposits under Jeremy's explicit authorization — not discriminant-12-return certification work; both correctly flag `G_derived=false`, `hierarchy_generator_found=false`, `factorised_G_observable_exists=false`, `open_item_count_change=false`. All file hashes verified exact. Every algebraic and numerical claim independently re-derived and confirmed correct, including an exact digit-for-digit match (every one of 30 displayed digits) of this entry's own independently-computed $\psi$ against the note's quoted value. No defect of substance found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–619, v14.550 (origin of the two open $G$ items), v14.616 (this auditor's own K/G status note, cited by both entries), v14.619 (live HEAD at this round's start).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `182f2a3...` (v14.621), matching local HEAD after fast-forward merge; live ledger max was v14.621. v14.622 is next-free. No collision.

---

## 1. v14.620 — ħ as the unit circle

**File hash:** `research-notes/Hbar_as_Unit_Circle.md` re-hashed and matches the manifest (`2b3cb68d...`).

**Consecutive-split anchor, re-derived independently (sympy, symbolic, not numeric spot-check):** for $(n,k)=(j{+}1,j)$, $\mathrm{AM}=j+\tfrac12$, $\mathrm{GM}^2=j(j+1)$, offset $=\tfrac12$ identically. Checked $\mathrm{AM}^2-\mathrm{offset}^2-\mathrm{GM}^2$ symbolically for general $j$: **identically zero**, confirming $(j+\tfrac12)^2-\tfrac14=j(j+1)$ exactly, independent of $j$. This is the note's central claim (rotor Casimir $=\mathrm{GM}^2$, Langer term $=\mathrm{AM}^2$, universal $\tfrac14=\mathrm{offset}^2$) and it holds without qualification.

**Scope check:** the note is explicit and correct that this is a statement about the *pattern* of quantization (an exact but purely arithmetic fact about consecutive-integer AM/GM splits), not a derivation of $\hbar$'s numerical value — it says so itself ("ħ's numerical value is dimensionful and is NOT derived — the same wall as $G$"). The extension to other actions (flux quantum, $E=h\nu$, power) is correctly and explicitly marked `[O]`, open, not claimed as theorem. No overclaim found.

## 2. v14.621 — Energy follows the AM/GM split; the G ingredients assembled

**File hash:** `research-notes/Energy_AM_GM_and_G_Ingredients_Addendum.md` re-hashed and matches the manifest (`64d3daec...`).

**The central algebraic identity, re-derived from scratch:** the note claims $\text{Dirac ratio} = \alpha\cdot(m_p/m_e)/\alpha_G$ with $\alpha_G=Gm_p^2/(\hbar c)$. Deriving this independently: $\alpha/\alpha_G = \dfrac{e^2/(4\pi\varepsilon_0\hbar c)}{Gm_p^2/(\hbar c)} = \dfrac{e^2}{4\pi\varepsilon_0 Gm_p^2}$, and multiplying by $m_p/m_e$ gives $\dfrac{e^2}{4\pi\varepsilon_0 Gm_pm_e}$ — exactly Dirac's ratio by definition. Confirmed algebraically correct, not approximate.

**Numerical re-verification (mpmath, 30 dps, independent of the note's own computation):**
- $\alpha = 0.00729735257374926169767143054553$ (CODATA-consistent).
- $\alpha_G = Gm_p^2/\hbar c = 5.9061494174239050478651093203\times10^{-39}$, matching the note's quoted $5.90615\times10^{-39}$ to every digit shown.
- $\alpha\cdot(m_p/m_e)/\text{Dirac}$, computed independently from the raw constants (not by algebraic substitution) $=5.9061494174239050478651093203\times10^{-39}$ — identical to $\alpha_G$ computed directly, match exact to 30 dps (difference $=0.0$).
- $\psi=\tfrac12\ln(\text{Dirac ratio}) = 45.3100043049815848431986723526$, matching the note's quoted $45.310004305$ to every digit shown, and matching this auditor's own independently-computed value from earlier in tonight's exploratory conversation with Jeremy (recorded informally, not previously ledgered) to all 30 displayed digits.
- Planck power $c^5/G = 3.62825490441128006447414463856\times10^{52}$ W, matching the note's quoted $3.62825\times10^{52}$ to every digit shown.

**Honesty of the verdict:** the note's own conclusion — that $\alpha$, the mass ratio, and the Dirac ratio contain exactly one unknown ($\alpha_G$, i.e. $G$) between them, so "assembling" them is circular and does not close v14.550's hierarchy-generator or factorised-observable items — is correct and is not overstated. §3's argument that a bare rapidity-chain hit on $\psi=45.31$ is chance-level without an independent selector principle is sound reasoning, consistent with the project's own prior standard (cf. v14.592's small-rational Airy near-misses) for distinguishing a real result from a guaranteed-by-counting coincidence.

## 3. Scope and consistency check

Both entries correctly limit their claims, explicitly cite their provenance (v14.550, v14.616) accurately, and neither claims a Lane A HANDOFF answer, a paper change, a certified-object change, or `G_derived`. The two open items from v14.550 §3 remain exactly as stated — unchanged by either deposit, as both entries' own scope flags say.

## 4. Verdict

```
Confirmed: v14.620 and v14.621 are honestly-scoped Sandbox interpretive
  deposits. All file hashes are exact. The consecutive-split AM/GM
  identity was re-derived symbolically (identically zero, all j).
  The Dirac-ratio/alpha_G identity was re-derived algebraically from
  first principles and re-verified numerically from raw constants
  (not by checking the note's own algebra), matching to 30 dps. The
  psi target, alpha_G value, and Planck power all match the notes'
  quoted values to every digit shown. No defect of substance found;
  neither entry touches the discriminant-12-return certification
  chain, the paper, or claims G is derived. The open-item count for
  the gravity side-thread remains two, as both entries themselves
  state.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.622
status: open
action: this auditor independently verified v14.620/v14.621 by hash check, independent symbolic re-derivation of the consecutive-split identity, and independent numerical re-derivation (from raw physical constants, not by checking the notes' own arithmetic) of the Dirac-ratio/alpha_G identity, the psi target, and the Planck power. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
