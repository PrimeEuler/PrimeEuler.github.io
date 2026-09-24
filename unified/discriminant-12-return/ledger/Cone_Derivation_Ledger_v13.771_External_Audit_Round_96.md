# Cone Derivation Ledger v13.771 — External Audit Round 96

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.770, pushed since the second checkpoint (v13.769, commit `24ab4ca`). This entry is an unsolicited cross-check offered by the project owner from separate divisor-summatory work, applied to Lane A's open Schur-nonresonance gate — not an item this auditor assigned.

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `9352de9`. This entry is pushed as v13.771.

## 1. v13.770 — divisor-shell rapidity test, verified: honest negative result with a real methodological payoff

This entry tests whether the classical Dirichlet divisor-summatory geometry (the hyperbola `xy=n`, sampled at integer points `(k,n/k)`) can be identified with Lane A's finite-interval trace functionals via the shared rapidity coordinate. It explicitly and correctly concludes the direct identification fails, for three independent, correctly-argued reasons, while extracting a genuine strategic lesson. Every computation was independently re-derived.

**Exact structural matches, confirmed:**
- The shell/rapidity substitution: with `n=e^{2A}`, `(x_k,y_k)=(k,n/k)`, `s_k=\log k-A` — I confirmed `k=e^{A+s_k}`, `n/k=e^{A-s_k}`, and that `s_k` sweeps exactly `[-A,A]` as `k` ranges `1` to `n`, matching Suzuki's finite interval exactly.
- The Jacobian identity `y\,dx=n\,ds` — confirmed by direct substitution (`e^{A-s}\cdot e^{A+s}=e^{2A}=n`).
- The parity decomposition of the discrepancy measure `\nu_A^{\rm div}=\mu_A^{\rm div}-n\cdot1_{[-A,A]}\,ds` into even/odd channels — confirmed by direct substitution using the (correctly noted) evenness of the bulk density `n\,ds` on the symmetric interval.
- The boundary-scale match `\sqrt n=e^A` against the classical Dirichlet hyperbola-method corner scale `Q_n=O(\sqrt n)` (v13.315) — confirmed, a genuine consequence of the exponential substitution, not a coincidence.

**Three independently confirmed obstructions to a literal identification:**
1. **Scale mismatch (§5).** Using the standard asymptotic `H_n=\log n+\gamma+O(1/n)`, I confirmed `\langle\nu_A^{\rm div},1\rangle=\gamma e^{2A}+\tfrac12+O(e^{-2A})` — an `O(e^{2A})` leading term, not the hoped-for `O(e^A)` boundary scale. This correctly mirrors the well-known classical fact that the divisor summatory function's smooth main term `n\log n+(2\gamma-1)n` must be subtracted before the genuine `O(\sqrt n)` error term `\Delta(n)` becomes visible.
2. **Nonlinearity mismatch (§6).** The actual divisor error involves the fractional-part identity `nH_n-D(n)=\sum_{k\le n}\{n/k\}` — I confirmed this from `\lfloor n/k\rfloor=n/k-\{n/k\}` — and correctly notes this nonlinear flooring operation cannot be captured by pairing the linearly-defined measure `\nu_A^{\rm div}` against a fixed test function.
3. **Arithmetic-content mismatch (§7).** Lane A's finite-place carrier is tied to `-\zeta'/\zeta` (the additive, prime-power-supported von Mangoldt current), while the divisor function's Dirichlet series is `\zeta(s)^2` (the multiplicative convolution `1*1`) — genuinely different arithmetic objects. Correctly and soberly stated, not overclaimed as related beyond both arising from `\zeta`.

§8 adds a fourth, functional-analytic observation confirmed sound: `\ell_{0,A},\ell_{1,A}` are absolutely continuous kernel functionals, while `\nu_A^{\rm div}` is an atomic-minus-continuous distribution — different measure classes entirely, independent of the arithmetic-content mismatch.

**What the entry correctly extracts as useful (§9–10):** not a formula, but a renormalization strategy — subtract the smooth/full-line bulk contribution before estimating the finite-`A` boundary remainder, since the raw discrepancy is dominated by exactly this kind of bulk term in the classical analogue. This motivates a concrete, appropriately-hedged next target: decompose `M_{00}=M_{00}^{\rm bulk}+M_{00}^{\rm bdry}` (and similarly for `M_{1x}`) and test whether the bulk pieces cancel at leading order, with the predicted scale hierarchy (`\text{bulk}\sim e^{2A}`, `\text{boundary}\sim e^A`) explicitly flagged as a guide, not an established fact for the Suzuki moments themselves.

No errors found. This does **not** close the Schur-nonresonance gate — `M_{00}>-1`, `M_{1x}>-1` remains exactly as open as it was after Round 95 — but it's a legitimate, honestly-reported piece of exploratory work that earns its place: a concrete new strategy (bulk/boundary decomposition) grounded in a real structural analogy, with the analogy's limits stated precisely rather than glossed over.

## 2. Result

\[
\boxed{\textbf{PASS: v13.770's exact structural matches (shell, parity, boundary scale), independently re-derived, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.770's three obstructions to literal identification are correctly argued, not errors but genuine, well-reasoned negative findings.}}
\]
\[
\boxed{\textbf{No overclaiming: the entry does not assert the Schur-nonresonance gate is closed or narrowed by a proven bound.}}
\]

No errors were found in this auditor's own work this round.

## 3. Updated Lane A status

Unchanged in substance from Round 95: `M_{00}>-1`, `M_{1x}>-1` remains the load-bearing open item. v13.770 adds a fifth candidate strategy to the four already on record (v13.769 A.1): a bulk/boundary decomposition of the trace moments, motivated by — but not yet derived for — the Suzuki operators themselves. The next concrete step, per v13.770 §10, is to actually carry out that decomposition for `R_A^{(\pm)}` and the two moments, rather than for the divisor-shell analogue.
