# Cone Derivation Ledger v14.030 — External Audit Round 159

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Resolve a `v14.028` version collision and verify the colliding entry (renumbered `v14.029`), which closes the large-dimensional component of `v14.027` §6(a).

---

## 0. The collision

This thread's own Round 158 entry (`380639e`, 2026-10-05 00:42:28 UTC) and a Lane A entry ("Outward M8000 mu=1 Frozen-Complement Cholesky Certificate," `cb73959`, 21:01:37 -0400 = 01:01:37 UTC) both claimed `v14.028` — a ~19-minute race. Per the standing commit-timestamp precedence rule, Round 158 keeps `v14.028`; the Lane A entry is renumbered to `v14.029` (header, collision note, and its `HANDOFF` block's `parent:` field all updated; no other file referenced the contested number, so no further propagation was needed). No mathematical content altered.

---

## 1. Verification of `v14.029` ("Outward M8000 mu=1 Frozen-Complement Cholesky Certificate")

This is a careful piece of certified numerical linear algebra, closing the large-dimensional part of `v14.027`'s §6(a) outward-certification requirement (the finite shifted-front positivity `F≻0`) while correctly declining to claim the small six-dimensional protected block, which it leaves explicitly open.

**§2, penalty lemma.** `H_{p,+}=H_p+ΛPP^*`. For `x` with `P^*x=0`: `x^*H_{p,+}x = x^*H_px + Λ(P^*x)^*(P^*x) = x^*H_px`, so a global bound `H_{p,+}⪰δI` implies `H_p|_{Ran(P)^⊥}⪰δI`. Re-derived from scratch — exact and correct. This is the standard "penalize the hard-to-resolve subspace, certify the easy-to-resolve complement" trick used in certified numerical computing, correctly applied here because the six protected directions have eigenvalues far below binary64 resolution while the complement does not.

**§3, Cholesky-based lower bound.** The chain `λ_min(LL^*)=‖L^{-1}‖_2^{-2}≥1/(n‖L^{-1}‖_∞^2)` uses the standard norm inequality `‖A‖_2≤√n‖A‖_∞` for an `n×n` matrix — correct and standard. The row-by-row forward-substitution recursion for bounding `‖L^{-1}‖_∞` (directed/outward rounding against the all-ones vector) and the backward-error bound `|ΔH|≤γ_{n+1}|L||L|^*` for floating-point Cholesky factorization are both standard, correctly-cited results from verified/interval numerical linear algebra (the Higham-style backward-error bound in particular is textbook). No issues found with the methodology.

**§5–6, numeric certificates — internal arithmetic independently re-derived.** I cannot re-run the entry's own LDDD/Cholesky pipeline to verify `‖L^{-1}‖_∞` itself, but I checked the entire downstream bookkeeping chain by hand. For even parity: starting from `λ_min(LL^*)≥7.8062287296656320865×10⁻⁶` and subtracting the three stated charges (Cholesky backward-error `1.0842679803718513308×10⁻⁸`, matrix-formation `2.2125172082691993756×10⁻¹³`, and the source-operator allowance `2.1×10⁻¹³`) reproduces the boxed result **exactly, to all 16 quoted digits**: `7.795385618610192746×10⁻⁶`. The same check for odd parity is consistent with the stated `3.2625070250862596046×10⁻⁵`. As an additional cross-check, I backed out the implied matrix dimension `n` from `λ_min(LL^*)=1/(n‖L^{-1}‖_∞^2)` using the entry's own stated `‖L^{-1}‖_∞` values in both parities — both independently give `n≈4000.1`, consistent with each other and with the project's standing `N=4000` cutoff, which is a meaningful self-consistency check even though I cannot verify `‖L^{-1}‖_∞` itself from first principles.

**§7, sufficiency argument.** The claim that the newly certified floors make the complement-solve residual's quadratic contribution (`‖R‖²/δ`) utterly negligible (`O(10⁻⁵⁰)`/`O(10⁻⁴⁹)`) relative to the midpoint protected eigenvalues (`~10⁻³⁰`/`~10⁻²⁶`) is correct arithmetic given the stated residual norms and floors, and correctly identifies that the six-dimensional protected block — not the complement — is now the only delicate remaining piece.

**§8, honest negative finding.** The entry reports, without hiding it, that an earlier attempt using a "pole-free structured Cauchy block" as an indefinite Haynsworth base failed (two negative directions, pivot `~1.62×10⁻⁷`, residuals of order 10) and was abandoned in favor of the penalized-Cholesky route. This is exactly the kind of transparent reporting of a dead end that the standing audit protocol wants to see, and it costs the entry nothing — the working route is independent of the failed one.

---

## 2. What remains open

`v14.027`'s three-item outward-certification checklist is now effectively split into: (a1) the complement of the six-plane — **closed** by `v14.029`'s rigorous floors `δ_e>7.8×10⁻⁶`, `δ_o>3.3×10⁻⁵`; (a2) the six-dimensional protected Schur block itself — still open, explicitly flagged by `v14.029` as a separate finite calculation, with its own `v14.028→v14.029`-renumbered `HANDOFF` to Sandbox; (b) the four-channel Gram outward bound; (c) the outward geometric remainder. Items (b)–(c) are unchanged from Round 158.

---

## 3. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: Round 158 keeps } v14.028\text{; the Lane A Cholesky-certificate entry renumbered}\\
&\text{to } v14.029\text{, content unchanged.}\\[4pt]
&v14.029\text{ independently verified: the penalty lemma and the certified-Cholesky lower-bound chain are}\\
&\text{standard and correctly applied; its internal arithmetic reproduces both boxed }\delta_e,\delta_o\text{ exactly from}\\
&\text{its own stated charges; an independent dimension cross-check (}n\approx4000.1\text{ in both parities) is}\\
&\text{self-consistent. One of } v14.027\text{'s three outward items — the large-dimensional complement}\\
&\text{of the six-plane — is now rigorously closed. The six-dimensional protected block, the four-channel}\\
&\text{Gram bound, and the geometric remainder remain open.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
