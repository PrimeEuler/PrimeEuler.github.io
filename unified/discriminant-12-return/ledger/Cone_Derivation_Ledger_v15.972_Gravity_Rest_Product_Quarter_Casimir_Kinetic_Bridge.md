# Cone Derivation Ledger v15.972 — Quarter rest/product circle normalizes the formal-vs-co-scaled Casimir difference

**Date:** 2026-11-14 Eastern. **Lane:** Gravity/EM Cone geometry. **User:** "lets do it, yeah i was thinking the 1/4 casimir circle is the gravity casimir but putting it as the sqrt(n) product circle makes since for our action circle / rest mass work." **Status:** [D] exact quarter product/rest shell and two different quadratic invariants; [D] co-scaled closed q2 Schwinger matrix and inability to identify odd-quarter formal j with an ordinary original-unit SU2 spin; [C] product/rest radius as kinetic lever arm; [N] no independently sourced physical gravity Casimir/kinetic coefficient.

**Parents and collision check:** v15.624/625 distinct EM and formal quarter-Casimir sectors; v15.602 projected q2 unit-step ladder defects; v15.934 three circles and the C_formal−C_scaled=L/8 identity; v15.951 fixed-D odd quarter shell; v15.955 (canonical additively repaired v15.968) state-centered Jxy correspondence; v15.969 Casimir as kinetic hypothesis; v15.970 three candidate inertias; v15.971 product-circle versus geometric Casimir-circle separation. Round 578 Audit v15.966 confirmed v15.954/955 mathematics and flagged numbering collisions, repaired v15.967/968. **Live master HEAD immediately prewrite:** cc54ea71eb7aba2786de7edf69723fb2a12a3a47 (new exact reproducer). Ledger target checked absent. Strictly additive: certified/frozen, Lane A, Sandbox and Audit paths untouched.

## Gate 754 — use the quarter primitive pair's product circle as a REST/ACTION carrier, not automatically as its Casimir

Use physical shared EM outer diameter **D=n+1** (D≥2) with endpoint grids u_e=1, u_q=1/2. The EM primitive pair is (D−1,1); the quarter primitive pair is (D−1/2,1/2). Both satisfy the same outer null-section circle, but have *different products*. Define

**P_e=R_rest,e²=D−1**, **P_q=R_rest,q²=(D−1/2)/2=(2D−1)/4**.

The prior shared-D q2 mesh index is **L_q=2D−1**, with formal quarter geometric label **j_q=L_q/4=(2D−1)/4=P_q**. Thus the candidate quarter-sector rest/product radius is EXACTLY related to its *formal* spin label by

**R_rest,q²=P_q=j_q**.

This is an indexing/geometric identity at the chosen quarter endpoint; it is not an equation between independent physical rest mass and angular momentum observables. The original EM rest/product is P_e=2j_e, with j_e=(D−1)/2. This rest circle is geometrically distinct from the *quarter geometric Casimir circle* with squared radius (D²−1/4)/4.

## Gate 755 — exact normalized formal-vs-co-scaled Casimir gap

At the quarter formal label j_q=P_q define the original-unit-step **formal polynomial** and the half-unit-step **co-scaled closed quadratic**:

**C_formal=j_q(j_q+1)**,
**C_scaled=j_q(j_q+1/2)=L_q(L_q+2)/16=(D²−1/4)/4**.

The latter equals the quarter *geometric Casimir circle radius squared* in our co-scaled convention; it is not the same scalar as C_formal. Their difference is **C_formal−C_scaled=j_q/2=P_q/2**. Dividing by the independently defined primitive product/rest radius squared R_rest,q²=P_q gives the exact shell-independent rational

**(C_formal−C_scaled)/R_rest,q² = 1/2**, for all D≥2.

This is the clean normalized statement. It is already implicit in v15.934's L_q/8 formula, but its **rest/product normalization and constant 1/2 consequence** are now explicit at the user's shared-D primitive endpoint. It does not by itself supply a new force, frequency or physical gravity kinetic energy.

For comparison with the *actual* EM spin-j Casimir C_e=(D²−1)/4 and EM product inertia P_e=D−1, define dimensionless conditional rotor ratios:

**C_e/P_e=(D+1)/4**, **C_scaled/P_q=(2D+1)/4**, **C_formal/P_q=(2D+3)/4**.

Thus quarter-scaled minus EM =D/4; quarter-formal minus EM =(D+2)/4, and their difference =1/2. This reconstructs and isolates the linear inner drift seen v15.970/971: the **common D-dependent term** reflects competing primitive product/inertia sizes, while **the within-quarter formal-vs-co-scaled difference** is a constant after rest-product normalization.

## Gate 756 — actual q2 closed ladder and its separate representation

The quarter mesh has **2D formal nodes** with refined magnetization step h=1/2. The *closed* refined-step Schwinger representation is the ordinary unit-step **spin J_ref=(2D−1)/2**, dimension 2D, with physical co-scaled matrices J'±=(1/2)J±, M'=(1/2)J_z. The quadratic central element in these scaled units is

**C_scaled=J_ref(J_ref+1)/4 = j_q(j_q+1/2)**,

and [J'+,J'−]=M' rather than the original-unit normalization 2M'. Exact matrices pass for D=2..8. A genuine standard original-unit SU2 representation with "spin j_q=(2D−1)/4" would have formal dimension 2j_q+1 = D+1/2, **not an integer**, so it cannot be a finite-dimensional unitary SU2 irrep. The original-unit-step quarter-polynomial C_formal is not therefore an independently physical SU2 kinetic Casimir. The projected original-step ladder has the previously audited nonclosure/boundary Casimir defects. Any physically sourced non-SU2 gravity Casimir would require a separate algebra and kinetic action.

The original EM Schwinger state-centered Q=Jx²+Jy² remains exactly matched to the shared-D half-integer physical *row positions* (v15.955/968), but it acts on a D-dimensional EM Fock carrier. The quarter q2 closed refined model has 2D states. Positional row correspondence is not a unitary intertwiner or a physical EM/G transition operator.

## Gate 757 — kinetic-action test and scale obstruction

If a physical thin-ring rotor action is additionally chosen,
**S=∫dt (I/2) θdot²**, with *chosen* inertia **I=M ℓ_*² P_q** (mass M and SI length conversion ℓ_*), and if the same physical rotor could realize both C_formal and C_scaled in a consistent observable comparison, its putative energy difference would be

**ΔE_toy = (ℏ²/(2I))(C_formal−C_scaled) = ℏ²/(4M ℓ_*²)**,

independent of D. This is only a formally normalized *two-polynomial* contrast: C_formal is not an ordinary closed SU2 Casimir for the q2 physical carrier and no field action selects it. The kinetic coefficient Mℓ_*² remains completely free; rescaling ℓ_* changes the gap by λ⁻² while preserving every factor parabola/null-cone/Casimir identity. No absolute physical clock, mass or gravitational G follows.

A shell-wise **central** energy gap by itself gives relative phase only if physically coherent sectors and a phase-sensitive interference coupling exist; it cannot cause within-shell J± transitions by itself. In particular a global phase in a single sector is unobservable. The rest/product circle can *motivate* an inertia candidate but does not yet establish a rest mass relation or canonical symplectic form.

## Verdict / next gate / verification

**Positive:** The candidate quarter rest/product circle has R_rest,q²=j_q, and it converts the formal-vs-co-scaled quarter Casimir gap into the universal **1/2** under the proposed rest-radius normalization. This refines the user's insight while resolving much of the earlier apparent kinetic drift.

**Negative:** That 1/2 is an exact relation between **two existing quadratic definitions**, and the formal version is not a closed ordinary SU2 Casimir on the 2D-node quarter carrier. We have NOT derived a different gravitational mass, a new physical Casimir, a kinetic field action or an experimentally distinguishable EM/G relative phase.

**Reproducer:** `research-notes/k4_rest_product_quarter_casimir_bridge_v15_972.py`, commit cc54ea71eb7aba2786de7edf69723fb2a12a3a47. Local SymPy independently checked exact symbolic formulas and full co-scaled SU2 matrices D=2..8, plus D=2..100 scalar shell spectrum; PASS. Independent Audit pending.

**NEXT:** Test whether the *action-circle* phase space has a canonically supplied symplectic two-form whose reduction selects q2's actual kinetic normalization. Compare the EM N=D−1 Schwinger action with q2 N=2D−1 at the same geometric D, without conflating product circle length, spin-label spacing, and Planck action units. If the period/action form requires a free coefficient, report an exact negative selector.

**HANDOFF Audit/Muse:** check P_q=j_q at fixed D, closed q2 Casimir normalization and exact 1/2 difference, source of formal-original-step boundary defects, the two different dimension counts D vs 2D, and the conditional rotor energy units.
