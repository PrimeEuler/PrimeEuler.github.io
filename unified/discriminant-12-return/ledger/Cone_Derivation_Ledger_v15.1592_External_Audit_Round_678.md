# Cone Derivation Ledger v15.1592 — External Audit Round 678

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1591 (explicit nonlinear global quarter-turn range: `0<η≤.1`, `b=.003`)
**Verdict:** CONFIRMED. A proof-only entry (no committed script); every numeric bound independently recomputed from scratch and matches exactly.

## v15.1591 — CONFIRMED

This entry makes the small-`η` existence/nondegeneracy theorem from Rounds 676–677 (v15.1586, v15.1589) fully explicit and quantitative for the concrete range `0<η≤1/10` at budget `b=.003`, replacing the qualitative "`η₀(b)` exists" with hard numeric bounds. This audit independently recomputed every one of them from scratch, with no reliance on the entry's own arithmetic:

- **Gate 1550** (Volterra remainder `r`): confirmed `r=\sinh(\sqrt2)/\sqrt2-1=0.3682988720085909<3/8` by direct evaluation. Confirmed the decomposition into the first two series terms (`2^n/(2n+1)!` at `n=1,2`, giving exactly `1/3` and `1/30`) plus a geometric-tail bound `(1/630)/(1-1/36)=0.0016326530612244899` — the resulting total (`0.368299...`) correctly upper-bounds the exact value. Confirmed `\varepsilon(\eta)=3\eta^2/[64(1-\eta^2/4)]` evaluates to exactly `3/6384=0.00046992481203007516<.00047` at `\eta=.1`.

- **Gate 1551** (moment nondegeneracy): using `B=1/\sqrt{332640}` and `C=240\sqrt{31/79833600}` (both independently confirmed in Round 676), recomputed `|M|\ge[15(b-\varepsilon)/11-B-2\varepsilon]/C` at `\eta=.1,b=.003` and obtained `0.005191407832494493`, matching the ledger's `.00519140783249449` exactly.

- **Gate 1552** (odd-grading tail bound): confirmed numerically that `\sum_{n\ge3,\text{odd}}\eta^n/(2n+1)!<\eta^3/5000` holds at `\eta=.1,.05,.01` (e.g. at `\eta=.1`: `1.984\times10^{-7}<2.000\times10^{-7}`), and confirmed the nonscalar-stretch conclusion is numerically consistent (`2\eta\cdot|M|_{\min}\approx0.00104>0.01\eta=0.001` at `\eta=.1`, using the Gate 1551 bound on `|M|`).

- **Gate 1553** (radial-derivative bound): independently derived the closed form `\sum_{k\ge2}2k(3/4)\eta^{2k-2}/4^k=(3/8)[(1-x)^{-2}-1]` (`x=\eta^2/4`) from the geometric-series derivative identity `\sum_{k\ge1}kx^{k-1}=1/(1-x)^2`, confirmed it matches a direct numerical summation exactly, and evaluated it at `\eta=.1` to get `0.001882054760962537`, matching the ledger's `.001882054760963` to full displayed precision. Confirmed the resulting threshold `2(b-\varepsilon)-.001883=0.0031771503759398495>.00317`.

No committed script accompanies this entry (it states "arithmetic checked with local Python math, no new optimizer run"), consistent with its own disclosure; this audit's independent from-scratch Python verification of every numeric claim stands in place of a script replay.

## Collision check

`v15.1592` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `8d291c8` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

v15.1591 makes the transported-endpoint-theorem existence range fully explicit for `b=.003`, `0<η≤.1`. Every numeric bound in it — the Volterra remainder estimate, the moment-nondegeneracy threshold, the odd-grading tail bound, and the radial-derivative bound — was independently recomputed from scratch this round and matches exactly. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
