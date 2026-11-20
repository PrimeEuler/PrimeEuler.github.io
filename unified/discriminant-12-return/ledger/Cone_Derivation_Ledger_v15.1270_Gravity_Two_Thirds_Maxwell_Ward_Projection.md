# Cone Derivation Ledger v15.1270 — Native-grid two-thirds projected Maxwell Ward gate

**Date:** 2026-11-20 Eastern. **Lane:** Gravity/Cone. **Status:** [D] strict componentwise |integer Fourier index|<N/3 projection of the v15.1267 transverse Nyquist-clean initial E field makes the **retained-band Fourier projection** of Maxwell local continuity and v15.729 K4 scalar Ward accurate to roundoff on the native N³ grid; [NEGATIVE] the full unprojected stress field on that same N³ product grid still fails its higher-band Ward/continuity checks; [O] consistent dealiased full Einstein–K4 metric and constraints; [N] no Cone-specific physical interaction. **Immediately prewrite HEAD:** 1430f3d53eb5f8bba7ce03f39db166d4b61a7e96. No overwrite; all certified v15.1262–1269, Audit, Suzuki, Sandbox/Muse untouched.

## Gate 1217 — computationally lighter consistent source-band option

The prior v15.1269 test restored Maxwell energy continuity and K4 scalar Ward by evaluating the full unchanged finite Fourier field's quadratic products on twice the mesh size in each dimension. Here instead choose a separate, explicitly **bandlimited** discretized source: after discrete transverse projection and common Nyquist removal, set all initial E Fourier coefficients to zero whenever any integer Cartesian FFT index has |m_j|>=N/3. Evolve Maxwell exactly as before. Evaluate quadratic stress on the original N³ grid, Fourier-transform its rho and F fields, and test **only the same retained band** |m_j|<N/3. The usual 2/3-rule protects this retained band from aliases of two retained modes on the N³ product grid. Do not assert the unretained bands are conserved, and do not claim this bandlimited source is numerically identical to the original v15.1267 full-band source.

Test uses exact analytic Maxwell time derivatives at tau=1.08 (not finite differences), identical v15.1269 scalar source mapping `Jphi=Jpsi=-sqrt(3)rho/tau`, `JB=-sqrt(3)divF/tau`. Direct local Python/NumPy execution gives:

| N³ | native-grid full-band scalar Ward error | native-grid **retained-band** scalar Ward error | retained-band continuity error |
|---|---:|---:|---:|
| 16³ | 8.2954864308e-4 | 2.4909744568e-19 | 1.3636050240e-19 |
| 24³ | 3.7475475964e-3 | 9.9272561768e-19 | 5.7888992021e-19 |
| 32³ | 5.6107141173e-3 | 1.5277206983e-18 | 6.8495597107e-19 |
| 40³ | 3.7890872082e-3 | 2.4665800728e-18 | 1.73491559996e-18 |
| 48³ | 1.08867991397e-4 | 2.8380094168e-18 | 1.3315103671e-18 |

Thus two defensible **different** numerical schemes exist: (A) maintain the full v15.1267 field bandwidth and 2N product grid, with corresponding resolved stress; (B) reduce source field bandwidth and evaluate/project gravitational stress strictly within the conserved 2/3 band at native N grid. They are not interchangeable pointwise at fixed N. In B the stress's high Fourier components after nonlinear multiplication must be discarded for the gravitational solver. The homogeneous mean must also be recomputed from precisely the same bandlimited initial E to avoid reintroducing the v15.1266 weld inconsistency.

**Reproducer:** `research-notes/k4_maxwell_two_thirds_ward_projection_v15_1270.py`, SHA `1430f3d53eb5f8bba7ce03f39db166d4b61a7e96`. This is a new additive Python file derived from the self-contained v15.1269 Maxwell source check. Exact uploaded byte-form still awaits independent clean-checkout replay; quoted numbers are from a separate equivalent local script actually executed.

**Next execution order:** choose and declare the scheme across the entire sourced K4 scalar/vector/tensor/Hamiltonian background calculation, and replay full local tidal trace and projected energy Ward concurrently. Expose time-series lapse, scalar spatial potential, vector shift and tensor spatial fields under the same source projection. Independently calculate all ADM Hamiltonian/momentum/spatial Einstein+solid residuals; the source Ward test is necessary but insufficient. Only with full constraints and common metric is a causal finite-baseline photon–mirror–clock test physically justified.

**Audit request:** independently check strict 2/3 projector behavior, spectral conjugacy, boundary at the cutoff, selection of post-product retained band, and why high-band residuals need not vanish; compare A/B at increasing spatial resolution. Preserve original unfiltered source's interpretation and do not claim quarter-grid gravitational novelty.
