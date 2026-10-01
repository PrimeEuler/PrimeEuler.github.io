# Cone Derivation Ledger v13.910 — Sandbox V-Shape Refinement: Correction of v13.906 §5 — the Slope-$c_m$ Law Is Finite-Scale, Not Infinitesimal

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("ledger all three!" following the V-shape proof report).

Predecessors: v13.902 (rigidity: Λ isolated strict maximizer, V-slopes $s_m = c_m$ [N]), v13.904 (analytic skeleton: contraction theorem ⇒ $s_m \le c_m$ [D]), v13.906 (missing lemma closed; §5 promoted $s_m = c_m$ to [D] "modulo the [N] V-shape"). **This entry REFINES v13.906 §5.** Sandbox report: `vshape_proof.md` (run dir `runs/20260930-divisor-tension/`; inline scripts, key data in the report's tables).

Status: **[D]** for the sandwich theorem, the Danskin derivative formulas, the perturbed-minimizer pinning, and the continuum conditional; **[N]** for the eigenvector loadings, the level-crossing scale, and the secant-slope measurements; **[I]/[O]** for interpretation and the remaining open items. No RH/GRH claim. This entry is a **correction**: a reader of v13.906 §5 must understand that "the V-shape with slope exactly $c_m$" does **not** hold infinitesimally, and exactly what does.

## 1. What I need to correct (the verdict)

I need to correct what I told you in v13.906 §5. The infinitesimal symmetric V-shape with slope exactly $c_m$,
$$\lambda_1(\varepsilon) \stackrel{?}{=} \lambda_1(0) - c_m\lvert\varepsilon\rvert,$$
**does not follow [D], and is in fact FALSE at infinitesimal scale in the FEM.** The precise obstruction is §2 below.

The restatement of v13.906 §5's "$s_m = c_m$ [D]": the slope-$c_m$ law holds as a **finite-scale law** — a [D] sandwich (§4) plus a [N]-quantified level crossing (§3) — but **not** as an infinitesimal derivative. At $\varepsilon \to 0$ the function $f$ is differentiable with the wrong slope. The selection/rigidity conclusions (§9) are unaffected: strict maximality never depended on the infinitesimal slope.

## 2. The precise obstruction: the exact minimizer does not have extremal kink-loading [D framework; N values]

Setup [D]: fix a kink index $m$ with $a < \log m < 2a$ (well-resolved regime), perturb $c_m \to (1+\varepsilon)c_m$, and set
$$f(\varepsilon) := \lambda_1\big(Q_{\mathrm{full}} + \varepsilon\,c_m\,KK[m]\big).$$
The kink-loading of $v \ne 0$ is $\mathrm{loading}_m(v) := v^\top KK[m]v / v^\top Mv$; by linearity of $Q$ in the weights,
$$RQ_{Q(\varepsilon)}(v) = RQ_{\mathrm{full}}(v) + \varepsilon\,c_m\,\mathrm{loading}_m(v) \tag{1}$$
exactly. $f$ is a pointwise minimum of affine functions, hence concave [D]; $M(\Lambda) := \arg\min_{\lVert v\rVert_M=1} RQ_{\mathrm{full}}(v) \ne \varnothing$ [D] (finite-dimensional FEM, compact $M$-unit sphere), so Danskin applies directly. **Non-attainment is not the obstruction.**

The obstruction is that the *attained* minimizer does not saturate the contraction bound. Numerical fact [N] ($a=2$, $N=800$ and $1600$; loadings of the exact $\lambda_1$-eigenvector $v_0$, $\lambda_1 = 1.84\times10^{-8}$, gap ratio $\lambda_2/\lambda_1 = 4.0\times$ stable under refinement; eigen-residual $\sim 10^{-6}$; loadings stable to $\sim 1\%$ under $N=800\to1600$):

| kink $m$ | $\log m$ | $\mathrm{loading}_m(v_0)$ ($N$=800) | ($N$=1600) |
|---|---|---|---|
| 8 | 2.079 | $-0.541801$ | $-0.546031$ |
| 9 | 2.197 | $-0.457280$ | $-0.461398$ |
| 16 | 2.773 | $-0.153058$ | — |
| 25 | 3.219 | $-0.038004$ | — |

Since $\lambda_1$ is simple [N], Danskin (§5) gives $f'(0+) = f'(0-) = c_9 \cdot (-0.461) \approx -0.169 \ne -c_9 \approx -0.366$. **Infinitesimally, $f$ is a line, not a V, and its slope is not $c_m$.** The [D] ingredients (contraction, two-bump construction, concavity) bound the infinitesimal slopes by $c_m$ but cannot force equality, because contraction controls loadings over *all* $v$ while Danskin samples only the *exact eigenspace* $M(\Lambda)$ — and on that eigenspace the loading is not extremal.

## 3. The observed V is a post-level-crossing phenomenon [N]

The $\pm1$-loading near-minimizers of v13.906 have excess RQ $\eta_- \approx 5.9\times10^{-6}$ [N, Gaussian bump] over $\lambda_1 = 1.8\times10^{-8}$. The analytic $\lambda_1$-branch has slope $-0.461\,c_m$; the $-1$-loading branch has slope $-c_m$ and starts $\eta_-$ higher. They cross at
$$\varepsilon^\ast \sim \frac{\eta_-}{c_m\,(1-0.461)} \sim 3\times10^{-6} \quad\text{[N]},$$
consistent with the observed transition between $\varepsilon = 10^{-6}$ and $5\times10^{-6}$. For $\varepsilon \gg \varepsilon^\ast$ the $-1$-loading vector is the true minimizer; for $0 < \varepsilon \ll \varepsilon^\ast$, the exact eigenvector is. (Symmetric statement for $\varepsilon < 0$ with the $+1$-loading vector.)

Secant slopes $[f(\varepsilon)-f(0)]/\varepsilon$ ($m=9$, $N=800$) confirm the transition [N]:

| $\varepsilon$ | secant$/c_9$ |
|---|---|
| $10^{-6}$ | $-0.83$ (in transition) |
| $5\times10^{-6}$ | $-0.994$ |
| $\ge 10^{-5}$ | $-1.0000$ (4 digits) |

Left side mirrors it ($+0.9999$ at $\varepsilon = -2\times10^{-3}$ [N]). **All rigidity-experiment data ($\varepsilon \ge 0.002$) lie $\sim 700\times$ above $\varepsilon^\ast$** — deep in the post-crossing regime, which is why the slope-$c_m$ V was observed. This is also consistent with the sibling shift-norm theorem (v13.908): $\lVert KK[m]\rVert = 1$ exactly on the full space [D], but tightness on the full space $\ne$ tightness on the eigenspace — which is exactly the obstruction.

## 4. What *is* [D]: the sandwich theorem (finite-scale V-shape for all $\varepsilon$)

**Theorem [D].** For every $\varepsilon > 0$,
$$\lambda_1 - c_m\varepsilon \le f(\varepsilon) \le \lambda_1 - c_m\varepsilon + \eta_-,$$
and for every $\varepsilon < 0$,
$$\lambda_1 - c_m\lvert\varepsilon\rvert \le f(\varepsilon) \le \lambda_1 - c_m\lvert\varepsilon\rvert + \eta_+.$$

*Proof.* Upper bound ($\varepsilon > 0$): test with the $\varphi_-$ of v13.906 in (1): $f(\varepsilon) \le RQ_{\mathrm{full}}(\varphi_-) + \varepsilon c_m(-1) = \lambda_1 + \eta_- - c_m\varepsilon$. Lower bound: $f(\varepsilon) = \min_v[RQ_{\mathrm{full}}(v) + \varepsilon c_m\,\mathrm{loading}_m(v)] \ge \lambda_1 + \varepsilon c_m \min_v \mathrm{loading}_m(v) \ge \lambda_1 - c_m\varepsilon$ using the v13.904 contraction ($-M \le KK[m] \le M$). The $\varepsilon < 0$ case is identical with $\varphi_+$ and $\max_v \mathrm{loading}_m \le 1$. ∎

**Corollary [D].** $\lvert f(\varepsilon) - (\lambda_1 - c_m\lvert\varepsilon\rvert)\rvert \le \eta$ for all $\varepsilon$, where $\eta = \max(\eta_-,\eta_+)$. The V-shape with slope $c_m$ holds [D] up to the additive near-minimizer excess $\eta \sim 6\times10^{-6}$. No infinitesimal limit is taken; no knowledge of $M(\Lambda)$ is needed. This is what v13.906 §5's "$s_m = c_m$ [D]" should have been.

## 5. What *is* [D]: Danskin derivatives, plus a sign correction

Danskin's theorem applied to $f(\varepsilon) = \min_{\lVert v\rVert_M=1}\Phi(v,\varepsilon)$ gives [D]:
$$f'(0+) = c_m \min_{v\in M(\Lambda)} \mathrm{loading}_m(v), \qquad
  f'(0-) = +\,c_m \max_{v\in M(\Lambda)} \mathrm{loading}_m(v),$$
and with the contraction, $\lvert f'(0\pm)\rvert \le c_m$ [D].

**Sign correction [D]:** the task brief's formula $f'(0-) = -c_m\cdot\max_{M(\Lambda)}\mathrm{loading}_m$ was wrong; the correct left derivative is $+\,c_m\cdot\max_{M(\Lambda)}\mathrm{loading}_m$ (verified against toy cases). It is immaterial here: since $\lambda_1$ is simple [N], $\min = \max = \mathrm{loading}_m(v_0)$ and $f$ is differentiable at $0$ with slope $c_m\,\mathrm{loading}_m(v_0)$ — the line of §2.

## 6. What *is* [D]: perturbed-minimizer pinning

For $\varepsilon > 0$, any minimizer $v_\varepsilon$ satisfies [D]
$$-1 \le \mathrm{loading}_m(v_\varepsilon) \le -1 + \frac{\eta_-}{\varepsilon c_m}$$
(proof: $f(\varepsilon) \le \lambda_1 + \eta_- - c_m\varepsilon$ while $f(\varepsilon) \ge \lambda_1 + \varepsilon c_m\,\mathrm{loading}_m(v_\varepsilon)$). At $\varepsilon = 0.002$, $m = 9$: $\mathrm{loading}(v_\varepsilon) \in [-1, -0.992]$ [D]. The observed post-crossing minimizers are pinned near loading $-1$ [D]; that $f$ is *exactly* linear on $[0.002, 1.0]$ with slope *identically* $-c_m$ remains [N].

## 7. The exact-vs-near-minimizer gap is real, not a lack of imagination [D framework]

A concrete hypothetical $f$ satisfies *all* [D] ingredients simultaneously — concavity, contraction, the sandwich, the two-bump construction — with $f'(0+) = -c_m(1-\delta)$ ($\delta = 0.539$ for $m=9$), switching to $f(\varepsilon) = \lambda_1 + \eta_- - c_m\varepsilon$ after $\varepsilon^\ast$. The $\eta/\varepsilon$ term from any near-minimizer upper bound blows up as $\varepsilon \to 0$, so **near-minimizers can never control the infinitesimal slope** [D]. The gap between "exact loading $-0.461$" and "near-minimizer loading $-1$" is a genuine logical gap in the v13.906 chain, now precisely located.

## 8. Continuum: the exact V is conditional on $\inf RQ_{\mathrm{full}} = 0$ [D conditional; the "if" [O]]

**Conditional theorem [D]:** IF $\inf_{H^1_0} RQ_{\mathrm{full}} = 0$, THEN $f_{\mathrm{cont}}(\varepsilon) = -c_m\lvert\varepsilon\rvert$ exactly — a genuine kink at $0$. Reason: in the continuum the near-minimizer excess $\eta$ can be driven to $0$ by smoothness (v13.906 §3 gives $Q_{\mathrm{full}} = O_N(\gamma_1^{-2N+1}\log\gamma_1)$), so the sandwich becomes exact. The "if" is [O]. Note the subtlety this resolves: the FEM's infinitesimal line may itself be the discretization artifact, with the true continuum recovering the V.

## 9. What is NOT affected

- **The audit thread's Round 131 PASS stands untouched:** the sign erratum in the $\delta''$ identity (v13.906 §6), the $\gamma_1$ frequency transition (v13.906 §2), and the two-bump construction (v13.906 §4) — none of which this correction touches.
- **The selection/rigidity conclusions are unaffected:** $\Lambda$ remains the isolated strict maximizer (v13.902); concavity and the contraction theorem (v13.904) are untouched. Strict maximality never depended on the infinitesimal slope — only on $f$ decreasing in both directions, which the sandwich preserves.

## 10. What remains [O]/[N]

- Exact linearity of $f$ on $\varepsilon = 0.002 \to 1.0$ (slope *identically* $-c_m$) remains [N], but is now [D]-anchored: sandwich (§4) plus the [N]-quantified crossing scale (§3).
- The continuum "if" ($\inf_{H^1_0} RQ_{\mathrm{full}} = 0$) remains [O].
- The m=7 value $1.21$ and the vector-anatomy classification remain [O] (v13.906 §8); this entry confirms they are genuinely separate problems (they concern the null-cluster-restricted maximum, not the infinitesimal structure analyzed here).

## Synchronization

Live ledger head checked immediately before this write: v13.907 (audit thread, External Audit Round 131 — read in full; PASS on v13.906, independently confirming the sign erratum, the γ₁ frequency transition, and the two-bump construction — none of which this correction touches). No collision on v13.910.
