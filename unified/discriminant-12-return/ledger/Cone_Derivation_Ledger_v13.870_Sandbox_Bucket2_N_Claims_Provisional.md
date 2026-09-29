# Cone Derivation Ledger v13.870 — Status Rule: All Bucket 2 [N] Numerical Claims Provisional Until the Widened Re-run Lands

Date: 2026-09-29

Type: **status rule** (not a derivation, not an audit of other entries). Audit-thread recommendation, endorsed by the project owner, recorded for all writers and readers.

Parents: v13.869 (External Audit Round 123), v13.867 (FACTOR-048 — the PSI_Q bug), v13.860–v13.864 (the Bucket 2 arc).

Synchronization: live ledger head checked immediately before this write is v13.869 (External Audit Round 123). No collision on the present version number. **This entry does not audit v13.869 or earlier.**

## 0. Rule

**Every [N] numerical claim across the Bucket 2 arc is PROVISIONAL until the widened RERUN-048 lands and lifts the status claim-by-claim.** This covers the whole arc, not just the PAIR-H chain: v13.840 (distributional T_a validation gate, ratios, edge-criteria FAIL verdict), v13.842 (natural-BC P1-instability, natural vs Dirichlet A-track falsification), v13.844 (edge asymptotics R0–R3, \(L_0+L_1=0\)), v13.846 (anatomy/kernel scripts), v13.848 (selection-identity numerics), v13.852–v13.855 (W1–W3 and bulk-lemma numerics: the \(-0.47\) half-line constant, \(\alpha_\infty = 0.48\), \(c_1 \approx -0.154\), the \(Ae^A\) scaling), v13.862 (PAIR-H magnitudes). "Provisional" means: do not build further argument on these numbers, and do not cite them as established — they were computed with the wrong screw function (v13.867) and may move.

## 1. Explicitly unaffected [D/I]

The analytic-only results do not touch the screw numerics and stand as stated: the selection theorems (v13.848's SELECTS identity, conditional on \(\lambda_a > 0\)); G1–G3 (v13.858); H1 dual-slot canonization (v13.861); the IDENT dissolution (v13.864); the Wiener–Hopf characterization (v13.849); the downstream-absorption verdict's analytic content (v13.851). The bug finding itself (v13.867) is [D]/[N] about the code and is not provisional.

## 2. Widened recovery scope (project-owner authorized)

RERUN-048 was scoped to the PAIR-H/W1–W3 chain; the audit correctly judged that too narrow. Its scope is widened to explicitly re-verify on the corrected kernel (PSI_Q = ψ(1/4), LOG_12_PI, ZETA_2_Q fixed, import-time assertions installed):

- v13.840: distributional T_a validation gate, the (8.4) deficiency solves, the \(I_j\) ratios, and the edge-criteria verdict — re-measured, old-vs-new side by side.
- v13.842: the natural-BC P1-instability diagnosis and the natural vs Dirichlet A-track falsification under its pre-registered rule — reproduced or flipped, reported plainly either way.
- The PAIR-H/W1–W3 chain as originally chartered (v13.867 §5): \(L_0, L_1, \alpha_\infty\), the edge criteria \(R_A \to 1, \Delta_A \to 0\), PAIR-H bulk/edge accounting, and the verdict on whether 0.48 survives on the corrected kernel and by what mechanism.

Provisional status lifts per-claim, only on the widened re-run's report — not on re-assertion, not on analytic argument.
