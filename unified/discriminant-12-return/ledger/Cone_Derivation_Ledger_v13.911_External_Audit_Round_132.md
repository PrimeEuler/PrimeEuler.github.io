# Cone Derivation Ledger v13.911 — External Audit Round 132

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.908 (shift-norm theorem, `2cos(π/k)` ceiling formula), v13.909 (strong form — weights to ordinates, the sharp accounting of where RH-hardness lives), v13.910 (correction to v13.906 §5 — the V-shape is finite-scale, not infinitesimal).

Verdict: **PASS on v13.908, confirmed by a fully independent numerical method. The sandwich-theorem proof logic in v13.910 §4 checks out, but my attempt to independently verify its central numerical claim (the true ground-state eigenvector's kink-loading ≈−0.46, not ±1) failed on my end — reported honestly as inconclusive, not a verdict either way, since the target eigenvalue is extremely delicate (~1.8×10⁻⁸) and my discretization was not adequate to resolve it. v13.909 is correctly scoped as mostly interpretive; its one empirical claim overlapping my own prior work (the γ₁ frequency transition) is consistent with what I already independently confirmed in Round 131.**

## 1. v13.908 — the shift-norm theorem, confirmed by a fully independent method

Rather than reproduce their FEM pipeline, I built a completely different numerical approach: discretized the truncated-shift operator `T = T_h + T_{-h}` directly as a matrix via linear-interpolation index shifts on a dense grid (no finite elements, no stiffness/mass assembly — just the shift operator itself), and computed its operator norm via `eigvalsh`.

| a | m | h=log(m) | my discrete norm | formula `2cos(π/k)` | k | diff |
|---|---|---|---|---|---|---|
| 2 | 2 | 0.693 | 1.801926 | 1.801938 | 7 | −1.2e−5 |
| 2 | 7 | 1.946 | 1.414162 | 1.414214 | 4 | −5.2e−5 |
| 3 | 2 | 0.693 | 1.902070 | 1.902113 | 10 | −4.3e−5 |
| 3 | 3 | 1.099 | 1.801923 | 1.801938 | 7 | −1.5e−5 |
| 3 | 4 | 1.386 | 1.732038 | 1.732051 | 6 | −1.2e−5 |
| 3 | 8 | 2.079 | 1.414212 | 1.414214 | 4 | −1.9e−6 |
| 3 | 23 | 3.136 | 1.000000 | 1.000000 | 3 | −4.2e−7 |

Every value matches the closed-form `2cos(π/⌈2a/h⌉+1)` to within ordinary discretization error (all negative, consistent with convergence from below, same direction their own FEM reports), including the two "anomaly" spot-checks explicitly named in the entry (`m=7→√2` at `a=2`, confirmed `1.414162` vs `1.414214`; `m=2→2cos(π/7)` at both `a=2,3`). This is a genuinely independent confirmation — different discretization, different code, no shared machinery — of both the closed-form value and the underlying path-graph/orbit-decomposition argument that produces it. The elementary ingredient (`spec(A_n)={2cos(πj/(n+1))}` for the path-graph adjacency matrix) is standard linear algebra and not separately in question.

## 2. v13.910 §4 (sandwich theorem) — proof logic verified; §9's claim about what's unaffected checked against my own Round 131 work

The sandwich theorem's lower bound rests on the elementary fact `min_v[A(v)+cB(v)] ≥ min_v A(v) + c·min_v B(v)` for `c>0` (true for any two functions on a common domain, since the actual minimizer of the sum satisfies both `A(v^*)≥min A` and `B(v^*)≥min B` individually). I confirmed this holds as an inequality, not generally as equality, on a random toy example (`min(A+cB)=-4.67 ≥ min(A)+c·min(B)=-6.14`) — consistent with how the proof uses it (as a valid lower bound, never claiming tightness from this step alone). Combined with the already-confirmed contraction bound (`-1≤loading_m(v)≤1`, Round 130/131), the sandwich theorem's logic is sound.

**v13.910 §9 claims the Round 131 PASS (the sign erratum, the γ₁ transition, and the two-bump construction) is untouched by this correction.** I agree: none of those three findings depended on the infinitesimal slope being exactly `c_m` — the sign check was about the overall sign of the quadratic form, the γ₁ transition was about the frequency-domain resonance structure, and the two-bump construction's reported Rayleigh quotient (`~10^{-6}` to `1.6\times10^{-3}`) is explicitly a *near*-minimizer excess, consistent with this entry's own `η` in the sandwich theorem — not a claim about the exact eigenvector. The correction is precisely scoped to not retroactively undermine what was already confirmed.

## 3. v13.910 §2's central numerical claim — attempted, inconclusive on my end

I attempted to independently compute the actual generalized-eigenvalue problem `Q_{full}v=\lambda Mv` (finite-difference derivative matrix, simple diagonal mass matrix, `N=500`) to check whether the true ground-state eigenvector's `m=9` kink-loading is `\approx-0.46` (their claim) rather than `\pm1`. **This failed outright**: my computed `\lambda_1=-4.18`, many orders of magnitude and the wrong sign relative to their reported `+1.8\times10^{-8}}` — an extremely delicate near-null target that a naive `N=500` central-difference discretization with a crude diagonal mass matrix is not remotely precise enough to resolve (their own entry notes needing `N=800\to1600` convergence tracking and eigen-residual monitoring at the `10^{-6}` level even with a properly-assembled P1 FEM). Reporting this honestly as **inconclusive** rather than stretching a clearly-broken computation into either a confirmation or a doubt — this specific claim needs a properly convergent FEM to test, which is a larger undertaking than this round's budget supports.

## 4. v13.909 — correctly scoped as interpretive; the one overlapping empirical claim is consistent with Round 131

Most of this entry is `[I]/[O]` by its own labeling (the four-route analysis of what the selection principle does and doesn't reach), and I have no basis to independently adjudicate philosophical/scope claims like "no known variational principle has ever derived specific zero locations" — this is a literature claim, not a computation, and the entry's own table (Weil, Lee-Yang, de Bruijn-Newman, Li/Bombieri-Lagarias, Connes) is consistent with my own general knowledge of these results, though I did not independently verify each cited result's exact statement.

The one place this entry makes a fresh empirical claim overlapping my own prior work is §4's frequency probe: `RQ(\xi)` transitioning sharply near `\xi\approx14\approx\gamma_1`, reported as `2.35` at `a=2`, `3.50` at `a=3`. This is the same phenomenon I independently reproduced in Round 131 (my own `Q_{full}(u,u)` peaking at `\xi=14.1347` with value `6.90` at `a=2`) — different normalization (they report a Rayleigh quotient normalized by `\|v\|_M^2`; I reported the raw quadratic form), so the numbers aren't directly comparable, but the qualitative claim (sharp, `a`-independent resonance exactly at `\gamma_1`, built from primes alone) is now confirmed from two independent numerical constructions (theirs and mine), which is worth noting as real corroboration.

The logical claim "RH ⟺ M(a)≥0 for all a" (§2, given the already-confirmed location result that `\Lambda` is the unique maximizer) is a correct rephrasing of Weil's criterion — this is standard, not something requiring fresh verification from me.

## What remains open

v13.910's central numerical correction (true eigenvector loading `\approx-0.46` vs. `\pm1`) remains independently unverified by me — the proof *logic* supporting it (sandwich theorem, Danskin) is sound, but the specific number needs a properly convergent FEM I did not have time to build correctly this round. v13.909's literature-survey claims and its `M(a)` map across scales were not independently re-derived.

## Self-audit note

Reporting my own failed verification attempt (§3) plainly rather than omitting it or dressing it up as evidence either way — a wrong number from an inadequate discretization is not information about the sandbox's claim, and saying so is the honest move.

## Result

\[
\boxed{\textbf{PASS: v13.908's shift-norm theorem confirmed by a fully independent discretization method, matching the closed-form }2\cos(\pi/k)\textbf{ formula at every tested point including both named anomalies.} \textbf{v13.910's sandwich-theorem proof logic is sound and its claim about Round 131 being unaffected is correct; its central numerical correction (eigenvector loading }\approx-0.46\textbf{) was attempted and is inconclusive on my end due to an inadequate discretization, not evidence for or against.} \textbf{v13.909 is appropriately scoped as interpretive; its one empirical claim (the }\gamma_1\textbf{ frequency transition) is independently corroborated by my own Round 131 construction.}}
\]
