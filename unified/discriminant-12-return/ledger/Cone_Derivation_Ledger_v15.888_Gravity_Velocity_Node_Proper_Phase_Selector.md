# Cone Derivation Ledger v15.888 — Gravity: proper-time phase across velocity nodes and conditional winding selector

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Gravity v15.884–886; Sandbox v15.233, v15.857, v15.866; External Audit Round 568/v15.887. **HEAD checked before write:** `49c8c814df9dfa0b279ece979863605e5bdba6bf` on master. Target path checked absent. Additive only; no historical, Suzuki, Audit, or Sandbox objects modified.

**Question:** If a massive state's action circle advances with the usual proper-time phase rate, can velocity-node traversal and a full-winding condition select the previously free Rindler-to-Compton ratio rho?

**Labels:** [D] exact SR kinematics and conditional proper-time phase; [N] no unique rho without a genuine periodic identification/boundary condition; [O] physical phase recurrence and mass/force selector.

## Gate 544 — compute phase using proper time rather than laboratory time

For uniformly accelerated motion with constant proper acceleration a>0, write beta=v/c=tanh eta, where eta=a tau/c and tau is comoving proper time, with eta=0 at rest. At illustrative velocity-axis node fractions beta_1=1/4 and beta_2=1/2,

Delta eta = atanh(1/2)-atanh(1/4) = (1/2) ln(9/5) = 0.2938933324510595... .

Delta tau = (c/a) Delta eta. This is distinct from laboratory time Delta t=(c/a)(1/sqrt(3)-1/sqrt(15)) in v15.885.

Assume an internal rest-phase clock dphi/dtau=mc^2/hbar (standard massive free-state phase, used here only as a conditional clock; the force/drive maintaining acceleration may change actual internal states). Given L_R=c^2/a=rho hbar/(mc),

**Delta phi = (mc^2/hbar) Delta tau = rho Delta eta = (rho/2) ln(9/5).**

At rho=1 this is 0.293893... radians, only 0.0467745766013... of a full 2pi winding. Therefore the previous rho=1 length weld is NOT the same as a full-cycle phase lock between these two assumed nodes.

## Gate 545 — what a genuine phase quantization condition *would* select

If and ONLY if the dynamics identify the two node events as endpoints of one closed internal phase loop, impose Delta phi=2pi N for positive integer N. Then

**rho_N = 4pi N/ln(9/5)**

and rho_1=21.3791352623690..., not 1. A different phase condition, such as antiperiodicity Delta phi=(2N+1)pi, gives different rho. If the endpoints are simply two different velocity events (as in the current model), no phase continuity boundary condition requires integer windings; rho remains any positive real. Nor is a time-independent external force automatically a periodic pump. Therefore this calculation is a *conditional spectral candidate*, not a selection theorem.

Caution: a single crossing on an accelerated worldline is not a closed orbit, even if the visual mesh shows two nodes. Closing a clock path must be supported by an actual recurrence, self-adjoint operator with its boundary domain, or dynamical return map. The EM 1/2 and gravity 1/4 mesh vertices are geometrical offsets, not proven universal physical speed fractions c/2 and c/4.

## Gate 546 — an independent standard-physics comparator leaves the same ratio free

For a uniformly accelerated detector in Minkowski vacuum, the standard Unruh temperature is T_U=hbar a/(2pi c k_B). In the rho-family this implies

**k_B T_U/(mc^2) = 1/(2pi rho)**,

and a thermal Boltzmann ratio for an assumed detector energy gap Delta E=mc^2 is **exp(-Delta E/(k_B T_U))=exp(-2pi rho)** (ideal detailed-balance comparator; rates also depend on detector coupling and response). For rho=1 this ratio is exp(-2pi)=0.0018674427317..., but no detector or bath equilibrium law forces that value. Identifying the rest energy with a specific detector excitation gap is a further hypothesis. This is an independent check that dimensionless quantities can depend on rho without selecting it.

## Gate 547 — checks, provenance, and next discriminator

Fresh local SymPy check: atanh(1/2)-atanh(1/4) rewritten into logarithms equals ln(9/5)/2 exactly; numerical Delta eta=0.2938933324510595 and rho_1=21.3791352623690 verified. Derivation for Delta phi follows from proper-time action phase and a=mc^3/(rho hbar), exactly. No numerical GR solver or experimental claim is made. **Independent Audit not yet performed** on this entry.

Compared with Sandbox v15.857, Hamilton–Jacobi inversion reconstructs the linear potential U(x)=ma x but preserves a; the new phase calculation does not repair that missing force selector. Sandbox v15.866 establishes sector-similar geometry at shared hbar; it does not establish a dynamical closed velocity-node loop.

**Verdict:** A closed proper-time phase interval would turn the continuous rho family into a conditional discrete set, but the assumed c/4,c/2 nodes and the closed-loop condition are not yet consequences of the frozen Cone action. The rho=1 weld and the full-winding hypothesis give inequivalent answers. Neither is promoted to physical prediction.

**NEXT:** derive (or fail to derive) a true node-to-node return map from an explicit Hamiltonian/Maxwell+gravity coupling with specified forcing and boundary conditions. Test a self-adjoint eigenvalue problem against the continuous-parameter control, and compare against ordinary accelerated-detector physics. Do not insert a Compton/radian equality, a G value, or a 2pi winding by hand.

**HANDOFF External Audit/Muse:** independently check the proper-time vs laboratory-time distinction; ln(9/5)/2; winding rho_N and rho_1; Unruh comparator normalization; and, most importantly, that a single accelerated traversal is not a periodic orbit. Report any correction as an additive later entry.
