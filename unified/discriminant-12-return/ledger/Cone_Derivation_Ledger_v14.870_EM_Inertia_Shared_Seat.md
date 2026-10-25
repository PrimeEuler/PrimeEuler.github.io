# Cone Derivation Ledger v14.870 — Electromagnetic inertia, radiation, and shared-seat test

Date 2026-10-25. Parents v14.680, v14.863–869. Research note research-notes/Seat_Electromagnetic_Inertia_Radiation_Gravity_Test.md, commit 420bddfdbc03a61c042aa1443e04c0d3a8c8de63. Live prewrite HEAD 420bddfdbc03a61c042aa1443e04c0d3a8c8de63. Additive only, Suzuki/far-tail untouched.

[I] Minimal regulated classical electric dipole: separated finite spherical blobs +q,-q with separation ℓ(t)=ℓ0+δ(t)>2a. Nonrelativistic and long-wavelength regime. δ as bicone seat is a proposed identification, not derived from Maxwell or cone algebra.

[D] Electrostatic interaction U_int=-C/(ℓ0+δ), C=q²/(4π ε0). U_int'(0)=C/ℓ0² nonzero; U_int''(0)=-2C/ℓ0³ negative. Coulomb attraction does not make δ=0 equilibrium or produce positive restoring curvature; stable seat requires a balancing constraint/force and sufficient positive added stiffness.

[D] Electric dipole p=q(ℓ0+δ), radiated power P=q² δddot²/(6π ε0 c³). Leading local reaction F_rr=τ δ''', τ=q²/(6π ε0 c³), satisfies ∫F_rr δdot=-τ∫δddot² + τ[δddot δdot] over intervals. The boundary term tracks reactive near-field energy; third-order approximation is not automatically a causal stable fundamental equation and needs finite-size or reduced-order treatment.

[D/O] Finite electromagnetic self-energy contributes to total stress-energy and gravitation. U_EM/c² is mass-equivalent energy of a complete isolated system, but deriving effective *internal-coordinate inertia* requires field momentum plus stabilizing stresses and a regulated retarded kernel. GR couples to all stress-energy, not a selectively Higgs-like source or an independent gravity monopole. A common geometric focus or seat does not prove one scalar field or a common coupling constant.

Decision: real electromagnetic backreaction for an internal dipole coordinate, but shared-seat EM/G dynamical equivalence remains UNPROVEN. Next gate: build explicit symmetry-respecting J^μ(δ) and T^{μν}(δ) from actual bicone Larmor geometry, compute quadratic Maxwell effective kernel, and test possible gravity coupling without introducing an arbitrary scalar.

Flags: Coulomb_seat_curvature=NEGATIVE; Coulomb_first_derivative=NONZERO; dipole_radiation=POSITIVE; effective_internal_inertia=NOT_DERIVED; shared_gravity_seat=HYPOTHESIS; Higgs_identification=UNPROVED; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: electromagnetic-inertia-shared-seat
parent: v14.870
status: open
action: Check regulated opposite-charge dipole potential derivative/curvature, radiation power, integrated Schott term, limitations of local reaction and total energy versus internal-coordinate inertia, and distinction between GR stress-energy coupling and new common scalar. Preserve Suzuki/far-tail.
deliverable: independent scoped verdict.
