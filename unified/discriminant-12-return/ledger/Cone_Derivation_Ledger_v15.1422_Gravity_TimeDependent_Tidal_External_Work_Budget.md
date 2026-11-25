# Cone Derivation Ledger v15.1422 — Prescribed time-dependent Weyl/tidal background does work on the coupled matter sector

**Date:** 2026-11-24 Eastern / Nov 25 UTC. **Gravity/Cone.** **Status:** [EXACT VARIATIONAL IDENTITY / NUMERICAL PASS] a time-dependent external tidal parameter in an explicitly local Maxwell–sigma canonical mode model changes its matter Hamiltonian by exactly the source's Noether work; [NEGATIVE] Maxwell+sigma alone need **not** conserve energy when a prescribed tidal coefficient varies in time, and an autonomous physical total-energy claim requires including dynamical gravitational degrees of freedom or a complete external-work budget; [OPEN] actual Einstein–Weyl metric variation, gauge/constraint consistency, UV cutoff, physically prepared packet and q2-only coupling. This does not overturn v15.1416's autonomous frozen-constant-coefficient Hamiltonian energy conservation, which is correctly scoped.

## Gate 1366 — energy identity with a time-dependent external tide

Take the explicit **two-mode reduction** (illustrative source-work diagnostic, not a full derivation from the four-index Weyl EFT)

`L=½(Adot²+udot²−A²−u²)+g c(t) Adot udot`

with real g and prescribed tidal coefficient c(t). Its symmetric velocity kinetic matrix is `M(t)=[[1,g c],[g c,1]]`, positive definite if `|g c|<1`. Canonical momenta are `p_A=Adot+g c udot, p_u=udot+g c Adot`. The full Legendre Hamiltonian is

`H=½ p^T M(t)^(−1) p +½(A²+u²)`.

Because H depends **explicitly** on external c(t), its exact evolution obeys

`dH/dt=∂H/∂t=−g cdot(t) Adot udot`.

The last expression is the work of the prescribed external tidal source, not an internally conserved Maxwell+sigma quantity. This matches the conventional Noether identity that explicit background-time dependence spoils separate matter Hamiltonian conservation. When g=0 or c(t)=constant, the autonomous matter total energy is conserved.

## Gate 1367 — independently integrate dynamic energy and prescribed source work

For a test with g=.08, c(t)=.4cos(.85t), interval t∈[0,11], positive matrix eigenvalues 1±.032 max, initial canonical state (A,u,p_A,p_u)=(.14,0,0,.09), solve the complete two-field Hamilton equations using DOP853 with tight tolerances. Separately evaluate the Hamiltonian at each sampled t, and integrate the **independent external work** `W=−g∫_0^T cdot Adot udot dt` by Simpson quadrature (3001 points).

Actually executed local Python `/mnt/data/cone_gate/k4_prescribed_weyl_external_work_v15_1422.py` yielded

| g | E_initial | E_final | E_final−E_initial | external W | |difference| |
| ---:|---:|---:|---:|---:|---:|
| .08 | .013854151451085914 | .013848682674333979 | −5.468776751935134e−6 | −5.468776749228318e−6 | 2.7068e−15 |
| 0 | .01385 | .013849999999996759 | −3.2422e−15 | 0 | 3.2422e−15 |

Thus the matter energy can decrease while the external tidal source accounts for the entire change to ~3×10^−15 absolute. The sign of net change depends on the phase/preparation; negative here is not a universal energy-loss law. This is independent of the earlier v15.1414 fixed-background photon mode work check: there, an externally prescribed sigma/TT source supplies positive electromagnetic energy without its own computed depletion; here, a *time-dependent tidal coupling coefficient* supplies or receives energy.

**Additive GitHub reproducer** `research-notes/k4_prescribed_weyl_external_work_v15_1422.py`, SHA **3791dbd107a1fa7182ed67ac9709fc7552cc3578**, equivalent to actual local code, exact-byte Audit replay pending.

## Gate 1368 — actual full coupling decision

The **complete** Weyl–Maxwell–H² action couples Einstein-metric second derivatives and F and the target area pullback B. In truly 3D spacetime C is identically zero (v15.1421), whereas in 4D the full Weyl tensor on an admissible prescribed TT curvature background has a physical transverse scalar–Maxwell local nonluminal characteristic branch (v15.1420). The standalone matter-sector Hamiltonian is **not generally conserved** when a dynamical gravitational tide has been replaced by a prescribed time-dependent external coefficient. Therefore no combination of the earlier positive reduced energy conserved result and the nonzero radiation source can yet claim a stable, causal, fully backreacted Einstein–Maxwell–H² theory. The correct next task is the constrained 3+1 metric variation, gauge-fixed principal symbol, stress/Noether consistency and EFT order-reduction below cutoff, plus matched same-enlarged-EFT comparison.

**AUDIT HANDOFF:** independently replay committed v15.1420–1422 source bytes; derive TT Riemann/Weyl curvature sign and complete tensor source, verify the background-gradient transverse mode and velocity Hessian, check correct 2+1 Weyl identity, representative metric-variation differential order, and the time-dependent Hamiltonian external-work sign. **High priority:** determine whether the local nonluminal branch survives imposing full Einstein constraints and EFT order reduction; do not extrapolate fixed-background characteristic phase speeds into physical superluminal signalling.

**NOVELTY VERDICT UNCHANGED:** H² curvature interaction is chosen rather than selected from the finite quarter-grid; exact radius/coupling degeneracy v15.1387/v15.1398 remains. The exact nested EM–q2–null 3:1 affine geometry, conditional π/2 holonomy and measured Dirac rapidity remain representation-space structures, not a computed G-free coupling or force.
