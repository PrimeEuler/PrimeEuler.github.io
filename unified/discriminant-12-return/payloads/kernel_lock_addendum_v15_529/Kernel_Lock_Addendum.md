# Addendum to the divisor-split sign test: everything is square-mode content because of the geometric mean

*Sandbox note (little Euler), 2026-11-07, after the
v15.527 delivery. Jeremy's line, verbatim in the title.
This note makes it precise, tests its generalization,
and files the result. Producers:
`divisor_split_kernel.py`, `divisor_split_kernel2.py`.*

## The statement, precisely

Every Voronoi mode of the divisor fluctuation has phase
4π√(kx) − π/4, and √(kx) **is the geometric mean**
GM(k, x) of the mode index and the argument — the cone's
own label, the height of the pair (k, x) on its hyperbola.
A family of modes phase-locks at argument x exactly when
their GMs with x are simultaneously integers, which
happens iff mode index and argument share a **squarefree
kernel**: at x = s·m² the locking modes are k = s·j²,
with GM = s·j·m. The v15.527 seat result is the kernel-1
case: at x = m² the square modes j² lock with GM = j·m.
So the square modes are not an imposed subsequence —
they are the modes whose GM with the argument is
integral, and the seat shells are where the kernel is
trivial. Jeremy's sentence is the mechanism.

## The kernel families, measured against their own predictions [D]

Shells x = s·m² ≤ 2×10⁶ (m ≥ 2); measured mean of
Δ(x)/x^{1/4} and fraction positive; predicted coherent
contribution P_s = (1/(2π))·s^{−3/4}·Σ_j d(s j²) j^{−3/2}
with the mode sum extended by factorization to
j ≤ 20000 (as in v15.527 for s = 1):

| s | shells | measured | frac + | predicted P_s | offset+1 mean |
|---|--------|----------|--------|---------------|----------------|
| 1 | 1413 | +2.1911 | 0.999 | +2.2112 | +1.9327 |
| 2 | 998 | +1.9652 | 0.999 | +1.9519 | +1.6839 |
| 3 | 815 | +1.6773 | 0.984 | +1.6350 | +1.4671 |
| 5 | 631 | +1.3052 | 0.949 | +1.2190 | +1.2058 |
| 6 | 576 | +1.5869 | 0.974 | +1.4427 | +1.2590 |
| 7 | 533 | +1.0954 | 0.931 | +0.9782 | +0.9346 |
| 10 | 446 | +1.2898 | 0.930 | +1.0757 | +0.9233 |
| 30 | 257 | +1.2898 | 0.926 | +0.7949 | +0.8948 |

Every kernel family carries the one-sided bias, declining
with s, and ≥ 92.6% positive throughout. The lock
accounts for the measured bias to within ~1% at s = 1, 2
and ~2.5% at s = 3. (The s = 10 and s = 30 measured means
agree to four decimals, +1.289750 vs +1.289835 — verified
distinct at six decimals; a coincidence, filed as one.)

## The residual at large kernels [D]

For s ≥ 5 the measured bias increasingly exceeds the
locking modes' contribution: the lock explains 93%, 91%,
89%, 83%, 62% of the measured mean at s = 5, 6, 7, 10,
30. The mode-sum tail beyond j = 20000 is far too small
to close the gap (≤ ~0.01 in P units at s = 30, estimated
from the summand's decay). The residual's source is not
identified in this scope; the named candidates are
incomplete cancellation of the slow non-locking modes
over the sampled shell sets, and local elevation of Δ
around highly composite shells (the offset+1 controls are
themselves elevated, declining more slowly than the
shell means — the lock is a wide bump of width ~m, not a
spike, so offsets share it). Filed open, sized, not
papered over.

## Verdict

Jeremy's generalization holds: the seat phenomenon of
v15.527 is the kernel-1 member of a family — **every
squarefree-kernel shell family carries a one-sided
divisor-fluctuation bias, set by the modes whose
geometric mean with the argument is integral.** The
unifying variable is the cone's label itself: the
Voronoi phase is 4π·GM − π/4, and coherence is
integrality of the GM. Scope unchanged from v15.527:
these are fingerprint-grade structures of the divisor
layer (now a kernel-indexed family of them), classical
in mechanism, and still not a discrete selection among
framework alternatives.
