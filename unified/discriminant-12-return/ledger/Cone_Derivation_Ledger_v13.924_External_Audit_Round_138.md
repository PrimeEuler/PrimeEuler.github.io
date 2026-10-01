# Cone Derivation Ledger v13.924 — External Audit Round 138

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.923` (Schoenberg Closure of the Cone Fixed-Locus Heat
Semigroup) — the entry that removes the semigroup/autonomy axiom Round 137
(`v13.922`) had flagged as the residual open question in `v13.921`'s
Gaussian Selection Theorem.

Verdict: **Confirmed.** This is a correct, textbook-standard application
of Schoenberg's theorem (the Lévy–Khintchine / Schoenberg correspondence
between conditionally negative definite functions and positive convolution
semigroups — see Berg–Christensen–Ressel, *Harmonic Analysis on
Semigroups*) to the cone's quadratic invariant. I hand-verified the one
nontrivial computation the whole argument rests on, and independently
confirmed it plus the theorem's conclusion and the generator identity
numerically.

## 1. The load-bearing computation — conditional negative definiteness of `q(Y)=Y²`

By hand: for `Σc_j=0`,

```
S = Σ_{j,k} c̄_j c_k (Y_j-Y_k)²
  = Σ_{j,k} c̄_j c_k Y_j² + Σ_{j,k} c̄_j c_k Y_k² - 2Σ_{j,k} c̄_j c_k Y_j Y_k
```

The first sum factors as `(Σ_j c̄_j Y_j²)(Σ_k c_k) = 0` since `Σc_k=0`; the
second factors as `(Σ_k c_k Y_k²)(Σ_j c̄_j) = 0` for the same reason. What
remains is `-2(Σc̄_jY_j)(Σc_kY_k) = -2|Σc_jY_j|²` (using `Y_j` real, so
`Σc̄_jY_j` is the conjugate of `Σc_jY_j`), which is `≤0` for any complex
coefficients. This exactly matches the entry's boxed result and is the only
genuinely nontrivial step in the whole derivation — everything after it
(Schoenberg, Bochner/Herglotz, the semigroup property, the generator) is
citation of standard theorems or direct computation once this is granted.

Independently verified numerically (`schoenberg_check.py`, fresh code): 5
random trials with random complex coefficients `c_j` constrained to
`Σc_j=0` and random real points `Y_j`, comparing the direct double sum
against `-2|Σc_jY_j|²` — matched to floating-point precision in every
trial, and `S≤0` held in every case.

## 2. Schoenberg's theorem itself — correctly cited and correctly applied

Schoenberg's theorem (`q` conditionally negative definite, `q(0)=0` `⟹`
`e^{-tq}` positive definite for all `t≥0`) is a genuine, standard theorem,
not something invented for this entry — I recognize it from the
Lévy-process / negative-definite-functions literature (it's the harmonic-
analysis engine behind why Brownian motion's generator comes from a
quadratic form). The entry applies it correctly: `q(0)=0` trivially, `q`
even, so `φ_t(Y)=e^{-tY²}` is positive definite for every `t≥0`.

**Independent numerical check**: for several random finite point sets
`{Y_j}` and several `t` values, I built the matrix `[e^{-t(Y_j-Y_k)²}]_{j,k}`
directly and checked its eigenvalues — all nonnegative (minimum eigenvalue
`~1e-11` to `~1e-2`, i.e. zero up to floating-point noise or genuinely
positive, never negative) at `t=0.3, 1.0, 3.0`. This is a direct,
model-free confirmation of positive-definiteness, not a restatement of the
theorem.

## 3. Bochner/Herglotz, the semigroup property, and the generator

- **Herglotz** (the circle-group analogue of Bochner's theorem: a
  normalized positive-definite sequence on `Z` is the Fourier transform of
  a unique probability measure on the dual circle `T`): standard, correctly
  invoked to get `κ_t` from `φ_t(m)=e^{-tm²}`.
- **Semigroup property** `κ_{t+s}=κ_t*κ_s`: follows from
  `e^{-(t+s)m²}=e^{-tm²}e^{-sm²}` pointwise plus injectivity of the Fourier
  transform on measures (convolution ↔ pointwise product is standard; the
  uniqueness step is exactly what Herglotz guarantees). Correct.
- **Generator**: `A e_m = -m² e_m` by differentiating `e^{-tm²}` at `t=0`.
  Checked symbolically (via `sympy`) that
  `d²/dθ² e^{2πimθ} = -4π²m² e^{2πimθ}`, so `A = (1/4π²)d²/dθ²` exactly —
  confirmed to match the entry's boxed formula.

## 4. What this does and doesn't close

Agree with the entry's own framing. This genuinely removes the axiom Round
137 flagged as residual: the autonomous positive semigroup is no longer an
assumption about admissible dynamics — it's forced by `q(Y)=Y²` being
conditionally negative definite, which is itself just a fact about the
cone's quadratic invariant (verified in §1). The logical chain `cone fixed
locus → q=Y² → conditionally negative definite → e^{-tq} positive definite
(Schoenberg) → probability convolution semigroup (Herglotz) → dual-circle
Laplacian generator → θ-trace` is sound at every link.

The entry is appropriately honest about what's left: the "residual
representation guardrail" (why the Pontryagin-dual circle is the right
carrier, not a claim that the full cone point set is a Lie group — a
genuine and correctly-flagged subtlety, since the construction only ever
uses the signed coordinate `Y∈R` and its lattice, never literal addition of
ambient cone points across root sheets) and the still-open items (no
self-adjoint point-spectrum operator constructed from the zero resonances;
no RH/GRH consequence) are carried forward honestly, not dissolved by this
result.

## What remains open

Unchanged: quantization of the zero resonances to a self-adjoint operator;
the representation-theoretic status of the Pontryagin-dual carrier (this
entry's own residual item); `G_- ≥ 0` (reported RH-hard, Round 136);
two-sided eigenfunction bounds for the odd-sector Picard divergence (Round
135). None of these are touched by `v13.923`.

## Result

\[
\boxed{\textbf{v13.923 is confirmed.} \textbf{The one nontrivial
computation — that } q(Y)=Y^2 \textbf{ is conditionally negative definite —
checks out exactly by hand and numerically (5/5 random trials). Schoenberg's
theorem, correctly cited, then forces positive-definiteness of } e^{-tY^2}
\textbf{(independently confirmed via direct eigenvalue checks on random
point sets), and the resulting semigroup/generator chain (Herglotz,
convolution semigroup, dual-circle Laplacian } A=(1/4\pi^2)d^2/d\theta^2
\textbf{) is standard and correctly executed.} \textbf{This genuinely
removes the semigroup/autonomy axiom Round 137 had flagged as residual in
} v13.921\textbf{'s Gaussian Selection Theorem — not by assumption, but as
a consequence of the cone's quadratic invariant and classical harmonic
duality.}}
\]
