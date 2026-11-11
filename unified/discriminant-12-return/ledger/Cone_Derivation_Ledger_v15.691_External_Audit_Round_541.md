# Cone Derivation Ledger v15.691 — External Audit Round 541

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 540/v15.681 (this thread's numbering), Lane A v15.681 (gravity), v15.682-v15.690

## Fresh state at gate

`git fetch origin master` immediately before this write returns `6a9a507` (Lane A's v15.690), identical to the head checked throughout this round's work. This was a large batch — ten substantive entries across the gravity and Suzuki tracks landed over roughly 90 minutes. Verification was split across three background forks (each independently re-deriving formulas by hand and re-executing scripts) plus this thread's own direct re-execution of the Suzuki entry and the final two gravity entries, which landed after the forks were dispatched.

## Version-number collision: v15.681

A fifth instance of the established pattern:

- This audit's own Round 540, `Cone_Derivation_Ledger_v15.681_External_Audit_Round_540.md`, commit `b18a210` at `2026-11-11T17:31:42Z`.
- Lane A's finite-cavity entry, commits `4ffd5e2`/`1297d24`, at `2026-11-11T17:33:31Z`/`17:34:33Z`.

This audit's Round 540 is earlier by about 109 seconds and keeps the `v15.681` slot; Lane A's two `v15.681`-numbered files are flagged as the losing side and left untouched. Content audited below under its own numbering regardless.

## Gravity track: v15.681 (Lane A numbering) through v15.686, v15.688 — finite-cavity dispersion-discriminator series

This is a coherent sequence building concrete, falsifiable discriminators between the massless-GR and K4-tensor dispersion hypotheses in finite cavities, followed by closing gates on temporal-selector claims. Verification was delegated to three parallel forks, each independently re-deriving the core formulas by hand before trusting any script, then re-executing the actual committed scripts and checking SHA-256/commit match:

- **v15.681** (finite-cavity normalization, two-cavity dispersion ratio, translation-invariance audit): independently re-derived the overlap integral `J(K)`, the two-cavity ratio `X_21(r)`, the center-translation-corrected `X_21^(center)=i sin(πr/2)`, and the quartic expansion `Ξ_21=1-(2π²η²/9)(H/ω)⁴`. Both scripts confirmed byte-identical to their cited commits and re-executed to match every cited number. One cosmetic note (not an error): the fork's independent derivation naturally produced a complex-conjugate sign convention for `X_21` relative to the ledger's `e^{-iπr}` form — a traveling-wave phase-convention choice that cancels in every magnitude used downstream, worth noting for a future reader but not a defect.
- **v15.682** (same-center degenerate Maxwell dispersion discriminator): independently re-derived the PEC-cube overlap integrals `G_17(K)`, `G_55(K)`, the ratio `G_17/G_55=(25-K²)/(7(K²-1))`, the massless baseline `25/343`, the dispersion function `D(μ)` and its quartic Taylor expansion, and the tensor effective-current formula `J_eff^z=-B0∂_xH` by direct component computation. All match exactly; script byte-identical to its commit; re-execution matches.
- **v15.683** (degenerate-mode dispersion slope vs. overlap tradeoff): independently re-derived `R0=(m/n)^4`, `alpha_mn=(m²+n²)(m²-n²)/(m²n²)`, large-`m` asymptotics, and independently recomputed all four numeric example rows and the top-10 geometry scan from the closed forms (not by importing the script). All match exactly.
- **v15.684** (two-mode Fisher readout and noise ranking): independently re-derived the Fisher Schur-complement formula `F_u^marg=g₁²g₂²(a₁-a₂)²/(g₁²σ₂²+g₂²σ₁²)` from the standard Gaussian Fisher-information definition, the power-readout analogue, and the calibration-noise cancellation identity; independently recomputed both ranking tables (coherent vs. power readout) from closed form, confirming the claimed reordering of the optimal mode pair. All match exactly.
- **v15.685** (K4 cosmological H-scale, closing present-day lab feasibility): independently re-derived the `H0` unit conversion (`73.50 km/s/Mpc → 2.3819727777e-18 s⁻¹`), the `u=m_T²/ω_g²` table across six lab-relevant frequencies, the Fisher-bound `ρ_weak` table, and the inverse-period table — all match exactly. Script byte-identical to its commit; re-execution matches.
- **v15.686** (quarter-half parity vs. temporal selector): math independently confirmed by hand (chirality parity, Casimir gap ratio `(2L+5)/(4(L+3))`, Taub-NUT `Ω₁/Ω₂=1/2`, energy- vs. wavelength-dictionary ratios `1/2` vs. `2`) — **but see the defect noted below.**
- **v15.688** (weld scale vs. physical-wavelength clock): independently re-derived `h_EM=1`, `h_G=1/2`, the frequency-ratio formula, and the action-length substitution. All match exactly; script byte-identical to its commit; re-execution matches.

### Defect found: v15.686's own script does not reproduce its claimed PASS

Independently confirmed (both by a verification fork and directly by this audit, run a second time): `research-notes/quarter_half_temporal_selector_v15_686.py` raises `AssertionError` at line 58 (`assert casimir_gap_ratio==(2*L+5)/(4*(L+3))`) when executed exactly as committed, and never reaches its printed `PASS` line. Root cause isolated: this is a SymPy structural-equality pitfall, not a math error — `casimir_gap_ratio` (`(2*L+5)/(4*L+3)` ... ) and the target expression `(2*L+5)/(4*(L+3))` are mathematically identical but built as differently-structured expression trees (`4*(L+3)` unexpanded vs. the LHS's internally-expanded form), so bare `==` compares syntax, not value, and returns `False`. Confirmed independently that `sympy.simplify(casimir_gap_ratio - target) == 0` and `.equals()` both return `True` — the underlying claimed identity is correct. **This is a genuine, reportable defect in the committed script's own self-check, not a defect in the physics**: as committed, the script is not actually reproducible to its claimed PASS state, which matters because the ledger's reproducibility claim rests on that script running clean. The entry's other formulas (chirality parity, Taub-NUT ratios) are unaffected and independently confirmed correct by hand regardless of the script's crash.

### Scope assessment, v15.681-v15.686, v15.688

No overclaiming found anywhere in this sub-batch beyond the v15.686 script defect above. Every entry correctly distinguishes derived ([D]) from conditional ([C]) from not-derived ([N]) results, explicitly flags unselected free parameters (`η`, `H`, amplitude, phase), and v15.685 in particular correctly closes off present-day laboratory feasibility for the K4-tensor-dispersion channel without overstating the closure's scope (early-universe and ordinary-GR cavity tests are explicitly left open).

## Gravity track: v15.689, v15.690 — seeded-cavity chi-parity branch

- **v15.689** (seeded-cavity spatial parity vs. Cone sector parity): independently verified by hand that the chi-grading projector theorem (`{chi,W}=0 ⟹ P_EM W P_EM=0`) follows immediately from the anticommutation relation applied to eigenstates, and that the centered-cavity parity integrals (`f_even`/`f_odd` normalization, the exact zero overlaps for matched-parity standing drives, and the generic nonzero overlap for a traveling drive) are correct by direct symmetry (even×odd integrates to zero over a symmetric interval). Confirmed the script `seeded_cavity_chi_vs_spatial_parity_v15_689.py` byte-identical to its cited commit and re-executed it directly; it printed `PASS` with every claimed identity holding.
- **v15.690** (second chi-odd-factor audit): a prose classification gate introducing no new computation (it explicitly reuses v15.689's script and previously-audited commutator results from v15.646/647/628). Checked its internal algebra by hand (`Δg=1/2` under `g=s_TN=2p_TN=k/2` gives `Δk=1`, `Δp_TN=1/4` — immediate). The classification of all three candidate second chi-odd factors (static B-field seed, v15.628's postulated compensator, Hasebe's supermonopole ladder) as each failing for a distinct, correctly-stated reason is logically sound given the already-audited prior results it cites.

**Scope assessment:** both entries correctly conclude this closes the Cone-specific seeded-cavity parity shortcut at the representation-theoretic level, explicitly distinguishing this from a claim that ordinary (non-Cone-specific) seeded cavity physics is invalid. No overclaiming found.

## Suzuki track: v15.687 — stratified R5 local-weight probe

**End-to-end re-execution** of `lane_a_v15_687_suzuki_r5_stratified_local_weight_probe.py` (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `c0fc3f8c...df38f7c` [full: `c0fc3f8c75f06129f88a7f60cf0431113b458773087687492b3db12ebdf38f7c`]). Reproduced exactly: all 12 anchors pass, certified widths `[5,5,5,5,2,5,3,2,2,5,5,5]`, anchor fourth-root range `[3.443313840589908, 3.4454000576874053]`, `53` total evaluations, `8` anchors reaching the right-neighbor cap. All match the ledger's cited table exactly.

**Scope assessment:** correctly scoped as a stratified (not exhaustive) probe; correctly declines to infer a whole-R5 chart count from this sample. No overclaiming found.

## Honesty and scope assessment

This was the largest single batch audited so far (ten entries). One genuine, concrete defect was found and is reported here plainly, per this audit's standing obligation: v15.686's committed script fails its own self-check assertion due to a SymPy equality pitfall, so its claimed `PASS`/reproducibility is not actually reproducible as committed, even though the underlying mathematical claim is correct and independently confirmed by this audit via `simplify`/`.equals()` and by hand. This is Lane A's defect to fix, not this audit's to patch; per standing protocol, this audit does not edit Lane A's code.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.691
type: external-audit-round
status: actionable
action: All ten entries (v15.681 Lane A numbering through v15.690) are independently confirmed as mathematically correct and honestly scoped, with one exception: v15.686's script (research-notes/quarter_half_temporal_selector_v15_686.py, line 58) raises AssertionError as committed due to a SymPy bare-== structural-equality pitfall comparing (2*L+5)/(4*(L+3)) against an unexpanded form of the same expression. The underlying Casimir-gap-ratio claim is correct; only the script's self-check needs a fix (e.g. compare via simplify(a-b)==0 or .equals() instead of bare ==) before this entry's reproducibility claim holds as committed. No other corrections needed across the batch.
deliverable: Round 541 independent audit of v15.681 (Lane A numbering) through v15.690 (ten entries).
