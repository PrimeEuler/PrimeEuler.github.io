# Cone Derivation Ledger v14.187 — Sandbox: v14.185 Contract Audited; v14.186 Norm-One Obstruction Confirmed

**Date:** 2026-10-09
**Track:** Sandbox / v14.185, v14.186 handoff responses
**Status:** [V] v14.185's w1/C_D/diagonal derivations verified; archive matches v14.183-verified content; [C] minor arithmetic correction to v14.182's C_D numerical check; [V] v14.186's ||C||=1 proof and leakage/mismatch charges verified; [O] unweighted J-defect route confirmed unable to supply 256k reserve.
**Parents:** v14.016, v14.044/v14.071, v14.092/v14.096, v14.114/v14.117–119, v14.123, v14.147, v14.155–157, v14.165/v14.168, v14.174–v14.186.
**Collision check:** live ledger max v14.186 at write time; v14.187 is next-free. No collision.

---

## 1. v14.185 §§1–4: analytic contract audited [V]

**w1 as leading coupling (§1).** The limit $nA_p(n,m)\to-cz_m+\alpha_pL_pp_p(m)$
as $n\to\infty$ (fixed $m$) is verified: $z_n$ bounded so $z_nm/n\to0$;
the pole term $\alpha_pL_pp_p(m)/(1+t/n^2)\to\alpha_pL_pp_p(m)$ cleanly.
The decomposition $B_pA_{p,N}^{-1}B_p^*=M_{p,11}u_pu_p^*+\cdots$ is exact
once $E_p$ is defined; no cross term dropped. w1 uses every finite mode
and the full $A_{p,N}^{-1}$, as claimed. ✓

**C_D isolation (§§2–3).** Pole channel: odd-minus-even gives
$-32\cosh(1)/\pi^2$ (verified via $\cosh^2(1/2)+\sinh^2(1/2)=\cosh(1)$).
Parity-arch rank-one: $+16E_0/\pi^2$ from the exact off-diagonal identity
$D_{\rm par}$ (denominator removed before inequality; leftover bounded by
$32E_2/(\pi^4nm)(n^{-2}+m^{-2})$ with $E_2$ in closed form). Diagonal
completion via integration by parts matches the rank-one form on-diagonal.
Scope correctly limited: $C_D$ is the isolated pole/parity-arch component,
not the full bare-kernel asymptotic. ✓

**Numerical correction [C].** v14.182 §3 reported $C_D\approx-4.39646$ with
$16E_0\approx5.99814$. High-precision evaluation gives $16E_0=5.9958896$ and
$C_D=-4.3955856$. The audit's $E_0$ term was off by $\approx0.0023$.
The historical "$C_D\approx-4.396$" remains consistent (rounds correctly);
only v14.182's five-digit claim is corrected. v14.185 states the formula,
not a decimal, and is unaffected.

**Archive (§5).** The published
`research-notes/payloads/exact_leading_source_run_37838070444/` manifest
(18 files, same schema) matches the artifact verified byte-level in v14.183.
Lane A's fresh replay is a distinct check from v14.183's payload-integrity
verification; both stand.

## 2. v14.186: norm-one and leakage charges verified [V]

**||C||=1 (§1).** Upper bound from unitarity immediate. Lower bound via
$x_{s-1}=1/\sqrt{s}$: the integral comparison
$\sum_{s}f(s)\ge\int_1^{M+1}f$ with $f(s)=1/[\sqrt{s}(r+s)]$ gives
$(Hx)_{r-1}\ge(2/\sqrt{r})[\arctan\sqrt{(M+1)/r}-\arctan(1/\sqrt{r})]$;
restricting to $K\le r\le M/K$ yields
$\langle x,Hx\rangle/\|x\|^2\ge[\pi-4\arctan(1/\sqrt{K})]\times$
(harmonic ratio $\to1$); $M,K\to\infty$ gives $\|H\|\ge\pi$, hence
$\|C\|=\|H\|/\pi=1$. Translation-invariance extends to any half-line
origin. No cutoff decay. ✓

**Leakage fraction (§2).** For $u_a(j)=1/(a+2j)$: keeping $a$ terms,
$|(Cu_a)_r|>1/(6\pi a)$ per row, $\|Cu_a\|^2>1/(36\pi^2a)$;
with $1/(2a)\le\|u_a\|^2\le1/a^2+1/(2a)$ and $\pi<22/7$ (Machin),
ratio $\ge49a/[8712(a+2)]>1/180$ for $a\ge162$ (verified at 162, 32001,
256001). At $a=256001$: leakage $>1.0985\times10^{-8}>5\times10^{-9}$
reserve — exact rational comparison. ✓

**Mismatch (§3).** $\|Ju-u\|^2\ge[2-\|Gu\|/\|u\|]\|u\|^2$ from unitarity and
Cauchy–Schwarz; jump at $j=0$ included in $\|Gu_a\|^2$. Verified:
$a=256001$ gives $\|Gu\|/\|u\|\le7/2500$ hence
$\|Ju-u\|^2>3.900766\times10^{-6}$, $\approx2\times$ the source energy.
Treating $Ju$ as close to $u$ in unweighted $\ell^2$ is quantitatively
false. ✓

## 3. v14.186 handoff verdict: obstruction confirmed [O]

The handoff asks for "a concrete inverse-weighted cancellation that
bypasses these absolute defects or confirm that the unweighted
small-J-defect route cannot serve the 256k reserve."

**Confirmed: the unweighted route cannot serve the reserve.** The three
quantified defects — $\|C\|=1$ (no decay), leakage fraction $\ge1/180$
($>2\times$ reserve at 256k for the reference source), mismatch energy
$\ge3.9\times10^{-6}$ ($\approx780\times$ reserve) — are absolute,
cutoff-independent lower bounds. Summing unweighted norms as small errors
is ruled out by the entry's own exact rational comparisons.

No inverse-weighted cancellation is supplied in v14.186, and none is
constructible from the given material without the actual frozen residual
$\rho$ and the actual remote inverse $\mathcal S_{p,>R}^{-1}$ (per the
entry's own constraints: $u_a$ is a reference, not $\rho$). The bulk
conjugacy (v14.180, audited) remains correct; its physical transport
requires the weighted/correlation argument the entry explicitly defers.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] v14.185 contract: w1 limit, }C_D\text{ isolation/scope,}\\
&\qquad\text{diagonal completion all verified; archive matches.}\\
&\text{[C] v14.182's }C_D\approx-4.39646\text{ corrected to }-4.3955856\\
&\qquad\text{(formula unaffected; historical }-4.396\text{ stands).}\\
&\text{[V] v14.186: }\|C\|=1\text{ proved; leakage }\ge1/180\text{;}\\
&\qquad\text{mismatch }\ge3.9\times10^{-6}\text{ at 256k — all verified.}\\
&\text{[O] Unweighted J-defect route cannot supply the 5e-9 reserve;}\\
&\qquad\text{defects are absolute lower bounds, not small errors.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.185
target: sandbox
status: closed
result: Sections 1-4 audited against the primary source: w1 derivation, C_D pole/arch isolation and scope, diagonal cusp/arch completion all verified. One minor arithmetic correction to v14.182's numerical C_D check (-4.39646 -> -4.3955856); the formula and historical value are unaffected. Published archive matches v14.183-verified content. No correction to v14.185's mathematics.
constraints: None.

HANDOFF-ACK
from: v14.186
target: sandbox
status: closed
result: Norm-one Hilbert argument, exact leakage/mismatch charges all independently verified. Confirmed: the unweighted small-J-defect route cannot serve the 256k reserve — the defects are cutoff-independent lower bounds exceeding the reserve by orders of magnitude. No inverse-weighted cancellation is available from the given material; the weighted transport remains the open work as the entry states.
constraints: None.
