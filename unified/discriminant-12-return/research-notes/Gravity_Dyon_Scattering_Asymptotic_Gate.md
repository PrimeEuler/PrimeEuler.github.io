# Gravity scattering gate: Taub–NUT versus MIC–Kepler radial-action obstruction

Date 2026-10-22. Parents v14.731–736. Self-contained symbolic computation; no Suzuki sandbox.

## Exact radial equations [D]
TN timelike HJ in geometric units, Sigma=r²+l², f=(r²−2mr−l²)/Sigma, conserved energy epsilon, angular Casimir J², and s=2epsilon*l:
\[
p_{r,\rm TN}^2=\varepsilon^2/f^2-1/f-(J^2-s^2)/(\Sigma f).
\]
MIC–Kepler in its standard flat-space normalization (Zwanziger s²/r² correction INCLUDED):
\[
H_{\rm MIC}=\tfrac12p_r^2+\frac{J^2}{2r^2}-\frac{\kappa}{r},
\quad
p_{r,\rm MIC}^2=2E+\frac{2\kappa}{r}-\frac{J^2}{r^2}.
\]
Here J² is the complete monopole angular Casimir, so the additional MIC inverse-square term is load-bearing: it cancels the deficit in mechanical angular momentum. Without that correction one is not comparing the separated integrable MIC system.

## Asymptotic expansion [D, independently symbolic]
Direct expansion about x=1/r=0:
\[
p_{r,\rm TN}^2=(\varepsilon^2-1)
+\frac{2m(2\varepsilon^2-1)}r
+\frac{(8\varepsilon^2-2)l^2+(12\varepsilon^2-4)m^2-J^2}{r^2}
+O(r^{-3}).
\]
This expression follows without assigning values to m,l,epsilon,J. In particular, with m=0 but l nonzero, the inverse-square mismatch with the standard MIC model remains \((8\varepsilon^2-2)l^2/r^2\). Matching the constant and 1/r terms sets E=(epsilon²−1)/2 and kappa=m(2epsilon²−1); it does not remove the generic 1/r² residual.

## Interpretation / no-go scope
The asymptotic difference is a **fixed-r, fixed-canonical-normalization obstruction** to literal radial-action equality with the standard flat MIC–Kepler Hamiltonian and the same angular Casimir. A radius change, energy-dependent action scaling, time reparametrization, or nontrivial symplectic map might transform the radial form; this computation is NOT a proof such maps do not exist. Nor does equality of the angular orbit cones establish equality of radial periods or scattering angles. True coordinate-invariant comparison requires computing a matched radial action or scattering map with consistent asymptotic physical angles, impact parameter, and bundle/gauge patch conventions. Taub–NUT's global asymptotics and Misner string add further nontrivial conditions.

The fixed-j boost ceiling from v14.731 is a kinematic angular admissibility bound; this 1/r² difference provides no new universal physical boost bound or law relating EM and gravitational couplings.

## Reproducer
Use SymPy to series-expand the exact expression via x=1/r; deposited producer gravity_dyon_scattering_asymptotics.py. No external numerical physics inputs.

**Verdict:** angular worldline core verified; naive full radial unification fails generically at order 1/r²; unrestricted canonical equivalence and full field unification remain open. No G derived, no Xi correction, no Suzuki compute.
