# Cone Derivation Ledger v15.639 — Lane A: bicone exchange parity is not the quarter-mesh EM/gravity Casimir parity

**Date:** 2026-11-10. **Parents:** v14.863 bicone Larmor angle; v14.869 KS so(4) scalar/triplet; v15.544 AMGM4/V4 bicone quarter rank-two consolidation (corrected by Audit Round 516); **v15.572 exact j=3/4 bicone encoding and its independent Audit Round 517 v15.575**; v15.625–628 all-mesh Casimir parity; v15.630 standard rotor SU2 obstruction; v15.637 physical Taub–NUT worldline only sees an Abelian monopole line; v15.638 External Audit Round 527 (confirms v15.636–637). **Status:** [D] exact grading and dynamics algebra; [C] comparison of physically distinct carrier labels; [O] physical EM/G intertwiner and coupling. **Immediately prewrite HEAD:** e1b30e89b69827a59285297bcfd9d4b54c7b3cc6; filename collision search negative. Additive only; no Suzuki or certified production objects touched.

## Redundancy check (important)

The precise four-state **j=3/4 defective quarter-ladder representation in the tensor algebra of two spin halves is ALREADY PROVED in v15.572, §1 and independently checked by v15.575.** In ordered basis (++,+−,−+,−−), that entry establishes
M_z=−J_{1z}−J_{2z}/2, J_+^q=√(3/2)(σ_-⊗I), D=−A_z, E=A_z²/2=diag(0,1/2,1/2,0).
The present reproducibility script independently rechecks these, but they are explicitly **not new** and do not furnish a physical SU2 intertwiner. v15.572's general odd-quarter rank-two boundary theorem is also preserved and not duplicated.

## Gate 149 — distinct gradings: bicone spin swap versus geometric shell Casimir

On the KS-glued spin-1/2×spin-1/2 bicone, define L_i=J_i^(1)+J_i^(2), A_i=J_i^(1)−J_i^(2), and physical spin-exchange S|a,b>=|b,a>. It is a self-adjoint involution, S²=I, with eigenspace multiplicities (+1)^3 (triplet L=1), (−1)^1 (singlet L=0). Directly **[S,L_i]=0 and {S,A_i}=0**. Hence A_i is *naturally odd under constituent-swap*, and has actual scalar/triplet matrix elements. This is a genuine internal bicone parity, not an external invented grading.

The prior q=2 geometric mesh uses χ_geom=exp(16πi C_geom), C_geom=j(j+1), with χ=(-1)^Lmesh when j=Lmesh/4. For the physical bicone *rotational* spin j=0 (singlet) or j=1 (triplet), the corresponding mesh indices are Lmesh=0 or 4 and **χ_geom=+I4**. Conversely a single fixed odd-quarter geometric j=3/4 shell has χ_geom=−I4 on all four of its magnetic nodes. Therefore **neither** grading can be identified with the bicone S, whose trace is 2, as χ=+I has trace 4 and χ=−I has trace −4. Traces/multiplicities are invariant under unitary change of basis, so no grading-preserving unitary intertwiner exists between these specified choices. This prevents treating scalar↔triplet A_i transition as EM↔odd-quarter sector exchange just because both use four states.

This is a scoped statement about the source-faithful spin labels, not a prohibition against new graded carriers or a separately specified map.

## Gate 150 — rank-two quadrupole is swap-even

The existing bicone quadrupole Q=A_x²−A_y²=(A_+²+A_-²)/2 obeys **[S,Q]=0** as a direct consequence of S A_i S=−A_i. In the spin-half⊗spin-half example, Q annihilates the singlet and has zero singlet↔triplet matrix elements. The previously established exact identity [L_+,[L_+,E]]=A_+² (v15.544/v15.572) does not change this grading: it transports a bicone operator inside the swap-even algebra, not between geometric EM/G Casimir classes. The independently audited 5/2 normalization to projected rank-two rotor from v15.544 remains a representation-specific matrix conversion, not a coupling strength.

## Gate 151 — simple Larmor exchange dynamics does not select an EM/G interaction

The existing orientational model uses **chosen** exchange H_ex=−λ J1·J2 (v14.863 and v14.869). This preserves S and yields energy 3λ/4 on the singlet versus −λ/4 on triplets. Adding a **chosen** relative driving source γ A_z gives in the (singlet, triplet m=0) basis

**H2=[[3λ/4,γ],[γ,−λ/4]], energy splitting Δ=√(λ²+4γ²).**

Thus bicone A_z can produce a genuine singlet–triplet response, while the static exchange alone cannot mix the two. But γ/λ remains free; neither coefficient follows from the cone geometry or Taub–NUT mass–NUT pair. Moreover the mixed states remain entirely in ordinary physical spin 0,1 and still have χ_geom=+1, so this is not an odd-quarter geometric transition. Even if γ≠0, there is no derived EM/G force or distinctive gravitational number.

## Verification and next gate

Exact SymPy reproducer **research-notes/bicone_exchange_vs_casimir_gate_v15_639.py**, created at commit e1b30e89b69827a59285297bcfd9d4b54c7b3cc6 and executed successfully in local Python. It checks S grading multiplicities and commutators, rank-two parity, exact H2 and its gap, and re-verifies old v15.572 matrices for provenance. No new image generated; frozen Suzuki untouched.

**Verdict:** The bicone provides a source-faithful relative operator odd under swap parity, but the swap parity is spectrally different from the quarter-mesh Casimir parity and **does not implement the required EM↔G odd-rung operator**. The earlier exact two-spin *matrix* encoding is real and already certified; the missing physical identification remains a missing representation map, not missing 4×4 algebra. No independent coupling, Newton G or novel G-free tidal response found.

**HANDOFF:** external-audit, gravity, sandbox; status open. Verify S=swap on two spin halves, [S,L]=0/{S,A}=0, fixed geometric χ=±I versus S trace/multiplicity obstruction, Q rank-two evenness, two-level H gap, and correct attribution to already audited v15.572. Do not infer a no-go for all extended representations or any physical EM↔G transition.

**Next gate:** inspect the *actual* phase/number carrier of the original moving bicone and any constraint linking internal swap to quarter-mesh shell index. If none is present, cease attempts to infer it from dimension matching and test original cone field equations for a parameter-free observable directly.
