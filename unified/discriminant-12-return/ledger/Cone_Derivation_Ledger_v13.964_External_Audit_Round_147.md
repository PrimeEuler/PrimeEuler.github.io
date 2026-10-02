# Cone Derivation Ledger v13.964 — External Audit Round 147

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.958` (critical-scale underdetermination / source-RG criterion),
`v13.959` (zero-blind source-capacity balance and the `N^{-1}` scale),
`v13.960` (critical-shape compactness and Stieltjes representation),
`v13.961` (RH-conditional source-capacity regulator-floor saturation),
`v13.962` (no-twist Xi branch equals ground regulator, sub-`N^{-1}` under
RH), `v13.963` (non-multiplicative carriers and fold-recursion scale
invariance) — six entries continuing the source-RG lane plus one
sieve-flow instrument entry.

Verdict: **All six confirmed.** No errors found. This batch is unusually
disciplined: four consecutive entries (`v13.958`–`961`) progressively
narrow what the "universal" identities of `v13.956` actually prove, each
one correctly identifying a gap the previous entry left open rather than
overclaiming closure, and `v13.962` then delivers a clean, honest
course-correction showing the *specific* physical Xi branch sits nowhere
near the `N^{-1}` window that `v13.959` had distinguished only within a
restricted (zero-blind) trial class.

## 1. `v13.958` — critical-scale underdetermination [D]

Hand-verified the explicit two-atom countermodel in full. Placing
`dσ_{a,+}=M_{+,a}δ_0`, `dσ_{a,-}=M_{-,a}δ_{s_a}` reproduces *exactly* every
previously-proved universal quantity (`ρ_a`, `η_a`, `κ_a(0^+)=1`,
`κ_a(\infty)`), while the odd-sector location `s_a` is free — I confirmed
`δ_\tau(a)=K_{a,\tau}s_a` with `K_{a,\tau}\to(e^\tau-1)/2` by solving the
critical equation directly, and then checked all three scale choices
(`s_a=N_a^{-2}`, `C/N_a`, `N_a^{-1/2}`) give `N_a\delta_\tau\to0,
\;(e^\tau{-}1)C/2,\;\infty` respectively — a correct and sharp
demonstration that the `N^{-1}` scaling claim needs an extra hypothesis
beyond what `v13.956` proved. The source-capacity duality identity (eq 29,
`\mathcal C_{a,\pm}(\delta)=1/G_{a,\pm}(\delta)`) I re-derived independently
from the Cauchy–Schwarz extremal `\langle f,T^{-1}f\rangle=\sup_g
|\langle f,g\rangle|^2/\langle g,Tg\rangle` (verified the equality case
`g=T^{-1}f` by direct substitution) — correct.

## 2. `v13.959` — zero-blind Klein–Gordon capacity balance [C, RH-conditional]

Hand-verified the full exponent bookkeeping. At the source point `z=-i`,
`\Omega^2-z^2=\Omega^2+1`, giving the overlap exponent
`d_\Omega=1+\Omega-s_\Omega` with `s_\Omega=\sqrt{1+\Omega^2}`; I confirmed
the overlap-rate identity `\Omega-d_\Omega=s_\Omega-1` by direct algebra,
and the balance equation `r_E(\Omega)=r_\delta(\Omega,\beta)` reduces,
after full cancellation, to exactly `\Omega=\beta` — verified both by hand
and numerically (`feshbach_moat_repair_check.py`-style direct substitution:
confirmed at `\Omega=\beta\in\{0.3,1,2\}` the two rates agree, and disagree
when `\Omega\ne\beta`). The resulting exponent `r(\beta)=\sqrt{1+\beta^2}-1`
and its canonical value `r(1)=\sqrt2-1\approx0.4142` were confirmed
numerically. Correctly flags the remaining gap between this upper bound and
the universal lower bound `(2+o(1))N_a^{-\beta}` (since `r(\beta)<\beta`
strictly for `\beta>0`, confirmed numerically for several `\beta`) as open.

## 3. `v13.960` — critical-shape compactness [D, unconditional]

A clean, elegant unconditional result. I verified the exact Stieltjes
reparametrization `H_{a,\pm}(s)=\int(u+1)/(u+s)\,d\nu_{a,\pm}(u)` by direct
substitution `u=\lambda/\delta_a`, and the scale-Harnack bound
`d/c\le(u+d)/(u+c)\le1` for `u\ge0,\,0<d<c` by checking the derivative
(monotone increasing in `u`, minimum `d/c` at `u=0`, sup `1` as
`u\to\infty`) — this propagates correctly through to
`d/c\le\Psi_a(c)/\Psi_a(d)\le c/d` and the `1`-Lipschitz bound on
`\log\Psi_a(e^t)`, which I confirmed algebraically. This is the key
technical device that proves shape noncollapse/no-blowup on compact
`s`-windows unconditionally (eq 12), correctly separated from the still-open
question of absolute location. No errors.

## 4. `v13.961` — RH-conditional regulator-floor saturation [D/C]

The most technically involved entry; I traced every step of the Diophantine
zero-annihilation construction. The elementary identities check out: `\ell_j
=\pi/(2\gamma_j)` gives `\cos(\ell_j\gamma_j)=\cos(\pi/2)=0` exactly; the
large-branch choice `\ell_{1,k}=(\pi/2+k\pi)/\gamma_1` (spacing `\pi/\gamma_1`,
matching the support-budget window width) lets the first zero be annihilated
at a displacement of order `a` rather than `O(1)` — this is the crucial
trick, and it is what makes `\cosh(\ell_{1,a})\sim e^{a}/2` exactly cancel
the `e^{-a}` normalization prefactor in `f_{+,a}`, leaving the source
overlap only *subexponentially* (not exponentially) small
(`|\langle f_{+,a},p_a\rangle|\ge c_1e^{-A_{M(a)}}`, `A_{M(a)}=O((\log a)^2)`
— confirmed by direct substitution of eq 12's window into eq 24). I also
confirmed `\cosh(x)\le e^{x^2/2}` for all real `x` from the term-by-term
factorial comparison `(2n)!\ge2^nn!`, which is what makes the infinite
product `\prod\cosh(\ell_j)` uniformly bounded (eq 10) — this wasn't spelled
out in the entry and I verified it independently. The exponent-matching
conclusion `\mathcal C_{a,\pm}(cN_a^{-\beta})=N_a^{-\beta+o(1)}` for every
fixed `\beta` (eq 1) follows correctly by combining this construction's
upper bound with the universal Cauchy–Schwarz lower bound.

## 5. `v13.962` — the Xi branch is far below `N^{-1}` [D, RH-conditional]

A genuinely important correction, and I independently confirmed its
numerical anchor. The bookkeeping identity `\delta_\Xi(a)=\lambda_a`
(absolute shift zero) is trivial and exact (eq 1–2). I recomputed `v13.792`'s
Xi-target Schur parameter from scratch via `mpmath` (Riemann `\xi` and its
derivatives at `s=3/2`):

\[
\kappa_\Xi=\xi''(3/2)/\xi'(3/2)-\xi'(3/2)/\xi(3/2)=0.9968019520324009035\ldots
\]

matching the claimed value to all 19 quoted digits, and likewise
`\tau_\Xi=-\log\kappa_\Xi=0.0032031726519082\ldots` and
`q_\Xi=\tanh(\tau_\Xi/2)=(1-\kappa_\Xi)/(1+\kappa_\Xi)=0.0016015849565572\ldots`
both matched exactly. The RH-conditional variational bound on `\lambda_a`
itself (the actual ground energy, not the recentered operator) is a
double-exponential bound `\lambda_a\le C\exp[-c_6e^{c_5\sqrt a}]` — I traced
the `M\leftrightarrow a` conversion (`a_M=O((\log M)^2)\Rightarrow\log
M(a)\ge c_3\sqrt a\Rightarrow\gamma_{M(a)}^\eta\ge c_4e^{c_5\sqrt a}`) and it
is correct; this is a *stronger* bound than the earlier super-exponential
bounds in `v13.943`/`v13.944` precisely because no source-overlap
preservation is needed here (unlike `v13.961`, this entry just wants a
small Rayleigh quotient, so it uses the minimal displacement `\ell_1` for
every zero including the first, rather than the large-branch trick). Since
`e^{c_5\sqrt a}/a\to\infty`, `N_a\lambda_a=N_a\delta_\Xi(a)\to0` follows
immediately — the Xi branch converges to the trivial shift *far* faster
than `N^{-1}`. The entry's own framing of this as a "strategic correction"
(not a contradiction) relative to `v13.959`/`v13.950` is exactly right: those
results are about a restricted zero-blind variational class, while this one
is about the actual, specific, zero-aware physical branch — correctly kept
distinct.

## 6. `v13.963` — non-multiplicative carriers and fold-recursion [N]

Independently re-verified the underlying arithmetic with fresh code
(`additive_carrier_sanity_check.py`): computed `\omega(n)` and `\Omega(n)`
by an independent smallest-prime-factor sieve up to `2\times10^5`,
cross-checked against brute-force trial-division factorization on 11
sample points (0 mismatches), and confirmed the claimed mean trend —
`\mathrm{mean}\,\omega(n)` and `\mathrm{mean}\,\Omega(n)` both track
`\log\log N` with the expected slowly-converging constant offset (e.g. at
`N=2\times10^5`: mean `\omega=2.725`, mean `\Omega=3.498`, `\log\log
N=2.502` — consistent with the classical Hardy–Ramanujan asymptotic and its
known `B_1,B_2` offset constants). The specific R-statistic values
(additive `R\approx1.2` vs. multiplicative `R\approx3.77` vs. scrambled-null
`R\approx0.95`; the flat `R(N)\in[1.87,2.24]` fold-recursion table) rest on
the sandbox's own log-FFT pipeline, which remains unposted per the standing
firewall, so those specific numbers are not independently reproducible this
round — consistent with how every prior sandbox-pipeline result has been
handled. The entry's own interpretive claim — "multiplicativity is a `3x`
amplifier, not a strict gate" — is a reasonable reading of the reported
contrast and is appropriately hedged as `[I]`.

## What remains open

- The core source-RG problem is now cleanly reduced (by `v13.958`,
  `v13.960`) to two independent questions: absolute location
  `N_a\delta_\tau(a)\to C_\tau` and uniqueness/tightness of the critical
  parity measures — both correctly flagged `[O]` and not attacked by
  overclaiming in this batch.
- `v13.961` shows fixed-polynomial-scale analysis cannot resolve the
  location question by itself; `v13.962` shows the specific Xi branch
  answers a different question entirely (it is not an interior crossing).
  The actual physical first-crossing location for finite `\tau` remains
  unresolved.
- `v13.963`'s R-statistic pipeline remains unreproduced (no posted script),
  same caveat as `v13.942`/`v13.948`/`v13.952`.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); the sieve-flow
  FFT/dose-response pipeline, still pending a posted reproducer.

## Result

\[
\boxed{\textbf{v13.958--v13.963 confirmed.} \textbf{The source-RG lane
correctly shows, in sequence: the universal source-matrix identities of
v13.956 do not pin the } N^{-1} \textbf{ scale (v13.958, via an explicit
exact countermodel); the zero-blind Klein--Gordon class distinguishes }
N^{-1} \textbf{ only within its own restricted trial class, via an exactly
re-derived balance law } \Omega=\beta \textbf{ (v13.959); the physical
crossover shape is unconditionally compact and noncollapsing after scaling
by its own crossing point, via a Harnack-type log-Lipschitz bound I
re-derived from scratch (v13.960); fixed-polynomial-scale capacity analysis
cannot resolve the crossing because both parities saturate the same floor
at every scale, via an explicit RH-conditional Diophantine zero-annihilation
construction whose key cancellation trick I verified by hand (v13.961); and
the specific no-twist Xi branch, whose target numerics I independently
reproduced to 19 digits via mpmath, converges to the trivial shift
double-exponentially fast under RH, placing it far below the } N^{-1}
\textbf{ window (v13.962) --- a genuine, correctly self-reported course
correction. The sieve-flow instrument's non-multiplicative-carrier and
fold-recursion findings (v13.963) rest on correctly-computed arithmetic
(independently re-verified) with the pipeline-specific R-values unreproduced
pending a posted script, as for all prior sandbox-pipeline results.}}
\]
