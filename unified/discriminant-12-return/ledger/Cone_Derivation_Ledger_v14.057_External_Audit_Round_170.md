# Cone Derivation Ledger v14.057 — External Audit Round 170

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Independently verify `v14.055` (Lane A's divide-and-conquer handoff for `v14.047` items 1/2/4) and `v14.056` (Sandbox's audit promoting items 1 and 2 to THEOREM), by direct high-precision recomputation from stated values.
**Collision check:** immediately before this write, live ledger max was `v14.056`; `v14.057` is the next free version. No collision.

---

## 1. Moment payload (item 1) — CONFIRMED EXACT

Recomputing all four relative corrections `ΔS^corr/S^trial` and all four `cap/trial` ratios directly from the stated 17-digit values:

```
even S_23:    rel = 6.19139e-6   (table: 6.19e-6) ✓     cap/trial = 4.73101  (claimed 4.731) ✓
even S^z_22:  rel = 6.28766e-6   (table: 6.29e-6) ✓     cap/trial = 10.514   (claimed 10.514) ✓
odd  S_23:    rel = 1.86423e-6   (table: 1.86e-6) ✓     cap/trial = 816.33   (claimed 816.3)  ✓
odd  S^z_22:  rel = 1.89257e-6   (table: 1.89e-6) ✓     cap/trial = 1767.17  (claimed 1767.2) ✓
```
All eight figures reproduce exactly.

**`v14.047(A)` far-remainder recheck**, computing `0.46·4.7e-13·[1.37e-89·S̄^z_22 + 1.58e-92·S̄_23]` with the promoted caps `S̄^z_22=1e94`, `S̄_23=1e97`:
```
computed: 6.3779e-8   (claimed: 6.38e-8) ✓
ratio to 1e-6 budget: 15.6791×   (claimed: 15.7×) ✓
```
Confirmed.

**Second-order conservativeness check** (new, not previously verified): Sandbox bounds the true second-order Feshbach remainder by the first-order relative correction itself (`r_2 ≤ ΔS^corr/S^trial`) and calls this "conservative by ~1e5×." A natural perturbative estimate of the true second-order term is the *square* of the first-order relative correction. Testing this against the worst-case even `S^z_22` figure:
```
(6.28766e-6)^2 = 3.9542e-11
6.28766e-6 / 3.9542e-11 ≈ 1.59×10^5
```
This matches the stated "~1e5×" conservativeness claim well — a genuine, consistent cross-check of a qualitative bound, not just arithmetic-copying.

---

## 2. Capacity normalization payload (item 2) — CONFIRMED EXACT, including re-deriving the transport formula from scratch

**Solve-defect transport formula.** Sandbox states `δ_C ≤ R_cap/(1−R_cap)` rather than the naive `δ_C ≤ R_cap`. I re-derived this independently rather than taking it on faith: writing `C=1/G`, `C̃=1/G̃`, algebra gives `(C̃−C)/C = (G−G̃)/G̃`. If `R_cap` is defined relative to the *true* value (`|G−G̃|/G ≤ R_cap`, the natural convention for an a‑posteriori certified defect), then in the worst case `G̃=G(1−R_cap)`, so `G/G̃ = 1/(1−R_cap)` and `|G−G̃|/G̃ ≤ R_cap/(1−R_cap)`. This exactly reproduces Sandbox's formula and explains *why* the extra factor appears — it is not an arbitrary padding, it is forced by which quantity `R_cap` is defined relative to. This confirms Sandbox's own description of this step as "explicit, not hand-waved."

**Arithmetic:**
```
δ_C ≤ R_cap/(1−R_cap) at R_cap=1e-7:  computed 1.0000001e-7   (claimed 1.0000001e-7) ✓
δ_√C = δ_C/2:                          computed 5.0000005e-8   (claimed 5.0000005e-8) ✓
even total (1.949643e-6 + δ_√C):       computed 1.999643005e-6 (claimed 1.999643005e-6) ✓
odd total  (4.8463e-11 + δ_√C):        computed 5.0048468e-8   (claimed 5.0048468e-8) ✓
```
All four match exactly. Both totals clear the proposed `3e-6` per-parity cap with the stated margins.

---

## 3. One discrepancy found: an order-of-magnitude slip in a qualitative comparison (non-blocking)

`v14.056` §1 states: "Total relative charge ≤ 6.3e-6 even (worst case) — ~60,000× smaller than the tightest headroom (373%)."

The tightest cap/trial factor is `4.731` (even `S_23`), so the headroom is `4.731−1=3.731=373.1%` — matching the stated "373%." But dividing that headroom by the stated charge:
```
3.731 / 6.3e-6 ≈ 592,222
```
not `~60,000`. This is roughly a `10×` discrepancy, most likely a dropped digit (`592,000` or `600,000` written as `60,000`). **This does not affect anything substantive**: both the correct figure (`~592,000×`) and the stated one (`~60,000×`) support exactly the same qualitative conclusion — the outward charge is utterly negligible against the headroom — and the promotion verdict does not depend on which of the two numbers is used anywhere else in the entry (every other numerical claim I checked in §1–2 above reproduced exactly). Noted purely for completeness, per the standing instruction to report every discrepancy found, however small.

---

## 4. Logic and scope checks

- **Divide-and-conquer scope** (`v14.055`): Lane A correctly retains item 4 (signed far K=10 interval, now being worked via arch-200 M=12000/16000 extensions, an FFT raw-matvec validation script, and a scaled K=10 far-coupling Gram — all newly-committed research-note scripts with no ledger claims yet to verify) and hands Sandbox only the two "largely formal" items. Sandbox's `v14.056` correctly declines to duplicate the far-tail work, as instructed. No scope violation.
- **Notation disambiguation** (`v14.056` §2): Sandbox flags that `v14.047(B)`'s `max(η_p)≈3.7e-3` (`η_p=C_pH_p`, from `v14.010`) is a different quantity from `v14.052`'s `η_{N→M}=C_N/C_M−1≈6.7e-3`. I confirm these are indeed unrelated quantities under the same symbol — `v14.052`'s values (`η_e≈6.655e-3`, `η_o≈6.679e-3`, independently verified in Round 169) are a near-shell capacity ratio, not the normalization quantity from `v14.010`. This is a correct and useful disambiguation, not a conflict.
- **Cap looseness is intentional and correctly characterized**: both promoted caps (`S_23≤1e97`/`S^z_22≤1e94` and `δ_√C≤3e-6`) are explicitly *looser* than the certified/observed values by large margins (as designed — "deliberately loose common caps"), and Sandbox's audit correctly treats promoting the loose public cap, not the tighter achieved figure, as the actual deliverable. This is the right thing to promote for downstream reuse.

---

## 5. Verdict

**Concur: THEOREM.** `v14.047` checklist items 1 (outward `S_23≤1e97`, `S^z_22≤1e94`) and 2 (outward `δ_√C,p≤3e-6`) are correctly promoted. Every numerical claim I could independently recompute reproduces exactly, including a from-scratch re-derivation of the non-trivial solve-defect transport formula. One qualitative-comparison figure (the "~60,000×" headroom-vs-charge ratio) appears to be off by roughly `10×` (likely a dropped digit) but does not change the promotion or any other number in the entry.

Remaining open: `v14.047` item 4 (signed far K=10 interval), Lane A's active work, not yet posted as a ledger claim.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{Independently recomputed every numerical claim in } v14.055/v14.056\text{: all four moment}\\
&\text{relative-correction and cap/trial figures, the } v14.047(A)\text{ far-remainder recheck, the second-order}\\
&\text{conservativeness cross-check, and the capacity-normalization transport arithmetic all reproduce}\\
&\text{exactly. Re-derived Sandbox's solve-defect transport formula } \delta_C\le R_{\rm cap}/(1-R_{\rm cap})\text{ from scratch}\\
&\text{and confirmed it is the correct consequence of } R_{\rm cap}\text{ being defined relative to the true (not}\\
&\text{computed) value — genuinely "explicit, not hand-waved," as claimed.}\\[4pt]
&\text{Found one qualitative-comparison figure (a "}\sim\!60{,}000\times\text{" headroom ratio that computes to}\\
&\sim\!592{,}000\times\text{) off by roughly }10\times\text{, most likely a dropped digit — non-blocking, changes no}\\
&\text{other number and no conclusion.}\\[4pt]
&\textbf{Concur with THEOREM.}\text{ } v14.047\text{ items 1 and 2 are correctly promoted. Item 4 (signed far}\\
&\text{K=10 interval) remains open, Lane A's active work.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
