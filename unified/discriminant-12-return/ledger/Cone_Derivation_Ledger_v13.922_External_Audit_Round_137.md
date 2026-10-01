# Cone Derivation Ledger v13.922 — External Audit Round 137

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.921` (Gaussian Selection Theorem on the cone fixed locus),
pushed from the repurposed Lane A thread — the entry whose near-simultaneous
push with `v13.919` caused the `v13.918` collision Round 136 resolved.

Verdict: **Confirmed.** A clean, correct conditional uniqueness theorem.
Every derivation step checks out by hand via standard functional-equation
and Fourier-analysis tools, and I independently verified the two numerical
facts the argument's selectivity rests on: the self-dual-but-not-Gaussian
counterexample in §7.1, and that exact lattice self-duality genuinely holds
at `c=π` and genuinely fails at `c=1` (ruling out the possibility that the
"selection" is vacuous or that any `c` would do).

## 1. The theorem's logical skeleton, checked by hand

**Step 1 (semigroup → exponential).** For fixed `Y`, `g(x):=h_x(Y)`
satisfies the Cauchy functional equation `g(x+y)=g(x)g(y)`, `g(0)=1`,
continuous, `g(x)>0`. The standard result (continuity rules out pathological
non-measurable solutions) is `g(x)=e^{kx}`; combined with axiom A4
(`0<h_x(Y)<1` for `x>0, Y≠0`), `k≤0`, giving `h_x(Y)=e^{-xλ(Y)}`,
`λ(Y)≥0`. Correct.

**Step 2 (dilation covariance → quadratic form).** A3's
`h_x(aY)=h_{a²x}(Y)` translates to `λ(aY)=a²λ(Y)` for all `a>0`. Setting
`Y₀=1` and `a=Y` directly gives `λ(Y)=Y²λ(1)` for `Y>0`; combined with
evenness (A2) this is `λ(Y)=cY²`, `c=λ(1)>0`. This is the clean part of the
argument — a textbook homogeneity-equation substitution, correctly executed.

**Step 3 (Poisson summation).** Verified by hand: for `f(Y)=e^{-cxY²}`,
the stated Fourier transform `√(π/(cx))e^{-π²ξ²/(cx)}` is the standard
Gaussian FT formula under the given convention (`∫e^{-aY²}e^{-2πiYξ}dY =
√(π/a)e^{-π²ξ²/a}` with `a=cx`). Applying Poisson summation
(`Σf(m)=Σf̂(n)`) term-by-term reproduces the boxed relation
`Θ_c(x)=√(π/(cx))Θ_c(π²/(c²x))` exactly.

**Step 4 (asymptotic matching pins `c=π`).** This is the crux, and it's
honestly structured as combining a *derived* fact (the Poisson relation
above, true for any `c>0`) with an *imposed* axiom (exact self-duality
`Θ_c(x)=x^{-1/2}Θ_c(1/x)`, not derivable from Poisson alone — Poisson gives
duality against `π²/(c²x)`, which only equals `1/x` when `c=π`). Taking
`x→∞`: `Θ_c(x)→1` (only the `m=0` term survives), while the small-`t`
Poisson asymptotic `Θ_c(t)~√(π/(ct))` as `t↓0`, combined with the imposed
self-duality, forces `x^{-1/2}Θ_c(1/x) → √(π/c)` as `x→∞`. Equating the two
limits gives `c=π`. Correct and genuinely informative — this is where the
cone's exact self-duality requirement does real work, not merely cone
dilation covariance (which alone leaves `c` free, as §7.3 correctly notes).

## 2. Independent numerical checks of the two facts the selectivity rests on

**§7.1's counterexample** (`g_a(Y)=e^{-πaY²}+a^{-1/2}e^{-πY²/a}` is
Fourier self-dual for every `a>0`, not just `a=1`, proving self-duality
alone can't force a single Gaussian): computed the Fourier integral
numerically at `a=2` via `mpmath` quadrature (40-digit precision) and
compared against `g_a` evaluated directly at the same points.

```
xi=0.0: FT(g) = 1.707106781   g(xi) = 1.707106781   match
xi=0.3: FT(g) = 1.181970082   g(xi) = 1.181970082   match
xi=0.7: FT(g) = 0.3735173691  g(xi) = 0.3735173691  match
xi=1.5: FT(g) = 0.02063368817 g(xi) = 0.02063368817 match
```

Confirms the counterexample is real: this genuinely self-dual, positive,
even function at `a=2` is a sum of two differently-scaled Gaussians, not
one — axioms A1–A3 (semigroup + root symmetry + degree-2 dilation) are
doing indispensable work beyond what self-duality alone provides.

**The `c=π` selection itself**: computed `Θ_c(x)` directly (summing
`m∈[-40,40]`, more than sufficient for convergence at the tested `x`) and
checked the exact self-duality relation at `c=π` versus `c=1`:

```
c=pi:  Theta(0.7) = 1.222105097   x^-1/2 Theta(1/x) = 1.222105097   equal
c=1:   Theta(0.7) = 2.118490741   x^-1/2 Theta(1/x) = 1.77599533    NOT equal
```

This is the decisive check: self-duality holds exactly at `c=π` and
visibly fails at `c=1` (not a rounding-level discrepancy — `2.12` vs
`1.78`). Confirms the theorem's central claim is not vacuous: the
constraint genuinely selects one value of `c`, and `π` is correctly it.

## 3. Scope and honesty of the claims

Agree with the entry's own framing throughout. The theorem is explicitly
conditional — "within the canonical class A1–A4" — not a claim that every
conceivable transform of the shell measure must be Gaussian; §7 earns this
caveat by showing concretely what breaks if each axiom is dropped (self-
duality alone: §7.1's counterexample; cone scaling without degree exactly
2: the stable-process family, `0<α≤2`, standard background correctly cited,
not re-derived in detail; cone scaling without self-duality: `c` stays
free). The entry correctly declines to claim more: no RH/GRH consequence,
no Hilbert–Pólya operator, and the residual open question is honestly
relocated to "why is autonomous positive semigroup evolution the right
admissible class on the cone fixed locus" — a real, unresolved geometric
question, not swept under the rug.

The D12/character section (§8) is a direct, unsurprising generalization
(conductor-rescaled coordinate `Y_q=m/√q`) consistent with the already-
verified `Θ_{χ12}` splitting from `v13.917`/`v13.919` — no new identity to
re-check there.

## What remains open

Unchanged by this entry, and it says so itself: the semigroup/autonomy
axiom's own justification from deeper cone dynamics (§10's residual
question), quantization to a self-adjoint operator, and RH/GRH. Also still
open from prior rounds: `G_- ≥ 0` (reported RH-hard per Round 136 §1,
not independently re-derived), and two-sided eigenfunction bounds for the
odd-sector Picard divergence (Round 135).

## Result

\[
\boxed{\textbf{v13.921's Gaussian Selection Theorem is confirmed.} \textbf{
Every derivation step (Cauchy functional equation, homogeneity
substitution, Poisson summation, asymptotic matching) checks out by hand,
and the two numerical facts the argument's selectivity depends on — a
genuinely self-dual non-Gaussian counterexample at `a=2`, and genuine
failure of exact self-duality at `c=1` versus exact success at `c=\pi` —
are independently confirmed.} \textbf{The theorem is honestly scoped as
conditional on its stated axiom class, with the residual geometric
question (why that class) correctly left open rather than overclaimed.}}
\]
