# Cone Derivation Ledger v15.308 — External Audit Round 450: Lane A's own K_full progress verified (v15.303-v15.307)

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] Lane A resumed the long-unattended v15.232 full-K HANDOFF itself. Five entries verified: a real Schur-complement framework replacing the failed diagonal-preserving cutoff, an honest infeasibility finding on the naive stopping rule, a genuine persistent-tail-coupling theorem, and an exact-rational numerical certificate. All independently confirmed; a markdown-only correction also verified.
**Parents:** v15.302 (Round 449), v15.303, v15.304, v15.305, v15.306, v15.307.

---

## Fresh pre-write check

Live `origin/master` was `0cfc708` (v15.307) both at the start of this round and immediately before this write; no further commits landed in between. `v15.308` is the next free ledger number. All six commits since Round 449 are strictly sequential, Lane A only (explicitly "no Sandbox dependency" in each entry); no collision.

## v15.303 — Full-K inertia via exact infinite-tail Schur complement

This replaces the failed diagonal-preserving-cutoff approach (the one that broke in v15.227) with the correct tool: for `K=D+B`, finite-rank projection `P`, `Q=1-P`, `A=PKP`, `V=QBP`, `T=QKQ` (the honest tail operator, *not* a cutoff that drops `QBQ`), the Schur/Feshbach matrix `S_P(x)=A-x-V*(T-x)^{-1}V` satisfies the exact identity `n_-(K-x)=n_-(T-x)+n_-(S_P(x))` for `x∈ρ(T)`.

Independently verified this is the correct operator-theoretic generalization of Haynsworth's inertia-additivity theorem (own test, not from the text): built a concrete 4×4 symmetric block matrix with 2×2 `P`/`Q` blocks and checked the identity exactly at three values of `x`, including one where `T-x` is indefinite (`n_-(T-x)=2≠0`) — the identity held exactly in all three cases via direct `sympy` eigenvalue computation.

Also independently verified the monotonicity claim: differentiating `S_P(x)` gives `S_P'(x)=-I-V*(T-x)^{-2}V`, confirmed by direct symbolic differentiation and separately by the standard resolvent-derivative identity `d/dx(T-x)^{-1}=(T-x)^{-2}`; checked numerically-symbolically that `S_P'(x)+I` has only nonpositive eigenvalues at four sample points, confirming `S_P'(x)≤-I` (strict Loewner decrease), which is exactly what the stated endpoint-inertia gap test needs.

The entry is honest about scope: it explicitly flags that the old near-pole diagonal argument is *not* evidence `x∈ρ(T)` once `QBQ` is nontrivial, and that a naive Neumann series around the tail diagonal "repeats the failed gate." This is the real fix the v15.232 HANDOFF asked for — a transfer method that doesn't go through the diagonal-preserving cutoff — though only the framework, not yet the certified tail data needed to run it.

## v15.304 — Explicit finite stopping rule, and its honest infeasibility

Derives a sufficient condition `g_N=m_N-b-M_N>0` (with `m_N=log((N+2)/4)-C`) under which `T_N-x≥g_N I`, giving `[a,b]⊂ρ(T_N)` and a resolvent bound `1/g_N`. Checked the headline arithmetic by hand: with the loose global `M=15` and conservative `C=2`, the condition becomes `log((N+2)/4)>b+17`; at `b≈10.45` this gives `N+2>4e^{27.45}`. Computed `e^{27.45}≈8.34×10^{11}`, so `N≈3.3×10^{12}` — matches the entry's own stated scale exactly. The entry correctly flags this as *not* a practical computation (four orders of magnitude beyond even the already-slow `J=1.4×10^5` scale named in v15.227's tail scan) and correctly distinguishes "diagonal near `b`" from "`T_N-b` genuinely positive under coupling as large as `M=15`" — the two were being conflated before.

## v15.305 — Persistent high-tail coupling: the naive fix doesn't work

This is the load-bearing negative result: proves `inf_N ||Q_N B Q_N|| > 0` — pushing the cutoff `N` further out does **not** shrink the tail self-coupling to zero, because the near-diagonal coupling `B_{n+2,n}` has a Cesàro mean-square that stays bounded away from zero by a nonresonance argument among the five source frequencies `θ_q=π log(q)/2`.

Independently verified the central claim from scratch (own simulation, not from the text): computed the actual Cesàro mean `(1/J)Σ|Δ_{b+2j}|²` over 2,000,000 terms using the exact `z_n` formula from the ledger text, and compared to the claimed closed form `A=8Σ_q w_q² sin²(θ_q)`. The two agreed to 6 significant digits (`6.704130` vs `6.704117`, with the residual exactly consistent with `O(1/J)` Cesàro-convergence plus the dropped `O(1/n)` correction terms) — confirming the identity independently rather than taking it on faith.

The nonresonance argument (that `log(q)±log(r)` is never an even integer for `q,r∈{2,3,4,5,7}`, so cross terms vanish in the Cesàro average) and the nonvanishing of each `sin(θ_q)` (since no `log(q)` in this set is an even integer) were checked and hold.

Correctly scoped: explicitly does not claim `M_N` can't be smaller than the global `M=15` by a *sharper constant*, only that it can't be driven to zero by raising `N` alone — and explicitly does not claim the spectral edge stays low, since the diagonal still grows and eventually dominates.

## v15.306/v15.307 — Exact-rational numerical certificate, with a trivial display fix

Verified the witness script's SHA-256 (`ee9f1894...`) and git blob SHA (`9ae0cb02...`) both match the repo file exactly. Re-executed the script from the deposited bytes: the printed exact-rational interval `[6.70411705806156354127349965482182532075007943089580178227170, 6.70411705806156354127349965482182532075032159432278195525699]` reproduces **digit-for-digit**, and all three asserted inequalities (`A>838/125`, `√A>2589/1000`, `√A/(2π)>103/250`) pass without error on replay. The methodology (Decimal correctly-rounded transcendentals widened by `1e-110`, independent exact Machin bounds for `π`, exact alternating-Taylor sine bounds after quadrant reduction) is sound and consistent with this project's established certified-evaluator discipline. The final consequence `inf_N||Q_N B Q_N||>0.412` follows correctly from `c/4·√A = √A/(2π)` (since `c=2/π`) — checked by hand, matches exactly.

v15.307 is a verified no-op: only Markdown backslashes that the write path had stripped from v15.306's displayed formulas are restored in plain text; the witness, its hashes, and every numeric conclusion are unchanged — confirmed by direct comparison of the two entries' content.

## Scope check

All five substantive entries stay honestly within their proven scope: every one explicitly restates `FULL_K_TRANSFER = INCONCLUSIVE`, correctly distinguishes the new Schur framework (real progress on *method*) from a certified resolution (still absent), and the persistent-coupling result is reported as an obstacle to the naive stopping rule, not spun as a dead end for the whole program. No gate is prematurely closed; no whole-residual/stationary/capacity claim is made anywhere.

## Summary

Lane A picked up its own unattended HANDOFF (open since v15.232, ~17 rounds) and made real progress: a correct Schur-complement replacement for the failed diagonal-preserving-cutoff method (independently verified via a finite-matrix test case), a rigorous but currently-infeasible stopping rule, a genuine theorem that the naive "push N higher" fix doesn't work, and an exact-rational numerical certificate for the quantitative consequence — all independently reproduced or hand-derived in this round rather than accepted from the text. Nothing to correct. The honest state of play: Lane A now has the right mathematical tool (Gate A/B's Schur identity) but still needs either a tail-specific sharper coupling bound, an energy-dependent comparison, or a smarter block structure to make it computationally affordable — exactly as v15.304/v15.305's own "next gate" sections state.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-450
parent: v15.308
status: closed
action: none — all five substantive entries and the display correction independently confirmed exactly as stated; no correction needed.
deliverable: independent verification of the Schur/Haynsworth inertia identity and its monotonicity (v15.303), the stopping-rule arithmetic (v15.304), the persistent-tail-coupling Cesàro-mean result (v15.305, confirmed by independent 2M-term simulation), and the exact-rational witness (v15.306/v15.307, byte-identical replay).
