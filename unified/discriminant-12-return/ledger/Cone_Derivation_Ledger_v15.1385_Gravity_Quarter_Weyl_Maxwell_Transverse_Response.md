# Cone Derivation Ledger v15.1385 — A Weyl–quarter-hyperboloid source radiates a transverse Maxwell Fourier mode

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Classification:** [C] physically allowed but freely chosen dimension-six Weyl–Maxwell–sigma target interaction on continuous positive-sheet H²; [N PASS, leading weak fixed backgrounds] direct source-current derivation, exact local conservation, Fourier polarization selection, independently solved retarded transverse Maxwell response, zero coupling control, linear field/quadratic mode-energy scaling; [NEGATIVE] no intrinsic physical quarter-grid selector, no SI scale, full dynamical self-consistency or observed photon; [OPEN] full target+metric+Maxwell variation, field-energy exchange, stress-energy conservation, nonlinear evolution, optical detector and same enlarged EFT comparator. Strictly additive; all historical files preserved. **Parents:** v15.1380–1382 and Audit Round 632/v15.1383. Exact v15.1382 prose sign corrected additively in v15.1384, **(dK)_xyz=+(dK)_txy**.

## Gate 1294 — specify all three free on-shell leading backgrounds and derive the current

Choose flat local (-+++) coordinates and a weak TT plus gravitational wave `hxx=epsilon cos(t−z), hyy=−hxx`. Its linearized first-order Riemann equals Weyl, and the linearized Einstein vacuum equation holds. Choose the *leading linear sigma-model solutions* `u=a sin(t−x)`, `v=b sin(t−y)`; `Box u=Box v=0` while nonlinear sigma EOM and gravitational backreaction enter beyond the approximation. Leading internal target area `B_mu nu=du wedge dv+O(a³b,ab³)`.

The proposed action interaction is `L_int=−g/2 C_mu nu rho sigma F^{mu nu} B^{rho sigma}` with `g=zeta/Lambda²`. Maxwell variation yields conserved effective source `Jnew^nu=−g partial_mu(C^{mu nu rho sigma}B_rho sigma)`. The direct four-index Riemann/Weyl contraction with explicit target wave derivatives, antisymmetric index raising and full 4-divergence gives, **to O(epsilon*a*b)**,

`Jnew^mu=g_eff (1,1,1,1) sin(2t−x−y) cos(t−z)`, `g_eff=(zeta/Lambda²)*epsilon*a*b`.

Independent symbolic divergence `partial_mu Jnew^mu=0` exactly; this is a nonzero **conserved** effective Maxwell source. This is a sourced Maxwell equation on a prescribed gravitational and internal-wave background, NOT a self-consistent full interacting Einstein-Maxwell-sigma solution. The GW and sigma waves are on shell only at the stated uncoupled leading perturbative order, and their backreaction (including sigma stress O(f²a²), O(f²b²)) is explicitly absent.

## Gate 1295 — two Fourier branches and a transverse EM polarization selector

The current's exact Fourier split is

`sin(2t−x−y) cos(t−z) = [sin(3t−x−y−z)+sin(t−x−y+z)]/2`.

The first generated mode has `q+=(1,1,1), omega+=3`, and spatial current direction `j=(1,1,1)`. Its transverse projector `P_T(q+) j=j−q+(q+·j)/|q+|²=0`, so **no transverse photon is excited by this Fourier branch**; its conserved longitudinal charge/current sector is not asserted absent.

The second has `q-=(1,1,−1), omega-=1`. Here

`P_T(q-) j=(2/3,2/3,4/3)`,

which is nonzero. This is an orientation-dependent *polarization selection rule* of the **proposed chosen operator and specified incoming waves**; it is not evidence that the quarter-grid uniquely selects an EM helicity or derives electromagnetic coupling.

## Gate 1296 — independently solve the retarded Maxwell mode

With Maxwell `partial_mu F^{mu nu}=Jnew^nu` and Lorenz gauge, `Box A^nu=Jnew^nu`. For the nonzero transverse q- component this becomes `A_T''+3A_T=−J_T(t)`, with exact zero initial photon potential and canonical momentum. At positive spatial Fourier q- convention `J_T(t)=(i g_eff/4)e^(−it) P_T(q-)j`. The exact retarded solution is

`A_T(t)=−[J_T(0)/(3−1)] [e^(−it)−cos(sqrt3 t)+(i/sqrt3)sin(sqrt3 t)]`.

Independent ODE integration with SciPy `solve_ivp` and an independent adaptive quadrature of the retarded sine Green kernel match this analytic solution to `1e−15` or better over t=.3,.7,1.1 at g_eff=.02. Actual executed Python/NumPy/SymPy/SciPy results:

| t | g_eff | |A_T| | quadratic transverse mode energy | maximum Green error | maximum ODE error |
|---|---:|---:|---:|---:|---:|
| .3 | .02 | .0003583293290092406 | .0000029118676032249134 | 2.24e−19 | 1.12e−15 |
| .7 | .02 | .0017426151915830282 | .000013951528983975607 | 4.63e−19 | 1.92e−15 |
| 1.1 | .02 | .003490245330311536 | .000027990414851220814 | 2.17e−19 | 4.23e−15 |

Mode energy means `(sum_i |A'_i|²+3 sum_i |A_i|²)/2` in the chosen Fourier normalization. It is a **diagnostic**, not a sourced total energy-conservation check. Halving g_eff halves induced |A| and reduces mode energy by exactly factor four; g_eff=0 yields exactly zero field and mode energy. The chosen g_eff=.02 is illustrative and completely **undetermined** by the quarter radius, K4 solid, or conventional SI constants. The background EM response is therefore parametrically predictable given the enlarged EFT parameters and initial data, but **not** a parameter-free Cone prediction.

**Actually executed local source:** `/mnt/data/cone_gate/quarter_weyl_maxwell_response_v15_1385.py`, full 4D TT Weyl construction, internal-wave pullback, exact J conservation, both transverse projections, three analytic retarded solutions, adaptive quadrature, independent ODE, negative controls. **Additive GitHub source:** `research-notes/k4_quarter_h2_weyl_maxwell_response_v15_1385.py`, commit **b21ede79588b1489000cf2264135b8acaff323eb**, equivalent independently authored program using same full Riemann/Weyl contraction and Fourier Green/ODE checks. Exact committed-byte replay is pending external Audit.

## Gates and hard novelty boundary

A positive geometric response with an independent Maxwell solution is meaningful **as a selected effective interaction candidate**, unlike the original Casimir-only proposal. It still requires independent continuous H² *fields*, no longer just an arithmetic quarter-grid, and a freely adjustable dimensionful coefficient. It is not proof of new physics: a comparator with the identical Weyl–sigma–Maxwell operator gives the same current and output, regardless of how the hyperboloid was labeled. Moreover normalized target area has no surviving explicit r=1/4; changing the target radius can be compensated by the target kinetic normalization and coupling. A separate intrinsic quarter-grid selector is therefore still missing.

**AUDIT HANDOFF:** replay exact GitHub v15.1385 source; independently verify Riemann sign, first-order consistency and 4-current divergence, both Fourier branch signs and transverse polarization vectors, Green solution initial conditions, `Box A=J` source sign, energy scaling and zero controls. Demand that the distinct source-side sigma action and stress conservation be derived before treating this as a fully coupled gravitational interaction or physical photon prediction. Do not label the Fourier mode an independent measured gravitational observable.

**NEXT:** establish the target H² nonlinear sigma equations and positivity (v15.1386), then vary `S_{EH}+S_{K4}+S_{Maxwell}+S_{sigma}+S_int` in every field, including Weyl-metric variation, derive an order-consistent total stress/Bianchi identity and investigate principal symbols/hyperbolicity within EFT cutoff. Finally source a finite localized map, propagate coupled Maxwell/sigma on the pre-validated K4 metric, and run a gauge/event-calibrated optical readout. Compare against a **matched same enlarged EFT** to isolate any truly quarter-grid-specific effect.
