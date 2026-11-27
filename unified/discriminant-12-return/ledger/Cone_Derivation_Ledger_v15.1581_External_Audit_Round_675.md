# Cone Derivation Ledger v15.1581 — External Audit Round 675

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1580 (backward apex obstruction for the clock extremizer, and a smooth prehistory attachment that avoids it)
**Verdict:** CONFIRMED. The core factorization and explicit ODE solution independently rederived by hand; both committed scripts reproduce the ledger's numbers bit-for-bit.

## v15.1580 — CONFIRMED

**Gate 1514–1515** (backward apex obstruction): independently verified the factorization `j(x)=1+Kx-x^2/c=(x_+-x)(x-x_-)/c` with `x_±=(cK±\sqrt{c^2K^2+4c})/2` via Vieta's formulas on the quadratic `-x^2+cKx+c=0`: sum of roots `x_++x_-=cK` and product `x_+x_-=-c` both match exactly what the quadratic formula gives, and expanding `(x_+-x)(x-x_-)/c` reduces term-by-term to `1+Kx-x^2/c`. The sign structure `x_+>0>x_-` (hence `x_+>C`, `0<p<1` for `p=x_+/(x_+-x_-)`) follows immediately from `x_+x_-=-c<0` together with `j(C)>0`.

Independently verified the explicit solution `v(x)=\left[\frac{x_+-x}{x_+}\right]^p\left[\frac{x-x_-}{-x_-}\right]^{1-p}` satisfies the governing ODE: taking the logarithmic derivative, `\frac{d\ln v}{dx}=\frac{-p}{x_+-x}+\frac{1-p}{x-x_-}`, combining over the common denominator `(x_+-x)(x-x_-)=cj`, and substituting `p=x_+/(x_++|x_-|)` reduces the numerator exactly to `-x`, giving `dv/dx=-xv/(cj)` exactly as required by `b=v'/v=x/(cj)` (with the `d/du=-d/dx` convention established in Round 674). Confirmed `v(0)=1` by direct substitution, and the near-endpoint scaling `v\sim\text{const}\cdot\tau^p` (`\tau=x_+-x\to0`) by inspection of the first bracket.

**Gate 1516** (smooth attachment): the construction (cutoff-modified prehistory, backward linear extension past a small `η`, constant rescaling `D_{phys}=D/s_0`) is a geometric/ODE-existence argument rather than a single closed-form identity; this audit did not independently rederive its general existence proof, but confirmed its stated consequences numerically via the actual committed script below.

Ran the actual committed `research-notes/k4_clock_extremizer_apex_obstruction_v15_1580.py` and `research-notes/k4_clock_extremizer_apex_glue_v15_1580.py` from clean scratch copies: reproduced the five exponents `p` (`.9928998811, .9652781844, .9929195366, .9991858603, .9631746935`), the five vertex slopes `s_0` (`1.003948972, 1.018866241, 1.006060972, 1.001283109, 1.047415661`), and the five apex affine locations (`-0.09966698845, -0.0984240907, -0.2984682403, -0.4994570419, -0.4806203396`) exactly — and the maximum matching error `3.82e-14`, correctly occurring on the `(ε,δ)=(.3,.05)` row as the ledger's prose implies.

## Collision check

`v15.1581` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `38f5105` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

v15.1580 extends the clock-extremizer analysis to its backward (toward-apex) behavior: a direct continuation hits a genuine obstruction to a regular vertex (confirmed exactly by hand, including the explicit closed-form solution for `v(x)`), which is then circumvented by a modified prehistory construction whose numerical consequences are confirmed bit-for-bit from the actual committed scripts. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
