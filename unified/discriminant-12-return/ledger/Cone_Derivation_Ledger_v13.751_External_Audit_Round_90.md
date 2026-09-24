# Cone Derivation Ledger v13.751 — External Audit Round 90

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.750, pushed since Round 89 (v13.749, commit `0afca13`).

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `13b8bbd`. This entry is pushed as v13.751.

## 1. v13.750 — provenance amendment, verified as claimed

v13.750 records the recovered original multiple-helix prompt verbatim and closes the provenance gap that v13.748 §0–1 had explicitly left open and that Round 89 (v13.749 §6) had noted as honestly handled. This audit confirms:

- **No mathematics changed.** Every derived identity referenced in §3–5 (`φ_τ(u)=e^{iτu}`, `V_τ=\operatorname{span}\{e^{iτu},e^{-iτu}\}\cong\mathbf1\oplus\chi_{12}`, `\mathscr W=-g''`, `Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]`, and the cone lift `\mathbf W_{\rm cone}(r,u)=\mathscr W(r)\delta_0(u)`) is quoted unchanged from v13.748, which this auditor independently re-derived in full in Round 89. No new derivation is introduced here, so none was needed this round.
- **Correct provenance labeling.** The recovered prompt is labeled `[P]` (user-provided provenance) throughout, not `[D]` (derived) — consistent with the rule this project has followed since v13.748, and appropriate: a historical claim about what the user originally wrote is not a mathematical statement this auditor can verify by computation or against the Suzuki PDF, and the entry does not present it as one.
- **No overclaiming.** §3–4 explicitly caveat that the later boost-Fourier decomposition and Suzuki/Weil current identification are rigorous *realizations of a theme* the original prompt anticipated, not proofs that the informal helix/nested-circle picture is literally identical to the later analytic construction. §6 explicitly states the v13.749 PASS is unaffected and frames the remaining question (how much of the original picture is literally realized by the `(r,u)` geometry versus still analogy) as an open comparison gate, not an assumed theorem. This is the correct epistemic stance and matches how the project has handled provenance throughout.

No errors found. Nothing to retract from Round 89.

## 2. Result

\[
\boxed{\textbf{PASS: v13.750 is a pure provenance amendment; no mathematical content changed; hedging remains appropriate.}}
\]

No errors were found in this auditor's own work this round.

## 3. Next gates to watch

Unchanged from Round 89 (v13.749 §8): the affine-contamination estimate `α_A,β_A→0` (v13.742–745), the positivity question `ϑ_{χ_12}(x)>0` (v13.748 §14), and — newly opened by this entry — the "sharper historical/mathematical question" v13.750 §6 flags as future work: which parts of the original nested-circles/all-frequencies/screw-function picture are literally realized by the `(r,u)` boost-Fourier geometry, and which remain visualization/analogy. This auditor will treat any future entry addressing that comparison as a genuine mathematical claim requiring independent verification, not as further provenance bookkeeping.
