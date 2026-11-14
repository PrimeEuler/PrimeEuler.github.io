# Cone Derivation Ledger v15.979 — Source-normalization gate: exact rank-1/rank-2 intersector response ratios are ordinary Clebsch–Gordan theory

**Date:** 2026-11-14 US Eastern. **Track:** Gravity. **User:** continue from v15.976 toward a physically distinguishable rank-1 EM / rank-2 tidal response. **Parents:** v15.524/525 Wigner–Eckart tidal control; v15.703 TT tidal rank-2 normalized eigenvalue triple; v15.908 EM/tidal Schwinger control; v15.937–938 hydrogen quadrupole and quarter carrier no-intertwiner; v15.973–976 shared-D two-closed-sector action spheres, relative Hopf charge, angular tensor selection and Spin(4)/Taub–NUT limitations. **Latest independent Audit Round 579, canonical v15.977, commit 907fc92**, confirmed v15.967–976 mathematics but found v15.969 original script bare SymPy equality defect. **Repair before this write:** additive corrected script `research-notes/k4_casimir_difference_kinetic_sector_phase_v15_978_audit_repair.py`, commit ec0ca7a139d16dd9a280b3f2fc2038c0b936bdab; original remains unchanged. **Immediately prewrite master HEAD:** ecf2e9a15f92ad65bebce04827ff6171d1500eb9; target absent. Strictly additive; no Audit, Sandbox, frozen Suzuki or preexisting certified objects edited.

**Status:** [D] exact rank-1/rank-2 angular CG response tables, ratios and polarization sums; [N] none distinguish Cone from ordinary SU2 or fixes the reduced field coupling; [C] physically interpreting oscillator pseudospin as a common genuine SO(3)/SU2 rotation and a field tensor source; [O] independent field action, state identification, frequency, experimentally distinguishable gravitational/tidal observable.

## Gate 774 — allowed rank-1 and rank-2 transitions, full matrix-element normalization

At the chosen common outer diameter D=n+1≥2, compare ordinary Schwinger EM spin `j_e=(D−1)/2` with closed co-scaled quarter spin `j_q=(2D−1)/2` in *ordinary* SU2 units; `j_q−j_e=D/2`. The proposed physical tensor T^(k)_q of integer rank k obeys

**<j_q,m'|T^(k)_q|j_e,m> = g_k <j_e,m;k,q|j_q,m'>**, with m'=m+q,

where g_k is an unknown reduced dynamical coefficient and an overall Wigner–Eckart normalization has been absorbed in its definition. For k=1,2 the CG triangle and integer-spin parity permit **(D,k)=(2,1),(2,2),(4,2)** only, exactly as v15.975 already found. In particular, every odd D is forbidden under a *common physical SU2 and integer tensor* premise. This selection is a standard rank rule, not a novel field effect.

The readout is an on-resonance or equal-line-shape normalized transition strength |g_k|²|CG|² for a prepared initial m and chosen field polarization q. Physical transition rates also depend on the driving spectrum, state occupation, detuning, and density of final states. Comparing different m values cancels |g_k|² only if the **same** reduced source and spectral normalization truly applies.

## Gate 775 — exact q=0 profiles and zero-parameter ratios

For an axial (q=0) source, exact CG coefficient squares are:

**D=2, k=1, j_e=1/2→j_q=3/2:** m=−1/2,+1/2 each **2/3**.

**D=2, k=2, j_e=1/2→j_q=3/2:** m=−1/2,+1/2 each **2/5**.

**D=4, k=2, j_e=3/2→j_q=7/2:** at m=(−3/2,−1/2,+1/2,+3/2), values **(2/7,18/35,18/35,2/7)**.

At D=4 the inner-to-outer axial transition-strength ratio is

**(18/35)/(2/7)=9/5**,

independent of g_2, but it is *exactly the standard Clebsch–Gordan number*. The D=2 axial pair ratios are 1. No new Cone-specific response survives dividing out the same reduced amplitude. This is a useful null-test target: a new sourced theory would have to change a fully specified observable ratio compared to 9/5 or predict a separate energy/phase shift without arbitrary model coefficients.

## Gate 776 — polarization-complete benchmark

The standard CG orthogonality relation implies, for every allowed (D,k) above and every initial m,

**sum_{q=−k}^k sum_{m'} |<j_e,m;k,q|j_q,m'>|² = (2j_q+1)/(2j_e+1)=2**.

Here m'=m+q, so there is at most one m' per q. Exact evaluation for D=2..19 and k=1,2 passes, with disallowed pairs having all coefficients zero. The universal 2 is the ratio of the **chosen carrier dimensions** 2D/D, a standard SU2 completeness identity, not a new gravity kinetic-energy ratio, amplification mechanism or free energy. The sum over polarizations is not a guarantee that an actual gravitational wave excites all q equally: TT radiation carries specific helicities and geometry, so a physical detector must project to those components and supply field amplitudes.

## Gate 777 — physical status and the next discriminant

No canonical map equates the abstract Schwinger **oscillator** pseudospins with physical spacetime angular momentum or gravitational wave helicity. Even if one assumes such a map, the allowed matrix-element patterns and 9/5 ratio are entirely standard. The actual linearized tidal Hamiltonian `H_tid=−(1/2)R_{0i0j}Q^{ij}` (with sign/conventions/factors dependent on proper definition of the quadrupole coordinate) is a rank-2 spatial tensor built from physical position in a Fermi normal frame, **not by default** the abstract quarter-grid `J^2` Casimir. The old hydrogen physical comparator v15.937 already ruled out a single universal proportionality between physical `x_i x_j` and the bicone auxiliary `A_i A_j` across its three channel blocks. The relative Berry/Hopf Chern degree D and formal quarter Casimir are not yet sourced contributions to this detector coupling.

**Reproducer:** `research-notes/k4_rank12_response_CG_v15_979.py`, additive commit **ecf2e9a15f92ad65bebce04827ff6171d1500eb9**. Actually executed Python/SymPy exact Wigner CG profiles and full polarization sums for D=2..19; PASS. Independent Audit pending. **Audit repair:** `research-notes/k4_casimir_difference_kinetic_sector_phase_v15_978_audit_repair.py`, commit **ec0ca7a139d16dd9a280b3f2fc2038c0b936bdab**, fixes only the reported assertion equivalence and retains original v15.969 for provenance.

**Verdict:** The fully normalized angular response is calculable and yields an **exact negative Cone novelty test**. There is no physical EM→G transition predicted at D=2 or 4 until an interaction Hamiltonian, cross-sector state carrier and field source are supplied; allowed CG numbers are necessary symmetry factors only. No experimental G-free observable, frequency or dynamical mass is newly selected.

**NEXT:** If any existing model supplies a *source-derived* modification beyond Wigner–Eckart, evaluate the same ratio under a fixed physical drive and matched detuning. Otherwise return to physically accessible rank-2 Fermi tidal strain response: derive a physical stiffness/detector susceptibility and test which combinations cancel amplitude and stay different from ordinary Maxwell/GR, with one unambiguous definition of the detector coordinates. Report a negative when all remaining coefficients are freely assigned.

**HANDOFF Audit/Muse:** verify D=4 9/5 CG ratio and full-polarization strength 2, meaning of unknown g versus a true field tensor, the exclusion of pseudospin↔spacetime angular momentum without an additional map, and exact v15.969 repair after Round 579.
