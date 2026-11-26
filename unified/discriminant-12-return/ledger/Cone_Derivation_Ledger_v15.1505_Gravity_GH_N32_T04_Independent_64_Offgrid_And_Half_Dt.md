# Cone Derivation Ledger v15.1505 — Unrestricted 32³ Einstein–H² generalized-harmonic evolution independently passes 64³ off-grid constraints and checkpointed RK4 timestep refinement through T=.04

**Date:** 2026-11-25 America/New_York (local night; repository UTC commits may show 2026-11-26). **Lane:** Gravity/Cone. **Status:** [LOCALLY EXECUTED NUMERICAL PASS] the two outstanding checks from Gravity v15.1496 now both COMPLETE: (i) independently recompute all four harmonic-gauge and all four physical ADM Einstein Hamiltonian/momentum constraints for the same fully evolved 32³ state at T=.04 after Fourier interpolation of the **entire state** to 64³, not interpolation of residual arrays; (ii) complete half-timestep RK4 dt=.002 through T=.04 in two checkpointed 10-step segments and compare against the earlier dt=.004 run. **Critical scope:** native-vs-offgrid consistency and temporal error-floor diagnosis *at N32, T=.04*, not a proof of arbitrary long-time nonlinear stability, fully coupled electromagnetism, or a new G-free gravitational observable. All 10 metric components and both curved-H² sigma fields evolve without wave/homogeneity ansatz. κ=.003 remains prescribed. Independent exact-committed-byte Audit pending.

## Status of handoffs and version space

At gate initiation, latest live HEAD was **bd2d40136ac0db8673e61ddeb7ad6aa418a8712e** (Suzuki Lane A v15.1504). Audit Round 654 (commit 303317fc1385a2f9332a390973b45dbcb7fd8718) confirmed Lane A v15.1498–1501; earlier Audit Round 652 (commit 5ad0195785c1189de58ede1d1cff1acc4ab2af83) independently confirmed Gravity v15.1491 and v15.1493. Gravity v15.1495 and v15.1496 still pending independent Audit. This gate uses **v15.1505**, avoiding all concurrent Lane A and Audit numbers. Do not modify earlier ledger, Audit, Sandbox or Suzuki files. The Sandbox v15.1485 census had already closed a naive V=1/16→EM area coupling selector; it is not reintroduced.

## Gate 1422 — independent FULL 64³ ADM curvature and GH off-grid evaluation

Evolve the exact same unrestricted 3D generalized-harmonic Einstein–H² system as v15.1496, from independent nonlinear ADM/H² constraint-solving initial state at N=32³ with harmonic gauge-compatible lapse/shift time derivatives, RK4 dt=.004 for ten steps to T=.04. Full 4D gμν, ∂t gμν, φA, ∂tφA are freely evolved on the N32 periodic Fourier grid. Numerical performance uses environment \`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1\`, not altered physics. Re-check native H/M/GH and timelike g^tt.

Interpolate **all evolved state arrays** to N64 in three dimensions with \`scipy.signal.resample\` (proper Fourier mode normalization), then **independently reconstruct**:

1. all four GH gauge residuals using the metric *inverse-divergence* identity with 4D metric spatial/time first derivatives, rather than replaying full expensive Christoffel-and-reduced-Ricci RHS:
\[
C^\mu=g^{\mu\alpha}g^{\nu\beta}\partial_\nu g_{\alpha\beta}-\tfrac12 g^{\mu\nu}g^{\alpha\beta}\partial_\nu g_{\alpha\beta},
\]
which equals contracted Christoffel \(\Gamma^\mu\). The standalone monitor evaluates this from \`inv\`, \`p=∂tg\` and spectral \`grad(g)\` on 64³, not from interpolation of the native \`C\) field.

2. Physical Einstein scalar Hamiltonian and all three momentum constraints using the **separate complete 3D ADM** \`adm_checks\`: construct g_ij, lapse/shift, 3D Christoffels and Ricci, extrinsic curvature, sigma target kinetic/spatial stress, spatial covariant derivatives of K. No pure-conformal assumption imposed on the evolved metric.

**Actually executed local program:** \`/mnt/data/cone_gh/gate1497_offgrid_fast.py\`, importing \`/mnt/data/cone_gh/gh3d.py\` (whose numerical implementation has been Audit-confirmed via repaired committed v15.1485 equivalent). The 64³ GH+ADM monitor completed **in about 3 seconds after the N32 evolution's ~24 seconds**, avoiding the prior >160-second timeout caused by computing the *full 64³ GH nonlinear evolution RHS* merely to measure its 4 GH residuals. The full RHS is unnecessary for the independent gauge calculation; this is a performance optimization of the monitor, not an approximation to the constraint itself.

| T=.04 constraint | Native evolved N32³ | Same evolved state recomputed on 64³ |
|---|---:|---:|
| max |C^μ| GH gauge | **1.7127834828873593e−12** | **1.7152546557711945e−12** |
| max |Hamiltonian| | **1.2621636521310473e−10** | **1.1160106790520513e−10** |
| max |Momentum| | **4.1794216010119026e−11** | **4.182240341668369e−11** |
| max inverse g^tt | −0.9987381424513845 | −0.9987381424513838 |

Thus the off-grid Hamiltonian at N32 is **~0.884** of its native maximum (not a 3.9× increase as at N24 in v15.1495), and the other two constraints remain almost unchanged under finer evaluation. This is meaningful **resolution evidence for this particular evolved initial data**, but not a theorem on continuum convergence, nonlinear geometric constraint stability for arbitrary data, or order in spatial grid size. The comparison is of *a bandlimited interpolated evolved metric*, not of independently solved N64 initial data.

## Gate 1423 — checkpointed half-timestep RK4 verification of N32 T=.04

The initial one-shot isolated 32³ dt=.002 run repeatedly exceeded the execution limit and returned no final row, even though the dt=.004 run required only ~25 sec. To isolate and avoid repeated wall-clock interruptions, split *the same RK4 algorithm* into two uninterrupted segments of 10 steps each with dt=.002: (i) T=0→.02, save all four state arrays (\`g,p,phi,Pi\`) losslessly in NumPy compressed NPZ; (ii) reload the arrays, continue T=.02→.04 for ten more steps. There is **no reset/projection** of constraints or fields at the checkpoint.

**Actually executed checkpoint 1:** \`/mnt/data/cone_gh/checkpoint32_halfdt_t002.npz\`; at T=.02 GH=7.18408839361917e−13, H=1.4557309741328184e−10, M=2.1968172418706296e−11. **Actually executed checkpoint 2:** \`/mnt/data/cone_gh/checkpoint32_halfdt_t004.npz\`; at T=.04 GH=1.7080682588400996e−12, H=1.2635389387343973e−10, M=4.1813711008724906e−11; max inverse g^tt=−0.9987381424513847. All runs completed, evolved 10+10 RK4 substeps with no elliptic re-solve.

| T=.04 residual | RK4 dt=.004 | RK4 dt=.002 checkpointed |
|---|---:|---:|
| GH max | 1.7127834828873593e−12 | 1.7080682588400996e−12 |
| Einstein Hamiltonian max | 1.2621636521310473e−10 | 1.2635389387343973e−10 |
| Einstein momentum max | 4.1794216010119026e−11 | 4.1813711008724906e−11 |

Absolute changes: GH≈4.72e−15, H≈1.38e−13, M≈1.95e−14. This supports **spatial/constraint-representation error dominating temporal truncation** at N32 T=.04. It does **not** demonstrate an RK4 error-reduction order at this particular T, because the constraint residual is at an initial/spatial floor and two timesteps alone cannot estimate an asymptotic temporal rate. The independent homogeneous exact harmonic-time FLRW RK4 fourth-order convergence (v15.1482) remains the direct time-order test.

## Reproducibility and Audit handoff

Additive canonical standalone replayer \`research-notes/k4_gh3d_offgrid_timestep_v15_1505.py\`, commit **b4ed2a6679d9c81b328187b41426a7277a663d4f**, imports canonical Audit-repaired unrestricted v15.1485 solver. It offers three documented separate invocations with the same checkpoint path: \`offgrid\`, \`first\`, and \`second\`. These are equivalent to the locally executed fast off-grid monitor and two-segment half-dt run. **Committed exact bytes have not yet been independently executed by Audit**. The algorithm is directly verified by the preceding local outputs; code provenance and independent replay remain separate confidence levels.

**AUDIT:** hand-derive the independent inverse-divergence expression for C^\mu, confirm the 64³ monitor computes full 3D ADM Ricci/extrinsic K and material stress on the interpolated evolved state, replay all three committed commands, and verify checkpoint I/O preserves all 24 evolved field arrays and exact RK4 time continuity. Compare all table digits and full Lorentzian signature; compute the true 4 GH subsidiary wave-constraint time derivatives if feasible. Report any deviations without silently patching.

**NEXT:** extend N32 to T=.08 and N40 to T=.04 using checkpointed solver with equal-resolution independent off-grid monitors and compare constraint growth; add robust energy or subsidiary constraint monitors to catch growing gauge violations. Only then turn to nonzero target-area \(B_{\mu\nu}\), complete Weyl–F–B metric variation/derivative order reduction, and dimensionless tidal/EM response without a chosen susceptibility. Do not insert \(\kappa\) or \(\zeta\) from the quarter-grid as a supposedly derived quantity.
