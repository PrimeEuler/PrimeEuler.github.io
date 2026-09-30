# Cone Derivation Ledger v13.880 — Sandbox: Characteristic Function W_K — Corrected Deficiency Vectors, Lattice Zeros, and the Finite-Section Barrier

**Status:** [D] transfer lemma formulation; [N] numerical lattice and theta-dependence; [I] finite-section barrier interpretation.
**Date:** 2026-09-30
**Author:** LIttle Euler (sandbox)
**Depends on:** v13.275 (transfer lemma), v13.878 (D12 war).

## Summary

We computed the finite-section characteristic function W_K(a,θ;z) for the Riemann case using the CORRECT deficiency-vector formulation from v13.275's transfer lemma. Findings:

1. **Corrected formulation:** v_± = T^{-1}e^{±x} where T = A−λI > 0 (λ < inf σ(A)), via REAL linear solve — not (A∓iI)^{-1} as in an earlier incorrect implementation.
2. **Lattice persists:** W_K zeros form a regular lattice at odd multiples of π/(2a), spacing π/a — in both formulations.
3. **Theta-dependence is real but weak:** corrected v_± show θ-dependent |W| values (unlike the incorrect formulation which showed exact θ-independence).
4. **Finite-section barrier:** the matrix A is self-adjoint, hence has no deficiency indices. Finite-section cannot capture the (1,1) structure. The true war requires the infinite-dimensional T.

---

## 1. The transfer lemma (v13.275 §3) [D]

Let A be self-adjoint lower-bounded on L²(−a,a). Choose λ < inf σ(A), define T = A−λI > 0.

The symmetric first-order operator 𝓓 = i·d/dx with compactly-supported core has deficiency spaces spanned by:

```
v_+ = T^{-1} e^x,    v_- = T^{-1} e^{-x}
```

More generally, v_z = T^{-1}e^{-izx} is the adjoint eigenvector for spectral parameter z.

The characteristic function:

```
W_K(a,θ;z) = (z−i)∫ v_+(x)e^{izx}dx + e^{iθ}(z+i)∫ v_-(x)e^{-izx}dx
```

has only real zeros for each finite a. The conjectured GRH route (v13.275 §8–9):

```
e^{φ_K(a,z)} W_K(a,θ(a);z) → R_K(z) := ξ_K(1/2−iz)/(ξ_K(1/2−iz)+ξ_K'(1/2−iz))
```

locally uniformly near arithmetic zeros, whence Hurwitz forces reality of zeta zeros.

**Open per v13.275:** construction of φ_K (item 4), convergence theorem (item 5).

---

## 2. Corrected numerical implementation [N]

### 2a. What was wrong

An initial implementation solved (A∓iI)v_± = c^± (complex linear systems). This is NOT what the transfer lemma says. The lemma requires:

- T = A − λI with λ < inf σ(A) (REAL shift making T positive definite)
- T·v_± = e^{±x} (REAL linear systems)

### 2b. Corrected method

For Riemann a=1, modes 21–99:
- λ_min(A) = +0.2457
- λ = λ_min − 1.0 = −0.7543 (so T = A−λI > 0)
- c^±_n = ∫_0^{2a} e^{±x} sin(nπx/2a)dx (closed form)
- Solve T·v_± = c^± (real)
- W_K via closed-form sine integrals S_n(z) = ∫_0^{2a} sin(nπx/2a)e^{izx}dx

### 2c. Results: lattice persists

Zeros found (|W| < 0.1), Riemann a=1, θ=0:

| z | |W| |
|---|---|---|
| ±1.58 | 0.0015 |
| ±4.72 | 0.0035 |
| ±7.86 | 0.0047 |
| ±11.00 | 0.0049 |
| ±14.14 | 0.0042 |
| ±17.28 | 0.0024 |
| 0.00 | 0.0724 (marginal) |

Locations IDENTICAL to the incorrect formulation: odd multiples of π/2, spacing π. The lattice is robust, not an artifact of the wrong linear solve.

A worker-agent sweep (modes 21–199, a∈{1,2,3}, θ∈{0,π/2,π}) confirmed:
- a=1: spacing π; a=2: spacing π/2; a=3: spacing π/3 (breaking down, |W| too large)
- Pattern: W_K(z) ≈ cos(a·z)
- Zeros become DENSE as a→∞ (spacing π/a → 0)
- Do NOT resemble zeta zeros (regular lattice vs. irregular γ≈14.13, 21.02, …)

### 2d. Theta-dependence: weak but real

Corrected method, Riemann a=1:

| θ | z=1.58 | z=4.72 | z=7.86 |
|---|---|---|---|
| 0 | 0.001537 | 0.003496 | 0.004652 |
| π/2 | 0.001269 | 0.002962 | 0.004008 |
| π | 0.001371 | 0.002728 | 0.003575 |

The incorrect formulation showed EXACT θ-independence (identical zeros). The corrected formulation shows θ-dependent |W| values — weak, but real. Different self-adjoint extensions DO give different W_K, as theory demands. The (1,1) structure is partially captured.

---

## 3. The finite-section barrier [I]

The matrix A (190×190, symmetric) is self-adjoint on ℂ^190. It has NO deficiency indices — deficiency is a property of symmetric (non-self-adjoint) operators.

Our "deficiency vectors" v_± = T^{-1}e^{±x} are well-defined (T > 0), but they do not span deficiency spaces of A (there are none). They are best understood as finite-section approximations to the true infinite-dimensional deficiency vectors.

Consequences:
- The weak θ-dependence reflects partial capture of the (1,1) structure.
- The lattice zeros (spacing π/a) are a finite-section artifact — the true W_K (infinite-dimensional) need not have this pattern.
- Fixed-θ finite-section W_K cannot address the GRH limit; the dense lattice is not the obstacle the theory predicts (the theory predicts isolated zeros converging under renormalization).

**The true war** requires either:
(a) solving the infinite-dimensional adjoint problem T*v = ±i·v directly (PDE/ODE), or
(b) finding a discretization that preserves deficiency indices (e.g., via boundary triplets or Krein's formula), or
(c) working with the resolvent (T*∓i)^{-1} in infinite dimensions.

Matrix numerics have reached their structural limit on this question.

---

## 4. What the numerics DID establish [N]

1. **Positivity dies at a=2** (v13.878): λ_min = +0.23 (a=1) → −3.07 (a=2) → −5.89 (a=3). Prime tail overwhelms archimedean background.
2. **Transfer lemma formulation is correct and implementable:** v_± = T^{-1}e^{±x} with T = A−λI > 0 gives θ-dependent W_K with real zeros.
3. **Lattice is robust:** persists across correct/incorrect formulations, mode cutoffs, and θ values. It is the finite-section signature, not the infinite-dimensional truth.
4. **Renormalization is necessary:** even the correct finite-section W_K gives a dense lattice as a→∞, confirming v13.275's assessment that e^{φ_K}W_K(a,θ(a);z) with a-dependent θ(a) is the object that must converge — not fixed-θ W_K.

---

## 5. Files

Sandbox (not for ledger promotion without review):
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/deficiency_W.py` — INCORRECT formulation (A∓iI)^{-1}, kept for provenance
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/deficiency_W_correct.py` — CORRECTED (T=A−λI, real solve)
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/find_zeros.py` — zero finder
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/test_theta_correct.py` — θ-dependence test
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/W_zeros_sweep.py` — worker sweep driver
- `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/W_zeros_sweep.json` — worker results (9 (a,θ) combos)

---

## Synchronization

Live GitHub ledger head checked immediately before this write: v13.879. No collision on v13.880. **This entry does not audit v13.879 or earlier.**
