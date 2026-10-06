# Cone Derivation Ledger v14.074 — External Audit Round 174

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Follow up on Round 173's `compression_svd_producer.py` fix by re-executing it; verify `v14.071` (the `γ_N=1` nested-coercivity theorem and 32k/64k finite-data launch), `v14.072` (Sandbox's oscillatory quadratic-form handoff), and `v14.073` (Sandbox's updated conditional-enclosure constants and admissible budgets) by direct recomputation and by independently running the newly-committed producer.
**Collision check:** immediately before this write, live ledger max was `v14.073`; `v14.074` is the next free version. No collision.

---

## 1. Follow-up: `compression_svd_producer.py` fix — runs now, with one new precision note

Round 173 flagged that this script failed outright (missing `/tmp/eff_core`). The fix commit repoints the import to the committed `suzuki_endpoint_M3999_midpoint_effective_core.py` module. **I ran it. It executes successfully now** — the import-failure finding is resolved.

The commit message claims "sigma values verified identical." Running it myself and comparing against `v14.067`'s own table:
```
         even σ_{r+1}          my fresh run        v14.067 cited
r=24:    1.577788e-06          1.5777881...e-06    1.577788e-06    ✓ exact
r=32:    1.207392e-08          1.2073918...e-08    1.207392e-08    ✓ exact
r=48:    2.263718e-13          2.2635336...e-13    2.263718e-13    close (differs ~0.008%)
r=64:    5.603915e-16          1.9162575...e-16    5.603915e-16    differs ~2.9×
r=96:    6.747023e-17          3.8415402...e-17    6.747023e-17    differs ~1.75×
```
(odd parity shows the same pattern: exact at `r=24,32`, close at `48`, and off by comparable factors at `64,96`.) So "verified identical" holds at the ranks that actually matter for the comparison table (`24`, `32`) and is close at `48`, but does not hold at `64`/`96`. **This changes nothing about `v14.067`'s OBSTRUCTION verdict** — both the cited and my freshly-computed values at `r=64`/`96` are deep in the binary64 noise floor (`~1e-16`–`~1e-17`, where `v14.067` itself notes `σ_{r+1}≤5.6e-16≈3·σ_1·ε_mach`), many orders of magnitude below the `~1e-6`-scale observed endpoint mismatches that the verdict actually turns on; if anything my fresh values are *smaller*, reinforcing rather than threatening the conclusion. Noted for completeness, not as a blocker.

---

## 2. `v14.071`: the `γ_N=1` nested-coercivity theorem — independently re-derived, CONFIRMED CORRECT

This is presented as `[D]` (theorem-level), so I re-derived the argument from scratch rather than accepting the label. Claim: given the already-promoted `S_{p,4000}⪰I` (`v14.044`/`v14.046`), the Schur complement onto any later remote space `H_{>N}` (`N≥4000`) also satisfies `S_{p,N}⪰I`.

**Step 1 (Schur-complement associativity):** splitting `H_{>4000}=H_{(4000,N]}⊕H_{>N}` and writing `S_{p,4000}=[[A,B],[B*,D]]` in block form, the remote operator after further eliminating the `(4000,N]` block is `S_{p,N}=D-B*A⁻¹B` — the same object obtained by Schur-complementing `[1,N]` directly out of the original operator. This is a standard, correct fact about nested Schur complements.

**Step 2 (variational characterization):** for any `z∈H_{>N}`, `z*S_{p,N}z = min_y [y;z]*S_{p,4000}[y;z]` (completion of squares, using invertibility of `A`). Standard and correct.

**Step 3 (coercivity transport):** since `S_{p,4000}⪰I`, for *every* `y`: `[y;z]*S_{p,4000}[y;z] ≥ |y|²+|z|²`. If `f(y)≥g(y)` pointwise, then `min_y f(y) ≥ min_y g(y)` (let `y*` minimize `f`; then `min f = f(y*) ≥ g(y*) ≥ min_y g(y)`). Applying this with `f(y)=[y;z]*S_{p,4000}[y;z]` and `g(y)=|y|²+|z|²` gives `min_y f(y) ≥ min_y g(y) = |z|²` (minimized at `y=0`). Hence `z*S_{p,N}z ≥ |z|²` for all `z`, i.e. `S_{p,N}⪰I`.

**Confirmed correct, step by step.** This is a genuine theorem, not a relabeled diagnostic — it correctly upgrades the exploratory `γ≈6.38` (a numerical diagonal/window estimate) to the rigorous `γ_N=1` for every nested `N≥4000`, with no new eigensolve required. A clean, well-executed piece of mathematics.

---

## 3. `v14.072`: Sandbox oscillatory-bound handoff — scope and guardrails sound

A pure strategy/handoff entry, no new numerical claims. The explicit instruction not to infer the theorem bound from the previously-observed `97×` numerical cancellation (already independently confirmed by me in Rounds 172–173, both by hand and by running `infinite_tail_cancellation.py`) is exactly the right discipline — a numerically observed cancellation is not a proof, and the entry correctly treats it as a target to beat analytically, not evidence to cite. No issues found.

---

## 4. `v14.073`: updated enclosure constants — CONFIRMED EXACT, including full producer re-execution

**Hand recomputation of the `δu` coarse table** (`2·A_max/(√12·N²)` at `A_max=804`):
```
N=16k:  2·804/(√12·16000²) = 1.813e-6   (table: 1.813e-6)   ✓
N=32k:  2·804/(√12·32000²) = 4.533e-7   (table: 4.533e-7)   ✓
N=64k:  2·804/(√12·64000²) = 1.133e-7   (table: 1.133e-7)   ✓
N=128k: 2·804/(√12·128000²)= 2.833e-8   (table: 2.833e-8)   ✓
```
and the margin ratios (`5.25×`, `1.31×`, `0.328×`, `0.082×`) all confirmed exactly by direct division against `m*=3.45557892442104×10⁻⁷`.

**64k admissible-budget arithmetic:**
```
m* - δu(64k) = 3.4556e-7 - 1.133e-7 = 2.322e-7   (entry: 2.322e-7)   ✓
0.35×2.322e-7 / K_diag(7.42e-7) = 8.127e-8/7.42e-7 = 0.1095 → |ΔA|<0.11   ✓
0.50×2.322e-7 / (804·7.42e-7²) = 1.161e-7/4.4265e-10 = 262.3 → |C_S|<262   ✓
```
Both match exactly.

**Independent execution of `gamma1_budget_update.py`** — this time genuinely committed to `research-notes/` (the ledger text's reference to `~/workspace/d12/gamma1_budget_update.py` is a stale prose artifact; the actual committed file ran cleanly with no missing-dependency issue, unlike §1's script). Running it reproduces the entire table and both verdicts bit-for-bit:
```
N=64000: K_up=7.8125e-06, dU(coarse)=1.1333e-07, dU/margin=0.328, K_diag=7.42e-07
         |dA| < 8.13e-08/7.42e-07 = 0.110   |C_S| < 262.3
N=32000: dU(coarse,32k)=4.533e-07 = 1.31x margin -> coarse enclosure CANNOT fit at 32k
```
Exact match to the ledger entry in every printed field.

**Cross-reference check:** the entry's "window computation gives `K_o−K_e=6.82e-10`" matches the exact figure (`6.819462e-10`) I independently computed by running `infinite_tail_cancellation.py` in Round 173 — a nice internal consistency confirmation that this entry is building on genuinely verified prior numbers, not restating an unverified one.

---

## 5. Verdict

All three entries check out. `v14.071`'s `γ_N=1` theorem is independently re-derived and confirmed correct from first principles, not just taken on the entry's own `[D]` label. `v14.073`'s updated enclosure constants and admissible 64k/32k budgets reproduce exactly both by hand and by direct execution of the newly-committed, now-functional producer. The Round 173 producer-gap finding is substantively closed, with one precision caveat at the two deepest, practically-irrelevant ranks noted for completeness.

Current state of the overall problem, for continuity: the finite near+far cumulative interval is theorem through `16000` (`v14.059`); `γ_N=1` is now theorem for every nested cutoff; `N=64000` is, with current coarse bounds, the first cutoff where the admissible-budget arithmetic has room — pending Lane A's `ΔA_{64k}`, `C_S^{paired}(64k)` (fixed-FFT producer running) and Sandbox's `R_osc^{max}(N)` construction (`v14.072`, dispatched, not yet delivered).

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{Re-ran } \texttt{compression\_svd\_producer.py}\text{: Round 173's import-failure finding is fixed; the cited}\\
&\sigma_{r+1}\text{ table matches exactly at } r{=}24,32\text{ and closely at } r{=}48\text{, but differs by } \sim\!2\text{--}3\times\text{ at the}\\
&\text{binary64-noise-floor ranks } r{=}64,96\text{ — immaterial to the OBSTRUCTION verdict either way.}\\[4pt]
&\text{Independently re-derived } v14.071\text{'s } \gamma_N=1\text{ nested-coercivity theorem step by step (Schur-}\\
&\text{complement associativity, the variational characterization, and the pointwise-minimum inequality}\\
&\text{all check out) — genuinely correct, not a relabeled diagnostic.}\\[4pt]
&\text{Confirmed every arithmetic claim in } v14.073\text{'s updated enclosure table and 64k/32k admissible}\\
&\text{budgets, both by hand and by running the newly-committed } \texttt{gamma1\_budget\_update.py}\text{ end to}\\
&\text{end — exact match in every field.}\\[4pt]
&\textbf{Concur with all three entries.}\text{ No theorem-promotion overreach found; } N\approx64\text{k remains the}\\
&\text{active target, pending Lane A's finite data and Sandbox's oscillatory-remainder construction.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
