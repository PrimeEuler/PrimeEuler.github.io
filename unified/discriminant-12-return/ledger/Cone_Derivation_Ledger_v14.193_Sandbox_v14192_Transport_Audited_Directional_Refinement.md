# Cone Derivation Ledger v14.193 — Sandbox: v14.192 Transport Audited; Directional Energy-Weighted Refinement Derived

**Date:** 2026-10-09
**Track:** Sandbox / v14.192 handoff response
**Status:** [V] Trace repair, Q inequalities, cross-block norm 23, and η values all verified; [D] directional energy-weighted transport inequality derived (√γ improvement, no J-defect needed); η bounds confirmed too large for 5e-9 as stated — the refinement is the path forward, not yet executed.
**Parents:** v14.044, v14.071, v14.155–157, v14.173, v14.176, v14.185–192.
**Collision check:** live ledger max v14.192 at write time; v14.193 is next-free. No collision.

---

## 1. v14.192 claims verified [V]

**Trace repair.** $d=(LW)^{-1}(Lu-t)$, $x=u-Wd$ gives
$Lx=Lu-LWd=Lu-(Lu-t)=t$ exactly. Both parities' rational identities
confirmed in payload (`trace_repair_identity_exact: true`). ✓

**Q energy/norm inequalities.** With $e=x-x_{\star}\in Q$,
$C_{Q}e=Q(Ax-g)$, $C_{Q}\succeq\gamma I$:
- $\|e\|=\|C_{Q}^{-1}Q(Ax-g)\|\le s_{x}/\gamma$. ✓
- $\langle e,Ae\rangle=\langle e,QAQe\rangle
  =\|C_{Q}^{-1/2}w\|^{2}\le\|w\|^{2}/\gamma\le s_{x}^{2}/\gamma$
  ($w=Q(Ax-g)$). ✓ No unit floor assigned to $C_{Q}$, as stated.

**Cross-block $\|B_{>R,\le R}\|<23$.**
$(z_{n}m-nz_{m})/(n^{2}-m^{2})
 =\tfrac12[(z_{n}-z_{m})/(n-m)-(z_{n}+z_{m})/(n+m)]$.
Discrete Hilbert $1/(n-m)$ on parity lattice: norm $\pi/2$ (rescaled
integer-lattice multiplier). Hankel $1/(n+m)$: $\le\pi/2$.
With $|z|\le11$: each commutator/anticommutator $\le11\pi/2$;
$c=2/\pi$ gives $(2/\pi)(11\pi)=22$. Pole: $|p(n)|\le2/n$,
cross norm $<1$ (verified $128<R$ by squaring). Physical diagonal
contributes zero cross block. Total $<23$. ✓ Covers the original
physical kernel including both denominator channels; no bulk-$J$
approximation. ✓

**Transport $\eta$.**
$\rho_{\star}-\rho_{u}=-B_{>R,\le R}(x_{\star}-u)$ so
$\|\rho_{\star}-\rho_{u}\|\le23\|x_{\star}-u\|
 \le23(\|W\|_{F}\|d\|+s_{x}/\gamma)$.
Payload values: even $4.136512\times10^{-4}$,
odd $3.128345\times10^{-6}$ — confirmed from
`actual256-finite-trial-transport.json`. ✓

**Gate honesty.** These $\eta$ exceed $5\times10^{-9}$ by
$8\times10^{4}$ (even) / $6\times10^{2}$ (odd). The entry states this
plainly ("do not establish the 5e-9 gate"; "not an impossibility
result"). Confirmed: the bounds are valid but too conservative.

## 2. Directional energy-weighted refinement [D]

The v14.192 norm transport charges the full $\|e\|\le s_{x}/\gamma$
against $\|B\|$. But v14.190's contract needs $v_{p}$ (inner products
$\langle\rho_{p},y_{p}\rangle$), not $\|\rho_{p}\|$. Derive the sharper
directional bound.

**Theorem.** Let $w=u-x_{\star}=Wd+e$ with $e\in Q$,
$\langle e,Ae\rangle\le s_{x}^{2}/\gamma$. For any $y$:

$$|\langle\rho_{\star}-\rho_{u},\,y\rangle|
 \le\|W\|_{F}\|d\|\,\|B_{>R,\le R}\|\,\|y\|
   +\frac{s_{x}}{\sqrt{\gamma}}\,
     \langle B_{>R,\le R}^{*}y,\,
            A^{-1}B_{>R,\le R}^{*}y\rangle^{1/2}.$$

*Proof.* $\langle\rho_{\star}-\rho_{u},y\rangle
 =\langle Bw,y\rangle=\langle w,B^{*}y\rangle$.
Split $w=Wd+e$:
$|\langle Wd,B^{*}y\rangle|\le\|Wd\|\|B^{*}y\|
 \le\|W\|_{F}\|d\|\|B\|\|y\|$.
For the $e$-term, $A$-Cauchy–Schwarz:
$|\langle e,B^{*}y\rangle|
 =|\langle A^{1/2}e,A^{-1/2}B^{*}y\rangle|
 \le\langle e,Ae\rangle^{1/2}
   \langle B^{*}y,A^{-1}B^{*}y\rangle^{1/2}
 \le(s_{x}/\sqrt{\gamma})
   \langle B^{*}y,A^{-1}B^{*}y\rangle^{1/2}$. ∎

**Why sharper.** The $e$-contribution uses $s_{x}/\sqrt{\gamma}$
instead of $s_{x}/\gamma$ — improvement by $\sqrt{\gamma}$
($\approx5\times10^{-7}$ even, $\approx6\times10^{-7}$ odd).
The $Wd$-term is directly computable and tiny
($\|d\|\sim10^{-17}$ from trace repair).
No $J$-defect or unweighted smallness assumed.

**Cost.** Requires $M(y)=\langle B^{*}y,A^{-1}B^{*}y\rangle$,
a finite-dimensional quadratic form in the back-coupled vector
$B^{*}y$. This is computable once $y$ is specified
($B^{*}$ maps remote→finite; $A^{-1}$ acts on the finite front).
It replaces the uncomputable-in-practice $\|e\|\le s_{x}/\gamma$
with a $y$-dependent certified quantity.

**For v14.190's contract.** The $2\eta_{p}\|y_{p}\|$ charge on $v_{p}$
becomes:
$$|v_{p}-v_{p,\mathrm{rep}}|
 \le4\|W\|_{F}\|d\|\|B\|\|y_{p}\|
   +\frac{2s_{x}}{\sqrt{\gamma}}M(y_{p})^{1/2}
   +\|y_{p}\|\delta_{p},$$
halving the $\eta_{p}$-bottleneck by $\sqrt{\gamma}$ at the price of
evaluating $M(y_{p})$. Whether this closes 5e-9 depends on the trial
$y_{p}$ — not yet constructed.

## 3. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] v14.192: trace repair exact; Q inequalities,}\\
&\qquad\text{cross-block }<23\text{, and }\eta\text{ values verified.}\\
&\text{[V] }\eta\text{ honestly too large for 5e-9 (not an error).}\\
&\text{[D] Directional refinement: }s_{x}/\sqrt{\gamma}\text{ replaces}\\
&\qquad s_{x}/\gamma\text{ via }A\text{-Cauchy–Schwarz; no }J\text{ needed.}\\
&\text{Trial }y_{p}\text{ and }M(y_{p})\text{ remain open (Lane A).}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.192
target: sandbox
status: closed
result: All v14.192 claims independently checked — exact trace repair, finite-Q energy/norm inequalities, physical cross-block norm 23 (both denominator channels, original kernel), and payload η values (4.14e-4 / 3.13e-6) confirmed. No correction needed. Derived the optional sharper directional transport inequality: A-inner-product Cauchy–Schwarz gives √γ improvement over the norm transport for the v_p inner-product charge, requiring only the finite quadratic form M(y)=⟨B*y,A^{-1}B*y⟩. This is the concrete refinement path; trial construction remains Lane A's per the work split.
constraints: None.
