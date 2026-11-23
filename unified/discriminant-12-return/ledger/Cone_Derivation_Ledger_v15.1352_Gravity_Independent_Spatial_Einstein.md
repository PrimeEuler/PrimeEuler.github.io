# Cone Derivation Ledger v15.1352 — Independent 4D Christoffel/Ricci reconstruction verifies all six spatial Einstein equations of complete weak-field Maxwell–K4 metric

**Date:** 2026-11-23 Eastern. **Lane:** Gravity/Cone. **Preledger HEAD:** d8175ba90a6a1299cdf1617b98db633daf3690bb. **Status:** [NUMERIC PASS, linearized/scoped] independent all-six spatial Einstein tensor from the assembled complete real 4-metric using spatial FFT and five separate full metric time slices, compared against independently computed physical Maxwell 3×3 tensor and independently varied frozen K4 material stress; [PASS] time-step halving ratio ~4 on 12³ and 24³; [NEGATIVE] deleting either Maxwell or K4 stress causes order-of-magnitude larger residuals; [OPEN] exact GitHub committed-byte Audit replay, nonlinear Einstein equations, continuum convergence, causal optical readout, Cone-only/quarter-grid action. **Strict additive:** previous Gravity/Audit/Sandbox/Suzuki untouched. Audit Round 628 canonical v15.1350 independently replayed previous v15.1349 real-space ADM Hamiltonian; v15.1351 independent ADM momentum is awaiting its own Audit.

## Gate 1271 — compute spatial Einstein tensor without mode ODE accelerations

The common-source assembled four-metric from v15.1347/1349/1351 is `g00=−1−2Phi`, `g0i=−aB_i`, `gij=a²(δij+sij)`, with s containing scalar spatial potential, homogeneous u and diagonal Bianchi beta, and **physically signed positive-source TT h**, all with identical 2N-dealiased compact vacuum Maxwell history. Work on the coasting background `a=tau/sqrt3` and weak field electric amplitude `A=.1`.

To reconstruct a **genuine independent geometric spatial Einstein tensor**, generate five complete metric solutions separately from initial tau=1 to endpoints `tau−2dt,tau−dt,tau,tau+dt,tau+2dt` (not a time derivative copied from a mode equation). First form `h_mu_nu=g_mu_nu−g0_mu_nu`; derive all first-order metric connection perturbations

`delta Gamma^alpha_munu = (1/2) g0^(alpha beta) (partial_mu h_beta nu + partial_nu h_beta mu − partial_beta h_mu nu) − (1/2) g0^(alpha gamma) h_gamma delta g0^(delta beta) (partial_mu g0_beta nu + partial_nu g0_beta mu − partial_beta g0_mu nu)`.

The background connections are `Gamma0_ij=a adot δij`, `Gammai_0j=Gammai_j0=δij/tau`; all spatial perturbation derivatives are Fourier FFT derivatives of reconstructed **real-space** metric. Time derivatives of perturbations use centered differences, then time derivatives of the computed **connection** use centered differences from the independent neighboring connection solutions. This uses five metric slices, not the K4 P/f/h second derivatives.

Independently compute all `delta R_mu nu = partial_alpha deltaGamma^alpha_munu − partial_nu deltaGamma^alpha_mu alpha + deltaGamma Gamma0 + Gamma0 deltaGamma − deltaGamma Gamma0 − Gamma0 deltaGamma`, scalar trace `delta R=−delta R00 + delta Rii/a² −2 tr(s)/tau²`, and **mixed spatial** Einstein perturbation

`delta G^i_j = delta R_ij/a² − 2s_ij/tau² − (1/2)δij delta R`.

The perturbative background mixed-index inverse metric contribution `−2 s_ij/tau²` is essential. The resultant spatial Einstein tensor is symmetric to ~1e−15.

## Gate 1272 — independently constructed Maxwell and material full stress tensor

Reconstruct Maxwell independently **again** from original E0 rather than the metric solver's SVT stress projections: transverse Gauss clean E0 and zero Nyquist, analytically propagate conformal Ehat and Bhat to tau, reconstruct both fields on doubled 2N³ spatial mesh, form `Tij_conf=rho δij−EiEj−BiBj`, FFT the full tensor on doubled mesh, project interior signed N-grid modes, discard Nyquist and transform back to physical 3D real field. Physical Maxwell spatial mixed stress is `9Tij_conf/tau⁴` in this normalization, preserving the true k0 anisotropy.

For the **frozen original degree-one material** `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, `eta_s=3/4,kappa C=1`, define `sij=gij/a²−δij` and solid label displacement `xi_i=partial_i P−f_i` (the vector-minus convention previously Audited). The linear material matrix strain `Dij=−sij+partial_i xi_j+partial_j xi_i`. Independent direct first variation of the original material stresses gives

`delta T^i_j(K4)=[Dij−(2/3)δij tr D]/tau²`.

This formula reproduces the individually verified scalar pressures, v15.1318 transverse vector offdiagonal stress `−ik f/tau²`, and the physical TT solid stress `−h/tau²`; the homogeneous Bianchi shear and scalar u contribution are also included via sij. **Do not** replace the stress by `delta G` or otherwise force agreement.

Compare all nine spatial matrix slots (six independent) pointwise:
`Cij=delta G^i_j−9Tij_conf/tau⁴−[Dij−(2/3)δij tr D]/tau²`.

The independent spatial *trace* and all off-diagonal components are included. The calculation is first-order in metric/Matter perturbations; it is not the exact nonlinear Einstein tensor.

## Gate 1273 — executed numerical results and debug-negative record

The actual local standalone Python/SciPy/NumPy implementation `/mnt/data/cone_gate/k4_independent_spatial_standalone_v15_1352.py` imported the previously executed assembled full-metric core and independently rebuilt Maxwell's complete physical stress tensor. At t=1.08, A=.1, nt=13, the following results were **actually executed**:

| Grid | centered half-step dt | max |Gsp| | max |Tsp| | max |Gsp−Tsp| | relative residual |
|---|---:|---:|---:|---:|---:|
| 12³ | .006 | .002904639363986469 | .002904866940026469 | 1.197076780815683e−6 | 4.120934987833813e−4 |
| 12³ | .003 | .002904809672120744 | .002904866940026469 | 2.994535281284011e−7 | 1.030868312769164e−4 |
| 16³ | .004 | .008029951740886523 | .008030394029655273 | 2.614111382949480e−6 | 3.255271625895172e−4 |
| 24³ | .003 | .048087516488181980 | .048090768773670710 | 7.487991652385673e−6 | 1.557053846992208e−4 |
| 24³ | .0015 | .048089914602538864 | .048090768773670710 | 1.900131233807667e−6 | 3.951135076983783e−5 |

At N12, dt-halving ratio ≈3.998; N24 ≈3.941, the expected second-order time-difference reduction. Matrix antisymmetry in the final spatial Einstein difference is <=3.4e−15 on the fine N24 run. The **trace residual** itself is nontrivially tested: max |tr C| decreases N12 .006→.003 from 3.5054e−6 to 8.7699e−7 and N24 .003→.0015 from 1.8775e−5 to 4.7012e−6. These are geometric numerical checks, not tautological input mode equations. N12/16 poorly resolve the original compact packet; no spatial continuum certification.

**Negative controls:** at N12/dt=.006, omit solid stress: max residual .000305438197, about 255× the actual residual. Omit Maxwell: .00264288284, about 2208×. At N24/dt=.0015, no-solid residual .00278838054, ~1467×; no-Maxwell .0459512351, ~24184×. Both are load-bearing sources.

**Debugging history required to preserve:** an initial direct-geometry implementation failed badly (spatial residual relative ~1.35), because indices of the *time-derivative metric tensor* were incorrectly accessed as if it were a four-dimensional derivative array; this produced unsymmetric first-order Christoffels/Ricci. After correcting that bug the residual improved to ~.0036 relative but a persistent antisymmetric spatial error ~1.6e−5 remained: the independently reconstructed k0 Maxwell pressure tensor was incorrectly filled with a diagonal-vector **broadcast**, rather than a diagonal matrix. Replacing this with the correct full k0 Maxwell tensor removed that second error. The final standalone reproducer **independently rebuilds the physical Maxwell 3×3 stress on 2N³**, thereby avoiding the k0 broadcast trap entirely. The failure/correction sequence is retained here; only the fixed program yields the PASS. No previous certified ledger asset was modified.

## Gate 1274 — provenance and Audit next step

A new additive canonical GitHub reproducer `research-notes/k4_independent_spatial_einstein_v15_1352.py` committed at SHA **d8175ba90a6a1299cdf1617b98db633daf3690bb** independently re-implements the **same tested algorithm** in a standalone script that imports the canonical v15.1351 metric-core source from the same `research-notes/` directory. The local numerical program imported the locally executed v15.1351 core. **The exact newly committed GitHub bytes have not been independently replayed**, so the authoritative numerical table is from the actually executed local script, with explicit external Audit replay necessary before claiming byte-for-byte reproducibility. GitHub script incorporates dt-halving assertions at N12 and N24, separate Maxwell/solid omission assertions, and connection lower-index symmetry assertion. No original files changed.

**AUDIT HANDOFF (priority):** independently execute GitHub v15.1351 first (3-momentum) and v15.1352 new spatial script, independently derive full physical mixed stress `delta T^i_j(K4)=(Dij−2δij trD/3)/tau²` by varying original F(B), check 4D connection and scalar mixed-index term, k0 Maxwell pressure (do not broadcast diagonal components), dt-halving, spatial trace and all 3 offdiag components, and the exact GitHub import of the parent script. If a difference or import failure appears, report as a new correction and preserve existing files. **Then** perform a higher-N/time-refinement and compare geometrically computed Hamiltonian/momentum/spatial Einstein residuals in a single run. The numerical pass now covers all ten independent *linearized* Einstein field equations when combined with v15.1349 ADM Hamiltonian and v15.1351 three ADM momenta, but those previous scripts use the ADM normal-normal and mixed momentum combinations rather than necessarily the exact same mixed-index contraction as this new spatial script. A fully common explicit 4D `delta G^mu_nu` tester is a worthwhile separate redundancy check.

**Physical novelty boundary:** independently verified Maxwell–Einstein–ordinary frozen K4 material *within the linearized weak-field domain*; Einstein+identical K4 comparator must be identical. No action-derived physical quarter-grid Casimir coupling, Newton-G-free number, SI calibrated prediction or causal photon/mirror/clock readout has emerged. Do not announce new gravitational physics from these residuals.
