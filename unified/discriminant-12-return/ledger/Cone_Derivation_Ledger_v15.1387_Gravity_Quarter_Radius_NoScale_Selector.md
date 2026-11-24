# Cone Derivation Ledger v15.1387 — Quarter-radius parameter degeneracy: explicit negative physical selector

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT NEGATIVE] a continuous positive-sheet hyperboloid target with a free sigma kinetic scale and free allowed Maxwell/Weyl coupling does **not** yield an observable physical interaction scale from its geometric radius r=1/4 alone; [D/PASS] exact action reparametrization under arbitrary positive radii, matching canonically normalized target curvature and all first-order Maxwell source couplings; [OPEN] any independent quantized finite-quarter-grid carrier, action-derived kinetic normalization, holonomy/defect/selection rule fixing a physical parameter, stable full interaction and measured clock response. All historical objects preserved, strictly additive.

## Gate 1300 — exact no-scale/quarter selector

For arbitrary r>0 on `H²_r:T²−X²−Y²=r²`, the unnormalized target metric is `g^target_AB=r² G_AB(u,v)` with normalized `G_AB=δ_AB−phi_A phi_B/(1+u²+v²)`; the physical oriented target area is `Omega_phys=r² Omega_norm`, with `Omega_norm=du wedge dv/sqrt(1+u²+v²)`.

Suppose the sigma kinetic term is `−f² r² G_AB ∂phi^A∂phi^B/2`, with **free** scale f, and a bare Maxwell or Weyl–Maxwell–area coupling uses `−g_bare r² F·Omega_norm/2` (or corresponding Weyl-contracted variant). Let r' be an arbitrary new positive target radius. Define

`f'=f*r/r'` and `g_bare'=g_bare*r²/r'²`.

Then **both the full sigma kinetic action and the full target-area interaction are exactly unchanged for all u,v spacetime configurations**. The curvature of the canonically normalized sigma target is `R_sigma=−2/(fr)²`, and is likewise invariant. Thus even a nonzero curvature-dependent EM response cannot distinguish r=1/4 from, say, r=1/3 or r=1/2 without an independently **fixed** f or g_bare. The normalized-target-area formulation used for v15.1380/1381 removes explicit r even earlier: its Maxwell mixing `−g_norm F·Omega_norm/2` simply has no radius factor at all.

This is not an assumption that the original discrete quarter-lattice has no possible measurable discrete information. It is a rigorous negative **for the continuous target sigma-EFT construction proposed in v15.1380–1386 with unspecified kinetic and mixing coefficients**. A finite lattice has no nontrivial common boost preserving all nodes (v15.1185); imposing it as a real physical spectrum would introduce additional structure absent from the current continuous sigma model. One must derive such structure from a legitimate physical Hilbert/gauge/dynamical action, not impose it after finding a desired number.

## Gate 1301 — executed symbolic checks

Actually executed local `/mnt/data/cone_gate/quarter_radius_degeneracy_v15_1387.py`: SymPy verified the sigma metric, target area and canonical target scalar curvature are invariant under above transformations for arbitrary symbolic r,r', f and g, with all assertions PASS. Additive GitHub equivalent `research-notes/k4_quarter_radius_no_selector_v15_1387.py`, SHA **eaec248b6a947c1e5b3930fcbc24415baccaf1e1** (exact byte replay pending External Audit). As a result, the geometrical `r=1/4` has not entered v15.1385's Maxwell mode amplitude except through independently chosen `g_eff`. The v15.1385 response is a valid *chosen EFT example*, not a quarter-induced gravitational constant, a new Casimir measurement, or a G-free parameter-free prediction.

## Audit and physical next gate

**Audit:** replay committed v15.1385–1387 scripts independently, check the sign/normalization of the full induced 4-current, the two Fourier branch transverse projectors, the source Green solution, target geometry and sigma nonlinear equations; explicitly verify no scale/spectrum fixed by the q2 closed-refined shell. Review all EFT field redefinitions, higher derivative metric variation and whether a discrete, constrained/quantized carrier could break the continuous radius reparameterization without violating local Lorentz/gauge covariance.

**NEXT:** formulate a real discrete/continuous interpolation with a physical invariant fixed by the quarter-mesh—not a free `f`, `g`, `zeta`, `Lambda` or auxiliary Casimir—then test its effect on the previously Audited Einstein–Maxwell+K4 optical readout against the exact same extended-action conventional EFT comparator. If no invariant survives these comparisons, the present positive transverse response remains ordinary extra-field EFT and the quarter-shell novelty claim fails.
