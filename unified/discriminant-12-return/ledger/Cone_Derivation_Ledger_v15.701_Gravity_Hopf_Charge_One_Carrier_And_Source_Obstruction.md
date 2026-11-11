# Cone Derivation Ledger v15.701 — Gravity: charge-one Hopf carrier, patching resolved, physical source still missing

**Date:** 2026-11-11 US Eastern. **Parents:** v14.731/732 Taub–NUT quarter-pair; v15.628 formal odd-rung compensator; v15.632 integer Chern charge; v15.646–647 supermonopole versus invariant Taub–NUT Dirac/KY; v15.689–690 cavity sector-parity obstruction; v15.695–696 source/normalization and compact-fiber selection. **External Audit Round 542 (v15.698):** independent confirmation of v15.692–694 and v15.696, with a second SymPy structural-equality reproducibility defect in v15.695. **Status:** [D] exact Hopf bundle/curvature/carrier identities; [D] additive reproducibility repair; [C] conventional two-component charge-one carrier as a possible missing-degree-of-freedom geometry; [N] no independently sourced Taub–NUT field action or coupling/matrix element. **Immediately prewrite live HEAD:** fccf44971e3efdbb8c846b60d56028cfe70e4597. Explicit target file absent; topic search found no prior Hopf charge-one gravity ledger entry. v15.697–700 already occupied by Suzuki and external audit; this entry takes next free v15.701. Frozen Suzuki/far-tail and previous audited files untouched.

## Gate 269 — audit repair without rewriting the failing historical object

Round 542 found that research-notes/maxwell_sector_source_normalization_v15_695.py has a mathematically true but structurally unequal SymPy matrix assertion at its line 27: P(gW)(gW)P versus g² P W² P. The original committed script therefore fails its own PASS claim. The separately added research-notes/maxwell_sector_source_assertion_repair_v15_701.py tests the exact same identity via matrix entrywise simplification/expansion, and locally executes PASS. The historical v15.695 script remains untouched and its failure remains traceable. This repeats the additive rather than silent modification protocol used after Round 541.

## Gate 270 — explicit, globally compatible two-component degree-one Hopf carrier

For northern/southern patches on S² with 0<=theta<=pi, phi periodic, define the local normalized two-component columns

**u_N=(cos(theta/2), exp(i phi) sin(theta/2))^T**,

**u_S=(exp(-i phi) cos(theta/2), sin(theta/2))^T**.

They obey

**u_N=exp(i phi) u_S**, and **u_N^dagger u_N=u_S^dagger u_S=1**.

Thus they provide a two-component unit-charge transition law of degree one, exactly the extra e^(i phi) patch coefficient required for a map between the k and k+1 monopole sectors in v15.646. This construction uses a **rank-two ambient carrier and a degree-one complex line subbundle**, not a globally nonzero scalar section of the nontrivial degree-one line bundle. The two components do not vanish simultaneously, while each individual scalar component has a pole zero.

The patch-independent projector

**Pi=u_N u_N^dagger=u_S u_S^dagger**, **Pi²=Pi**, **tr Pi=1**

is a globally defined ordinary 2-by-2 field. The projector is geometric and carries no physical coupling by itself. The sign of the Chern class below tracks the stated transition/orientation convention.

## Gate 271 — monopole curvature and integer first Chern number are recovered exactly

Define the local Berry/U(1) connections with the convention

**A_N=-i u_N^dagger d u_N=(1-cos theta)dphi/2**,

**A_S=-i u_S^dagger d u_S=-(1+cos theta)dphi/2**.

Then

**A_N-A_S=dphi**,

**F=dA_N=dA_S=(sin theta/2)dtheta wedge dphi**,

**(1/(2pi)) integral_(S²) F=1**.

This independently reproduces the unit-Chern patch requirement of v15.632 and the L_1 bundle coefficient needed by v15.646. It shows a concrete global **two-component representation** is geometrically available, so the earlier objection was specifically to a nowhere-zero globally scalar charge-step coefficient, not a ban on all charge-changing fields.

It does not, however, identify u with a physical Taub–NUT fermion or metric perturbation. The Hopf spinor is conventional geometry; patch compatibility is only a necessary prerequisite, not a derivation of matter dynamics.

## Gate 272 — unit bundle normalization does not determine interaction strength

If an independent physical field action supplied a charge-one source whose normalized angular part were u, then its source magnitude/coupling would still be a separate parameter. For a toy operator W_g=g u, its squared norm is

**W_g^dagger W_g=|g|²**,

with arbitrary g. The geometric unit normalization u^dagger u=1 cannot force g=1 because g has the physical dimensions/normalization fixed only by the missing action and its canonical field normalization. In particular, the construction does not provide the entire globally defined spinor/bundle field equations, the scalar/spinor contraction of a charge-changing interaction, a physical excitation and readout, or an experimental gravitational/EM coupling coefficient.

The standard Taub–NUT KY/Dirac symmetry operators previously tested are still fiber-invariant and conserve k; the present explicit Hopf spinor is not a new invariant KY operator. A dynamical noninvariant charge-one source and its globally patched interaction must be added and justified independently.

## Gate 273 — frontier verdict

**[D] Positive geometric result:** a normalized two-component charge-one Hopf carrier with the correct Chern winding and patch-invariant projector exists. This resolves the elementary *existence* issue for a globally compatible charged carrier and sharpens the target to dynamics, rather than claiming all possible charge-changing maps are topologically forbidden.

**[N] Physical result not yet obtained:** no source-derived Taub–NUT/K4 field action fixes the charge-changing interaction and its normalization. There is no newly predicted gravity force, tidal amplitude, G-free local observable or Casimir-frequency selector.

**[O] Next real gate:** determine whether an independently motivated, physically covariant spinor or bundle field action produces the charge-one transition in a fixed Taub–NUT geometry, including its kinetic operator, global patching, conserved total charge, boundary conditions, and canonical coupling. Merely writing an arbitrary Yukawa/spinor perturbation with a free coefficient would show allowance, not a Cone prediction. If the only answer is an unselected source coupling, preserve this geometric lead and return to the separately justified rank-1/rank-2 tidal response program.

**Reproducibility:** additive repair research-notes/maxwell_sector_source_assertion_repair_v15_701.py (commit 9e136f9fed359f51514635b3b742228bb2e4009f); Hopf proof research-notes/hopf_charge_one_source_carrier_v15_701.py (commit fccf44971e3efdbb8c846b60d56028cfe70e4597). Both locally executed to PASS, with mathematical checks for transition law, covariant Berry patches, Chern flux, projector and arbitrary coupling normalization. No image generator, no protected-object modifications.

**HANDOFF:** external audit/gravity/sandbox: re-execute both scripts, check Hopf orientation/convention and global rank-one line embedding carefully, and distinguish the positive existence of a two-component charged carrier from a sourced physical Taub–NUT interaction. Preserve the original v15.695 failing script and confirm the repair fixes only mathematical-equality testing.

**NEXT:** examine the covariant Dirac/spin-c connection on the actual Taub–NUT fibration, not an arbitrary topological doublet. Ask whether fiber-invariant Dirac coupling already produces a k-step (expected no by [P,D]=0) and whether a geometrically mandated non-invariant spinor field exists. If no mandatory source, close the Hopf branch at bundle existence and return to physical tidal rank-1/rank-2 response, with the quarter bridge held as an explicit open hypothesis.
