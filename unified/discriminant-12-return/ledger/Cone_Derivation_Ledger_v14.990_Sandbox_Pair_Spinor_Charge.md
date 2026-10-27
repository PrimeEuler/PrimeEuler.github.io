# Ledger v14.990 — Sandbox: the pair spinor — crossing point's square root carries a conserved, quantized, ghost-free charge

**Lane:** Sandbox (little Euler), exploratory; continuation of v14.988.
**Parents:** v14.946 (s-shift model, continuous charge), v14.952/953
(Hessian pair metric; ghost as matter target), v14.985 (discreteness is
pair-side), v14.988 (U(1) quantizes the dressed momentum, kinematically).
**Payload:** `payloads/pair_spinor_v14_990/` (NOTE.md + spinor.py).
Suzuki-quarter weld PARKED; no protected files touched.

## Results [D], machine-verified

**Spinor dictionary.** For χ = √u + i√v on a positive pair (u, v):
χ² = (u−v) + 2i√(uv) = 2(X + iY), |χ|² = u + v = 2T — the crossing point
W = X + iY has χ as its spinor square root (double cover χ → −χ);
φ = arg W = 2 arg χ, z = (χ/|χ|)², tanh s = cos 2θ, sech s = sin 2θ,
dθ/ds = −1/(2cosh s). The (ħ/2)ℤ lattice of φ-momenta (v14.988) is the
ℏℤ lattice of θ-momenta through the square root.

**Two pair metrics.** Hessian (product side): 2 du dv, Killing = s-shift,
charge continuous, ghost as matter target (v14.953). Spinor (sum side):
|dχ|² = (du²/u + dv²/v)/4, whose (ρ, s) matrix
[[cosh s/(2ρ), sinh s/2], [sinh s/2, ρ cosh s/2]] has determinant exactly
1/4 — positive-definite, no ghost. Killing = θ-rotation at fixed r = √(2T).

**The charge.** For S = ∫[(1/2)|∂χ|² − V(|χ|)], the θ-rotation is an
exact symmetry with Noether density, in pair variables,
**q_χ = √u ∂_τ√v − √v ∂_τ√u = −ρṡ** (machine-verified): product-side
amplitude times shape velocity. Conserved on-shell; ℏℤ spectrum by U(1)
single-valuedness (θ ∈ S¹). First object in the source search that is
simultaneously an exact Noether charge of an explicit action, ℏℤ-quantized,
and carried by a ghost-free kinetic term. It is distinct from both
v14.946's Q_s and v14.988's fixed-ρ dressed momentum.

## Status of the identification [I/O]

The open question is now a **metric-selection question**: physical
matter-target kinetic term = Hessian (spacetime-side, ghost as target) or
spinor (healthy, compact charge)? Nothing yet forces the choice. Coupling
of q_χ to the k4 radial flux or stress-energy NOT derived — source = q_χ
remains a conjecture with an explicit healthy model attached.
G_derived=FALSE; Suzuki_quarter=PARKED.

## Handoffs

→ **external-audit:** verification of the payload identities.
→ **gravity lane:** information — a healthy pair-side candidate charge
exists on the spinor metric; relevant to the lane's constitutive
necessary-conditions gate (v14.986 NEXT) as a target-space alternative.
No action requested.
