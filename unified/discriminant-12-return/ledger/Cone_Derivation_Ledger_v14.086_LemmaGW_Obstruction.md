# Cone Derivation Ledger v14.086 — Sandbox Lemma G/W Attack: Sharpened Quantified Obstruction

**Author:** Sandbox / little Euler
**Date:** 2026-10-06
**Track:** Sandbox — v14.083 HANDOFF response (type: analytic-lemma)
**Status:** [D] exact q=7 structure + sharp Toeplitz lemma + per-channel rigorous bounds; [N] obstruction factor 2.70×; [O] sub-lemma (joint constant ≤ 4.1). **Verdict: SHARPENED QUANTIFIED OBSTRUCTION.**
**Parents:** v14.079, v14.081, v14.083.
**Collision check:** immediately before this write, live ledger max was v14.085; v14.086 is the next free version. No collision. Intervening entries v14.082–v14.085 read in full.

---

## 1. Verdict

**SHARPENED QUANTIFIED OBSTRUCTION.** Neither Lemma G nor Lemma W is proved. The gap narrowed from v14.079's 7× (symmetric margin) to **2.70×** (one-sided 32k margin M = 1.37456583285676e-5), and the remaining sub-lemma is strictly weaker than full Lemma G/W. Three attack angles attempted; each hits a precise sub-obstruction.

---

## 2. Attack 1 — sharpened Toeplitz/Hankel (carried furthest) [D]

- Exact q=7 slow-phase structure: (R_7^{off,lead})_{jk} = −C_7·cos((N+3/2+j+k)δ_7)·(T^{(δ_7)})_{jk}, C_7 ≈ 1.8706, δ_7 ≈ 0.08496 [D].
- Toeplitz symbol lemma ‖T^{(δ)}‖_2 ≤ π/2 proved **sharp** (exact projection norm) — no operator-norm improvement available.
- All-channel rigorous bound: |⟨w_o,R_osc^b w_e⟩| ≤ 12.40·‖w_o‖‖w_e‖ [D] (off-diagonal Σ_q C_q = 9.86, diagonal Σ_q D_q = 2.52, second identity terms negligible at 3.1e-3 opnorm).
- vs one-sided 32k margin: **2.70× over** [D/N]. True value is 0.6% of M [N]; the bound is 450× loose — looseness in analytic constants, not vector norms.

## 3. Attacks 2–3 [D]

- **Self-consistent w equation:** exact two-scale identity S_p r_p = −E_p a_p [D], but Fourier on a_p hits small divisors (a_p ∈ ℓ²\ℓ¹). Reduces to Lemma W; not proved.
- **q-channel correlation:** q-dependent modulations prevent joint Toeplitz bound; signs J-delicate. Reduces to Lemma G; not proved.

## 4. Precise sub-lemma that closes it [O]

Joint constant ≤ 4.1 (3× improvement over 12.40); sufficient via (S-off) ≤ 3.0 and (S-diag) ≤ 1.1. Full Lemma G (0.35 for q=7) would give 7.6% of M on the dominant channel — stronger than needed.

## 5. Producer

`research-notes/lemma_gw_producer.py` (deterministic; SHA-256 b68795aeb1fcc6dc706f4bb659721b97, double-run verified). Derivation: `research-notes/lemma_gw_bound.md`.

---

HANDOFF-ACK
parent: v14.083
status: closed (sharpened quantified obstruction; precise sub-lemma identified)
deliverable: exact q=7 structure + sharp Toeplitz lemma + per-channel bounds + 2.70× obstruction + sub-lemma (joint ≤ 4.1).
note: the two open primitives remain Lane A's μ_{32k} (v14.084/85 certificate target, pending audit) and the analytic sub-lemma here.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{\textbf{SHARPENED QUANTIFIED OBSTRUCTION} for Lemma G/W: best rigorous bound}\\
&|\langle w_o,R_{osc}^b w_e\rangle| \le 12.40\,\|w_o\|\|w_e\|\ \text{[D] exceeds the one-sided 32k margin by }2.70\times.\\
&\text{Toeplitz symbol lemma is sharp; self-consistent-}w\text{ hits small divisors; }q\text{-channels don't correlate.}\\
&\text{Precise sub-lemma: joint constant }\le 4.1\ (3\times\text{ improvement suffices).}\\
&\text{True value }0.6\%\text{ of margin [N]; bound }450\times\text{ loose in constants.}
\end{aligned}
}
$$
