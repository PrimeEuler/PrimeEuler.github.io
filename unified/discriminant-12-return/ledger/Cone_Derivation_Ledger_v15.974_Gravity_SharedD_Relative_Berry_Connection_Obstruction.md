# Cone Derivation Ledger v15.974 — Matched n+1 action sphere: relative Berry charge D, holonomy parity, and no canonical Casimir intertwiner

**Date:** 2026-11-14 Eastern. **Gravity lane.** **User:** continue v15.973 into a possible extra connection/phase on existing EM Schwinger CP1, distinct from the formal quarter Casimir. **Status:** [D] exact matched-D relative Berry bundle/curvature/phase and two normalized Casimir differences; [D] no nonzero full-SU2 intertwiner between the two conventional closed spin irreps; [C] common identification of their CP1 base manifolds and choice of independent quarter oscillator action; [N] no independently selected physical relative connection, gravity Casimir, measured G or G-free observable.

**Redundancy and prior work:** v15.617 factor-plane symplectic caution; v15.623 already derives native oscillator CP1 and missing physical action selector; v15.625 and v15.934 distinguish formal versus co-scaled quarter quadratic; v15.631–633 independent Taub–NUT angular Chern charge, integer winding and ordinary fourth-root obstruction; v15.651 zero-mode spinor angular bridge and dimension limitations; v15.692 equal-Chern holonomy versus equal-pair ambiguity and nonidentity with Cone parity; v15.701 already constructs the exact charge-one Hopf projector and Berry curvature; v15.951 shared-D formal odd-quarter label; v15.972 rest/product normalization; v15.973 closed 2D-state q2 symplectic quantization versus invalid naive original-step half-integer prequantum index. **Audit:** latest independently verified relevant Round 578 = canonical v15.966; v15.967/968 collision repairs landed. **Immediately prewrite HEAD:** 9c8e9b21296abfee3eb91fe92eb97ebe52088061 (new exact reproducer); this ledger path absent. Additive-only; certified/frozen, Suzuki, Audit and Sandbox untouched.

## Gate 762 — compare *two actual closed oscillator* action spheres at the same geometric diameter

Fix integer D=n+1≥2. Under the same proposed geometric outer transition circle, the EM Schwinger carrier has total occupation **N_e=D−1**, spin **J_e=(D−1)/2**, and Hilbert dimension **D**. The quarter **co-scaled closed Schwinger** carrier has **N_q=2D−1**, ordinary spin **J_q=(2D−1)/2**, and Hilbert dimension **2D**. Its *geometric* spin coordinate is j_q=J_q/2=(2D−1)/4 and has a scaled commutator, not the ordinary SU2 brackets of that numeric spin. The formal original-unit-step C_formal=j_q(j_q+1) is **not** the closed q2 SU2 Casimir.

v15.623/973 reduce the genuine two-oscillator action to a CP1/S2 symplectic sphere, with integral action area **A_e/(2pi hbar)=N_e** and **A_q/(2pi hbar)=N_q**. For the following comparison choose to identify the two abstract CP1 BASE spheres by the same angles (theta,phi); their symplectic forms remain different. This base identification is a mathematical comparison convention, **not a physical cross-sector map**.

## Gate 763 — exact relative U1 bundle has integer charge D

For ordinary Hopf/Schwinger prequantum lines over that chosen S2, use standard north/south monopole potentials of degree k:

**A_N(k)=(k/2)(1−cos theta)dphi**, **A_S(k)=−(k/2)(1+cos theta)dphi**.

They obey **A_N−A_S=k dphi**, **F(k)=dA=(k/2)sin theta dtheta wedge dphi**, **c1=(1/(2pi))∫F=k**. These are precisely the familiar Hopf/Dirac monopole connections already exhibited in v15.692/701, NOT new topology.

The EM and quarter closed spheres have k_e=D−1 and k_q=2D−1. Their **relative bundle** Hom(L_e,L_q)=L_q⊗L_e* therefore has

**Δk=k_q−k_e=D**,

**A_rel,N=(D/2)(1−cos theta)dphi**, **A_rel,S=−(D/2)(1+cos theta)dphi**,

**F_rel=(D/2)sin theta dtheta wedge dphi**, **c1_rel=D**.

The north-patch latitude holonomy is **W_rel(theta)=exp[i pi D(1−cos theta)]**, so at the equator **W_rel(pi/2)=(-1)^D**. This is a G-independent, integer-quantized *mathematical* relative phase after choosing to identify angular loops. For D=2,3,4,5 it alternates +1,−1,+1,−1.

Critically the shared-circle **formal odd-quarter index L_q=2D−1 is odd for every D**; its parity is **not** the variable relative holonomy (-1)^D. The old Cone character chi(L_q)=(-1)^Lq=-1 for every D does not equal W_rel for even D. This extends the explicit parity-versus-holonomy mismatch already recorded in v15.692; do not rename the relative Berry winding a new quarter Casimir or gravitational field.

## Gate 764 — no canonical sector identification or full multiplet SU2 intertwiner

A global everywhere nonzero *scalar* bundle isomorphism L_e→L_q would be a nowhere-zero section of the relative degree-D line bundle. Since D>0, that is topologically impossible: a nowhere-zero section would trivialize the bundle, forcing c1_rel=0. Smooth sections exist but must vanish somewhere; for a generic holomorphic section of O(D), zeros count D with multiplicity. Consequently, an EM↔quarter scalar field with globally nonzero local amplitude cannot arise solely from these two different prequantum lines. Additional components, zeros, singularities or physical fields are required (as in the already-known v15.701 two-component Hopf construction).

At the **quantum multiplet** level, H_e=H^0(CP1,O(D−1)) is the spin-(D−1)/2 irrep, dimension D; H_q=H^0(CP1,O(2D−1)) is the spin-(2D−1)/2 irrep, dimension 2D. An explicit *chosen* injection exists by multiplying any degree-(D−1) homogeneous polynomial by z_0^D, making degree 2D−1; it is not SU2 equivariant, because it selects the z_0 axis. Schur's lemma forbids a nonzero operator T:H_e→H_q intertwining the FULL respective SU2 actions (their irreps are inequivalent and have distinct dimensions). This no-go is for a full SU2 intertwiner, not all tensor/vector/spinor intersector operators; ordinary Wigner–Eckart tensors may connect different j when an independently defined transforming source is supplied. A sourced field or nontrivial representation content could enable them.

## Gate 765 — what the action connection does and does NOT explain about the kinetic Casimir

Under ordinary dimensionless SU2 normalization, **C_e=J_e(J_e+1)=(D²−1)/4** and **C_q,norm=J_q(J_q+1)=D²−1/4**, giving **C_q,norm−C_e=3D²/4**. Under the *co-scaled quarter geometric normalization* K_i=J_q,i/2, its quadratic is **C_q,scaled=(D²−1/4)/4** and the fixed-D contrast is

**C_q,scaled−C_e=3/16**,

the geometric fixed-outer-circle +3/16 from v15.951 in correct matched labels. This does NOT mean the two physical Casimir operators differ by +3/16 on the same Hilbert space: their dimensions/commutator normalization differ, and there is no canonical intertwiner. The formal quarter polynomial remains another operator convention, not an independently sourced physical gravitational Casimir.

The relative Berry charge Δk=D grows with D, whereas the *scaled geometric Casimir* gap is 3/16 independent of D. Neither relation fixes a rotor kinetic inertia I, physical frequency or a measurable EM/G relative phase. Berry curvature requires a prepared state, specified adiabatic path and physically meaningful relative-phase readout; the common-CP1 identification and source action are not supplied by the null-cone coordinates. At equal integer Chern classes one instead gets equal phases, as already established in v15.692; this gate changes the matching rule to same geometric D, not the physics of monopoles.

## Verification, scope and next test

**Reproducer:** `research-notes/k4_relative_berry_bundle_sharedD_v15_974.py`, additive commit **9c8e9b21296abfee3eb91fe92eb97ebe52088061**. Local exact SymPy proof of north/south potential difference, F_rel and Chern class, formal equatorial parity comparison, normalized and scaled Casimir gaps and explicit polynomial injection dimensions; D=2..100 integer checks PASS. The module is combinatorially simple and independently checkable. **Independent Audit pending.**

**Positive:** The *relative connection* is globally consistent as an ordinary integer monopole charge **D**, and its equatorial phase is exactly (-1)^D after fixing a loop. This gives a precise connection candidate on the same outer-circle dictionary rather than a vague quarter-phase suggestion.

**Negative selector:** this is the known Hopf/Dirac/Berry bundle construction with no novel local curvature law. It cannot canonically identify the D- and 2D-dimensional quantum sectors or turn the quarter formal Casimir into physical kinetic energy. The bundle difference creates an obstruction to a nowhere-zero scalar sector map, not a physical coupling. The mismatched parity and different normalizations defeat a parameter-free new gravity observable.

**NEXT:** Test whether an independently sourced rank-1 or rank-2 tensor operator with definite angular transformation law could connect the inequivalent representations without an arbitrary reduced matrix element, compared against the old Wigner–Eckart/TT tidal negative gates. If the reduced matrix element is free, return negative and hold the quarter connection as a geometric comparator. Alternatively a physically motivated multi-component charged field action would be needed; no bare Berry connection supplies one.

**HANDOFF Audit/Muse:** independently verify the relative Chern D with an explicit chosen CP1 identification, equatorial phase, topological no-global-scalar-isomorphism, quantum SU2 Schur obstruction, and distinction C_q,norm−C_e=3D²/4 versus C_q,scaled−C_e=3/16. Preserve any physical interpretation as conditional.
