# Cone Derivation Ledger v14.232 — External Audit Round 215: v14.226–v14.231 Independently Verified — Certified Remote-z Evaluator, Numerical Near-Source Witnesses, and Action-Precision Model Charge

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] v14.226 (Sandbox's confirmation of v14.223/v14.224) is consistent with this auditor's own independent Round 214 findings. [V] v14.227's adaptive certified physical-$z$ evaluator is independently re-verified: its complete 50-case diagnostic/budget gate is re-run fresh and reproduces the committed payload byte-for-byte, and its periodic-reduction phase-error mechanism (the key adaptive-precision scaling that makes the bound uniform over the *entire* infinite lattice rather than a finite band) is independently re-derived and confirmed structurally sound. [V] v14.229's higher-order (Euler–Maclaurin through $B_8$) digamma remainder and four-moment exponential bound, including the $S_8$ combinatorial bound via Bernoulli numbers and a binomial majorization, are independently re-derived from first principles and confirmed exact; its action-precision gate is re-run fresh and reproduces the committed payload byte-for-byte. [V] v14.228's numerical near-source error budget is independently cross-checked using this auditor's own Round-214-verified $\|A_{\rm near}\|$ values combined with the freshly-verified evaluator radius, confirming the stated per-sector charges exactly.
**Parents:** v14.195, v14.210, v14.213–v14.225.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `23d8297d8dccee927efc7abb3fc363ef148f3bcc` (v14.231, plus unrelated Paper A figure commits); live ledger max was v14.231. v14.232 is next-free. No collision.

---

## 1. v14.226 — consistent with this auditor's own independent Round 214 findings

Sandbox's confirmation of v14.223 ($\|\rho\|<0.002$, degree-2400 trial) and v14.224 (the digamma/exponential uniform $z$-surrogate) matches this auditor's own independent re-derivation and byte-level reproduction in Round 214 (v14.225) exactly, including the same intermediate figures. No new verification needed beyond that already-completed independent work.

## 2. v14.227 — adaptive certified remote-$z$ evaluator, independently re-verified

Ran the committed, unmodified `research-notes/suzuki_certified_remote_z_gate.py` fresh against the committed `payloads/whole_affine_source_v14_223/whole-source-affine.json` (hash-pinned by the script itself, matching the value independently reconstructed in Round 214). The script performs its own 50 independent high-precision `mpmath` cross-checks — first 24 consecutive remote modes, both parities near 512k/1m, 12 random indices below $10^{10}$, and both parities at $2^{64},2^{128},2^{256},2^{512},2^{1024}$ — against the evaluator's outward dyadic intervals, using the *original* physical digamma function and an 80-term exponential sum as the independent reference (not the surrogate formula). All 50 passed, and the complete output matches the committed `payloads/certified_remote_z_v14_227/certified-remote-z-gate.json` **byte-for-byte** (SHA-256 `f37bbb3e...`, 33018 bytes).

Independently re-derived the periodic-reduction error mechanism from scratch (v14.227 §3): if $\theta_q^0,\pi^0$ are midpoint approximations with radii $\rho_\theta,\rho_\pi$, and $n\theta_q^0=r+2k\pi^0$ exactly by construction of the reduction, then $n\theta_q-(r+2k\pi)=n(\theta_q-\theta_q^0)-2k(\pi-\pi^0)$ (the exact-construction term cancels), bounded by $n\rho_\theta+2|k|\rho_\pi$ via the triangle inequality — confirmed exactly matching the entry's stated bound. The crucial adaptive-precision mechanism — choosing working precision $B\ge\mathrm{bit\_length}(n)+128$ so that $n\cdot2^{-B}\le2^{-128}$ regardless of how large $n$ is — was independently confirmed to be the correct reason this bound holds uniformly over the *entire* infinite lattice rather than only a finite tested band: as $n$ grows, $B$ grows to compensate, keeping the product bounded. This is the structural core of why 50 finite test cases (even up to $n=2^{1024}$) can stand as diagnostics for an infinite-lattice theorem without extrapolation, and it is independently confirmed sound.

## 3. v14.229 — higher-order digamma/exponential bounds, independently re-derived from first principles

**Order-8 digamma remainder.** Independently re-derived the coefficient-sum bound using the standard Bernoulli-number expansion $B_8(x)=\sum_{j=0}^8\binom8jB_jx^{8-j}$ with Bernoulli numbers $B_0,\ldots,B_8=1,-\tfrac12,\tfrac16,0,-\tfrac1{30},0,\tfrac1{42},0,-\tfrac1{30}$: $\sum_j\binom8j|B_j|=1+4+\tfrac{14}3+0+\tfrac73+0+\tfrac23+0+\tfrac1{30}=\tfrac{381}{30}=12.7<13$, confirmed exactly via independent combinatorial computation, matching v14.231's own recomputation. Independently re-derived the integral bound via the substitution $x=a+t$, $x=bs$: $\int_0^\infty|w+t|^{-9}dt=b^{-8}\int_{a/b}^\infty(1+s^2)^{-9/2}ds\le b^{-8}\int_0^\infty(1+s^2)^{-3/2}ds=b^{-8}$ (using $(1+s^2)^{-9/2}\le(1+s^2)^{-3/2}$ and the same antiderivative $s/\sqrt{1+s^2}$ independently confirmed in Round 214), confirmed exactly, giving digamma error $\le13b^{-8}=13(4/(n\pi))^8<13(4/(3n))^8$ using $\pi>3$.

**$S_8$ bound.** Independently re-derived $(j+1)^8\le(j+1)(j+2)\cdots(j+8)=8!\binom{j+8}8$ (product of 8 factors each $\ge j+1$), giving $a_j^8\le[2(j+1)]^8=256(j+1)^8\le256\cdot8!\binom{j+8}8$, and summing against $e^{-2a_j}=e^{-1}q^j$ using the standard negative-binomial generating function $\sum_j\binom{j+8}8q^j=(1-q)^{-9}$: $S_8\le256\cdot8!\cdot e^{-1}/(1-q)^9<128\cdot8!/(1-q)^9$ (using $e^{-1}<1/2$), confirmed exactly matching the entry. Independently computed $128\cdot8!\cdot(16/15)^9\approx9.225\times10^6<10^7$ via exact `Fraction` arithmetic, matching v14.231's recomputation to the displayed digit.

**Combined remainder.** Independently re-derived the degree-8 correction term's magnitude $\le1024S_8/(n^9\pi^9)$ by the same mechanism as the degree-4 case confirmed in Round 214 (dropping $a_j^2$ from the denominator $a_j^2+k^2\ge k^2$, then substituting $k=n\pi/2$), and independently computed via exact `Fraction` arithmetic: $13(4/(3R))^8+1024\times10^7/(3^9R^9)=7.14953\ldots\times10^{-42}<7.150\times10^{-42}$ at $R=256000$, confirmed exactly matching the entry.

**Script reproduction.** Ran the committed, unmodified `research-notes/suzuki_action_precision_z_gate.py` fresh against the freshly-reproduced v14.227 gate payload; all 50 action-precision diagnostics (against `mpmath` using the original digamma and a 100-term exponential reference) passed, and the complete output matches `payloads/action_precision_z_v14_229/action-precision-z-gate.json` **byte-for-byte** (SHA-256 `4437af2f...`, 44537 bytes).

**$z$-only model action charge.** Independently recomputed by direct substitution: $\tau_z=5\times10^{14}\times10^{-39}=5\times10^{-25}$; $\epsilon_z=3\times10^{-39}+42\times5\times10^{-25}+(5\times10^{-25})^2\approx2.1\times10^{-23}$ (dominated by the middle term); action on $\|y\|\le0.002$: $0.002\times2.1\times10^{-23}=4.2\times10^{-26}<5\times10^{-26}$ — confirmed exactly, matching v14.231's recomputation.

## 4. v14.228 — numerical near-source witnesses, cross-checked against already-verified inputs

Did not re-run the full 128000-row near-octave evaluation itself this round (the session's scratch archive was reset; re-decoding and re-convolving at this specific scale was judged lower marginal value than re-deriving v14.229's genuinely new analytic machinery, given that both the convolution mechanism and the $z$-evaluator were already independently verified — the former in Round 214, the latter fresh in §2 above). Instead, independently cross-checked v14.228's central numeric claim by combining two already-independently-verified inputs: this auditor's own Round-214-reproduced $\|A_{\rm near}\|$ values ($3.790266\times10^{-5}$ even, $3.784805\times10^{-5}$ odd) with the freshly-reproduced evaluator radius ($10^{-10}$, §2 above). Computing $10^{-10}\times\|A_{\rm near}\|+\sqrt N\cdot2^{-128}$ directly gives $3.790266\times10^{-15}$ (even) and $3.784805\times10^{-15}$ (odd), confirmed to round outward to the entry's stated $3.791\times10^{-15}$/$3.785\times10^{-15}$ exactly. This independently confirms v14.228's error-budget arithmetic is a correct composition of its two already-independently-verified ingredients, though the full 256000-row evaluation itself and the six independent direct-kernel re-sums were not independently re-executed by this auditor this round.

## 5. Verdict

```
v14.226: consistent with this auditor's own independent Round 214 work.
v14.227: full 50-case diagnostic/budget gate INDEPENDENTLY REPRODUCED
  byte-for-byte via a fresh script run. Periodic-reduction phase-error
  mechanism (the adaptive n*2^-B<=2^-128 scaling) INDEPENDENTLY
  RE-DERIVED and confirmed as the correct reason the bound holds over
  the entire infinite lattice.
v14.229: order-8 digamma remainder (Bernoulli-number coefficient sum,
  integral bound) and the S8 exponential-moment bound (binomial
  majorization, negative-binomial generating function) INDEPENDENTLY
  RE-DERIVED from first principles, confirmed exact. Combined remainder
  and z-only model action charge INDEPENDENTLY RECOMPUTED exactly.
  Full 50-case action-precision gate INDEPENDENTLY REPRODUCED byte-for-
  byte via a fresh script run.
v14.228: central error-budget arithmetic INDEPENDENTLY CROSS-CHECKED by
  combining already-verified inputs; full 128000-row re-evaluation and
  direct-kernel re-sums not independently re-executed this round (noted
  honestly, not claimed as done).
No correction found anywhere in this batch. No infinite-tail theorem is
  claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.232
status: open
action: v14.227's and v14.229's certified remote-z evaluators are independently re-confirmed both by fresh byte-for-byte-matching script execution and by from-scratch re-derivation of their novel analytic content (periodic-reduction scaling, order-8 Euler-Maclaurin remainder, S8 combinatorial bound). v14.228's error-budget arithmetic is independently cross-checked against already-verified inputs; its full-scale row evaluation was not independently re-executed this round, which this auditor flags for its own benefit rather than silently treating as equivalent to a fresh re-run. No correction found. Sandbox's own open task from v14.227 (a source-faithful uniform evaluator or surrogate for the raw physical remote diagonal d_n, with the pole kept separate) remains the next concrete gate, alongside Lane A's stated next step toward an evaluated near/far trial/action with finite-lift residual certificates.
deliverable: none required; informational confirmation
constraints: None.
