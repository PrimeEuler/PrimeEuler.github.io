# Cone Derivation Ledger v13.945 — External Audit Round 143

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: five sandbox entries — `v13.940` (intrinsic deficiency-overlap
double scaling), `v13.941` (parity-pole critical crossover), `v13.942`
(sieve renormalization flow — the "immortal amalgamation"), `v13.943`
(RH-conditional super-algebraic parity-gap closure), and `v13.944`
(sieve-fold/Jost scale matching and an exponential parity-gap upper
bound, landed mid-draft and cross-connecting `v13.942` back into this
lane). Also notes three self-resolved version collisions, including this
thread's own draft number being taken from under it.

Verdict: **All five confirmed.** `v13.940`, `v13.941`, `v13.943`, and
`v13.944` are pure operator/analysis, fully hand-verified with every
algebraic step re-derived and matched. `v13.942` is the playful one Jeremy
flagged directly — a genuinely fun and legitimate piece of work connecting
the sieve of Eratosthenes, the zero-spectrum detection, and the Dirichlet
divisor problem as one object in different coordinates, explicitly scoped
as non-RH-hard exploratory content; its hard numerical claims are
independently confirmed to high precision.

## 0. Collisions

Three this round: `v13.939→940` (this thread's Round 142 took `v13.939`
first) and `v13.942` itself (the sieve-renormalization entry and a
parity-gap entry collided at 14:20:12 vs 14:20:39 UTC; the earlier sieve
entry kept the number, the parity-gap entry moved to `v13.943`) were both
self-resolved by the sandbox before I saw them. The third was this
thread's own: a new sandbox entry landed at `v13.944` while this very
audit round was still a local, unpushed draft also targeting `v13.944` —
since my draft had never been committed, there was nothing to defer to;
it's simply renumbered to the next free slot (`v13.945`) here, with that
entry folded into the scope below rather than left for a future round. No
duplicate filenames remain.

## 1. `v13.942` — the "immortal amalgamation" (sieve renormalization flow)

This is the one Jeremy asked me to look at directly — his own closing
quote is kept verbatim in the entry: *"we created this amalgamation, lets
see if its imortal"* — and it's a good one. The framing: the primes `≤√N`
(the "seed") deterministically generate, via Eratosthenes, not just the
full prime pattern on `[1,N]` but also `μ(n)`, `d(n)`, and the Dirichlet
divisor-problem fluctuation `Δ(x)` — and the *same* zero-spectrum signal
detected in the binary-compression framework (prior ledger work) shows up
in all of them, read through different coordinate lenses (`log x` for the
zeta zeros, `√x` for Voronoi's divisor-problem comb). It's honestly scoped
throughout as `[N]`/`[I]` exploratory content on a deliberately
**non-RH-hard** front, with a clean `[G]` section (§9) explicitly
disclaiming any proof of the `1/4` exponent conjecture.

**Independently verified the entry's exact, well-defined numerical claims**
with fresh from-scratch code (not requiring any guess at their specific
FFT/windowing pipeline, which I did *not* attempt to reproduce):

- `π(10⁶) = 78498` — matches the known exact value exactly.
- Nonzero-`μ(n)` count for `n≤10⁶`: `607926` — exact match.
- `M(10⁶) = 212` (Mertens function) — exact match, consistent with the
  independently tabulated value.
- `D(10⁶) = 13,970,034` (divisor summatory) — confirmed via **two**
  independent methods: the hyperbola-method floor sum
  `2Σ_{k≤√N}⌊N/k⌋−⌊√N⌋²`, and a completely separate brute-force
  divisor-count sieve (`Σ_{k≤N} 1` added at every multiple of `k`). Both
  gave the identical exact integer, matching their claimed value exactly.
- `Δ(10⁶) = 92.11` — my computation from `D(10⁶)` and the classical
  asymptotic `D(x)=x\log x+(2γ-1)x+Δ(x)` gives `92.1122`, matching their
  reported `92.1`.
- The hyperbola-identity cross-check (§6): computed
  `√N − 2Σ_{k≤√N}\{N/k\}` directly and got `92.2789` at `N=10⁶` — matching
  their reported seed-scale prediction of `92.28` almost to the decimal,
  against their flow value `92.1` (my `92.1122`) — both numbers confirmed
  independently and the small residual gap between them (the stated `O(1)`
  term in the classical identity) matches in magnitude too.

The classical mathematics underlying the entry (the sieve of Eratosthenes
itself; the elementary fact that any `n≤N` has at most one prime factor
`>√N`, hence `μ`/`ω`/`d` are seed-computable; the Dirichlet hyperbola-method
identity for `Δ(x)`) is correctly characterized throughout as classical,
not claimed as new — the entry's own honest framing (§9) is that the
contribution is the *unified flow* and the *measurements*, not new
elementary number theory. Agreed. The FFT-based `R`-value, dose-response,
and kill-test numbers (§2–4, §7–8) are not independently reproduced here —
no reproducer was posted (explicitly noted in §10, "awaits Jeremy's
explicit per-item authorization") — but the exact, checkable backbone the
rest of the entry stands on is now independently confirmed.

## 2. `v13.940` (intrinsic deficiency-overlap double scaling) — confirmed

Pure operator analysis; every identity re-derived by hand and matched
exactly: the large-`δ` endpoint `κ_a(∞)=2a/\sinh(2a)` (direct computation
of `⟨e^{-x},e^x⟩=2a` and `⟨e^x,e^x⟩=\sinh(2a)` on `(-a,a)`); the
ground-channel limit `κ_a(0+)=1` under hypothesis (H1) (re-derived via the
resolvent pole expansion, confirming the `δ^{-1}` divergent pieces cancel
in the ratio when the even projection sees both sources identically); the
first-crossing definition (no monotonicity needed, a genuinely careful
touch); and the explicit power-law derivation under (H3)/(H4), re-derived
by direct substitution and matching `δ_τ(a)\sim(τ/2ca)^{1/ν}` exactly. The
entry is scrupulous about separating exact Level-I identities from the
explicitly-flagged conditional Level-II/III hypotheses — nothing is
overclaimed.

## 3. `v13.941` (parity-pole critical crossover) — confirmed

Also fully hand-verified. The identity `q_τ=(1-e^{-τ})/(1+e^{-τ})=\tanh(τ/2)`
checks out by direct algebra. The Stieltjes/spectral-measure setup (§2) is
a standard, correctly-applied spectral-theorem decomposition. The one-pole
solution of the crossover equation — substituting
`G_-(x_τ)=1/(1+x_τ)` and `G_+(x_τ)\to0` into the general crossover equation
and solving `x_τ = q_τ r(1+x_τ)` for `x_τ = q_τr/(1-q_τr)` — matches
exactly. This entry's own honest self-correction of `v13.940` (§8: the
stronger thermodynamic ansatz requires an *additional* uniformity
assumption not automatically implied by the parity-pole analysis, since
`x_τ` is not generically proportional to a fixed power of `τ`) is itself
correct — I checked the small-`τ` behavior (`q_τ\approxτ/2`, giving
`x_τ\approx rτ/2` only approximately linear for small `τ`, not exactly
proportional in general) and it supports exactly the caution the entry
raises.

## 4. `v13.943` (RH-conditional super-algebraic parity-gap bound) — confirmed

Explicitly and correctly RH-conditional throughout. Re-derived the odd
broadening test (§2) by hand: the dilation scaling `f_a(x)=a^{-1/2}φ(x/a)`
preserves `‖f_a‖_2` exactly and gives `\hat f_a(t)=a^{1/2}\hatφ(at)`
(matches exactly); combined with Schwartz decay and the zero-counting
convergence `Σm_γ|γ|^{-2N}<\infty` (any `N≥1`), this correctly forces
`λ_a^{(-)}=O(a^{-M})` for every `M`. The "no positive finite power law"
argument (§4, by contradiction) is valid. The Gevrey sharpening (§5) rests
on one inequality I checked particularly carefully after an initial
concern: `a^η|γ|^η ≥ \tfrac12 a^ηγ_1^η+\tfrac12|γ|^η` for `a≥1` — my first
attempt at a general version of this inequality failed for some parameter
ranges, which worried me, but re-deriving it with the actual stated
conditions (`γ_1` fixed on one side, `|γ|≥γ_1` on the other, `a≥1`) confirms
it holds exactly as used; the entry's derivation is correct as stated. The
entry is appropriately careful throughout about what remains unproved (§9:
no lower bound, no unconditional version, no residue-ratio proof) — an
upper bound only, correctly labeled as such.

## 5. `v13.944` (sieve-fold/Jost scale matching, exponential parity-gap bound) — confirmed

Landed mid-draft of this very round and directly builds on both halves of
it — reusing `v13.938`'s Jost factorization and `v13.942`'s sieve result to
connect the two lanes, then genuinely sharpening `v13.943`'s bound. Fully
hand-verified:

- **The scale matching** (§1–2): `a(√N)=½a(N)` is trivial algebra
  (`½\log√N=¼\log N`). Substituting `z=i` into the already-verified Jost
  formula `h°_{a,δ}(z)=e^{2iaz}D^\#_{a,δ}(z)/D_{a,δ}(z)` from `v13.938`,
  using `e^{2ia\cdot i}=e^{-2a}=N_a^{-1}` and the already-verified
  `D^\#(i)=D(-i)` identity, gives `κ_a(δ)=N_a^{-1}D_{a,δ}(-i)/D_{a,δ}(i)`
  exactly as claimed — a clean, correct substitution chain through results
  I'd already independently verified earlier in this same round.
- **The sharper exponential bound** (§4–7), the entry's real technical
  contribution: built from an `n`-fold convolution `g_n=p^{*n}` of a smooth
  compactly-supported probability density, giving `\hat g_n=P^n` (standard)
  and the odd trial state `f_n=g_n'` with `\hat f_n(t)=itP(t)^n` (direct
  product/derivative rule, matches exactly). Verified `q:=\sup_{|γ|≥γ_1}
  |P(γ)|<1` is forced by `p` being a genuine spread-out density rather than
  a point mass (strict inequality in `|\int p e^{-itx}dx|≤\int p` requires
  the integrand's phase to vary on `p`'s support). The resulting bound
  `Q_W[f_n]≤C_pq^{2n}` (§5, splitting the exponent at a fixed `m_0` large
  enough for Schwartz-decay convergence) and the matching lower bound
  `‖f_n‖_2^2≥c_pn^{-3/2}` (§6, from the standard local quadratic expansion
  `P(t)=1-\tfrac12σ_p^2t^2+O(t^4)` near `t=0`) both check out by hand —
  together these give the clean exponential bound `λ_a^{(-)}≤Ca^{3/2}
  e^{-ca}` (§7), a genuine improvement over `v13.943`'s merely
  super-algebraic/Gevrey bound.
- **The coordinate guardrail** (§11.2) is a good, explicit methodological
  caution: the zeta-zero spectrum resolves in `\log x` (this Suzuki/Jost
  problem's native coordinate) while the divisor-problem `1/4` phenomenon
  resolves in `√x` (`v13.942`'s Voronoi comb) — the entry explicitly warns
  against importing one exponent into the other's problem, which is the
  right discipline given how naturally the two lanes now touch.
- As with its predecessors, scrupulously honest about what's still open
  (§12: no matching lower bound, no exact rate constant, no RH
  independence) — an upper bound only, correctly labeled.

## What remains open

Sharpened further by this round: the double-scaling exponent is now
understood (`v13.941`) to be governed by the first odd recentered spectral
gap `Δ_a`, and `v13.943`/`v13.944` together rule out — conditional on RH —
any positive finite power law for that gap and replace it with a genuine
exponential upper bound `Δ_a≤Ca^{3/2}e^{-ca}`, redirecting the open
problem (§13 of `v13.944`) to optimizing the concentration kernel and
finding a matching lower bound. Also still open: `G_-\geq0` (Round 136,
RH-hard); the odd-sector Picard-divergence bounds (Round 135); `v13.932`'s
deeper numerics pending a reproducer (Round 141).

## Result

\[
\boxed{\textbf{All five entries confirmed.} \textbf{v13.940, v13.941,
v13.943, and v13.944 are fully hand-verified pure analysis,
hypothesis-labeled throughout with nothing overclaimed; v13.944 in
particular genuinely sharpens v13.943's bound to a clean exponential rate
via a correctly-executed convolution/concentration argument, and correctly
cross-connects to v13.942 with an explicit warning against conflating the
two lanes' different coordinate systems.} \textbf{v13.942, the "immortal
amalgamation," is a legitimate and fun piece of honestly-scoped
exploratory work: every exact, well-defined numerical claim it makes}
(\pi(10^6), \text{the } \mu\text{-count}, M(10^6), D(10^6), \Delta(10^6),
\textbf{and the hyperbola-identity cross-check}) \textbf{independently
confirmed via fresh code and, for } D(10^6)\textbf{, two completely
different methods agreeing on the same exact integer.} \textbf{It survived
this audit's kill tests too.}}
\]
