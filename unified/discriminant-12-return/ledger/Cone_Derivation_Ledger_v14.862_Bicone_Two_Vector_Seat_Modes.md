# Cone Derivation Ledger v14.862 — Bicone two-vector exchange and relative seat mode

Date 2026-10-25. Parents v13.595, v14.097–099, v14.856–861. Research note research-notes/Bicone_Two_Vector_Exchange_Seat_Modes.md commit 03755a7178f0153c04cbb994db5ff83ad798f4a7. Live prewrite HEAD 03755a7178f0153c04cbb994db5ff83ad798f4a7. Additive only; no Suzuki/far-tail changes.

[D, conditional Hamiltonian] Two spin-j bicone sectors with \(\mathbf L=\mathbf J_1+\mathbf J_2,\mathbf A=\mathbf J_1-\mathbf J_2\) and a NEW POSTULATED exchange \(H_{\rm ex}=-\lambda\mathbf J_1\cdot\mathbf J_2\) have exact total-spin eigenvalues \(E_L=-\lambda[L(L+1)-2j(j+1)]/2,\ L=0,\ldots,2j\). For λ>0, ground multiplet L=2j, next L=2j-1 gap 2λj. At fixed classical vector lengths and small relative angle, exchange energy excess is \(+\lambda j²\theta²/2\). This is intrinsic relative-angle restoring torque, and common rotation is free. Exchange is NOT derived from bicone algebra.

[D] Uniform bias/drive \(-\Omega L_z\), or rotating \(L_x,L_y\), preserves L² and addresses common precession; staggered \(A_x,A_y\) can address relative L sectors. Classical linear modes around aligned z vectors have common precession frequency Ω and relative precession Ω+2λj (for Ω,λ>0 under consistent sign convention).

[D] Exact j=1/2 test: triplet exchange energy -λ/4, singlet +3λ/4. In bias Ω>0, |t,+1> has E=-λ/4-Ω and couples through \(-g\delta A_x\) to singlet with matrix element magnitude 1/√2. Ground-state curvature contribution is \(E''(0)=-g²/(\lambda+\Omega)<0\). Thus a positive angular restoring torque under prescribed relative rotation does NOT imply a positive seat-displacement stiffness when the seat linearly perturbs the differential magnetic field: this perturbation softens the seat.

[O] Derive seat displacement-to-relative-angle map from opposing parabolic geometry and an actual magnetic field/drive, and test whether the contact-quantized system can select λ, Ω, g and the physical cutoff. No Newton G or physical hierarchy derived. No Suzuki/Weil arithmetic-carrier identification.

Flags: bicone_exchange_spectrum=EXACT_GIVEN_POSTULATE; relative_angle_curvature=POSITIVE_FOR_LAMBDA_POSITIVE; uniform_drive_preserves_total_L=TRUE; differential_seat_ground_curvature=NEGATIVE; bicone_coupling_derived=NO; G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: bicone-two-vector-magnetic-seat-coupling
parent: v14.862
status: open
action: Independently verify total-spin eigenvalues, gap and exchange selection symmetry, classical common/relative precession, j=1/2 differential-field matrix element and negative seat curvature; ensure λ remains a new postulate and no tensor/GR or Newton G claims. Preserve Suzuki/far-tail.
deliverable: scoped audit verdict.
