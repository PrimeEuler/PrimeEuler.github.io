# Cone Derivation Ledger v13.866 — External Audit Round 122

Date: 2026-09-29

Auditor: External audit thread (Claude, independent instance).

Scope: v13.864 (IDENT — the identification leg dissolves into `(CONV) ∧ (SUZ-LIM)`, with `(SUZ-LIM)` shown to be RH-hard by Suzuki's own Corollary 1.6). v13.865 (a build-conventions note, not a derivation) and the ~30 "raw-wrap" commits are infrastructural and out of mathematical-audit scope — spot-checked one and confirmed genuinely cosmetic (Jekyll/Liquid brace-escaping, no content change).

Verdict: **PASS on v13.864, with a bonus finding directly relevant to the standing `λ_a>0` strategic note (v13.860), found while checking this entry's citations rather than claimed by the entry itself.**

## 1. The central citation, checked directly and exactly

v13.864's whole verdict rests on one factual claim about the source: "Corollary 1.6 (textual fact): (1.12) ⟹ RH." I pulled page 7 directly rather than accept this secondhand. Suzuki's Corollary 1.6, verbatim: "If one can choose `θ=θ(a)` and `φ(a,z)`... such that `lim_{a→∞}e^{φ(a,z)}W(a,θ;z) = ξ(1/2-iz)/(ξ(1/2-iz)+ξ'(1/2-iz))` (1.12) holds uniformly on every compact subset `K⊂C`, then RH holds." This is exactly `(1.12)⟹RH`, word for word — not a stretch of the source, not a paraphrase drifting from what's actually claimed. The surrounding text also confirms the "conjectural"/"heuristic"/"we do not pursue" framing v13.864 attributes to it: the same page states the limit formula's justification is deferred to §7, is "motivated by" RH-dependent results from a cited reference, and that the paper explicitly declines to pursue whether `θ=π` is the natural choice.

I also checked §7.8 directly (cited as the source of the `B_0/B_π=(a/b)D/\Xi` boundary-form computation): the de Branges reproducing-kernel construction and the `θ=π` boundary-form computation (yielding `(2i/π)ξ'(3/2)ξ(1/2-iz)`) are exactly as described, confirming this part of the citation chain is real machinery in the source, not invented.

## 2. The argument itself, assessed

Given the citation holds, the entry's logic is sound: it correctly separates "our finite-`A` computation matches Suzuki's finite-`a` construction" (§2, closed — `v_{+i}=T_A^{-1}e_{+i}` satisfying `D_A^*v_{+i}=+iv_{+i}` literally *is* Suzuki's deficiency vector per §6.3, and v13.848 already established the Galerkin computation converges to it) from "Suzuki's own conjectural infinite-volume limit holds" (open, and now correctly identified as RH-hard rather than merely difficult). The diagnosis that the `\delta_\infty` discrepancy equation "cannot fail while `(CONV)` and `(SUZ-LIM)` hold" (§3d) is a correct structural point: an exact identity (the de Branges computation under RH) can't be "corrected" by adding a boundary term without that being a contradiction, so the old W3 §6 "if NO" branch — treating a possible mismatch as something to fix with a boundary correction — was a category error, and retiring it is the right call. This is good analytic hygiene: recognizing that a sub-question was ill-posed is real progress, not a null result.

## 3. Bonus finding, directly relevant to v13.860

Reading page 7 for the Corollary 1.6 citation, I also found a sentence not cited by v13.864 but directly bearing on my own standing strategic note (v13.860): "**Under RH, one has `A_a>0`**, so that `λ=0` may be chosen in `T_a` for every `a>0`." This is a one-directional implication — `RH⟹(λ_a>0` for all `a)` — not stated as an equivalence. It sharpens, but does not overturn, v13.860's claim that `λ_a>0` at one fixed finite `a` is not RH-equivalent: there is no stated implication in the other direction (`λ_a>0` at some finite `a` does not, per this text, establish RH). Two consequences worth recording: (a) `λ_a>0` remains, as claimed, a tractable, non-RH-equivalent target — my earlier note's central claim holds; (b) there is now a known, textually-grounded *pressure-test* angle: a rigorous demonstration that `λ_a≤0` at some specific finite `a` would be a genuine RH-disproof, so if Lane A's numerics for the bottom eigenvalue of the relevant operator ever came back non-positive with a certified margin, that would be a real finding, not just an inconclusive result. This is worth folding into the strategic note's record but does not change its recommendation.

## Self-audit note

No error of my own found this round. The bonus finding is a positive addition to the record, surfaced by doing the citation-check thoroughly rather than narrowly.

## Result

\[
\boxed{\textbf{PASS: v13.864 confirmed.} \textbf{Corollary 1.6's exact statement — (1.12)}\Rightarrow\textbf{RH — checked directly against the source and reproduces precisely.} \textbf{The identification leg's dissolution into (CONV)}\wedge\textbf{(SUZ-LIM), with (SUZ-LIM) now correctly flagged as RH-hard and outside Bucket 2's scope, is a genuine and correctly-reasoned scope clarification.} \textbf{Bonus: Suzuki's text states RH}\Rightarrow\lambda_a>0\textbf{ for all }a\textbf{ (one direction only) — refining, not overturning, the }\lambda_a>0\textbf{ strategic note's non-RH-equivalence claim, and naming a legitimate pressure-test angle (a certified }\lambda_a\le0\textbf{ finding would disprove RH).}}
\]
