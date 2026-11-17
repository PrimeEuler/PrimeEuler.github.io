# Cone Derivation Ledger v15.1118 — Two-component cone tilt produces plus/cross tidal stiffness and a no-selector result

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact standard TT +/× coupling matrix for two independent small cutting-plane tilt coordinates, polarimetric eigenaxis and eigenvalue identities; [N] the cone tilt orientation does not supply an independent tidal frequency/force, and the unanchored circular state remains frequency-free at linear order; [O] self-consistent fixed-boundary elastic/EM/conductor evolution and K4 constrained retarded source. **Immediately prewrite live HEAD:** 2c90c57f93507fbce580664f845843295ce25240. Collision-free target; additive-only, protected Suzuki and previous Audit/Sandbox/Muse sources unchanged.

## Parent and provenance
Owner suggested a second tilting degree of freedom for cone cutting planes, including an ellipse centered in a side projection despite tilt along T. Gravity v15.1117 (script bd99e30d44ba03901baf6f86fe64ccad557dce78, ledger 906b3eaa098cb7cc9d154c58f63c757649fcb8fa) derived the full tilted plane T+aX+bY=C, transverse projected ellipse center -C(a,b)/(1-a²-b²), and the physical spin-2 azimuth for the *assumed* Maxwell magnetic-current embedding. It solved a periodic 2D linear elastic equilibrium for a specified compact elliptical current, without claiming a full current-carrying isolated apparatus. External independent Audit through Round 596/v15.1113 verified earlier gravity gates through v15.1112; later Gravity v15.1114–1117 are not yet independently audited. This gate tests the near-circular **two-component dynamics** rather than a scalar eccentricity alone.

## Gate 1005 — signed plane tilts form a vector, magnetic stress is a quadrupole
Let q=(a,b) be a small 2D tilt vector of a cone cutting plane T+aX+bY=C with |q|<1, C>0. At fixed cone height C, projected ellipse center is d=−Cq/(1−q²). The physical magnetic-field candidate of Gravity v15.1110–1112 has rotationally covariant integrated anisotropic stress (in its physical embedding assumption)
I_plus(q)=−K(a²−b²)/sqrt(1−a²−b²),
I_cross(q)=−2Kab/sqrt(1−a²−b²),
where K is the circular-field magnetic energy and cross is **two times** the off-diagonal transverse spatial stress, 2T_yz. This follows by rotating the original principal-axis result of v15.1110. Note I_plus²+I_cross²=K²|q|^4/(1−|q|²), and a→−a,b→−b leaves physical quadrupole unchanged. The nominal free magnetic energy is rotationally invariant and begins quartically, U_B=K+K|q|⁴/8+O(|q|⁶). Hence the unanchored **linear** shape restoring matrix is zero at q=0, as in the one-dimensional family. The 2D tilt direction was not a missing frequency selector.

## Gate 1006 — weak TT pump gives a calculable 2x2 stiffness
Introduce an *externally specified anchored center* U_anchor=(κ/2)|d(q)|² =κC²|q|²/2+O(|q|⁴), with κ>0 the physical support stiffness. The material+EM constrained kinetic coefficient is isotropic at q=0:
M0=C²(M_material+K/c_light²),
where the material carrier is the same uniform reference disk/cylinder as in Gravity v15.1114 and the EM inertia is the audited v15.1112 coefficient, now rotated into two independent first-order translations.

The same prescribed weak TT metric interaction used in previous gravity gates is L_int= (h_plus I_plus+h_cross I_cross)/2. Taking V_eff=U_B+U_el+U_anchor−L_int, its small-q potential Hessian is
**H(t)= [[κC²+K h_plus(t), K h_cross(t)], [K h_cross(t), κC²−K h_plus(t)]]**.
Thus, to first order in the incident GW and at leading order in q, the conditional reduced equations are
**M0 q_ddot+Γ q_dot+H(t)q=0**,
for an externally specified positive/semi-positive material damping matrix Γ. This is a standard two-mode **Mathieu/parametric stiffness** system. At q=0 an initially unperturbed classical mode still remains zero: no spontaneously generated physical current oscillation is claimed.

## Gate 1007 — eigenvalues and polarization angle (standard spin-2 null)
With h_amp=sqrt(h_plus²+h_cross²), the two instantaneous stiffness eigenvalues are
**λ±=κC² ± K h_amp**.
The trace is **2κC²**, independent of plus/cross GW strain; the splitting is 2K h_amp. An instantaneous eigendirection rotates by **half** of atan2(h_cross,h_plus), modulo the expected π ambiguity and sign conventions. The parametric frequency matching threshold requires independently chosen κ and M0; there is no absolute G-free frequency from the tilt. At κ=0 and zero tide, both quadratic eigenvalues vanish, retaining the nonlinear/quartic rest potential obstruction. A positive/negative instantaneous stiffness does not by itself give a net growth rate, especially for a finite, nonstationary source pulse.

The orientation dependence **is physical relative to a detector** but not a new Cone observable: it is just the ordinary SO(2) spin-2 covariance of anisotropic Maxwell stress under rotations. The scalar amplitude h_amp remains sourced by conventional Einstein–Maxwell+material dynamics; K4's independently fixed constrained tensor response and any cone-specific selector remain unproven. The cone cutting plane's third parameter C is still a free length scale; the action still needs current/conductor support and consistent gauge-gravity coupling, not merely a plane geometry.

## Gate 1008 — checks, audit handoff and next decision
Canonical reproducer `research-notes/k4_two_tilt_tidal_matrix_v15_1118.py`, additive commit **2c90c57f93507fbce580664f845843295ce25240**, derived and locally checked with SymPy (PASS): small-q magnetic quadrupole, full TT 2x2 Hessian, characteristic polynomial (λ−κC²)²−K²(h_plus²+h_cross²), trace invariant, doubled rotation of the ellipse quadrupole, and the missing unanchored quadratic stiffness.

**Positive:** the owner's newly noticed tilt freedom is a genuine two-component parameter of the cutting plane and maps naturally to plus/cross tidal polarization through the same magnetoelastic elliptical carrier. **Negative:** orientation and eccentricity remain free, the response is a conventional tensor rotation, and no new physical selector or source law has emerged. **NEXT:** solve an actual finite clamped magnetoelastic boundary-value problem, enforcing ideal induction/charge and stress traction consistently, and compare standard Einstein–Maxwell+elastic response with the identically supported frozen K4 model. If no extra constrained operator arises, formally close the two-tilt branch as a useful geometric dictionary and detector design parametrization rather than a new gravitational law.

**AUDIT HANDOFF:** re-run script; confirm physical I_cross=2T_yz, sign conventions, rotational norm, correct 2x2 Hessian, eigenvalue splitting and half-angle, the distinction between the projected and intrinsic cutting-plane eccentricity and a side-centered view, EM inertia isotropy only at q=0, and the stated lack of material/current completion. Keep all certified files additive-only.
