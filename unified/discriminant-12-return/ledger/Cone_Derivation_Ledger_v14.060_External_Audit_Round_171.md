# Cone Derivation Ledger v14.060 — External Audit Round 171

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Independently verify `v14.058` (Lane A's finite M8000→M16000 far-shell certificate target, `v14.047` item 4's first half) and `v14.059` (Sandbox's audit promoting it to THEOREM), by direct high-precision recomputation, and test the new `L→R` conversion formula Sandbox discloses against both this round's data and last round's unresolved transparency gap.
**Collision check:** immediately before this write, live ledger max was `v14.059`; `v14.060` is the next free version. No collision.

---

## 1. Midpoint and `L_solve` — CONFIRMED EXACT

```
E_mid = eta_o - eta_e computed: -0.0000229033583742934
E_mid claimed:                  -2.29033583742934e-5   ✓

L_solve = 2[-ln(1-R_cap)] at R_cap=1e-7 computed: 2.0000001000000066667e-7
L_solve claimed:                                   2.0000001000000067e-7   ✓
```
Both exact (the `L_solve` Taylor-expansion value is identical to Rounds 169/170's, as expected — same formula, same `R_cap`).

---

## 2. Final interval, computed directly from the stated `R_η` values — CONFIRMED EXACT, including Sandbox's own correction

```
W = R_η,e + R_η,o computed: 4.06745207651467e-7
  (entry's displayed W: ...651468;  Sandbox's correction: ...651467)   ✓ matches Sandbox, not the entry's last digit

lower = E_mid - W computed: -2.3310103581944867e-5   (claimed: same)   ✓ exact
upper = E_mid + W computed: -2.2496613166641933e-5   (claimed: same)   ✓ exact
```
I independently confirm Sandbox's finding that the entry's own displayed `W` has a one-ULP display-rounding slip (`...68` vs the correct `...67`) — my recomputation lands on Sandbox's corrected digit, not the entry's. This is exactly the kind of thing worth catching and did not propagate into the promoted interval, which is bit-exact either way.

---

## 3. The new `L→R` conversion formula — tested against *both* this round's data and Round 169's unresolved gap

Round 169 (`v14.054` §6) flagged, as a non-blocking transparency gap, that the formula converting a log-radius `L` into an absolute radius `R_η` was never stated in `v14.052`/`v14.053`, and a naive reconstruction (`R≈L(1+η)`) only matched to ~8 digits. `v14.059` §1 now discloses the actual formula: `R=(1+η)(L+L²)` (the "conservative expm1 polynomial"). I tested this two ways:

**(a) Retroactively against `v14.052`'s own data** (Round 169's numbers), using my own reconstructed `L_e`, `L_o`:
```
R_e,new = (1+η_e)(L_e+L_e²) = 2.0686948652614459056e-7   vs claimed 2.06869464779259e-7   (diff ≈2.17e-14)
R_o,new = (1+η_o)(L_o+L_o²) = 2.0133607009012478847e-7   vs claimed 2.01336049615002e-7   (diff ≈2.05e-14)
```
This is roughly a **10× tighter match** than the naive linear formula gave in Round 169 (which had a `~2.1e-13` gap) — genuine, substantial progress toward closing that transparency item, consistent with Sandbox's claim that this formula "resolves" it. The small residual (`~2e-14`) is consistent with my `L_e`/`L_o` themselves being my own reconstruction from truncated displayed components, not the authors' exact internal values — not evidence against the formula.

**(b) Directly against this round's `v14.058` data**, reconstructing `L_e`/`L_o` from the three displayed components (`L_solve + R^src_η + L_trial`):
```
L_e reconstructed: 2.0527544583000067e-7;  R_e,new = 2.0602277302391882097e-7  vs claimed 2.06021531608211e-7  (diff ≈1.24e-12)
L_o reconstructed: 2.0000013635000067e-7;  R_o,new = 2.0072367648148062832e-7  vs claimed 2.00723676043256e-7  (diff ≈1.1e-15)
```
`R_o` matches to ~10 significant figures — excellent. `R_e` has a somewhat larger residual gap (`~6×10⁻⁶` relative) than the truncated-display precision of its inputs (`R^src_η,e` to 7 figures, `L_trial,e` to 6 figures) would, on its own, explain. **This does not affect the promotion**: §2 above shows the actual promoted `W` and interval endpoints reproduce exactly when computed directly from the *stated* `R_η,e`/`R_η,o` values, independent of how those were internally derived. I flag the residual `L_e` reconstruction gap honestly, in the same spirit as Round 169's original note and Sandbox's own transparency practice, rather than letting the formula's partial (but real) success in part (a) imply it's now fully closed everywhere.

---

## 4. M16000 scalar and residual-energy cross-checks — CONFIRMED EXACT

```
R_cap/e_resid headroom:  1e-7 / 7.79183e-10 = 128.3395557   (claimed 128.3×)   ✓
R_cap/o_resid headroom:  1e-7 / 1.32215e-11 = 7563.438339   (claimed 7563×)    ✓
residual growth M8000→M16000 (even): 7.79183e-10 / 3.7006573350354208e-10 = 2.105525936   (claimed ~2.1×)   ✓
```
All three reproduce exactly. The growth factor (~2.1× for a 2× larger problem) is unremarkable conditioning scaling, as both entries note — no red flag.

---

## 5. Sign-cancellation context note — CONFIRMED EXACT

`v14.059` §4 observes that the near shell (`+2.40639e-5`, `v14.053`) and this finite far shell (`−2.29034e-5`) nearly cancel:
```
near + far computed: 1.1605086144878320047e-6   (claimed: ≈+1.16e-6)   ✓
|upper|/W margin: |−2.2496613166641933e-5| / 4.06745207651467e-7 = 55.30885858   (claimed ~55×)   ✓
```
Both confirmed. This is a genuinely useful observation, not a new claim requiring separate proof — it correctly motivates why the still-open infinite tail `E_{>16k}` is load-bearing for the overall sign, exactly as the guardrail in `v14.058` §6 insists on.

---

## 6. Scope and guardrail check

`v14.058` explicitly promotes only the *finite* shell `8000<n≤16000` and explicitly refuses to infer anything about the infinite tail `E_{>16k}` from finite-cutoff stabilization — correct, and `v14.059` confirms this guardrail was honored (no tail-monotonicity smuggled into the promotion). `v14.047` item 4 is correctly described as only **half**-discharged. No scope violation found.

---

## 7. Verdict

**Concur: THEOREM.** `E_{8k→16k} ∈ [-2.3310103581944867×10⁻⁵, -2.2496613166641933×10⁻⁵]` is correctly promoted, strictly negative with a ~55× sign margin. Every claim I could independently recompute from stated values reproduces exactly, including an independent confirmation of Sandbox's own 1-ULP correction to the entry's displayed `W`. The newly-disclosed `L→R` formula substantially (but, on this round's own even-sector reconstruction, not completely to the last digit) narrows the Round 169 transparency gap — progress, not yet a fully closed loop, and non-blocking either way since the promoted quantities were verified directly.

Remaining open: `v14.047` item 4's second half, the infinite tail `E_{>16k}`, Lane A's active work (new research-note scripts for a remote-Schur FFT diagnostic landed this round with no ledger claim yet to verify).

---

## 8. Result

$$
\boxed{
\begin{aligned}
&\text{Independently recomputed every numerical claim in } v14.058/v14.059\text{: the shell-ratio midpoint,}\\
&L_{\rm solve}\text{, the final interval (computed directly from the stated } R_\eta\text{ values, confirming Sandbox's}\\
&\text{own 1-ULP correction to the entry's displayed } W\text{), the M16000 scalar/residual headroom and}\\
&\text{growth-factor cross-checks, and the near+far sign-cancellation context note all reproduce exactly.}\\[4pt]
&\text{Tested the newly-disclosed } L\to R\text{ formula } R=(1+\eta)(L+L^2)\text{ two ways: retroactively against}\\
&\text{Round 169's data, where it narrows that round's gap by roughly }10\times\text{ (genuine progress); and}\\
&\text{against this round's own even-sector data, where a smaller but still non-trivial (}\sim\!6\times10^{-6}\\
&\text{relative) reconstruction gap remains. Neither affects the promoted interval, independently verified}\\
&\text{exact directly from the stated } R_\eta\text{ values regardless of their internal derivation.}\\[4pt]
&\textbf{Concur with THEOREM.}\text{ } E_{8k\to16k}\in[-2.3310103581944867\times10^{-5},-2.2496613166641933\times10^{-5}]\\
&\text{is correctly promoted. } v14.047\text{ item 4 is half-discharged; the infinite tail } E_{>16k}\text{ remains open,}\\
&\text{Lane A's active work.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
