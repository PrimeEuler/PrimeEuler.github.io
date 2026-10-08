# Cone Derivation Ledger v14.167 — Sandbox: v14.165 Five-Cap Producer Audited

**Date:** 2026-10-08
**Track:** Sandbox / v14.165 handoff response
**Status:** [V] Carry-free convolution re-derived from first principles; scalar slack table verified; kernel symmetry and cap formulas checked. No obstruction.
**Parents:** v14.155–v14.166.
**Collision check:** live ledger max v14.166 at write time; v14.167 is next-free. No collision.

---

## 1. Carry-free signed convolution: re-derived from first principles [V]

v14.166 explicitly left this open ("not yet independently re-derived from
first principles by this thread"). Re-derived here:

**Scheme.** For signed integer families $a,b$, set $C_a=2^{\max{\rm bit\_length}(|a_i|)}$,
$a'_i=a_i+C_a\geq0$ (similarly $b'$). Pack into base-$B$ blocks with
$B=2^{8w}$ and multiply the packed integers.

**Carry-free bound.** $(a'*b')_k\leq(\text{terms})\cdot(2C_a)(2C_b)
\leq\min({\rm len})\cdot4C_aC_b$. Need $B>4C_aC_b\min({\rm len})$, i.e.
$8w>{\rm bit\_length}(\max|a|)+{\rm bit\_length}(\max|b|)+2+\log_2\min({\rm len})$.
Using ${\rm bit\_length}(\min({\rm len}))\geq\log_2\min({\rm len})$ (conservative)
plus $+1$ for strict inequality gives exactly v14.165 §2's formula. ✓

**Recovery.** $(a'_ib'_j)=(a_i+C_a)(b_j+C_b)
=a_ib_j+C_ab_j+C_ba_i+C_aC_b$. Summing over $i+j=k$:
$\sum a_ib_j=(a'*b')_k-C_a\sum b_j-C_b\sum a_i-C_aC_bN_k$.
v14.165's "subtract $C_b\sum(a_i)+C_a\sum(b_j)+C_aC_b\cdot\text{terms}$"
matches (note $C_b$ multiplies the $a$-sum). ✓

**Numerical test.** Random signed families: packed convolution recovers the
direct schoolbook result exactly. ✓

## 2. Scalar applicability bridge (§3): verified [V]

The slack table (audited decimal cap + reconstruction slack ≤ point-source cap):

| Family | Audited | Slack | Sum | Cap | ✓ |
|---|---|---|---|---|---|
| z | 5.88e-39 | 1e-39 | 6.88e-39 | 1e-38 | ✓ |
| d | 4.318e-37 | 1e-39 | 4.328e-37 | 4.4e-37 | ✓ |
| pole | 7.365e-40 | 1e-40 | 8.365e-40 | 1e-39 | ✓ |
| c | 6.74e-42 | 1e-41 | 1.674e-41 | 2e-41 | ✓ |

All round upward conservatively. The per-component slack (5e-40 for
$|x|<100$, etc.) is consistent with 41-significant-digit decimal
reconstruction. The bridge correctly identifies that audited caps apply to
`ld_string` output while the point operator uses exact binary hi+lo sums.

## 3. Point-source kernel: symmetry note [V with flag]

$A0_{ij}=(c_0/2)[(z_{0,i}-z_{0,j})T_{0,ij}-(z_{0,i}+z_{0,j})H_{0,ij}]
+\alpha p_{0,i}p_{0,j}$.

$H_{0,ij}=1/[2(i+j+a)]$ is symmetric in $i,j$ exactly. For $A_0$ symmetric,
need $T_{0,ji}=-T_{0,ij}$. If $T_0$ uses floor toward $-\infty$,
$T_{0,ji}={\rm floor}(-x)=-{\rm ceil}(x)\neq-{\rm floor}(x)$ in general —
exact antisymmetry requires the implementation to enforce it (compute for
$i>j$, set $T_{0,ji}=-T_{0,ij}$, or use symmetric rounding).

**This does not affect the certificate:** the kernel error bound
($<2^{-256}$ per entry, giving $\|A-A_0\|\leq\delta_A$) covers dyadic
approximation error regardless of rounding direction. The "symmetric exactly"
claim depends on implementation detail; the error charge does not. Flagged
for the record, not an obstruction.

The $\delta_A$ composition
($\delta_{\rm scalar}+22N\cdot2^{-256}$) and $\delta_g=N\cdot2^{-256}$ follow
the stated bounds correctly.

## 4. Projector and cap formulas (§4): structure verified [V]

$\|Qy_j\|^2=\|y_j\|^2-(P^*y_j)^*G^{-1}(P^*y_j)$ is the exact Euclidean
projector formula (verified algebraically). The five caps
($\alpha_J=\delta_AW_2+6r$, $\alpha_\beta=\delta_Awu+\delta_gw+6r$,
$\alpha_\eta=\delta_AU_2+2\delta_gu+r$, $f=f_0+\delta_Aw$,
$s=s_0+\delta_Au+\delta_g$) have the correct perturbation-theory structure:
operator error $\times$ norm products, plus source error charges, plus
$1e^{-100}$ serialization grid terms. The $6r$ factors correctly count the
$6\times6$ graph block entries.

## 5. Smoke replay: confirmed via audit [V]

v14.166 independently re-executed the frozen smoke replay byte-identically
(24/24 checks true, all cap values match v14.165 §5's table). This audit
does not duplicate that re-execution; the mathematical components above are
the independent contribution.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Carry-free convolution re-derived from first principles;}\\
&\qquad\text{bound formula, recovery, and numerical test all confirm.}\\
&\text{[V] Scalar slack table arithmetic verified (all four rows).}\\
&\text{[V] Kernel/projector/cap formulas structurally sound.}\\
&\text{[Flag] }A_0\text{ exact symmetry needs antisymmetric }T_0\text{ construction;}\\
&\qquad\text{error bound unaffected. Not an obstruction.}\\
&\text{No obstruction found. Actual 64k/128k pending CI as stated.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.165
target: sandbox
status: closed
result: Five-cap producer audited. Carry-free signed convolution independently re-derived (the piece v14.166 left open); scalar decimal-to-dyadic slack table verified; point-source kernel symmetry condition identified (implementation must enforce antisymmetric T0; error charge unaffected); projector and cap formulas structurally confirmed. No obstruction; actual-cutoff closure pending CI as stated.
constraints: None.
