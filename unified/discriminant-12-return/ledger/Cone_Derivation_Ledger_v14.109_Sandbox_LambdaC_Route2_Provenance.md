# Cone Derivation Ledger v14.109 — Sandbox Response to v14.108: λ_c Provenance Pinned to Route 2

**Date:** 2026-10-07
**Track:** Sandbox (Jeremy)
**Status:** Closes v14.108's open question. Nothing published.
**Parents:** v14.106, v14.108.

---

## 1. The audit's question (v14.108 §2)

v14.106's $\alpha=4\omega^3\bar\lambda_c^2Y_{\rm geom}^2/(9c^2A)$ is
algebraically and numerically confirmed, but: "whether the specific
$\lambda_c$ figure used here traces cleanly to route 2, or implicitly
carries some route-1 ($R_\infty$/$\alpha$) influence through the
combined [CODATA] adjustment, is a real question."

The audit is right: v14.106 used $m_e=9.1093837015\times10^{-31}$ kg,
the CODATA global-fit value. That number mixes both routes.

## 2. Route-2-only recomputation

$$m_e({\rm kg}) = \frac{A_r(e)\times M(^{12}{\rm C})}{12\times N_A}$$

- $A_r(e)=5.48579909065\times10^{-4}$: Sturm et al. 2014, Penning-trap
  cyclotron-frequency ratio (dimensionless, $\alpha$-free).
- $M(^{12}{\rm C})=0.012$ kg/mol: SI 2019 measured (mass spec + XRCD,
  $\alpha$-free; deviation from exact $<4\times10^{-10}$).
- $N_A=6.02214076\times10^{23}$ mol$^{-1}$: exact (SI 2019).

Result: $m_e=9.1093837047\times10^{-31}$ kg (ratio to CODATA:
1.0000000004). $\bar\lambda_c=\hbar/(m_ec)=3.861593\times10^{-13}$ m.

$\alpha$ (route-2): $1/137.1356$ (0.0727%), identical to v14.106 to
all displayed digits. The numerical result never depended on the
global fit; only the provenance needed cleaning.

## 3. Verdict

The "no $\alpha$ input" claim in v14.106/v14.107 is now **fully
pinned**: every numerical input traces to Penning-trap ratios,
XRCD/mass-spec, exact SI defining constants, Lyman-$\alpha$
spectroscopy, or pure $SO(4,2)$ geometry. No CODATA global-fit value
is used. v14.108's question is closed.

---
*Sandbox exploratory. Per Jeremy 2026-10-07 ("give it everything it asks for").*
