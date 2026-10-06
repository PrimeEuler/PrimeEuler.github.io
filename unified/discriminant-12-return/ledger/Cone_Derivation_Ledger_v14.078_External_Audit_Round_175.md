# Cone Derivation Ledger v14.078 — External Audit Round 175

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Verify `v14.075` (32k fixed-FFT checkpoint and `C_ρ` architecture replacement), `v14.076` (the conditional 16k→32k coarse operator-radius sign-flip target), and `v14.077` (the one-sided 32k tail-closure strategy built on the sign flip). This batch contains a potentially significant development — a conditional sign flip of the cumulative finite interval at 32k — so verification is thorough.
**Collision check:** immediately before this write, live ledger max was `v14.077`; `v14.078` is the next free version. No collision.

---

## 1. `v14.075`: 32k checkpoint — CONFIRMED EXACT

```
A_e,32k = C_e,32k · L_e,32k² computed: 1200.45870519507233268597046122   (stated: same)   ✓
A_o,32k = C_o,32k · L_o,32k² computed: 1184.94755401610825318114006664   (stated: same)   ✓
ΔA_32k = A_o - A_e computed: -15.511151178964079505   (claimed -15.5111511789641)          ✓
M_o,11 - M_e,11 computed: -644.22366740353019847   (claimed -644.223667403530)             ✓
C_S(32k) = C_D - (M_o-M_e), C_D=-4.396: 639.82766740353019847   (claimed +639.827667403530) ✓
η_o,16k→32k - η_e,16k→32k computed: -2.393557979841e-5   (claimed -2.39355797984e-5)       ✓
```
All six reproduce exactly. The `C_ρ`-architecture decision — retire the low-order absolute `C_ρ` route entirely in favor of the already-audited exact-near/K=10-separated-far split (`N<n<2N` exact, `n≥2N` K=10) — is a sound reuse of machinery independently verified in much earlier rounds (Round 156/`v14.023`), not a new unverified claim.

---

## 2. `v14.076`: the conditional 16k→32k sign flip — CONFIRMED EXACT, correctly framed as conditional

This is the significant item this round: *if* the global relative operator/source radius `θ_p` from `v14.052`/`v14.058` transports unchanged to the nested `N=32000` finite section, the cumulative finite interval through 32k flips from the small positive 16k interval to a **large, strictly negative** one. I verified the entire computation chain independently:

```
E_mid(16k→32k) = η_o - η_e computed: -2.393557979844793e-5   (exact match)                    ✓
L_src,e = 2[-ln(1-θ_e)], θ_e=3.899270146651301e-6: computed 7.7985554976498e-6
L_src,o = 2[-ln(1-θ_o)], θ_o=9.69258681013552e-11: computed 1.9385173621211e-10
L_solve = 2[-ln(1-R_cap)], R_cap=1e-7: computed 2.0000001000000067e-7   (same as prior rounds)
L_e = L_src,e + L_solve = 7.998555507649803e-6   (exact match)                                 ✓
L_o = L_src,o + L_solve = 2.001938617362128e-7   (exact match)                                 ✓
R_η,e = (1+η_e)(L_e+L_e²) = 8.0138908041990716833e-6   (claimed 8.01389080419907e-6)           ✓
R_η,o = (1+η_o)(L_o+L_o²) = 2.0057132914765268359e-7   (claimed 2.00571329147653e-7)           ✓
W = R_η,e + R_η,o = 8.2144621333467243669e-6   (claimed 8.21446213334672e-6)                    ✓
[E_mid-W, E_mid+W] = [-3.21500419317947e-5, -1.57211176651012e-5]   (exact match both ends)   ✓
```
I also independently verified the `L→R` conversion formula `R=(1+η)(L+L²)` — disclosed by Sandbox in Round 171 and only approximately reproducible there from truncated inputs — now matches **exactly** given this entry's full-precision `L` values, retroactively confirming that Round 171's residual gap was a reconstruction artifact (truncated display inputs), not a flaw in the formula itself.

**Cumulative 4k→32k interval**, combining the already-promoted `4k→16k` interval with this `16k→32k` shell:
```
lower: 3.45557892442104e-7 + (-3.21500419317947e-5) = -3.18044840393526e-5   (exact match)   ✓
upper: 1.97545933653356e-6 + (-1.57211176651012e-5) = -1.37456583285676e-5   (exact match)    ✓
```
Both reproduce exactly.

**Framing check.** The entry is explicit and correct that none of this is promoted: the sign flip is conditional on an open audit question (whether `θ_p` transports to the nested 32k section), and the guardrail against inferring the infinite tail from finite stabilization is respected throughout. The handoff to Sandbox correctly separates the two possible outcomes (transport confirmed → promote; transport fails → quantify the largest admissible `θ_e^{32k}`) rather than presupposing either.

---

## 3. `v14.077`: one-sided tail-closure strategy — CONFIRMED EXACT, sign logic independently verified

Building on `v14.071`'s `γ_N=1` theorem (confirmed correct in Round 174), this entry observes that `S_{p,N}⪰I` makes `K_{p,N}=⟨u,S_{p,N}^{-1}u⟩>0` for nonzero `u` — a positive-definite quadratic form — and that the signs of the two leading tail terms are therefore fixed by the signs of `ΔA_{32k}` and `C_S(32k)` alone.

**Arithmetic:**
```
ΔA_32k computed: -15.5111511789640795...   (claimed -15.5111511789640795)   ✓ (consistent with v14.075)
C_S(32k) using the more precise C_D=-4.395585571978897: computed 639.82808183155130147   (claimed 639.8280818315513)   ✓
"~40× looser" check: 1.37456583285676e-5 / 3.4556e-7 = 39.78×   (claimed "~forty times")   ✓
"3.3% of new margin" check: 4.533e-7 / 1.37456583285676e-5 = 3.298%   (claimed "~3.3%")   ✓
```
All four confirmed.

**Sign-propagation logic**, re-derived rather than taken on faith: `T^{(1)}_{32k}=ΔA_{32k}·K_{o,32k}`; since `ΔA_{32k}<0` and `K_{o,32k}>0` (from `v14.071`'s coercivity), `T^{(1)}_{32k}<0`. Likewise `T^{(2)}_{32k}=-A_{e,32k}·C_S(32k)·K_{o,32k}·K_{e,32k}`; since `A_{e,32k}>0`, `C_S(32k)>0`, and both `K`'s are `>0`, the product of four positives negated is `<0`, so `T^{(2)}_{32k}<0`. Both signs confirmed correct given the stated premises, making it valid to discard both terms when seeking only an *upper* bound on `E_{>32k}` — a materially easier one-sided task than the original symmetric (absolute-value) budget.

**Scope check.** The entry correctly flags that the midpoint `ΔA`/`C_S` values are not yet outward sign certificates, that `v14.076`'s finite interval remains an open, unaudited premise, and that the favorable-sign argument requires those signs to be outward-certified (not just true at the midpoint) before it can be used in a theorem. This is the right level of caution for a strategy-setting entry.

---

## 4. Verdict

All three entries check out — every numerical claim I attempted reproduces exactly, and the one piece of new mathematical reasoning (sign propagation from `ΔA`/`C_S` through the positive-definite `K_{p,N}` factors) is independently re-derived and correct. Nothing here is a THEOREM yet: `v14.076`'s sign flip is explicitly conditional on an open transport question, and `v14.077`'s one-sided strategy is explicitly conditional on both that and outward sign-certifying `ΔA_{32k}`/`C_S(32k)`. Both guardrails are honored throughout.

This is a genuinely promising strategic turn: if the `θ_p` transport question resolves favorably, the remaining one-sided margin (`1.37×10⁻⁵`) is about 40× looser than the symmetric 16k-based target the project had been working against — a substantially easier bar for the still-open infinite-tail analysis (`v14.072`'s dispatched oscillatory bound) to clear.

---

## 5. Result

$$
\boxed{
\begin{aligned}
&\text{Independently verified every numerical claim across } v14.075\text{–}v14.077\text{: the 32k fixed-FFT}\\
&\text{checkpoint data, the full } \theta_p\text{-transport conditional sign-flip computation (midpoint, log-radii,}\\
&\text{the } L\to R\text{ conversion, and both the 16k}\to\text{32k and cumulative 4k}\to\text{32k intervals), and the}\\
&\text{one-sided tail-closure arithmetic all reproduce exactly. Re-derived the sign-propagation argument}\\
&\text{(}T^{(1)},T^{(2)}<0\text{ from } \Delta A_{32k}<0\text{, } C_S(32k)>0\text{, and } K_{p,32k}>0\text{ via } v14.071\text{'s coercivity) from}\\
&\text{scratch — correct.}\\[4pt]
&\text{No THEOREM overreach: the sign flip and the one-sided strategy both remain correctly framed as}\\
&\text{conditional on open audit questions. If the transport premise holds, the remaining margin for the}\\
&\text{infinite tail relaxes by } \sim\!40\times\text{ — a significant, well-verified strategic development.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
