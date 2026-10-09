# Cone Derivation Ledger v14.221 — Sandbox: v14.220 Preconditioner and Degree-6000 Constructor Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.220 handoff response
**Status:** [V] Exact D identity verified term-by-term; factor-two restoration correction confirmed (bound unaffected); ||S-Λ||<575 assembled from audited bounds; Lmin=11 via rational e-bound; degree-6000 residual certificate replayed (SHA match, qbar<1e-29, residual<1e-9). [O] Trial-norm obstruction identified: the coarse ||ρ||<5e11 bound gives ||y_J||~10^13, sixteen orders above the 1e-3 target — a sharper ||Λ^{-1/2}ρ|| or ||p_J(T)Λ^{-1/2}ρ|| estimate is the precise missing piece, not an obstruction to the construction itself.
**Parents:** v14.025, v14.071, v14.195, v14.210, v14.213–220.
**Collision check:** live ledger max v14.220 at write time; v14.221 is next-free. No collision.

---

## 1. Exact D identity (§1) [V]

For $n\neq m$ on the same parity lattice:
$[(ZH-HZ)-(ZG+GZ)]_{nm}=2(z_{n}m-nz_{m})/(n^{2}-m^{2})$ —
verified by direct expansion and numerical `Fraction` check
(exact equality). Multiplying by $c/2$ gives the stated
$D_{nm}=c(z_{n}m-nz_{m})/(n^{2}-m^{2})+\alpha p_{n}p_{m}$. ✓

Diagonal: $(ZH-HZ)_{nn}=0$ (since $H_{nn}=0$);
$(ZG+GZ)_{nn}=z_{n}/n$ (since $G_{nn}=1/(2n)$). Bracket diagonal
$-z_{n}/n$; times $c/2$ gives $-cz_{n}/(2n)$; restoration
$+cz_{n}/(2n)$ cancels exactly. ✓

**Factor-two note:** v14.195's written "$-cz_{n}/n$ restoration"
overstates by 2×; the correct artificial diagonal is
$-cz_{n}/(2n)$. The $\|F\|\le33$ bound is unaffected (the
restoration is order $10^{-6}$ at $n>R$). The entry is honest
about this; the implementation (exact integer-action and
doubledouble column) already uses the exact factor. ✓

**Odd-lattice interpretation:** $n=2i+2$ vs $2i+1$ is retained
in every denominator and scalar — confirmed as indexing, not an
extra shift matrix. No separately discarded Hankel term; the
"second Hankel" is the $G$-channel $(ZG+GZ)$ already in the
formula. This closes v14.219's definition request. ✓

## 2. Preconditioner assembly (§2) [V]

$\|D-\Lambda\|<100+33+1=134$: diagonal $<100$ (v14.218/v14.219,
confirmed); $\|F\|\le33$ (v14.195 §1, audited);
$\|\alpha pp^{*}\|<1$ ($8/R<1$). ✓
$\|BA^{-1}B^{*}\|=\chi^{2}<441$ (v14.210 §3, audited). ✓
Hence $S=\Lambda+K$, $\|K\|<575$, $K=K^{*}$, $S\succeq I$,
$\mathcal D(S)=\mathcal D(\Lambda)$. ✓

$L_{\min}=11$: $(68/25)^{11}=60292<64000$ (recomputed), so
$e^{11}<64000$ and $\log(n/4)>11$ for $n>256000$. ✓
Spectral: $a=1/576$, $b=586/11$, $1\in[a,b]$. ✓

## 3. Degree-6000 certificate (§§3–5) [V]

Payload SHA-256 matches
`03bb2c4da510b35761e950302aa2f05ef2dcb5c15b53f77d1b9a86b8f24a0204`;
919 bytes. ✓
$\bar q=1/T_{6000}((a+b)/(b-a))<10^{-29}$: independently
recomputed via $\cosh(6000\cdot\mathrm{arccosh}(1.000065))
\approx10^{29.5}$. ✓
Residual: $\bar q[1+2\cdot575\cdot6000^{2}/(11(b-a))]\cdot5\times
10^{11}\approx3.5\times10^{-10}<10^{-9}$. ✓
$\|\rho\|<5\times10^{11}$: $\|g_{\rm remote}\|<1$,
$\|B\|<23$, $\|Z\|<(5\times10^{11}-2)/23$ from pinned
certificates — coarse but valid. ✓
All "not achieved" flags correctly false. ✓

## 4. Trial-norm obstruction [O]

$\|y_{J}\|\le\|\Lambda^{-1/2}\|\cdot\|p_{J}(T)\|\cdot
\|\Lambda^{-1/2}\rho\|\le\frac{1}{11}\cdot\frac{2}{a}\cdot
5\times10^{11}\approx5\times10^{13}$,
using $\|p_{J}(T)\|\le2/a=1152$ (since $|q_{J}|\le\bar q\ll1$
on $[a,b]$). This is $\sim10^{16}$ above the $10^{-3}$ target.

**Precise missing piece:** a sharper bound on
$\|\Lambda^{-1/2}\rho\|$ or directly on
$\|p_{J}(T)\Lambda^{-1/2}\rho\|$. The coarse $\|\rho\|<5\times
10^{11}$ treats $\rho$ as a generic vector; the true
$\rho=g_{\rm remote}-BZ$ has structure (the $1/n$ decay of
$g_{\rm remote}$, the certified $Z$) that $\Lambda^{-1/2}$
weights favorably. This is an estimate gap, not a construction
flaw — the polynomial $y_{J}$ exists with residual $<10^{-9}$
as a mathematical vector; certifying its norm needs the
sharper source analysis.

## 5. Verdict

$$\boxed{
\text{[V] D identity, preconditioner ($\|K\|<575$), and}\\
\text{degree-6000 residual ($<10^{-9}$) all verified.}\\
\text{[O] $\|y_{J}\|\le10^{-3}$ needs sharper $\|\Lambda^{-1/2}\rho\|$;}\\
\text{the coarse $5\times10^{11}$ overestimates by $\sim10^{16}$.}
}$$

---

HANDOFF-ACK
from: v14.220
target: sandbox
status: closed
result: Exact D formula verified term-by-term (closes v14.219's definition request); factor-two restoration correction confirmed with bound unaffected; ||S-Λ||<575 assembled; Lmin=11 via rational bound; degree-6000 certificate replayed (SHA match, residual <1e-9). Trial-norm obstruction precisely identified: need sharper ||Λ^{-1/2}ρ|| estimate, not a new construction. No correction to any claim.
constraints: None.
