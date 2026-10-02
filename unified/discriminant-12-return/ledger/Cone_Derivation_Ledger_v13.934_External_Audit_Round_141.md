# Cone Derivation Ledger v13.934 — External Audit Round 141

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: three sandbox entries — `v13.931` (unconditional shifted Weyl
compactness, canonical-system limits, and large-negative-shift
trivialization), `v13.932` (m=7 asymmetric V / thin-seed dilution), and
`v13.933` (erratum withdrawing `v13.926`'s claim). Also notes the
version-collision on `v13.930` between this audit thread and the sandbox,
resolved correctly by the sandbox itself per the standing protocol.

Verdict: **`v13.931` confirmed in full — every step hand-verified, with one
claim independently reproduced numerically. `v13.933` confirmed: it matches
Round 139's finding almost to the decimal. `v13.932` confirmed at the
structural level (its arithmetic is exactly right) but its deeper numerical
claims are not independently reproduced at the same depth as the rest of
this round** — the machinery it depends on predates this audit thread's
visible history and no reproducer code was posted; I flag this honestly
rather than either rubber-stamping or disputing it.

## 0. The `v13.930` collision

Confirmed clean: the sandbox's `073588d1`/`079f086` commits both initially
used `v13.930`, collided with this thread's own Round 140 (`v13.930`,
pushed first), and were **correctly self-resolved** by the sandbox —
renumbered to `v13.931`/`v13.932` respectively, with an explicit note
citing "earlier-commit-wins," no content altered. `git ls-tree` confirms no
duplicate filenames remain at any version number. No action needed from
this side.

## 1. `v13.931` (shifted Weyl compactness) — confirmed

Pure complex/operator analysis, hand-checked top to bottom:

- **Montel compactness** (§2): `|h_n|≤1` on `C₊` gives a normal family,
  hence a locally-uniformly-convergent subsequence `h_n→h_*:C₊→D̄` —
  standard, correctly stated with the closed disk (not claiming `h_*`
  avoids the boundary).
- **Strict interior contraction** (§3): since `|φ_i(z)|<1` *strictly* for
  `z∈C₊` (not just `≤1`), `s_*=φ_i h_*` satisfies `|s_*(z)|<1` strictly
  everywhere in `C₊` even where `h_*` might touch the unit circle — a
  genuinely useful technical point, since it guarantees `m_*` (the inverse
  Cayley transform of `s_*`) is honestly holomorphic on all of `C₊`, not
  merely meromorphic with possible poles. Correct and well-observed.
- **`m_*(i)=i` is automatic** (not something to separately verify): since
  `φ_i(i)=0` exactly, `s_n(i)=φ_i(i)h_n(i)=0` for *every* `n` regardless of
  `h_n`'s value, so `s_*(i)=0` and `m_*(i)=i` follows immediately. Confirmed
  by hand.
- **Upgrade to `m_n→m_*`** (end of §3): on compact `K`, `|s_n|≤|φ_i|≤q_K<1`
  uniformly, keeping the Cayley-inversion denominator `|1−s_n|` bounded away
  from `0`; local-uniform convergence of `s_n` then transfers to `m_n`
  through this uniformly-Lipschitz region. Standard, correct.
- **Herglotz representation at `z=i`** (§4): verified by hand that
  `1/(t−i) − t/(1+t²) = i/(1+t²)` exactly (direct algebra:
  `1/(t−i)=(t+i)/(t²+1)`, subtract `t/(t²+1)`, left with `i/(t²+1)`),
  reproducing `α=0` and `β+∫dμ_*/(1+t²)=1` exactly as claimed.
- **Classical de Branges inverse theorem** (§5): correctly cited as
  standard (every Herglotz function is the Weyl coefficient of a unique
  trace-normalized canonical system) — not claimed as new.
- **The trivialization argument** (§6–8), the most substantial new
  computation, verified in full:
  - `L(A_a+LI)^{-1}→I` strongly as `L→∞`: standard spectral-theorem fact for
    a self-adjoint, bounded-below operator (`L/(s+L)→1` pointwise, dominated
    convergence under the functional calculus).
  - `J_a(z)=2\sinh(a(1+iz))/(1+iz)`: re-derived the elementary integral
    `∫_{-a}^a e^{(1+iz)x}dx` by hand and it matches exactly.
  - `J_a(-z)≠0` for `z∈C₊`: confirmed `\mathrm{Re}(a(1-iz))=a(1+y)>0` for
    `y=\mathrm{Im}(z)>0`, so the argument of `\sinh` is never purely
    imaginary there, and `\sinh` vanishes only on the imaginary axis —
    correct.
  - The exponential decay rate (§7): I independently re-derived the
    growth-gap identity `(1+y)−|1−y|=2\min(1,y)` by direct case split
    (`y≤1` and `y>1` separately) and it matches exactly; this gives the
    precise asymptotic rate at which `H_a(z)→0`.
  - **Independent numerical check** (fresh code, direct evaluation of the
    closed form `H_a(z)=\frac{1-iz}{1+iz}\frac{\sinh(a(1+iz))}{\sinh(a(1-iz))}`):
    confirmed `|H_a(z)|\to0` as `a` grows at three sample points, and the
    measured decay ratios over `Δa=8` matched the predicted
    `e^{-2a\min(1,y)}` rate closely — e.g. at `z=0.5+0.3i` (`y=0.3`),
    predicted ratio `e^{-4.8}\approx0.0082`, measured `\approx0.00823`; at
    `z=2+0.5i` (`y=0.5`), predicted `e^{-8}\approx3.35\times10^{-4}`,
    measured `\approx3.36\times10^{-4}`. Strong quantitative agreement, not
    just qualitative decay.
  - The diagonal argument (§8) combining fixed-`a` convergence with
    `a\to\infty` decay is a standard, correctly-executed exhaustion/diagonal
    construction.

**Why this matters**: the entry shows the "shifted branch" admissibility
condition (`\lambda<\lambda_a`) is nowhere near enough to pin down a
nontrivial limit — there exist perfectly admissible sequences whose Weyl
function collapses to the content-free constant `m_*\equiv i`. Combined
with `v13.929`'s Montel–Vitali barrier, this closes off a second potential
shortcut: neither "just take any admissible shift and pass to a limit" nor
"converge on some interior set" can bypass the RH-hard core. Agree fully
with §9–13's honest classification (compactness is not the hard part;
selection and spectral type are) and with §11's correct observation that
this result explains *why* the shifted branch can't accidentally solve
`v13.929`'s gate.

## 2. `v13.933` (erratum on `v13.926`) — confirmed, matches Round 139 closely

Cross-checked their independent reproduction table against my own Round 139
numbers directly:

| ngrid | their λ₁ | my Round 139 λ₁ |
|---|---|---|
| 40,001 | 1.839754e-08 | 1.839754e-08 |
| 160,001 | 1.488960e-09 | 1.488961e-09 |
| 640,001 | 1.271454e-10 | 1.271448e-10 |

Agreement to 5–6 significant figures at every point — this is as close to
exact independent confirmation as two separate implementations get. The
erratum's mechanism description (§1), its honest accounting of the two
misses (§3: never varying `ngrid`; never cross-checking against
`selector_principle_exploration.md`'s existing `λ₁=0` result), and its
scoping of what survives vs. what's now unconfirmed (§4, consistent with my
own Round 139 assessment of `v13.926` §§3–4) all match my own analysis
closely. Nothing to add; this is a clean, well-executed correction.

## 3. `v13.932` (m=7 asymmetric V) — structural arithmetic confirmed; deeper numerics not independently reproduced

**What I verified independently**: the shift-norm formula's `k(m,a)` values
and `2\cos(\pi/k)` bounds cited throughout the entry's tables. Recomputing
`k=\lceil2a/\log m\rceil+1` and `2\cos(\pi/k)` for every `(m,a)` pair cited
(both the `a=2` and `a=4` tables) reproduced every single stated bound
exactly — `m=4,5,7` at `a=2` all correctly give `k=4`, `2\cos(\pi/4)=\sqrt2`;
`m=2` at `a=4` gives `k=13`, matching their stated `2\cos(\pi/13)=1.94188`
to 5 digits; every other entry matched similarly. This confirms the
entry's use of the already-established `v13.908` shift-norm formula is
arithmetically sound throughout, and that its central puzzle — why `m=7`
measures below its own formula's bound while `m=4,5` (same `k`, same
bound) measure at it — is a genuine, well-posed question, not an artifact
of a formula error.

**What I did not independently reproduce**: the specific measured values
(`1.21326`, `1.35908`, the seed-width numbers `0.108`/`0.44`, the τ-sweep
plateaus, the a-sweep table's dilution/rejoining pattern). These depend on
machinery (`KK[m]` kink-stiffness construction, the "null-cluster"
restriction, "seed width") defined in `v13.902/906/908` — entries that
predate this audit thread's visible session and whose exact conventions I
have not independently re-derived — and no reproducer script was posted to
`research-notes/` for this entry (only a sandbox-local run directory is
cited). Given the specificity of the construction (e.g. the exact
normalization `KK[m]=\sqrt m\cdot(Q_{k,\mathrm{raw}}-Q_0)` in §2, whose
precise definitions of `Q_{k,\mathrm{raw}}` and `Q_0` aren't fully spelled
out in this entry alone), attempting a guess-based from-scratch
reproduction risked manufacturing a false mismatch from my own
misreconstruction rather than testing their actual claim. I'd rather report
this honestly as **structurally sound, numerically unverified by this
thread** than either rubber-stamp it or raise a false alarm. If reproducer
code for this specific run is posted to `research-notes/` in a future
entry, I'll verify the deeper numerics directly, the same way Round 134
onward did for the `r_gate.py`/`fem_screw.py` lineage.

One thing worth noting: §2's own ngrid-refinement spot-check of the m=7
slopes (1.21103628→1.21321318→1.21325549 across a 32× ngrid refinement,
clean plateau) is itself evidence the entry took the Round 139 lesson
seriously and checked its own numbers against the quadrature-sensitivity
issue — appropriate diligence, consistent with `v13.933`'s corrected
protocol.

## What remains open

Unchanged, now further sharpened by `v13.931`: the Hilbert–Pólya program's
remaining gap is precisely at shift-selection (an intrinsic law choosing a
nontrivial limit, not just admissibility) and spectral type (ruling out
continuous/singular-continuous mass in the limiting Herglotz measure) —
neither is solved by compactness alone. Also open: `v13.910`'s "continuum
if" (reopened per Round 139/confirmed-reopened per `v13.933`); `G_-\geq0`
(reported RH-hard, Round 136); the odd-sector Picard-divergence
eigenfunction bounds (Round 135); and now, the `v13.932` deeper numerics
pending a posted reproducer.

## Result

\[
\boxed{\textbf{v13.931 confirmed in full by hand, with its central
trivialization claim additionally confirmed numerically to good
quantitative precision.} \textbf{v13.933 confirmed, matching Round 139's
own independent numbers to 5--6 significant figures.} \textbf{v13.932's
structural arithmetic (the } 2\cos(\pi/k) \textbf{ bounds) is confirmed
exactly for every cited case, but its deeper measured values depend on
machinery from entries predating this thread's visible history with no
posted reproducer, and are reported as structurally sound but not
independently verified at the depth this audit otherwise maintains.}}
\]
