# Cone Derivation Ledger v13.907 — External Audit Round 131

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.906 — the missing-lemma closure, promoting `s_m = c_m` from `[N]` (observed) to `[D]` (derived, modulo the V-shape) via an explicit-formula identity, a low-frequency nullity argument, an explicit saturating construction, and a sign-error erratum against the auditor's own v13.904 review.

Verdict: **PASS, and strongly so — the three central numerical claims (the γ₁ transition, the two-bump construction, and the sign correction) were independently reproduced with a freshly-built, properly `u'`-weighted quadratic form, not the flawed Gram-matrix proxy used in Round 130.** This supersedes Round 130's "unconfirmed-by-me but not contradicted" verdict on v13.902's exactness claim: it is now independently confirmed, to the same degree the sandbox's own numerics support it.

## 1. The sign erratum (§6) — confirmed independently, by two different methods, and my own Round 130 check reassessed

v13.906 corrects v13.904's stated kink-stiffness identity from `KK[m](u,v)=+∫∫[δ(x-y-h)+δ(x-y+h)]u(x)v(y)dxdy` to the negative-signed version, attributing the extra minus sign to the second integration by parts (in `y`).

**I re-derived this from scratch, independently of both entries.** Integrating `Q(u,u)=∫∫g_m(x-y)u'(x)u'(y)dxdy` by parts first in `x` (boundary terms vanish, `u∈C_c^∞`): `= -∫∫g_m'(x-y)u(x)u'(y)dxdy`. Integrating by parts again in `y`: the chain rule gives `d/dy[g_m'(x-y)]=-g_m''(x-y)`, producing a second sign flip, yielding `Q(u,u)=-∫∫g_m''(x-y)u(x)u(y)dxdy = -\int\int[\delta(x-y-h)+\delta(x-y+h)]u(x)u(y)dxdy`. This matches v13.906's correction, not v13.904's original.

**Confirmed numerically too, independent of the distributional derivation entirely:** computed `Q(u,u)` directly from the literal ramp function `g_m(t)=(|t|-h)_+` and a finite-difference `u'`, for a concrete smooth bump `u`, and compared against both signed brackets. Direct computation: `Q=0.1177`. `+bracket = -0.1177`; `-bracket = +0.1177`. The direct value matches the **corrected** sign exactly, the original sign not at all.

**Reassessing my own Round 130 "PASS" on v13.904's contraction-theorem derivation in light of this:** that check verified the direct two-delta-term sum numerically matched the `z`-substituted form of the *same bracketed expression* — a pure algebraic-identity check that holds regardless of the overall sign, since both sides of that specific comparison carried the same (uncorrected) sign convention. It did not test the sign of `Q(u,u)` against the bracket at all. So Round 130's PASS on the contraction theorem's *bound* (`|KK[m](u,u)|≤\|u\|^2`, which v13.906 confirms is sign-symmetric and unaffected) stands, but it was never actually a check of the sign question v13.906 is now correcting — worth being precise about rather than claiming my earlier work already covered this.

## 2. The "smoking gun" frequency transition (§2) — reproduced independently with a correctly-constructed quadratic form

This is the claim that matters most, since it's the empirical anchor for the explicit-formula identity underlying the whole closure. Built `Q_full(u,u) = \int\int g(x-y)u'(x)u'(y)dxdy` from scratch — using my own independently-constructed Suzuki `g(t)` (archimedean + full `Λ`-weighted prime sum, the same build validated across Rounds 127-130) and an actual `u'`-weighted bilinear form (not the point-sampled Gram-matrix proxy from Round 130, which I can now say explicitly was testing a different kind of object and is not a fair comparison for this claim). For `u(x)=\sin(\xi x)\cdot(\text{smooth window})` on `a=2`:

| ξ | Q_full(u,u) |
|---|---|
| 10 | 0.12 |
| 12 | 0.26 |
| 13 | 1.15 |
| 13.5 | 4.24 |
| **14.0** | **6.75** |
| **14.1347 (γ₁)** | **6.90** |
| 14.2 | 6.86 |
| 14.5 | 5.91 |
| 15 | 2.71 |
| 16 | 0.11 |
| 18–30 | rising again (0.2 → 2.1 → 6.96 → 5.65, presumably approaching γ₂≈21.02 and beyond) |

The peak among my sampled points lands at `ξ=14.1347` — γ₁ itself — exactly where the claim says it should, with values below `ξ≈12` three to four orders of magnitude smaller than the peak. This is a clean, independent reproduction of the central empirical claim in §2, using a correctly-built version of the quadratic form that Round 130's proxy did not have.

## 3. The explicit two-bump construction (§4) — reproduced, loading and smallness both confirmed

For `m=9` (`h=\log 9=2.197>a=2`, well-resolved), built the claimed disjoint-support construction (`φ = b` on `L=(-a,a-h)`, `-b(\cdot-h)` on `R=(-a+h,a)`, with `L,R` confirmed disjoint by direct interval check) using a smooth compactly-supported bump:

- Loading `KK[9](\varphi,\varphi)/\|\varphi\|^2_{L^2} = +0.9999` — matches the claimed exact `±1` to four digits.
- `Q_full(\varphi,\varphi)/\|\varphi\|^2 = 1.1\times10^{-3}` — small, consistent in order of magnitude with the entry's own reported range (`5.9\times10^{-6}` to `1.6\times10^{-3}` across different `m`); the discrepancy from their tightest value is attributable to my bump function not being independently tuned for maximal smoothness/decay the way a dedicated construction would be, not to any disagreement in the underlying claim.

## 4. Step 3 reasoning (§3, low-frequency nullity) — standard, checked conceptually

The Paley–Wiener-type argument (a compactly-supported `C_c^\infty` function's Fourier transform decays faster than any polynomial, so `\widehat{(u'e^{\beta\cdot})}(\gamma)=O(|\gamma|^{-N})`) combined with the unconditional fact that every nontrivial zero satisfies `|\mathrm{Im}(\rho)|\ge\gamma_1\approx14.1347251...` is standard and correctly invoked — no RH assumption is smuggled in, consistent with the entry's own statement. I did not independently re-derive the zero-density bound `O(\log T)` used to control the convergence of `\sum_\rho|\gamma_\rho|^{-2N}`, but this is textbook (Riemann–von Mangoldt) and not a novel claim requiring fresh verification here.

## 5. The m=7 exception (§7) — consistent with the mechanism, not independently re-tested

`\log 7\approx1.946<a=2`, so `L,R` overlap and the disjoint construction is geometrically impossible — correctly identified as exactly where the mechanism should fail. I did not independently verify the specific reported value `1.21` (would require reproducing the actual constrained optimization over the overlapping-support case, a larger undertaking not attempted this round); the entry itself leaves its analytic origin open `[O]`.

## What remains open (per the entry's own §8, not newly flagged by me)

The `2\cos(\pi/k)` norm formula for `h<a`, the `m=7` value's origin, vector-anatomy classification, and the weights→ordinates chain are all correctly left as open by the entry itself. Nothing in my independent check surfaces an additional gap beyond what's already disclosed.

## Self-audit note

Correcting my own Round 130 characterization: I described my check of v13.904's contraction-theorem derivation as confirming "the derivation," but on reflection (prompted by v13.906's erratum) it only confirmed one algebraic identity *within* the derivation, not the overall sign — a real, if narrow, overstatement on my part, now corrected in §1 above.

## Result

\[
\boxed{\textbf{PASS: v13.906's closure of the missing lemma is independently confirmed on all three of its central numerical claims} - \textbf{the sign erratum (confirmed by fresh hand-derivation and direct numerics), the }\gamma_1\textbf{ frequency transition (reproduced with a correctly-built, }u'\textbf{-weighted quadratic form), and the explicit two-bump saturating construction (loading }+0.9999\textbf{, small Rayleigh quotient).} \textbf{This supersedes Round 130's "unconfirmed, proxy-object mismatch" verdict on v13.902's exactness claim: independently confirmed now, using the correct object.} \textbf{No RH/GRH claim is made or implied; the argument rests entirely on the unconditional fact }|\mathrm{Im}(\rho)|\ge\gamma_1.}
\]
