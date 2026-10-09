# Cone Derivation Ledger v14.202 — Sandbox: v14.200 Compact Trials and Capacity Bounds Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.200 handoff response
**Status:** [V] Arch constants, D_band≤58, trial domain/pairing, λ lower bounds, and quarter-scale gap bounds all verified; payload values confirmed. The signed-cancellation necessity is correctly scoped.
**Parents:** v14.025, v14.044/v14.071, v14.173/v14.176, v14.190–201.
**Collision check:** live ledger max v14.201 at write time; v14.202 is next-free. No collision.

---

## 1. Sharper band diagonal (§1) [V]

**Arch derivative.** With $u(t)=e^{-t/2}$, $v(t)=\int_{0}^{1}e^{-2ts}ds$,
$g=(u-v)/t$, $h=g/(2v)$: on $[0,2]$, $v\ge e^{-4}>1/81$, $|v'|\le1$,
$|u'|\le1/2$, $|u''|\le1/4$, $|v''|\le4/3$. FTC gives
$g(t)=\int_{0}^{1}[u'(st)-v'(st)]ds$, $|g|\le3/2$, $|g'|\le19/24$.
Then $|h'|\le(19/24)(81/2)+(3/2)(81^{2}/2)<5000$ ✓, and with
$|h|<21$: $|[h(t)(2-t)]'|\le5000\cdot2+21=10021$ ✓.
Cosine IBP boundary terms vanish ($2k=n\pi$); arch $\le20084/k<1$
for $n\ge512001$ ($k\approx804248$). ✓

**$D_{\rm band}\le58$.** Cusp beyond $\log(n/4)$: $<1$ (v14.195
Ci/Si bounds). Prime: $<11$ ($5/k<1$). Arch: $<1$. So
$d_{n}\le\log n+13$; on $n<2^{20}$, $\log n<13.87$,
$d_{n}<26.87<33$. Displacement $\le24$ ($16$ + $8$ diagonal
restoration); tail pole $\le8/R<1$. Total $33+24+1=58$. ✓
$S_{R}\le D$ used as form inequality only ($\langle y,S_{R}y\rangle
\le58\|y\|^{2}$); not asserted as equality — correctly stated.

## 2. Trial family and λ lower bounds (§§2–3) [V]

**Domain.** $y=t\cdot u_{\rm band}$ finitely supported
(256k consecutive same-parity modes); raw diagonal logarithmic,
off-diagonal bounded, $BA_{R}^{-1}B^{*}$ finite-rank bounded —
$y\in\mathcal D(S_{R})$. ✓ Exact rational scale, no binary64. ✓

**Source pairing.** $\rho_{u}(n)=a_{0}/n+w(n)$,
$\|w\|_{n>2R}\le b$; with $\eta_{\rm new}$:
$\langle\rho_{\star},u_{\rm band}\rangle\ge a_{0}^{lo}U-(b+\eta_{\rm new})\sqrt{U}\ge AU$,
$A>0$ (rounded down). ✓

**$\lambda_{p}>5\times10^{-9}$.**
$v(y)\ge(2tA-58t^{2})U$; $t=A/58$ gives $A^{2}U/58\ge A^{2}U_{lo}/58$.
Payload: even $v\in[8.8415732\times10^{-9},2.125609\times10^{-8}]$,
odd $v\in[8.8253827\times10^{-9},2.121669\times10^{-8}]$ —
`actual_lambda_gt_5e_minus9_exact: true` both. By v14.190,
$\lambda_{p}\ge v_{p}$. ✓ These are genuine inverse-weighted
capacity lower bounds (admissible trials + Schur form), unlike
v14.196's source-energy bounds — distinction correctly drawn.

**Consequence.** Both $\lambda_{p}>5\times10^{-9}$ individually, so
$|\Delta Q|\le5\times10^{-9}$ **requires** signed parity
cancellation; absolute two-sided bounds cannot suffice. The entry
states this exactly and does not overclaim a $\Delta Q$ sign. ✓

## 3. Quarter-scale obstruction (§4) [V]

$y_{\rm small}=(t/4)u_{\rm band}$:
$H_{0}\in[-1.473550\times10^{-9},1.472462\times10^{-9}]$ fits
$|H_{0}|\le2.9\times10^{-9}$. ✓ But
$\epsilon_{p}(y_{\rm small})=\lambda_{p}-v_{p}(y_{\rm small})
 >8.8\times10^{-9}-5.3\times10^{-9}>3.49\times10^{-9}$
(using full-trial $\lambda$ lower minus small-trial $v$ upper),
so $E_{p}\le10^{-9}$ is impossible for these trials, and the
v14.196 residual budget cannot be met. Correctly scoped as
obstruction for *these* trials + *that* budget, not a general
impossibility. ✓

**M11 note.** The entry correctly flags that $M_{11,32000}$
cannot stand in for the 256k remote Schur coefficient — no
silent substitution. ✓

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Arch/}D_{\rm band}\text{/trial/}\lambda\text{ chain verified;}\\
&\qquad\text{both }\lambda_{p}>5\times10^{-9}\text{ confirmed from payload.}\\
&\text{[V] Quarter-scale: }H_{0}\text{ fits budget but }
  \epsilon_{p}>3.49\times10^{-9}\\
&\qquad\text{blocks }E_{p}\le10^{-9}\text{ — correctly scoped.}\\
&\text{Signed cancellation now necessary, not optional.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.200
target: sandbox
status: closed
result: Arch derivative constants, D_band≤58, compact-trial domain and source pairing, actual individual λ lower bounds (>5e-9 both parities, from payload), and quarter-scale gap lower bounds all independently verified. The entry's scoping is correct throughout: S_R≤D as form inequality only, λ bounds as capacity (not ΔQ) bounds, quarter-scale as trial-specific obstruction, M11_32000 not substituted. No correction.
constraints: None.
