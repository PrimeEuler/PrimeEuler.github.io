# Cone Derivation Ledger v15.457 — External Audit Round 497: v15.456's finite-annulus truncation barrier independently re-derived and confirmed numerically; one cosmetic float-rounding note in the printed ratio

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.456 — proving that the 45-diagonal near-band operator from Round 496 cannot itself be truncated to finitely many annuli and treated by a separate triangle charge on the rest, because the constant-Hankel operator's diagonal block at *every* annulus index `a`, however large, has a Rayleigh quotient on the simple normalized constant vector exceeding a fixed `1/8` (not decaying with `a`) — independently re-derived and confirmed both analytically and numerically on small finite blocks. Correctly scoped as ruling out one truncation strategy, not the full signed joint gate.
**Parents:** v15.454 (Round 496), v15.455, v15.456.

---

## Fresh pre-write check

`git fetch origin master` returns `8643809` (v15.456), identical to the head just read. `v15.457` is next free; no collisions.

## What this entry rules out, and why it matters

Round 496 reduced the constant-Hankel problem to a 45-diagonal near-band operator `C_near(22)`, still infinite (infinitely many annulus indices `a>=0`). The obvious next move would be to further truncate to finitely many annuli (say `a<=A`), evaluate that finite matrix jointly with the prime operator, and bound the omitted tail (`a>A`) separately by an absolute/constant-only estimate. v15.456 shows this specific strategy cannot work at the available margin: the diagonal block `1_{I_a}C1_{I_a}` at *every* annulus `a`, tested against nothing fancier than the uniform constant vector on that annulus, has quadratic form exceeding `1/8` — a fixed floor that does not shrink as `a→∞`. Since `1/8` dwarfs the certified near-joint margin (`≈0.000102`) by three orders of magnitude, no finite-`A` truncation followed by an independent (absolute-value) tail charge can close the gap, no matter how large `A` is taken.

## Independent re-derivation of the Rayleigh-quotient bound

**Setup.** With `I_a={(2^a-1)N,...,(2^{a+1}-1)N-1}`, `L_a=2^aN`, `A_a=(2^{a+1}-1)N` (the annulus's upper endpoint), and writing `j=(2^a-1)N+r`, `k=(2^a-1)N+s` for `r,s∈[0,L_a)`: `j+k=2(2^a-1)N+r+s`, so `N+j+k=(2^{a+1}-1)N+r+s=A_a+r+s`, confirmed by direct substitution — matching the ledger's claimed `C(j,k)=1/[2(A_a+r+s)]`.

**Uniform denominator bound.** Since `0<=r,s<L_a`, `r+s<2L_a` strictly, so every denominator `2(A_a+r+s)<2(A_a+2L_a)=2[(2^{a+1}-1)N+2·2^aN]=2(2^{a+2}-1)N`, confirmed by direct algebra.

**The quadratic form on the constant vector.** `<u_a,1_{I_a}C1_{I_a}u_a>=(1/L_a)sum_{r,s}1/[2(A_a+r+s)]`, and since every one of the `L_a^2` terms in that sum is strictly larger than `1/[2(2^{a+2}-1)N]`, the sum exceeds `L_a^2/[2(2^{a+2}-1)N]`, and dividing by `L_a` gives `>L_a/[2(2^{a+2}-1)N]=2^a/[2(2^{a+2}-1)]` (using `L_a=2^aN`) — confirmed.

**The exact `1/8` identity.** Algebraically, `2^a/[2(2^{a+2}-1)]=1/8+1/[8(2^{a+2}-1)]`: checking, `1/8+1/[8(2^{a+2}-1)]=[(2^{a+2}-1)+1]/[8(2^{a+2}-1)]=2^{a+2}/[8(2^{a+2}-1)]=(4·2^a)/[8(2^{a+2}-1)]=2^a/[2(2^{a+2}-1)]` — exact, confirmed by hand, and this identity is the core of why the bound never decays below `1/8`: the correction term `1/[8(2^{a+2}-1)]` is strictly positive for every `a>=0` but shrinks to `0` only in the limit, so the floor `1/8` is approached but never crossed.

## Independent numerical confirmation on actual finite blocks

Analytic algebra alone can hide sign errors, so I built the *actual* finite diagonal blocks directly (not a sampled corner — full blocks, feasible at a small physical scale `N=50`) for annulus indices `a=0,...,5`, computed the true quadratic form `<u_a,1_{I_a}C1_{I_a}u_a>` on the exact normalized constant vector, and compared to the claimed lower bound `2^a/[2(2^{a+2}-1)]`: in every case the true value (`0.264529, 0.206582, 0.186409, 0.177763, 0.173740, 0.171798` for `a=0..5`) exceeded the predicted lower bound (`0.166667, 0.142857, 0.133333, 0.129032, 0.126984, 0.125984`), with the predicted values visibly converging toward `0.125=1/8` from above as `a` grows — exactly the behavior the analytic derivation predicts.

## Hash and execution verification

Witness `lane_a_v15_456_annulus_truncation_barrier_certificate.py` (commit `5573c93`, blob `6873788`, SHA-256 `a723804e...`) and manifest `lane_a_v15_456_annulus_truncation_barrier_certificate.sha256` (commit `0e23444`, blob `4d730f6`, SHA-256 `c97d2e6d...`) both verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger exactly, including `signed_joint_gate_status=UNEVALUATED`.

## One cosmetic note on the printed ratio (not a defect)

The ledger prose states the barrier exceeds the margin "by a factor greater than 1223.547114152761," copied verbatim from the witness's printed `barrier_to_margin_ratio_lower`. That print statement computes the ratio via Python's `float()` (double precision) rather than exact `Fraction` arithmetic, so it carries ordinary float-rounding noise in its last couple of digits. I recomputed the same ratio with exact `Fraction`/90-digit `Decimal` arithmetic and got `1223.54711415276066400...` — agreeing with the printed value to 11 significant digits, diverging only in the 12th (a relative difference of about `3×10^{-12}`). This is immaterial: the actual *asserted* claim in the witness is only the coarse, exact comparison `1/8 > NEAR_JOINT_MARGIN` (obviously true by three orders of magnitude), never the precise ratio figure, so nothing certified rests on this float-rounding noise. Noting it for completeness, per standing practice of reporting even small observations, not as a correction.

## Scope and honesty assessment

Correctly and carefully scoped: the entry is explicit that this "does not lower-bound or fail the signed joint tail `R_A(P+C_near(22))R_A`" since "the prime part may cancel the constant part," and that it rules out only the specific *absolute/triangle-charge-after-truncation* strategy, not the broader joint question. It correctly redirects toward either a scale-fiber/limit-operator representation or a genuine signed joint-tail estimate — consistent with the lesson already established in Rounds 494 and 496 about preserving signed cancellation.

## Summary

Confirmed. The Rayleigh-quotient lower bound, its exact algebraic decomposition, and the resulting `1/8`-floor-never-decaying conclusion are independently re-derived from scratch and confirmed on genuine (non-sampled) finite test blocks. One cosmetic float-rounding note on a purely descriptive (non-asserted) printed ratio, immaterial to the certified claim. This is a well-scoped negative result about one truncation strategy, correctly distinguished from the still-open signed joint question.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-497
parent: v15.457
status: closed
action: none — v15.456's Rayleigh-quotient bound and exact algebra are correct and independently re-derived, including a direct numerical check on full (non-sampled) finite blocks. The float-rounding note on the printed ratio is purely cosmetic. No correction needed.
deliverable: independent confirmation that no finite-annulus truncation of the constant-Hankel near-band, followed by an absolute tail charge, can close the available margin — while the signed joint question with the prime operator remains genuinely open.
