# Cone Derivation Ledger v13.904 — Sandbox Analytic Skeleton: Contraction Theorem Behind the Exact Kink-Loadings

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("yes ledger then continue" following the analytic-origin report).

Predecessors: v13.902 (rigidity experiment: Λ an isolated maximizer of λ₁; exact V-slopes s_m = c_m; level-crossing mechanism), and the sandbox-only analytic investigation `analytic_origin_kink_loadings.md` (run dir `runs/20260930-divisor-tension/`), which this entry records.

Status: **[D]** for the three derivations below (elementary; proofs sketched in full); **[N]** for the saturation and shift-norm observations; **[I]/[O]** for interpretation and the missing lemma. No RH/GRH claim. This entry explains the *values* behind v13.902's exactness; it does not extend the selection claim beyond v13.902's honest scope (weights, not ordinates).

## 1. The three numerical facts are one fact [D, via Danskin]

f(w) = λ₁(Q(w)) with Q affine in w is a pointwise minimum of affine functions, hence concave [D]. By Danskin's theorem, the one-sided directional derivatives along the single-kink ray w(ε) = Λ + εc_m e_m are c_m times the extremal null-cluster kink-loadings. The observed [N] V-shape λ₁(ε) = −s_m|ε| then gives min/max loadings = ∓s_m/c_m, so:

> **s_m = c_m ⟺ the null cluster achieves kink-loadings exactly ±1. [D, conditional on the [N] V-shape]**

Convexity explains the V-structure, its symmetry, and the level-crossing form — but it cannot produce the *value* ±1. That comes from the kernel.

## 2. The kink stiffness is a truncated shift [D]

For the pure kink g_m(t) = (|t| − h)_+, h = log m, and u,v ∈ H¹_0(−a,a), two integrations by parts (boundary terms vanish by Dirichlet BC; g_m'' = δ_h + δ_{−h} in D′) give:

> KK[m](u,v) = ∫∫ [δ(x−y−h) + δ(x−y+h)] u(x)v(y) dx dy. [D]

The kink stiffness is a sum of two truncated shifts; the loading is twice the (normalized) autocorrelation at lag h = log m [D].

## 3. Contraction theorem [D] — the centerpiece

> **Theorem.** For h = log m > a: −M ≤ KK[m] ≤ M as quadratic forms on H¹_0(−a,a) (hence on the P1 FEM subspace).

*Proof.* KK[m](u,u) = 2∫_{−a+h/2}^{a−h/2} u(z+h/2)u(z−h/2)dz ≤ ∫_{−a+h}^{a} u² + ∫_{−a}^{a−h} u² (2pq ≤ p²+q², change of variables). For h > a the intervals [−a+h,a] ⊂ [0,a] and [−a,a−h] ⊂ [−a,0] are disjoint, so the sum ≤ ‖u‖². The lower bound is identical with −2pq ≤ p²+q². ∎

**Corollary [D]:** for every well-resolved kink (log m > a), the V-slope satisfies **s_m ≤ c_m** — the von Mangoldt coefficient is an analytic upper bound on the V-slope. (Along w(ε) = Λ + εc_m e_m: λ₁(ε) ≥ λ₁(Q_full) − εc_m via KK[m] ≥ −M; the right-derivative gives −s_m ≥ −c_m.)

**Numerical validation [N]:** the largest generalized eigenvalue of (KK[m], M) drops to 1.0000 (4 digits) exactly when log m crosses a — tested a = 1, 2, 3 (transition at m = e^a). The [D] bound is tight.

## 4. The small-kink "anomalies" are exact shift-norms [N]

For log m < a the disjointness argument fails and ‖KK[m]‖ > 1; numerically the norm is **2cos(π/k)** for integer k, N-stable to 7 digits (e.g. a=2: m=2 → 2cos(π/7) = 1.8019377, m=3 → φ, m=4 → √2), matching the V-slope ratios s_m/c_m. The ratios move with a (m=2: 1.4142/1.8019/1.9021 at a=1/2/3) — **finite-a window effects**, the same contraction mechanism below threshold. The √2 at m=4 is the k=4 rung, not tower physics (|λ₁(minus_4)| = √2·c_4 = c_2 is arithmetic: Λ(4) = Λ(2)). The k(m,a) pattern and its proof remain [O].

## 5. The missing lemma [O]

Half-derived, precisely: the [D] half says ±1 is the largest possible loading; the [N] half says the null cluster attains it (saturation). **Why the null cluster contains the contraction-saturating directions is open** — stationarity only forces the balanced cluster (loadings average to zero per kink), not the extremal magnitudes. A proof needs to exhibit or force these directions (stronger KKT/complementary-slackness for the maximin problem, or an explicit approximate null-vector construction). This is the single step between the current [N] exactness and a **[D] rigidity theorem**. Further open: the 2cos(π/k) proof, the m=7 exception (null max 1.21 < global max √2 — the one non-saturating kink), closed forms for the extremal null vectors, and the downstream weights→ordinates chain (strong form of the heresy untouched).

## 6. What this is not

- **Not a rigidity theorem yet.** The saturation half is numerical; the missing lemma is the gap.
- **Not an RH result.** It explains values (why the maximizer's coordinates involve Λ(n)/√n-shaped bounds), not zeros.
- **Not connected to the twisted channel or the de Branges line.**

**Version note:** drafted as v13.903; the auditor thread's v13.903 (Voronoi debugging saga — read, no content interaction with this entry) landed mid-write, so this takes v13.904.

## Synchronization

Live ledger head checked immediately before this write: v13.903 (auditor thread, Voronoi saga — read in full). No collision on v13.904.
