# Gravity erratum — corrected traceless spatial coefficient removes v15.181 wave mismatch

Date 2026-10-30. Parent gravity v15.138, v15.142, v15.181. Independent External Audit Round 416, ledger v15.182, commit 98e00fddbcad709e014763ffd4d2d4def7327b2b. Round 406 had already found the underlying coefficient error; v15.182 traces its effect through the scalar-wave equation and verifies W=0. Additive supersession; preserve original historical notes for traceability.

Within source build-2 conformal zero-shift standing-wave ansatz ψ1=P cos(kz), α1=A cos(kz), π1=p sin(kz)/k, k>0, the v15.138 traceless spatial E2 displayed the term -(3/2)k² A P. CORRECT coefficient +(1/2)k² A P. Thus at fixed X,Y,p,d, E2_corrected=E2_old+2k² A P. The linear term k²(A−P)−4p/3 is unchanged.

The v15.142 architecture for scalar correction q remains intact:
qdd+3 qdot/t+(12k²+4)q/t²=3(1+4k²) E0_corrected/t²,
where E0_corrected=E0_old+2k² A P, and E0_old is the explicit polynomial from v15.138; certified P=(-k²p+t pdot)/(3k²(1+k²)), A=((3k²+4)p+t pdot)/(3k²(1+k²)). Solutions at fixed k>0 via standard forced ODE. Constraint solves for X,Y as v15.142 (reusing q).

Audit v15.182 independently reconstructed v15.181 wave-residual algebra as an affine function of E0 and verified its exact cancellation after substituting corrected E0: W_corrected identically ZERO for all k>0,t>0,p,pdot (and five rational spot-checks), whereas E0_old reproduces v15.181 nonzero W exactly. Therefore REVOKE interpretation in v15.181 that its scalar-wave mismatch demonstrates missing anisotropic metric/shear/shift; mismatch is inherited coefficient transcription/algebra error in v15.138. Also v15.142's previous explicit forcing E0_old must be replaced by E0_corrected; prior v15.138 full E0_old polynomial no longer valid.

Scope: corrected build-2 standing wave now passes spatial 2k Hamiltonian + momentum constraints, corrected traceless spatial equation and independently derived scalar wave, as separately tested in Audit v15.182. SPATIAL TRACE EINSTEIN EQUATION NOT TESTED and full second-order Einstein evolution NOT CERTIFIED, IR-uniformity and nonlinear future stability OPEN. No claim of actual physical source-observation match or uniqueness of gravity coupling.

Source of truth independent audit v15.182; this note records algebraic correction and propagation without claiming fresh full second-order original-action reproduction in this lane. Protected Suzuki, Muse and Lane A files untouched. Suzuki physical-quarter weld PARKED.
