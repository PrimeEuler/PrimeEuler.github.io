# Cone Derivation Ledger v13.759 — External Audit Round 92

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.756–758, the three entries pushed since Round 91 (v13.755, commit `d96413f`).

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `0dcc926`. This entry is pushed as v13.759.

All three entries continue the Suzuki finite-edge/Hermite–Biehler convergence lane (the thread that started with the Round 88 correction). None of them touch the norm-quotient/idele-class representation lane (last active at v13.736) — the user mentioned kicking two dormant threads back into action, but only one of them shows new commits so far. This audit covers what has actually landed.

## 1. v13.756 — finite-to-infinite HB determinant convergence, verified

Establishes that local-uniform scalar convergence `m_A→m_∞` alone is sufficient for local-uniform convergence of the normalized HB determinant `Δ_A→Δ_∞`. I independently re-derived the key decomposition
\[
\Delta_A-\Delta_\infty=\frac{m_\infty-m_A}{d_A}+(\tau_{HB}-m_\infty)\left(\frac1{d_A}-\frac1{d_\infty}\right)
\]
by direct algebra from the definitions (`d_A:=τ_{HB}-m_A(z_*)`, `d_∞:=τ_{HB}-m_∞(z_*)`), and confirmed both terms vanish uniformly on compacta given the hypothesis. The logarithmic-derivative convergence (§4, via Cauchy's formula for holomorphic convergence) and the Hurwitz-theorem zero-stability argument (§5) are standard complex analysis, correctly invoked and correctly hedged (§5 explicitly notes this does not imply real-axis zeros, since `τ_{HB}` is complex). The Krein resolvent-convergence discussion (§6) correctly separates what scalar convergence alone gives (rank-one trace convergence, §7) from what additional strong/norm convergence of reference resolvents and gamma fields would be needed for full operator convergence — appropriately marked open rather than assumed. No errors found.

## 2. v13.757 — reduction to a single channel ratio, verified

Reduces the finite Weyl function `m_A` to a Möbius function of a single ratio `ρ_A:=H_A/G_A` of the two (now source-faithful, post-correction) deficiency transforms. I independently re-solved the Möbius relation `m_A=-i[(z-i)+(z+i)ρ_A]/[(z-i)-(z+i)ρ_A]` for `ρ_A` and confirmed it matches the entry's boxed result `ρ_A=\frac{z-i}{z+i}\cdot\frac{im_A-1}{im_A+1}` exactly (verified by multiplying my own solved form through by `i` to match). I then substituted the already-audited infinite target `m_∞=-i(a/b)D_ξ/Ξ` (Round 91) into the same relation and confirmed it reproduces the entry's `ρ_∞` exactly.

The asymptotic link to the affine contamination (§10) is a genuine unification: substituting the already-audited `α_A,β_A` formulas (v13.745, Round 91) and doing the elementary limit analysis, I confirmed that bounded `r_{0,A},r_{1,A}` forces `α_A,β_A→0` (since `Ae^{-A}→0`), and that the sharper sufficient conditions `r_{1,A}=o(e^A/A)`, `r_{0,A}=o(e^A)` are exactly what's needed term-by-term in the `β_A` expansion. This correctly shows the same two scalar ratios control both the previously-separate affine-edge and Weyl-convergence questions.

One item flagged rather than fully verified: §2's claim `u_{A,-}=-Ru_{A,+}`, extending the elementary fact `DR=-RD` (which I verified directly: `(DRf)(x)=-f'(-x)=-(RDf)(x)`) to the transported operators on `H(S_A)`. This is a reasonable extension given the established reflection-compatible structure, but the entry doesn't fully spell out how `R` acts on `H(S_A)` versus `H(T_A)`, so this auditor treats it as plausible-but-not-independently-re-derived-from-more-primitive-assumptions rather than confirmed from scratch. No error found, but flagged for a future round if it becomes load-bearing elsewhere.

## 3. v13.758 — boundary-functional obstruction, verified (and commendable self-correction)

This entry's own §0 records that it caught an invalid step before committing it: treating the response moments `M_{00},M_{1x},M_{0e},M_{1e}` (which are boundary-functional evaluations `ℓ_{j,A}(R_Af)`) as if they were automatically Hilbert-space inner products, which would have licensed an unjustified Cauchy–Schwarz bound. This is a correct and non-trivial functional-analysis distinction — a bounded linear functional on a Banach space is not automatically represented by an inner product unless a Riesz representation theorem is established for it, and none was. The entry does not import one, and instead falls back to the strictly weaker but valid duality bound `|M_{0e}|≤‖ℓ_{0,A}‖·‖R_A^{(+)}f_+‖`, which is just the definition of the dual/operator norm and requires no additional structure.

Independently verified:
- The parity split `e^x-1-x=(\cosh x-1)+(\sinh x-x)` — confirmed by direct algebra (`\cosh x+\sinh x=e^x`).
- The resulting vanishing-by-parity reductions `M_{0e}=ℓ_{0,A}(R_A^{(+)}f_+)`, `M_{1e}=ℓ_{1,A}(R_A^{(-)}f_-)` — confirmed using the already-established parities of `ℓ_{0,A}` (even), `ℓ_{1,A}` (odd), and of `R_A` acting on even/odd inputs (from v13.745, already audited).
- The basepoint-vanishing conditions `f_+(0)=f_+'(0)=0` and `f_-(0)=f_-'(0)=f_-''(0)=0` — confirmed by direct differentiation (`\cosh0-1=0`, `\sinh0=0`; `\sinh0-0=0`, `\cosh0-1=0`, `\sinh0=0`).
- The resulting sufficient asymptotic criteria on the norm quotients, obtained by substituting the new bounds into the already-audited `α_A,β_A` formulas — correct, consistent with v13.757's parallel analysis on `r_{0,A},r_{1,A}` directly.

The entry is honestly scoped throughout: it explicitly states what the helix/screw–Weil bulk carrier *can* address (the response norms `‖R_A^{(±)}f_±‖`) versus what it *cannot* (the boundary functionals `ℓ_{0,A},ℓ_{1,A}` themselves and the Schur-complement denominators `d_{0,A},d_{1,A}`), consistent with v13.742's earlier observation that twice-differentiating the equation discards exactly this boundary data. No errors found; this is careful, self-policing work.

## 4. Result

\[
\boxed{\textbf{PASS: v13.756, independently re-derived, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.757, independently re-derived, no errors (one reflection-transport step flagged as plausible-not-fully-reconstructed rather than confirmed).}}
\]
\[
\boxed{\textbf{PASS: v13.758, independently re-derived, no errors. Notable: the entry self-caught and retracted an invalid Cauchy–Schwarz step before it was ledgered.}}
\]

No errors were found in this auditor's own work this round.

## 5. Next gates to watch

1. The now-unified target: bound `r_{0,A},r_{1,A}` (equivalently the norm quotients in v13.758 §4) to close simultaneously the affine-edge contamination (`α_A,β_A→0`) and the finite Weyl convergence (`ρ_A→ρ_∞`, hence `m_A→m_∞`, hence `Δ_A→Δ_∞`).
2. The boundary-functional/Schur-denominator estimates (`‖ℓ_{0,A}‖,‖ℓ_{1,A}‖,d_{0,A}^{-1},d_{1,A}^{-1}`) that v13.758 correctly identifies as outside what the bulk helix/Weil carrier alone can supply.
3. The norm-quotient/idele-class representation thread (v13.730–736) — still no new activity as of this round, despite being one of the two threads the user restarted.
4. v13.757's unverified reflection-transport step (§2), if it becomes load-bearing in a future entry.
