# Cone Derivation Ledger v15.651 — Gravity lane: spinor twist cancels unit monopole-charge obstruction and gives an exact lowest-multiplet bridge

**Date:** 2026-11-10. **Parents:** v14.731–732 Taub–NUT mass–NUT pair and monopole angular charge; v15.625–628 geometric quarter Casimir and its characters; v15.630 physical SU2 distinction; v15.632 true integer monopole bundle winding; v15.646 Hasebe fermionic half-charge ladder comparator; v15.647 standard Taub–NUT Killing–Yano symmetries preserve fiber momentum. **Status:** [D] global CP1/S² bundle equivalence, monopole Dirac index and SU2 lowest-multiplet intertwiner, precise two-step obstruction; [C] physical scalar-to-chiral-spinor carrier extension and choice of compatible round-sphere connections; [O] Lorentzian Taub–NUT matter source, complete charge-raising dynamics, G and a novel gravity response. **Live prewrite HEAD:** 3ff77e2d3adea6f6733a6622c5971b3daf3dd2f9; search for v15.651 and overlap empty. Historical v15.633/v15.640 numbering collisions preserved; no old entry touched. Suzuki production, certified objects, and parked physical Suzuki-quarter weld untouched.

**Source comparison:** Rogelio Jante & Bernd Schroers, *Dirac operators on the Taub-NUT space, monopoles and SU(2) representations*, JHEP 01 (2014) 114, DOI 10.1007/JHEP01(2014)114 (the 4D normalizability question explicitly involves an additional abelian self-dual gauge potential); standard twisted S² Dirac monopole index/zero-mode theorem, e.g. *On Monopoles with Arbitrary Symmetry*, Appendix A.4, and the standard CP1 spin bundle construction. These are standard mathematical facts; the following cross-carrier application is an independently checked comparison, not a new index theorem.

## Gate 167 — chiral spinor cancels the unit Chern-class mismatch exactly

On oriented round S²≅CP1, denote the ordinary monopole line bundle by **L_k=O(k)**, c1=k, and use the standard spin structure with chiral spinor lines **S⁺=K^(1/2)=O(−1)** and **S⁻=O(+1)** (orientation/chirality names can be reversed consistently). The scalar charge-changing hom bundle is **Hom(L_k,L_(k+1))≅L_1**, c1=+1, so no nowhere-vanishing scalar zeroth-order isomorphism exists (v15.646–647).

However, the spinor-valued target is different:

**S⁺⊗L_(k+1)=O(−1)⊗O(k+1)=O(k)=L_k,**
**Hom(L_k,S⁺⊗L_(k+1))=O(0)**.

Thus there **is** a nowhere-zero smooth global scalar-to-*charged-chiral-spinor* bundle map for every k, without an additional fourth-root bundle. The spinor factor supplies precisely the extra transition e^(−iφ) needed to cancel the charge-changing e^(+iφ). For the standard compatible unit-charge Dirac monopole connection and round-sphere chiral spin connection, the local connection one-forms can be chosen opposite; the map can be a covariantly constant unit isometry. **Physical usage of an extra spinor field is an input**, not a field established in the original Taub–NUT worldline model. A parallel isometry is determined up to a constant U(1) phase once bundle, metric, connection and equivariance are fixed, but its coefficient in a Hamiltonian is not determined.

## Gate 168 — twisted Dirac zero modes identify exactly with scalar lowest Landau/rotor multiplet

For **k≥0**, the S² chiral Dirac operator twisted by charge-(k+1) line bundle has

**ind(D⁺_(k+1))=k+1**, **dim ker D⁺_(k+1)=k+1**, **dim ker D⁻_(k+1)=0**,

in the chosen chirality convention. The positive-chiral bundle is S⁺⊗L_(k+1)=O(k); its normalizable zero modes are the holomorphic polynomials of homogeneous degree k, i.e. H⁰(CP1,O(k)). The original charge-k **scalar monopole lowest-angular-momentum space** is the same H⁰(O(k)); each is the unique SU2 spin j=k/2 irrep of dimension k+1. Thus

**B_k : H_scalar,lowest(L_k) ≅ ker D⁺_(k+1)**

is a *global SU2-equivariant unitary intertwiner* once compatible normalizations are chosen. In a common normalized polynomial basis (r=0,...,k) the operator can be represented by the identity and the usual ladder weights **(J_+)_(r+1,r)=sqrt((k−r)(r+1))**. No quarter-spin obstruction applies because the **target is a spinor**, which compensates the change in monopole charge's rotational central sign. This refines the scoped scalar-to-scalar obstruction of v15.646, without contradicting it.

The k=0 map sends the scalar charge-0 constant state to the unique twisted charge-1 positive-chirality Dirac zero mode; k=1 maps the two spin-1/2 scalar lowest states to the two charge-2 Dirac zero modes. Their angular spin j is unchanged in the one-step map.

## Gate 169 — physical Casimir preservation; no geometric quarter-Casimir identification

The actual angular representation on both sides of B_k is j=k/2, with **C_phys=k(k+2)/4**. The separate geometric q=2 shell assignment for the same integer k is j_geom=k/4, **C_geom=k(k+4)/16**, differing by **k(3k+4)/16** for k>0. Therefore the genuine topological + spinorial monopole-charge bridge **does not** yield the Cone odd-quarter angular Casimir. It raises **pair charge p=k/4** to p+1/4 only under the conditional v14.731 identification and simultaneously changes field species, while preserving actual angular j. At k=1, original scalar minimum j=1/2 and spinor target charge k+1=2 still j=1/2 (C=3/4), not 5/16.

## Gate 170 — a one-rung bridge does not automatically square into an all-up scalar/spinor ladder

The natural next map in a naive alternating tower would send **S⁺⊗L_(k+1)→L_(k+2)**. Its homomorphism line is **Hom(S⁺⊗L_(k+1), L_(k+2))=O(2)**, with first Chern number +2, so no nowhere-zero smooth scalar bundle isomorphism gives the second upward step. Likewise the zero-mode dimensions of the next *ordinary scalar* charge-(k+2) lowest multiplet are k+3, while those of the spinor target at k+1 are k+1, so a unitary full-multiplet map cannot occur without further state content. This is a scope-limited obstruction to this **specific scalar→chiral-spinor→scalar alternation**, not a general impossibility of differential charge ladders, higher-spin tensor targets or a larger SUSY representation. In particular it does not reconstruct Hasebe's full fermionic UOSp(1|2) algebra or his fixed-superspin coefficients by itself.

## Gate 171 — S² angular bridge is not a complete physical Taub–NUT transition

The Jante–Schroers 2014 paper studies **normalizable zero modes of a four-dimensional Euclidean Taub–NUT Dirac operator coupled to an additional abelian gauge field with self-dual curvature**. Its relation to S² monopole zero modes supports the angular-sector comparison, but **S² zero modes alone do not establish 4D radial normalizability**, a native Lorentzian worldline Dirac carrier, or an actual charge-changing TN symmetry. At fixed l the Misner time Fourier shift k→k+1 requires ΔE=ℏ c/(4l), so the would-be physical operator is *spectrum-generating* and cannot commute with the unchanged Hamiltonian. Any scalar↔spinor transition also requires physically permitted fermionic parity/source structure and a nonzero interaction coefficient; neither is dictated by the original cone/monopole geometry.

**Main verdict:** A new *specific, globally defined mathematical angular bridge* does exist: the positive-chiral spinor contribution of degree −1 exactly cancels the charge +1 monopole twist, identifying charge-k scalar lowest states with charge-(k+1) twisted Dirac zero modes, SU2-equivariantly. It is the first source-standard bundle-based step here that circumvents the earlier scalar charge-change obstruction *without postulating arbitrary fractional holonomy*. It still does **not** realize a full repeated quarter-rung operator, fix its physical coupling or produce the odd-quarter geometric Casimir/novel G-free prediction.

## Verification, record and audit

Exact local SymPy reproducibility archive **cone_spinor_gates_167_171.zip** contains `cone_spinor_gate_167_171/reproduce.py` and `REPORT.md`; script executed successfully. Checks charge-one versus spin-minus-one gauge transitions and curvature, degree-zero and degree-two Hom-bundles, index/multiplet dimensions for k≥0, explicit normalized SU2 Jz,J± matrices, exact Casimir and identity-intertwining up to k=9. SHA256 local producer: c15ff7aab7a5b086b237b8998a4750ba5cd4e1c5c6fda221856d114167801947.

**HANDOFF** target external-audit, gravity, sandbox; independently verify spin bundle chirality conventions O(±1), SU2 equivariance of H⁰(O(k)), index/zero-mode count, curvature cancellation at the round-sphere monopole connection, the exact second-step O(2) obstruction, and distinguish S² angular modes from 4D TN zero modes and real gravitational dynamics. Critically, note this is a *positive one-step result*, not a physical quarter-spin prediction.

**Next gate:** take the specific 4D Euclidean Taub–NUT Dirac separation and radial normalizability in Jante–Schroers (2014) to test whether a single scalar→spinor charge increment survives the full radial operator at fixed asymptotic spinor charge/coupling, and whether existing TN metric or gauge data fixes it. Preserve Euclidean vs Lorentzian distinction.
