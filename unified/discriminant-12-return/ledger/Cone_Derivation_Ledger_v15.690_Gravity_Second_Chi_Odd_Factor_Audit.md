# Cone Derivation Ledger v15.690 — Gravity lane: second chi-odd-factor audit for seeded cavity conversion

**Date:** 2026-11-11 US Eastern. **Parents:** v15.628 auxiliary compensator construction; v15.646 supermonopole half-charge ladder; v15.647 Taub–NUT KY/Dirac charge-preservation result; v15.680 static-magnetic-seed cavity conversion; v15.689 seeded-cavity sector-parity theorem. **Status:** [D] classification of the three strongest candidate second chi-odd factors from the existing ledger; [N] no independently derived physical second chi-odd factor in the actual Taub–NUT/EM cavity system; [C] supersymmetric supermonopole ladder gives the right charge step only on an enlarged carrier; [O] a source-derived physical compensator/intertwiner and normalization. **Immediately prewrite live HEAD:** 9eae060b47a923a42b25ec9b06a18a5c98be409d. Collision searches found no v15.690 or prior “second chi-odd” ledger entry. Frozen Suzuki/far-tail objects untouched.

## Gate 245 — static magnetic seed is ordinary EM and therefore not the missing odd compensator

The seeded cavity source of v15.680 is

**(partial_t^2-partial_z^2)a_y = 2 B0 partial_z b.**

The prepared B0 is an ordinary electromagnetic background field. Under the current q=2 sector dictionary, ordinary EM belongs to the **chi=+** subspace. No earlier ledger entry assigns the static magnetic bias a chi-odd transformation law or a quarter-sector charge.

Therefore the external magnetic seed cannot be promoted to the second chi-odd factor merely because it multiplies the gravitational perturbation in Maxwell’s equation. Under the current sector assignment it is chi-even.

If a gravitational quarter-rung W_G were chi-odd, then “W_G times ordinary B0” remains chi-odd at the sector-algebra level unless B0 is represented by an additional operator that is itself independently shown to flip chi. No such representation has been derived.

Thus the ordinary inverse-Gertsenshtein magnetic bias solves the **physical EM seeding problem** but does not solve the **Cone sector-parity compensation problem**.

## Gate 246 — the v15.628 compensator works algebraically but is explicitly postulated

v15.628 constructed an auxiliary two-state system with lowering tau_- and

**H_int = g W tensor tau_- + g* W^dagger tensor tau_+.**

This makes the combined conserved charge work while W changes the subsystem grading. It is an exact existence proof that an additional compensating degree of freedom can turn an otherwise forbidden odd transition into a symmetry-compatible composite interaction.

However v15.628 is explicit that:

- the auxiliary system is externally postulated;
- its charge assignment is chosen;
- the coupling g is arbitrary;
- no relation to a photon, graviton, Newton G, Taub–NUT source or concrete field was derived.

Therefore this compensator cannot be used as the missing physical second odd factor without adding precisely the dynamical input the Cone program is trying to derive.

## Gate 247 — Hasebe’s charge-changing supermonopole ladder has the right step, but not the right physical carrier

v15.646 found the strongest positive external analogue. Hasebe’s fermionic supermonopole operator changes

**Delta g = 1/2.**

Under the conditional dictionary

**g = s_TN = 2 p_TN,   p_TN=k/4,**

this gives

**Delta k=1, Delta p_TN=1/4.**

So it realizes exactly one gravitational pair quantum per step and requires a spinorial/graded carrier, which is structurally compatible with the need for an odd factor.

But v15.646 also proved that the map acts in an enlarged **UOSp(1|2) super-Landau/supersphere Hilbert space**. A charge-changing map L_k→L_(k+1) needs a nontrivial degree-one bundle coefficient; it is not a constant scalar operator on the ordinary Taub–NUT carrier.

v15.647 then checked the actual Taub–NUT Dirac/Killing–Yano symmetry operators and found

**[P_4,Q_KY]=0.**

They preserve the Taub–NUT fiber charge k. The simple local phase e^(i psi) shifts k but is not by itself a globally defined scalar intertwiner, and a k→k+1 operator on fixed-l Lorentzian time modes changes energy by

**Delta E=hbar c/(4l).**

Therefore the existing physical Taub–NUT symmetry operators do **not** supply Hasebe’s charge-changing odd factor.

This leaves the supermonopole ladder as a useful representation-theoretic existence proof, not a sourced gravitational cavity ingredient.

## Gate 248 — no existing second odd factor closes the seeded-cavity Cone interaction

Combine v15.689 with Gates 245–247.

To produce an ordinary EM→EM seeded cavity response using a chi-odd gravity rung, the effective interaction must be chi-even. The simplest route is a product of two chi-odd factors.

The three best existing candidates fail for distinct reasons:

1. **Static magnetic seed B0:** physically real, but ordinary EM/chi-even under the current dictionary.
2. **v15.628 auxiliary compensator:** algebraically chi-compatible, but introduced by hand with arbitrary coupling.
3. **Hasebe supermonopole charge ladder:** carries the right quarter-pair step on an enlarged supersymmetric carrier, but is not realized by the ordinary Taub–NUT KY/Dirac dynamics and lacks a sourced cavity coupling.

Therefore there is currently **no independently derived physical second chi-odd factor** that turns the q=2 sector parity into a nonzero seeded EM cavity transition.

## Verdict

This closes the present **Cone-specific seeded-cavity parity branch** at the representation-theoretic level:

**[D]** Ordinary seeded cavity conversion remains valid conventional curved-spacetime Maxwell physics.

**[D]** The q=2 Cone grading gives an exact sector selection rule.

**[D]** A single chi-odd quarter-rung cannot connect ordinary EM states.

**[N]** No second physical chi-odd compensator has been derived from the static magnetic seed, standard Taub–NUT symmetries or existing Cone operators.

**[C]** An enlarged spinorial/supersymmetric carrier can realize the required odd charge step, but importing it would be new model structure rather than a result already forced by the Cone.

This means the cavity exploration has now cleanly separated conventional detector engineering from the unresolved Cone physics. The remaining missing object is no longer vague: it is a **globally defined, source-derived, chi-odd gravitational/charge intertwiner with fixed normalization** whose composite with another independently derived odd factor acts within the EM sector.

Absent that object, neither the quarter-grid 2:1 pump picture nor the quarter-parity seeded-conversion picture is a new Cone prediction.

**Reproducibility:** this gate reuses the exact matrix projector identities of research-notes/seeded_cavity_chi_vs_spatial_parity_v15_689.py and the previously independently checked bundle/charge commutators of v15.646–647. No new numerical approximation is introduced.

**HANDOFF:** external audit/gravity/sandbox should verify only the classification step: whether the current sector dictionary indeed makes the static magnetic bias chi-even; whether any existing physical Taub–NUT operator was missed that changes k by one; and whether any earlier Cone operator already supplies a second odd factor with fixed normalization. Any such counterexample reopens the branch.

**NEXT:** return to the gravity program’s core observable criterion. Inventory the surviving genuinely dimensionless, G-free results after closing the two cavity-specific Cone shortcuts: (i) q=2 sector parity; (ii) welded half-scale counting resolution; (iii) Taub–NUT quarter-pair quantization; (iv) K4 tensor dispersion, now known to be cosmological-scale. Test whether any **ratio or topological phase built solely from these certified objects** distinguishes gravity from EM without requiring a new coupling operator. If not, record the gravity lane’s present frontier as “representation/topology established; local interaction selector still missing.”
