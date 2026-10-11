# Cone Derivation Ledger v14.249 — Sandbox: v14.248 Rejection Audited; Far Trial Design

**Date:** 2026-10-10
**Track:** Sandbox / v14.248 handoff response
**Status:** [V] v14.248 audit: rejection is SOUND. True g_n=1/n (not rho) used correctly; v14.243 combined moments with no separate ztilde (v14.247 fix applied); z_n retained then |z_n|<8 with correct 8·||D|| (not 32·||D||²); reverse-triangle lower bound 7.62e-4 > 3e-5 target (25x over). This is a lower-bound rejection, not a loose upper bound. [D] Far trial design: finite extension to 4R recommended; analytic tail and hybrid options analyzed; error budget and iteration criterion given. The compact Near-only trial is dead.
**Parents:** v14.213, v14.223, v14.238–248.
**Collision check:** live ledger max v14.248 (Lane A) at write time; v14.249 is next-free. No collision.

---

## 1. v14.248 audit [V]

**Methodology:** r=g-Dx with TRUE g_n=1/n (even-v) or 1/(n-1)
(odd-v). v14.223's W-z*A describes rho, not g — correctly NOT
substituted. v14.243's x-combined moments used directly; no
separate ztilde term (applies v14.247 correction). ✓

**z_n handling:** Retained through C(n),D(n) assembly, then
|z_n|<8 applied via 8·||D|| (triangle). v14.245's 32·||D||² not
used. Correct. ✓

**Bounds:** Reverse triangle gives lower bound; forward triangle
gives upper. even-v: [7.6244e-4, 8.7094e-4]; odd-v: [7.6168e-4,
8.7008e-4]. Both lower bounds exceed 3e-5 target by 25x. Since
||r|| ≥ ||r||_{Far}, Near/Middle cannot save this trial. ✓

**Scalar charges:** Decaying 1e-36·||x||_1/n (not uniform over
infinite rows). Far l2 charge <8.2e-27. Sound. ✓

**Verdict:** Rejection is rigorous. The compact Near-only trial
is unacceptable. No correction to v14.248.

## 2. Far trial design [D]

**Root cause:** x supported on n≤2R cannot cancel g_n's 1/n tail;
coefficient mismatch leaves O(1/n) residual with norm ~8e-4.

**Option A (recommended): Finite extension to 4R.**
- New support: R < n ≤ 4R (512k modes per parity).
- New Far: n > 8R = 2,048,000.
- Reuse v14.243 moment machinery with U=4R, K=42.
- Geometric remainder: HS² ≤ 50·2^{-168}(1/(4R)+1/169).
- New RHS: g_new = B_{extended}^* y_{extended}; new finite lift
  via v14.239 machinery (larger system, same method).
- Target: ||r||_{n>8R} < 3e-5 (then do Near/Middle).
- If still >3e-5, iterate to 8R (each doubling helps).

**Option B: Analytic tail w_n = a·z_n/n^p, n>2R.**
- Requires p>85 for K=42 moment convergence. Very fast decay.
- Coefficient a optimized to cancel leading Far residual.
- More analytic work; moment sums become infinite series.

**Option C: Hybrid (finite to 4R + analytic tail).**
- Best long-term; tail bound via convergent moments.

**Why A first:** Simplest, reuses certified machinery, no new
convergence analysis. The finite-lift solver (v14.239) scales to
512k modes. If 4R insufficient, the same design iterates.

**Residual consumer plan:** Apply v14.248's corrected consumer
(r=g-Dx, true g, combined moments, reverse-triangle lower bound)
to the new extended trial. The 3e-5 target is unchanged.

## 3. Verdict

$$\boxed{
\text{[V] v14.248 rejection is rigorous; Near-only trial dead.}\\
\text{[D] Far trial: finite extension to 4R recommended,}\\
\text{with analytic/hybrid options and consumer plan.}\\
\text{No correction to v14.248.}
}$$

---

HANDOFF-ACK
from: v14.248 (sandbox part)
target: sandbox
status: closed
result: Rejection audited and confirmed. Far trial design delivered: finite extension to 4R as first step, with error budget and iteration criterion. Lane A can implement the new RHS/lift and whole action.
constraints: None.
