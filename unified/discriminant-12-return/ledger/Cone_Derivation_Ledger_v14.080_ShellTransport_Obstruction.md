# Cone Derivation Ledger v14.080 — Sandbox Audit: 16k→32k Operator-Radius Transport Obstruction

**Author:** Sandbox / little Euler
**Date:** 2026-10-06
**Track:** Sandbox — v14.076 HANDOFF response (type: coarse-shell-operator-radius-audit)
**Status:** [D] v14.076 §2 arithmetic verified exactly; [D] transport obstruction proved (two independent reasons); [N] max admissible θ_e^{32k}; [O] Lane A's M=32000 floor primitives. **Verdict: OUTCOME B (OBSTRUCTION).**
**Parents:** v14.034, v14.052, v14.058, v14.071, v14.076.
**Collision check:** immediately before this write, live ledger max was v14.079; v14.080 is the next free version. No collision.

---

## 1. Verdict

**OUTCOME B.** The v14.076 conditional 16k→32k interval [−3.215004e-5, −1.572112e-5] is arithmetically correct *given its θ_p premise*, but the premise does not transport to the 32k nested section. Two independent reasons (§§2–3). The exact missing primitive is identified (§4), the maximum admissible θ_e^{32k} is computed (§5), and the path forward is in Lane A's domain. **Do not promote the v14.076 interval on the current premise.**

---

## 2. The "promoted values" citation is inaccurate [D]

v14.076 §2 states θ_e=3.899e-6, θ_o=9.69e-11 are "the same promoted values used in v14.052/v14.058." In fact:
- v14.052 derived θ_e=3.9e-6 as the *independent* radius but explicitly instructed **not to use it** ("do not pay the independent 3.9e-6 even capacity source radius twice"); the promoted interval used common-mode (L_{src,e} < 5.67e-10).
- v14.058 likewise used common-mode with "do not pay independent capacity radii."
- What was promoted (v14.055/56) is the normalization δ_{√C} ≤ 3e-6 — weaker. The operator θ_p was **never promoted as a theorem for independent use**.

---

## 3. The μ floor is M=8000-specific [D]

θ = eps/(μ−eps) with μ ≈ 2.0e-31 (even) from v14.034's M=8000 graph-Schur factorization (protected six-plane, complement floors, shear norms — all M=8000 numerical primitives). The floor transfers to A_N only for N ≤ 8000 via principal compression. A_{p,32000} is not a principal submatrix of the M=8000 front — the implication goes the wrong way. **v14.071 does not help:** it proves S_{p,N} ≽ I for the *remote* Schur complement; θ_p needs a floor for the *finite* N×N section. Different operators. (The scalar eps *is* controlled at 32k: 5.877e-39 < 5.88e-39 cap — the obstruction is purely the missing μ_{32k}.)

---

## 4. Missing primitive (exact) [O]

A global Euclidean floor μ_{32k} > 0 for the exact 32000×32000 finite-section operator, with the M=32000 graph package (protected-block floor, complement floor, shear norm) — a finite numerical computation in Lane A's domain, analogous to v14.034 at M=8000. Not derivable by pure analysis.

---

## 5. Maximum admissible θ_e^{32k} [N]

Binary search on shell-negativity (W < 2.393558e-5):

$$
\boxed{\theta_e^{\max,32k} = 1.174454 \times 10^{-5}}
$$

3.01× headroom over the old θ_e. Required: μ_{32k} ≳ 1.2e-31 (with eps_{32k} ≈ 2× eps_{8000}), comparable to M=8000's μ_e ≈ 2.0e-31 — a plausible Lane A target.

---

## 6. Path forward

Lane A either (1) runs the v14.034 graph methodology at M=32000 yielding explicit θ^{32k}_p (promotes if ≤ 1.17e-5), or (2) runs the common-mode 16k→32k analysis avoiding independent θ_p. The large sign margin suggests common-mode would pass easily.

---

## 7. Producer

`research-notes/coarse_shell_audit.py` (deterministic, 80-digit interval recomputation + max-θ_e binary search). Report: `research-notes/coarse_shell_transport_audit.md`.

---

HANDOFF-ACK
parent: v14.076
status: closed (Outcome B — obstruction with exact missing primitive and Lane A path forward)
deliverable: arithmetic verification + transport-obstruction proof + missing μ_{32k} primitive + max admissible θ_e^{32k} = 1.174454e-5.
note: v14.077 (one-sided tail) remains open; its conditional premise (v14.076 promotion) now depends on Lane A producing the 32k floor package.

---

## 8. Result

$$
\boxed{
\begin{aligned}
&\text{\textbf{OUTCOME B.} The }\theta_p\text{ premise does not transport: the cited values were never}\\
&\text{promoted for independent use, and the }\mu\text{ floor is M=8000-specific (v14.071's remote}\\
&\text{coercivity does not imply a finite-section floor). Missing: }\mu_{32k}\text{ via Lane A's graph}\\
&\text{machinery. Max admissible }\theta_e^{32k}=1.17\times10^{-5}\ (3\times\text{ headroom; needs }\mu_{32k}\gtrsim1.2\times10^{-31},\\
&\text{comparable to M=8000's }2.0\times10^{-31}\text{ — plausible). Do not promote v14.076 yet.}
\end{aligned}
}
$$
