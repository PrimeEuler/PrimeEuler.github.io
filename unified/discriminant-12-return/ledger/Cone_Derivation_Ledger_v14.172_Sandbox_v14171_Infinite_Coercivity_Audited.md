# Cone Derivation Ledger v14.172 — Sandbox: v14.171 Uniform Infinite Full-Q Coercivity Audited

**Date:** 2026-10-08
**Track:** Sandbox / v14.171 handoff response
**Status:** [V] Uniform Hilbert cross-block proof independently verified step-by-step; physical-kernel indexing, pole bound, partial-Schur comparison, and both public floors confirmed; reproducer byte-identical. No obstruction.
**Parents:** v14.025, v14.034/v14.036, v14.044/v14.071, v14.155/v14.158/v14.161, v14.168–v14.171.
**Collision check:** live ledger max v14.171 at write time; v14.172 is next-free. No collision.

---

## 1. Hilbert norm bound: verified from first principles [V]

The analytic proof in v14.171 §2 is correct:

- **Convexity.** $f_a(t)=t^{-1/2}/(a+t)$, $a=r+1/2>0$:
  $f_a''(t)=(3a^2+10at+15t^2)/(4t^{5/2}(a+t)^3)>0$. All numerator
  coefficients positive; denominator positive. ✓
- **Row sums.** Midpoint Jensen on each $[j,j+1]$:
  $f_a(j+1/2)\leq\int_j^{j+1}f_a$. Summing:
  $\sum_j w_j/(r+j+1)\leq\int_0^\infty dt/(\sqrt{t}(a+t))$.
  The integral: $t=as^2$ gives $(2/\sqrt{a})\arctan|_0^\infty=\pi/\sqrt{a}
  =\pi w_r$. Independently recomputed. ✓
- **Schur test.** Weighted Cauchy–Schwarz:
  $|(Hx)_r|^2\leq(\sum_jH_{rj}w_j)(\sum_jH_{rj}|x_j|^2/w_j)$.
  Row bound $\sum_jH_{rj}w_j\leq\pi w_r$ and column bound (by symmetry)
  $\sum_rH_{rk}w_r\leq\pi w_k$ give
  $\sum_r|(Hx)_r|^2\leq\pi^2\sum_k|x_k|^2$. Hence $\|H\|\leq\pi$,
  for every rectangular compression and the infinite operator
  (monotone truncation; no $\ell^2$ assumption on weights). ✓
- The endpoint singularity at $t=0$ is integrable
  ($\int_0^1t^{-1/2}dt=2$); Jensen on $[0,1]$ follows by truncation
  as stated. ✓

## 2. Physical-kernel indexing and entrywise domination [V]

- $|z_n|\leq10$ (finite front v14.034 + all $n\geq8000$ v14.025 — both
  audited inputs, not re-derived here).
- $\left|\frac{2}{\pi}\frac{z_nm-nz_m}{n^2-m^2}\right|
  \leq\frac{20}{\pi}\frac{|n|+|m|}{|n-m||n+m|}
  =\frac{20}{\pi|n-m|}$ for $n,m>0$ (where $|n|+|m|=|n+m|$). ✓
- Same-parity gap $|n-m|=2(r+j+1)$ with $r=3999-i$ (reversed front
  index) and $j\geq0$ (shell index): the front/shell decomposition is
  as stated; the factor 2 is the same-parity mode spacing.
- Entrywise: $|B_{\rm disp}(r,j)|\leq\frac{10}{\pi}H(r,j)$, so
  $\|B_{\rm disp}\|\leq\frac{10}{\pi}\|H\|\leq10$, finite or infinite. ✓

## 3. Pole block and total cross bound [V]

- $\cosh(1/2)=1.12763<8/7=1.14286$ (independently computed). ✓
- $4\cosh^2(1/2)=5.086<256/49=5.224$. ✓
- $\|B\|<10+256/49=746/49=15.224<16$, uniformly for all $R\geq8000$
  and the infinite shell. ✓
- Orthogonal restriction to Q8 cannot increase norms (stated;
  standard). ✓

## 4. Infinite partial-Schur comparison [V]

$H_Q=D-B^*C_8^{-1}B=S_{8,\infty}+E^*S_8^{-1}E\succeq I$ on the shell
domain. This reuses the audited v14.155 bridge structure with:
- $C_8\geq\delta_pI$ ($\delta_e=7.79\times10^{-6}$,
  $\delta_o=3.26\times10^{-5}$, audited v14.158),
- protected-positive $S_8$ (v14.034/v14.036),
- $S_{8,\infty}\geq I$ (nested remote v14.044/v14.071).
The new content is that the uniform $\|B\|<16$ makes the finite-dimensional
inverse/shear maps bounded on the infinite form domain; closedness extends
the estimate. The proof does not identify the full-Q operator with the
remote operator (explicitly disclaimed). No missing hypothesis found.

## 5. Coercivity floors: independently recomputed [V]

Completing the square with $L=C_8^{-1}B$, $\|L\|<16/\delta_p$:
$\langle C(x,y),(x,y)\rangle\geq\delta_p(\|x+Ly\|^2+\|y\|^2)
\geq\frac{\delta_p}{(1+16/\delta_p)^2}(\|x\|^2+\|y\|^2)$.
The shear lemma $(1+c)^2(u^2+v^2)\geq(u+cv)^2+v^2$ verified:
difference $=2c(u^2-uv+v^2)+c^2u^2\geq0$. ✓

| Sector | $\delta_p$ | Derived floor | Public floor | $>$ public? |
|---|---|---|---|---|
| even | 7.79e-6 | 1.847e-18 | 1.84e-18 | ✓ |
| odd | 3.26e-5 | 1.353e-16 | 1.35e-16 | ✓ |

Both match v14.171 §3 to displayed precision; exact $>$ public confirmed
by the reproducer's Fraction comparison.

## 6. Reproducer: byte-identical [V]

Ran `suzuki_infinite_fullq_coercivity_bridge.py` from scratch: output is
SHA-256-identical to the frozen
`payloads/infinite_fullq_bridge_v14_171/infinite_fullq_bridge.json`.
The script checks coefficient positivity, the $\cosh$ bound, floor
rounding-down, and three independent exact finite block examples
(random seeds 31/107/211, PSD verified). All pass.

## 7. Scope: correctly stated [V]

v14.171 proves **uniform infinite full-Q coercivity** — a necessary
ingredient. It explicitly does **not** close the infinite capacity
remainder $Q_\infty-Q_R$ (v14.114/v14.117 correlated physical correction),
which needs the K10 far-residual expansion with frozen finite solution
and exact octave correlation. The entry is honest about this boundary:
"Neither the improved full-Q floor nor a successful finite 256k interval
alone closes this quantity." No overclaim found.

## 8. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Hilbert bound }\|H\|\leq\pi\text{ verified via midpoint}\\
&\qquad\text{convexity + weighted Schur; integral recomputed.}\\
&\text{[V] Physical kernel indexing and }\|B_{\rm disp}\|\leq10\text{ confirmed.}\\
&\text{[V] Pole bound and total }\|B\|<16\text{ confirmed.}\\
&\text{[V] Infinite partial-Schur comparison sound on audited inputs.}\\
&\text{[V] Both public floors recomputed; reproducer byte-identical.}\\
&\text{[V] Scope honest: coercivity closed, capacity remainder still open.}\\
&\text{No obstruction. No missing hypothesis before theorem-grade reuse}\\
&\text{of the uniform coercivity itself.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.171
target: sandbox
status: closed
result: Uniform Hilbert cross-block proof independently verified from first principles (convexity, integral, Schur test all recomputed); physical-kernel indexing and entrywise domination confirmed; pole/total bounds confirmed; infinite partial-Schur comparison checked against audited inputs; both public full-Q floors recomputed and match; reproducer byte-identical. No missing hypothesis; no obstruction. The still-open infinite capacity remainder is correctly scoped as separate work.
constraints: None.
