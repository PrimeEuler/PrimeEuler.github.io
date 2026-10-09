# Cone Derivation Ledger v14.197 — Sandbox: v14.195 Transport and v14.196 Acceptance Consumer Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.195, v14.196 handoff responses
**Status:** [V] v14.195's cross-block bookkeeping, diagonal bound, nested-Schur energy transport, and η_new values verified; [V] v14.196's far lower bounds, zero-trial obstruction, corner consumer, and trial budget verified; no correction needed.
**Parents:** v14.025, v14.034, v14.044/v14.071, v14.171–176, v14.185–196.
**Collision check:** live ledger max v14.196 at write time; v14.197 is next-free. No collision.

---

## 1. v14.195: energy-weighted transport audited [V]

**Cross-block bookkeeping (§1).** The entry now supplies the full
derivation v14.194 requested: on each parity lattice $\|H\|\le\pi/2$
(rescaled integer-lattice Fourier multiplier $i(\theta-\pi)$,
$|\cdot|\le\pi$), $\|G\|\le\pi/2$ (v14.171 weighted Schur; even
entrywise-dominated by odd). With $\|Z\|\le11$: each of
$(ZH-HZ)$, $(ZG+GZ)$ has norm $\le11\pi$ **before** the $1/2$ factor,
$\le11\pi/2$ after; sum $\le11\pi$; times $c=2/\pi$ gives **22**.
Pole cross $<1$ ($|p(n)|\le2/n$, $|\alpha|=2$, $2\sqrt{8\cdot4/R}<1$
at $R=256000$). Total $\|B_{>R,\le R}\|<23$. The "22" bookkeeping
question from v14.194 §8 is now explicitly closed. ✓

**Diagonal bound (§2).** $d_{n}$ exact physical form verified
term-by-term: cusp $\le\log n+4$ (integration by parts:
$|{\rm Ci}|\le2/x$, $|{\rm Si}|\le\pi/2+2/x$), prime $<15$
(five weights $<1$, $\log q<2$, $1/k<1$), arch $<84$
($|h(t)|<21$ on $(0,2]$, integral $<21(2+2/k)<84$).
Sum: $d_{n}\le\log n+103$. With $T=2^{128}$:
$D_{\rm near}\le(\log T+137)I<(128+137)I<400I$. ✓
$T$ is proof-only; no matrix assembled.

**Energy transport (§3).** Nested-Schur identity
$D-B_{Q}C_{Q}^{-1}B_{Q}^{*}=S_{R}+E_{\rm protected}^{*}
 S_{\rm protected}^{-1}E_{\rm protected}\succeq I$
(v14.171 protected-positive argument at $R=256000$) gives
$\langle B_{\rm near}^{*}y,C_{Q}^{-1}B_{\rm near}^{*}y\rangle
 \le\langle y,D_{\rm near}y\rangle\le400\|y\|^{2}$,
hence $\|B_{\rm near}e\|\le\sqrt{400E}$ by duality —
avoiding $\|C_{Q}^{-1}\|=1/\gamma$. Far:
$|A(n,m)|\le28/n<32/n$ ($n>T>2R$), $\|B_{\rm far}\|_{HS}^{2}\le1024N/T$,
$\|B_{\rm far}e\|\le\sqrt{1024NE/(T\gamma)}$.
$\eta_{\rm new}=23\|W\|_{F}\|d\|+\sqrt{400E}+\sqrt{1024NE/(T\gamma)}$
is a valid whole-tail bound (near/far disjoint; summed
conservatively). ✓

**$\eta_{\rm new}$ values (§4).** Payload
`actual256-energy-weighted-source-transport.json` confirmed:
even $1.7511036592\ldots\times10^{-10}<1.751104\times10^{-10}$,
odd $5.5416722875\ldots\times10^{-12}<5.541673\times10^{-12}$,
both `eta_lt_2e_minus10_exact: true`. Improvement over v14.192:
$2.4\times10^{6}$ (even) / $5.6\times10^{5}$ (odd). ✓
This is a uniform source-norm bound, improving **both** the
$v_{p}$ charge and the $r_{p}$ charge in v14.190's contract —
stronger than v14.193's inner-product-only directional estimate,
as the entry notes.

## 2. v14.196: acceptance consumer audited [V]

**Far lower bounds (§1).**
$\|F\rho_{\star}\|\ge\|F\rho_{u}\|-\eta_{\rm new}$ by reverse
triangle; $\eta_{\rm new}\sim10^{-10}\ll\|F\rho_{u}\|\sim10^{-3}$,
so the transport correction is negligible at displayed precision:
$1.0898838307\times10^{-6}$ / $1.0878808700\times10^{-6}$, both
$>10^{-6}$ exactly. Closes the finite-inverse gap in v14.176's
certificates (subject to v14.195, now audited). Not a
$\lambda$-lower bound — correctly not claimed. ✓

**Zero-trial obstruction (§2).** $y=0\Rightarrow v=0$,
$r=\rho_{\star}$; any certified $E_{\rm even}\ge\|\rho_{\rm even}\|^{2}
>10^{-6}$ forces the box corner $(10^{-6},0)$ admissible.
$H(10^{-6},0)=10^{-6}(1-C_{S}K_{o})
 >10^{-6}(1-640\cdot2\times10^{-6})=0.99872\times10^{-6}
 >5\times10^{-9}$. Precisely scoped: a limitation of the
independent-box enclosure, not of $\Delta Q$ itself. ✓

**Corner consumer (§3).** 32-corner direct + 128-corner
$H_{0}$/remainder intersection; both polynomials multilinear
in box variables (extrema at corners); positivity clipping
valid; 3699 rational interior checks are consumer-arithmetic
checks, not a substitute for the corner theorem — correctly
stated. Nulls for missing trial data preserved. ✓

**Trial budget (§4).** Verified:
$E_{p}\le(3\times10^{-5}+3\times10^{-10})^{2}<10^{-9}$;
$|T_{e}|\le E_{e}$ (since $C_{S}(K_{o}+v_{o})<7.7\times10^{-3}<1$);
$|T_{o}|\le1.00768E_{o}$; $|T_{\rm cross}|\le6.4\times10^{-16}$;
total $\le2.9+1+1.00768+0.00000064=4.90768064\times10^{-9}
<5\times10^{-9}$. ✓ Sufficient, not necessary, as stated.
Current $\eta_{\rm new}$ already satisfies $\eta_{\rm total}\le2\times10^{-10}$
(even $1.75\times10^{-10}$ leaves $2.5\times10^{-11}$ assembly
allowance). The remaining open items are exactly as listed:
admissible $y_{p}$, $M(y_{p})$/$\delta$, represented $H_{0}$.

## 3. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] v14.195: 22/23 bookkeeping closed; diagonal}\\
&\qquad\le\log n+103;\ \eta_{\rm new}=1.75\times10^{-10}/
  5.54\times10^{-12}\\
&\qquad\text{confirmed from payload.}\\
&\text{[V] v14.196: far bounds }>10^{-6}\text{; zero-trial}\\
&\qquad\text{obstruction scoped; budget }<4.91\times10^{-9}\\
&\qquad\text{verified sufficient.}\\
&\text{No correction. Trial construction remains Lane A's.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.195
target: sandbox
status: closed
result: Logarithmic diagonal bound, explicit 22/23 cross-block bookkeeping (closing v14.194's question), nested-Schur energy transport, and η_new values all independently verified against the payload. No missing hypothesis found for use in the remote-trial contract.
constraints: None.

HANDOFF-ACK
from: v14.196
target: sandbox
status: closed
result: Upgraded far lower bounds, zero-trial box obstruction (precisely scoped), corner consumer logic, and sufficient trial budget all verified. No correction before numerical trial use. The budget is a concrete producer target; trial execution remains Lane A's.
constraints: None.
