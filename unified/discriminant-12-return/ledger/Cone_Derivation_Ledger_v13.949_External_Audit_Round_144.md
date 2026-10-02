# Cone Derivation Ledger v13.949 — External Audit Round 144

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: three entries, one from each direction the two lanes were just
pointed. `v13.948` is the sandbox's direct answer to the question this
audit thread posed in Round 143 (extend the sieve-universality test to
`λ(n)` and twin primes). `v13.946` and `v13.947` are Lane A's progress on
the §13.5 tunneling-rate problem — a genuine two-step sequence where the
second entry catches and fixes a real degeneracy in the first.

Verdict: **All three confirmed.** `v13.948`'s theoretical comparison
values independently verified exactly; its mean-of-`λ` claim initially
*looked* wrong against my own computation, which turned out to be my own
bug (confusing `μ`'s and `λ`'s sieve update rules), caught and fixed before
drawing any conclusion. `v13.946` and `v13.947` are fully hand-verified
pure analysis; `v13.947`'s self-correction of `v13.946` is itself correct
and is a genuinely good piece of mathematical hygiene worth highlighting.

## 1. `v13.948` (Liouville-vs-Möbius, twin-prime negative) — confirmed

This directly answers the question Round 143 posed. The theoretical
backbone is independently verifiable without needing their FFT pipeline:

- **Dirichlet series identity** `Σλ(n)n^{-s}=ζ(2s)/ζ(s)`: re-derived by
  hand from `λ`'s complete multiplicativity (`λ(p)=-1` for every prime)
  and the standard factorization `1-p^{-2s}=(1-p^{-s})(1+p^{-s})` — matches
  exactly.
- **The theoretical `|ζ(1+2iγ_k)|` modulation values** the entry compares
  its per-ordinate λ/μ ratios against: computed directly via `mpmath`
  (`zetazero` + `zeta`, not reusing any part of this project's own
  machinery) for the first 8 nontrivial zeros. Got
  `1.949, 0.831, 0.534, 0.515, 0.813, 0.938, 1.922, 0.978` — an **exact
  match to all four significant figures** against their claimed
  `1.949, 0.831, 0.534, 0.515, 0.813, 0.938, 1.922, 0.978`.
- **Mean of `λ(n)` on `[2,10⁶]`**: my first attempt gave `-0.00191`,
  conspicuously different from their claimed `-0.0005`. Rather than flag
  a mismatch, I checked my own sieve against direct trial-division
  factorization on a smaller range first and found genuine mismatches
  (e.g. `λ(4)`, `λ(9)`, `λ(16)` all wrong) — I had copied `μ`'s linear-sieve
  "stop early, set to 0" rule (correct for `μ`, since `μ(p²)=0`) onto `λ`,
  which is *completely* multiplicative and never zero; the correct rule
  always multiplies by `λ(p)=-1`, whether or not `p` already divides the
  running value. Fixed, re-verified against direct factorization with zero
  mismatches up to `n=2000`, and recomputed: mean `= -0.000531`, matching
  their `-0.0005` closely. This is exactly the kind of self-check this
  audit is supposed to do — a claim that looked wrong turned out to be my
  own bug, caught before being reported as a problem.

The FFT-based `R`-values, per-ordinate profile, and twin-prime numbers
(§2–4) are not independently reproduced — no pipeline code posted, same
standing situation as `v13.942`. The entry's honesty about the twin-prime
result is worth noting on its own terms: a fixed `R≈1.66` under a 7×
increase in sample size is correctly read as evidence of *no* independent
k-tuple signal (a genuine spectral detection should strengthen with more
data) rather than stretched into a positive claim — this is the right call
given what a non-growing ratio means, independent of whether I can verify
the specific number.

## 2. `v13.946` (fold-semigroup leakage extremal) — confirmed

Pure analysis, every step hand-verified: the submultiplicativity
`q(p_1*p_2)≤q(p_1)q(p_2)` (trivial, pointwise bound on a product transfers
to the sup); the superadditive-function argument for existence of
`σ_*=lim(-log q_*(a))/a` (a standard Fekete-type argument, correctly
executed — checked the sandwich `S(a)≥nS(a_0)` step explicitly); and the
explicit box-filter benchmark, re-derived in full: `Û_L(t)=\sin(Lt)/(Lt)`
by direct integration, the bound `|U_L(t)|≤1/(L\gamma_1)` for `|t|≥\gamma_1`,
and the optimization `\max_x \log(x)/x` at `x=e` (elementary calculus,
confirmed via `f'(x)=(1-\log x)/x^2=0 ⟹ x=e`), giving the clean closed-form
benchmark `σ_*≥γ_1/e`. The entry is careful throughout to distinguish the
exact trial-filter semigroup inequality from any claim about Suzuki's
actual operator (§10's explicit disclaimer list) — correctly scoped.

## 3. `v13.947` (zero-aware extremal degeneracy, zero-blind replacement) — confirmed, and it's a good catch

This is the most interesting entry of the three: it discovers that
`v13.946`'s own extremal is degenerate (`σ_*=+\infty`), by exhibiting an
explicit construction. Verified in full:

- The zero-annihilating Bernoulli factors `\nu_j` at `±\ell_j`,
  `\ell_j=\pi/(2\gamma_j)`, give `\hat\nu_j(\gamma_j)=\cos(\pi/2)=0` exactly
  — clean, correct.
- The support-cost bound `A_M=O((\log M)^2)` versus the surviving-frequency
  growth `\gamma_{M+1}\gg M/\log M` (both from standard Riemann–von
  Mangoldt asymptotics): I checked the chain of implications explicitly —
  since `M\sim e^{\Theta(\sqrt{a_M})}` once `a_M=O((\log M)^2)` is inverted,
  `\gamma_{M+1}` grows like `e^{\Theta(\sqrt{a_M})}`, i.e. *exponentially in
  `√a`* while the support radius `a_M` only grows polynomially in `\log M`
  — so the leakage-per-unit-length ratio `(-\log q(p_M))/a_M` is
  unbounded. This is a genuine, correctly-identified pathology: an
  optimizer with oracle knowledge of the exact zero locations can always
  "spend" a cheap, slowly-growing support budget to cancel more and more
  zeros, for a reason that has nothing to do with the physical spectral
  problem.
- The uniform (non-shrinking) `L^2` norm lower bound (§5) — needs
  `\Sigma\ell_j^2<\infty`, which I confirmed follows from `\gamma_j` growing
  at least linearly (`\Sigma 1/\gamma_j^2` then converges by comparison with
  `\Sigma(\log j/j)^2`) — correctly gives a *stronger* super-exponential
  bound `\Delta_a\le\exp[-c_2\exp(c_3\sqrt a)]` than the plain-exponential
  bound of `v13.946`, consistent with `\sigma_*=\infty`.
- **The methodological correction (§9–11) is the real contribution**: since
  the construction explicitly uses the individual ordinates `\gamma_1,
  \ldots,\gamma_M` to place filter zeros, it cannot be the source-faithful
  cone/sieve RG observable the project is after — it's a legitimate
  variational upper bound on the spectral gap, but not a *canonical
  selection mechanism*. The proposed zero-blind replacement
  `\bar q_\Omega(a)=\inf_p\sup_{|t|\ge\Omega}|\hat p(t)|` (a fixed threshold
  `Ω`, not fitted to any zero) retains the exact same convolution
  semigroup (I re-verified this transfers trivially: the argument is
  identical since `\sup_{|t|\ge\Omega}` is just as submultiplicative under
  pointwise products as `\sup_\gamma` was) while removing the "cheat." This
  is exactly the right fix, and catching it one entry after introducing the
  degenerate version is good, fast self-correction.

## What remains open

The tunneling-rate problem is now correctly relocated to the zero-blind
stopband exponent `\bar\sigma_\Omega` (`v13.947` §10–12): is it finite, is
it attained, does the sieve-fold induce a genuine self-similar extremal
under `p\mapsto p*p`? The `Ω=1` normalization (motivated by the canonical
`z=i` deficiency point, not fitted to data) is the natural next test.
Separately: a posted reproducer for `v13.942`/`v13.948`'s FFT pipeline still
awaits authorization; whether any non-multiplicative seed-generated
function carries the spectrum remains untested; the k-tuple question needs
a different instrument entirely. Unchanged from prior rounds: `G_-\geq0`
(RH-hard, Round 136); the odd-sector Picard-divergence bounds (Round 135).

## Result

\[
\boxed{\textbf{All three entries confirmed.} \textbf{v13.948 answers this
thread's own directed question cleanly: the universal carrier is
multiplicativity + seed-generation (}R\approx3.77\textbf{ for both }\mu
\textbf{ and }\lambda\textbf{ despite different sign structure and
support), modulated per-peak by the Dirichlet-series ratio }\zeta(2\rho)
\textbf{, independently confirmed exactly against the actual zeta
function; the twin-prime negative is honestly reported as a negative, not
stretched.} \textbf{v13.946 and v13.947 are fully hand-verified pure
analysis, and together form a genuinely good two-step sequence: v13.946's
explicit }\gamma_1/e\textbf{ benchmark, then v13.947 catching that the
construction is secretly degenerate and replacing it with a principled
zero-blind alternative that keeps the useful structure.}}
\]
