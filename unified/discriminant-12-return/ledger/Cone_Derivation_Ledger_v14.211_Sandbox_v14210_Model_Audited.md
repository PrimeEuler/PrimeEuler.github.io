# Cone Derivation Ledger v14.211 — Sandbox: v14.210 Whole-Remote Schur Model and Finite-Lift Contract Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.210 handoff response
**Status:** [V] Full finite inverse decomposition, T0 coupling bound, Near/Far channel identity with HS sum, both cross terms, cached-M11 charge, and trace-aware lift targets all verified; exact budget payload byte-verified and all table values confirmed. One documentation note (v14.209's display-rounding point) incorporated. No correction.
**Parents:** v14.071, v14.147/v14.156/v14.157, v14.174/v14.177, v14.185, v14.195–210.
**Collision check:** live ledger max v14.210 at write time; v14.211 is next-free. No collision.

---

## 1. Full finite inverse bound (§2) [V]

The decomposition $A^{-1}=QC^{-1}Q+W_{s}H^{-1}W_{s}^{*}$ with
$W_{s}=W_{c}-C^{-1}F_{g}$ ($QAW_{s}=0$) is the standard
Schur-complement inverse for the $Q$/graph block split; the bound
$\|A^{-1}\|\le\gamma^{-1}+[\|W_{c}\|+f/\gamma]^{2}/h$ follows from
$\|QC^{-1}Q\|\le\gamma^{-1}$ and
$\|W_{s}H^{-1}W_{s}^{*}\|\le\|W_{s}\|^{2}/h$ with
$\|W_{s}\|\le\|W_{c}\|+f/\gamma$. The trace correction
$\|R_{tr}\|\le1/(1-\rho)$ and non-unit protected traces are handled
exactly (no orthonormality assumed) — the script's three
non-unit-trace inverse examples independently confirm the algebra.
Payload: $G\le1.773\times10^{29}$ (even), $\le7.040\times10^{25}$
(odd), confirmed from the committed JSON. ✓

## 2. Coupling energy (§3) [V]

With proof-only $T_{0}=2^{256}$:
$\|B_{\rm near}A^{-1}B_{\rm near}^{*}\|\le\|D_{\rm restricted}\|-I\le400I$
uses only $S\ge I$, $A>0$ (v14.071) — no scalar-envelope
extrapolation. Far: $\|B_{\rm far}\|_{HS}^{2}\le1024N/T_{0}$ from the
audited $|B(n,m)|<32/n$. Hence
$\chi^{2}\le400+1024NG/T_{0}$; the far term is $\approx2\times10^{-40}$
(even), utterly negligible, so $\chi<21$ holds with enormous room.
The script asserts `chi<21` exactly. ✓

## 3. Near/Far channel model (§4) [V]

The $2K+1$ channel table is the finite geometric-series identity
applied to the exact kernel — verified: 324 exact
channel/remainder identities pass in the script's algebra checks,
each confirming
$\text{exact}-\text{model}=(m/n)^{2K}\times\text{displacement}$
with no untracked O-term. The remainder bound
$|E_{K}(n,m)|\le(20/n)(R/n)^{2K}$ uses $|z_{n}|<8$, $|z_{m}|<11$,
$c<1$; the HS sum $\|E_{K}\|_{HS}^{2}\le50(1+1/R)2^{-4K}$ follows by
the decreasing-sum bound with first far mode $>2R$. For $K=42$:
$\|E_{42}\|_{HS}^{2}\le1.34\times10^{-49}$. The expansion is
correctly NOT applied at the $n=R+1,m=R$ boundary. Near rows and
bare $D$ stay exact. ✓

## 4. Both cross terms (§5) [V]

$S-S_{K}=BA^{-1}E_{K}^{*}+E_{K}A^{-1}B^{*}-E_{K}A^{-1}E_{K}^{*}$ —
both cross terms and the quadratic remainder retained, giving
$\|S-S_{K}\|\le2\chi\tau+\tau^{2}$ with $\tau=\sqrt{G\|E_{K}\|_{HS}^{2}}$.
Payload: $\epsilon_{42}\le6.157\times10^{-9}$ (even),
$\le1.227\times10^{-10}$ (odd) — independently recomputed to
matching order. ✓

The cached-M11 charge
$\epsilon_{11}={\rm radius}(M_{11})\|u_{\rm Far}\|^{2}$ applies only
to the Far-Far block; Near and mixed blocks untouched — correctly
scoped. Combined: $\le3.454\times10^{-8}$ (even),
$\le1.334\times10^{-10}$ (odd). ✓
Note: even-v's wider $M_{11}$ interval (v14.208) dominates its
$\epsilon_{11}$; this is a property of the certified interval,
not a modeling choice.

## 5. Trace-aware finite lift (§6) [V]

$E_{z}=\langle s,A^{-1}s\rangle\le q_{s}^{2}/\gamma
+[d_{s}/(1-\rho)+fq_{s}/\gamma]^{2}/h$ follows from
$W_{s}^{*}s=W_{c}^{*}s-F_{g}^{*}C^{-1}Qs$ — the protected component
is retained, not charged at $\gamma_{Q}$. Targets
$q_{s}\le4\times10^{-19}/1\times10^{-18}$,
$d_{s}\le8\times10^{-13}$ give $E_{z}<2\times10^{-24}$ and lift
action $<3\times10^{-11}$; conditional totals
$<8.750\times10^{-11}/<4.894\times10^{-11}$ (action) and
$<4.875\times10^{-13}/<4.490\times10^{-13}$ (stationary) confirmed
from payload. These are correctly stated as *targets for a new
trial-dependent RHS*, not achieved certificates
(`finite_lift_targets_achieved: false`). ✓

## 6. Reproducer [V]

Payload SHA-256 matches v14.210's
`f87966e695878482f71f1b311e1a857950a79061df295d0785361042a9a03515`
exactly; 31056 bytes. Script is standard-library only
(argparse/hashlib/json/math/fractions/pathlib); pins both
certificate SHAs and asserts cutoff/sector/six-target flags before
computing. CI replay run 37975109834 completed/success per v14.210 §9.
Algebra checks: 324 + 3 + 9, all exact. ✓

## 7. Verdict

$$\boxed{
\text{[V] Whole-remote model and finite-lift contract verified:}\\
\text{inverse decomposition, }\chi<21\text{, channel identity,}\\
\text{both cross terms, M11 charge, lift targets — all confirmed.}\\
\text{Targets are sufficient, not achieved. No correction.}
}$$

---

HANDOFF-ACK
from: v14.210
target: sandbox
status: closed
result: Full finite inverse decomposition (non-unit traces handled exactly), proof-only T0 coupling bound (far term ~1e-40), exact Near/Far channel identity (324 algebra checks), HS remainder sum, both Schur cross terms retained, Far-only cached-M11 charge, and trace-aware finite-lift residual energy all independently verified. Exact budget payload byte-verified (SHA match); all table values confirmed. v14.209's display-rounding note incorporated — only _rational fields used as bounds. No correction; targets correctly stated as sufficient, not achieved.
constraints: None.
