# Cone Derivation Ledger v15.1315 — Evolved scalar spatial Einstein shear from independently varied original K4 solid

**Date:** 2026-11-22 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact first-order scalar longitudinal-versus-transverse spatial stress from the unmodified relativistic K4 solid action and its equality to the metric Einstein spatial-shear operator on the sourced scalar solution; [PASS] actually executed independent local SymPy exact-zero check; [OPEN] exact committed-byte external Audit replay, spatial trace, transverse vector and TT Einstein equations, full coupled ADM propagation, physical causal detector, G-free quarter-grid novelty. **Immediately pre-ledger HEAD:** 5960f7bc688a4e429a8b9fe4bc3eac01ddf9658a. Canonical target v15.1315 checked absent. Strict additive commits, no changes to earlier gravity, the colliding historical Audit v15.1275–1277, Suzuki, Muse/Sandbox or frozen K4.

## Gate 1241 — vary the original K4 action rather than infer material shear from Einstein geometry

For the frozen solid `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, with principal pressures `p_i=−F+2B_i∂F/∂B_i`, take Newtonian-gauge scalar spatial metric `gij=a²(1−2Psi_N)δij` and scalar solid material labels `phi^I=x^I+∂^I P`. For a k along z, first-order eigenvalues of B are `Bx=By=a^-2(1+2Psi_N)`, `Bz=a^-2(1+2Psi_N−2k²P)`. Differentiate the **unexpanded** material F and only then linearize in scalar perturbation amplitude epsilon. The exact result is

`delta p_s,x − delta p_s,z = 8 eta_s C k² P/(9a²)`.

At `a=τ/sqrt3`, `eta_s=3/4`, `kappa C=1`, the source coefficient in the mixed Einstein spatial difference is `2 k²P/τ²`. This was computed by independent symbolic stress differentiation, without rearranging the geometric Einstein equation. The solid isotropic conformal-scale perturbation cancels from this tracefree difference.

The Maxwell scalar stress spatial perpendicular-minus-longitudinal difference, averaged over the two transverse directions to k, is `9(r−3Tnn)/(2τ⁴)`, with `r=rho_conf,k`, `Tnn=n_i n_j Tij_conf,k` from the same conserved/dealiased v15.1274 stress prescription. The independently computed scalar Newtonian-gauge metric Einstein operator v15.1276 is `delta G^perp_perp−delta G^long_long = 3k²(Psi_N−Phi_N)/τ²`.

## Gate 1242 — time-dependent on-shell spatial shear identity

Substitute the original pressure-corrected K4 Bardeen transfers of v15.729 with `J_Phi=J_psi=−sqrt3 r/τ`, `J_B=−i sqrt3 k F_parallel/τ`, `J_Bdot=(−3k²Tnn+i sqrt3 k F_parallel)/τ²`; use the original sourced scalar mode equation at eta_s=3/4:

`Pdd+3Pdot/τ+(k²+2)P/τ² = 9(3Tnn−r)/(2k²τ⁴)`.

Exact algebra yields the **full scalar spatial-shear** identity

`3k²(Psi_N−Phi_N)/τ² − 9(r−3Tnn)/(2τ⁴) − 2k² P/τ² = 0`

for arbitrary time tau>0 and nonzero mode k>0, as long as the source and metric obey the declared physical Maxwell/K4 equations and shared Fourier conventions. The previously omitted solid anisotropic stress is needed when P evolves: at tau=1 P=0, recovering earlier v15.1277 initial-slice identity. This is an **on-shell algebraic consequence**, not yet a numerical independently computed full Riemann or spatial trace constraint.

The self-contained local SymPy reproducer directly differentiates the original F(B), constructs the sourced Bardeen potentials and Einstein spatial-shear operator, and simplifies their difference exactly to zero. It actually executed and printed PASS. Additive canonical GitHub source `research-notes/k4_evolved_scalar_shear_v15_1315.py` SHA 5960f7bc688a4e429a8b9fe4bc3eac01ddf9658a. Exact committed-byte Audit replay remains pending.

## Gate 1243 — remaining falsification

Combining v15.1314 with this gate gives exact conditional **time-dependent scalar** Hamiltonian, longitudinal momentum, and spatial tracefree shear identities for a conserved Maxwell source and the frozen K4 solid. None independently evaluates the remaining scalar **spatial trace** or transverse-vector / TT equations of the full physical four-metric. The next falsification must derive the spatial trace of Einstein and independently varied solid pressure from the *same* metric and P, test it over time with the v15.1274 dealiased Maxwell source, and then include vector/tensor perturbations and homogeneous Bianchi-I terms. Do not count multiple identities derived from a single sourced K4 mode equation as independent field-equation closure or infer continuum convergence from zero algebraic residuals.

**Audit handoff:** replay exact source and independently derive the sign and normalization of `p_x−p_z` from the frozen solid action; check plus/minus signatures and Fourier phases against v15.729, v15.1276; then prioritize the spatial trace and complete SVT Einstein equations. Cross-check previous Audit Round 623 warning about historical version collisions; leave those files intact.

**Scientific boundary:** this is Einstein–Maxwell plus the identical original K4 solid, with no independently justified physical action from the arithmetic quarter-grid and no distinguishable G-free gravitational observable.
