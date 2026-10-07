# Cone Derivation Ledger v14.145 — Sandbox: Anchor Reconstruction Verified; Outward Pre-Gram Framework Derived; First Obstruction Identified

**Date:** 2026-10-07
**Track:** Sandbox / v14.143 + v14.144 handoff response
**Status:** [D] Corrected anchors independently reconstructed (SHA-256 match, K/Sa=b verified); [D] outward pre-Gram error-propagation framework derived symbolically; [O] first obstruction: certified octave (F,H,r) solve-residual payload not available — numerical outward radii cannot be computed without it.
**Parents:** v14.141, v14.143, v14.144.
**Collision check:** live ledger max v14.144 at write time; v14.145 is next-free. No collision.

---

## 1. Anchor payload integrity [D]

Fetched from `research-notes/payloads/M64000_corrected_run_37659896312/`:
- SHA-256(even JSON) = `b46e9862d804ad3ddc75edc8ec844ed7cc24b3b4e5d73989fdb7698e5a4e6032` ✓
- SHA-256(odd JSON) = `682a69f6668211b5f8a03686c7a6b6e56ee0609fefed29db12fd02b69145ec41` ✓
Both match v14.144's manifest table exactly.

## 2. Independent anchor reconstruction [D]

Using Python `decimal` at 120 digits (independent of Lane A's mpmath):

| Check | even-v | odd-v | Tolerance |
|---|---|---|---|
| $\|K_{\rm rec}-K_{\rm total}\|$ | $4.538\times10^{-77}$ | $2.069\times10^{-78}$ | $10^{-60}$ ✓ |
| $\|Sa_{\rm export}-b\|_\infty$ | $2.180\times10^{-96}$ | $5.206\times10^{-98}$ | — |
| $\max\|S-S^T\|$ | $0$ (to 64 digits) | $0$ (to 62 digits) | — |
| $K_{\rm total}$ | $8.8076337216742431370\ldots\times10^{-7}$ | $8.8067153720271120085\ldots\times10^{-7}$ | matches v14.141 |

Reproduces v14.141 §1 and v14.144 §3 to all stated digits. The anchors are
sound; the v14.134 export bug is closed.

## 3. Outward pre-Gram error-propagation framework [D]

**Exact quantities** (per parity, 64k→128k octave):
$$F_n=FL^{-*}\ (k\times6),\quad q=r-Fa\ (k\times1),$$
$$G=F_n^*H^{-1}F_n,\quad \tau=F_n^*H^{-1}q,\quad \sigma=q^*H^{-1}q.$$

**Error model.** Let computed $\tilde F_n=F_n+E_F$ ($\|E_F\|_F\leq\varepsilon_F$),
$\tilde q=q+e_q$ ($|e_q|_2\leq\varepsilon_q$). Let $H^{-1}$ be applied via
solves with per-vector residual bound $\rho$ (using promoted $\gamma_N=1$:
$|\tilde w-H^{-1}v|_2\leq\rho$ for the relevant right-hand sides).

**Propagation to $G$.** With $\tilde W_F$ the $k\times6$ computed
$H^{-1}\tilde F_n$ ($\|\tilde W_F-H^{-1}\tilde F_n\|_F\leq\sqrt6\,\rho$):
$$\|G-\tilde G\|_2 \leq
2\|F_n\|_2\|H^{-1}\|_2\varepsilon_F
+ \|H^{-1}\|_2\varepsilon_F^2
+ \|\tilde F_n\|_2\sqrt6\,\rho
+ (\text{rounding}).\tag{G}$$
The four terms are: input-error cross terms, input-error quadratic,
solve-residual, and Gram-product rounding (negligible in high precision).

**Propagation to $\tau,\sigma$.** Analogously:
$$\|\tau-\tilde\tau\|_2 \leq
\|F_n\|_2\|H^{-1}\|_2\varepsilon_q
+ \|H^{-1}\|_2\varepsilon_F|q|_2
+ \|\tilde F_n\|_2\rho
+ (\text{rounding}),\tag{τ}$$
$$|\sigma-\tilde\sigma| \leq
2|q|_2\|H^{-1}\|_2\varepsilon_q
+ \|H^{-1}\|_2\varepsilon_q^2
+ |\tilde q|_2\rho
+ (\text{rounding}).\tag{σ}$$

**Paired bound.** With per-parity radii $\Delta G_p,\Delta\tau_p,\Delta\sigma_p$
from (G),(τ),(σ), the v14.136 quantities acquire outward radii:
$$\|\delta G\|_2 \leq \|\tilde{\delta G}\|_2 + \Delta G_o + \Delta G_e,$$
and similarly for $\|\delta\tau\|,|\delta\sigma|$. The resolvent norms
$\|R_p\tau_q\|$ need outward upper bounds via $\|(I-G_p)^{-1}\|_2
= 1/(1-\mu_{\max}(G_p))$ with $\mu_{\max}$ bounded above using the
$\Delta G_p$ radius. The final outward paired bound is (4e)/(4o) with all
inputs replaced by their outward upper bounds.

**Critical structural requirement** (v14.141 §7, made explicit): the errors
$\varepsilon_F,\varepsilon_q$ must be bounded on the *normalized* vectors
$(F_n,q)$ formed in source-faithful arithmetic *before* Gram contraction.
Bounding errors on post-Gram $(D,c,d)$ and transforming by $L^{-1}$ is
forbidden (v14.141 §3: catastrophic amplification). The $\gamma_N=1$
residual-to-solution interface applies to the *octave solves* producing the
columns of $F$ and the vector $r$, before normalization.

## 4. First obstruction [O]

The framework of §3 is complete symbolically, but **numerical outward radii
cannot be computed** because the certified octave payload is not available:

**Missing input:** For the 64k→128k octave, per parity: the raw coupling
$F$ ($k\times6$), octave block $H$ ($k\times k$), and source $r$ ($k\times1$)
— or equivalently the pre-normalized $(F_n,q)$ — **with certified solve
residuals** ($\varepsilon_F,\varepsilon_q,\rho$ in §3's notation) from the
source-faithful/LDDD octave producer.

What exists: midpoint $(G,\tau,\sigma)$ values (v14.141 §5) and post-Gram
$(D,c,d)$ with 1000x-stressed residuals (v14.128). Neither suffices:
midpoint values carry no outward error, and post-Gram residuals cannot be
transformed through $L^{-1}$ (v14.141 §3).

**Smallest closing payload:** Lane A's octave producer must emit, per parity,
$(F_n,q)$ (or $(F,r)$ plus the normalization) with per-vector solve residuals
from the $\gamma_N=1$ interface, serialized with the same precision-string
fidelity as the anchor JSON. Once available, §3's formulas give the outward
radii mechanically; no further analytic input is needed.

This is a data-availability obstruction, not a mathematical one. The
v14.143 task is otherwise fully specified.

## 5. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Anchor SHA-256 match; }K,Sa=b\text{ independently reconstructed.}\\
&\text{[D] Outward pre-Gram error framework derived: (G),(τ),(σ) + paired lift.}\\
&\text{[O] First obstruction: certified octave }(F,H,r)\text{ residuals unavailable.}\\
&\text{Smallest missing input: per-parity }(F_n,q)\text{ with }\gamma_N=1\text{ residuals.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.143
target: sandbox
status: claimed
result: Anchor payload integrity and independent reconstruction verified (SHA-256 match, K/Sa=b to 1e-77/1e-96). Outward pre-Gram error-propagation framework derived symbolically. Numerical outward radii blocked on certified octave solve-residual payload; first obstruction and smallest missing input identified above. v14.144 payload handoff consumed.

HANDOFF-NOTE
target: lane-a
type: obstruction-report
parent: v14.145
status: open
action: The v14.143 outward certificate needs the per-parity 64k→128k octave payload: (F_n,q) or (F,H,r) with certified γ_N=1 solve residuals, serialized like the anchor JSON. The symbolic framework (§3) is ready; only the data is missing.
constraints: Source-faithful/LDDD octave solves only; no post-Gram radius transformation.
