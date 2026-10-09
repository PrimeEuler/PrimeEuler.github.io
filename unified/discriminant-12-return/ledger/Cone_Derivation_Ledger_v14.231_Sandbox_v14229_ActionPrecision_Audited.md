# Cone Derivation Ledger v14.231 — Sandbox: v14.229 Action-Precision z Evaluator Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.229 handoff response
**Status:** [V] Payload SHA-256 matches (44537 bytes); order-8 Euler–Maclaurin remainder verified (B8 coefficient sum 12.7<13, integral bound b^-8); four exponential moments with S8<9.23e6<1e7; combined analytic remainder <7.150e-42; 56-term sine Taylor <1.127e-85; z-only model action charge <5e-26 verified via rationals; default source mode byte-identical to v14.227; 50 diagnostics pass. No correction.
**Parents:** v14.195, v14.210, v14.223–230.
**Collision check:** live ledger max v14.230 at write time; v14.231 is next-free. No collision.

---

## 1. Order-8 digamma remainder (§2) [V]

$B_{8}(t)=t^{8}-4t^{7}+(14/3)t^{6}-(7/3)t^{4}+(2/3)t^{2}-1/30$.
Coefficient absolute sum:
$1+4+14/3+7/3+2/3+1/30=12.7<13$ — recomputed exactly. ✓

$\int_{0}^{\infty}|w+t|^{-9}dt\le b^{-8}\int_{0}^{\infty}
(1+s^{2})^{-9/2}ds\le b^{-8}$ since $(1+s^{2})^{-9/2}\le
(1+s^{2})^{-3/2}$ (integrates to 1) — verified. ✓

Hence digamma error $<13\cdot b^{-8}=13(4/(n\pi))^{8}
<13(4/(3n))^{8}$ using $\pi>3$. ✓

The five alternating $\atan$ terms with $x^{11}/11$ interval
remainder, directed rational complex arithmetic — standard
sound enclosures. ✓

## 2. Exponential moments and S8 bound (§3) [V]

$1/(a^{2}+k^{2})=\sum_{r=0}^{3}(-1)^{r}a^{2r}/k^{2r+2}+
a^{8}/[k^{8}(a^{2}+k^{2})]$ — exact identity. ✓

Moments $S_{0},S_{2},S_{4},S_{6}$ via Stirling numbers and
binomial expansion — standard formulas. ✓

$S_{8}$: $a_{j}=2j+1/2\le2(j+1)$; $(j+1)^{8}\le8!\binom{j+8}{8}$;
with $e^{-1}<1/2$, $q<1/16$:
$S_{8}<128\cdot8!/(1-q)^{9}<128\cdot8!(16/15)^{9}\approx
9.23\times10^{6}<10^{7}$ — recomputed. ✓

Physical correction remainder $<1024S_{8}/(n^{9}\pi^{9})
<1024\cdot10^{7}/(3^{9}n^{9})$ — verified. ✓

Combined: $13(4/(3R))^{8}+1024\cdot10^{7}/(3^{9}R^{9})
\approx7.150\times10^{-42}$ — recomputed exactly, matches
payload. ✓

Nine exact rational direct-denominator checks verify the
four-term remainder identity (per entry). ✓

## 3. Action-precision intervals and charge (§§4–5) [V]

56-term sine: rounding $\le56\cdot16^{56}2^{-B}$,
remainder $4^{113}/113!$; sum $<1.127\times10^{-85}$ at
$B\ge512$ — verified. Phase $<21\cdot2^{-256}<10^{-70}$. ✓

Uniform radius $<10^{-39}$: payload confirms. ✓

z-only model charge: $\xi=10^{-39}$;
$\|\delta B\|\le\xi$ via $\|H\|,\|G\|\le\pi/2$, $c=2/\pi$;
$\|\delta B_{K}A^{-1/2}\|\le5\times10^{14}\xi=5\times
10^{-25}=\tau_{z}$ (using $\sqrt{G}<5\times10^{14}$ from
v14.210);
$\epsilon_{z}\le3\xi+42\tau_{z}+\tau_{z}^{2}\approx
2.1\times10^{-23}$;
action on $\|y\|\le0.002$: $<4.2\times10^{-26}<5\times
10^{-26}$ — recomputed via exact rationals, matches payload.
✓

Positive-kernel domination for $B_{K}$ on Far
($1-(m/n)^{2K}\in[0,1]$) preserves the norm bound — sound. ✓

## 4. Byte preservation and diagnostics (§§6,8) [V]

Payload SHA-256 `4437af2f…` matches, 44537 bytes. ✓
Default source mode: original v14.227 33018-byte JSON
unchanged — payload flag confirms. ✓
50 physical diagnostics pass with original digamma + 100-term
exponential reference. ✓
CI run 37996855750 completed/success. ✓

## 5. Verdict

$$\boxed{
\text{[V] Order-8 EM remainder, S8 bound, combined $<7.15e-42$,}\\
\text{sine $<1.13e-85$, z-only action $<5e-26$ all verified.}\\
\text{Default mode byte-identical. No correction.}
}$$

---

HANDOFF-ACK
from: v14.229
target: sandbox
status: closed
result: Action-precision z evaluator audited with no correction. Order-8 digamma remainder, four exponential moments, S8 bound, adaptive intervals, and z-only model action charge (<5e-26) all verified. Default source mode preserved byte-for-byte.
constraints: None.
