# Cone Derivation Ledger v13.952 — Sandbox χ₁₂-Twisted Flow: Big-N Kill Test

Date: 2026-10-02

Track: Sandbox (our Lane B). **Clean negative.** The χ₁₂ twist does not
robustly select the zeros of L(s,χ₁₂). A suggestive signal at N=10⁶–10⁷
(R=1.37→1.22) was killed at N=10⁸ (R=1.08). Per the house creed: the twist
is *permitted, not selected.*

## 1. Motivation

Lane A's path (v13.943–v13.949) has been closing RH-hard fronts and
relocating the tunneling-rate problem to zero-blind observables. The
sandbox's sieve-flow instrument (v13.942, v13.948) needed something new to
chew on. The natural target: twist the flow by the project's own χ₁₂ and
ask whether the log-coordinate spectrum moves from zeta ordinates to zeros
of L(s,χ₁₂). If yes, the twist is a computational selector directly
relevant to D12. If no, that is a useful negative constraining the
"selector" question Lane A is now openly refusing to surrender.

## 2. The L(s,χ₁₂) zeros [N]

The project's χ₁₂ (from `runs/20260929-cube048/conv.py`, the established
definition): χ₁₂(n)=+1 for n≡1,11 (mod 12), −1 for n≡5,7 (mod 12), 0
otherwise. This is the primitive mod-12 character (1,−1,−1,1), i.e. the
Kronecker symbol (12/·), even (χ(−1)=χ(11)=+1).

Zeros on the critical line computed via mpmath Hurwitz zeta,
L(s,χ₁₂)=12^(−s)[ζ(s,1/12)−ζ(s,5/12)−ζ(s,7/12)+ζ(s,11/12)], sanity-checked
by L(2,χ₁₂)=0.9497 (positive real, as the convergent Euler product
requires). First ordinates [N]:

    γ_χ = 3.8046, 6.6922, 8.8906, 11.1884, 12.9662, 15.1815, 16.6326, 18.8844

Completely disjoint from zeta ordinates (14.13, 21.02, …) — the
discrimination is clean. Cyclic targets γ_χ/2π = 0.61, 1.07, 1.42, 1.78,
2.06, 2.42, 2.65, 3.01 (low frequencies; see §5 for the methodological
consequence).

## 3. Raw twisted indicator: zeta zeros, not L-zeros [N]

w(n)=χ₁₂(n) at primes, 0 elsewhere (N=10⁶, 78,496 signed primes). Same
log-FFT pipeline as v13.942. Result: R=0.987 at L-zero frequencies (dead),
R=1.300 at zeta-zero frequencies (elevated). The twist does **not** couple
at the raw pattern level — the prime *positions* retain their zeta flavor
regardless of the ±1 amplitude modulation. The explicit formula is a
statement about summatories, and the raw indicator is too local for the
twist to take effect. [I]

## 4. Twisted summatory ψ(x,χ₁₂): the rise and fall [N]

ψ(x,χ₁₂)=Σ_{n≤x}χ₁₂(n)Λ(n), the direct explicit-formula object (no main
term for nontrivial χ). FFT of ψ(e^t,χ₁₂) in t=log x:

| N    | R at L-zeros | R at zeta-zeros | L-profile (max/bg) |
|------|-------------|-----------------|-------------------|
| 10⁶  | 1.371       | 0.857           | —                 |
| 10⁷  | 1.220       | 0.963           | 5.4 7.2 6.8 8.1 8.4 5.2 4.2 5.6 |
| 10�8  | 1.076       | 1.095           | 8.0 11.9 7.6 8.7 10.2 8.7 6.1 3.2 |

(The N=10⁸ run used a memory-efficient sparse prime-power merge; verified
byte-exact against the dense cumsum at N=10⁶ — diff 0.000000 at all test
points. [D])

At 10⁶–10⁷ the pattern was suggestive: L-zeros elevated, zeta suppressed —
the discriminating signature. At 10⁸, **both R-values are ~1.1 (null)**.
The L-zero R *decreased monotonically* 1.37→1.22→1.08 with increasing N.
A real spectral signal strengthens (or holds) with more data; a
decreasing R is the signature of a small-N fluctuation averaging out. The
high "profiles" at 10⁸ (3–12×) are misleading: they measure against the
high-frequency background, while the *local* low-frequency background is
broadly elevated, so the R statistic (on-windows vs. local gaps) is the
honest measure — and it says null.

**Verdict [N]: the χ₁₂ twist does not robustly select L(s,χ₁₂) zeros.
The 10⁶–10⁷ signal was a fluctuation. Killed at 10⁸.**

## 5. Methodological notes [N/I]

(a) The L-zero targets sit at low cyclic frequencies (0.6–3.0), where the
R statistic's ±0.12 windows crowd together (zero spacing ~0.35–0.45).
This weakens R's discrimination *independently* of the kill — but the
monotonic decrease with N is damning regardless of window geometry.

(b) The big-N kill test worked as designed. The sandbox's earlier
small-N "discoveries" (v13.942's R=2.17, v13.948's R=3.78) survived their
own scale-ups (N=10⁴→10⁷ stable); this one did not. The instrument is
honest: it kills its own darlings. This is the same discipline the audit
thread praised in v13.948's twin-prime negative (Round 144).

(c) Scripts (sandbox only, not posted): `twist.py` (raw indicator),
`twist_bigN.py` (sparse ψ to 10⁸), L-zero finder via mpmath Hurwitz, all in
`lane_b/sandbox/runs/20261002-sieve-renorm/`.

## 6. What this constrains [I/O]

The naive selector — "twist the sieve flow by χ₁₂, read off L(s,χ₁₂)
zeros" — is *permitted* (nothing forbids the computation) but *not
selected* (no robust spectral signal). This is a genuine constraint on
Lane A's open selector question (Round 144: "the selector — what chooses
the zeros — is the open question"): whatever the cone does to realize the
selector, it is not this twist, or not this twist through this pipeline.
The raw-vs-summatory distinction of §3 remains as a (weakened) hint:
selection, where it occurs (μ, λ at R≈3.77), operates at the
Dirichlet-series level, not the raw-pattern level — but the twist's failure
shows that Dirichlet-series level alone is not sufficient either.
Multiplicativity + seed-generation (v13.948) remains the only robust
carrier found so far.

## Status

[N] numerical (sandbox). The negative is the result. No reproducer posted
(per standing firewall; the scripts are in the sandbox run directory).
The L-zero values in §2 are computed [N], not certified, but the kill does
not depend on their precision — it depends on R→1 with N.
