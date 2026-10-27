# The pair spinor: the crossing point has a square root, and its charge is conserved and quantized (Sandbox)

**Continuation of v14.988.** There the U(1) (ħ unit circle) derivation
quantized the dressed momentum L = cosh(s)·p_s kinematically, but no field
theory carried that charge as a conserved Noether charge. This note builds
the phase-primary pair theory and finds the charge — at the cost of a
different kinetic metric on pair space than the cone's Hessian.

## The spinor dictionary [D]

Let χ = √u + i√v for a positive factor pair (u, v). Then exactly:

  χ² = (u − v) + 2i√(uv) = 2(X + iY),   |χ|² = u + v = 2T,

for the crossing (X, Y, T) = ((u−v)/2, √(uv), (u+v)/2). **The crossing
point W = X + iY has χ as its spinor square root** (χ → −χ is the double
cover); the encoding phase is φ = arg W = 2θ with θ = arg χ, and
z = (χ/|χ|)². With u = r²cos²θ, v = r²sin²θ (r² = 2T):
tanh s = cos 2θ, sech s = sin 2θ, dθ/ds = −1/(2 cosh s); at fixed ρ the
θ-flow is −2cosh(s) times the φ̃-flow of v14.988 — the (ħ/2)ℤ lattice of
φ-momenta is the ℏℤ lattice of θ-momenta seen through the square root.

## Two natural pair metrics, two symmetries [D]

- **Hessian** (from the product P = uv): dℓ² = 2 du dv
  = 2dρ² − 2ρ²ds² (v14.952). Killing symmetry: s-shift. Charge Q_s,
  continuous spectrum; as a matter target the s-direction is a ghost
  (v14.953).
- **Spinor** (from the sum-side radius r = √(2T)): |dχ|² = dξ² + dη² in
  ξ = √u, η = √v, i.e. (du²/u + dv²/v)/4. In (ρ, s) its matrix is
  [[cosh s/(2ρ), sinh s/2], [sinh s/2, ρ cosh s/2]] with
  **determinant exactly 1/4 > 0 — positive-definite, no ghost**
  (machine-verified). Killing symmetry: the θ-rotation χ → e^{iα}χ
  (fixed r, i.e. fixed sum/T).

## The charge [D]

For S = ∫[(1/2)|∂χ|² − V(|χ|)] (any V of the modulus; flat/frozen
background for the density), the θ-rotation is an exact symmetry and its
Noether charge density in pair variables is

  q_χ = Im(χ*∂_τχ) = √u ∂_τ√v − √v ∂_τ√u = **−ρ ṡ**   (machine-verified),

the product-side amplitude times the shape velocity. It is conserved
on-shell, and its operator spectrum is ℏℤ by the same U(1)
single-valuedness (θ ∈ S¹, χ single-valued by construction) — the first
object in the source search that is simultaneously (i) an exact Noether
charge of an explicit action, (ii) ℏℤ-quantized, (iii) carried by a
ghost-free kinetic term. Note it is NOT v14.988's fixed-ρ dressed
momentum and NOT v14.946's Q_s; three different actions give three
different charges, and only the spinor action's symmetry is compact.

## What this does and does not settle [I/O]

- The source-identification question sharpens to a **metric-selection
  question**: is the pair's physical (matter-target) kinetic term the
  Hessian one or the spinor one? The Hessian is selected by the product
  function's second derivative and generates the gravity lane's spacetime
  side; the spinor metric is selected by the T-circle's square root and
  is the healthy matter-side candidate. Nothing yet forces the choice.
- q_χ = −ρṡ is a pair-side charge (built from ρ, answering v14.985's
  requirement), but no coupling of q_χ to the k4 radial flux Φ (v14.944)
  or to stress-energy is derived. Source = q_χ remains a conjecture,
  now with an explicit healthy model attached.
- The vertices u = 0 or v = 0 are the spinor metric's coordinate
  singularities (centrifugal type, as in polar coordinates at r = 0 on
  the ξ/η axes) — regular for χ itself, singular only in (u, v)
  coordinates. G not derived. Suzuki weld parked.

**Reproducer:** `spinor.py` (payload): verifies the χ² dictionary, the
tanh/sech–2θ identities, the kinetic matrix and its determinant 1/4, and
q_χ = −ρṡ.
