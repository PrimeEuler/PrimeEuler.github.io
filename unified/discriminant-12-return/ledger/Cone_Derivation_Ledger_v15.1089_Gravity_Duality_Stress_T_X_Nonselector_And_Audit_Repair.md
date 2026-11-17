# Cone Derivation Ledger v15.1089 — Vacuum Maxwell duality preserves the complete gravitational source while swapping T/X field labels; Audit reproduction repair

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Status:** [D] full vacuum Maxwell stress-energy is pointwise invariant under continuous electric/magnetic duality; [N] T/X field-sector sign is not selected by the existing Einstein–K4 gravity source or any sourced scalar/vector/tensor Weyl response based on that stress alone; [D] I1=0 alone does not define radiative null Maxwell configurations; [V, scoped] exact reported v15.1081 source Fourier coefficient survives corrected O(q^4) assertion. **Live HEAD immediately prewrite:** f5978e188ad58ae79374781cf67467507101427e. Strict additive commits, no certified objects, Suzuki, Audit, Muse or Sandbox changed.

## Protocol: latest Audit, Sandbox, and version collision

Latest completed **External Audit Round 591/v15.1087**, commit c3e18f30c1cabcf73777a8e005157e5eebc83886, verified all of Gravity v15.1080, v15.1083, v15.1085 and Sandbox v15.1082, v15.1084, v15.1086. It independently verified the *formula* of v15.1081 including +7q²/25 and -431/(10 ell²), but disclosed an **undocumented failure** in Gravity's original v15.1081 reproducer: the script asserts equality of q²-truncated Fourier functions as exact, missing an O(q⁴) residual -q⁴ c³ M0/4 = -512 q⁴ c³/45045. This is a real executable defect. The historic source remains untouched.

The repair was first deposited under a provisional Gravity v15.1088 script at commit 85d1c734179dcd40f5f537413dc312821121cafc; a separate preliminary duality script was provisionally deposited as v15.1088 at 8fc281a0d8fa7bd95ea24ea34c737672b1061a4b. Immediately before these scripts, however, **Sandbox had already reserved canonical v15.1088** with `Cone_Derivation_Ledger_v15.1088_Sandbox_Charge_Run_Gravity_Cross_Reference`, ledger commit 77e319b4297d732ba8cb7a98291dc33c34ac611b, after payload c7ab83c and b40f811. Sandbox v15.1088 retains its precedence and is NOT edited. Both provisional Gravity v15.1088 scripts remain as history; canonical copies are **v15.1089**:
- `research-notes/k4_compact_maxwell_fourier_tt_jet_v15_1089_audit_fix.py`, commit **11069f30745e5269788c87a37080364d2cadde0a**;
- `research-notes/k4_maxwell_duality_stress_gravity_nogo_v15_1089.py`, commit **f5978e188ad58ae79374781cf67467507101427e**.

The repair changes only the false exact assertion: using q²-truncated F0,F1, residual = -q⁴ c³ M0/4 exactly, and its Taylor series through q³ vanishes. The earlier analytic coefficient and physics are unchanged. The canonical duality script independently ran locally through every check for stress, momentum, dual invariants and counterexample; the repaired assertion itself is an exact rational/SymPy identity and awaits Audit execution of the complete canonical fixed v15.1089 script.

Sandbox's newly arrived v15.1088 cross-reference correctly emphasizes imported standard EM/GR charge-versus-mass tagging and the missing gravity dipole for isolated conserved total momentum, without selecting G or a new K4 source. It calls the EM content sourcing Gravity's TT entries 'the null hinge sector'. **This description is not generally true for the actual compact Maxwell initial packet**: initially B=0 and E!=0 on its support, so I1=E²>0, not I1=0. Even after evolution it cannot be assumed everywhere null; radiation may tend to null far away in relevant regimes. The ledger therefore retains the actual source's pointwise invariants instead of replacing them with a radiation label.

## Gate 913 — exact full EM stress under duality and the K4 source no-go

In units c_light=epsilon0=mu0=1, write a vacuum electromagnetic field E,B and its continuous electric/magnetic duality rotation
E_theta=cos(theta) E+sin(theta) B,
B_theta=cos(theta) B-sin(theta) E.
At each spacetime point, the total energy density, momentum/Poynting density and Maxwell spatial stress are
rho=(E²+B²)/2,
S=E cross B,
T_ij=rho delta_ij-E_iE_j-B_iB_j.
The rotation is orthogonal in the two-dimensional EM duality plane; therefore
rho_theta=rho, S_theta=S, T_ij(theta)=T_ij
**pointwise and exactly for all theta**. The canonical script checks these identities as polynomial expressions modulo cos²+sin²=1 and at 90°, 45° and a 3/5-4/5 rotation.

In source-free Maxwell theory with no electric/magnetic charges, duality is a symmetry of the field equations on any fixed 4D Lorentzian background, and it carries compact initial data into another globally sourceless Maxwell solution. Thus the **entire time-dependent T_munu**, not merely a leading Fourier coefficient, is identical for dual-related solutions. On the coasting K4 background this equality survives the common a_FLRW^-4 orthonormal scaling, and it passes to *every* Fourier component and scalar/vector/tensor decomposition. The linear Einstein–K4 scalar/vector ADM source constraints and TT source receive identical data. With the same gravitational, solid, initial and boundary conditions, the resulting metric/curvature solutions are identical. This is a **conditional source-to-gravity no-go** for using the T/X field sign alone as a new gravitational observable under the existing action. It does NOT establish equivalence of electromagnetic forces on ordinary electric charges: an electrically charged probe breaks this continuous duality unless magnetic charges and charge couplings are transformed consistently.

## Gate 914 — the exact two-invariant classification and a false-null counterexample

Define I1=E²-B² and I2=E dot B. Under the same duality rotation with C=cos theta,S=sin theta,
I1_theta=(C²-S²) I1+4CS I2,
I2_theta=(C²-S²) I2-CS I1.
In particular theta=pi/2 sends I1 -> -I1 and I2 -> -I2, exchanging the sign-based electric-T and magnetic-X classifications without modifying T_munu. At theta=pi/4 a nonzero purely electric initial field (E=e xhat,B=0) goes to (E=e xhat/sqrt2,B=-e xhat/sqrt2), so
I1_theta=0 yet I2_theta=-e²/2 !=0, S=0,
with the **same nonzero energy density and spatial stress tensor as before**. Hence I1=0 is not a sufficient 'radiation hinge' condition. A nonzero electromagnetic field is algebraically **null** precisely when BOTH I1=0 and I2=0. Neither condition alone is enough. There is no requirement to interpret all I1=0 configurations as radiation. More strongly, the duality circle continuously moves generic non-null fields through I1=0 while keeping the full gravitational source invariant. The sign-based T/X dictionary is therefore **not intrinsic to gravitational stress-energy**.

This sharpens Sandbox v15.1086's correct scoped statement that its sorting is a dictionary, not a new dynamics or coupling. The two Maxwell invariants and duality phase encode data that ordinary Einstein gravity through T_munu does not separately measure. Extra charged matter can distinguish fields via Lorentz forces, but that distinction is already ordinary electromagnetism and does not provide a novel Cone gravity force.

## Gate 915 — apply to our particular compact packet and the existing Weyl chain

Gravity v15.1078 compact initial data E=(∂y Psi,-∂x Psi,0),B=0 are free Maxwell Cauchy data, not a charged Coulomb monopole. Their 90° dual E_dual=0,B_dual=-E also satisfy div E_dual=0,div B_dual=0 with compact support. They have sign(I1)>0 versus <0 wherever E!=0, thus lie in different nominal T/X field sectors, yet their full T_munu is pointwise equal at t=0 and stays equal during vacuum Maxwell evolution. Consequently both share the earlier exact 3/5 transverse-stress ratio, the nonzero-q Fourier +7/25 correction, full source Ward identities, and all tensor electric-Weyl expansions from v15.1083, plus any eventual fully constrained scalar/vector Weyl completion using the same Einstein–K4 action.

This does not remove the need to solve the full metric/solid ADM constraints for a detector signal. It shows that **doing so cannot by itself distinguish dual electromagnetic field labels**. If a future Cone interaction claims T/X asymmetry, it must supply a specific action term depending on duality phase/invariants beyond T_munu, an independent physical coupling coefficient and a consistent covariant conservation/gauge structure. Otherwise the T/X difference is representation/bookkeeping.

## Gate 916 — audit reproducibility and decisive next direction

Canonical scripts are listed above. Local execution of the duality SymPy calculations passed all source equivalence and I1=0,I2!=0 tests. The v15.1081 corrected assertion now checks the exact q⁴ remainder as well as its vanishing modulo q⁴, rather than asserting a nonexistent exact equality. The original failing script is preserved; the defect and correction are fully disclosed here, following protocol.

**Positive:** full physical gravitational source duality degeneracy has been proved and an invalid field-hinge inference corrected. **Negative:** no new G-free dimensionless tidal observable, q2 transition/source operator or physical second X spacetime follows from the invariant-sign dictionary; matched K4 versus Einstein+the same elastic solid remains identically zero.

**AUDIT HANDOFF:** (1) run the complete canonical v15.1089 corrected Fourier script, verify exact residual -q⁴ c³ M0/4, original v15.1081 failure and +7/25 coefficient; (2) check arbitrary-duality invariance of every full Maxwell stress tensor component (no charged matter); (3) check pi/4 pure-E -> I1=0,I2!=0 counterexample and its nonzero energy with no Poynting; (4) review warning that compact initial electromagnetic fields are **not** intrinsically radiative/null at the packet's support; (5) confirm Sandbox v15.1088 chronological precedence and preservation of all four provisional/canonical Gravity scripts. Suggested subsequent gate: source-first **charged probe** couplings versus purely tidal probes to see exactly which observable measures EM duality phase and which is universally blind.
