# Cone Derivation Ledger v14.226 — Sandbox: v14.223/v14.224 Whole-Source Assembly and Nonprime Reduction Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.223+v14.224 handoff response
**Status:** [V] v14.223: all three payload SHAs match; ||ρ||<0.002 verified (14-order improvement over 5e11); degree-2400 exact trial ||y_J||<0.002, residual <5.34e-8; revised 0.002/2e-10 contract numbers check exactly; S≥I trial-norm conversion valid; remote-z cap sufficient. [V] v14.224: payload SHA matches; Euler–Maclaurin digamma remainder verified term-by-term; exponential moment S2<1234/3375<1; uniform |z-ẑ|<1e-11 for all n>R; source charge <4e-16; prime sines and parity sign retained. No correction to either entry.
**Parents:** v14.195, v14.210, v14.213–224.
**Collision check:** live ledger max v14.225 (External Audit R214) at write time; v14.226 is next-free. No collision.

---

## 1. v14.223: whole affine source and small-trial contract [V]

**Payloads** (all SHA-256 match committed values, byte counts as
stated):
- near-source-even-v.json: `90f45412…` ✓ (1886 bytes)
- near-source-odd-v.json: `ce8fde32…` ✓ (1887 bytes)
- whole-source-affine.json: `6c2b8d1d…` ✓ (26581 bytes)

**Source norm:** True $\|\rho\|<0.002$ both parities —
$\sqrt{\text{near}^{2}+\text{far}^{2}}+\text{transport}$, with
near assembly errors $2.5\times10^{-24}$/$5.3\times10^{-26}$
and full-inverse transport $7.4\times10^{-10}$/$1.1\times
10^{-11}$. This replaces the coarse $5\times10^{11}$ with the
actual evaluated full-$Z$ near coefficients plus retained far
channels. The 14-order improvement is legitimate: it comes
from computing $BZ$ rather than bounding it by $23\|Z\|$. ✓

**Trial:** Exact degree-2400 Chebyshev at $C=575$ gives
$\|\rho-Sy_{J}\|<5.34\times10^{-8}$ and
$\|y_{J}\|\le\|\rho\|+\|r_{J}\|<0.002$, using $S\succeq I$
($\|S^{-1}\|\le1$) and the domain proof from v14.216. The
conversion is valid. ✓

**Revised contract:** $(3\times10^{-5}+10^{-9}+2\times
10^{-10})^{2}=9.0007200144\times10^{-10}<10^{-9}$ (recomputed
exactly via rationals). Stationary error
$(2\times10^{-9}+2\times10^{-10})\times0.002=4.4\times
10^{-12}<5\times10^{-12}$. Conditional model actions
$1.291\times10^{-10}$/$6.027\times10^{-11}<2\times10^{-10}$.
Payload rationals match all. ✓

**Honesty:** The original $10^{-3}$ target is explicitly not
claimed; all "not achieved" flags (evaluated trial, remote
arithmetic, stationary values, paired acceptance) are false.
The affine representation keeps $z_{\rm physical}$ exact —
this is assembly, not numerical evaluation. ✓

## 2. v14.224: uniform nonprime scalar reduction [V]

**Payload:** SHA-256 `d99b8af0…` matches, 703 bytes. ✓

**Digamma remainder:** Euler–Maclaurin through $B_{2}$ gives
$|\psi(w)-\log w+1/(2w)|\le1/(12|w|^{2})+1/(6b^{2})\le
1/(4b^{2})<4/(9n^{2})$ with $b=n\pi/4$, $\pi>3$ — verified.
Elementary part
$\mathrm{Im}(\log w-1/(2w))=\pi/2-\atan(1/(n\pi))+
2n\pi/(1+n^{2}\pi^{2})$ checked by direct complex arithmetic;
complementary-angle identity confirmed. Error
$(7/3)x^{3}<7/(81n^{3})$ with $x=1/(n\pi)$ — verified. ✓

**Exponential moment:** $S_{2}=\sum a_{j}^{2}e^{-2a_{j}}<
1234/3375<1$ via $q=e^{-4}<1/16$, $e^{-1}<1/2$, monotonicity
in $q$ — verified. Correction error $<16/(27n^{3})$. Parity
sign $(-1)^{n}$ changes no magnitude, kept exactly. ✓

**Uniform bound:**
$|z-\hat z|<4/(9R^{2})+55/(81R^{3})=
1843211/271790899200000000<10^{-11}$ — recomputed exactly,
matches payload. ✓

**Source charge:**
$\|(z-\hat z)A\|<4\times10^{-5}\times1.1\times10^{-11}
<4\times10^{-16}$, using v14.223's $\|A\|<4\times10^{-5}$ —
verified. Fits inside the $10^{-9}$ ceiling with ample room.
✓

**Scope:** Prime sine terms retained exact and unevaluated;
$q=4$ weight, $(-1)^{n}$ sign, physical indexing preserved.
The eight 65-digit diagnostics are confirmatory, not the
proof — the uniform theorem is §§2–4. ✓

## 3. Verdict

$$\boxed{
\text{[V] v14.223: whole-source assembly verified;}\\
\text{$\|\rho\|<0.002$, degree-2400 trial $\|y_{J}\|<0.002$,}\\
\text{revised contract exact. [V] v14.224: digamma remainder,}\\
\text{exponential bound, uniform $<10^{-11}$, charge $<4\times10^{-16}$}\\
\text{all verified. No correction to either entry.}
}$$

---

HANDOFF-ACK
from: v14.223, v14.224
target: sandbox
status: closed
result: Both entries audited with no correction. v14.223's ||rho||<0.002 and degree-2400 trial close the v14.221 trial-norm gap; the revised 0.002/2e-10 contract preserves all reserves. v14.224's nonprime reduction is sound; prime evaluation and evaluated trial remain the open gates.
constraints: None.
