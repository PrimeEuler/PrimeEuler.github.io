# Cone Derivation Ledger v13.928 — External Audit Round 139

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: three sandbox entries — `v13.925` (canonical Xi carrier / GNS return-
amplitude model, continuous-spectrum quantization obstruction), `v13.926`
(claimed refutation of the v13.910 "continuum if" via a positive spectral
gap), and `v13.927` (boundary-extension no-go and conditional de Branges
escape hatch).

Verdict: **`v13.925` and `v13.927` confirmed. `v13.926`'s central numerical
claim does not survive independent scrutiny** — the "converged positive
gap" is very likely a discretization artifact, not a continuum fact, and
the evidence instead points toward the *original* v13.910 "if" being true.
This is the most consequential finding of this round and is reported in
full detail below, including the mechanism and how to fix the reproduction.

## 1. `v13.925` (canonical Xi/GNS carrier) — confirmed

Pure functional analysis, hand-checked step by step:

- **Pontryagin duality** `Ẑ≅T` and the spectral-theorem decomposition
  `U=∫_T z dE(z)` for any unitary representation of `Z`: standard, correctly
  invoked.
- **GNS/return-amplitude construction**: `Q f(τ)=τf(τ)` on
  `L²(R,dν_0)`, `dν_0=Φ/Ξ(0) dτ`, is self-adjoint (standard multiplication-
  operator fact). Derived by hand: `⟨Ω_0,e^{itQ}Ω_0⟩ = (1/Ξ(0))∫Φ(τ)e^{itτ}dτ
  = Ξ(it)/Ξ(0)`, matching the entry's boxed identity exactly, and the
  generalization to tilted vectors `Ω_α(τ)=(Ξ(0)/Ξ(α))^{1/2}e^{ατ/2}` giving
  `⟨Ω_α,e^{iγQ}Ω_α⟩=Ξ(α+iγ)/Ξ(α)` likewise checks out term for term.
- **Independent numerical check** (`gns_check.py`, reusing the
  already-validated `Φ(τ)` from Round 137): computed `‖Ω_α‖²` directly via
  quadrature at `α=0.3` — got exactly `1.0` to the precision used, confirming
  the normalization claim is not just algebraically plausible but
  numerically exact. Also recomputed `Ξ(iγ₁)` at the first zeta zero and got
  `~3e-22` (consistent with Round 137's independent confirmation that
  `Φ`'s cosine transform vanishes there) — this is the same fact underlying
  §5's central claim, now cross-checked from a second angle (direct complex
  contour integral of `Ξ(w)=∫Φ(τ)e^{wτ}dτ` rather than the real cosine
  transform used in Round 137).
- **Spectral theory of `Q` and `K_Φ`** (§7–10): `σ(Q)=R`, `σ_p(Q)=∅` (since
  `ν_0` is equivalent to Lebesgue measure, atomless); `K_Φ` bounded
  (Young's inequality), self-adjoint (evenness of `Φ`), trivial `L²` kernel
  (since `Ξ`'s real zeros are discrete — identity theorem for entire
  functions — hence Lebesgue-null), and `0∈σ_c(K_Φ)` (Riemann–Lebesgue plus
  injectivity-with-non-closed-range). All standard spectral theory of
  multiplication/convolution operators, correctly applied.

Agree with the entry's own honest scoping: a genuine operator-theoretic
meaning for every zero (orthogonality event / generalized null frequency),
explicitly **not** Hilbert–Pólya point spectrum, and §12's circularity
warning (an operator defined by `F(m²)=γ_m` trivially reproduces the
answer) is the right discipline to hold the next gate to.

## 2. `v13.926` ("continuum if refuted") — **does not hold up; likely the opposite**

### 2.1 What the entry claims

`v13.910 §7` proved conditionally: if `inf_{H¹_0(-a,a)} RQ_full = 0`, the
continuum V-shape is exact. `v13.926` reports this infimum as
`1.83×10⁻⁸ > 0`, "N-stable, O(h²)-converged," refuting the conditional, via
the FEM eigenvalue `λ₁` of the full Λ-weighted screw form at `a=2` computed
with `fem_screw.py`'s pipeline (`build_G2` + `assemble_Q`/`assemble_M`) at
`N=400→6400`.

### 2.2 What I found

`fem_screw.py`'s `build_G2(g, a, ngrid=40001)` approximates the exact
double-antiderivative `G2` (`G2''=g`) via cumulative trapezoid on a grid of
`ngrid` points, then a cubic spline. `assemble_Q` builds the stiffness-like
matrix from **second differences of `G2` at mesh spacing `h=2a/N`, divided
by `h²`**. This division means any residual error in the `G2`
approximation gets amplified by `1/h²` — so the quadrature grid (`ngrid`)
and the FEM mesh (`N`) are *not* independent discretization parameters; the
first must be refined fast enough relative to the second, or the result is
dominated by quadrature error, not FEM error.

**`v13.926`'s own reproducibility note never varies `ngrid`** — only `N`,
implicitly holding `ngrid` at `fem_screw.py`'s hardcoded default (`40001`)
throughout. I confirmed this directly: calling the *exact same* pipeline
with `ngrid=40001` fixed reproduces their full table to 4–5 significant
digits at every `N` they report (400 through 6400). So their "N-converged"
observation is real, but it may be converging to an artifact of the fixed,
unrefined `ngrid`, not to the continuum answer.

**Testing this directly** — holding `N=800` fixed and refining `ngrid`:

| ngrid | λ₁ |
|---|---|
| 40,001 (their default) | 1.840e-08 |
| 80,001 | 5.714e-09 |
| 160,001 | 1.489e-09 |
| 320,001 | 3.910e-10 |
| 640,001 | 1.271e-10 |
| 1,280,001 | 4.136e-11 |
| 2,560,001 | 1.714e-11 |

`λ₁` shrinks by a consistent factor of ~3–4 per doubling of `ngrid` — the
textbook signature of an `O(δ²)` quadrature error (`δ` = `G2` grid spacing)
*itself* converging to zero, not of a positive eigenvalue being resolved.
No plateau appears anywhere in this range (a sevenfold refinement of
`ngrid` beyond their default, a ~1000× reduction in `λ₁`).

**Jointly refining both** `N` and `ngrid` (`ngrid=200N+1`) shows the same
collapse: `6.0e-9 → 1.49e-9 → 3.67e-10 → 1.09e-10` at `N=400,800,1600,3200`
— again no plateau. Pushed further at `N=3200`: `ngrid=2,560,001` gives
`8.4e-12`; `ngrid=5,120,001` gives `3.7e-12` — still falling, now **5000
times smaller** than their reported "converged" value.

**Scale-dependence confirms the mechanism**: at `N=20`, `λ₁` is genuinely
stable across `ngrid` (`7.325e-6 → 7.295e-6`, 3 digits unchanged) — small
`h` isn't yet amplifying the fixed `G2` error. At `N=100` it begins
drifting (`4.27e-8 → 2.23e-8`). At `N=200` it's clearly unstable
(`2.22e-8 → 1.79e-9`). This is exactly the `1/h²` amplification mechanism
predicted above, confirmed by direct test rather than asserted.

**Cross-check against a brute-force, completely independent computation**:
at small `N=20`, I computed several `Q` matrix entries via adaptive
`scipy.integrate.dblquad` directly on the double integral
`∫∫g(x-y)φ_i'(x)φ_j'(y)dxdy`, bypassing `build_G2` entirely. (First attempt
had a `dblquad` argument-order bug of my own, caught and fixed — `dblquad`
calls `func(y,x)` with `x` as the *outer* variable, which I'd initially
reversed, producing nonsensical exact zeros for non-adjacent node pairs;
corrected before drawing any conclusion from it.) The corrected diagonal
entry matched the `build_G2`-based value to 7 digits at `N=20` — consistent
with `N=20` being a regime where `ngrid=40001` is already more than
adequate, which is exactly why no instability shows up there. This
localizes the problem correctly: individual matrix entries are fine; it's
the `1/h²`-amplified sensitivity at larger `N` that breaks.

### 2.3 What this means

This directly contradicts a result already sitting in the ledger from a
different angle: `selector_principle_exploration.md` (part of the `v13.915`
bundle, Test A) reports, for the *same* object — "Full form: λ₁ = 0.000000
in both sectors (**numerical floor, as expected** at a = 2)." That entry
treats `λ₁(Q_full)≈0` at `a=2` as the established, expected behavior
consistent with the entire Λ-rigidity arc's premise (the "knife-edge":
`λ₁(Q_full)` sits at the boundary of the positivity cone). `v13.926`'s
`1.83e-8` is not that — and my refinement tests show it heading toward
exactly that expected floor as resolution improves, not away from it.

**I have not proven `inf RQ_full = 0` exactly** — only that (a) the
specific claimed converged positive value is unreliable by a demonstrated,
mechanistic, reproducible margin of three-to-four orders of magnitude, and
(b) every available trend points toward zero, consistent with the
project's own prior expectation and the original (not yet actually
refuted) v13.910 "if." The two-bump Ritz plateau (§4) and frequency-
response (§3) results in `v13.926` are not re-checked here — they may use
a different computational path not implicated by this specific bug, but
given that the whole entry's interpretive framing leans on §2's "converged
positive floor" being real, I'd treat those sections as unconfirmed pending
resolution of this issue too, not as independently safe.

**Recommendation for the sandbox**: rerun the `N`-convergence study with
`ngrid` scaled well above `N` (e.g. `ngrid ≳ 100N`) at every `N`, or replace
`build_G2`'s fixed-grid cumulative-trapezoid approach with a quadrature
scheme whose error is controlled independently of `N` (e.g. adaptive
quadrature per Toeplitz entry, or an analytically exact piecewise
antiderivative between consecutive kinks of `g`, since `g`'s kink locations
`log n` are known exactly). Until then, `v13.910`'s "if" should be treated
as still open, not refuted.

## 3. `v13.927` (boundary-extension no-go) — confirmed

Pure extension theory, no numerics applicable or needed; hand-verified:

- `Q=Q^*` is maximal symmetric (standard: a self-adjoint operator admits no
  proper symmetric extension) — correctly blocks "just extend `Q`."
- The finite-deficiency no-go (§3): for `S⊂Q` with finite equal deficiency
  index `n`, Krein's resolvent formula gives rank-`≤n` resolvent
  differences between self-adjoint extensions of `S`; Weyl's theorem on
  essential-spectrum invariance under finite-rank resolvent perturbations
  then gives `σ_ess(H_Θ)=σ_ess(Q)=R` for *any* such extension — correctly
  ruling out discrete spectrum this way. Standard Krein–Weyl extension
  theory, correctly cited and applied.
- `K_Φ` bounded and everywhere-defined `⟹` no proper closed restriction
  with the same action (standard).
- The de Branges escape hatch (§9–11): `E(z)=Ξ(z)+iΞ'(z)` built via the
  standard HB-conjugate `E^#(z)=conj(E(z̄))`, confirmed by hand using
  `Ξ`'s reality on the real axis plus the Schwarz reflection consequence of
  entirety, giving `A=(E+E^#)/2=Ξ(z)` exactly and `B=Ξ'(z)` exactly (not
  merely proportional, though "`∝`" is also a true, weaker statement).
  Citing de Branges' own theorem that self-adjoint extensions of
  multiplication on `H(E)` have spectra equal to zeros of
  `A cosα+B sinα` is standard de Branges space theory.
- **The entry's own honest flag in §11 is exactly right and is the single
  most important sentence in it**: demanding `E=Ξ+iΞ'∈` Hermite–Biehler
  forces `A=Ξ`'s zeros to be real, i.e. **is RH itself** (or at least
  RH-hard) — not a free construction. This correctly identifies that the
  "escape hatch" relocates the difficulty rather than resolving it, and the
  entry says so plainly rather than burying it.

Agree with every boxed verdict in §14, and with §13's seven-item
non-circularity checklist as the right bar for anything claiming to close
this gate in the future.

## What remains open

Reopened by this round: **`v13.910`'s "continuum if" (`inf RQ_full=0`) is
back to open**, with the available evidence leaning toward *true* rather
than the "refuted" verdict `v13.926` claimed. Unchanged from prior rounds:
quantization of the zero resonances (now sharply localized per `v13.927` to
the missing finite-to-infinite canonical-system limit, `v13.833`'s Bucket
2); `G_-≥0` (reported RH-hard, Round 136); two-sided eigenfunction bounds
for the odd-sector Picard divergence (Round 135).

## Result

\[
\boxed{\textbf{v13.925 and v13.927 confirmed by hand (standard GNS/
spectral and extension/de Branges theory, correctly applied, honestly
scoped).} \textbf{v13.926's central numerical claim does not survive
independent testing: its "converged positive gap" } \lambda_1\approx
1.83\times10^{-8} \textbf{ is a discretization artifact from an
unrefined quadrature grid in a third-party FEM pipeline, demonstrated by
holding the FEM mesh fixed and refining that grid alone (a 1000}\times
\textbf{reduction with no plateau across seven doublings, extended to a
5000}\times\textbf{ reduction at the largest } N \textbf{ tested), by
jointly refining both parameters, and by confirming the instability is
absent at small } N \textbf{ and grows with it exactly as the } 1/h^2
\textbf{ amplification mechanism predicts.} \textbf{This directly
contradicts an existing, independent ledger result (}
\texttt{selector\_principle\_exploration.md}\textbf{'s } \lambda_1=0
\textbf{ "as expected") that v13.926 did not cross-check against.}
\textbf{v13.910's "if" should be treated as reopened, not refuted, pending
a reproduction with properly controlled quadrature.}}
\]
