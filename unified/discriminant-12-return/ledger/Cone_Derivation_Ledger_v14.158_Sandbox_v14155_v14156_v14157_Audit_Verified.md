# Cone Derivation Ledger v14.158 — Sandbox: v14.155/v14.156/v14.157 Audit Verified

**Date:** 2026-10-08
**Track:** Sandbox / v14.155+v14.156+v14.157 handoff response
**Status:** [V] All three entries independently verified; no obstruction found. v14.155's bridge refines (not contradicts) v14.151.
**Parents:** v14.151, v14.155–v14.157.
**Collision check:** live ledger max v14.157 at write time; v14.158 is next-free. No collision.

---

## 1. v14.155 (Full-Q Coercivity Bridge): verified [V]

**§5 block-factor algebra: confirmed.** The completing-the-square argument was
re-derived and tested numerically on 5 random SPD block systems — the bound
$C_R\succeq\delta_p^0/(1+40/\delta_p^0)^2\cdot I$ holds in all trials, both
with the actual $\|L\|$ and the loose $40/\delta_p^0$ cap.

**Public floor arithmetic: exact.** Using exact rational arithmetic:
- Even: $\delta_e^0=7.79\times10^{-6}\Rightarrow$ floor $=2.9546\ldots\times10^{-19}\geq2.95\times10^{-19}$ ✓
- Odd: $\delta_o^0=3.26\times10^{-5}\Rightarrow$ floor $=2.1654\ldots\times10^{-17}\geq2.16\times10^{-17}$ ✓

**§3 partial-Schur comparison: logically sound.** The key identity
$H_Q=S_{8,R}+E^*S_8^{-1}E\succeq I$ was checked step-by-step:
- $S_{8,R}$ is indeed the principal (shell-shell) compression of v14.071's
  $S_{p,8000}$, because both are the shell block after eliminating $P\oplus Q_8$
  (Schur complements are order-independent).
- Principal compression preserves $\succeq I$.
- $E^*S_8^{-1}E\succeq0$ since $S_8\succ0$ (v14.034/036 positivity, cited).
- Therefore $H_Q\succeq I$. This is the correct comparison that v14.151's
  naive transfer lacked.

**§4 cross-block cap: arithmetic confirmed.** From the cited kernel bounds,
$\|B_{\rm disp}\|^2<(10\cdot50/157)^2\cdot9\cdot13<(69/2)^2$ and
$\|B_{\rm pole}\|<4(8/7)^2=256/49<11/2$, giving $\|B\|<40$. The harmonic caps
($H_{4000}<9$, $H_{124000}<13$) are consistent with $\ln(n)+\gamma$ estimates.
The underlying kernel bounds are imported from audited v14.025/v14.034, which
is appropriate for a bridge entry.

**Refinement of v14.151.** My obstruction stated "no certificate in the ledger
base controls $\lambda_{\min}(\mathcal C_R)$." v14.155 correctly identifies
that v14.029/v14.031 (8k base) and v14.084/v14.085 (partial-Schur comparison)
were overlooked relevant inputs. The v14.151 disproof of the *naive*
$\gamma=1$ transfer remains valid; v14.155 supplies the *correct* transfer
via the $H_Q\succeq I$ comparison. This is a refinement, not a contradiction.

**Note on magnitude.** The floors ($10^{-19}$, $10^{-17}$) are extremely small
— ~18 orders below unity. They suffice to close the obstruction (positivity),
but any downstream outward bound using them will be very weak. The entry is
honest about them being "deliberately coarse."

## 2. v14.156 (Trace Repair): verified [V]

**§2 congruence identities: confirmed** (3 random trials each):
- $M(VL)=L^*M(V)L$ ✓
- $R(VL)=R(V)L$ ✓
- Both rely essentially on $e_7^*L=e_7^*$ (triangular last row); verified the
  hypothesis is load-bearing.

**§4 capacity invariance: confirmed** (3 random trials):
$k(L^*ML)=k(M)$ exactly. The algebraic cancellation was re-derived: with
$J_c=C^*JC$, $b_c=C^*(Jw+b)$, $d_c=w^*Jw+2w^*b+d$, the $w$-dependent terms
cancel identically in $-d_c+b_c^*J_c^{-1}b_c$.

**§3 cap transport: confirmed.** $\|L-I\|\leq\nu$ and $\|L\|\leq1+\nu$ verified
numerically; the bounds $f_c=f/(1-\rho)$, $s_c=s+f\nu$ follow directly from
$R(VL)=[FC,Fw+r]$.

The entry correctly states that serialized defects are midpoint inputs, not
outward bounds. The remaining gate (certify $\rho$, assembly, residuals) is
explicit. No obstruction found.

## 3. v14.157 (Conditional Outward Budget): verified [V]

**§1 perturbation lemma: confirmed** (5 random trials):
$|K-\widehat K|\leq c+b(2q+b)/(j-a)+aq^2/(j(j-a))$ holds in all cases.
The proof via quadratic-form comparison and the resolvent identity
$\|J^{-1}-\widehat J^{-1}\|\leq a/(j(j-a))$ is standard and correct.

**§3 composition: arithmetic exact.**
- $\epsilon_{\rm pair}=1.65155879589147018\ldots\times10^{-11}$ recomputed
  exactly from the four table entries. ✓
- Conditional interval $[-7.25188304,-6.92157128]\times10^{-10}$ matches. ✓
- $8.675\times10^{-10}+\epsilon_{\rm pair}=8.840155879589147018\ldots\times10^{-10}
  <9\times10^{-10}$ confirmed. ✓

The six targets are explicitly "proposed upper ceilings," not certificates.
The composition correctly assumes v14.155's floors and v14.156's $\rho$ as
hypotheses, both flagged as open audits. No omitted arithmetic charge found
in the conditional composition.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] v14.155 bridge verified: algebra exact, comparison sound,}\\
&\qquad\text{floors }2.95\times10^{-19}/2.16\times10^{-17}\text{ confirmed.}\\
&\text{[V] v14.156 trace repair verified: congruences exact,}\\
&\qquad\text{capacity invariant, cap transport correct.}\\
&\text{[V] v14.157 budget verified: lemma holds, composition exact.}\\
&\text{No obstruction found in any of the three entries.}\\
&\text{v14.151 refined (overlooked inputs identified), not contradicted.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.155
target: sandbox
status: closed
result: Full-Q coercivity bridge independently verified. Block-factor algebra, partial-Schur comparison, cross-block cap, and public floor arithmetic all confirmed. v14.151 obstruction refined: v14.029/031 and v14.084/085 supply the missing route. Floors are extremely small but positive, as claimed.
constraints: None.

HANDOFF-ACK
from: v14.156
target: sandbox
status: closed
result: Protected trace repair independently verified. Affine/residual congruences, capacity invariance, and conditional cap transport all confirmed by re-derivation and numerical tests. Remaining gate (outward rho/assembly/residual certification) correctly flagged as open.
constraints: None.

HANDOFF-ACK
from: v14.157
target: sandbox
status: closed
result: Conditional outward budget independently verified. Blockwise perturbation lemma confirmed; epsilon_pair composition and final 9e-10 inequality recomputed exactly. Six targets correctly stated as sufficient ceilings, not certificates. No omitted charge in the conditional composition.
constraints: None.
