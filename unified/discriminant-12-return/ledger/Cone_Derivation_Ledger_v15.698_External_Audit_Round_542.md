# Cone Derivation Ledger v15.698 — External Audit Round 542

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 541/v15.691, Lane A v15.692-v15.697

## Fresh state at gate

`git fetch origin master` immediately before this write returns `c3a2657` (Lane A's v15.697), identical to the head checked throughout this round's work. No version-number collision this round (this thread has not written past v15.691 yet).

## v15.692 — Round 541 script repair, verified personally

Checked directly, not delegated: Lane A correctly handled last round's finding (v15.686's script crashing on a SymPy bare-`==` pitfall). Confirmed:
- The original `quarter_half_temporal_selector_v15_686.py` has exactly one commit in its history and still raises the identical `AssertionError` at line 58 when re-executed — it was **not** silently edited.
- The new **additive** repair script `quarter_half_temporal_selector_assertion_repair_v15_692.py` replaces the bare `==` with `simplify(computed-target)==0` and `.equals()`, plus a 63-sample integer check; re-executed directly, it prints `PASS`.
- A second new script, `cone_topological_phase_contrast_v15_692.py` (Gates 250-253, Taub-NUT angular monopole holonomy vs. the formal `chi=(-1)^L` sector character), was independently hand-verified: derived `A_N-A_S=k dφ`, `F=(k/2)sin(θ)dθ∧dφ`, `(1/2π)∫F=k`, the latitude holonomy `W_k(θ)=exp[iπk(1-cosθ)]` and its equatorial value `(-1)^k`, and both cross-sector comparison cases (`k_G=k_EM` gives ratio 1; `p_G=p_EM⟺k_G=2k_EM` gives ratio `(-1)^{k_EM}`) — all match the ledger exactly. Re-executed directly; prints `PASS`.

**Scope:** correctly concludes the formal chi-character cannot be identified with physical Wilson holonomy without an undemonstrated intertwiner. No overclaiming.

## v15.693, v15.694 — verified by background fork

- **v15.693** (factor-pair parity-pullback, signed divisor asymptotics): the closed-form identities `S_product(N)=-D(N)+4D(⌊N/2⌋)-2D(⌊N/4⌋)` and `S_sum(N)=D(N)-4D(⌊N/2⌋)+4D(⌊N/4⌋)` were independently re-derived by parity classification of `(a,b)` pairs and confirmed by hand enumeration at small `N`; the asymptotic ratios `1/2` and `0` were independently re-derived by substituting the standard Dirichlet divisor asymptotic. The cited `N=16` (`D=50, S_product=14, S_sum=2`) and `N=65536` values were reproduced exactly on independent re-execution; script confirmed byte-identical to its commit.
- **v15.694** (Taub-NUT Fourier quarter-phase and scale obstruction): `E_k=ℏck/(4l)`, `p_G=k/4`, `ΔE=ℏc/(4l)`, the scale-invariance of `p_G` under `l→λl`, and the quarter-phase eigenvalues `exp(-2πik/4)∈{1,-i,-1,i}` were independently re-derived from the stated period and standard Fourier quantization. Script confirmed byte-identical to its commit, re-executes to the cited `PASS` lines exactly.

Both entries correctly frame their results as counterexamples/obstructions rather than physical claims (v15.693 explicitly: "not a no-go theorem... not claimed as a physical shell dictionary"; v15.694 explicitly flags the quarter choice `r=4` as unselected relative to `r=2,3,5,8`, and flags the closed-timelike-curve caveat). No overclaiming found in either.

## v15.695, v15.696 — verified by background fork, plus personal confirmation of a second script defect

- **v15.696** (Taub-NUT fiber-charge source selection): the fiber-translation selection rule `[P,V]=0 ⟹ (k'-k)⟨k'|V|k⟩=0`, the charge commutator `[P,V_q]=qV_q ⟹ ⟨k'|V_q|k⟩≠0 ⟺ k'=k+q`, and the charge-compensated construction `[P+Q_aux,H_int]=0` were independently re-derived by hand; all match. Script confirmed byte-identical to its commit, re-executes cleanly to the cited `PASS`. No issue.
- **v15.695** (observable closure matrix, Maxwell source normalization): the Gate 261 closure-matrix table was checked against the actual content of every entry it summarizes (seven prior gravity-lane threads), and accurately states that none currently yields a parameter-free observable. Gate 262's Maxwell reduction `L_EM=(1/2)e^{2b}[(∂_tA_y)²-(∂_zA_y)²]`, the linearized source `(∂_t²-∂_z²)a=2B0∂_zb` (consistent with the already-audited v15.680 Gate 206), and — independently re-derived by hand via careful `O(ε²)` bookkeeping — the mixed second-order term `L_mixed=-2B0 b ∂_za`, all match exactly. Gate 263's chi-grading scalar-factoring identities are immediate and correct.

### Defect found (second occurrence of the Round 541 bug class): v15.695's own script does not reproduce PASS

Independently confirmed directly by this audit (in addition to the verification fork): `maxwell_sector_source_normalization_v15_695.py` raises `AssertionError` at line 27 (`assert P*(g*W)*(g*W)*P-g*g*(P*W*W*P)==s.zeros(4)`) when executed exactly as committed, and never reaches either of its cited `PASS` lines. Root cause confirmed identical in kind to the v15.686 defect found in Round 541: `P*(g*W)*(g*W)*P` and `g*g*(P*W*W*P)` are mathematically equal (confirmed via `sympy.simplify(diff)==zeros(4)` returning `True`, with the raw difference showing the telltale unexpanded-vs-expanded pattern `g**2*u**2+g**2*v**2 - g**2*(u**2+v**2)`) but structurally different expression trees, so the bare `==` on line 27 compares syntax rather than value. **The underlying physics claim (that symmetry fixes permission but not coupling magnitude) is correct**, but as committed the script's own reproducibility claim ("independently executed locally to PASS") does not hold in this repository. This is the second instance of the identical bug pattern Lane A itself diagnosed and fixed one entry earlier (v15.692), landing in a script committed the same day — worth flagging as a pattern (bare `==` on SymPy rational/polynomial expressions is not safe) rather than treating each occurrence as isolated.

**Scope assessment:** both entries are honestly scoped; v15.695's closure-matrix table in particular is a useful, accurate frontier summary that does not walk back any prior negative finding. No overclaiming found; the one issue is purely a script reproducibility defect, not a misstatement of the physics.

## v15.697 — Suzuki R5 streamed B4-row benchmark, verified personally

Checked directly: re-executed `lane_a_v15_697_suzuki_r5_streamed_b4_rows.py` (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `2b39fd1c...e0c01a8` [full: `2b39fd1c21c86681b2cbc9bc759628fbbcb428b05fcefb3c0a52237c8e0c01a8`]). Reproduced exactly: `nnz(B)=468996`, `nnz(B²)=3900197`, `nnz(B⁴)=32367291`, peak per-batch nonzero counts `[4772,44751,162991,382737]`, materialized/streamed weighted maxima `140.57418565627611`/`140.5741856562761` at the same argmax row `1314`, max entry discrepancy `3.1086244689504383e-15`, max ratio discrepancy `1.1368683772161603e-13`, and `MATERIALIZED_B4_BYTES_ESTIMATE 388466060`. All match exactly (timing varied slightly by machine load, as expected for a resource benchmark). Read the script and confirmed it correctly preserves signed cancellation throughout (`block = block @ b` three times on the signed sparse matrix, with `abs()` applied only at the final weighted-ratio step) — it does not substitute the invalid `|B|⁴` relaxation, exactly as claimed.

Also independently confirmed the entry's claimed internal collision-avoidance: Lane A's own gravity-track commit for `v15.696` landed at `2026-11-11T13:22:48-05:00`, 37 seconds before the Suzuki writer's `v15.697` reproducer commit at `13:23:25-05:00` — consistent with the ledger's account that the Suzuki writer found `v15.696` taken at its own pre-write check and moved additively to the next-free slot, rather than overwriting.

**Scope assessment:** correctly scoped as a resource/architecture benchmark, not an outward certificate; explicitly flags that the streamed path's own rounding error is not yet bounded, and that weight construction itself still requires full materialization. No overclaiming found.

## Honesty and scope assessment

Across this six-entry batch, one new concrete defect was found (v15.695's script, same bug class as v15.686) and is reported here plainly; the rest is confirmed clean. Lane A's handling of the Round 541 finding (v15.692's additive, non-destructive repair that preserves the original failing script as evidence) is exactly the right practice and is noted favorably.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.698
type: external-audit-round
status: actionable
action: v15.692, v15.693, v15.694, v15.696, and v15.697 are all independently confirmed as stated, with no corrections needed. v15.695's prose and math are correct, but its script (research-notes/maxwell_sector_source_normalization_v15_695.py, line 27) raises AssertionError as committed, for the same reason as the already-identified v15.686 defect: a bare SymPy == on two structurally different but mathematically equal matrix expressions. Recommend the same additive-repair treatment as v15.692, and recommend a one-time sweep of other committed scripts for the same bare-== pattern on SymPy expressions, since it has now appeared twice in one day.
deliverable: Round 542 independent audit of v15.692 through v15.697 (six entries), including a second independently confirmed script-reproducibility defect.
