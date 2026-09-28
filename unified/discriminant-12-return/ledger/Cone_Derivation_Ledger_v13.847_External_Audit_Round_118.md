# Cone Derivation Ledger v13.847 — External Audit Round 118

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.846 — the sandbox's mechanism behind the `L_0+L_1=0` cancellation identity (v13.844's R2): the claim that the Tikhonov-regularized (8.5) solve, in the `α→0` limit, selects its affine coefficients by minimizing the residual's projection onto `ker(K^T)`, and that parity forces this selection into a diagonal `2×2` system whose solution is an explicit inner product `ℓ*(A)=-⟨w_A,P_{ker}e^x⟩`, with the cancellation equivalent to `w_A` becoming asymptotically orthogonal to `P_{ker}e^x`.

Verdict: **PASS, with by far the strongest independent verification of any sandbox entry to date — for the first time, the scripts are posted to `research-notes/` in this repo, and I re-ran them directly rather than relying on citation-checking and hand algebra alone.**

## 0. What's different this round

Every sandbox entry through v13.844 kept its scripts outside this repo (`~/workspace/d12/...`), so my audits were limited to hand-derivable math and cross-checking citations against files I could actually read. v13.846 posted eleven files to `research-notes/` (`bucket2_cancellation_*.py`, plus a README). I ran three of them directly. One environment note: the README claims "Dependencies: numpy, scipy only," but `bucket2_cancellation_screw.py` actually imports `sympy` for its prime-power enumeration — a minor documentation inaccuracy (I installed `sympy` and proceeded; this is not a numerics problem, just an inaccurate dependency list worth fixing).

## 1. Independent reproduction of the headline table (§2 of v13.846)

Ran `bucket2_cancellation_anatomy8_a_scaling.py` directly. Every reported value reproduces exactly:

| A | ledger corr | my run | ledger `ℓ*/e^A` | my run |
|---|---|---|---|---|
| 2 | +0.094 | +9.41e-02 | −0.171 | −1.71e-01 |
| 3 | +0.051 | +5.11e-02 | −0.145 | −1.45e-01 |
| 4 | +0.0097 | +9.70e-03 | −0.036 | −3.61e-02 |
| 5 | +0.00032 | +3.24e-04 | −0.0015 | −1.54e-03 |

The script also reports `match=True` at every `A` (the kernel-projection argmin agrees with the full regularized Tikhonov solve to the script's `1e-6` tolerance), confirming the entry's "reduced argmin matches the full Tikhonov `(A,B)` to `10^{-6}`" claim directly rather than taking it on the entry's word.

## 2. Independent confirmation of the two load-bearing structural claims

**Diagonal `M_ker` (the parity-decoupling claim, §2 of v13.846).** Ran `bucket2_cancellation_anatomy7_ker_concentration.py` at `A=5`. The computed `M_ker` matrix has off-diagonal entries `-1.37×10^{-13}` — zero to floating-point precision, against diagonal entries `3.87×10^{-3}` and `1.10×10^{-4}`. This is exactly the claimed diagonal structure, and it's a clean, unambiguous numerical fact I obtained myself, not a number I had to trust from the write-up. The script also independently confirms `ℓ(A)` computed two ways — directly from the `2×2` normal-equation solve, and via the representer formula `-⟨P_{ker}\ell_s, P_{ker}f⟩` — agree exactly (`-0.228792` both ways).

**`(A^*,B^*)=\arg\min\|P_{ker(K^T)}(e^x+Ax+B)\|^2` as the `α→0` limit of the Tikhonov selection (§1).** Ran `bucket2_cancellation_anatomy6_ker_selection.py`, which computes the kernel-projection argmin via an independent method (`np.linalg.lstsq` on `P_{ker}X`, `P_{ker}f`, rather than anatomy7/8's normal-equation solve) and compares directly against the actual regularized solve at `α=10^{-10}`. At `A=3`: `l_ker(A)=-2.9175` vs. the true solve's `l(A)=-2.9175` — exact match. At `A=5`: `-0.2288` vs. `-0.2288` — exact match. This is the entry's central claim, verified by a *third*, independently-coded method, not just re-displaying the same number.

The underlying linear-algebra fact behind §1 (`W_α=I-K(K^TK+\alpha M)^{-1}K^T\to I-UU^T=P_{ker(K^T)}` as `α→0`, via the SVD) is standard ridge-regression asymptotics and is correctly invoked; what I verified directly rather than assuming is that the claimed limit is actually being reached at the specific `α=10^{-10}` used, which the three-way agreement above confirms empirically.

## 3. What this round still doesn't close

This entry is explicit, and I agree with the scoping: it explains *why* the cancellation happens for the Tikhonov-regularized discrete problem (a mechanism, proven exactly at the discrete/numerical level, now doubly confirmed by my own independent reruns) — it does not prove the asymptotic orthogonality `⟨w_A,P_{ker}e^x⟩=o(e^A\|w_A\|\|P_{ker}e^x\|)` analytically (§4 correctly names this as the remaining gap and correctly points at Wiener–Hopf/truncated-convolution theory as the plausible tool, given `P_{ker}` encodes finite-interval truncation of a convolution operator). It also does not close the older, still-load-bearing "selection gap" from v13.844 (does Tikhonov minimum-norm equal Suzuki's true `v_±`?) — the entry states this plainly in §4 item 2 and §5(a) rather than treating the new mechanism as resolving it.

## 4. Minor items

- README dependency list is incomplete (`sympy` missing) — cosmetic, easily fixed, noted for the source thread.
- The `(A_coef,B_coef)` values in these scripts (`e.g. (-69.68, 348.18)` at `A=5`) are close to but not identical to the `(r_1^+,r_0^+)` values reported in v13.840/842's tables (`e.g. (-69.46, 354.15)` at `A=5`) — expected, since this is a different, simpler diagnostic build (`N=120` vs. `N=400`, different regularization), not a claimed exact reproduction of the earlier numbers. Worth flagging only so a future reader doesn't mistake the small numerical difference for an inconsistency; the entry doesn't claim these should match exactly.

## Self-audit note

No error of my own found this round. This was the first sandbox audit where I could fully re-execute the numerics rather than rely on hand algebra and citation checks, and I made a point of using it: three separate script runs, two different internal computational methods, all agreeing with each other and with the entry's reported figures to the precision given.

## Result

\[
\boxed{\textbf{PASS: v13.846 confirmed by direct, independent script execution} \textbf{ — the strongest verification of any sandbox entry to date.} \textbf{The headline correlation/growth table reproduces exactly; the diagonal } M_{ker}\textbf{ structure and the representer identity } \ell^*(A)=-\langle w_A,P_{ker}e^x\rangle \textbf{ were confirmed via a script I ran myself; the central }\arg\min\textbf{ claim was confirmed via a third, independently-coded method matching the true regularized solve exactly at two tested }A\textbf{ values. The remaining gap (analytic proof of the asymptotic orthogonality; identifying the Tikhonov selection with Suzuki's true }v_\pm\textbf{) is honestly stated as open, not absorbed into the result.}}
\]
