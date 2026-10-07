# Cone Derivation Ledger v14.098 — External Audit Round 180: v14.097 (Bicone Dipole / e² Direction) Checked — Arithmetic Confirmed, Core Algebra Not Independently Reproducible

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] Both numerical/algebraic facts stated in v14.097 that are checkable from committed material are confirmed exact; [N] the e²-from-transitions result is reproduced once the standard degeneracy/sum factor omitted from the entry's one-line formula is supplied; [FLAG] the entry's central group-theoretic claims (bicone ladder algebra, SO(3) tensor-failure obstruction) rest entirely on an uncommitted sandbox-only report with no producer script in this repository, so they could not be independently re-run this round.
**Parents:** v14.096, v14.097.
**Collision check:** immediately before this write, live HEAD was `fbfc6c16d538441617c82f0e8ddb31df401042b6` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.097. No collision. Re-checked immediately before commit (see §4).

---

## 1. Scope note

v14.097 is on a different mathematical track from every prior round audited in this thread (the Suzuki/Jost Xi-scalar double-scaling program on the discriminant-12-return project): it explores deriving the hydrogen 1s–2p dipole matrix element and the fine-structure constant from a bicone/SO(4,2) oscillator construction. It is explicitly labeled exploratory ("Sandbox, Jeremy-directed," "Nothing published," "Per-item Jeremy authorization"). Since it is a new ledger entry under the same project directory, it falls under the standing audit mandate, so it is checked here with the same rigor applied to the Xi-scalar rounds — adjusted for the fact that no backing code was committed (noted below).

---

## 2. Verified by hand (mpmath, dps=30)

**§2's target value.** `768/(243√6) = 1.29026620195986336036729366898...`, matching the entry's stated `≈1.290266`. Exact.

**§3's algebraic identity.** The entry's two boxed numbers are claimed to satisfy `|⟨R₁₀|r|R₂₁⟩| = √3·|C|` with `C/a₀ = 256/(243√2)`. Computed both sides independently:
- `C/a₀ = 256/(243√2) = 0.744935539027803153...`, matching the stated `≈0.7449`.
- `√3 · C/a₀ = 1.29026620195986336036729366898...` — identical to §2's target to all 30 computed digits (difference `< 2×10⁻³¹`).

So the claimed relation between the obstruction-blocked constant `|C|` and the known target is an **exact algebraic identity**, not an approximate numerical coincidence: `√3·256/(243√2) = 128√6/243 = 768/(243√6)`. Confirmed by direct simplification as well as by floating-point check.

---

## 3. e²-from-transitions (§4) — reproduced, with a formula gap flagged

Recomputing from physical constants (CODATA ℏ, c, ε₀, e, a₀) and the stated inputs (`A₂₁=6.265×10⁸ s⁻¹`, `E=10.2 eV`, standard-QM radial element `768/(243√6)·a₀`):

Plugging directly into the one-line formula as literally written in §4, `A = ω³e²|⟨r⟩|²/(3πε₀ℏc³)`, and solving for `e²` gives `8.563×10⁻³⁹ C²` — off from the known `2.567×10⁻³⁸ C²` by a factor of ≈3, **not** the claimed 0.07%.

The missing factor is the standard degeneracy/angular sum rule for a `2p→1s` (`l'=1→l=0`) spontaneous-emission rate, `A = (4αω³/3c²)·(l_max/(2l'+1))·|⟨r⟩|²` (Bethe–Salpeter/Hilborn convention), which carries an extra factor `l_max/(2l'+1) = 1/3` for this transition. Supplying that factor and recomputing:

```
e² = 2.56884×10⁻³⁸ C²   (known: 2.56697×10⁻³⁸ C²)
percent difference = 0.073%
1/α = 136.94
```

This matches the entry's claimed "`e²=2.569×10⁻³⁸` vs known `2.567×10⁻³⁸` (0.07%), `α≈1/136.94`" essentially exactly. **Conclusion: the computation itself is correct and reproducible** — the actual calculation evidently used the correct degeneracy-weighted formula — but the formula as *written* in §4 is incomplete (it omits the `l_max/(2l'+1)` factor needed to get the 2p→1s rate right). This is a presentational/transcription gap in the ledger text, not a computational error; worth fixing in a future revision so a reader can reproduce the number directly from the stated formula.

---

## 4. Flag: core algebraic claims not independently reproducible from this repository

§2's ladder-algebra computation (`M[i,j,m]` selection rule, the `δ_{q,−m}` pattern) and §3's obstruction (that `ab`-type bilinears fail the `[L_±,·]` commutation relations needed to form an `SO(3)` vector operator) are both described as "machine-verified," but their sole cited source is `workspace/d12/explorations/bicone-dipole/REPORT.md`, explicitly marked "(sandbox-only)." I searched this repository (`find . -iname "*bicone*" -o -iname "*dipole*"`) and found no committed producer script or report backing these claims — only the ledger entry itself.

This means that, unlike every Xi-scalar round audited this session, **I could not independently re-run or hand-verify the entry's central new algebraic content** this round. I am not asserting it is wrong — I have no evidence either way — only that it is not currently independently checkable from what is in the repository. This is a reproducibility gap, not a refutation.

---

## 5. Verdict

```
v14.097 §2/§3 target-value and C-constant identity: CONFIRMED EXACT (hand algebra + mpmath).
v14.097 §4 e²-from-transitions numeric result: CONFIRMED, once the standard 2p->1s
   degeneracy factor (omitted from the entry's one-line formula) is supplied.
   Recommend the ledger text state the formula with that factor explicit.
v14.097 §2/§3 core bicone ladder-algebra/obstruction claims: NOT independently
   reproducible this round -- no producer script or report is committed to the
   repository; only a sandbox-only external report is cited.
```

No ledger content is altered by this entry.

---

HANDOFF-NOTE
target: sandbox
type: audit-finding
parent: v14.098
status: open
action: (1) Consider stating the §4 A-coefficient formula with its l_max/(2l'+1) degeneracy factor explicit, since the bare formula as written does not reproduce the claimed 0.07% agreement (it is off by ~3x without that factor). (2) If this bicone/SO(4,2) direction continues, consider committing the ladder-algebra verification (even a short script checking the L_± commutation-relation failure numerically/symbolically) to the repository, so the obstruction claim in S3 is independently checkable the way every Xi-scalar round's producers have been.
constraints: This is a finding on reproducibility and formula completeness, not a claim that v14.097's results are incorrect.
