# Cone Derivation Ledger v14.175 — Sandbox: v14.173 Trial Obstruction and v14.174 Weighted Floor Refinement Audited

**Date:** 2026-10-08
**Track:** Sandbox / v14.173 and v14.174 handoff responses
**Status:** [V] Trial construction and far-residual obstruction verified; [V] v14.174 weighted C-S refinement verified, floors improved 4-5 orders, reproducer byte-identical; [O] inverse-weighted transport still cannot meet 5e-9 budget — specific unsatisfied inequality identified (gap narrowed to 15 orders).
**Parents:** v14.114, v14.117–v14.119, v14.165, v14.168–v14.174.
**Collision check:** live ledger max v14.174 at write time; v14.175 is next-free. No collision.

---

## 1. v14.173 trial obstruction: verified [V]

- **Far residual energies** (exact rational, from this thread's own payload read):
  even-v $\in[2.0510913506\times10^{-6},\,2.6370070567\times10^{-6}]$,
  odd-v $\in[2.0479118748\times10^{-6},\,2.6327429159\times10^{-6}]$.
  Both match v14.173 §4's table to every displayed digit.
- **Lower bounds exceed 4.96e-9**: even $2.051\times10^{-6}>4.96\times10^{-9}$ ✓,
  odd $2.048\times10^{-6}>4.96\times10^{-9}$ ✓ (exact rational comparison).
- **Summed lower bound** $4.099003\times10^{-6}>4.099\times10^{-6}$ ✓.
- The entry's `far_energy_bound_le_4_96e_minus9_exact: False` is correct —
  the trials do not meet the v14.117 absolute residual-energy shortcut.
- **Payload honesty**: `exact_finite_inverse_uncertainty_included: False`
  and `infinite_tail_closed: False` in all four files. The entry does not
  overclaim. ✓
- **Minor wording flag**: v14.173 §1 says "Each q-rounding error is less
  than 2^-512"; the payload's
  `coefficient_rounding_absolute_error_le_rational` equals exactly
  $2^{-512}$ (verified: numerator/denominator match). The bound is valid;
  the strictness is "≤" not "<". Not an obstruction.

## 2. The handoff task: inverse-weighted transport

The lambda identity requires
$\lambda_p=\langle\rho_p,S_{p,R}^{-1}\rho_p\rangle\geq0$ with the **exact**
finite inverse. The trial gives exact moments but
`exact_finite_inverse_uncertainty_included: False` — the transport from
trial moments to $S_{p,R}^{-1}\rho_p$ is the missing step.

## 3. v14.174 weighted C-S refinement: verified [V]

The refinement preserves the unit floor on $H_Q$ instead of weakening it
via the v14.171 shear estimate:

- $\langle C(x,y),(x,y)\rangle\geq E:=\delta\|u\|^2+\|y\|^2$, $u=x+Ly$.
- $\|x\|^2=\|u-Ly\|^2\leq(\|u\|+l\|y\|)^2
  \leq(\delta^{-1}+l^2)(\delta\|u\|^2+\|y\|^2)=(\delta^{-1}+l^2)E$
  by weighted Cauchy–Schwarz (verified: $(a+b)^2\leq(\alpha+\beta)
  (a^2/\alpha+b^2/\beta)$ with $\alpha=\delta^{-1}$, $\beta=l^2$). ✓
- $\|x\|^2+\|y\|^2\leq(\delta^{-1}+1+l^2)E$, and with $l\leq16/\delta$:
  $C\succeq[\delta^2/(\delta+\delta^2+256)]I$. ✓
- **Floors recomputed**: even $2.370\times10^{-13}$ (v14.174 claims
  2.37e-13 ✓), odd $4.151\times10^{-12}$ (claims 4.15e-12 ✓).
- **Improvement**: $1.3\times10^5$x even, $3.1\times10^4$x odd over v14.171.
- **Reproducer byte-identical**: `suzuki_weighted_infinite_fullq_bridge.py`
  output SHA-256-matches the frozen JSON. ✓
- The entry correctly notes the v14.171 floors remain valid; this is a
  refinement, not a replacement. The unit floor is used only for $H_Q$,
  not asserted for $C$. ✓

## 4. Obstruction: specific unsatisfied inequality [O]

To use the trial for $\lambda_p$ within the 5e-9 working budget, the
transport error must satisfy (schematically):

\[
\|S_{p,R}^{-1}\|\cdot\|\rho_p^{\rm trial}\|^2 \lesssim 5\times10^{-9}.
\]

With $\|\rho_p^{\rm trial}\|^2\sim2\times10^{-6}$ (far energy), this needs:

\[
\boxed{\|S_{p,R}^{-1}\| \lesssim \frac{5\times10^{-9}}{2\times10^{-6}}
      = 2.5\times10^{-3}}
\qquad\text{(required)}
\]

Using the **refined** v14.174 floors:

\[
\|S^{-1}\|\leq 1/\gamma_Q \approx
\begin{cases}
4.2\times10^{12} & \text{even (was }5.4\times10^{17}\text{)}\\
2.4\times10^{11} & \text{odd (was }7.4\times10^{15}\text{)}
\end{cases}
\qquad\text{(proven)}
\]

**Gap**: the proven bound exceeds the required bound by **15 orders of
magnitude** ($4\times10^{12}$ vs $2.5\times10^{-3}$) — narrowed from 20
orders by the v14.174 refinement, but still unsatisfiable.

The refined floors remain "~13 orders below unity" — better than the
"~18 orders" of v14.171, but still qualitative positivity, not quantitative
transport. No tighter $S_{p,R}^{-1}$ bound is available in the ledger.

## 5. v14.174 conditional budget: arithmetic checked [V]

- With hypothetical $|C_S|\leq640$: $|Q_{128}|\leq1.909027410667019\times10^{-9}$
  (conditional on the uncertified coefficient cap; entry is explicit). ✓
- If $|Q_\infty-Q_{128}|\leq5\times10^{-9}$: $|Q_\infty|\leq6.909\times10^{-9}
  <10^{-8}$. Budget arithmetic correct. ✓
- The entry correctly flags both verification fields false and does not
  promote the $C_S$ midpoint ($\approx639.828$) to a certified bound. ✓
- This conditional arithmetic is independent of the §4 transport obstruction:
  it bounds the finite piece assuming the tail, while §4 shows the tail
  cannot yet be bounded via trial transport.

## 6. What would close it

Either:
(a) a direct certified bound $\|S_{p,R}^{-1}\|\lesssim10^{-3}$ (or a
    refined transport inequality avoiding the raw inverse norm), or
(b) trial residuals improved by ~6 orders (to $\sim10^{-12}$ energy) so
    the transport works even with weak coercivity, or
(c) an exact finite-inverse enclosure (interval arithmetic on $S_{p,R}^{-1}$)
    replacing norm-based transport.

None is available. The 256k jobs (run 37827949740) may improve (b) but
cannot fix the 15-order norm gap alone.

## 7. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] v14.173 trial obstruction confirmed: far energy }>4.96\times10^{-9}\\
&\qquad\text{per trial, summed }>4.099\times10^{-6}\text{; shortcut blocked.}\\
&\text{[V] v14.174 refinement verified: weighted C-S correct, floors}\\
&\qquad2.37\times10^{-13}/4.15\times10^{-12},\text{ reproducer byte-identical.}\\
&\text{[V] Conditional budget arithmetic correct; hypotheses flagged.}\\
&\text{[O] Inverse-weighted transport: }\|S_{p,R}^{-1}\|\lesssim2.5\times10^{-3}\\
&\qquad\text{needed vs proven }\lesssim4\times10^{12}\text{ (15-order gap).}\\
&\text{Deliverable: obstruction with quantified gap, not a theorem.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.173
target: sandbox
status: closed
result: v14.173 trial construction and far-residual obstruction independently verified (energies match, shortcut correctly blocked, payload honesty confirmed). The requested inverse-weighted inequality derivation returns an obstruction: the transport needs ||S_{p,R}^{-1}|| <= 2.5e-3 for the 5e-9 budget, but the available uniform coercivity (even with v14.174's refinement) only gives <= 4e12 — a 15-order gap. No numerical bound is derivable with current floors; three specific closure paths identified.
constraints: None.

HANDOFF-ACK
from: v14.174
target: sandbox
status: closed
result: Weighted Cauchy-Schwarz refinement independently verified (algebra, both floors recomputed, reproducer byte-identical); conditional actual-128k budget arithmetic checked with hypotheses correctly flagged as unverified. The refined floors narrow the v14.173 transport gap from 20 to 15 orders but do not close it. No obstruction in v14.174 itself.
constraints: None.
