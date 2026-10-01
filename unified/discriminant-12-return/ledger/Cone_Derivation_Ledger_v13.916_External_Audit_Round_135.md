# Cone Derivation Ledger v13.916 — External Audit Round 135

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.915` §1 (`research-notes/odd_sector_analytic.md`) — the analytic
narrowing of the de Branges odd-sector question (`v13.912`), which reframes
Round 134's confirmed numerical symptom as specifically **Picard failure**
(`x ∉ Ran(T_-)`), not a null mode. `v13.915` §2 (the selector-principle /
compression-cone handoff bundle) was read in full per protocol but is
explicitly addressed to the Lane A worker, not this thread; noted below,
not independently verified.

Verdict: **Confirmed, via a completely independent from-scratch
implementation** — new code, not reusing `r_gate.py`'s assembly or odd-sector
projection, with my own independently-built `g(t)` (from Round 134). Every
numbered claim in `odd_sector_analytic.md` that is checkable without new
analytic machinery reproduces. One honest bump: my first attempt at the
Picard-sum computation had a coefficient-convention bug that made it look
flat; caught via a Parseval cross-check against a direct linear solve, fixed,
and the corrected computation shows clean, unambiguous divergence.

## 1. The two analytic claims — checked by hand, then numerically

**Kernel identity**: for `x,y > 0`, `N(x,y) − N(x,−y) = min(x,y)`, where
`N(x,y) = (x²+y²)/(4A) − |x−y|/2 + A/6`. By hand: the `(x²+y²)/(4A)` and
`A/6` terms cancel in the difference (even in `y`); what remains is
`−|x−y|/2 + |x+y|/2`, which for `x,y>0` is `(x+y)/2 − |x−y|/2`, splitting to
`y` when `x≥y` and `x` when `x<y` — exactly `min(x,y)`. Confirmed numerically
at three cases (`x>y`, `x<y`, `x=y`) to floating-point exactness.

**`min(x,y)` is the Green's function of `−d²/dx²` on `(0,A)` with Dirichlet
at 0, Neumann at `A`**: for `u(x) = ∫_0^A min(x,y)f(y)dy`, splitting the
integral at `y=x` and applying Leibniz gives `u'(x) = ∫_x^A f(y)dy` (the two
boundary terms from differentiating the split cancel), hence `u(0)=0`,
`u'(A)=0`, `−u''=f`. Independently re-derived by hand, then checked against
the claimed explicit eigensystem `m_k = (A/((k+½)π))²`: built this exact
operator (kernel `min(x,y)` only, no `g`) via my own from-scratch P1 Galerkin
assembly and solved the generalized eigenproblem. The top 5 eigenvalues
matched `m_k` for `k=0..4` to `1e-7`–`1e-5` relative error — this also
validated my FEM assembly machinery itself before trusting it on the full
problem.

## 2. Independent from-scratch assembly of `T_-`

Wrote `odd_sector_independent.py`: direct element-Gauss (8-point) P1 Galerkin
assembly of `T_-` on `(0,A)` with kernel `k_-(x,y) = [g(x−y) − g(x+y)] +
min(x,y)`, dofs = nodes 1..N_sub (node 0 dropped for Dirichlet, node N_sub
kept for natural Neumann), using Round 134's independently-built `g(t)`. Not
a single line reused from `r_gate.py`'s assembly or odd-projection code —
this is a second, independent route to the same operator. Spot-checked one
matrix entry (`T[0,0]` at `N_sub=4`) against a brute-force `scipy.dblquad`
and matched to 0.15% (consistent with 8-point Gauss not fully resolving the
`min(x,y)` kink inside a single element — expected, negligible at scale).

## 3. No negative eigenvalues — confirmed

| N_sub | neg. eigs (full T_-) | μ_min | μ_2nd |
|---|---|---|---|
| 100 | 0 | 7.28e-05 | 7.62e-05 |
| 200 | 0 | 2.61e-05 | 2.87e-05 |
| 400 | 0 | 1.15e-05 | 1.21e-05 |

Matches §4's claim: the odd-projected Galerkin operator is positive definite
at every resolution tested.

## 4. `G_-` isolated positivity — confirmed, including the magnitude

Rebuilt the convolution-only piece (`g(x−y) − g(x+y)`, dropping `min(x,y)`)
separately and solved its own generalized eigenproblem:

| N_sub | min eig(G_-) | max eig(G_-) | n_negative |
|---|---|---|---|
| 100 | +1.20e-05 | +2.0084e-02 | 0 |
| 200 | +9.45e-06 | +2.0081e-02 | 0 |
| 400 | +8.68e-06 | +2.0080e-02 | 0 |

Zero negative eigenvalues at every resolution, and the max eigenvalue is
stable at **≈0.0201**, matching §5's reported magnitude (~0.020 at A=2)
almost exactly despite completely independent code and `g(t)`. Strong
corroboration of Route D's numerical claim.

## 5. Dominant eigenvector frequency tracks the mesh — confirmed qualitatively

| N_sub | dominant FFT freq of μ_min eigenvector | fraction of N_sub |
|---|---|---|
| 100 | 49 | 0.49 |
| 200 | 98 | 0.49 |
| 400 | 188 | 0.47 |

Consistently ~0.47–0.49 of `N_sub` at every resolution — never settling to a
fixed absolute frequency, i.e. a compact tail, not a converging eigenfunction.
This is the same qualitative finding as §4's table (there ~0.4× the odd-dof
count). The precise fraction differs (0.47–0.49 vs their ~0.40); most likely
explanation is differing treatment of the `g`-kink at `x=y` under 8-point
element-Gauss vs their Toeplitz-grid quadrature (their own Appendix flags a
~7% diagonal quadrature error from exactly this kink). Doesn't affect the
qualitative conclusion, which is what the claim rests on.

## 6. Picard-sum divergence — confirmed, after catching my own bug

First attempt: expanded the x-source in the `M`-orthonormal Galerkin
eigenbasis using `coeffs = V.T @ (M @ bx)`, which gave an apparently flat
total (`≈50–55` at `N_sub=100,200,400`) — looked like convergence, in tension
with Round 134's own prior direct-solve divergence. Didn't trust it: cross-
checked via Parseval against a plain linear solve, `‖T⁻¹b_x‖²_M` vs the
eigen-expansion sum, and they didn't match (153 vs 84885 at `N_sub=400`) —
proof of a bug, not a result. Root cause: `scipy.linalg.eigh(T,M)` normalizes
eigenvectors so `V.T @ M @ V = I`, so the correct expansion coefficients are
`coeffs = V.T @ bx` (not `V.T @ (M @ bx)`); with that fix, the eigen-
reconstructed solution matched the direct solve to `1e-12` relative error.

Corrected Picard sum (`= Σ coeffs_j²/μ_j² = u^T M u`, confirmed via Parseval):

| N_sub | Picard sum (= `u^T M u`) |
|---|---|
| 100 | 71.4 |
| 200 | 104.6 |
| 400 | 153.2 |
| 800 | 324.2 |

Clean, monotonic, accelerating growth — no sign of saturation through four
doublings. This is the corrected version of §6's claim, independently
reproduced: `x ∉ Ran(T_-)` in the only sense a finite discretization can show
it (the Picard proxy grows without bound under refinement).

## 7. Cross-check: direct linear solve also diverges

Independently of the eigen-expansion, solved `T_- u = b_x` directly at each
`N_sub` and tracked `‖u‖₂` and `cond(T_-)`:

| N_sub | ‖u‖₂ | cond(T_-) |
|---|---|---|
| 100 | 103.2 | 6.72e+04 |
| 200 | 167.8 | 1.90e+05 |
| 400 | 291.4 | 4.36e+05 |
| 800 | 653.3 | 6.00e+06 |

Both the solution norm and the condition number grow sharply and without
leveling off — a third independent angle (on top of Round 134's full-domain
direct solve, which used different code entirely) confirming the same
divergence.

## Verdict: agree with `v13.915`'s narrowing

My independent checks support every row of their summary table:

- `0 ∈ σ(L_A^{(-)})`: trivially true by compactness — standard operator
  theory, not something to numerically re-derive, and uncontested.
- `0` **not** an eigenvalue: confirmed (positive-definite Galerkin at every
  resolution, no converging null eigenvector).
- `L_A^{(-)}` injective with unbounded inverse: consistent with all evidence
  (no null mode found; divergence present via two independent numerical
  routes — Picard sum and direct solve).
- `x ∉ Ran(T_-)`: confirmed (Picard sum diverges cleanly once my bug was
  fixed).
- `M_{1x}=1`'s hypothesis fails, so the identity is vacuous, and the `r_1`
  gate is not testable as currently stated: both are direct logical
  consequences of the above, not separately numerical — agree.

**What remains open, unchanged from `v13.915`:** neither I nor the sandbox
report proved `G_- ≥ 0` as an analytic fact (only numerically, at finite
resolution) — that is the single highest-value remaining step, promoting
injectivity from `[N]` to `[D]`. Nor did either side prove the Picard
divergence with two-sided eigenfunction bounds. Both are genuinely open
analytic questions; nothing in this round closes them.

## Note on `v13.915` §2 (not independently verified this round)

Read `compression_cone_handoff_README.md`, `selector_theory_derivation.md`,
and `selector_principle_exploration.md` in full per the standing protocol.
This bundle is explicitly addressed to the Lane A worker (the cone-geometry
program), carries its own `[D]`/`[N]`/`[I]`/`[O]` tags, and makes no RH
claims — the selector-principle derivation (§1 of that bundle) reads as
sound standard analytic number theory (Guinand–Weil / Riemann–von Mangoldt
explicit formulas, correctly flagged as RH-agnostic), and the "positivity
selects" exploration is honestly scoped as philosophy pending a uniqueness
theorem. Since this is routed to a different worker and not addressed to the
audit thread, I did not spend independent-verification budget on it this
round; flagging only that it was read in full, consistent with the standing
protocol, and nothing in it raised a concern.

## Self-audit note

The Picard-sum bug above is worth keeping as a general caution for anyone
reusing `eigh(T, M)`-based Picard/Parseval computations: the `M`-orthonormal
convention means source-vector expansion coefficients are `V.T @ b`, **not**
`V.T @ (M @ b)` — the extra `M` silently produces a wrong but plausible-
looking (flat, bounded) answer rather than an obvious crash, which is exactly
the dangerous kind of bug. Caught here only because the result contradicted
an already-trusted independent check (Round 134's direct solve); it would not
have been caught by code review alone.

## Result

\[
\boxed{\textbf{`v13.915` §1's odd-sector analytic narrowing (0 is not an
eigenvalue; the divergence is Picard failure, } x\notin\mathrm{Ran}(T_-)
\textbf{) is independently confirmed via a completely fresh implementation:
the kernel identity and Green's-function characterization by hand and to
high numerical precision; no negative eigenvalues of } T_-\textbf{ and of }
G_-\textbf{ alone at three resolutions; the } G_-\textbf{ max-eigenvalue
magnitude (≈0.020) matched almost exactly; the near-null eigenvector's
non-convergent, mesh-tracking frequency reproduced qualitatively; and the
Picard-sum divergence reproduced cleanly (71→105→153→324 over four
doublings) after catching and fixing a coefficient-convention bug in my own
first attempt, cross-validated by an independent direct-solve divergence
check.} \textbf{The remaining open items — an analytic proof that }
G_-\geq 0\textbf{, and two-sided eigenfunction bounds for the Picard
divergence — are unchanged and still open.}}
\]
