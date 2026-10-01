# Odd-sector analytic attack: is 0 ∈ σ(L_A^{(-)})?

**Sandbox only. NOT ledgered. No repo/ledger/research-notes writes.**
Date: 2026-10-01. Complements the audit thread's numerical reproduction of v13.912 §4
(which is not duplicated here). All numerics below serve the analytic question.

Status discipline: `[D]` derived, `[N]` numerical/provisional, `[I]` interpretation, `[O]` open.
λ = −1 throughout (Suzuki v2 sign convention k = g − λN; never λ = 0).

---

## 1. The precise question

L_A is the integral operator on (−A,A) with kernel k(x,y) = g(x−y) − λN(x,y),
λ = −1, g Suzuki's screw function, N(x,y) = (x²+y²)/(4A) − |x−y|/2 + A/6.
It commutes with reflection, so the odd sector L_A^{(-)} is well-defined.

**[D] 0 ∈ σ(L_A^{(-)}) is trivially true.** L_A^{(-)} is Hilbert–Schmidt, hence compact,
on infinite-dimensional L²; a compact operator cannot be surjective (else the identity
would be compact). The substantive question is the Fredholm dichotomy:

- (a) **0 is an eigenvalue**: ∃ nonzero odd u with L_A u = 0 (non-injective), or
- (b) **L_A^{(-)} is injective** with dense range and **unbounded** inverse
  (0 is an accumulation point / continuous spectrum, not an eigenvalue).

The moments M_{1x} = ℓ_1(L_A^{-1}x), M_{1e} need x, sinh−x ∈ Ran(L_A^{(-)}).
Case (a) kills them via ker^⊥ obstruction; case (b) kills them via Picard failure
(§6). Either way the §4 divergence is explained — but the *mechanism* and the
*remedy* differ completely, which is why the distinction matters.

---

## 2. Route A: parity reduction [D] — the odd sector on (0,A)

For odd u and x ∈ (0,A):
(L_A u)(x) = ∫_0^A [k(x,y) − k(x,−y)] u(y) dy.
With k(x,y) − k(x,−y) = [g(x−y) − g(x+y)] − λ[N(x,y) − N(x,−y)] and, for x,y > 0,

**[D]** N(x,y) − N(x,−y) = min(x,y),

since |x+y| = x+y gives −|x−y|/2 + (x+y)/2 = min(x,y). Hence the odd sector is
exactly the operator T_- on L²(0,A) with kernel

k_-(x,y) = [g(x−y) − g(x+y)] + min(x,y)      (λ = −1).

**[D]** min(x,y) is the Green's function of −d²/dx² on (0,A) with **Dirichlet at 0,
Neumann at A**: u(x) = ∫_0^A min(x,y)f(y)dy satisfies u(0) = 0,
u'(x) = ∫_x^A f, u'(A) = 0, −u'' = f. (The odd reflection of the Neumann problem
gives Dirichlet at 0; the Neumann BC at A is inherited.)

So **[D]** T_- = G_- + M, where M = (−Δ_{D0,NA})^{-1} > 0 has the explicit
eigensystem φ_k(x) = √(2/A)·sin((k+½)πx/A), eigenvalues
m_k = (A/((k+½)π))², k = 0,1,2,…, and G_- is the odd-sector convolution with
[g(x−y) − g(x+y)].

*Verification [N]:* the kernel identity holds pointwise to 2.2e−16; the odd-projected
Galerkin matrix QᵀKQ matches the direct (0,A) assembly with k_- on interior dofs
(1.7% on a checked entry; residual is the known |x−y|-kink quadrature in the
Toeplitz assembly, plus a boundary-dof artifact of the Toeplitz trick — both
negligible for the scaling study).

---

## 3. Route B: what Galerkin divergence can and cannot prove [D/I]

For compact self-adjoint T_-, the Galerkin method for the first-kind equation
T_-u = x can diverge **both** when 0 is an eigenvalue (case a) **and** when T_- is
injective with unbounded inverse (case b, Picard failure). The observed
M_{1x} ~ N^{0.7} divergence therefore does **not** by itself establish a null mode
— it is equally consistent with x ∉ Ran(T_-). Distinguishing requires the
eigenvector test (§4) and the Picard test (§6).

---

## 4. Route C: eigenvalue/eigenvector tracking [N] — no null mode

Odd-projected Galerkin (QᵀKQ, QᵀMQ) generalized eigenvalues, A = 2:

| N   | odd dofs | μ_min(T_-) | μ_2nd   | neg. eigs | dom. freq of min eigenvector |
|-----|----------|------------|---------|-----------|------------------------------|
| 400 | 200      | 2.82e−05   | 2.91e−05| 0         | 78                           |
| 800 | 400      | 8.64e−06   | 9.14e−06| 0         | 168                          |
| 1600| 800      | 2.45e−06   | 2.50e−06| 0         | 358                          |
| 3200| 1600     | 7.46e−07   | 7.46e−07| 0         | 646                          |

Findings:
- **No negative eigenvalues** at any N: the Galerkin T_- is positive definite.
- μ_min → 0 at ~m^{−1.74} (m = odd dofs), i.e. **slower** than the pure-Laplacian
  tail m^{−2} (the min-part alone tracks (A/mπ)² to 4.0× per doubling, exactly).
  The g-part shifts small eigenvalues **up** (μ_min ≈ 3–4× the Laplacian tail).
- **Decisive [N]:** the smallest eigenvector's dominant Fourier mode is
  78 → 168 → 358 → 646, i.e. ~0.4× Nyquist at every N — it tracks the mesh and
  becomes *more* oscillatory. A genuine null mode would converge to a fixed
  L² shape (fixed dominant frequency). This is the compact tail (accumulation
  at 0), **not** a resolving eigenfunction.

**[N] verdict of this route: 0 is not an eigenvalue of T_-.** The near-null
Galerkin modes (~1.6e−8 plain / ~1e−6 generalized, cf. v13.912 §4) are the
expected small eigenvalues of a compact operator, not a nullspace.

---

## 5. Route D: positivity of the odd convolution [N] + conditional [D]

Let G_- be the odd-sector convolution (kernel g(x−y) − g(x+y)) and test its
Galerkin generalized eigenvalues against the P1 mass matrix:

| A   | N=400 min | N=800 min | #negative (full spectrum) | max eig |
|-----|-----------|-----------|---------------------------|---------|
| 1.0 | 1.21e−06  | 3.46e−07  | 0                         | ~0.010  |
| 2.0 | 3.32e−06  | 1.02e−06  | 0                         | ~0.020  |
| 4.0 | 6.37e−06  | 1.71e−06  | 0                         | ~0.039  |

**[N]** The odd-sector G_- is positive definite in Galerkin (zero negative
eigenvalues across A and N; max eigenvalue stable under refinement). The min
→ 0 is the compact tail.

**[D, conditional]** If G_- ≥ 0 as an operator, then T_- = M + G_- ≥ M > 0:
⟨Mu,u⟩ = ‖v'‖² > 0 for u ≠ 0 (v = Mu ∈ H², mixed BCs, integration by parts),
so ⟨T_-u,u⟩ > 0 ∀u ≠ 0 — T_- is **strictly positive definite, hence injective**,
and 0 cannot be an eigenvalue. This would promote §4's [N] to [D].

**[I]** What G_- ≥ 0 means: with ũ the odd extension of u (∫ũ = 0),
⟨G_-u,u⟩ = ½∫_{−A}^A∫_{−A}^A g(x−y)ũ(x)ũ(y)dxdy, so positivity is
positive-definiteness of Suzuki's screw kernel on mean-zero (odd) functions —
equivalently ĝ ≥ 0 as a distribution (Bochner). This is Krein screw-function
territory: it holds iff g is a screw function in Krein's sense on this class.

**[O]** Prove G_- ≥ 0 analytically (via ĝ ≥ 0 from the explicit formula, or via
Krein's screw-function characterization of Suzuki's g). This is the single
most valuable analytic target: it closes injectivity in one step.

---

## 6. Route E: Picard test [N] — the actual obstruction

Expand the x-source in the Galerkin eigensystem (N = 3200, A = 2):
partial sums of Σ|⟨x,ψ_j⟩|²/μ_j² (eigenvalues ascending):

4.5e+04 → 7.8e+07 → 1.2e+08 → 1.6e+08 → 2.0e+08 → 2.3e+08 → 2.4e+08 → 2.5e+08
(still growing at the last mode).

**[N]** The Picard series diverges: **x ∉ Ran(T_-)**. The formal solution of
T_-u = x is not an L² function. This is the precise mechanism of the v13.912 §4
divergence — an **unbounded-inverse / Picard failure** (case (b)), not a null
mode (case (a)).

Control: the even sector's 1-source Picard sums (49 → 89 → 126 → 246, far
smaller) and its convergent moments show the method resolves solvable cases;
the odd x-source is genuinely outside the range. (Note: the even sector has one
negative Galerkin eigenvalue ≈ −0.27 — the even operator is indefinite, a
separate matter not affecting the odd question.)

**Consequence [N/I]:** M_{1x} = ℓ_1(L_A^{-1}x) and M_{1e} do not exist as L²
moments. The analytic identity M_{1x} = 1 ([D], Round 133) is vacuous — its
hypothesis ("u = L_A^{-1}x exists in L²") fails. The r_1 half of the v13.757
gate is not merely untestable with the current discretization; on the present
evidence the moments it needs **do not exist**. Any reformulation of the gate
must either project the sources onto Ran(T_-) or work with the pseudoinverse.

---

## 7. Routes F/G: Birman–Schwinger and Fredholm determinant [I/O]

**Attempted.** The naive Birman–Schwinger operator S = M^{-1/2}G_-M^{-1/2} is
**not bounded on L²**: G_- gains only one derivative (g is C⁰ with kinks), so
S : L² → H^{-1}. The form-domain version is the correct setting, but needs more
machinery than this session. The computable proxy is the generalized eigenvalue
problem G_-u = −νMu (§5): no generalized eigenvalue near −1 (G_- > 0 in
Galerkin), consistent with no null mode.

The parity-reduced Fredholm determinant det(K_odd) > 0 at all N (positive
definiteness) but → 0 as N → ∞ (compact tail) — not informative about
eigenvalues. The determinant that would matter is det_2(I + G_-M^{-1}) on the
form domain, i.e. again the (G_-, M) pencil.

**[O]** A rigorous BS/form-domain treatment, or the ĝ ≥ 0 proof of §5.

---

## 8. Route H: deficiency vectors v_{A,±} [I]

From v13.745/v13.757: the deficiency equation is
L_A v_A = C_A e^x + A_A x + B_A, with reflection-compatible normalization
v_{A,−} = Rv_{A,+}. Its odd part needs sinh, x ∈ Ran(L_A^{(-)}).
**Nothing in the closed form of v_{A,±} forces or forbids a null odd mode** —
the equation is scale-homogeneous (v13.745 §7) and assumes R_A exists. The
invertibility question is purely about Ran(L_A^{(-)}), answered (numerically)
by §4–§6 above. Route H adds no independent leverage.

---

## 9. Verdict: **NARROWED** (not resolved)

| Question | Status |
|----------|--------|
| 0 ∈ σ(L_A^{(-)})? | **[D] Yes, trivially** (compactness). |
| 0 an eigenvalue (non-injective)? | **[N] No** — eigenvector non-convergence (§4), Galerkin positive definite (§4–§5). |
| L_A^{(-)} injective? | **[N] Yes** (same evidence); **[D] iff G_- ≥ 0 proved** (§5). |
| x ∈ Ran(L_A^{(-)})? | **[N] No** — Picard divergence (§6). |
| M_{1x} = 1 applicable? | **[D] Hypothesis fails** — no L² preimage of x. |
| r_1 gate testable? | **[N] No** — moments don't exist, not just ill-conditioned. |

**The obstruction is precisely characterized:** the odd sector is (numerically)
injective with **unbounded inverse**; the §4 divergence is **Picard failure**
(x outside the range), not a null mode and not a λ-resonance. The v13.912 §5
route 1 question is therefore answered in the negative in the sense that
matters: there is no odd null mode to find, and the missing ingredient was
never 0 ∈ σ_p but x ∈ Ran.

### What would close it (in dependency order)

1. **[O, highest value]** Prove G_- ≥ 0 analytically (ĝ ≥ 0 via the explicit
   formula, or Krein's screw-function theory for Suzuki's g). Promotes
   injectivity §4–§5 from [N] to [D] in one step.
2. **[O]** Prove the Picard divergence with two-sided eigenfunction bounds for
   T_- (needs the eigenfunction asymptotics of M + G_-; the numerics suggest
   μ_k decays slower than the Laplacian 1/k² because the order-1 G_- dominates
   the tail).
3. **[O]** If (1) is proved, reformulate the v13.757 r_1 gate with the
   pseudoinverse / range-projected sources, since M_{1x}, M_{1e} as stated do
   not exist.

### Deliberately not done

- No re-verification of the §4 divergence table (audit thread's job).
- No λ = 0 solves (canary).
- No ledger/research-notes writes (sandbox report only).

---

## Appendix: method notes

- Odd projection Q: columns (φ_i − φ_{N−i})/√2, i < N/2 (middle node is even).
  [D] kernel identity k(x,y) − k(x,−y) = [g(x−y) − g(x+y)] + min(x,y) verified
  pointwise to 2.2e−16; projection matches direct (0,A) assembly on interior dofs.
- The r_gate.py Toeplitz assembly has a known ~7% diagonal error from the g-kink
  at t = 0 (Gauss-Legendre across the kink) and a boundary-dof artifact (half-hat
  vs full-hat); both verified negligible for the scaling conclusions (interior
  entry matched an analytic dblquad to 1.7%; max G_- eigenvalue stable across N).
- Generalized eigenproblems via scipy.linalg.eigh; Picard sums from the
  M-orthonormal Galerkin eigensystem at N = 3200 (1601 odd dofs).
- Portability note (from audit Round 134's self-audit): newer scipy versions
  removed the `eigvals=` keyword from `eigvalsh` (and it no longer returns
  eigenvectors) — use `eigh` with `subset_by_index` instead. "The code runs as
  posted" is environment-dependent.
