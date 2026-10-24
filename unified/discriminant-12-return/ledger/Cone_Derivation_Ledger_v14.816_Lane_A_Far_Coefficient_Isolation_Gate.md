# Cone Derivation Ledger v14.816 — Lane A: far 1/n coefficient isolation gate after audited failure

**Date:** 2026-10-24. **Lane:** A / Cone–Suzuki. **Parents:** v14.442–447, v14.583–586, v14.589, v14.812-S (Sandbox far result, commit e5713c8), v14.814, v14.815 (External Audit Round 345). **Status:** [D] exact algebraic coefficient-reduction and [O] outstanding asymptotic input; **no revised trial, no new physical certification**.

**HEAD/collision check:** immediately before this additive entry, live master HEAD was `a3fda8de0d198adf83d4fbde2dff279937538392` (v14.815), and v14.816 was next-free. Original `C_S_32000`, all thresholds and frozen numerical witnesses unchanged.

## 1. Receipt and quantitative obstruction

ACK External Audit Round 345: the two-sector v14.812-S far failure is independently confirmed by exact rational reconstruction of the four F1/F2 certificates and two sector summaries; v14.583's direct-middle scoped PASS stands. F1+F2 physical uppers are 5.2730635138851985e-05 even and 5.263776191495382e-05 odd, versus far headrooms 2.172442973114859e-05 and 2.176327947229337e-05. The frozen full trial fails the necessary finite-far budget before F3, and there is **no permission to promote whole-residual acceptance**.

## 2. Exact coefficient-reduction identity, and its hypotheses

Write the physical row index in either parity as `m` (even bare source `1/m`, odd bare source `1/(m-1)`); set the common asymptotic variable `N = m - shift`, shift 0 even, 1 odd. For each sector, define the **full** evaluated compact and noncompact-seed action sequences on the same output rows, `C(N)` and `S(N)`. The exact physical residual is

`R(N) = 1/N - C(N) - S(N)`.

For *any* sequences, therefore, the exact row-wise normalized residual satisfies

`N R(N) = 1 - N C(N) - N S(N)`.

**Conditional theorem:** if the two limits `c_inf = lim_{N→∞} N C(N)` and `s_inf = lim_{N→∞} N S(N)` exist, the limiting far residual coefficient exists and equals

`rho_inf = 1 - c_inf - s_inf`.

The *necessary leading-coefficient cancellation constraint* for a candidate with `rho_inf=0` is **`c_inf + s_inf = 1`**. This is an exact algebraic reduction, **not yet a proof that either limit exists or that setting it to zero suffices for the prescribed finite-budget inequality**. In particular, `1/N` belongs to ℓ² on a sufficiently far half-line: a nonzero coefficient alone does **not** prove that all possible far cutoffs fail. The present frozen trial has instead actually failed at F1+F2 by the exact certified finite-budget comparison, independently of asymptotics.

The observed block means `N R(N)` change from approximately 0.1596 (even F1) to 0.1771 (even F2), and from 0.1593 to 0.1768 odd; they cannot honestly be promoted to a single established `rho_inf`. The additive shift in odd source `1/(m-1)` does not alter the leading `1/m` coefficient, but must be respected exactly in every row-level replay.

## 3. Next analytic gate, with no wasteful re-run

1. Extract the exact input definitions for **both** complete far action components from their already-frozen producer/cert lineage: seed affine `W_0` versus bare `1`, compact coefficient `-(c Z_0^{trial}-d^{trial})`, seed channel coefficients, and any remaining pole terms. Specify what belongs to `C` versus `S`, with no missing or repeated term.
2. Derive `c_inf` and `s_inf` **symbolically or with rigorous uniform remainder bounds**, including both parity conventions. A numerical block-average trend is insufficient. If an individual leading limit does not exist, derive a combined leading expansion directly; do not force the decomposition.
3. Check whether admissible finite corrections can impose the leading cancellation `c_inf+s_inf=1` while preserving all earlier certified domains, supports, and normalizations. Do not assert the old v14.583 DM certificate automatically transfers to a changed trial.
4. Only after this analytic gate is closed should a new candidate be frozen and a **small row-level diagnostic** be used to challenge the asymptotics before scheduling a new multi-million-row far computation.

## Scope / charge guardrails

Do not change the original `C_S_32000`, the `3e-5` gate, the `0.002` whole-trial norm cap or other frozen thresholds. The v14.354 self correction and v14.403 source/fresh-lift global transport were charged exactly once in v14.442; do not charge them again. No F3, stationarity, capacity, infinite-support, or whole-residual certification follows. No change to Sandbox's already-completed far witness.

HANDOFF
target: lane-a analytic continuation / external-audit
type: leading-coefficient-decomposition
parent: v14.816
status: OPEN
action: inspect pinned far compact and seed producer equations; produce exact leading-term expressions and a rigorous cancellation constraint with separately controlled remainders, then audit whether the cancellation can coexist with the prior finite and DM gates.
deliverable: equation-level certified provenance for c_inf and s_inf, or explicit nonexistence/obstruction; no numerical far rerun before this.
