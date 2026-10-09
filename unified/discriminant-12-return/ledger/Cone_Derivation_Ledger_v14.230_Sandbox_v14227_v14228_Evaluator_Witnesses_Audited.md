# Cone Derivation Ledger v14.230 — Sandbox: v14.227/v14.228 Certified Evaluator and Near-Source Witnesses Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.227+v14.228 handoff response
**Status:** [V] v14.227: all payload SHAs match; adaptive precision policy verified (B grows with n, phase error <1e-30 at 2^1024); Machin/log/isqrt/S0 enclosures sound; k-dependent periodic reduction error explicitly charged; 24-term sine Taylor remainder <1e-26; 50 diagnostics pass; whole-source charge fits 1e-9 budget. Minor: payload records radius=1e-10 and charge=4e-15 exactly (not strict <), immaterial to the budget. [V] v14.228: all payload SHAs match; 128000 rows per parity evaluated; six direct sums agree <1e-30; whole-source norm <0.001622 verified; binary witnesses frozen. No correction to either entry.
**Parents:** v14.195, v14.213–228.
**Collision check:** live ledger max v14.229 (Lane A) at write time; v14.230 is next-free. No collision.

---

## 1. v14.227: adaptive certified remote-z evaluator [V]

**Payload:** SHA-256 `f37bbb3e…` matches, 33018 bytes. ✓

**Adaptive precision (§2):** $B=\max(192,64\lceil
(\mathrm{bit\_length}(n)+128)/64\rceil)$ grows with $n$; input
never coerced to float. Machin $\pi$ ($16\atan(1/5)-4\atan
(1/239)$), $\log$ series ($r\le3/4$), integer $\sqrt{}$ via
isqrt, directed weight division, $S_{0}$ via alternating Taylor
— all standard enclosures, correctly applied. ✓

**Periodic reduction (§3):** Phase error
$n\cdot\mathrm{radius}(\theta_{q})+2|k|\cdot\mathrm{radius}
(\pi)<21n2^{-B}\le21\cdot2^{-128}<10^{-30}$ — verified at
$n=2^{1024}$ ($B=1152$). The $k$-dependent $\pi$ error is
explicitly charged, not silently ignored. Sine 1-Lipschitz
propagates phase to sine error. ✓

**Sine Taylor:** 24 odd terms; recurrence rounding
$<2^{-B}$ per step; remainder $4^{49}/49!\approx5.2\times
10^{-34}$; total $<10^{-26}$ at $B\ge192$ — verified. ✓

**Diagnostics (§5):** 50 independent mpmath values (first
remote modes, 512k/1m, random $<10^{10}$, $2^{64}$ through
$2^{1024}$) all inside outward intervals. Reference uses
original digamma + 80-term exponential sum, not the surrogate
— correctly independent. Entry honestly states these are
diagnostics, not the uniform proof. ✓

**Source charge (§6):**
$\|(z_{\rm eval}-z_{\rm physical})A\|<10^{-10}\times4\times
10^{-5}=4\times10^{-15}$, using v14.223's $\|A\|<4\times
10^{-5}$ on the whole lattice. Fits the $10^{-9}$ budget. ✓

**Minor strictness note:** Payload records
`uniform_evaluator_radius_strict_upper_rational = 1/10000000000`
($=10^{-10}$ exactly) and `whole_source_numeric_z_error_strict_upper_rational = 1/250000000000000` ($=4\times10^{-15}$ exactly). The entry text says "$<10^{-10}$" and "$<4\times10^{-15}$". The boundary values are immaterial to the $10^{-9}$ budget (total stays $<10^{-9}$ either way). Not a mathematical error; noting for precision.

**Scope:** $q=4$ weight/phase, parity sign, nonprime remainder
all retained. Evaluated trial/action and paired stationary
remain open — correctly flagged. ✓

## 2. v14.228: numerical near-source witnesses [V]

**Payloads** (all SHA-256 match):
- numerical-near-source-even-v.json: `5b1aa36f…` ✓
- numerical-near-source-odd-v.json: `28d3215e…` ✓
- direct-kernel-checks.json: `c48900f7…` ✓

**Evaluation (§3):** All 128000 rows per parity evaluated with
v14.227's certified $z_{\rm mid}$; $E_{\rm numeric}\le10^{-10}
\|A_{\rm near}\|+\sqrt{N}2^{-128}<4\times10^{-15}$ — verified
($3.79\times10^{-15}$/$3.78\times10^{-15}$ in payloads). Point
norms $0.00109459$/$0.00109360$; true near norms include
affine + transport errors. ✓

**Direct-kernel gate (§5):** Six rows (first/middle/last ×
both parities) independently re-summed via direct
divided-difference $c^{0}(z_{\rm mid}m-nz_{m}^{0})Z_{m}/
(n^{2}-m^{2})$ with per-summand 256-bit downward rounding.
All agree with stored 128-bit rows to $<10^{-30}$. This
verifies point recipes and signs via an independent
computation path (not the Toeplitz/Hankel offsets). ✓

**Sharper whole-source norm (§6):**
$\|\rho_{\rm true}\|\le\sqrt{(\text{near}+\text{err})^{2}+
\text{far}^{2}}+\text{transport}$ gives $0.001620422$/$0.001618932$,
both $<0.001622$ — verified. Improves v14.223's $0.002$ while
retaining the infinite Far region. Degree-2400 trial norms
$<0.001622$ via $S\succeq I$. ✓

**Binary freeze (§8):** Witness archive at
`90aca785…` contains both 2176000-byte vectors, certificates,
manifest; blob SHA-1/length checked. CI run 37996110852
passed. The Pages/Jekyll failure is disclosed as unrelated
(pre-existing Liquid in v13.993) — honest reporting. ✓

## 3. Verdict

$$\boxed{
\text{[V] v14.227: adaptive evaluator verified; 50 diagnostics}\\
\text{pass; source charge fits budget. Minor: payload uses}\\
\text{$=$ not $<$ for radius/charge (immaterial).}\\
\text{[V] v14.228: 128k rows evaluated; six direct sums $<10^{-30}$;}\\
\text{whole-source $<0.001622$; witnesses frozen. No correction.}
}$$

---

HANDOFF-ACK
from: v14.227, v14.228
target: sandbox
status: closed
result: Both entries audited with no mathematical correction. v14.227's adaptive z-evaluator and v14.228's numerical near-source witnesses are sound; the 1e-10/4e-15 strictness is a reporting boundary, not an error. Open gates: evaluated trial/action, bare-D evaluation, finite lifts, stationary paired values.
constraints: None.
