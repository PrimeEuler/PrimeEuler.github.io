# Cone Derivation Ledger v14.190 — Sandbox: Actual-256k Paired Variational Enclosure Theorem and Input Contract

**Date:** 2026-10-09
**Track:** Sandbox / v14.189 variational handoff response
**Status:** [D] Variational enclosure theorem proved; exact H-identity and corner rule derived and rationally checked; minimal producer input contract with explicit 5e-9 acceptance inequalities; source/operator uncertainty charges derived. No numerical trial executed — this is the analytic architecture; Lane A owns residual-source certification.
**Parents:** v14.044, v14.071, v14.117, v14.155–157, v14.173, v14.176, v14.180, v14.185–189.
**Collision check:** live ledger max v14.189 at write time; v14.190 is next-free. No collision.

---

## 1. Variational identity for the remote inverse [D]

Let $\mathcal S_{p}=\mathcal S_{p,>R}\succeq I$ (v14.044/v14.071) on its
domain, $\rho_{p}$ the exact residual after eliminating the finite front.
For any trial $y_{p}\in\mathcal D(\mathcal S_{p})$ define

$$v_{p}=2\mathrm{Re}\langle\rho_{p},y_{p}\rangle
      -\langle y_{p},\mathcal S_{p}y_{p}\rangle,
\qquad
r_{p}=\rho_{p}-\mathcal S_{p}y_{p},
\qquad
\epsilon_{p}=\langle r_{p},\mathcal S_{p}^{-1}r_{p}\rangle.$$

**Theorem.** $\lambda_{p}=\langle\rho_{p},\mathcal S_{p}^{-1}\rho_{p}\rangle
=v_{p}+\epsilon_{p}$ with $0\le\epsilon_{p}\le\|r_{p}\|^{2}$.

*Proof.* Write $r_{p}=\rho_{p}-\mathcal S_{p}y_{p}$. Then
$\langle r_{p},\mathcal S_{p}^{-1}r_{p}\rangle
 =\langle\rho_{p},\mathcal S_{p}^{-1}\rho_{p}\rangle
  -2\mathrm{Re}\langle\rho_{p},y_{p}\rangle
  +\langle y_{p},\mathcal S_{p}y_{p}\rangle$
(using $\langle\mathcal S_{p}y_{p},
 \mathcal S_{p}^{-1}\mathcal S_{p}y_{p}\rangle
 =\langle y_{p},\mathcal S_{p}y_{p}\rangle$).
Rearranging gives $\lambda_{p}=v_{p}+\epsilon_{p}$.
Positivity: $\epsilon_{p}\ge0$ since $\mathcal S_{p}^{-1}\succeq0$.
Upper bound: $\epsilon_{p}\le\|\mathcal S_{p}^{-1}\|\,\|r_{p}\|^{2}
\le\|r_{p}\|^{2}$ since $\mathcal S_{p}\succeq I$. ∎

Thus $v_{p}$ is a computable variational lower bound; $\epsilon_{p}$ is the
controlled gap. Finite-dimensional exact rational check passed
($\lambda=5/6$, $v+\epsilon=5/6$ both optimal and non-optimal trials).

## 2. The $H$-correction identity [D]

For $H(a,b)=a-b-C_{S}(bK_{e}+aK_{o}+ab)$:

$$H(v_{e}+\epsilon_{e},v_{o}+\epsilon_{o})-H(v_{e},v_{o})
 =\epsilon_{e}[1-C_{S}(K_{o}+v_{o})]
  -\epsilon_{o}[1+C_{S}(K_{e}+v_{e})]
  -C_{S}\epsilon_{e}\epsilon_{o}.$$

*Proof.* Direct expansion; the cross terms
$-C_{S}(\epsilon_{e}v_{o}+v_{e}\epsilon_{o}+\epsilon_{e}\epsilon_{o})$
regroup exactly as stated. ∎ (Exact rational check passed.)

Since $\Delta Q=H(\lambda_{e},\lambda_{o})
=H(v_{e}+\epsilon_{e},v_{o}+\epsilon_{o})$, this separates the computable
signed quantity $H(v_{e},v_{o})$ from the gap corrections.

## 3. Exact outward corner rule [D]

**Inputs** (outward intervals; $E_{p}$ an upper bound for $\epsilon_{p}$):
- $C_{S}\in[c_{lo},c_{hi}]$, $0<c_{lo}$ (v14.185: $[639.817,639.839]$);
- $K_{e}\in[ke_{lo},ke_{hi}]$, $K_{o}\in[ko_{lo},ko_{hi}]$ (finite 256k);
- $v_{e}\in[ve_{lo},ve_{hi}]$, $v_{o}\in[vo_{lo},vo_{hi}]$ (trial stationary
  values, possibly negative);
- $0\le\epsilon_{p}\le E_{p}$.

**Rule.** Write $\Delta Q=H_{0}+T_{e}+T_{o}+T_{eo}$ with:
- $H_{0}=H(v_{e},v_{o})$: enclose by interval arithmetic; each product
  $[a_{lo},a_{hi}]\cdot[b_{lo},b_{hi}]$ via the 4-corner min/max, sums
  outward. (Multilinear terms attain extrema at corners.)
- $T_{e}=\epsilon_{e}\cdot[1-C_{S}(K_{o}+v_{o})]$: let
  $C^{e}=[1-c_{hi}(ko_{hi}+vo_{hi}),\,1-c_{lo}(ko_{lo}+vo_{lo})]$
  (outward; flip if $c_{lo}(ko_{lo}+vo_{lo})$ ordering inverts — use
  full 8-corner min/max for rigor). Then
  $T_{e}\in[\min(0,E_{e}C^{e}_{lo},E_{e}C^{e}_{hi}),
             \max(0,E_{e}C^{e}_{lo},E_{e}C^{e}_{hi})]$.
- $T_{o}=-\epsilon_{o}\cdot[1+C_{S}(K_{e}+v_{e})]$: analogous with
  $C^{o}=[1+c_{lo}(ke_{lo}+ve_{lo}),\,1+c_{hi}(ke_{hi}+ve_{hi})]$
  (8-corner for rigor).
- $T_{eo}=-C_{S}\epsilon_{e}\epsilon_{o}\in[-c_{hi}E_{e}E_{o},\,0]$.

Sum all four intervals outward to obtain $[H_{lo},H_{hi}]\ni\Delta Q$.
No sign or monotonicity assumption on $v_{p}$; $\lambda_{p}\ge0$ used only
via $\epsilon_{p}\ge0$.

**5e-9 acceptance.** The enclosure closes the working goal iff
$H_{hi}\le5\times10^{-9}$ **and** $H_{lo}\ge-5\times10^{-9}$.

## 4. Source and operator uncertainty charges [D]

Suppose Lane A certifies $\|\rho_{p}-\rho_{p,\mathrm{rep}}\|\le\eta_{p}$
and, where represented $\mathcal S$ arithmetic is used,
$\|(\mathcal S_{p}-\mathcal S_{p,\mathrm{rep}})y_{p}\|\le\delta_{p}$.

- **Stationary scalar:** with
  $v_{p,\mathrm{rep}}=2\mathrm{Re}\langle\rho_{p,\mathrm{rep}},y_{p}\rangle
   -\langle y_{p},\mathcal S_{p,\mathrm{rep}}y_{p}\rangle$,
  $$|v_{p}-v_{p,\mathrm{rep}}|
    \le2\eta_{p}\|y_{p}\|+\|y_{p}\|\delta_{p}.$$
  (First term: Cauchy–Schwarz on $2\mathrm{Re}\langle\rho_{p}-
   \rho_{p,\mathrm{rep}},y_{p}\rangle$. Second: quadratic-form
   operator-action charge.)
- **Residual norm:** with
  $r_{p,\mathrm{rep}}=\rho_{p,\mathrm{rep}}-\mathcal S_{p,\mathrm{rep}}y_{p}$,
  $$\|r_{p}\|\le\|r_{p,\mathrm{rep}}\|+\eta_{p}+\delta_{p},
  \qquad E_{p}=(\|r_{p,\mathrm{rep}}\|+\eta_{p}+\delta_{p})^{2}.$$

These are the explicit charges the handoff requests ($2\eta_{p}\|y_{p}\|$
for $v_{p}$; $\eta_{p}$ in the residual norm). All other physical terms
(second Hankel, varying diagonal, odd-index shifts, finite-front Schur
self-energy) reside inside the true $\mathcal S_{p}/\rho_{p}$ or their
certified charges $\delta_{p}/\eta_{p}$ — not dropped.

## 5. Minimal producer input contract

To execute the corner rule and test 5e-9, the producer (Lane A) supplies:

1. Outward finite intervals $[ke_{lo},ke_{hi}]$, $[ko_{lo},ko_{hi}]$ at 256k.
2. Outward $C_{S}$ interval (have: $[639.8173111086,639.8388534352]$).
3. Trial vectors $y_{p}\in\mathcal D(\mathcal S_{p,>R})$ with stated domain,
   near/far interface, and the computed $v_{p,\mathrm{rep}}$,
   $\|y_{p}\|$, $\|r_{p,\mathrm{rep}}\|$.
4. Certified $\eta_{p}$ (represented-to-exact residual transport) and
   $\delta_{p}$ (represented operator-action error on $y_{p}$), or the
   raw data to derive them.
5. Confirmation that $y_{p}$ trials do not reuse the unweighted
   small-$J$-defect shortcut (v14.186 obstruction).

Uncertified numerical values are diagnostics only, labeled as such.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Variational enclosure proved: }\lambda_{p}=v_{p}+\epsilon_{p},
  \ 0\le\epsilon_{p}\le\|r_{p}\|^{2}.\\
&\text{[D] }H\text{-identity verified exactly; outward corner rule}\\
&\qquad\text{derived with no sign/monotonicity assumptions.}\\
&\text{[D] Source charges: }2\eta_{p}\|y_{p}\|\text{ on }v_{p},
  \ \eta_{p}+\delta_{p}\text{ on }\|r_{p}\|.\\
&\text{Input contract + 5e-9 acceptance inequalities specified.}\\
&\text{No trial executed; residual certification remains Lane A's.}\\
&\text{Architecture cannot reduce certified quantities below the}\\
&\qquad\text{contract — if }\eta_{p},\delta_{p},E_{p}\text{ are too large,}\\
&\qquad\text{the obstruction is quantitative, not structural.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.189 (ledger variational handoff)
target: sandbox
status: closed
result: Variational enclosure theorem proved and exactly checked (finite-dimensional rational verification of both the v_p/epsilon_p decomposition and the H-correction identity). Outward box/corner rule derived with explicit interval formulas, no sign assumptions on v_p. Source/operator charges derived (2 eta_p ||y_p||, eta_p + delta_p). Minimal 5-item producer input contract and 5e-9 acceptance criterion specified. No numerical trial run — analytic architecture delivered; Lane A retains residual-source certification per the work split.
constraints: None.
