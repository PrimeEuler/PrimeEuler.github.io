# Cone Derivation Ledger v15.1314 — Evolved k>0 scalar Einstein Hamiltonian and longitudinal momentum constraints from conserved Maxwell+K4 solid

**Date:** 2026-11-22 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact time-dependent scalar k>0 constraint identities from v15.729 Bardeen potentials, v15.1262 sourced P dynamics, v15.1276 independently reconstructed metric Einstein operator, full Maxwell Ward, and the physical original K4 determinant solid stress; [N PASS] 4-grid dealiased Maxwell source, nonzero-source time evolution and all retained modes at 17 slices tau=1..1.08, with distinct no-solid negative controls; [OPEN] independent external committed-byte replay, nonzero spatial trace/shear, transverse vector/tensor field equations, complete metric, optical null-ray/mirror/clock detector, continuum accuracy, Cone-only interaction. **Immediately prewrite live HEAD:** a2fd523d7de9fe8fab8bd8d641766b8caa653572. Earlier audit Round 623 (SHA c7b03fcf9ba7894450b4fc2de798809e3ad7868b, canonical v15.1298) independently replayed and passed Gravity v15.1275–1277, but found **three version collisions**: Audit already used v15.1275–1277 earlier on 2026-11-21. This entry therefore uses the independently checked absent **v15.1314** slot, not 1278/1299/etc. Audit liveness occupies v15.1299–1313. No modification to historical colliding files, K4 parents, Suzuki, Sandbox/Muse or Audit.

## Gate 1237 — independently recover the material source terms before imposing constraints

For a first-order scalar Newtonian-gauge FLRW metric `ds²=-(1+2Phi_N)dτ²+a²(1-2Psi_N)δij dxidxj`, `a=τ/sqrt3`, and comoving K4 material fields `phi^I=x^I+∂^I P`, expand the original frozen degree-one solid Lagrangian `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²-1/3)]`, `B^IJ=g^μν ∂μ phi^I ∂ν phi^J`. The anisotropy correction begins at quadratic order in scalar strain around isotropy, so the linear energy variation follows from the determinant alone:

`delta rho_s=(C/a²)(2Psi_N+(2/3)∇²P)=(6Psi_N-2k²P)/τ²` at `κC=1`.
Thus `delta T^0_0,solid=-6Psi_N/τ²+2k²P/τ²`.

A first-order fluid/material velocity constrained by `u^μ ∂_μ phi^I=0` gives `u_i=-a² ∂_i Pdot`; the frozen solid's isotropic `rho_s+p_s=2C/(3a²)` gives `delta T^0_i,solid=-(2C/3)∂_i Pdot=-2ik_i Pdot/3` in model convention. These solid source formulas were cross-checked by a separate SymPy first-order determinant expansion and normalization algebra. They are not defined by taking the difference of the Einstein tensor and Maxwell stress.

The Maxwell source follows v15.1274: original v15.1078 compact E0, transverse projection, common Nyquist-zero, exact conformal Maxwell evolution, 2N³ padded real reconstruction, **all quadratic source products on 2N³**, and projection to the original N³ strictly interior non-Nyquist Fourier modes. This identical source supplies `r=rho_conf,k`, `F_parallel`, `T_nn`, and analytic time derivatives on all slices, with `rdot + i sqrt3 k F_parallel/τ=0` to roundoff.

## Gate 1238 — exact time-dependent Einstein 00 and longitudinal momentum identities

Apply v15.729 pressure-corrected source-first Bardeen formulas to the same physical Maxwell history and the evolving sourced K4 longitudinal displacement `P`, whose equation at eta_s=3/4 is

`Pdd+3Pdot/τ+(k²+2)P/τ²=9(3Tnn-r)/(2k² τ⁴)`.

With `J_Phi=J_psi=-sqrt3 r/τ`, `J_B=-i sqrt3 k F_parallel/τ`, `J_Bdot=(-3k²Tnn+i sqrt3 k F_parallel)/τ²`, and the Maxwell continuity/pressure Ward identity, explicit differentiation of `Psi_N` yields the simplification

`Q := τ Psidot_N+Phi_N = τ Pdot/3 + 3 sqrt3 i F_parallel/(2k τ²)`.

Use independently derived metric operators v15.1276:
`delta G^0_0=6(k²Psi_N+Q)/τ²`, `delta G^0_parallel=-2ik Q/τ`.

Substitution produces exact identities for all k>0:

`delta G^0_0 = -9r/τ⁴ -6Psi_N/τ² + 2k²P/τ²`,
`delta G^0_parallel = 3sqrt3 F_parallel/τ³ -2ik Pdot/3`.

RHS terms are precisely the first-order Maxwell plus determinant-solid energy and material momentum stress in the fixed metric convention. The two independent geometrical constraint expressions and separate solid variation make this a stronger sourced test than v15.1277, which used only tau=1 and F=P=Pdot=0. **However**, the identities are consequences of the already assumed sourced K4 mode equation and Maxwell Ward; they do not independently establish that all time-dependent Einstein spatial equations, gauge constraints or causal initial-value evolution close.

## Gate 1239 — actual numerical four-grid test and negative controls

The new local Python/NumPy/SciPy program evolves P and Pdot with RK4 using cubic-spline time interpolation of the **dealiased Maxwell quadratic stress** on 17 common time samples tau in [1,1.08]. It evaluates the full source at each output time, differentiating its Maxwell propagation analytically (no finite-difference approximations for rdot or Fdot). The scalar metric `Phi_N`, `Psi_N` and `Psi_Ndot` are built from the archived source-first formulas. Report the maximum absolute complex Fourier residual over **every retained nonzero interior mode and time**:

| N³ | max |C00| | max |C0parallel| | max Maxwell energy Ward | max |C00| without solid | max |C0parallel| without solid |
| --- | ---: | ---: | ---: | ---: | ---: |
| 12³ | 4.6046628366e-18 | 8.0654177360e-19 | 9.5392160654e-20 | 0.00170775517 | 0.00019927476 |
| 16³ | 7.4363259653e-18 | 1.3479759547e-18 | 2.7139831202e-19 | 0.00317194519 | 0.00022028972 |
| 24³ | 2.6457399164e-17 | 4.8793633266e-18 | 1.3023445704e-18 | 0.00735393878 | 0.00072148707 |
| 32³ | 2.4146640898e-17 | 4.1327740875e-18 | 1.7347237020e-18 | 0.00690533148 | 0.00066055426 |

The initial `P=Pdot=0` and Maxwell `F=0`; at tau>1, nonzero flux and evolved solid `Pdot` give a **nonzero** 0i equation on both sides. For N=24 the maximal magnitude of `P(tau=1.08)` is `1.0206025393452533e-4` and `Pdot` is `2.164461201399428e-3`, so the evolved solid material terms are genuinely active.

Temporal sensitivity at N=24, with 9/17/33 source samples, yields max no-solid Hamiltonian 0.00735143184 / 0.00735393878 / 0.00735432476. This demonstrates that the *dynamical response amplitude* changes with temporal quadrature; the constraint identities remain small even when P is only numerically approximated, because the same computed P/Pdot/acceleration is substituted on both sides. Do **not** claim convergence, physical prediction or independent spacetime closure from tiny constraint residuals alone. Low N field magnitudes vary substantially across spatial meshes; no physical accuracy certification.

**Execution provenance:** Python script `/mnt/data/cone_gate/k4_evolved_scalar_constraints_v15_1314.py` actually executed with 4 grids and 9/17/33 temporal sensitivity test. New additive canonical GitHub script `research-notes/k4_evolved_scalar_constraints_v15_1314.py` commit a2fd523d7de9fe8fab8bd8d641766b8caa653572 implements the same mathematical test; its **exact uploaded bytes still await independent Audit replay**. Historical parent files untouched.

## Gate 1240 — next noncircular closure check

The **priority** is the spatial Einstein equations computed from the *same full metric* and an independently varied **full K4 solid stress**, including linear anisotropic elasticity, trace pressure and displacement-gradient stress, plus actual Maxwell anisotropic stress in the same projection. Check spatial trace and longitudinal/transverse shear at tau>1 **without using those equations to define the residual by construction**. Next restore transverse K4 vector shift/velocity and TT tensor metric, compare their mixed Einstein components and off-diagonal stress, and then the complete position/time-dependent metric plus all ADM constraints. Finally a finite-baseline causal optical clock/mirror/null-ray response against the identical-action Einstein–Maxwell+K4 comparator can be constructed.

**Audit handoff:** (1) independently replay exact committed script; (2) verify tau derivative signs of `J_Bdot`, Maxwell Ward, and sign of mixed `T^0_i` for the (-+++) convention; (3) independently vary the determinant-and-anisotropy K4 solid to confirm `delta T^0_0` and `delta T^0_i` without using `delta G`; (4) check spatial Einstein trace and shear and temporal refinement; (5) preserve existing collided v15.1275–1277 audit records.

**Scientific boundary:** this remains ordinary Einstein–Maxwell plus the specified K4 solid, not an independent gravitational interaction arising from the quarter-grid arithmetic/Casimir construction, and no dimensionless G-free experimental prediction has emerged.
