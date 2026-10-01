# Cone Derivation Ledger v13.895 — Sandbox: ψ = log lcm Identity; Λ as the Jump Function

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [D] classical identities; [N] auditor-thread numerics (cited, not re-run); [I]/[O] assessment
**Authorization:** Jeremy, 2026-10-01 ("absolutly lets ledger that" — auditor-thread point relayed by Jeremy)
**Predecessors:** v13.894 (Suzuki stability test); auditor thread (prime-powers discussion)
**Note:** v13.893 is audit-thread; this takes the next free version.

---

## The identities [D]

1. **d(p^m) = m+1** — trivial: the divisors of p^m are 1, p, p², …, p^m.
2. **lcm(1,…,n) moves only at prime powers:** if n = p^k, the lcm picks up one
   more factor of p (p^k was not needed to cover any smaller number); otherwise
   the lcm does not move. Hence
   log lcm(1,…,n) − log lcm(1,…,n−1) = Λ(n)
   — the "LCM rate" is the von Mangoldt function, viewed as multiplicative
   jumps rather than an additive indicator.
3. **log lcm(1,…,⌊x⌋) = ψ(x)**, the Chebyshev function — classical (Chebyshev).
   So ψ(x) − x fluctuating against the zeta zeros is the explicit formula in
   its most basic form.

## Numerical confirmation [N] (auditor thread — cited, not re-run here)

max|log(lcm(1..n)) − ψ(n)| = 1.8×10⁻¹² over the tested range — pure
floating-point noise. The identity holds exactly.

## Gap-prediction null [N] (auditor thread — cited, not re-run here)

Prime-power presence in the first k composites vs gap length: correlations
~0.001–0.005 — no predictive signal. Since LCM rate = Λ(n) identically, there
is no separate "LCM rate" experiment left to run on gaps; it would reproduce
that number exactly.

## Assessment [I]/[O]

1. **Different question from our ablation.** The null above concerns gap
   *prediction* (where the next prime lands). Our in-flight prime-power
   ablation asks which jumps of ψ hold the Weil form *positive* — positivity
   anatomy, not forecasting. The identity sharpens that question; it does not
   dissolve it.
2. **No flattening of the sandbox arc.** That the untwisted frequency
   mechanism is the explicit formula was already recorded honestly in v13.891
   ("a binary view of the standard explicit formula, not a newly discovered
   zero mechanism"). But the arc is not all ψ-rediscovery: the twisted loops
   (χ₃, χ₄, χ₅, χ₁₂; v13.885–890), the two selection axes (residue support vs
   character holonomy, v13.887 — lives in twisted sums, not in ψ), the
   trivial-zero sign corrections (v13.890/891), and the positivity program
   (v13.894 + the full-A_a FEM joint experiment) are distinct contributions.
3. **Agreement, not refutation.** "Λ(n) is genuinely the right object" is our
   knife-edge finding stated from the other side: only the exact Λ weights
   hold A_a positive — the joint experiment showed the indicator captures 96%
   of the Λ lift yet still lands negative. The identity explains *why* the
   knife-edge sits exactly at Λ: Λ is ψ's jump function, the canonical prime
   weighting. The Weil-form prime sum Σ Λ(n)/√n·(|t|−log n) now has its
   classical name attached.

## Implication

One line for the weights: the positivity program's "Λ weights" are the jumps
of ψ(x) = log lcm(1,…,⌊x⌋). Nothing in this entry changes v13.894 or the joint
experiment; it grounds them.
