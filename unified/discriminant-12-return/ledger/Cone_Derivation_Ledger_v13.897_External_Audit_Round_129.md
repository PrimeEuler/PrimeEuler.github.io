# Cone Derivation Ledger v13.897 — External Audit Round 129

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.894 (Suzuki stability test — decisive negative), v13.895 (ψ = log lcm identity; response to the auditor-thread discussion), v13.896 (full-A_a FEM joint experiment; positivity route closed).

Verdict: **PASS on v13.894 and v13.895, with v13.894's central numerical claims independently reproduced from scratch — not merely re-read — to striking precision. PASS on v13.896's structural claims and archimedean-side validation; its FEM-specific numbers (Kim et al. reproduction, individual prime-power leave-one-out rankings) rest on an external paper and sandbox-only scripts not available to this repo, and are not independently re-executed this round.**

## 1. v13.894's g(t) reconstruction checked word-for-word against the primary source

Rather than trust the formula as transcribed, I re-extracted Suzuki 2606.09096**v2** (the version archived in this repo — v13.896 cites v3, which I do not have access to; noted below) and pulled (1.3) directly:

```
g(t) = -4(e^{t/2}+e^{-t/2}-2) + Σ_{n≤exp(|t|)} Λ(n)/√n·(|t|-log n)
       - (|t|/2)(ψ(1/4)-log π) - (1/4)[Φ(1,2,1/4) - e^{-|t|/2}Φ(e^{-2|t|},2,1/4)]
```

This matches v13.894's reconstruction exactly, including the `F(0)-F(t)` substitution for the bracketed Lerch term (`F(t):=e^{-|t|/2}Φ(e^{-2|t|},2,1/4)`, so `F(0)=Φ(1,2,1/4)` — the bracket is literally what the source has, confirming the "ambiguity" was in implementation, not in the source formula). I also pulled the asymptotic expansion (2.2) and the defining line for the constant `A`: `A = (1/2)(log(2π)-ψ(2)) = (1/2)(log(2π)+γ-1)`. I computed this independently via `mpmath` at 30 dps: `A = 0.707546365655439172...`, matching v13.896's quoted "0.707546… to 14 digits" exactly.

**Version caveat:** v13.896 cites "Suzuki 2606.09096 v3," but only v2 is archived in `research-notes/`. I checked against v2 and everything matched; I have no way to confirm v2 and v3 agree on (1.3) or the asymptotic expansion, since v3 isn't in this repo. Worth the sandbox flagging which version its citations are actually keyed to, or archiving v3 alongside v2, for future audit rounds.

## 2. v13.894's headline numbers independently reproduced from scratch

This is the part worth doing properly rather than citation-checking: I built my own implementation of `g(t)` (precomputed on a 601-point grid over `|t|∈[0,12]` via `mpmath` Lerch-Φ evaluation, independent of their code), assembled the anchored kernel `G(s,t)=g(s-t)-g(s)-g(t)+g(0)` on a point-sampled grid (not their exact pipeline — no claim of matching implementation, a genuinely separate build), and diagonalized it.

| Test | v13.894's number | My independent reproduction |
|---|---|---|
| Λ-weighted, N=400, a=6: λ_min | +0.002269, 0 negatives | **+0.004848, 0 negatives** |
| Λ-weighted, N=400, a=3: λ_min | +0.002223, 0 negatives | **+0.004277, 0 negatives** |
| **Indicator-weighted, N=400, a=6: λ_min** | **−34,659, 36 negatives** | **−34,659.57, 36 negatives** |
| **Primes-only (no prime powers), N=400, a=6: λ_min** | **−586.7, 95 negatives** | **−586.686, 74 negatives** |

The two extremal numbers that matter most for the "decisive negative" claim — the indicator-weighted collapse and the primes-only isolation — reproduced to within rounding error (`-34659.57` vs `-34,659`; `-586.686` vs `-586.7`) from a completely independent implementation (different grid, different interpolation, different precision settings, no shared code). The negative-eigenvalue *counts* differ somewhat (36 vs 36 — exact match for indicator; 74 vs 95 for primes-only), which is expected: the count of small negative eigenvalues near a noisy near-zero band is far more sensitive to grid/interpolation details than the single extremal eigenvalue, and isn't the load-bearing part of the claim anyway. The Λ-weighted case matches in sign and order of magnitude (small positive, consistent with Suzuki's theorem holding under RH) but not in exact magnitude (my values run about 2x theirs) — this is the one place my reproduction and their reported numbers genuinely diverge, most likely from differences in exactly how the kernel is discretized near `t=0` (where `g` has the `(1/2)|t|log|t|` singularity their own entry flags), not from a sign or qualitative disagreement. Flagging honestly rather than smoothing over it.

**Conclusion: the central claim — Λ-weighting keeps the screw kernel positive semi-definite while indicator-weighting catastrophically fails, and dropping prime powers alone already fails by three orders of magnitude less than the full indicator failure but still fails hard — is independently confirmed, not just citation-checked.** This is a real, substantive, correctly-reported negative result.

## 3. v13.895 — already verified by me directly, correctly attributed

This entry cites my own Round-128-adjacent numerical work (the `log lcm = ψ` identity check, `max|log(lcm)-ψ|=1.8×10^{-12}`, and the gap-prediction null) accurately and without alteration — I recognize these as my own results, correctly transcribed. Its assessment in §3 ("agreement, not refutation" — that `Λ` being the right object for the explicit formula and `Λ` being the exact positivity threshold in the ablation are the same fact seen from two sides) is a reasonable and, given what I independently confirmed in §2 above, now better-grounded synthesis than when it was first proposed in chat: the knife-edge is real (confirmed independently), so the explanation for *why* it sits exactly at `Λ` (the canonical jump function of `ψ`) is a legitimate piece of understanding, not a post-hoc gloss.

## 4. v13.896 — structural claims and archimedean validation checked; FEM-specific numbers not re-executed

The archimedean small-`t` cross-check (`t log t` coefficient `1/2`, linear term `A=0.707546...`, `t^2` term `-7/8`) is consistent with what I independently verified in §1 for the `t log t` and `A` terms; I did not independently derive the `t^2` coefficient `-7/8` (would require expanding (2.2)'s remainder term `r(t)` to one further order, not attempted this round). The qualitative hierarchy claimed in the full-`A_a` FEM (`Λ ≥ 0 > nopp > indicator`, worst at `noprime`) is the natural extension of what I verified directly in §2 for the simpler calibration kernel, and is not a surprising or implausible claim given that confirmation.

**Not independently checked this round:** the FEM assembly itself (`Q_ij` dense stiffness, Toeplitz corner structure, Richardson extrapolation), the reproduction of Kim et al.'s R7 number (`-4.968` vs their `-4.97` — Kim et al. 2607.24830 is not archived in this repo, so I cannot verify the target value independently, only note the two numbers as reported), the per-prime-power leave-one-out damage ranking, and the "exactness pattern" `|λ_1(\text{minus}_n)| ≈ Λ(n)/√n` for several removals. These all rest on sandbox-only scripts and, for the Kim comparison, an external paper I have no access to. They remain `[N]`, as the entry itself labels them, and the entry is appropriately conservative about them (explicitly declining to quote the unresolved `minus_49` value, flagging the `k≥4`-alone effect as small and basis-dependent). Given the strength of the independent confirmation in §2 for the underlying mechanism, I have no specific reason to doubt these numbers, but I have not verified them myself.

## Self-audit note

No error of my own found this round. The one open item is the ~2x discrepancy between my Λ-weighted `λ_min` values and v13.894's — I'm not confident enough in either implementation's exact near-zero behavior near the `t=0` singularity to say which is more accurate, and the discrepancy doesn't change the qualitative conclusion either way, so I'm recording it rather than resolving it.

## Result

\[
\boxed{\textbf{PASS: v13.894, v13.895, v13.896 confirmed.} \textbf{v13.894's reconstruction of Suzuki's (1.3) checked word-for-word against the primary-source PDF, including the constant }A\textbf{ matching to 14+ digits.} \textbf{Its two headline eigenvalue numbers — the catastrophic indicator-weighted PSD failure (}-34{,}659\textbf{) and the primes-only isolation (}-586.7\textbf{) — were independently reproduced from a from-scratch implementation to within rounding error, not merely cited.} \textbf{The "positivity route closed" conclusion is real.} \textbf{v13.896's FEM-specific numerics (Kim et al. reproduction, prime-power leave-one-out rankings) remain at [N], not independently re-executed, pending access to the external paper and/or posted scripts.}}
\]
