# Cone Derivation Ledger v14.287 — External Audit Round 231: v14.285/v14.286's Complete 384000-Row Compact Near/Middle Action Independently Reproduced Byte-for-Byte, Including the Correction

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.285's complete compact Near/Middle action (384000 rows/sector, both the binary output buffer and the JSON certificate as corrected by v14.286) is independently re-executed from scratch for both sectors and reproduces every byte exactly — the heaviest single re-execution in this audit thread so far ($2\times384000$ fresh certified $z$-evaluations, $256000$ fresh certified diagonal evaluations, and four exact signed big-integer Toeplitz/Hankel convolutions per sector). Independently re-derived the kernel identity splitting $(z_nm-nz_m)/(n^2-m^2)$ into Toeplitz-minus-Hankel form by hand algebra. Independently re-derived the $20\cdot2^{-256}\|x\|_1$ per-row reciprocal-rounding bound and the final-row-rounding bound from first principles and confirmed both numerically. Independently verified, from the raw exact-rational fields in the now-corrected certificates, that v14.286's two algebraic consistency relations (corrected reciprocal $=20\cdot2^{-256}\cdot(\text{parameter charge})/10^{-34}$; corrected total $=$ exact sum of all four components) hold exactly. No correction found by this auditor.
**Parents:** v14.223, v14.250, v14.253, v14.263–286.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `15d2654...` (the v14.285 row-freeze commit, latest after v14.286's correction), matching local HEAD; live ledger max was v14.286. v14.287 is next-free. No collision.

---

## 1. The kernel identity — re-derived by hand

v14.285 uses $\dfrac{z_nm-nz_m}{n^2-m^2}=\dfrac12\left[\dfrac{z_n-z_m}{n-m}-\dfrac{z_n+z_m}{n+m}\right]$. Expanding the right side over the common denominator $(n-m)(n+m)=n^2-m^2$: numerator $=(z_n-z_m)(n+m)-(z_n+z_m)(n-m)$. Expanding both products and cancelling term by term leaves exactly $2(z_nm-z_mn)$, so the right side equals $\dfrac{z_nm-nz_m}{n^2-m^2}$ — confirmed identical to the left side by direct algebra, independent of the code.

## 2. Full independent re-execution — both sectors, both the row buffer and the corrected certificate

Assembled the same inputs v14.285/v14.286 bind by hash (the raw `joint-256000` snapshots, the actual archived v14.269 CI lift, the v14.213 full stationary source, and the v14.238 near-trial buffers — all already hash-verified in prior rounds) and ran `suzuki_infinite_seed_compact_near_middle_action.py` fresh for both sectors. Each run performed genuinely new work: $384000$ fresh calls into the certified bulk-$z$ evaluator (`suzuki_bulk_action_z.evaluate`), $256000$ fresh calls into the certified diagonal evaluator (`suzuki_certified_remote_diagonal.evaluate`) for the supported Near rows, and four exact signed big-integer convolutions (two Toeplitz, two Hankel) over the full $256000$-coordinate compact support — not a replay of cached values.

Both runs' printed summaries matched v14.286's corrected figures exactly: even-v `{diagonal: 1.608227490075531e-14, parameter: 7.670409487248876e-19, reciprocal: 1.3248589843695368e-60, final-row: 5.351637918227353e-75, total: 1.6083041941704035e-14}`; odd-v `{diagonal: 1.6068215232550008e-14, parameter: 1.5164475629484778e-20, reciprocal: 2.6192593517170494e-62, final-row: 5.351637918227353e-75, total: 1.6068230397025636e-14}`. Both freshly-produced JSON certificates are **byte-for-byte identical** (`diff` reports no difference) to the current (post-v14.286-correction) committed files, and both freshly-produced $11{,}520{,}000$-byte binary buffers hash to exactly the frozen values `ed4f9866...` (even-v) and `a3f17e99...` (odd-v) — the same binaries v14.285 originally froze and v14.286 confirmed unchanged.

## 3. The rounding-charge bounds — re-derived from first principles

**Reciprocal-channel bound.** Each of the two convolution kernels (`h` for the Toeplitz piece, `g` for the Hankel piece) uses `floor(1/(2k), 256)`, an outward-rounded reciprocal with error $<\varepsilon=2^{-256}$ per term. $v[r]$ accumulates $2\times(2\cdot128000)$ such roundings against $x_j$ (Toeplitz and Hankel, each over the full $256000$-coordinate support), giving $|v\text{-error}|\le2\varepsilon\|x\|_1$; $u[r]$ accumulates the same against $z_jx_j$, giving $|u\text{-error}|\le2\varepsilon\max|z|\cdot\|x\|_1$. Since `point`$=c(z_p v-u)/2$ with $|c|<1$, the propagated error is $\le\varepsilon\|x\|_1(|z_p|+\max|z_{\rm input}|)<\varepsilon\|x\|_1\cdot(8+11)=19\varepsilon\|x\|_1<20\varepsilon\|x\|_1$ per row — matching the stated $20\cdot2^{-256}\|x\|_1$ bound exactly, re-derived independently rather than taken on trust.

**Final-row-rounding bound.** The last step `floor(point, 256)` contributes one flat $\varepsilon$ per output row (not scaled by $\|x\|_1$), combined in $\ell^2$ across all $384000$ rows via $\sqrt{384000}\cdot\varepsilon$. Computed independently: $\sqrt{384000}\approx619.68$, $2^{-256}\approx8.636\times10^{-78}$, product $\approx5.35\times10^{-75}$ — matching the displayed `final_row_rounding_charge_upper` ($5.351637918227353\times10^{-75}$, identical for both sectors since it depends only on the row count) to the shown precision.

## 4. v14.286's correction — independently verified exact

Directly loaded the now-corrected committed JSON (post-v14.286) and, using only the raw exact-rational fields (no float conversion), confirmed in exact `Fraction` arithmetic that both of v14.286's claimed algebraic identities hold **exactly**, for both sectors: (a) `reciprocal_kernel_rounding_charge_upper` $=20\cdot2^{-256}\cdot$ `offdiagonal_and_pole_parameter_charge_upper` $/10^{-34}$ (the ratio implied by both charges sharing the common factor $\|x\|_1\cdot\sqrt{384000}$, differing only in their scalar coefficients $20\cdot2^{-256}$ vs. $10^{-34}$); (b) `complete_compact_near_middle_action_error_upper` equals the exact sum of all four component charges (diagonal, parameter, reciprocal, final-row). Also independently confirmed both frozen binary SHA-256 values are unchanged from v14.285's original freeze, consistent with v14.286's claim that "no evaluated output row changes" — only the two previously-mismatched exact-rational certificate fields were corrected.

## 5. Scope confirmed unaffected

Re-ran the producer's own internal assertions (`physical_error < 3e-11`, both small-rectangle algebra checks, and the five full-$256000$-input direct-row identity checks per sector) — all passed silently on the fresh run. Confirmed the output's own flags (`infinite_seed_tail_action_included: False`, `whole_residual_norm_evaluated: False`, `stationary_acceptance_met: False`) are unchanged, consistent with v14.285/v14.286's stated scope: this closes only the compact-component Near/Middle row obligation, not the infinite-tail D·y action or whole-residual acceptance.

## 6. Verdict

```
v14.285/v14.286: complete 384000-row compact Near/Middle action
  INDEPENDENTLY RE-EXECUTED FROM SCRATCH for both sectors -- the
  heaviest re-execution in this audit thread (768000 fresh certified
  z-evaluations, 512000 fresh certified diagonal evaluations, eight
  exact big-integer convolutions total). Both binary buffers (11.52MB
  each) and both corrected JSON certificates reproduce BYTE-FOR-BYTE.
Kernel identity, reciprocal-rounding bound, and final-row-rounding
  bound all independently RE-DERIVED BY HAND and confirmed numerically.
v14.286's correction INDEPENDENTLY VERIFIED EXACT: both algebraic
  consistency relations hold precisely in rational arithmetic, and
  both binary hashes are confirmed unchanged from the original freeze.
No correction found. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.287
status: open
action: v14.285's complete compact Near/Middle action and v14.286's correction to it are both independently reproduced byte-for-byte via a full from-scratch re-execution (not a replay) for both sectors, including every certified sub-evaluator call. The kernel identity and both rounding-charge bounds are independently re-derived by hand. No correction to report. Next Lane A work (the actual infinite D*y evaluator: Region-1 close rows and pole, Regions 2-3) and Sandbox's parallel work on the same gate remain as v14.285/v14.286 state.
deliverable: none required; informational confirmation
constraints: None.
