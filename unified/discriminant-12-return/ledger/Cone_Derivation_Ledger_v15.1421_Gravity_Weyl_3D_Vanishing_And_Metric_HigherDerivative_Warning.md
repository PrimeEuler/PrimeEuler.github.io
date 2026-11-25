# Cone Derivation Ledger v15.1421 — Full Weyl requires 3+1 spacetime and metric variation carries higher derivatives

**Date:** 2026-11-24 Eastern / Nov 25 UTC. **Gravity/Cone.** **Status:** [EXACT NEGATIVE] the Weyl tensor vanishes identically in a truly 2+1-dimensional spacetime, so nonzero `C F B` Weyl coupling cannot be faithfully obtained by a strictly 2+1 Lorentzian theory; [STRUCTURAL WARNING] the curvature operator includes second metric derivatives contracted with first derivatives of Maxwell and H² sigma fields, and its metric/Maxwell variational equations contain higher derivatives before possible gauge/field-redefinition/constraint cancellations; [NOT PROVEN] ghost, fatal causality failure, or impossibility of consistent effective theory; [OPEN] full 4D metric variation, Bianchi/Noether identity, EFT order reduction, cutoff, and quarter selector. Additive; existing 1+1 frozen-tidal numerics remain valid for their stated reduced action, not automatically for the full Weyl-Einstein system.

## Gate 1364 — tensor dimension matters

For a three-dimensional spacetime (not the two-dimensional target H², which is a different mathematical space), any Riemann tensor is entirely determined by its Ricci tensor. In an orthonormal Euclidean test frame for the algebraic identity, define `P_ij=Ric_ij−(R/4)g_ij` and

`R_ijkl=g_ik P_jl−g_il P_jk−g_jk P_il+g_jl P_ik`.

Substituting into the dimension-3 Weyl definition gives `C_ijkl=0` identically for **every** symmetric Ricci matrix. Signature-independent algebraic identity; Minkowski Lorentzian 2+1 has the same vanishing Weyl. This does not prevent nonzero Weyl in 3+1 from being sampled on a lower-dimensional plane or a physically *externally prescribed* tide. It forbids interpreting a standalone genuinely 2+1 gravitational metric as a source of this operator.

The v15.1415–1417 local 1+1 Hamiltonian simulations were **explicit frozen-curvature reduced theories**, not full Weyl dynamical field equations. This is another reason an actual 3+1 metric/gravitational wave is required before claiming a self-consistent gravitational mechanism.

## Gate 1365 — high-derivative metric variation warning

The action `S_int=−(g/2)∫sqrt(-g) C_{μνρσ}F^{μν}B^{ρσ}` contains the spacetime curvature C and thus **second derivatives of the metric**. Although a term is linear in curvature, its variation contains a double covariant derivative acting on its Riemann derivative `P^{μανβ}=∂L_int/∂R_{μανβ}`, which is a Weyl-symmetry projection of `F^{μν}B^{ρσ}`. Differentiating P can produce **third derivatives** of the Maxwell vector potential A and of the scalar target fields. Varying A likewise brings derivatives of the Weyl tensor, which contain up to third derivatives of the metric before gauge identities. This requires an actual constrained EFT analysis; the minimal Maxwell second-order equations in a *fixed external* C from v15.1385 are not the full dynamical problem.

As a transparent **representative index-component derivative-order check**, take a local quadratic interaction density `L=λ h''(t) A'(t) B(t)`. Its Euler–Lagrange contributions are `E_h=λ(A' B)''` and `E_A=−λ(h''B)'`, both allowing third derivatives. This test is a **structural warning only**: a full Weyl contraction, Bianchi identities, on-shell field redefinitions, Einstein constraints and EFT order reduction might eliminate or rearrange some higher-order terms. It is NOT a proof of a propagating Ostrogradsky ghost or fatal causality pathology.

**Actual independent local exact SymPy** `/mnt/data/cone_gate/k4_weyl_dimension_metric_variation_v15_1421.py` verified 3D Ricci reconstruction and all 81 Weyl components vanish for generic Ricci, plus both illustrative Euler–Lagrange derivative-order identities, PASS. **New additive GitHub source** `research-notes/k4_weyl_dimension_metric_variation_v15_1421.py` SHA **0436c34de264eeebb59aa31695db08aae226bc3c**, exact committed-byte Audit replay pending.

**AUDIT:** rederive 3D Weyl identity in Lorentz signature, verify general metric variation tensor P and distinguish potential total divergences from independent higher-derivative dynamics. Work out whether Weyl-F-exact-H²-area is redundant under **general on-shell EFT** field redefinitions, not just the earlier simplest Maxwell potential shift. Do not claim an entirely novel operator. Test a fully covariant background and gauge-fixed principal symbol with metric/sigma/EM constraints.

**NEXT:** the energy exchanged with a prescribed time-variable tidal metric cannot be balanced inside EM+sigma alone; derive the explicit source work identity, then add dynamically evolving Einstein metric and gravitational energy accounting. v15.1422 isolates the source-work issue.
