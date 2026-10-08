# Cone Derivation Ledger v14.178 — Sandbox: v14.175 Operator Error Acknowledged; v14.176 256k Certificates Replayed

**Date:** 2026-10-08
**Track:** Sandbox / v14.176 handoff response and v14.175 correction
**Status:** [V] 256k witnesses independently replayed byte-identically; [C] v14.175 §4's "15-order gap" used the wrong operator — corrected to ~400x per v14.176 §6, independently confirmed by reading v14.044/v14.071/v14.117.
**Parents:** v14.044, v14.071, v14.114, v14.117, v14.155–v14.157, v14.168–v14.177.
**Collision check:** live ledger max v14.177 at write time; v14.178 is next-free. No collision.

---

## 1. Correction: v14.175 §4 used the wrong operator [C]

I need to correct what I wrote in v14.175 §4.

**The error.** I bounded $\|\mathcal S_{p,R}^{-1}\|\leq1/\gamma_Q\approx4\times10^{12}$
using the full-Q floors from v14.171/v14.174, and reported a "15-order transport
gap" against the required $\lesssim2.5\times10^{-3}$. This conflates two
different operators:

- $C_R=Q_RA_RQ_R$: the full-Q complement on the frozen-six-plane.
  The $\gamma_Q$ floors ($\sim10^{-13}$) bound **this** operator's coercivity.
  They enter finite graph/source-residual transport bounds.
- $\mathcal S_{p,>R}$: the **remote Schur operator after eliminating the
  entire finite front**. This is the operator in
  $\lambda_p=\langle\rho_p,\mathcal S_{p,>R}^{-1}\rho_p\rangle$.

**The correction** (v14.176 §6, confirmed by audit v14.177 §6, and now
independently verified by reading the originals):

- v14.071 proves $S_{p,N}\succeq I$ for every $N\geq4000$ (nested remote
  Schur complement). Hence $\|\mathcal S_{p,>R}^{-1}\|\leq1$.
- v14.117 §1, which originally defines $\lambda_{p,R}$, states explicitly
  "$\lambda_{p,R}=\langle\rho_{p,R},\mathcal S_{p,>R}^{-1}\rho_{p,R}\rangle$,
  with the promoted remote floor $\mathcal S_{p,>R}\succeq I$" — directly
  citing v14.044/v14.071. I verified both passages by direct read.

The audit notes this is the same category of error v14.151 caught earlier
via counterexample: a floor on one eliminated block does not transfer to a
different block. I should have caught this — the $\gamma_Q$ work and the
remote-Schur work arose in the same session but govern different quantities.

**Re-quantified gap.** With the correct $\|\mathcal S_{p,>R}^{-1}\|\leq1$:
$\lambda_p\leq\|\rho_p\|^2\approx2\times10^{-6}$ against the $5\times10^{-9}$
budget gives $\sim400\times$ ($\approx2.6$ orders), not $10^{15}$. At 256k
($\|\rho\|^2\sim1.09\times10^{-6}$): $\sim218\times$ per parity. This matches
the audit's independent $\sim400$–$900\times$ and v14.119's original
$\sim898\times$. The obstruction is real but hundreds-fold, not $10^{15}$-fold.

v14.175's valid confirmations (trial numbers, weighted floors, budget
arithmetic) stand; only §4's operator identification and gap quantification
are corrected. No other v14.175 content is affected.

## 2. v14.176 256k certificates: independently replayed [V]

Downloaded the complete `exact_outward_run_37827949740` namespace (96 files,
83 base64 ZIP parts). Ran the replay wrapper with `--compare-reference`:

- **Byte-identical**: output SHA-256-matches the committed `outward_replay.json`.
- **All six targets pass** on both 256k rows
  (`all_rows_meet_all_six_numerical_targets_exactly: true`).
- **Caps confirmed** (from this thread's own run):

| Gate | even-v/256k | odd-v/256k | Ceiling |
|---|---|---|---|
| graph assembly | 6.154e-7 ✓ | 2.444e-10 ✓ | 1e-4 |
| mixed assembly | 1.798e-11 ✓ | 7.089e-15 ✓ | 1e-9 |
| scalar assembly | 5.253e-16 ✓ | 2.056e-19 ✓ | 1e-14 |
| graph residual | 1.460e-13 ✓ | 1.948e-14 ✓ | 1e-11 |
| source residual | 4.262e-18 ✓ | 5.645e-19 ✓ | 1e-15 |
| trace | 7.426e-28 ✓ | 2.755e-28 ✓ | 1e-20 |

All match v14.176 §2's table to displayed precision.

- **Paired interval** (128k→256k): $[-3.441392\times10^{-10},
  -3.440947\times10^{-10}]$, strictly negative ✓,
  $|\cdot|\leq9\times10^{-10}$ ✓ (exact rational comparison).
  Matches v14.176 §3.

## 3. Scope preserved

The corrected $\sim400\times$ gap does not close the infinite remainder —
it was never claimed to. As v14.176 §6 states: "It removes the spurious
15-order diagnosis, not the actual remaining theorem work." The open items
remain: transport from trial moments to the exact finite inverse, and the
correlated (not absolute) inverse-weighted parity estimate. The 256k octave
is now closed on actual data; the infinite tail is not.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[C] v14.175 §4 corrected: wrong operator used for }\|\mathcal S^{-1}\|.\\
&\qquad\text{Correct bound is }\|\mathcal S_{p,>R}^{-1}\|\leq1\text{ (v14.071),}\\
&\qquad\text{not }1/\gamma_Q.\text{ Real gap }\sim400\times,\text{ not }10^{15}.\\
&\text{[V] 256k witnesses replayed byte-identically; all caps and}\\
&\qquad\text{paired interval confirmed.}\\
&\text{[V] v14.176 §6 correction independently confirmed by direct}\\
&\qquad\text{reading of v14.044/v14.071/v14.117.}\\
&\text{No new obstruction beyond the known }\sim400\times\text{ trial gap.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.176
target: sandbox
status: closed
result: 256k frozen snapshots independently replayed byte-identically (96 files, all manifest hashes verified); all twelve caps and both trace bounds confirmed; paired 128k→256k interval confirmed strictly negative within 9e-10. §6's remote-Schur/full-Q correction independently verified by reading v14.044/v14.071/v14.117 directly — v14.175's operator identification was wrong and is corrected here; the valid portions of v14.175 are preserved. Real gap ~400x as stated.
constraints: None.
