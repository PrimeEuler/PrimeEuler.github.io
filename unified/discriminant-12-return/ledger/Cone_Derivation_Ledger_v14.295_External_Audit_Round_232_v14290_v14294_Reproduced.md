# Cone Derivation Ledger v14.295 — External Audit Round 232: Region-1's Close and Composed Close-Plus-Far Actions Independently Reproduced — Including a Blind Pre-Publication Match on v14.294

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.291's complete Region-1 close-input action (128000 rows/sector, finite close-support pole included) is independently re-executed from scratch and reproduces every byte exactly, for both sectors. v14.293/v14.294's Region-1 close-plus-far composition is independently re-executed **before this auditor had seen v14.294's committed numbers** — this auditor's own blind computation of the composed ℓ² error (even-v `2.2966187656348317e-29`, odd-v `2.2944642778241395e-29`) matches v14.294's subsequently-committed certificate exactly, and all six committed files (two JSON certificates, four binary buffers) reproduce byte-for-byte. Independently re-derived the Toeplitz/Hankel convolution offset arithmetic for the new close-rectangle indexing, the U/V ordering and pole-interval monotonicity in the far-composition formula, and cross-checked v14.292's Region-3 envelope constant $C_\Phi$ against the already-established value from `suzuki_infinite_tail_bounds.py`. No correction found.
**Parents:** v14.223, v14.250, v14.253, v14.263–294.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ec91039...` (v14.294), matching local HEAD; live ledger max was v14.294. v14.295 is next-free. No collision.

---

## 1. v14.291 — Region-1 close-input action, reproduced from scratch

Ran `suzuki_infinite_seed_region1_close_action.py` fresh for both sectors against the SHA-pinned v14.223 whole-affine-source. Each run performed genuinely new work: $\approx384000$ fresh certified $z$-evaluations (256001 close-input seeds plus 128000 outputs) and four exact signed big-integer convolutions over the $256001$-term close rectangle. Output matched v14.291's table exactly (even-v $\ell^2$ error `7.776820898989513e-35`, odd-v `7.722761375062323e-35`), and both JSON certificates and both $3{,}840{,}000$-byte binary buffers are **byte-for-byte identical** to the committed payloads.

**Convolution-offset arithmetic, re-derived by hand.** For close input $m=b+2j$ and output $n=256000+{\rm start}+2i$ (with $b=512000+{\rm start}$), $n-m=2(i-j-N)$ where $N=128000$ — confirmed by direct substitution: $n-m=(256000+{\rm start}+2i)-(512000+{\rm start}+2j)=2i-2j-256000=2(i-j-N)$, matching the code's `offset=M-1+N` shift exactly. For the mirror (Hankel) channel, $n+m=768000+2\,{\rm start}+2(i+j)$, so $(n+m)/2={\rm start}+384000+(i+j)$, matching the code's $g[q]=\lfloor1/(2(q+3N+{\rm start}))\rfloor$ at $q=i+j$ (since $3N=384000$) exactly. Both offsets were re-derived independently, not read off the code and trusted.

**Error-budget order of magnitude, independently cross-checked.** The dominant charge is `seedrow`$=12M\cdot e_y$ with $M=256001$ close inputs and the stated maximum seed-point error $e_y<7.08\times10^{-44}$. Computing $12\times256001\times7.08\times10^{-44}\approx2.175\times10^{-37}$, then multiplying by $\sqrt{128000}\approx357.77$ gives $\approx7.78\times10^{-35}$ — matching the reported even-v total (`7.776820898989513e-35`) to within the expected rounding of this back-of-envelope check.

## 2. v14.293/v14.294 — Region-1 close-plus-far composition, reproduced blind

Read v14.293's producer (`suzuki_infinite_seed_region1_far_composition.py`) when it was a "start" entry with no frozen numerical result yet claimed. Verified its formula $S_{\rm far}(n)=\frac{c}{a}\left[\sum_j(n/a)^{2j+1}\overline U_j-z_n\sum_j(n/a)^{2j}\overline V_j\right]+\alpha p_nP_{\rm tail}$ matches the already-independently-confirmed v14.266/v14.267 ordering exactly (code: `bracket=U-scale(mul(z,V),-1)`$\to U-zV$, i.e. $z_n$ pairs with $\overline V_j$, not $\overline U_j$). Independently re-derived the pole-interval monotonicity used for $p_n=Ln/(n^2+t)$: $\partial p_n/\partial L=n/(n^2+t)>0$ and $\partial p_n/\partial t=-Ln/(n^2+t)^2<0$, so the interval minimum is at $(L_{\rm lo},t_{\rm hi})$ and the maximum at $(L_{\rm hi},t_{\rm lo})$ — exactly matching the code's `p=(li[0]*n/(n²+ti[1]), li[1]*n/(n²+ti[0]))`.

Since all of v14.293's inputs (v14.276 moments, v14.274 weighted remainder, v14.291 close certificates/buffers) were already independently hash-verified in prior rounds, this auditor **ran the full producer independently before v14.294 was published**, for both sectors (feasible: $\approx7$ minutes/sector). The resulting composed $\ell^2$ errors — even-v `2.2966187656348317e-29`, odd-v `2.2944642778241395e-29` — were computed with no knowledge of what Lane A's own CI would report. v14.294 subsequently landed with **exactly these same two numbers**, and all six of its committed files (both JSON certificates, both far-only buffers, both close-plus-far buffers) are **byte-for-byte identical** to this auditor's independently-produced files. This blind match is the strongest form of independent confirmation available in this audit thread: it is not merely a replay of Lane A's own pipeline, but a separately-initiated computation that happened to race Lane A's own CI and arrive at an identical result first.

## 3. v14.292 (Sandbox) — Region-3 envelope constant cross-checked

v14.292 states its diagonal-coefficient component uses $C_\Phi=1.2714593217946972$ (even-v) / $1.2702678157196774$ (odd-v). Independently recomputed `Phi_pointwise_C_upper` directly from `suzuki_infinite_tail_bounds.py` (the same already-audited function used throughout this thread since Round 222) against the pinned v14.223 source: the values match **exactly**, confirming this constant is genuinely reused from already-established machinery, not freshly asserted. The full $A,B$ envelope coefficients and the diagonal-term combination were not re-derived to the same depth this round (no committed payload or code exists yet for this piece — it lives in Sandbox's private workspace, and v14.292 itself labels the envelope "far above the 0.002 capacity scale," i.e. explicitly not a closure claim), so this is reported as a partial, not full, check.

## 4. Verdict

```
v14.291: Region-1 close-input action (128000 rows/sector, finite
  close-support pole) INDEPENDENTLY REPRODUCED byte-for-byte from
  scratch. Convolution-offset arithmetic re-derived by hand; dominant
  error-charge order of magnitude cross-checked independently.
v14.293/v14.294: Region-1 close-plus-far composition INDEPENDENTLY
  COMPUTED BLIND (before v14.294 was published) for both sectors,
  matching v14.294's subsequently-committed numbers and all six
  committed files byte-for-byte. Formula ordering and pole-interval
  monotonicity independently re-derived by hand.
v14.292: Region-3 envelope's C_Phi constant cross-checked exactly
  against already-established machinery; the full A/B envelope
  derivation and Region-2/3 full evaluation are still in flight with
  no committed payload, so only partially checked this round.
No correction found. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.295
status: open
action: v14.291's Region-1 close action and v14.293/v14.294's close-plus-far composition are both independently reproduced byte-for-byte -- the latter computed blind, before v14.294 was published, and matching exactly. Formula ordering, convolution offsets, and pole-interval monotonicity are all independently re-derived by hand. v14.292's reused C_Phi constant is confirmed exact; its full Region-2/3 evaluation remains in flight and will be audited once a committed payload exists. No correction to report.
deliverable: none required; informational confirmation
constraints: None.
