# Cone Derivation Ledger v15.1057 — Conditional K4 plus/cross tensor susceptibility after secant-circle canonical lift

**Date:** 2026-11-16 Eastern; Gravity/Cone. **Status:** [D] exact K4 quartic mixed Hessian and normalized spatial overlap in a conditional double-polarization background; [N] frozen reflection-symmetric K4/Maxwell has no sourced odd channel, and canonical circle transport cannot create one; [O] sourced plus/cross background, dynamical tensor Green function, original open-q2 match. **Prewrite live HEAD:** 7c34231f764e00a5cb7eac47a2913103a16bd958 (v15.1057 reproducer); target absent. Strictly additive. No modifications to Suzuki, external Audit, Muse, Sandbox or certified objects.

## Redundancy and Audit controls
v15.602/991 gives original-unit q2 cross-shell witness T with T†T=2E and squared edge amplitude (L+1)/4. v15.995–998 derive actual frozen K4+Maxwell vertices and the reflection Z2 obstruction in a symmetric background, independently verified by External Audit Round 585 (v15.999). v15.1049 establishes Pell/V4 ray correspondence but no physical intertwiner. v15.1053–1055 give secant-circle arithmetic and sign-sheet quotient. v15.1056 proves a canonical cotangent lift plus nonunique rank-two V4 projectors, but derives no action. This gate does NOT claim to rediscover the mixed b²c² quartic K4 term or v15.997's cross-cross spatial overlap. Its focused new calculation is the cross *Hessian* response in a stipulated background containing BOTH plus and cross components, with exact normalization and zero-source control.

## Gate 866 — mixed Hessian of frozen isotropic K4 quartic invariant
The K4 invariant expansion already audited v15.999 is
J(b,c)=8/9*(b²+c²) - 8/9*(b²+c²)² + 112/135*(b²+c²)³ +...
At quadratic-plus-quartic truncation:
∂²J/(∂b ∂c)=-64/9*b*c.
Thus every reflection-symmetric plus-only background c=0 has zero plus/cross mixed Hessian. The next r⁶ contribution produces higher-order BC(B²+C²) corrections, so the formula is explicitly **quartic-truncation only**, not exact nonperturbatively.

For a stipulated background b0(z)=B cos(2z), c0(z)=C cos(2z), take normalized tensor spatial modes e0=1/sqrt(pi), e4=sqrt(2/pi)*cos(4z) on z in [0,pi]. Direct exact integration:
I04=int_0^pi e0 e4 cos²(2z) dz = sqrt(2)/4.
The mixed mode response from the quartic J contribution, with the action-dependent overall prefactor stripped off, is
K04^(J4)=-64/9*B*C*I04=-16sqrt(2)/9*B*C.
This is an off-diagonal Hessian of the chosen elastic invariant, not yet a propagator or photon transition vertex; other EH, background, kinetic and constraint contributions require treatment in a full theory. Under C->-C the kernel changes sign, and C=0 makes it vanish. Its magnitude cannot be inferred without an independently derived background C.

## Gate 867 — selection-rule and canonical-coordinate invariance
For the reflection-invariant reduced Maxwell/K4 system of v15.998, parity P_y reverses A_y and cross metric c while leaving A_x and plus b invariant. With no parity-odd background/source, integrating out the tensor modes preserves parity: any effective photon-only term with an odd number of y-photon insertions, notably O4=(a_x†)^3 a_y, has zero coefficient. Conjugating or reparameterizing the secant-circle phase space is a canonical coordinate change and cannot alter this zero physical matrix element. The two signed circle sheets are not identified with photon P_y representations by any established physical carrier, so the argument is **not** a claimed equivalence of the two parities.

A nonzero C could break the veto, but requires a sourced solution to actual field equations, a nonsymmetric boundary, or a physical parity-breaking external condition. Even in such a hypothetical background, the full nonlinear propagator, coupling normalization and shell-by-shell q2 matrix matching remain open. Prior v15.998 shows an unsourced even symbolic O4 monomial 2sqrt3 can appear in a product of physical vertices, but its coefficient cannot be promoted to a physical interaction absent such a propagator.

## Gate 868 — exact reproducer and conclusion
Script research-notes/k4_cross_spurion_circle_source_v15_1057.py, commit 7c34231f764e00a5cb7eac47a2913103a16bd958, tests the symbolic b,c Hessian, normalized spatial overlap, projected BC coefficient, parity oddness and zero-at-C. An independent local SymPy computation executed successfully with results -64bc/9, sqrt2/4, -16sqrt2 BC/9. Independent Audit of this gate pending.

**Verdict:** a precisely scoped conditional positive (mixed tensor response linear in a stipulated parity-odd cross background) with a robust negative (symmetric frozen-source model still zero and canonical circle transport cannot supply the missing parity-odd input). No physical frequency, universal rank-two selector, G-free dimensionless observable or quarter-ladder coupling derived.

**Audit handoff:** verify coefficient -64/9, overlap sqrt2/4 and truncation limitation; distinguish physical parity from V4/product sign and avoid interpreting the local Hessian as a sourced propagator. A future gate must solve constraints and find independently physical background/boundary source, and then compare full matrix elements with q2 T†T=2E for multiple L.
