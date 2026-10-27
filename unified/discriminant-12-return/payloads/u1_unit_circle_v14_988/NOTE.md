# Can charge quantization be derived from U(1) as the ħ unit circle? (Sandbox test)

**Proposal (Jeremy, 2026-10-27).** Derive the quantized source charge from
U(1) being the ħ unit circle: phase = action/ħ winds on U(1), and
single-valuedness is quantization (his v14.620 framing).

**Answer in one line.** Yes — for the momentum conjugate to the pair's
circular angle; and that momentum is not the bare squeeze momentum p_s the
flux chain tested, but the AM/GM-dressed momentum L = cosh(s)·p_s.

## The two parametrizations of a pair [D]

For a factor pair (n, k), the unit-circle encoding
z_{n,k} = ((n−k) + 2i√(nk))/(n+k), |z| = 1, has angle φ with

  cos φ = (n−k)/(n+k) = tanh s,   sin φ = 2√(nk)/(n+k) = sech s,

where s = (1/2)ln(n/k) is the shape (rapidity) coordinate — the
Gudermannian bridge between the hyperbolic and circular parametrizations,
verified symbolically (dφ/ds = −sech s exactly; ∫sech s ds over R = π, one
orientation covers the upper semicircle; the swapped pair covers the
lower; together the full U(1)). The dressing factor is the means ratio:

  cosh s = (n+k)/(2√(nk)) = AM/GM  (= the γ of v14.621).

Classically, (φ̃, L) with φ̃ = π − φ and **L = cosh(s)·p_s** is an exact
canonical pair: {φ̃, L} = φ̃'(s)·cosh s = sech s·cosh s = 1 (machine-checked).
Quantum-mechanically L is unitarily the circle momentum −iℏ∂_φ̃ under this
change of variables (measure sech s ds), so single-valuedness on U(1)
gives **L ∈ ℏℤ**. This is the same mechanism as the dyon quarter's Misner
derivation (v14.731): a periodic identification quantizing its conjugate
charge. It is Jeremy's ħ-unit-circle principle applied to the pair angle.

## Why the flux chain's negative is consistent [D/I]

v14.944–950 tested the bare shift charge Q_s = ∫π_s of the s-translation.
s is hyperbolic, its conjugate p_s is a boost, and boosts do not quantize
— correctly negative, but about the *undressed* variable. The U(1)
variable is φ, and its charge is the dressed field momentum

  Q_φ = −∫ cosh(s) π_s d³x   (vs. Q_s = ∫ π_s d³x).

On the isotropic k4 background the factor pairs are equal (s₀ = 0),
cosh s₀ = 1, and Q_φ = −Q_s there: the distinction is invisible in every
background analysis so far and bites only for anisotropic configurations,
where the homogeneous mode's s-charge would sit in units ℏ·sech(s₀).

## What is NOT derived [O]

- That the physical k4 radial source charge (v14.944's Φ) *is* Q_φ. The
  quantization of Q_φ is derived; its identification with the
  gravitational source amplitude is a new, precise conjecture, not a
  theorem: **the source charge, if U(1)-derived, is the φ-momentum
  (winding) charge with lattice ℏℤ, equal to the bare s-flux only at
  s = 0.**
- The vertices φ = 0, π are the degenerate pair points (Y = 0); smoothness
  of eigenfunctions across them is exactly the single-valuedness
  condition used above, but a full field-theoretic realization of the
  φ-parametrization (vs. the s-parametrization of v14.946/952/953, whose
  kinetic functions differ by the cosh²s Jacobian factor) is not built.
- No coupling of Q_φ to stress-energy or gravity is shown. G not derived.
  Suzuki-quarter weld remains parked.

**Reproducer:** `gudermannian.py` (payload): verifies |z| = 1, the
Gudermannian identities, dφ/ds, the sech measure, cosh s = AM/GM at sample
crossings (incl. (1,4): 5/4), and the canonical bracket {φ̃, L} = 1.
