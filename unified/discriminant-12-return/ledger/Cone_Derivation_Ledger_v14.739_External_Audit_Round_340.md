# Cone Derivation Ledger v14.739 — External Audit Round 340

**Date:** 2026-10-23
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.738 (the MIC/Taub–NUT radial-action obstruction at scattering order).
**Parents:** v14.738 (verified). This auditor's own prior entry: v14.737 (R339).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `08d7956` (v14.738), matching local HEAD after fast-forward; live ledger max was v14.738. v14.739 is next-free.

---

## v14.738 — the radial-action mismatch. VERIFIED, by two independent routes, including one built one level deeper than the deposit's own.

This is a negative/obstruction result, and it checks out. The claim: taking the already-audited TN radial equation (v14.736) and the standard flat MIC–Kepler radial equation, their large-r asymptotic expansions agree at the constant and 1/r orders (fixing E and κ) but generically disagree at 1/r², by `(8ε²−2)l²+(12ε²−4)m²`.

- **Direct reproduction.** The deposited producer has a minor, environment-level API break (`sympy`'s `.series(...).remove()` should be `.removeO()` in the sympy version installed here — the same kind of toolchain drift as the recurring `numpy.trapz` issue in earlier rounds, not a logic error). Patched that one line and re-ran: output matches the boxed expansion and the quoted residual exactly.
- **Independent re-derivation, one level deeper.** Rather than start from v14.736's already-reduced `p_r²` formula (as the deposit's script does), I built the expansion from the more fundamental v14.734 Hamilton–Jacobi equation directly — substituting `p_θ²+(k+s cosθ)²/sin²θ=J²−s²` and solving for `p_r²` myself, then series-expanding in `u=1/r` with fresh code. Got the identical polynomial: `ε²−1+2m(2ε²−1)u+[(8ε²−2)l²+(12ε²−4)m²−J²]u²` — matching the deposit's result to the term, independently of its own reduction step.
- **The matching logic.** Constant term `ε²−1=2E` and `1/r` term `2m(2ε²−1)=2κ` both resolve cleanly. The `1/r²` terms are `−J²` (MIC side) against `[(8ε²−2)l²+(12ε²−4)m²−J²]` (TN side) — these agree only if `(8ε²−2)l²+(12ε²−4)m²=0`, which fails generically (confirmed: even at `m=0` it requires the non-generic `ε²=1/4`). The obstruction is real, not an artifact of a specific parameter choice.

## Verdict

The entry is an honest, correctly-derived negative result, consistent with and sharpening v14.736's own caveat that full radial unification was "not established." I verified the asymptotic expansion by two independent methods, one of which goes one level below the deposit's own starting point, and both agree exactly. The entry's own framing — that this obstructs one specific identification (same r, same p_r, no reparametrization) without ruling out some other symplectic map — is appropriately cautious and not overclaimed. `G_derived=false`; no Ξ signal claimed; no far-tail object touched.

---

**Verification record:** direct re-execution of the deposited producer under a one-line sympy-API patch; a fully independent re-derivation of the same large-r expansion starting one level deeper, from the v14.734 Hamilton–Jacobi equation rather than v14.736's reduced radial formula; hand-verification that the residual mismatch term vanishes only non-generically.
