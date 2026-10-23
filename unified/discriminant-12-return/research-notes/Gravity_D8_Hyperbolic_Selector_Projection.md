# Gravity D8-equivariant compact–hyperbolic selector test

Date 2026-10-23. Parent ledger v13.535, v13.599, v13.624, v14.760–763. All statements are **model-theoretic**, not a proven intertwiner from tetrahedral paths to the physical cone.

## Construction
Let D8 act on a compact phase angle by \(\theta\mapsto\theta+k\pi/2\) and \(\theta\mapsto-\theta+k\pi/2\), k=0,1,2,3. It does not act on rapidity u≥0 or freely chosen real offset s. Define a coupled seed
\[
\mathcal K_s(\theta,u;z,t)=e^{-z\cosh u+t\cosh u\cos\theta}\cosh(su),\qquad z>|t|\ge0.
\]
Group-average over 8 elements:
\[
P_{D8}\mathcal K_s
=\frac12e^{-z\cosh u}\cosh(su)
[\cosh(t\cosh u\cos\theta)+\cosh(t\cosh u\sin\theta)].
\]
Exact derivation: the quarter-turn orbit has cosθ, -sinθ, -cosθ, sinθ, each duplicated by reflections; averaging exponentials gives the two cosh terms. Numeric independent 8-term enumeration checked at sample point to floating precision.

The quarter-turn/reflection projection selects Fourier cos(4nθ) harmonics, forbids sin and all other orders. But \(\cosh(su)\) is independent of θ so every s is allowed. Integrability: \(|P\mathcal K_s|\le e^{-(z-|t|)\cosh u}\cosh(|s|u)\); superexponential damping at large u makes the u-integral finite for all finite real s. The projected kernel is even in s. Indeed its derivative vanishes at s=0 and second derivative positive for the *unnormalized positive integrated kernel*:
\[
\partial_s^2\int_0^\infty P\mathcal K_s\,du
=\int_0^\infty u^2 P\mathcal K_s\,du>0.
\]
Thus treating the integrated kernel itself as an energy would minimize at s=0, but there is **no derived reason** it equals a physical effective action, nor that monopole s equals the free pair split ψ. Using negative log or other functional may reverse stability.

## Connection to earlier exact D8 results and guardrails
v13.599 proved \(\ker Q_j\) is one even line for integer j and empty for half-integer j, with spectral-flattened nonzero part carrying D8 planes. It is an abstract real representation connection, not an identified zero-mode of this integral operator. Projected scalar angular functions carry the **trivial D8 representation**, while standard two-dimensional D8 representation \(\rho\) has no fixed vector, so its direct group average is zero. As a result, naïvely projecting a single nonzero-volume plane from v13.599 onto invariants annihilates it; the integer-spin trivial kernel line survives but does not dictate s. This proves an important representation-theoretic obstruction to identifying the group projector with a physical offset selector.

A physically meaningful coupling between \(\rho\) and scalar invariants requires tensor/intertwiner data, e.g. \(\rho\otimes\rho\) contains a scalar via the dot product, and a specified action/Hessian for ψ. The exact marked-generator mismatch from v13.535 must be respected before identifying the tetrahedral representation with the hyperbolic phase action.

## Verdict
D8-equivariant coupled compact–hyperbolic operator constructed and explicitly projected. Harmonic selection proven. No distinguished nonzero s or ψ produced by equivariance alone; tetrahedral zero-volume state does not cure this. Next test: derive a genuine cross-sector intertwining kernel from Cone phase seats and a physical action, and test independent normalization / boundary data. No G, α or hierarchy derived. No Suzuki sandbox tasks.
