# Cone Derivation Ledger v15.614 — Lane A: exact zeta series for fixed-product staircase constant and normalization/selector gate

**Date:** 2026-11-10. **Parents:** v13.197 exact divisor/triangle staircase, v14.367 circle secant dictionary, v14.767 normalized factor hyperbola scaling, v15.602 refined Casimir, v15.608–609 circle-area integrals, v15.611 fixed-step/co-scaled comparison, v15.612 shifted origin/measure robustness, v15.613 fixed-physical-product asymptotic. **Status:** [D] exact zeta transform and algebraic normalization; [N] independent finite evaluations; [O] physical origin, step selection, Hamiltonian and G. **Prewrite HEAD:** ac272a73218995dd1514b91a800902f32c438c2e; v15.614 collision search negative. Additive only, no frozen Suzuki modifications.

## Gate 88 — rapid, exact zeta-function expansion of S

For the exact v15.613 divisor-staircase asymptotic coefficient

S=Σ_{ℓ≥1}[ℓ^(3/2)−(ℓ−1)^(3/2)]/ℓ^(5/2),

write ℓ=1 separately, and for ℓ≥2 use
[ℓ^(3/2)−(ℓ−1)^(3/2)]/ℓ^(5/2)=ℓ^(−1)[1−(1−1/ℓ)^(3/2)].
The binomial expansion for |1/ℓ|≤1/2, interchanged with the absolutely convergent ℓ-sum, gives the **exact identity**

**S=1+Σ_{k≥1}(−1)^(k+1) binom(3/2,k)[ζ(k+1)−1].**

The subtracted 1 is important: it removes the isolated first staircase row and the series converges exponentially in k rather than merely as a power tail. Since |binom(3/2,k)|≤3/8 for k≥2 and ζ(k+1)−1≤2^(−k) for k≥2, the truncation after K≥2 has conservative bound ≤(3/8)2^(−K). Numerically S=1.885331267660461576438... (60-digit mpmath transformed sum; checked against direct positive summation). It is a classical discrete staircase coefficient, not an externally inserted physical coupling.

## Gate 89 — finite physical-product normalized response is not a unique q=2 fingerprint

Fix X>0, u=1/q, n=floor(Xq²), original physical transition s=1, using the v13.197 staircases and v15.613 circle-Jacobian boundary integral. Define dimensionless R_q(X)=B_D(q,X)/B_T(q,X) and complement share 1−R_q. From v15.613, as q→∞,

**R_q(X)∼S q^(−3/2), q^(3/2)R_q(X)→S** for every fixed X>0.

At q=2 exact-column numerical values are:
X=1: R=.7517077230; X=2: .6158392707; X=3: .5668360449; X=5: .5268358294.
The ratio cancels common amplitude and overall units, but explicitly depends on the physical cutoff X at finite q. The renormalized limit removes leading q-decay but yields the **same** S along all refinement trajectories. Neither is a physically derived q=2 selector. For q=1 and integer X≥1, the A-region contribution is zero by unit-strip support and staircase region structure; that is algebraic, not electromagnetic measurement.

## Gate 90 — compare secant decay and normalized defect ratio

At fixed X the unit-circle diameter/secant dictionary of v14.767 gives χ_q=2q√X/(q²X+1)∼2/(q√X). Then
**R_q(X)/χ_q^(3/2)→S X^(3/4)/2^(3/2)**.
If one additionally multiplies by X^(−3/4), this tends to S/2^(3/2), approximately 0.66656526207. This numerical proximity to 2/3 is **not** an exact equality: the difference is approximately 0.0001014, and no operator identity, physical cut-off or dynamical principle requires this ad hoc extra normalization. Do not infer an equality with the exact j=1/2 Archimedean 2/3 identity in v15.606. The secant height ratio decays q^(−1) and the divisor defect fraction q^(−3/2); the exponents are related by a chosen ratio of independently defined geometric quantities, not an established emission or gravitational law.

## Reproducer and independent verification

Conversation file `cone_gates_88_90.zip` includes `reproduce.py`, `checks.txt`, and `REPORT.md`. Reproducer reuses the retained v15.613 exact-column implementation, computes R and secant ratios at X∈{1,2,3,5}, q∈{1,2,4,8,16,32,64}, and computes S both from the exact accelerated zeta series and independent direct sum with 60-digit precision. Zeta transform difference <1e−16. The previous v15.613 asymptotic itself remains a separate external-audit item, not replaced by testing finite q.

**Conclusion:** finite q=2 has a robust *nonzero support distinction* relative to co-scaled dynamics, but no universal coupling or mesh selector is obtained from common scale cancellation or secant normalization alone. A physical choice of step operator, carrier measure and fixed-cutoff condition remains necessary; no value of G, photon, chirality or observed force law follows.

**HANDOFF** target external-audit, gravity, sandbox; status open; type exact zeta expansion/finite ratio/normalization selector negative. Independently check S identity and tail, all X-dependent q=2 ratios, S vs 2^(3/2)·(2/3), and the underlying q-asymptotic from v15.613. No Suzuki production or frozen changes.
