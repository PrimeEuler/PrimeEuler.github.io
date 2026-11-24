# Cone Derivation Ledger v15.1381 — Weyl tidal curvature interacts with hyperboloid area and EM

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [C] a specific generally covariant U(1)-gauge- and orientation-preserving target-isometry-invariant **tidal interaction** involving two new hyperboloid coordinates and electromagnetic field; [D/PASS] exact linear vacuum-TT-wave geometric test proves curvature-activated two-form need not be closed and therefore cannot generically be eliminated by the **simple electromagnetic-potential shift** that trivialized the v15.1380 minimal F·B mixing; [NEGATIVE] its EFT coefficient and excitation scale remain freely chosen, the frozen K4 Maxwell packet alone cannot excite an initially constant hyperboloid field, and related ordinary QED curvature-photon EFT operators have a long literature; [OPEN] full coupled Einstein–Maxwell–H² action, conservation/initial-value evolution, stability, physical detector and genuinely Cone-selected coupling. Strict additive, no historical objects rewritten.

## Gate 1289 — a gravity-dependent candidate, not a bare Casimir

Retain continuous internal target `H²_r:T²−X²−Y²=r²` with `r=1/4` as the *candidate* geometric q2 closed-refined sheet (hence Q=1/16, not an independently measured gravitational Casimir). The map `n(x)=r(sqrt(1+u²+v²),u,v)` gives the target-isometry-invariant normalized area pullback

`B_mu nu=[(partial_mu u)(partial_nu v)−(partial_nu u)(partial_mu v)]/sqrt(1+u²+v²)`.

The separate explicitly **chosen** higher-dimensional EFT interaction is

`L_tidal=−(zeta/(2 Lambda²)) C_mu nu rho sigma F^{mu nu} B^{rho sigma}`,

where `C_mu nu rho sigma` is the physical spacetime Weyl curvature (NOT the internal quarter Casimir), `F` is Maxwell field strength, `Lambda` is a new cutoff scale and `zeta` an independent dimensionless coupling. In four spacetime dimensions with u,v dimensionless, B and F have mass dimension 2, Weyl curvature has mass dimension 2, so the operator has mass dimension 6 and requires `1/Lambda²`. This is a legitimate action-level candidate, gauge invariant and covariant; orientation reversal of the internal H² area form changes its sign and is not a preserved symmetry unless the coefficient/spurion changes as well. Maxwell variation gives

`nabla_mu[F^{mu nu}+(zeta/Lambda²) C^{mu nu rho sigma} B_rho sigma]=J^nu`,

where curvature also changes under the new stress-energy variation, so a full coupled metric evolution **cannot** be obtained by inserting an external effective Maxwell current alone into the frozen Einstein metric.

Its induced Maxwell current is `J_quarter^nu=−(zeta/Lambda²)nabla_mu(C^{mu nu rho sigma} B_rho sigma)`, identically conserved by antisymmetry of the first pair under covariant double divergence, irrespective of Ricci/Weyl background. The action is zero if Weyl C=0 (strict conformally flat FLRW) or B=0 (the internal field is constant or explores only one independent target coordinate); it turns on when a physical tidal field meets a two-dimensional internal-area sweep. Even when a Maxwell packet generates nonzero Weyl through Einstein+K4, an unexcited uniform H² map gives **zero** new source, an honest negative selector.

## Gate 1290 — explicit on-shell gravitational wave test and field-redefinition distinction

Take the legitimate linear vacuum Minkowski TT plus gravitational wave `h_xx=h(t-z)`, `h_yy=−h(t-z)` with `h=epsilon cos(omega(t-z))`. The first-order Ricci tensor vanishes, so Weyl equals the first-order Riemann. Independently deriving its components gives

`C_0x0x=−h_tt/2,` `C_zx0x=+h_tt/2`.

Choose nonconstant internal sigma map `u=a sin(m t)`, `v=b sin(k x)`, whose area pullback has only `B_tx=u_t v_x/sqrt(1+u²+v²)`. Define `K_mu nu=C_mu nu rho sigma B^{rho sigma}`. The signature (-+++) implies `B^{0x}=−B_tx`, hence

`K_tx=h_tt B_tx,` `K_zx=−h_tt B_tx`.

Although `B=dC_internal` is exact on the contractible hyperboloid (v15.1380), the **Weyl-contracted** two-form K is **not generically closed**:

`(dK)_tzx = ∂t K_zx −∂z K_tx=−h_tt ∂t B_tx`.

The wave identity `(∂t+∂z)h_tt=0` is essential to the last equality. At leading order in internal amplitudes,

`(dK)_tzx=−epsilon a b k m² omega² sin(m t) cos(k x) cos(omega(t-z)) + O(a³b,ab³)`,

nonzero for generic t,x,z. Therefore the potential shift `A_new=A+const*C_internal` that can absorb the v15.1380 minimal F·B term **cannot generically absorb this curvature-dependent K** by the same simple local shift; a one-form primitive for a nonclosed K cannot exist. This is a sharply defined distinct **operator candidate**, not proof against all EFT equation-of-motion redundancies or more elaborate local field redefinitions. Nonzero K and dK do not by themselves guarantee a new physically measurable S-matrix amplitude or stable coupled dynamics.

**Exact symbolic test:** locally executed Python `/mnt/data/cone_gate/quarter_tidal_weyl_test_v15_1381.py`, PASS both independent Weyl components, full nonclosed K derivative and nonzero leading internal amplitude. New additive GitHub equivalent `research-notes/k4_quarter_hyperboloid_weyl_em_v15_1381.py`, SHA **5ba674039b13bbe58e27bf32c82c02852747ec5d**, requires independent committed-byte replay. Do not claim this is an observed physical interaction or derived uniquely by the quarter mesh.

## Gate 1291 — comparator, literature and immediate falsification protocol

Curvature-dependent photon EFTs already exist: Drummond and Hathrell (Phys. Rev. D **22**, 343, 1980; DOI 10.1103/PhysRevD.22.343) derived loop-induced terms including curvature×F². The proposed **C·F·B** term is a structurally different chosen target-area contraction, but it fits normal effective-field-theory construction principles; no literature-wide uniqueness review or novel result is asserted. In particular the fraction 1/4 enters only the *choice of normalized target coordinates*; it **cancels** from B, and neither `zeta` nor `Lambda` nor internal sigma kinetic scale `f` has been derived from Cone arithmetic, a Ward identity, or source data. The prior frozen Einstein–Maxwell+identical K4 comparator is guaranteed to differ from a model with a newly chosen operator, but that alone cannot establish Cone physics: one must compare against the **identical enlarged EFT** for a truly intrinsic quarter selector. With fixed free coefficients the model is ordinary extra-field EFT, not a G-free prediction.

**AUDIT HANDOFF:** replay exact v15.1380 and v15.1381 committed codes; verify operator normalization, Lorentz and target covariance, sign of B^{0x}, linear plane-wave Weyl components, dK identity, symmetry and positive sigma kinetic, and dimensional EFT counting. Search the exact and related operator in established EFT bases and check on-shell/EOM redundancy beyond the simple A shift. Do not transfer the on-shell *gravitational wave* status to the externally prescribed internal u,v map. Independently verify that a fixed discrete finite quarter-grid is NOT the same as the continuous SO+(2,1) sigma target.

**NEXT FALSIFICATION:** specify a kinetic action for the two H² fields with positive energy; choose smooth finite-energy initial data that *dynamically* sweep target area, not a prescribed static source; solve Maxwell+sigma with this chosen Weyl interaction in a fixed Audited K4 tidal background, with conserved total stress and well-posedness/ghost checks; then include the metric response and compare a clock/optical detector against (i) the original matched Einstein–Maxwell+K4 model and (ii) the matched **same enlarged EFT**. Measure a parameter-free ratio, if possible. If only free-parameter EFT corrections arise, record a negative Cone-specific novelty verdict.

**Novelty verdict:** Found a mathematically admissible *possible interaction living on the continuous quarter-hyperboloid sheet*, not a determined force of the arithmetic grid. It is curvature-sensitive in an explicit way and not removed by the simplest field redefinition, but neither coupling nor physical target carrier is selected.
