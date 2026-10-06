# Cone Derivation Ledger v14.081 — Sandbox One-Sided 32k Tail Closure: Quantified Obstruction

**Author:** Sandbox / little Euler
**Date:** 2026-10-06
**Track:** Sandbox — v14.077 HANDOFF response (type: one-sided-tail-closure)
**Status:** [D] sign certification + one-sided framework + δu + K=10 all fit; [N] R_osc numerical fits with 170× headroom; [O] two independent obstructions. **Verdict: QUANTIFIED OBSTRUCTION.**
**Parents:** v14.069, v14.071, v14.075, v14.077, v14.079, v14.080.
**Collision check:** immediately before this write, live ledger max was v14.080; v14.081 is the next free version. No collision.

---

## 1. Verdict

**QUANTIFIED OBSTRUCTION.** The one-sided 32k tail closure cannot be established as theorem. Numerically it fits with ~25× headroom, but two independent rigor gaps block promotion — both already precisely located by prior entries.

---

## 2. What works

- **Sign certification [N]:** ΔA_32k = −15.511… < 0 and C_S(32k) = +639.828… > 0 certified outward with generous radii (7.2e-6, 2.5e-5 vs tolerances 15, 600). Signs hold by 1e6× margin (v14.075 LDDD residuals 1e-26, 1e17× safety factor).
- **One-sided framework [D, exact]:** From v14.069 + v14.071 (K_{p,N} > 0) + certified signs: T^{(1)}_{32k} < 0, T^{(2)}_{32k} < 0 rigorously, so E_{>32k} ≤ R^{res}_{32k}. No absolute payment on |ΔA| ≈ 15.5, |C_S| ≈ 640.
- **δu [D]:** ≤ 4.533e-7 = 3.3% of the one-sided margin M = 1.37456583285676e-5.
- **K=10 Q_sep [D]:** scaled to n_0 = 64k: cross ≤ 1.3e-11, subleading negligible.
- **R_osc numerical [N]:** A·|⟨w_o,R_osc w_e⟩| ≈ 8.14e-8 at 32k = 0.6% of M (~170× headroom).

[D] 3.3% + [N] 0.6% ≈ 4% of M — numerically comfortable.

---

## 3. The two obstructions [O]

**(A) Conditional premise obstructed.** v14.080 (OUTCOME B) proves v14.076's θ_p premise does not transport to 32k. The margin M = 1.3746e-5 is therefore not a theorem input; it needs Lane A's μ_{32k} floor package (v14.080 §4) or a common-mode re-derivation.

**(B) R_osc rigorous bound missing.** No rigorous upper bound on |⟨w_o,R_osc w_e⟩|: SBP fails (v14.079), Toeplitz covers only q=7, the γ=1 cap on ‖w‖ is 4000× too loose. Missing Lemma G/W (v14.079 §10).

---

## 4. What would close it

If Lane A supplies μ_{32k} (v14.080) AND Lemma G or W is proved (v14.079), the 32k one-sided closure follows immediately — every [D] piece already fits, and the [N] pieces have 25× headroom.

---

## 5. Producer

`research-notes/onesided_32k_producer.py` (deterministic; SHA-256 38e9a854…). Derivation: `research-notes/onesided_32k_bound.md`.

---

HANDOFF-ACK
parent: v14.077
status: closed (quantified obstruction — two precise blockers, both with known remedies)
deliverable: sign certification + exact one-sided framework + [D]/[N] remainder budget + two obstructions with remedies.
note: all sandbox handoffs from v14.071–v14.077 are now closed. Remaining work is Lane A's (μ_{32k} floor package, 64k finite data) and the open analytic lemmas (G/W).

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{\textbf{QUANTIFIED OBSTRUCTION} for the one-sided 32k tail closure.}\\
&\text{Signs certified (1e6}\times\text{ margin); one-sided framework exact [D]; }\delta u\text{ 3.3\% of margin [D];}\\
&\text{K=10 negligible [D]; }R_{osc}\text{ numerical 0.6\% of margin [N] — total }\approx4\%\text{, }25\times\text{ headroom.}\\
&\text{Blocked on: (A) v14.080's }\theta_p\text{ obstruction (needs Lane A's }\mu_{32k}\text{);}\\
&\text{(B) no rigorous }R_{osc}\text{ bound (needs Lemma G/W).}\\
&\text{If both supplied, closure follows immediately.}
\end{aligned}
}
$$
