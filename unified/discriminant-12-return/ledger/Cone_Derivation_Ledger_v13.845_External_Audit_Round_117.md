# Cone Derivation Ledger v13.845 — External Audit Round 117

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.844 — the Bucket 2 edge-criteria archaeology (tracing every prior entry from v13.742 onward that touched `α_A,β_A,r_{0,A},r_{1,A}`) and the proposed R0–R3 reformulation (retiring the falsified `o(e^A)`-type conditions in favor of finite normalized limits and a cancellation identity).

Verdict: **PASS. Every quoted citation verified against the actual ledger files (not the sandbox's paraphrase of them), and the central new mathematical claim (R2, the cancellation identity) independently re-derived by hand and confirmed correct.**

## 0. Method note

Unlike Rounds 114–116, every citation in this entry is to files already in this repo — no external PDF tooling needed. This let me check quote fidelity directly and exhaustively rather than sampling: I pulled the actual line ranges from v13.743, v13.757, v13.758, and v13.774 myself and diffed them against v13.844's quotes. The entry makes no new `[N]` numerical claims of its own — §2 is an explicit recap of the already-audited v13.840/v13.842 numerics (Rounds 115–116), and the new content is entirely archaeology (`[D]`) and analytic reformulation (`[I]/[O]`).

## 1. Citation fidelity — checked exhaustively, not sampled

- **v13.743**, the origin entry: the `α_A,β_A` definitions (`α_A:=A_{A,+}/(C_Ae^A)`, `β_A:=(AA_{A,+}+B_{A,+})/(C_Ae^A)`) reproduce exactly from §4. "The pure exponential edge source is recovered iff `α_A→0,β_A→0`" reproduces exactly (§4, immediately following the scaled-source derivation). The §10 warning — "the deficiency vector itself may carry `e^A`-scale boundary mass... The correct comparison is amplitude, not functional type" — reproduces exactly, word for word. This is the entry's most important archaeological claim (that v13.743's own author anticipated the failure mode Horn B later confirmed), and it checks out completely: the warning is really there, in those words, in the origin entry.
- **v13.757**: "A sufficient route to Weyl convergence is therefore: 1. establish asymptotic limits or controlled expansions `r_{0,A}=r_{0,∞}+o(1)`..." reproduces exactly (§9). The `o(e^A/A)`/`o(e^A)` sufficient-condition statement and "the same two scalar feedback ratios control both the affine contamination and the corrected deficiency shape" both reproduce exactly (§10). I also independently confirmed the `α_A=-e^{-A}(1+r_{1,A})`, `β_A=-e^{-A}[A(1+r_{1,A})+1+r_{0,A}]` formulas appear here (attributed to v13.745) — v13.844 attributes the same formulas to v13.773 §5, which is also accurate (v13.773 §5 independently restates them after retracting the Schur-ratio derivation that produced them in v13.745). Both attributions are individually correct; it's a pre-existing minor cross-reference looseness between two much older entries, not something v13.844 introduced.
- **v13.758**: "bulk explicit-formula current + two boundary constants are both required" reproduces exactly — correctly presented as v13.758's own boxed restatement, and v13.758 itself credits it to v13.742, which v13.844 doesn't repeat but doesn't misrepresent either.
- **v13.774**: all three quoted fragments ("the slope constant `α_A` survives one derivative as a constant source"; "both affine constants disappear from the twice-differentiated interior current"; "`β_A` survives only as primitive value/boundary data") reproduce exactly from §2, in that order. "The pure compensated problem of v13.733 is the special case `α_A=β_A=0`" reproduces exactly from §3. The corrected edge equation `S_{edge}q_±=±i(e^{-ξ}-δ_0)+𝓑_{α,β,±}` reproduces exactly, boxed, from §3 — confirming R3's claim that this equation already exists and simply needs the measured `(α_∞,β_∞)` fed into the `𝓑` term instead of the old `(0,0)` assumption. The zero-frequency principal-part formula `β_A/p, -α_A/p²` reproduces exactly from §4.
- **Lemma 6.2 / uniqueness claim**: "Suzuki's deficiency vectors are unique when `T_a` is invertible... there is nothing to select" is consistent with what I independently verified from the primary source in Rounds 115–116 (`T_a` invertible for `λ<λ_a` gives unique solutions to `(T_av)(x)=C_±e^{±x}`, per Lemma 6.2's proof).

Zero misquotes found across seven cited entries. This is the strongest citation-fidelity showing of any sandbox entry so far.

## 2. R2, the cancellation identity — independently re-derived by hand

This is the entry's one genuinely new mathematical claim, so I did not accept the derivation as given — I redid it myself from the definitions. With `C_A=1` (the entry's stated normalization), `β_A=-e^{-A}[A(1+I_{1,A})+(1+I_{0,A})]`. Substituting the assumed leading asymptotics `I_{1,A}\sim L_1e^A` and `I_{0,A}\sim L_0Ae^A`:

\[
\beta_A = -e^{-A}\big[A\cdot I_{1,A} + I_{0,A} + A + 1\big] \sim -e^{-A}\big[AL_1e^A + L_0Ae^A\big] + O(e^{-A}(A+1)) = -A(L_0+L_1) + o(1).
\]

So `β_A` stays bounded (and the numerics show it tending to `0`) if and only if `L_0+L_1=0`; otherwise `β_A\sim-(L_0+L_1)A\to\pm\infty` linearly. This matches the entry's claim exactly, and I worked it from the raw definitions rather than checking their algebra line-by-line — it's correct. Plugging in the reported `L_1\approx-0.48,L_0\approx+0.48` gives `L_0+L_1\approx0` at the precision reported, consistent with (not proof of) the identity — the entry is appropriately honest that the cancellation itself is "numerically supported... analytically unexplained," not derived from first principles. That's the right amount of confidence for what's actually been shown.

## 3. Logical assessment of the reformulation and the directed evaluations

- **R1** (finite normalized limits replace the vanishing conditions) is a correct weakening: `o(e^A/A)→0` and `L_1` finite are genuinely different statements, and R1 is honestly flagged as a conjecture about the true (unique, where `T_a` is invertible) solution rather than something the numerics prove.
- **R0** (renaming "criteria" to "edge asymptotics") is a well-argued point, not just cosmetic: since Lemma 6.2 gives uniqueness (conditional on `λ_a>0`, itself flagged as open), there was never a selection problem, only a property-of-the-unique-solution problem — the old "criteria/gate" framing did suggest an admissibility test that was never actually what was being computed. §4(d)'s handling of this is careful, not overreaching: it explicitly notes the uniqueness claim itself inherits the unresolved `λ_a`-sign caveat rather than treating Lemma 6.2 as unconditionally closing the matter.
- **§4(c)**'s distinction between the validation gate (checks a computed `v` satisfies Suzuki's equation) and the old growth criteria (characterizes the continuum solution's asymptotic shape) is the sharpest single point in the entry and is correct: a small residual proves the numerics solved *an* equation faithfully, not that the solution has any particular growth rate. Conflating the two would have been the easy mistake to make here, and the entry avoids it.
- The open items in §5 are honestly triaged: the Tikhonov minimum-norm selection question (does it equal Suzuki's true `v_±`, given the 2D near-nullspace from v13.838) is correctly flagged as still open and load-bearing for everything else in this entry, not quietly assumed away.

## 4. What remains unverified

As with every sandbox `[N]` entry, the specific numerical values in §2 (recapped from v13.840/v13.842) were not re-derived here — they were already the subject of Rounds 115–116's audits, and this entry doesn't add new numerics of its own. Nothing here changes that prior assessment.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.844 confirmed.} \textbf{Every citation checked against seven prior ledger entries reproduces exactly — the strongest citation-fidelity result of any sandbox entry audited so far. The new analytic content (R2, the cancellation identity }L_0+L_1=0\textbf{) was independently re-derived by hand from the raw definitions and confirmed correct, distinct from and not dependent on the sandbox's own algebra. The reformulation (R0–R3) is a sound, appropriately-hedged replacement for the falsified edge criteria, with the remaining open items (minimum-norm selection vs. Suzuki's true }v_\pm\textbf{; the cancellation identity's mechanism; the }\lambda_a\textbf{ sign) honestly preserved as open rather than absorbed into the conclusion.}}
\]
