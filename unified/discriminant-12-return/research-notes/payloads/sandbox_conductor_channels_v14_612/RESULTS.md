# Other conductors — their own channels and constants

*Sandbox (little Euler), 2026-10-18. [I]/[O] exploratory. Producer:
`conductors.py` (mpmath, dps 50). Follows Jeremy's question: the
12/11 dictionary as the (n+1)/n family member.*

## The general channel [D, from repo sources]

Suzuki's zero-free formula (ledger v13.258 §3 for χ₁₂; research-notes
`suzuki_chi4_zeeman_kernel_compression.py` for χ₋₄) gives every
primitive degree-1 Dirichlet channel the same archimedean ramp shape:

𝒜_χ(t) = (t/2)[ψ(a) + log(q/π)] + (1/4)[ζ(2,a) − e^{−2at}Φ(e^{−2t},2,a)]

with q the conductor and **a = 1/4 (χ even) / 3/4 (χ odd)**. The Lerch
term is shared by all characters of a parity; the conductor enters
only through log(q/π) in the slope. Constants: C₁(χ) = ψ(a)+log(q/π);
the Lerch singular constant C_LERCH(1/4) = 0.35090557984795486267
(run 2, exact) and C_LERCH(3/4) ≈ −0.397 (3-point Richardson here,
slow w·log w convergence — refine before quoting digits).

Geometry side [I]: diameter-q circle, R = q/2, dictionary edge
L = q/(q−1) (Jeremy's (n+1)/n at n = q−1), envelope
Ã_q(t) = R√(1−e^{−2t}), quotient T_χ = 𝒜_χ/Ã_q, dive rate
**s(χ) = −C₁(χ)/q**.

## Measured channels

Control q=12 even reproduces s = 0.2406063975, t₀ = 1.912049281. ✓

| χ | q | a | C₁ | s(χ) | t₀ | bump (max 𝒜) |
|---|---|---|---|---|---|---|
| χ₅ | 5 | 1/4 | −3.762745507 | 0.7525491014 | 0.9647178 | 0.2030 @ t=0.373 |
| χ₈ | 8 | 1/4 | −3.292741878 | 0.4115927347 | 1.4049016 | 0.3101 @ 0.548 |
| χ₁₂ | 12 | 1/4 | −2.887276769 | 0.2406063975 | 1.9120493 | 0.4410 @ 0.752 |
| χ₁₃ | 13 | 1/4 | −2.807234062 | 0.2159410817 | 2.0290748 | 0.4720 @ 0.798 |
| χ₂₁ | 21 | 1/4 | −2.327660982 | 0.1108409991 | 2.8795213 | 0.7009 @ 1.123 |
| χ₂₄ | 24 | 1/4 | −2.194129589 | 0.0914220662 | 3.1726013 | 0.7798 @ 1.237 |
| χ₋₃ | 3 | 3/4 | −1.131978477 | 0.377326159 | 0.9185877 | 0.1446 @ 0.315 |
| χ₋₄ | 4 | 3/4 | −0.8442964045 | 0.2110741011 | 1.3685135 | 0.1987 @ 0.447 |
| χ₇ odd | 7 | 3/4 | −0.2846806166 | 0.04066865951 | 4.4605622 | 0.3919 @ 1.071 |
| χ₋₈ | 8 | 3/4 | −0.151149224 | 0.01889365299 | 8.4084908 | 0.4749 @ 1.457 |
| χ₁₁ odd | 11 | 3/4 | **+0.1673045072** | **−0.01520950065** | — | — |

## The threshold [D]

The dive (and with it the bump, the zero, and the whole
representation problem in its χ₁₂ form) exists iff C₁(χ) < 0, i.e.

q < π·e^{−ψ(a)}: **215.33252 (even), 9.3053617 (odd)**.

Consequences measured above: as odd q → 9.31⁻, s → 0⁺ and the zero
t₀ runs off (q=8: t₀ = 8.41); at q = 11 the constant flips sign —
s = −0.0152, 𝒜 grows positive-linearly, T_χ → +∞ at the centre, and
the overlay obstruction reappears mirrored (a +log pile-up instead
of a −log dive). Even channels keep the χ₁₂ anatomy for every
conductor up to 215.

## Scope

- Constants and anatomy are [D] (closed forms + root-finds of the
  ledgered ramp). The per-conductor geometry/dictionary pairing is
  [I] — the geometric counterpart construction, same status as the
  q=12 overlay.
- Per-channel P constructions (the kernel split at each s(χ)) were
  NOT run; the machinery is L- and s-covariant, so each is the same
  run with new constants. ζ itself is excluded deliberately: it
  carries the pole term and its conductor-1 geometry is degenerate
  (L = q/(q−1) diverges — no circle).
