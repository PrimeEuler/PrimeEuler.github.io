# Cone selector: minimal variational model, symmetry no-go and coefficient-source test

Date 2026-10-23. Parents v14.696, v14.731–739 and v14.759. Self-run gravity model, **not a derivation of G**. No Suzuki sandbox work.

## Model on a quantized pair-product leaf

For n≠0, q_n=|n|/4, parameterize positive dimensionless gravitational-pair couplings \(\alpha_1=q_ne^\psi,\ \alpha_2=q_ne^{-\psi}\). This is precisely the pair-product constraint, not a relation between an EM electric coupling and the gravitational coupling of an independently chosen particle. The two sectors have separate quantization leaves; identifying their \(\psi\) requires an extra cross-sector law.

Consider a positive quadratic cost in the two constituent couplings:
\[
U=a\alpha_1^2+b\alpha_2^2
=q_n^2(ae^{2\psi}+be^{-2\psi}),\qquad a,b>0.
\]
Here a,b would need to be computed from *physical, coordinate-invariant*, positive susceptibilities/boundary data (e.g. normalized field energies or renormalized kinetic coefficients with a specified regulator), not simply chosen to fit alpha/G.

\[
U'=2q_n^2(ae^{2\psi}-be^{-2\psi}),\quad
U''=4q_n^2(ae^{2\psi}+be^{-2\psi})>0.
\]
Unique global minimum:
\[
\boxed{\psi_*=\tfrac14\ln(b/a)},\qquad
U_{\min}=2q_n^2\sqrt{ab},\quad
U''(\psi_*)=8q_n^2\sqrt{ab}.
\]
Exact invariances: \(a,b\) rescale together -> psi unchanged; \(a\leftrightarrow b\) -> psi sign flips; a=b -> psi=0; pair rung n affects energy scale, not the selected split.

If the two sectors have exact exchange symmetry with no explicit/spontaneous symmetry-breaking coefficient, the strictly convex quadratic cost selects no hierarchy. More generally *any* exchange-symmetric convex function U(psi)=U(−psi) with unique minimizer must place it at psi=0. An exchange-symmetric **nonconvex** potential can select ±psi_0 by spontaneous breaking, but its symmetry does not determine psi_0 and cannot distinguish the sign without additional boundary data. Therefore a physical explanation must derive a strongly asymmetric coefficient ratio, a calculable dynamical transmutation scale, or a real external boundary condition.

Required ratio \(b/a=e^{4\psi_*}\). For psi≈45, ratio≈e^180≈1.49×10^78. This is the burden of explanation, not a solution: inserting that number or G itself as an input is circular. A large log could arise from a derived RG running or near-separatrix boundary, but v14.696's initial-separatrix seat is still free and not predictive.

The geometric TN areal-radius mismatch from v14.759 depends on lengths m,l and energy epsilon. It is **not** an independently computed positive quadratic coefficient ratio a/b; trying to identify it with b/a without normalized action integrals, sources, and boundary conditions is unjustified. Even a gravity-pair selector would not automatically predict the EM fine-structure constant or the ratio alpha/alpha_G: those are distinct physical quantities on distinct leaves.

## Evaluation / falsifiable fork

A *candidate real selector* must provide the following from independently stated equations, with no coupling-hierarchy target fed back in:
1. Derive a,b (or a fully specified nonlinear effective potential) from the EM and gravitoelectric/magnetic field actions, with fixed physically admissible boundary and renormalization conditions; check global causality issues for Misner time.
2. Give a regulator/gauge/coordinate-independent finite \(\psi_*\) (or a controlled running relation with measured inputs transparently listed).
3. Predict at least one independent quantity, e.g. response to source geometry or scattering, that can falsify the mechanism rather than merely fitting \(\psi_*\).
4. Verify stability (positive second variation) and sector coupling, not just a stationary point.

**Classification:** minimal variational selector *works mathematically* but provides only a conditional selection equation; physical coefficients absent; no derived G, alpha, NUT charge, field unification, or hierarchy. No sandbox work issued.
