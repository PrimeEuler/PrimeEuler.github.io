# Cone Derivation Ledger v15.970 — Can the conserved n+1 null cone fix the kinetic inertia/clock from its three circles?

**Date:** 2026-11-14 Eastern. **Gravity research lane.** **Owner authorization:** after v15.969's conditional EM/G Casimir kinetic-energy difference, directly test whether n+1 null-cone circle, action-circle geometry or Casimir radii select a kinetic inertia and physical frequency without measured G. **Parents/redundancy:** v15.900 explicit radial rotor counterfamily (turning radii do not fix potential), v15.904 canonical reissue v15.916 n+1 clock selector negative and speed constraint, v15.934 co-scaled Casimir circles, v15.950/951 equal product vs shared outer diameter and three inequivalent Casimir offsets, v15.955 (canonical v15.968) Jxy midpoint operator and Pauli blocks, v15.969 conditional kinetic splitting. **Audit Round 578 v15.966** verified v15.954/955 and their label-collision reissues v15.967/968 were made additively. **Immediately prewrite HEAD:** 5f4c0c15eca4fa09cc1b716eea5f6b7894880637. Checked target absence. Additive only; Suzuki, frozen, Audit and Sandbox objects untouched.

**Status:** [D] three exact candidate inertia/kinetic profiles and explicit no-selector counterfamily; [C] rotor action, chosen interpretation of each circle as an inertial radius, same physical mass and length conversion; [N] geometry cannot fix kinetic inertia, clock, G or a physical gravitational Casimir; [O] field-sourced action.

## Gate 748 — precise kinetic question and scale dimensions

The standard rotor action and its conjugate momentum are **S=∫dt (I/2) theta_dot²**, **p_theta=I theta_dot**, and its Hamiltonian is **H=p_theta²/(2I)**. With a proper SO3 rotor representation, **E_j=ℏ² j(j+1)/(2I)**. An angular coordinate and radius without the coefficient I are insufficient to define physical energy, rate or action; an overall positive I and physical time/length scales remain free. A sector's full SU2 Casimir is scalar on a fixed multiplet and does not itself induce within-shell J± transitions.

At shared physical *geometric* outer diameter D=n+1≥2, use the conditional **formal** assignment

**C_e=(D²−1)/4**, **C_q=(2D−1)(2D+3)/16**, **C_q−C_e=(4D+1)/16**.

The q quantity is the old odd-quarter geometric Casimir label; it is NOT an independently established physical gravity operator (v15.624–625) and resides in a different carrier. The calculation below deliberately assumes its kinetic interpretation only as a stress test.

Let a geometric squared radius r² be mapped to physical inertia **I=M ℓ_*² r²** for a thin ring of mass M. These are extra mechanical assumptions, including the same mass M and length calibration ℓ_* for the two sectors. At fixed D the candidate geometric radius squares are:

- OUTER: r_e²=r_q²=D²/4 (shared null-cone section).
- CASIMIR radius: r_e²=(D²−1)/4, r_q²=(D²−1/4)/4 (the chosen geometrical R_C formula from v15.951; not a physical angular momentum magnitude).
- INNER product chord: r_e²=D−1, r_q²=D/2−1/4 (factor endpoint pair (D−1,1) vs (D−1/2,1/2)).

Each produces a **conditional** normalized energy difference

**F(D) := (2Mℓ_*²/ℏ²)(E_q−E_e) = C_q/r_q²−C_e/r_e²**.

## Gate 749 — three different exact kinetic profiles at the same outer null diameter

Direct symbolic substitution gives

**F_outer(D)=(4D+1)/(4D²)**,

**F_Casimir-radius(D)=2/(2D+1)**,

**F_inner(D)=(D+2)/4**.

For D=2: (9/16, 2/5, 1); for D=3: (13/36, 2/7, 5/4); D=5: (21/100, 2/11, 7/4). These have **different functional dependence on the conserved shell size**, though all draw their radii from the same Cone circles. In particular outer and Casimir radius choices decay like 1/D, while inner grows like D. The Casimir-radius cancellation **C_e/r_C,e²=1** holds by construction and must not be presented as physical inertia selection; it is precisely an algebraic radius named after an operator Casimir. No independent kinetic action or equilibrium principle favors any one of these I=Mℓ²r² identifications. Therefore the n+1 null-cone geometry does NOT uniquely select a dimensionless energy-gap profile once the kinetic metric itself is unspecified.

These are mathematical comparisons of physical rotor *hypotheses*. In particular the formal quarter C and geometric quarter radius R_C,q² are different quadratic constructs, so the special F_Casimir-radius value is not an equality of physical operators.

## Gate 750 — explicit positive-inertia counterfamily kills an automatic splitting

Even if the two sectors share the OUTER radius and ℓ_*, but are allowed different inertial masses M_e,M_q>0, their kinetic energies satisfy **E_q−E_e=(ℏ²/(2ℓ_*² r_o²))(C_q/M_q−C_e/M_e)**. Choosing

**M_q/M_e=C_q/C_e=(2D−1)(2D+3)/[4(D−1)(D+1)]>0**

makes E_q=E_e **exactly**, despite nonzero formal Casimir gap C_q−C_e>0. Larger/smaller mass ratios change the sign. Both models preserve all of the same lattice, null-cone and Casimir-label identities. This is a direct counterexample to the idea that a geometric Casimir gap by itself forces an independently measurable kinetic splitting. The ratio is an allowed *model choice*, not a suggested physical prediction or mass hierarchy.

Furthermore, with mass M held fixed, the free conversion ℓ_*→λℓ_* changes EVERY rotor energy splitting by **1/λ²**. Hence even choosing a circle and equal masses gives no clock in seconds or joules, absent independently specified M,ℓ_* (or an equivalent measured/derived dynamical coefficient). ħ alone is an action unit and does not supply both missing mechanical scales.

## Gate 751 — compare to existing no-go and the physical frontier

This result is complementary to the already audited v15.900 counterfamily (different V(r) give distinct radial frequencies) and v15.916 shell-frequency obstruction (n+1 is a conserved diameter/dimension, not an automatically physical frequency). It does NOT claim a new global no-go over every conceivable field action: an independently sourced field kinetic term, gauge-normalized radius, fixed mass, or kinetic metric could choose one profile. Current Cone static arithmetic supplies none, and choosing I by identifying it with a geometric Casimir radius would be circular as a physical derivation.

The **positive** exact output is a menu of falsifiably different conditional kinetic **shape** functions F(D), including an unexpected exact simplicity for the Casimir-radius test. **The negative** is the rigorous nonidentifiability of inertial normalization or absolute energy from the present static Cone geometry. No experimentally distinguishable gravity observable, universal G-free frequency or physical gravity Casimir has been derived.

**Reproducer:** `research-notes/k4_casimir_kinetic_circle_inertia_selector_v15_970.py`, additive commit **5f4c0c15eca4fa09cc1b716eea5f6b7894880637**. Exact symbolic SymPy proof of three profiles, positive inertia cancellation, action Legendre transform, length rescaling λ^−2, and D=2..1000 sample checks; executed locally PASS (reference code checked with an identical local version). **Independent Audit pending.**

**NEXT:** Decide whether the user-proposed null-cone action circle actually supplies a canonical symplectic action variable `J=∮p dq` and a field-derived kinetic metric, not merely an SI length. For any suggested action-angle map, demand an explicit nondegenerate 2-form and separately normalized Hamiltonian. Check whether a physical EM ↔ gravity coupling operator's relative phase remains measurable after accounting for sector coherence and superselection. If no field-sourced Mℓ_*² or equivalent kinetic coefficient emerges, register negative rather than relabel one of the three circles as inertia.

**HANDOFF Audit/Muse:** independently verify the 3 shape functions, scale and mass counterfamilies, proper distinction between the ordinary EM SU2 Casimir, q2 formal odd-quarter label and R_C,q geometric radius, and the lack of an independently normalized physical action.
