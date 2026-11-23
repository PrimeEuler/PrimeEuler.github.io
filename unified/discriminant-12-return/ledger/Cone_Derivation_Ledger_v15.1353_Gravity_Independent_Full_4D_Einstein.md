# Cone Derivation Ledger v15.1353 — One common independent 4D Einstein tensor: all ten linearized field equations

**Date:** 2026-11-23 Eastern. **Lane:** Gravity/Cone. **Status:** [N PASS scoped] an independently reconstructed complete 4D first-order Einstein tensor from five separately assembled numerical real-space four-metric histories is now compared in the same geometric computation to all Maxwell+frozen K4 matter components (00, 0i, ij) at one common epoch; [PASS] 12³ and 24³ centered-dt halving, two separately load-bearing matter omissions in each geometric sector; [OPEN] exact newly committed code replay by External Audit, spatial continuum convergence, nonlinear Einstein evolution, metric-coupled Maxwell correction, causal photon/mirror/clock observable, any distinct physical quarter-grid coupling. **Immediately preledger inspected HEAD:** bfff143eed1b9ed8fbab08cecb65140aa17d6d1f. Ledger path checked absent. Strictly additive: certified earlier Gravity, external Audit, Suzuki, Muse/Sandbox untouched.

## Gate 1275 — same geometry for all ten Einstein components

Previously independent Audited v15.1349 reconstructed the real-space ADM Hamiltonian, and Gravity v15.1351 reconstructed three ADM momenta, while v15.1352 calculated the six spatial mixed components from direct 4D curvature. Their respective geometric methods and normalization conventions had not previously been tested in **one** consistent 4D calculation. This gate extends the v15.1352 five-slice *full Ricci* implementation to all 4D components, so that there is **one common** Christoffel/Ricci tensor and Ricci scalar, computed from the complete first-order four-metric with physical-sign TT strain, nonzero scalar/vector components and k=0 Bianchi response. The same original v15.1078 compact Maxwell stream field, A=.1, conformal Maxwell E/B, and 2N-dealiased quadratic source is used on tau=1.08.

Compute a time-centered perturbation `h_mu nu=g_mu nu−g0_mu nu` at independent times tau−2dt,−dt,0,+dt,+2dt; FFT all spatial derivatives; use centered time differences of perturbations to form `delta Gamma^alpha_mu nu` on three slices and centered differences of these independently computed connections to form `partial_tau delta Gamma`. Assemble the full first-order Ricci `delta R_mu nu`, including its background-connection cross terms, and scalar `delta R=−delta R00+delta Rii/a²−2 tr(s)/tau²`. The background coasting FLRW Ricci tensor is `R00^(0)=0`, `Rij^(0)=2/3 deltaij` for a=tau/sqrt3. Then, with the complete mixed-index inverse-metric correction, obtain

`delta G^0_0=−delta R00−delta R/2`,

`delta G^0_i=−delta R0i+2h0i/tau²`,

`delta G^i_j=delta Rij/a²−2sij/tau²−delta^i_j delta R/2`.

These equations were not reconstructed separately in S/V/T from K4 mode equations: they follow the **one** numerical 4D Christoffel geometry across the full real-space metric.

## Gate 1276 — independently varied full matter 00 / 0i / ij

The Maxwell mixed stress tensor is obtained from the same dealiased physical E/B Maxwell field, with conformal `rho=(E²+B²)/2`, flux `F=E×B`, and `Tij=rho δij−EiEj−BiBj`, all projected onto the allowed N Fourier modes including the physical k0 energy/pressure. At tau,

`delta T^0_0(EM)=−9rho/tau⁴`,
`delta T^0_i(EM)=3sqrt3 Fi/tau³`,
`delta T^i_j(EM)=9Tij/tau⁴`.

The original unmodified K4 relativistic solid `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, eta_s=3/4, kappa C=1, with scalar material coordinate shift `+grad P` and transverse vector material shift `−f_i`, contributes

`delta rho_s=(−6u+6Psi−2k²P)/tau²`,
`delta T^0_i(solid)=−(2/3)∂i Pdot +(2/3)(f_i,dot−B_i/a)`,
`delta T^i_j(solid)=[Dij−2 deltaij trD/3]/tau²`

with `Dij=−sij+∂i xi_j+∂j xi_i`, `xi_i=∂i P−f_i`. These are direct first-order material-energy/momentum/spatial constitutive relationships, **not** residual definitions derived by subtracting geometry. The source components are compared directly with the three numerical geometric Einstein sectors in **one** run.

## Gate 1277 — actually executed common-geometry numerical check

At t=1.08 and A=.1, four spatial grids/time-step combinations plus one additional step refinement were **actually executed**, with five independent metric trajectories per test. Numbers below are maximum absolute real-space component residuals:

| N³ | dt | max |C00| | max |C0i| | max |Cij| |
|---|---:|---:|---:|---:|
| 12³ | .006 | 3.4433862667926406e−7 | 9.230708523106225e−8 | 1.1970767808156826e−6 |
| 12³ | .003 | 8.616225346765906e−8 | 2.3075540170950347e−8 | 2.9945352812840113e−7 |
| 16³ | .004 | 1.4600901094051835e−6 | 2.678375896601691e−7 | 2.61411138294948e−6 |
| 24³ | .003 | 3.703515241757112e−6 | 1.628169232596136e−6 | 7.487991652385673e−6 |
| 24³ | .0015 | 9.26128346662343e−7 | 4.071697828460512e−7 | 1.900131233807667e−6 |

For N12 the relative residuals at the finer dt are approximately 3.84e−5 (00), 7.15e−5 (0i), and 1.03e−4 (ij); for N24 finer dt they are 2.27e−5, 2.97e−5, 3.95e−5. Each residual class decreases by ~4 under dt halving at both N12 and N24, as expected from centered time derivatives; a small departure from exactly 4 in the spatial N24 ratio is consistent with remaining subleading temporal errors. This is **temporal convergence of the independent geometry**, not a spatial continuum error bound.

The matter omissions are decisive. At N24/dt=.0015, for example, the 00 residual ~9.26e−7 jumps to ~.007242 when solid energy is omitted and ~.047940 when Maxwell is omitted; the 0i residual ~4.07e−7 jumps to ~.000361 without solid momentum and ~.013339 without Maxwell momentum; the spatial residual ~1.90e−6 jumps to ~.002788 without solid pressure and ~.045951 without Maxwell stress. The original Maxwell and K4 matter sectors are individually necessary in each geometrical equation. A pure vacuum consistency identity cannot produce the observed six independent omission controls.

**Execution provenance:** local standalone actually executed `/mnt/data/cone_gate/k4_independent_full_einstein_v15_1353.py`. It was built additively from the already executed local v15.1352 five-slice spatial Christoffel program with independent 00/0i geometric and stress comparisons, assertions on the three sectors, omission controls and dt² tests. The new GitHub source `research-notes/k4_independent_full_einstein_v15_1353.py`, commit **bfff143eed1b9ed8fbab08cecb65140aa17d6d1f**, reproduces the same 4D Ricci approach as an additive extension of the prior v15.1352 GitHub script. The precise uploaded GitHub bytes have **not yet been independently executed**; Audit must replay them, including their parent v15.1351 import, before labeling the new committed version independently certified.

## Gate 1278 — scope and next falsification

This is a genuine independent real-space **ten-component first-order Einstein reconstruction**, building on the separate Audited Hamiltonian, rather than merely verifying the original sector ODE accelerations against themselves. Nonetheless, the proof is limited to the **linearized** Einstein–Maxwell plus the identical frozen K4 relativistic solid at A=.1 for finite N; it does not test the exact nonlinear Einstein tensor, matter/Maxwell backreaction, physical cosmological background viability, or continuum accuracy. The original model remains an ordinary Einstein+specified-solid comparator, **not** a demonstration of new gravity from the arithmetic 1/4 grid.

**AUDIT PRIORITY:** replay GitHub v15.1351, v15.1352 and this v15.1353 source in sequence; verify true mixed-index correction in the full 4D geometry, Maxwell and original K4 solid normalization and sign, no spatial k0 pressure broadcast, exact time-derivative index ordering, all ten residuals and dt scaling, and independently re-derive the `+2 h0i/tau²` mixed `G^0_i` term from the FLRW background Ricci tensor. Check material amplitude scaling, and ensure neither the same mode accelerations nor an imposed on-shell identity were reused as the independently evaluated geometric side. If any error appears, report as an additive correction and preserve this record.

**Next:** spatial N32/40/48 refinement and a genuinely causal, gauge-controlled photon-emitter/free-mirror/clock finite-baseline null observation in this complete metric, with fully matched Einstein–Maxwell+identical-K4 null comparator. A nonzero Cone-specific residual requires a separate **action-derived** quarter-grid interaction beyond the ordinary K4 model. No such interaction or Newton-G-free dimensionless measured observable has yet been established.
