# Cone Derivation Ledger v15.1085 — Complete compact-Maxwell initial Fourier SVT stress and scalar ADM constraint obstruction

**Date:** 2026-11-17 Eastern. **Gravity/Cone lane. Status:** [D] exact spatial longitudinal Fourier stress SVT source decomposition and initial energy/momentum Ward jet for the previously certified compact vacuum Maxwell Cauchy field; [N] the TT-only electric Weyl component of v15.1083 cannot stand for full constrained tidal field; [O] solve scalar/vector ADM metric constraints and obtain detector-local electric Weyl. **Prewrite live HEAD:** 8e865cbf5490b3a9c90b629917dd490c6b4f6426; ledger target absent. Strict additive only, no edits to protected Suzuki or Audit/Sandbox/Muse/earlier certified artifacts.

## Redundancy, Audit and version control
External Audit Round 590/v15.1079 independently verified v15.1076–1078. Gravity v15.1080 derived initial Maxwell anisotropic stress time curvature; v15.1081 derived nonzero longitudinal Fourier source jet; v15.1083 derived the TT-only coasting K4 electric Weyl jet with explicit Maxwell a_FLRW^-4 conformal factor. **Sandbox owns v15.1082 and v15.1084**, latter ledger commit 5360de7e6659d73215125dc7c6dcb651edf4a002; gravity's collision with Sandbox v15.1082 was resolved additively in v15.1083. This gate is v15.1085. Earlier v15.717 and v15.750 derived the ADM scalar source Ward and a general sourced three-sector electric Weyl decomposition; no claim to rediscover them. New task: calculate which precise scalar/vector/TT sources the **actual compact Maxwell Cauchy data** presents at one nonzero Fourier orientation.

## Gate 909 — actual initial Fourier stress components, not only plus TT
Take flat/conformal Maxwell Cauchy field from v15.1078, Psi=A f(x/a)f(y/b)f(z/c), E=(partial_y Psi,-partial_x Psi,0), B=0 initially, f(s)=(1-s²)^3 on |s|<1 and 0 outside. Let I0=2048/3003, I1=1024/385, and F0(q)=∫_R f(z/c)^2 exp(-iqz)dz, q≠0. Set
R(q)=A² I0 I1 (a/b+b/a)F0(q)/2,
P(q)=A² I0 I1 (b/a-a/b)F0(q)/2.
All Fourier components here involve transverse integration at wavevector (0,0,q). At the initial slice, in orthonormal conformal Minkowski conventions,
T00=R; T0i=0; Tij=diag(P,-P,R);
off-diagonal integrated stresses vanish because x/y factors are odd total derivatives or E_z=B=0. In particular spatial stress trace Tii=R, the four-dimensional electromagnetic stress trace -T00+Tii=0, and the longitudinal Tzz=R. The spatial TT projection for q parallel z yields Tij_TT=diag(P,-P,0), with no cross component at initial time. P/R=(b²-a²)/(b²+a²), equaling 3/5 for a:b=1:2, and zero when a=b.

The 3D spatial scalar traceless longitudinal stress is
S_L=Tzz-(Tii/3)=2R/3.
It is nonzero even when P=0 at a=b. For a:b=1:2, S_L/P=(2/3)/(3/5)=10/9, valid wherever F0(q)≠0. Thus a tensor-only truncation is not an accurate full gravitational source even for a simplified longitudinal Fourier slice. S_L and P have different rotation/SVT characters; their ratio alone is not a curvature or signal amplitude ratio. Vector momentum and vector anisotropy are zero *on the initial slice* for this projected q orientation, not proved zero at arbitrary times or all general Fourier orientations.

## Gate 910 — source stress conservation fixes a scalar Ward initial jet
In free conformal Minkowski Maxwell coordinates, local energy and momentum conservation imply the longitudinal Fourier equations
∂eta R(q,eta)+iq S_z(q,eta)=0,
∂eta S_z(q,eta)+iq Tzz(q,eta)=0
after integrating transverse coordinates over all R²; transverse divergence surface terms vanish for the compact-support finite-propagation field. At eta=0, S_z=0 and Tzz=R. Thus
R'(q,0)=0, S_z'(q,0)=-iq R(q,0), R''(q,0)=-q² R(q,0).
For the physical FLRW source, orthonormal energy and momentum stresses all scale as a_FLRW^-4. If \mathcal R_phys=a_FLRW^-4 R and \mathcal S_phys=a_FLRW^-4 S_z, the cosmological source conservation is equivalently
∂eta(a_FLRW^4 \mathcal R_phys)+iq a_FLRW^4 \mathcal S_phys=0,
∂eta(a_FLRW^4 \mathcal S_phys)+iq a_FLRW^4 (Tzz)_phys=0,
for source-free conformally invariant Maxwell matter. These identities are necessary input to the already derived K4 ADM source Ward relation (v15.717); no separately imposed nonconserved stress can be substituted for the full Maxwell packet. This gate does NOT solve ADM lapse/shift or compute sourced scalar potentials.

## Gate 911 — strict completeness limitation on tensor electric Weyl
The TT tensor-mode Weyl time jet of v15.1083 remains a valid result for the projected TT dynamical subproblem with its declared zero initial tensor data and stress convention. However the compact Maxwell field also has R and S_L nonzero and developing longitudinal momentum, so the Hamiltonian and momentum constraints source scalar lapse, scalar spatial metric and longitudinal shift. A complete constraint-consistent initial gravitational state cannot generically set every scalar metric perturbation and its constraint data to zero while keeping R nonzero. Therefore the v15.1083 TT electric Weyl W_+ cannot simply be called the **full** electric tidal field of the physical packet. Scalar electric Weyl terms and potentially vector terms for general Fourier orientations must be reconstructed from the ADM constraints in a common gauge. The earlier v15.750 decomposition establishes tensor, vector and scalar curvature formulas, but importing a scalar formula without source-compatible initial/boundary data would hide the open gravitational constraint problem.

The above source Ward relations do not specify unique scalar gravitational data: boundary conditions, gauge, homogeneous solid field modes and possible constraints' zero-mode restrictions must be fixed. A complete physical detector receives their combined electric Weyl, which must then be compared against Einstein+the SAME elastic-solid matter/Maxwell source and optical probe. With no additional action-derived Cone operator the matched comparison remains a null baseline; the new scalar source itself is a standard electromagnetism result.

## Gate 912 — reproducibility and next gate
Exact SymPy reproducer research-notes/k4_maxwell_full_initial_svt_source_v15_1085.py, additive commit 8e865cbf5490b3a9c90b629917dd490c6b4f6426. Independently re-executed equivalent local Python program: PASS for compact integrals I0/I1, stress Fourier factorization and TT projection, S_L/R=2/3 and S_L/P=10/9 at ratio 1:2, traceless full EM stress, symmetric source control P=0 but nonzero scalar S_L, and the longitudinal Maxwell Ward initial time jet. No free parameter fitted, no physical G derived.

**Next actual constraint gate:** use the archived v15.713/717/750 ADM source formulas, impose the full conformal Maxwell R,S_z,Tzz and transverse momentum on a nonzero longitudinal Fourier mode, solve scalar lapse/shift with compatible initial/boundary solid perturbations, and compute scalar plus tensor orthonormal electric Weyl at a chosen event. Then repeat with identical Einstein+elastic comparator and test for an operator genuinely fixed by the arithmetic meshes.

**AUDIT HANDOFF:** independently check spatial Maxwell stress sign/conventions and TT+ projection; traceless trace and scalar STF; 10/9 source ratio; Fourier source Ward signs and FLRW a^-4 conservation; and distinction between initial source compatibility and actually solving ADM constraints. Do not conflate spatial Fourier q with q=2 ladder. Preserve both Sandbox v15.1082/v15.1084 and collision history.
