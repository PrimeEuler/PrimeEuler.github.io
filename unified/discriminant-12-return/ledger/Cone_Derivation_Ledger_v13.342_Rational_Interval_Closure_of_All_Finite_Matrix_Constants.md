# Cone Derivation Ledger v13.342 — Rational-Interval Closure of All Finite-Matrix Constants

After v13.339--341, every remaining constant in the N=155 finite matrix can be enclosed from rational data alone.

- π: Machin formula
  \[
  \pi=16\arctan(1/5)-4\arctan(1/239)
  \]
  with alternating-series remainder.
- logarithms: power-of-two scaling plus the atanh series.
- square roots √2,√3,√5,√7: rational Newton/bisection intervals.
- base prime trigonometric constants: Taylor series after certified argument reduction.
- Euler γ: Euler-Maclaurin at N=64.
- small Si/Ci values: entire power series.
- large odd Si/Ci values: Laplace asymptotics with exact integral remainder.
- archimedean block: exact rational Bernoulli/Euler Taylor coefficients plus finite sine/cosine moment recurrences and an analytic truncation bound.
- pole block: exact rank-one formula.

Representative proof settings overresolve the current needs by many orders of magnitude: Machin 24/8 terms, 32 log terms, 50 small-Si/Ci terms.  The finite matrix therefore admits an implementation using exact integer/rational arithmetic and outward-rounded rational intervals only; general transcendental libraries are optional accelerators, not trusted proof primitives.

This is a certificate-construction result, not a positivity or RH result.