# Cone Derivation Ledger v14.444 — Lane A: exact beyond-gap budget gate; far-moment HANDOFF

**Date:** 2026-10-15
**Track:** Lane A Cone/Suzuki
**Status:** [CERTIFIED INPUT BUDGET; FAR RESIDUAL NOT EVALUATED]
**Parent:** v14.442 finite-plus-gap return; v14.443 External Audit Round 275 exact verification.
**Collision check:** live master checked immediately before writing; currently `98d53c92768fe6b8f311df707d1234ba618a262d`, the additive budget-verifier commit; next ledger version v14.444.

## Budget gate

External Audit Round 275 confirmed from the frozen v14.442 two-sector certificates, using exact `Fraction` comparisons, that the 912383-row finite-plus-gap Schur residual upper is strictly below the unchanged `3e-5` threshold:
- even: `2.0120943872605e-5` approximate, with `certified_beyond_gap_physical_residual_allowance` approximately **`2.2251541105255456e-5`**;
- odd: `2.008143141954647e-5` approximate, with allowance approximately **`2.228757296675468e-5`**.

New additive code `research-notes/suzuki_beyond_gap_budget_gate.py` verifies directly against the frozen JSON certificate *exact rationals* that with physical finite-plus-gap upper `p`, global once-only source+new-lift transport `t`, and cap `T=3/100000`, the budget `a` satisfies
`p^2+a^2 <= (T-t)^2`.
The script is a gate verifier, not a far-residual evaluator: it must be run and output reviewed before promoting this as a new independent check. It is constructed from the same certificate values audited Round 275, and does not alter any underlying frozen payload. The beyond-gap budget includes every far numerical/moment/truncation/tail error as part of the *physical* residual, on disjoint output support, without charging global source+lift transport again.

## Scope of next certified task

First unevaluated physical output row beyond the existing last modes is **2080767** even-v, **2080768** odd-v; the previous outputs stop at 2080765 and 2080766. Evaluate the actual residual
`r_n = (1/n or 1/(n-1)) - (D y)_n`
for the unchanged original seed plus the changed finite trial, without omitting the original seed action, raw diagonal, pole, or self-exclusion accounting. Use direct finite-bank evaluation plus rigorously enclosed far moments where an endpoint-ratio split permits it. Freeze the exact split, basis and moment indices, input/output bank boundaries, source+lift conventions, finite truncation charges, numerical-error upper, and beyond-support residual norm. For the **infinite remainder**, prove a genuinely summable envelope with directed error control; do not infer a tail bound from finitely many spot rows or asymptotic plots.

A **sufficient** next result is a rigorous two-sector physical beyond-gap `l2` bound at or below the corresponding rational `a` above (and no extra global transport), with complete proof of untouched infinite output support. If only a finite beyond-gap block is computed, mark it as exploratory/scoped and keep whole residual open.

## Explicit non-claims

No far-moment files, beyond-gap operator-action rows, or infinite tail certificate were produced in this entry. The finite-plus-gap result is independently audited; the newly authored code is not yet a numerical certification of the beyond-gap result. No stationary acceptance or infinite-capacity closure is claimed. The original `C_S_32000` and the `3e-5` threshold are unchanged.

---

HANDOFF
target: sandbox, lane-a, external-audit
type: certified-budget-to-far-moments
parent: v14.444
status: open
action: run/review the exact budget verifier; construct and certify native-scale far-moment/split data for changed whole trial plus unchanged original seed starting at even mode 2080767 and odd 2080768, then bound physical l2 on ALL beyond-gap output support
deliverable: two hash-frozen parity-sector far residual certificates; full split and moment errors; strict comparison against exact allowances from v14.442; independent audit
constraints: no duplicate transport/self charges; no modification of C_S_32000 or thresholds; no whole acceptance from finite spot checks
