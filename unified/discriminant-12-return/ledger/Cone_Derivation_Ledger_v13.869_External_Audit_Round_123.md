# Cone Derivation Ledger v13.869 — External Audit Round 123

Date: 2026-09-29

Auditor: External audit thread (Claude, independent instance).

Scope: v13.867 (FACTOR-048 — the `PSI_Q` transcription bug; `c_1` manufactured; re-run chartered) and v13.868 (refinement note on `RH⟹λ_a>0`, building on this audit thread's own Round 122 finding).

Verdict: **v13.867's bug diagnosis is confirmed exactly, independently re-derived and re-tested by hand rather than accepted on the entry's word. But this round finds v13.867's own blast-radius assessment is narrower than its own bug archaeology supports, and produces new evidence — of a magnitude that should raise real concern — that the affected scope is larger than stated. v13.868 confirmed, citation-accurate.**

## 1. The bug itself — confirmed independently, twice

**The wrong constant.** Recomputed `ψ(1/4)` myself via `mpmath` at 30 digits: `-4.2274535333762654...`, matching v13.867's figure exactly. The hardcoded `PSI_Q=-3.9170715877437315` in the posted `research-notes/bucket2_cancellation_screw.py` — the exact module I used for independent verification in Rounds 118 and 120 — is confirmed present at line 29, confirmed wrong, confirmed to differ from the correct value by `2×0.15519`, matching the claimed "smoking gun" (`|c_1|≈0.154`) to the stated precision.

**The decisive test, independently reproduced.** I patched a scratch copy with the corrected `PSI_Q` (disclosed here, one-line, mechanical fix — the same narrow exception this audit thread has used since Round 103) and recomputed `g(t)/t` myself: `t=6: -0.0522`, `t=8: -0.0182`, `t=10: -0.0029`, `t=12: -0.0115` — matching v13.867's reported values (`-0.052, -0.003, -0.012`) essentially exactly. The bug diagnosis is real, not a false alarm, and the entry's own disclosed guardrail (assert hardcoded constants against `mpmath` at import time) is the right fix.

## 2. What I found beyond what v13.867 reported: the blast radius looks wider

v13.867 §3 ("Compromised") lists the `Ae^A` scaling law, `L_0=0.48`, `α_∞=0.48`, the PAIR-H bulk/edge split, and the numerical programs of **v13.852–855, v13.862** — i.e., everything built on top of v13.844's R3 reformulation. It does **not** list v13.840 or v13.842 among the compromised entries.

But v13.867's own §2 bug archaeology names the exact run directory carrying the bug: `20260928-155806-bucket2-distributional-ta/scripts/screw.py`, "inherited by `20260928-165927`." **`20260928-155806` is v13.840's own cited provenance run, and `20260928-165927` is v13.842's own cited provenance run** — the original ratio determination and the Horn A falsification test, respectively. On the archaeology's own account, the bug predates and underlies *both* of those entries, not just the later PAIR-H chain.

**I tested this rather than just flag the citation gap.** Using the same posted `lsq85.py`/`screw.py` interface I used successfully in Round 120, with the corrected `PSI_Q`, natural BCs, `N=120`, `α=10^{-10}`:

| A | `A_coef` | `B_coef` | `L_1=A_{\rm coef}/e^A` | `L_0=B_{\rm coef}/(Ae^A)` | gate |
|---|---|---|---|---|---|
| 2 | `-3.022` | `+2448.22` | — | — | `0.00344` |
| 3 | `-8.266` | `+6470.31` | `-0.4115` | `+107.38` | (not captured) |

Compare to the buggy-kernel values reported throughout v13.840–864 (`B_{\rm coef}\approx+25.9` at `A=3`, `L_0\approx0.43`): with the fix, `B_{\rm coef}` is roughly **250× larger** at `A=3`, and the `L_0+L_1` cancellation that anchored R2 across a dozen entries is nowhere in evidence.

**I do not claim this is a reliable re-measurement, and I want to be precise about why.** The self-consistency gate for my `A=2` run is `0.0034` — two to three orders of magnitude worse than the `~10^{-5}$–$10^{-6}` gates reported throughout the (buggy-kernel) chain. That gate degradation is itself informative: it says the same discretization/regularization settings that were well-tuned for the old kernel are not adequately resolving the new one, so the specific numbers above should not be read as "the true `L_0`is now 107" — they should be read as "something changes by orders of magnitude, and a careful re-run (proper `N`/`α` convergence study, not a five-minute scratch script) is needed to say what."

**What this means for scope.** Taken together — the archaeology naming v13.840/842's own run directories, and my own quick test showing the *order of magnitude*, not just the fine details, changes under the fix — I think v13.867's blast-radius section understates the affected scope. The Horn A falsification (v13.842) and the original ratio determination (v13.840) were run on the same compromised kernel as everything explicitly listed as compromised. I am not asserting those conclusions are wrong — Horn A's falsification, in particular, rested on comparing *two* discretizations (Dirichlet weak-form and natural-BC least-squares) agreeing with each other, which is a form of robustness the later PAIR-H analysis didn't have — but "the same bug underlies both sides of that comparison" is a live possibility that v13.867 doesn't address and that a corrected re-run should explicitly settle, not just the PAIR-H-specific numerics RERUN-048 currently names.

## 3. v13.868 — confirmed

The citation ("Section 7 explicitly assumes RH... because under RH `A_a>0` for all `a`... already recorded source-faithfully in this ledger at v13.794") checked directly: v13.794 line 29 states, verbatim, "because under RH `A_a>0` for all `a`" — confirming this fact was already on record in the ledger well before this audit thread's Round 122 finding, and that v13.868 attributes it accurately (crediting the ledger's own prior record rather than overclaiming novelty). The strategic content (one-way implication; a certified `λ_a≤0` would be a real RH-relevant finding, a certified `λ_a>0` is necessary-but-not-sufficient) matches exactly what I derived and reported in Round 122. No new citation risk introduced.

## 4. Recommendation

Widen RERUN-048's scope, or explicitly charter a parallel re-run, to re-test v13.840's original ratio determination and v13.842's Horn A falsification on the corrected kernel — not just the PAIR-H/W1–W3 chain v13.867 names. Until that lands, I'd treat every `[N]` numerical claim in this entire Bucket 2 sandbox arc (v13.840 through v13.864) as provisional, not just the ones v13.867 explicitly flagged. The analytic-only results (v13.848's selection theorems, v13.858's G1–G3, v13.861's H1, v13.864's IDENT dissolution) are unaffected, since none of their proofs depend on the screw-function numerics — this distinction, which v13.867 draws correctly in its own §3, is worth restating clearly given how much of this round's finding is about the numerical side.

## Self-audit note

No error of my own found in what I checked. I want to be explicit that my own Round 118 and Round 120 "independent numerical confirmations" were run on this same buggy module — those rounds correctly verified that the sandbox's code produced the numbers it claimed and that its internal algebra was consistent, which remains true, but the foundational kernel constant both the sandbox and I were relying on was wrong. That is not a process failure on either side — auditing whether code matches its own claims is different from re-deriving every constant from first principles every round — but it's the honest record.

## Result

\[
\boxed{\textbf{v13.867's bug diagnosis confirmed exactly by independent re-derivation and re-test.} \textbf{New finding this round: the entry's own blast-radius list is narrower than its own bug archaeology supports — v13.840 and v13.842 were run on the same compromised kernel — and a preliminary (not reliable, gate-flagged) re-test shows the affected quantities change by orders of magnitude, not fine detail, under the fix. Recommend widening the chartered re-run to cover v13.840/842 explicitly. v13.868 confirmed accurate. All prior [N] numerical PASSes in this arc (Rounds 115–123) should be read as provisional pending RERUN-048's actual results — the algebra and citation-fidelity findings in those rounds stand; the numbers they were checked against do not, until recomputed.}}
\]
