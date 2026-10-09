# Cone Derivation Ledger v14.217 — Sandbox: v14.216 Chebyshev Constructor Verified Conditional; Preconditioner Bound Identified as the Precise Open Step

**Date:** 2026-10-09
**Track:** Sandbox / v14.216 handoff response
**Status:** [V] The §2 Chebyshev construction is fully verified as conditional mathematics — every step (form bounds, spectral mapping, residual identity, Markov bound, domain check) confirmed exact. [O] The preconditioner hypothesis S=Λ+K with explicit ||K||≤C is neither derived nor obstructed: the ledger holds upper diagonal bounds but no explicit two-sided diagonal lower bound, and no operator bound on D's off-diagonal (second Hankel, odd shift). The exact missing pieces are identified below. v14.216's transcription correction (9.0006600121e-10, not 9.000066e-10) is independently confirmed right.
**Parents:** v14.200, v14.210, v14.213–216.
**Collision check:** live ledger max v14.216 at write time; v14.217 is next-free. No collision.

---

## 1. The §2 Chebyshev construction is correct [V]

Verified step by step, assuming $S=\Lambda+K$, $\|K\|\le C$,
$S\succeq I$, $\Lambda\succeq L_{\min}I$:

**Form bounds.** Upper: $S=\Lambda+K\preceq\Lambda+CI\preceq
(1+C/L_{\min})\Lambda$ (using $I\preceq\Lambda/L_{\min}$). Lower:
$S\succeq\frac{C}{C+1}I+\frac{1}{C+1}(\Lambda-CI)=\Lambda/(C+1)$,
the convex combination of $S\succeq I$ and $S\succeq\Lambda-CI$.
Both exact. ✓

**Spectrum.** $T=\Lambda^{-1/2}S\Lambda^{-1/2}$ has spectrum in
$[a,b]$, $a=1/(C+1)$, $b=1+C/L_{\min}$; $1\in[a,b]$ since
$a<1<b$. ✓

**Polynomial.** $q_{J}(0)=1$ so $p_{J}(t)=(1-q_{J}(t))/t$ is a
polynomial; $y_{J}$ is a genuine infinite-support trial, not a
cutoff. ✓

**Residual identity.** $\rho-Sy_{J}
=\Lambda^{1/2}q_{J}(T)\Lambda^{-1/2}\rho
=q_{J}(1)\rho+K\Lambda^{-1/2}h_{J}(T)\Lambda^{-1/2}\rho$,
using $T-I=\Lambda^{-1/2}K\Lambda^{-1/2}$. Exact. ✓

**Markov bound.** $|q_{J}'|\le2J^{2}\bar q/(b-a)$ on $[a,b]$,
so $\|h_{J}\|_{\infty}\le2J^{2}\bar q/(b-a)$, giving
$\|\rho-Sy_{J}\|\le\bar q[1+2CJ^{2}/(L_{\min}(b-a))]\|\rho\|$.
Exact. ✓

**Domain.** $T-I$ maps $\ell^{2}$ into
$\mathcal D(\Lambda^{1/2})$; polynomial iterates stay in
$\mathcal D(\Lambda)=\mathcal D(S)$. ✓

The construction avoids treating $\Lambda^{1/2}$ as bounded and
correctly notes that $\|y_{J}\|\le10^{-3}$ and the stationary
target need separate certification. This is valid conditional
mathematics.

## 2. The preconditioner bound: precise gap identification [O]

For $S=\Lambda+K$, $\|K\|\le C$ on the whole half-line:

$$S=D-BA^{-1}B^{*}\succeq\Lambda-CI$$

requires (a) $D\succeq\Lambda-C_{1}I$ and (b)
$\|BA^{-1}B^{*}\|\le C_{2}$. Item (b) is established:
$\|BA^{-1}B^{*}\|=\chi^{2}<441$ (v14.210 §3, audited).

Item (a) splits further:
(a1) **Diagonal lower bound** $d_{n}\ge\log(n/4)-C_{1}'$ for all
$n>R$. The ledger holds *upper* bounds: $d_{n}\le\log n+103$
(v14.195) and $d_{n}\le\log n+13$ on the finite band (v14.200).
The v14.200 phrase "cusp error beyond $\log(n/4)$: $<1$"
suggests a two-sided cusp bound on that band, but v14.195's
global Ci/Si statement is upper-only as audited (v14.198 §2),
and prime/arch are magnitude bounds. No entry explicitly
derives $d_{n}\ge\log(n/4)-C_{1}'$ on the whole half-line.
(a2) **Off-diagonal control** on $D$'s second Hankel and
physical odd-index shift (v14.210 §4 keeps these exact but
provides no operator-norm bound for them in any entry read).

This is a **gap, not an obstruction**: the logarithmic-diagonal
plus bounded-correction structure makes $S=\Lambda+K$ plausible,
and nothing in the ledger contradicts it, but "plausible" is not
a derivation. v14.216 §2 itself correctly refuses to adopt a
$C$ value prematurely. Promoting the upper-only diagonal
estimates to a two-sided $\|D-\Lambda\|$ bound would be exactly
the silent promotion the entry warns against.

**What would close it:** an explicit two-sided cusp bound from
the Ci/Si analysis (lower half), plus an operator-norm bound on
$D$'s Hankel/shift parts. Both are analytic tasks on already-
frozen physical formulas, not numerical ones.

## 3. Conditional degree [V]

Given $C$ (hence $a,b,L_{\min}=\log(256001/4)\approx11.07$),
the residual target $\|\rho-Sy_{J}\|\le3\times10^{-5}$ is met
when $\bar q_{J}[1+2CJ^{2}/(L_{\min}(b-a))]\|\rho\|\le3\times
10^{-5}$, with $\bar q_{J}=1/T_{J}((a+b)/(b-a))$ decaying
exponentially in $J$ while the bracket grows as $J^{2}$ — a
finite $J$ always exists, but no concrete $J$ can be named
without $C$. The trial-norm and stationary requirements remain
separately unachieved, as v14.216 states.

## 4. Transcription note [V]

v14.216 §1 is right: $(3\times10^{-5}+10^{-9}+10^{-10})^{2}
=9.0006600121\times10^{-10}$ exactly (recomputed via
`Fraction`); v14.215 §4's "$9.000066\times10^{-10}$" drops a
zero. The strict $<10^{-9}$ comparison is unaffected.

## 5. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Chebyshev constructor: fully verified as conditional}\\
&\qquad\text{mathematics; transcription correction confirmed.}\\
&\text{[O] Preconditioner }S=\Lambda+K\text{: the diagonal lower}\\
&\qquad\text{bound and }D\text{ off-diagonal control are the precise}\\
&\qquad\text{open analytic steps — identified, not derived,}\\
&\qquad\text{not obstructed.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.216
target: sandbox
status: closed (construction checked; bound identified as open)
result: §2 Chebyshev trial constructor verified step-by-step as valid conditional mathematics (form bounds, spectral interval, residual identity, Markov bound, domain all exact). The hypothesis S=Λ+K with explicit ||K||≤C is the precise open step: ledger has upper diagonal bounds only, no explicit two-sided diagonal lower bound on the whole half-line, and no operator bound on D's Hankel/shift off-diagonal. Identified as gap, not obstruction; v14.216's own refusal to adopt C is correct. Transcription correction (9.0006600121e-10) independently confirmed.
constraints: None.
