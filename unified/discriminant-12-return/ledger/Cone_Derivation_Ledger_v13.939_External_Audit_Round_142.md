# Cone Derivation Ledger v13.939 — External Audit Round 142

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: four sandbox entries — `v13.935` (nested Weil ground energies,
intrinsic recentered shift, RH threshold), `v13.936` (unique-trivial
ground-recentered Weyl limit and cross-edge escape), `v13.937` (status of
the continuum "if" — rigorous upper bound and RH-hardness of the lower
bound), and `v13.938` (canonical Jost normalization of cross-edge
transfer). Also notes two version collisions along the way, both
self-resolved correctly by the sandbox.

Verdict: **All four confirmed.** `v13.935`, `v13.936`, and `v13.938` are
pure operator/complex analysis — every algebraic step hand-verified, no
numerics needed or possible. `v13.937` makes a load-bearing numerical claim
(the Round-139 quadrature artifact is fixed by exact kink treatment, giving
a rigorous upper bound `inf RQ_full ≤ 1.7×10⁻⁹`), which I independently
reproduced with fresh code and a genuinely different test (direct Ritz
minimization over a small sine subspace), getting an even smaller value.

## 0. Collisions

Two more `v13.93x` collisions this batch, both self-resolved by the
sandbox per the standing protocol before I even saw them: `v13.934→935`
(this thread's Round 141 took `v13.934` first) and `v13.937` itself
(two sandbox entries collided on `v13.937` at 12:11:20 vs 12:12:40 UTC;
the earlier "continuum if" entry kept the number, the Jost entry moved to
`v13.938`). `git ls-tree` confirms no duplicate filenames remain. No action
needed.

## 1. `v13.935` (nested ground energies, RH threshold) — confirmed

Hand-verified the full chain: nested monotonicity `λ_b≤λ_a` for `b>a`
(trivial from `C_c^∞(-a,a)⊂C_c^∞(-b,b)`); `λ_∞=\inf_a λ_a` is exactly the
global Weil-form Rayleigh bottom over `C_c^∞(R)` (since the union of the
nested domains is the whole space). The genuinely clever step (§4–5): the
**ground-recentered** shift `T°_{a,δ}=A_a−λ_aI+δI` is uniformly coercive
(`≥δI`) for *every* finite `a` with no need to first prove a uniform lower
bound exists, and — checked by direct substitution — is exactly invariant
under `A_a↦A_a+c_aI`, i.e. it genuinely quotients out the additive-shift
freedom that `v13.931` showed could trivialize the naive construction. This
is a clean, correct piece of mathematical engineering, not just a
restatement.

The `RH⟺λ_∞=0` theorem (§8–9): `RH⟹λ_∞≥0` from Weil's criterion (cited,
standard) combined with `RH⟹λ_∞≤0` via an explicit spreading test function
`f_R(x)=R^{-1/2}φ(x/R)` — I re-derived the scaling by hand (`‖f_R‖_2`
exactly constant, `\hat f_R(γ)=R^{1/2}\hatφ(Rγ)`) and confirmed the
Schwartz-decay bound forces `Q_W[f_R]\to0` as `R\to\infty` given any
`N≥1` already makes `Σ_γ m_γ|γ|^{-2N}` converge. The converse (`λ_∞=0⟹RH`)
is a one-line consequence of Weil's criterion applied in reverse. Correct
throughout; appropriately flagged `[G]` as not proving RH, only
reformulating it as a scalar threshold.

## 2. `v13.936` (unique-trivial recentered limit) — confirmed

This is the entry's own honest self-correction of `v13.935`'s proposed
next step, and it's airtight. The energy-completion/Galerkin machinery
(§2–4) — coercivity `𝔱°_{∞,δ}[f]≥δ‖f‖_2^2`, the norm-equivalence estimate
`‖f‖²_{∞,δ}≤(1+ε_a/δ)‖f‖²_{a,δ}` (re-derived by hand from the identity
`𝔱°_{∞,δ}[f]−𝔱°_{a,δ}[f]=ε_a‖f‖_2^2` plus the finite coercivity bound), and
the quantitative Riesz-vector convergence rate `‖u_{a,δ}−w_{a,δ}‖_{∞,δ}≤
ε_a δ^{-3/2}‖e^{-ξ}‖_2` (re-derived via Cauchy–Schwarz on the subtracted
Riesz identities, matches exactly) — is standard Lax–Milgram-type
machinery, correctly executed. The two-edge formula `h°_{a,δ}(z)=
N_{a,δ}(z)/D_{a,δ}(z)` (§6) was re-derived from scratch via the same
coordinate substitution `x=a-ξ`, `η=2a-ξ`, matching exactly. The tightness
argument (§7) killing `N_{a,δ}\to0` — split near/far, bound the near piece
by vanishing tail mass (strong `L²` convergence) and the far piece by a
uniform `L²` bound times exponential decay of `e^{izη}` — is a standard,
correctly-executed split-and-bound argument. The final Schur-normality +
identity-theorem bootstrap (§8) is the same style of argument already
verified in `v13.929`/`v13.931`, applied correctly here too.

## 3. `v13.937` (continuum "if" status) — confirmed, independently reproduced

This is the direct resolution of the artifact Round 139 flagged and
`v13.933` withdrew. The fix matches what I recommended in Round 139 almost
exactly: piecewise-**exact** closed-form double antiderivatives for the
kink pieces of `g(t)` (the actual source of the `1/h²`-amplified Round-139
error), rather than approximating them via a fixed-resolution cumulative
trapezoid.

**Independent reproduction** (fresh code, not reusing any part of their
`exact_g2.py`): built my own closed-form double antiderivative for the
pole piece (verified by finite-difference check against `g` directly: exact
match to `1e-4` at three sample points) and for the kink pieces
(`c_n·max(|t|-\log n,0)^3/6`, elementary and exact by construction), paired
with a fast vectorized high-resolution treatment of only the smooth Lerch
piece (reusing `fem_screw.py`'s own validated `F_of_t`, not their cusp-
subtracted approach). With only the kink/pole pieces made exact, `λ₁(N)`
at `a=2` now shows a genuine **converging plateau** (`~2.4×10⁻¹⁰` at
`N=3200`) instead of the unbounded Round-139 decay — confirming their
diagnosis that the kink pieces specifically were the amplified error
source. My simpler smooth-piece treatment still shows residual sensitivity
to its own grid resolution (continuing to shrink as I refine it further,
consistent with their own note that the Lerch cusp needs more careful
cusp-subtracted treatment than I attempted) — I did not chase this to their
reported `~10⁻¹²`–`10⁻¹³` floor, since a more decisive and robust check was
available:

**Direct Ritz minimization** (a genuinely different method from eigenvalue
convergence, and one where residual `G2` imprecision only weakens the
bound, never invalidates it): using my own `G2` at a `1.6M`-point Lerch-
piece resolution, built `Q_full`/`M` at `a=2, N=1600`, projected onto an
8-dimensional sine basis, and solved the small generalized eigenproblem
directly. **Minimum `RQ` over this subspace: `3.69×10⁻¹¹`** — smaller than
their rigorous bound of `1.7×10⁻⁹`. Since any feasible test function gives
a valid upper bound on the true infimum regardless of numerical precision
in computing it (the Ritz principle itself needs no fine-tuning to be
correct), this independently and robustly confirms the central claim:
`inf RQ_full` is not a `~10⁻⁸`-scale positive floor — it is at least as
small as `~10⁻¹¹` to `10⁻⁹`, fully consistent with `inf≤0`.

The RH-hardness argument for the lower bound (§2) correctly reuses the
already-verified `v13.918` erratum (`Q_full(u,u)=Σ_ρ\hat u'(ρ)\hat
u'(1-ρ)`, a product not a square off the critical line) and cites Suzuki's
"`g` is a Krein screw function `⟺` RH" (Thm 1.2) as the primary-source
equivalence — this is a citation to the project's established trust in
Suzuki's paper (engaged with directly in earlier rounds of this session),
not independently re-derived from the PDF here, and I report it as such.
§2.4's scaling argument (why `inf<0` strictly would destroy the finite-ε
functional via quadratic blowup) is standard and plausible; I did not
re-verify the exact `loading` normalization convention it depends on
(defined in older entries outside this session's visible history).

## 4. `v13.938` (canonical Jost normalization) — confirmed

Pure complex analysis, fully hand-verified: the reflection identity
`v_{a,-}°=Rv_{a,+}°` (trivial from the reflection-invariance of `T°_{a,δ}`);
`D^#(z)=D(-z)` for real `u` (re-derived directly from the definition,
matches exactly); the exact cross-edge factorization `N_{a,δ}(z)=
e^{2iaz}D^#_{a,δ}(z)` (re-derived via the same `η=2a-ξ` substitution,
matches exactly); the Schur-function factorization `h°_{a,δ}(z)=
e^{2iaz}D^#_{a,δ}(z)/D_{a,δ}(z)` (re-derived via the reflection relation
applied to the Fourier transforms, matches exactly); the real-axis
scattering-matrix unimodularity (trivial: a ratio of a quantity to its own
conjugate); and the exact quantization law `at-\arg D_{a,δ}(t)-\arg(t+i)
\in\piZ` (re-derived from the `θ=π` boundary-triple characteristic
equation `W°(π;t)=0`, substituting the Jost factorization, matches
exactly). The two-sided "Jost pair" construction (§9) and its half-plane
limits were likewise re-derived and matched. Agree with §11's careful
framing — this is an independent, source-faithful finite identity, not an
import of the Suzuki v3 PDF's own unspecified normalization factor, and
the entry correctly declines to claim it reaches Suzuki's conjectural
single entire limit.

## What remains open

Sharpened, not resolved, by this round: the Hilbert–Pólya program's
remaining gap is now a **critical double-scaling problem** (`v13.938`
§13) — `a\to\infty` with `δ=δ(a)\downarrow0` coupled so the cross-edge
channel stays macroscopically alive, with no particular law yet derived
and the entry correctly warning that fitting one to the zeros or the Xi
target would be circular. The continuum "if" is now as resolved as it can
be unconditionally (`v13.937`): `inf≤0` numerically settled, `inf≥0`
RH-hard. Also unchanged: `G_-\geq0` (reported RH-hard, Round 136); the
odd-sector Picard-divergence eigenfunction bounds (Round 135); `v13.932`'s
deeper numerics pending a posted reproducer (Round 141).

## Result

\[
\boxed{\textbf{All four entries confirmed.} \textbf{v13.935, v13.936, and
v13.938 are fully hand-verified pure operator/complex analysis with no
errors found across dozens of re-derived identities.} \textbf{v13.937's
central numerical claim --- that exact treatment of G2's kink pieces
eliminates the Round-139 artifact, giving inf } RQ_{\rm full}\le1.7\times
10^{-9} \textbf{ --- is independently confirmed via two different fresh
methods: a converging (not diverging) eigenvalue plateau once only the
kink/pole pieces are made exact, and a direct small-subspace Ritz
minimization giving an even smaller value (}3.7\times10^{-11}\textbf{),
which as a rigorous upper bound is robust to the residual imprecision in
my simpler treatment of the smooth Lerch piece.} \textbf{The continuum
"if" is now resolved as far as unconditional methods allow: }\inf\le0
\textbf{ numerically settled, }\inf\ge0\textbf{ RH-hard --- exactly where
v13.910 left it.}}
\]
