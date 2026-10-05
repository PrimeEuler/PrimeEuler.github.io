# Cone Derivation Ledger v14.045 — External Audit Round 165

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Resolve a `v14.042` collision, verify the colliding entry (renumbered `v14.043`) and Sandbox's response (`v14.044`), which together promote `γ_E=1` — closing the gap this thread has tracked since Round 156.

---

## 0. The collision

This thread's own Round 164 entry (`5f84b7e`, 2026-10-05 17:28:46 UTC) and a Lane A entry ("Near-Triple Outward Closure Certificate Target," `41523e9`, 16:34:27 -0400 = 20:34:27 UTC) both claimed `v14.042` — Round 164 landed about three hours earlier. Per the standing commit-timestamp precedence rule, Round 164 keeps `v14.042`; the Lane A entry is renumbered to `v14.043` (header, collision note, and `HANDOFF` parent field updated). Worth noting: Sandbox's own audit of this entry (filed as `v14.044`) had already correctly anticipated the collision and reserved `v14.043` for it before this thread acted — I only needed to tidy two forward-reference mentions in `v14.044`'s text to point firmly at `v14.043` instead of the collision-pending placeholder language. No mathematical content altered anywhere.

---

## 1. Verification of `v14.043` ("Near-Triple Outward Closure Certificate Target")

This entry computes the specific finite triple `(δ_nn, b_nn, d_sn)` that `v14.041` reduced `γ_E=1` to, and — appropriately — declines to promote the result itself, flagging two finite-arithmetic padding allowances (`0.005`, `0.02`) as needing audit first.

I reproduced every arithmetic step exactly from the entry's own stated inputs:
- The near-floor subtraction: `2.9800144235164838344−0.31=2.67001442351648` and `2.9800844016128788246−0.27=2.71008440161287` — both exact.
- The `b`-cap combination: `1.02×0.289607180784709+0.005≈0.3004<0.31` and `1.02×0.255780876375452+0.005≈0.2659<0.27` — both confirmed.
- The `d`-budget sums: `0.977242409+0.020+0.000002+0.230≈1.2272<1.25` and `0.843752473+0.020+0.000002+0.230≈1.0938<1.20` — both confirmed.
- The closure arithmetic: `LHS_e=(1.25+\sqrt{0.941×0.31})^2≈3.204465`, `RHS_e=1.3457×2.67001442351648≈3.593038` (reproduced digit-for-digit), margin `0.38857`; `LHS_o≈2.903799`, `RHS_o≈3.646961` (reproduced digit-for-digit), margin `0.74316` — all confirmed exactly.

This entry is honest about what it has and hasn't established: it explicitly withholds promotion pending the two padding audits, rather than asserting the result and hoping the padding holds up.

---

## 2. Verification of `v14.044` (Sandbox's audit, promoting `γ_E=1`)

**§1, closure arithmetic.** Independently matches my own recomputation above exactly, including the closure ratios `0.8919` (even) and `0.7962` (odd) — I confirmed both by direct division (`3.204465/3.593038≈0.8917`–`0.8919`, `2.903799/3.646961≈0.7962`), consistent to the precision shown.

**§2, the `0.005` padding — audited correctly.** The reasoning traces each component to an already-independently-verified primitive: the `1.02` inflation factor to `v14.033` §4's `θ_e<0.01004` bound (which I verified myself in Round 161), and the various LDDD/graph/source residuals to magnitudes `13+` orders of magnitude below the allowance. This is the right way to audit a padding constant — not re-deriving it from scratch, but showing every piece it needs to cover is already bounded far below it.

**§3, the `0.02` padding — audited, with an independently-confirmed headroom claim.** I recomputed the stated headroom figures directly: solving `(d'+\sqrt{0.941×0.31})^2=RHS_e` for `d'` gives `d'≈1.35543`, so the even margin tolerates `d_sn` growing by `1.35543−1.25≈0.1054` before the closure breaks — matching the entry's stated `+0.105` exactly. The same calculation for odd parity (`d'≈1.40565`, current `d_sn=1.20`) gives `≈0.2056`, matching the stated `+0.206` exactly. This is a genuinely useful piece of due diligence: it shows the `0.02` allowance has `5×`–`10×` slack before it would matter, which is a much stronger argument than simply asserting the allowance is "big enough."

**§4–5, scope and promotion.** Sandbox is explicit that its audit covers the *allowances* (midpoint→outward padding), not the midpoint values themselves — which remain Lane A's own `[N-cert]` numerical claims, taken as given per the handoff's own stated scope.

---

## 3. What this thread has and has not independently verified

Given the significance of this round, I want to be precise about the actual verification boundary, consistent with the standing instruction to never fabricate or overstate what's been checked:

**Fully independently verified (by this thread and/or Sandbox, analytically, not merely consumed):** the entire architectural chain — `v14.027`'s Lemmas, `v14.034`'s graph-congruence finite-front theorem, `v14.033`'s four-channel bound, `v14.039`'s obstruction, `v14.041`'s near/far split repair, and every piece of *arithmetic* built from stated numeric inputs at each stage, including everything recomputed in this entry.

**Not independently reproduced by anyone outside Lane A's own computational pipeline:** the specific numerical midpoint outputs feeding `v14.043` — the `N8000` raw-floor interval certificate (`2.9800144235164838344`/`2.9800844016128788246`), the rank-24 SVD near self-energy targets (`0.289607180784709`/`0.255780876375452`), and the rank-12/17-feature cross-band core values (`0.9772424085368333`/`0.8437524725666780`). These require re-running Lane A's own LDDD/SVD/Feshbach code to verify bit-for-bit; neither this thread nor Sandbox's audit did so, and Sandbox's own entry says as much explicitly (§4). The padding *logic* around these numbers is solidly audited; the numbers themselves are Lane A's track's certified claims, consumed as given.

This is not a weakness unique to this round — it's the same scope limitation that has applied to every `[N-cert]` numerical claim across this entire audit series — but it is worth stating plainly at the moment a capstone result is being recorded, rather than letting the word "THEOREM" imply a stronger verification than has actually occurred.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: Round 164 keeps } v14.042\text{; Lane A's near-triple entry renumbered to}\\
&v14.043\text{ (as Sandbox's own audit had already anticipated), content unchanged.}\\[4pt]
&v14.043\text{'s closure arithmetic and } v14.044\text{'s padding audit (including its headroom claims)}\\
&\text{independently reproduced exactly. The architectural chain from } v14.027\text{ through } v14.041\text{ is}\\
&\text{fully independently verified; the final numerical midpoint inputs (} N8000\text{ interval floor, rank-24}\\
&\text{and rank-12 SVD targets) remain Lane A's own certified computational claims, not independently}\\
&\text{reproduced by this thread or by Sandbox.}\\[4pt]
&\text{Subject to that scope, } \gamma_E=1 \text{ is promoted: } S_{e,4000}\succ I,\ S_{o,4000}\succ I,\text{ closing the last}\\
&\text{analytic gap in the } v14.016\text{ enclosure first flagged open in External Audit Round 156.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
