# Cone Derivation Ledger v15.1389 — Phase-matched on-shell Weyl–H² current with nonzero transverse Maxwell response

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Parent:** v15.1381/1382 Weyl–Maxwell–H² area operator, v15.1385 off-shell transverse response, v15.1388 on-shell photon gate. **Live preledger master HEAD:** 219b7e01c0cc3dda5389fa1cc61c3cd39086fbd7. **Status:** [N PASS at prescribed leading backgrounds] three *individually on-shell* wave four-vectors combine to a *null* output four-vector whose tensor-derived conserved electromagnetic source is **transverse and nonzero**; [N PASS] analytic resonant retarded response matches independent full ODE and independent Green quadrature to near 10^-15; [NEGATIVE] sources are infinite plane waves, no finite energy, no total coupled stress-energy conservation, no cutoff or measured detector, no dimensionless quarter-grid coupling fixed; [OPEN] finite localized wave packets, coupled field equations, stable fully backreacted solution and same-enlarged-EFT comparator. Strict additive, no historical file changed.

## Gate 1303 — exact on-shell Fourier geometry

Work in flat (-+++) coordinates in the leading perturbative limit. Choose two **distinct** positive-frequency null internal sigma waves with lower-index Fourier wave-vectors p=(-1,1,0,0) and q=(-1,0,1,0). Choose the conjugated Fourier branch of a physical linearized vacuum TT gravitational wave with lower-index vector k=(-1,1/2,1/2,1/√2), spatial direction c=(1/2,1/2,1/√2). It is exactly null: k·k=0. Define TT polarization e1=(1,-1,0)/√2 and e2=c×e1=(1/2,1/2,-1/√2); h_ij=e1_i e1_j−e2_i e2_j, with h0μ=0. It is exactly symmetric, tracefree and transverse to c. Its linear vacuum Ricci is zero. The leading area two-form from the two *independent* internal wave derivatives has Fourier coefficient B_ab=−(p_a q_b−q_a p_b), up to common internal amplitudes a*b.

The generated difference-frequency Fourier branch has

P=p+q−k=(-1,1/2,1/2,−1/√2).

This **exactly obeys P·P=0**, so its (omega_out,|q_out|)=(1,1). This contrasts v15.1385's original off-shell branch (1,√3): the obstruction was the chosen geometry/phase matching, not a universal no-radiation theorem. The physical real incoming waves contain both conjugate Fourier signs needed for p+q−k; no nonlinear frequency insertion or altered dispersion is needed.

## Gate 1304 — real tensor source has a transverse on-shell channel

Compute the full linearized Weyl/Riemann tensor from h via the explicit four-index Fourier second-derivative formula and verify all Ricci components vanish to numerical roundoff (~5.6e−17). Define K_mu nu=C_mu nu rho sigma B^{rho sigma}; the proposed **freely chosen** EFT Weyl operator contributes an effective Maxwell current J^ν∝−∂_μ K^{μν}. Direct antisymmetric contraction gives a complex Fourier current (after factoring out common wave amplitudes and coefficient) proportional to

J^mu=(0,i/2,−i/2,0).

The computed source is conserved to ~8.2e−18, P_mu J^mu=0, and its *spatial transverse projector* equals itself because q_out·(1,−1,0)=0. Norm |J_T|=1/√2. This is a **genuinely on-shell transverse Maxwell source for the specified chosen EFT operator**. It is not a derivation of a fundamental quarter-grid gravitational interaction. No earlier source or material action was modified. The three inputs solve their *decoupled leading-order* null wave equations, not the full coupled system; sigma stress at order f²a²/f²b² and TT backreaction must be accounted for in a true energy exchange experiment.

## Gate 1305 — resonant retarded Maxwell wave and independent verification

With illustrative free coefficient g_eff=0.02 and current Fourier amplitude J0=g_eff J_T, in the positive spatial Fourier branch the transverse Maxwell oscillator is

A_T''+|q_out|² A_T=−J0 exp(−i omega_out t), |q_out|=omega_out=1,

and zero initial A(0),A'(0). Its exact retarded solution is

A_T(t)=[J0/(2i omega_out)] [t exp(−i omega_out t)−sin(omega_out t)/omega_out].

The t exp(−i omega t) term is the expected **resonant secular response** in the infinite monochromatic prescribed-background approximation. This is not permission to extrapolate arbitrary energy growth: backreaction, finite wave packet duration, kinetic energy transfer, and EFT validity must bound a real experiment.

Actual locally executed /mnt/data/cone_gate/k4_quarter_weyl_phasematched_photon_v15_1389.py evaluated (i) the full TT Weyl tensor, (ii) source transversality and conservation, (iii) an independent adaptive quadrature of the retarded Green sine kernel, and (iv) an independent SciPy solve_ivp ODE, agreeing at:

| model t | |A_T|, g_eff=.02 | max absolute Green/ODE vs analytic |
|---|---:|---:|
| .4 | .0011114002196915423 | 1.10e−16 |
| 1 | .006319715149624582 | 4.89e−16 |
| 2 | .01780509309305579 | 1.39e−15 |
| 4 | .025115052289822908 | 3.97e−15 |

This calculation checks **classical radiative mass-shell kinematics and retarded Maxwell response**, not canonical photon quantization, irreversible emitted radiation flux, full interacting Hamiltonian conservation, or a single isolated on-shell scattering amplitude. Since all prescribed input waves fill space forever, no finite-energy detector waveform or physical photon count can be inferred. Arbitrary illustrative g_eff sets the amplitude; any conventional theory with the identical extended Weyl–sigma–EM action reproduces it.

**Additive GitHub reproducer** `research-notes/k4_quarter_weyl_phasematched_photon_v15_1389.py`, SHA **af9e6324c40abdf7029a5a9502d41bb99cf1d87c**, authored with the same tests; precise committed-byte replay by external Audit pending. Local runtime file actually executed and printed the above results.

## Audit and next physical test

**AUDIT:** independently reconstruct null input and output 4-vectors with metric (-+++), both transverse TT polarization basis vectors, Ricci zero, all four Weyl-index contractions, resulting complex J and Ward identity, and Green/ODE sign/normalization. Distinguish off-shell gate v15.1388 from positive phase-matched v15.1389, and flag the chosen free g_eff and infinite-plane-wave energy issue. Review possible on-shell EFT operator redundancies beyond the earlier simple field-redefinition no-go; null P and nonzero J are only necessary, not automatically a gauge-invariant S-matrix proof.

**NEXT:** localized finite-energy on-shell wave packets preserving phase matching within finite bandwidth, controlled full-sigma/EM energy transfer and perturbative backreaction, and detailed metric variation of curvature coupling with Ward/Bianchi conservation. Seek an independent **quarter-grid** parameter/carrier selector that survives v15.1387's exact radius reparametrization; absent such a selector, both on-shell and off-shell examples are ordinary freely chosen extended EFT effects, not new Cone-specific physics.
