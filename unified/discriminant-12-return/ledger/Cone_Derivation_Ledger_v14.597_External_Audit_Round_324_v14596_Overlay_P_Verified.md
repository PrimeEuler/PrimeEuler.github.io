# Cone Derivation Ledger v14.597 — External Audit Round 324: v14.596 Overlay-P Distribution-Class Closure Verified

**Date:** 2026-10-19
**Track:** External Audit
**Status:** [V] v14.596 is a tangential Sandbox exploratory closure (helix-representation obstruction from the 2026-09-28 product-form arc) — not discriminant-12-return certification work; correctly flags `answers_lane_a_handoff=false`, `certified_objects_modified=false`, `verification_is_proof=false`, `G_derived=false`. Both deposited file hashes verified exact. The producer `overlay_P.py` was re-executed unmodified (full run, ~507s, no edits) and reproduces **every single cited number exactly** — all sanity anchors, all seven independent-quadrature anchor agreements (≤8.04×10⁻¹³), the tail-law fit, the centre constant, the product-error budget, the sign-change location, and the four conditional-convergence partial sums. This auditor additionally re-derived the construction's load-bearing closed-form identity from scratch, independently of the producer, and confirmed it. No defect found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–595, v14.593 (closes the item v14.593 explicitly left open).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `b23b0fa...` (v14.596), matching local HEAD; live ledger max was v14.596. v14.597 is next-free. No collision.

---

## 1. File-hash verification

| file | stated SHA-256 | re-hashed |
|---|---|---|
| `Overlay_P_Distribution_Class_Closure.md` | `18828ece50635b68b123fc9762ca5e3ebeb79322216a82ce5b77f55233fd8b6f` | match |
| `overlay_P.py` | `fbef5a0b207f5a9a18e3776fa7ec53da6fe6676d839777a10e8c634664747f70` | match |

## 2. Producer re-execution (unmodified, full precision, clean)

`overlay_P.py` was run directly from the checkout with no modification (dps 30, 8191-point Chebyshev–Lobatto grid of Lerch-transcendent evaluations, ~507s wall time). Every cited figure reproduces exactly, including quantities not shown as headline numbers in the ledger prose but printed by the script:

- `s = 0.24060639745313877267` (expect `...78`); `t0 = 1.91204928086509854` (STATUS `...85`); `T(30) direct = tail formula` exact match.
- Coarse-scan bump max `0.441011939527` at `t=0.75047934` — matches the ledger's own characterization as a coarse value against the STATUS-refined `0.4410123794637466`.
- `a0/2 = 0.035905161267`.
- All seven independent mpmath-quadrature anchors (n=1,2,3,5,8,13,21) agree with the grid-derived coefficients to `≤8.04×10⁻¹³` — matching the ledger's `≤8×10⁻¹³`.
- Tail fit `A=0.150064, B=-0.014744, C=-0.0008`; `Σ|r_n| (n≤512) = 0.3920`.
- Centre constant: `0.7163830844` vs `ζ(2,1/4)/24 = 0.7165553814`, diff `1.72e-04` — matches `1.7×10⁻⁴`.
- Product check: `max|err| = 1.033e-03` at `t=30`, `rms = 2.162e-04`, `max rel err (|A12|>1) = 3.503e-05` — all three match the ledger exactly.
- Sign-change: P zero at `t=1.912049582569` vs exact `t0=1.912049280865`, diff `3.02e-07` — matches `3.0×10⁻⁷`.
- Conditional-convergence partial sums `S_N(0)+s·log N` at N=64/256/1024/4096: `0.26293809 / 0.28302622 / 0.29274951 / 0.29752642` — matches the ledger's `0.26294 / 0.28303 / 0.29275 / 0.29753` exactly.
- Crossover errors at c=0.5/1/2/4: `0.1110 / 0.0168 / 0.0050 / 0.0012` — matches exactly.

Nothing in the ledger prose rounds favorably or omits a figure the producer actually printed.

## 3. Independent re-derivation of the construction's load-bearing identity

The construction's central move is the closed-form resummation $\sum_{n\ge1}(-s/n)\cos(n\pi x/L) = s\log(2\sin(\pi x/(2L)))$. This is the classical Fourier identity $\sum_{n\ge1}\cos(n\theta)/n = -\log(2\sin(\theta/2))$, $0<\theta<2\pi$. Using fresh `mpmath` code (not reading the producer), this auditor computed the partial sum to $N=20000$ at $x\in\{0.3,0.7,1.0\}$ ($\theta=\pi x/L$, $L=12/11$, $s=0.24060639745313878$) and compared against the closed form: differences of order $6\times10^{-6}$ at $N=20000$, consistent with the expected $O(1/N)$ convergence rate of this conditionally-convergent series — confirming the identity independently of the producer script.

## 4. Scope and honesty check

The entry is explicit that this is numerical verification on $t\in[0.02,30]$ at stated tolerances, not a proof (`verification_is_proof=false`; the class proof remains report 2 §3a from 2026-09-28). It is explicit that P is the quotient's own spectral distribution exhibited per the prior report's prescription, not an independent geometric derivation (`phase_derived_from_helix_first_principles=false`). It records its own debugging history honestly (a first attempt crashed at grid point ~7000 on an unguarded endpoint, fixed and rerun clean) rather than silently presenting a polished final run. No certified Suzuki object, paper, or threshold in the discriminant-12-return chain is touched.

## 5. Verdict

```
Confirmed: v14.596 is an honestly-scoped, numerically thorough closure
  of a tangential sandbox obstruction. Every cited number was
  reproduced exactly by an unmodified re-execution of the deposited
  producer, and the construction's central closed-form identity was
  independently re-derived from scratch and confirmed. No G is
  derived, no certified object or threshold in the discriminant-12-
  return chain is touched, and the scope flags match the content.
No defect found.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.597
status: open
action: this auditor independently verified v14.596 exactly, by full unmodified producer re-execution plus an independent from-scratch re-derivation of its central identity. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
