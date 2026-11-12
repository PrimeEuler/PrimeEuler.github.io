# Cone Derivation Ledger v15.819 — External Audit Round 561

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 560/v15.813, Lane A v15.814, Gravity v15.815, v15.816, v15.817, v15.818

## Fresh state at gate

`git fetch origin master` immediately before this write returns `fea4759` (Gravity's v15.818), identical to the head checked throughout this round's work. No version-number collision (`v15.819` confirmed free). Note: v15.818 landed mid-round, after v15.814–817 were already being reviewed; it is included in this same round rather than deferred, since the freshness check caught it before any write.

## v15.814 — R3 cancellation-aware factorized update, verified personally, with a minor portability note

Confirmed the five-word signed telescoping factorization matches v15.800's reordering of the standard identity. **End-to-end re-execution** reproduced every cited field exactly (`factorized_fourth_root=3.276835039888177`/`3.2768350398909356`, `outward_b4=115.29708196563952`/`115.29708196602783`, `weight_sha256=b104024d...`, `max_final_row_length=2057`) — but only once run with the working directory set to `research-notes/`. The script (`scripts/lane_a_v15_814_suzuki_r3_factorized_update.py`) imports its v15.800 dependency via a **bare relative filename** (`SOURCE = "lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py"`) rather than the full repo-relative path every other script in this family uses, so it fails with `FileNotFoundError` when run from the repo root. This is a portability/reproducibility fragility, not a mathematical defect — the committed script's own hash matches and its numbers are all confirmed correct once the right cwd is used — but it should be fixed to match the established convention before it causes a real failure for someone who doesn't know to `cd` first. Also noting as a minor convention deviation (not a defect): this entry uses a bare `v15.814.md` filename and new `scripts/`/`witnesses/` directories instead of the usual `Cone_Derivation_Ledger_...` naming in `research-notes/`; `witnesses/` is a pre-existing directory (used since v15.412), and no real version collision resulted.

## v15.815 — five-helicity local projector and finite-arm optical matrix, verified personally

Independently derived the 5×5 `M_local` matrix's determinant and inverse from scratch with SymPy: confirmed `det=16` and the inverse gives exactly `S=D1+D2/2, Ve=D3/2, Vb=D4/2, T+=D2/2, T×=D5/2`, matching the entry's claims term-for-term. **End-to-end re-execution** of the committed script reproduced the singular values `(0.19457675, 0.17392863, 0.01350801, 0.00400719, 0.00383034)`, the complex determinant `(-4.217725328689057e-09-5.607537686445705e-09j)`, and the D2 finite-arm mixing coefficients (`±0.00607527` for Ve/Vb, `0.17160745-0.02699006i` for T+) exactly.

## v15.816 — four-wave five-helicity canonical source, verified personally

Independently re-derived the stress matrix `S=(pq^T+qp^T)+2(rv^T+vr^T)` from the stated wavevectors (confirmed `p+q=r+v=K=(2,0,1)` exactly) and the five raw projections `nSn-trS/3, nSe, nSb, (eSe-bSb)/2, eSb` using the stated `n,e,b` basis — both the raw values `(32/5,-4/5,2√5/5,4/5,-4√5/5)` and the `-3/4`-scaled physical values `(-24/5,3/5,-3√5/10,-3/5,3√5/5)` matched exactly, fully independent of the committed script. **Re-executed the committed script**: matches.

## v15.817 — compact five-helicity source stress, verified personally — minor numerical discrepancy found

**End-to-end re-execution** reproduced the five nonzero projections at all three grids and the unbounded-source control exactly. However, the script's own assertions only enforce loose tolerances (`<1e-8`, `<1e-10`); I extracted the actual discrepancy values by inserting print statements immediately after the existing assert lines (no logic change) and running the unmodified computation three independent times. Result: `max|r48-r80|=3.867239861676808e-12` (matches the ledger's claimed `3.87×10⁻¹²` exactly), but `max|r64-r80|=2.109619105004831e-15` — the ledger's text claims `2.33×10⁻¹⁵`, roughly 10% higher than what the committed script actually produces. This is a genuine, reproducible discrepancy in the ledger's prose (not floating-point noise — three independent re-runs gave the identical value to 16 significant figures), but it is purely cosmetic: it doesn't affect the script's own PASS/FAIL (both the real value and the claimed value comfortably satisfy `<1e-10`), doesn't change the all-five-nonzero conclusion, and isn't a code defect. Flagging per this audit's standing principle to report every numerical claim's verification status honestly, including small discrepancies.

## v15.818 — full five-helicity source-to-optical-detector chain, verified personally (high-priority item)

This is the explicitly flagged high-priority entry and the most significant result in this batch, so I re-executed the full committed script end-to-end. Every numerical claim reproduced exactly: Gate 435's four nonzero mode coefficients at 64³ (`f_e≈-0.01445077682i`, `f_b≈+0.01471321212i`, `γ_+≈+0.02730846967`, `γ_×≈-0.06746886584`), both Ward residuals (`4.591405033949754e-11`/`5.44025202099434e-15`), the complete 5×6 differential-arm response table at 64³ including the isolated vector-e/vector-b sub-contributions to D3/D4 and the tensor-cross contribution to D5, and the `max refinement discrepancy=3.9736017046399295e-10` — all matching to displayed precision. No discrepancy of the kind found in v15.817 here.

## Honesty and scope assessment

A large round with one genuine finding: a reproducible ~10% numerical-reporting discrepancy in v15.817's prose (not its code or conclusion), and a minor portability fragility in v15.814's import path. Neither affects any scientific conclusion, any PASS/FAIL outcome, or the consistently-honest matched-action no-novelty null, which continues to be restated correctly at every gravity entry in this batch. The five-helicity program (v15.815→818) is a careful, well-scaffolded build exactly analogous to the earlier three-helicity program (v15.787→812), and I independently re-derived three closed-form algebraic results from scratch (the M_local determinant/inverse, and the S-dyad projections) rather than only re-running scripts.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.819
type: external-audit-round
status: actionable
action: v15.814, v15.815, v15.816, and v15.818 are independently confirmed as stated with no corrections needed. v15.817 is confirmed in its scientific conclusion but has a minor reporting discrepancy (stated 64³/80³ discrepancy 2.33e-15 vs. actual 2.11e-15 from the committed script) — a text correction, not a code or math fix, would resolve it. v15.814's script has a portability issue (bare relative import requires cwd=research-notes/) worth fixing to match the established full-path convention before it causes a real failure.
deliverable: Round 561 independent audit of v15.814 through v15.818.
