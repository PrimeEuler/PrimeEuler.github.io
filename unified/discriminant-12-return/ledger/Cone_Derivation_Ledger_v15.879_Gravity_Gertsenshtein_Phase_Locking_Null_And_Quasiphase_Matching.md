# Cone Derivation Ledger v15.879 — Gravity: Gertsenshtein phase transfer does not self-lock; magnetic sign reversals enable ordinary quasi-phase matching

**Date:** 2026-11-13 US Eastern. **Parents:** v15.878 Gravity exact Maxwell cross-stress and four-channel Hermitian photon/graviton WKB conversion, v15.866/867/869 Muse per-sector half/quarter phase dictionaries, v15.871–876 force/parametric oscillator controls, External Audit Round 567 (v15.877) confirming the earlier source and phase tests. **Immediately before writing this ledger, live HEAD:** 52eadf07b8b8c9f5a7ecb181b00f1677d74a5c2e. Target absent; additive-only, no previous certified object or Suzuki payload modified.

**Scientific classification:** [D] exact uniform-field Gertsenshtein transfer preserves relative polarization coherence, without attractive phase stabilization; [D] basis-independent full-state unitary overlap obstruction for genuine autonomous global phase locking, also under spatially rotating fields and birefringence; [N] numerical benchmark: *physical spatial magnetic sign reversals* coherently boost detuned conversion compared to a cancelling uniform-field path; [N] this is externally engineered standard quasi-phase matching, not a Cone-derived phase selector; [O] action-derived quarter-mesh prescription for external magnetic-field reversals or a new dissipation/feedback mechanism compatible with causal Maxwell+K4+matter dynamics.

## Gate 518 — a coupling sign convention is not a phase-locking force

Recall the usual canonical normalized WKB 4-vector **Psi=(A_x,A_y,h_+,h_x)** and homogeneous, lossless, equal photon dispersion mixing:

**i∂_z Psi = H Psi**, with **H=[[Delta I_2,C],[C^T,0]]**,

**C=mu [[sin(theta),-cos(theta)],[cos(theta),sin(theta)]]**, **C^TC=mu² I_2**.

At B along +x (theta=0), the polarization map is **A_x ∝ -h_x, A_y ∝ +h_+** under the selected sign convention. Redefining one polarization axis or mode changes the displayed minus sign, not the physical prediction. The physics resides in correlations measured relative to a fixed field/detector orientation. Literature on polarization-resolved mixing includes **JCAP 09 (2026) 071, DOI 10.1088/1475-7516/2026/09/071** (Côté and Fortin), which formulates phase shifts and Stokes parameters; PRL 132 131402 (2024) gives the 2×2 WKB mixing matrix and magnetic coupling as conventional control.

The uniform field exact evolution **U(L)=exp(-iHL)** has photon-from-graviton transfer subblock **T(L)=f(Delta,mu,L) R(theta)** for one *complex scalar* f and real orthogonal R(theta)=C/mu. Therefore

**T†T=|f|² I_2 = P_(g→gamma) I_2**,

**P_(g→gamma)=[4mu²/(Delta²+4mu²)] sin²[L sqrt(Delta²+4mu²)/2]**.

Every normalized incoming 2-component graviton polarization is transferred with exactly the same probability. The outgoing photon **normalized Stokes vector** is the Stokes vector of the geometrically rotated incoming polarization. The relative quadrature *can be transmitted and measured*, but there is no unique phase to which arbitrary incoming polarizations converge. In particular incoming h=(1,i)/sqrt2 is no more dynamically selected than (1,1)/sqrt2 or nearby (1,i exp(i epsilon))/sqrt2. Under T, their polarization differences retain their distinguishability up to the common conversion amplitude sqrt(P), so the tiny input phase error is not damped toward zero.

For a pure global phase e^{i alpha}, even the relative Stokes vector is unchanged; only a relative phase between h_+ and h_x can influence output polarization. A basis-relative sign equivalent to alpha→alpha+pi cannot alone establish a physical, dynamical quarter-cycle lock.

## Gate 519 — irreversible attraction is impossible in the *full* lossless Hermitian model

For any real magnetic orientation, detuning and **real Hermitian** nonuniform H(z), evolution is unitary (path-ordered as required). For *any* two solutions Psi_1(z), Psi_2(z),

**d/dz[Psi_1† Psi_2]=0**, hence both norm and their complex overlap are exactly conserved. In particular distinct initial pure states cannot asymptotically converge to the same unique full photon–graviton state under closed lossless mixing. This is a basis-independent no-attractor theorem and continues to hold for a rotating transverse magnetic-field angle theta(z), a z-dependent mixing mu(z), and distinct lossless photon refractive shifts. It does not forbid driven phase-locked systems with external coherent references, nonlinear dissipation, measurement/postselection, or lossy mode filtering. Conditional photon *subsystems* can show polarization filtering even though the full four-state evolution is unitary; therefore the statement is intentionally about autonomous asymptotic attraction of the full closed system.

Reproducer evolves two graviton states separated in relative phase by 0.1 rad along a 25-length nonuniform Hermitian H(z) with theta(z), mu(z), Delta(z), and photon split(z). Their complete complex overlap remains the same within ~10^-12, and the norms remain 1. For a homogeneous case with input phase disturbances epsilon=10^-2,10^-3,10^-4, normalized photon transfer distances retain the source perturbation, rather than collapsing to a preferred quarter phase.

**Verdict:** the Gertsenshtein effect supports **coherent phase transfer**, but does not by itself generate **attractive phase locking**. Assigning the Cone half/quarter offsets as the initial h-polarization phases is a *choice of input* rather than a derived dynamical constraint.

## Gate 520 — a real sign change can nevertheless synchronize *spatial* conversion

A separate question closely aligned with the user's sign intuition is whether **physical changes of magnetic-field direction** can compensate photon–graviton detuning to keep the conversion amplitudes accumulating coherently. The answer is yes, via ordinary **quasi-phase matching (QPM)**.

In the first-order weak-mixing / undepleted gravitational-wave limit, for a single polarization mode of the conventional two-state mixer,

**A_gamma(L) ≈ -i ∫_0^L mu(z) exp(i Delta z) dz**,

up to an overall propagation phase. With constant nonzero detuning Delta and a constant mu, **P_uniform≈(mu L)^2 sinc²(Delta L/2)** and can vanish at a full number of mismatch cycles. If instead one *physically reverses the signed transverse magnetic field* so that

**mu(z)=mu0 sign[cos(Delta z)]**,

the integrand is periodically reoriented and its coherent sum grows. For L covering an integer number of whole mismatch cycles, the Born amplitude magnitude is **|A_QPM|=(2/pi)mu0 L**, hence **P_QPM≈[(2/pi)mu0 L]²**.

This sign reversal is NOT a mere change of polarization basis. It is a **spatially varying real background B field** supplied by an external magnetic geometry and its supporting currents; the period is set by the independently supplied refractive mismatch Delta. It is also not dynamical *phase locking in time*; it is engineered spatial phase matching in a linear wave mixer.

**Exact two-state matrix-product demonstration**, with dimensionless test values **mu0=0.002, Delta=0.8, L=8pi/Delta=10pi≈31.4159265** and the field switched at the sign changes of cos(Delta z), gives

| arrangement | exact numerical P_(g→gamma) |
| --- | ---: |
| unflipped uniform field | **6.16827138805×10^-13** |
| sign-reversed magnetic field | **0.00159914301833** |
| first-order weak-mixing QPM analytical estimate | **0.00160000000000** |

Matrix evolution remains unitary; numerical QPM answer differs by only ~0.054% from the leading Born approximation. The extremely small uniform-field value is a deliberately chosen **destructive-interference path** and is not a realistic experimental sensitivity or an extraordinary gain over all ordinary GR fields. The result is standard coherent-wave engineering. The sign of conversion amplitude under a *real B reversal* differs from a removable convention sign on photon or graviton polarization coordinates.

## Gate 521 — the physical Cone selector remains missing

The EM 1/2 and gravity 1/4 offsets can be consistently interpreted as relative node and turning-point coordinates, and their values may inspire a QPM hypothesis. However **nothing in the frozen K4 EH+relativistic-solid plus standard Maxwell action derives** (i) a magnetic reversal schedule B(z), (ii) a refractive mismatch Delta(z), (iii) a phase-stabilizing nonlinear/dissipative reference, (iv) a preferred wave frequency, or (v) a new coupling coefficient fixed by the Cone meshes. Both the coherent transfer and externally engineered QPM are already present in conventional Einstein–Maxwell theory. Consequently matched conventional subtraction still produces zero Cone-only effect without a new justified operator or selector.

A stringent next test would be to derive actual field and current dynamics on the Cone mesh from a covariant action or a constraint principle, and predict **a reproducible physical B-field sign-reversal length relative to Delta** before fitting sources. Then test it with polarization-resolved photon–graviton conversion under spatial dispersion and compare with ordinary medium/QED expectations. Alternatively seek a fully conservative nonlinear reference mode and ask for **bounded phase stability**, carefully distinguishing oscillatory stability from dissipative attraction.

## Provenance, reproducibility and audit

**Reproducer:** research-notes/k4_gertsenshtein_phase_lock_qpm_v15_879.py, additive SHA **52eadf07b8b8c9f5a7ecb181b00f1677d74a5c2e**. Exact or equivalent local NumPy/SciPy execution passed the uniform transfer/rotation/phase perturbation control, nonuniform full-state overlaps, and independently the exact 2×2 magnet-reversal QPM numerical comparison. The newly committed exact bytes await external independent reexecution; no certified historical files changed. The prior v15.877 Audit/Gravity version collision was reconciled by Gravity's uniquely labeled v15.878 ledger without overwriting any other entry; this new v15.879 was checked globally unused at creation.

**HANDOFF — external audit and Muse/Sandbox:** Independently reexecute v15.879 script. Verify phase-basis covariance, transfer-subblock singular values, full-state unitary overlap theorem and 2×2 B-reversal QPM with fine-grained propagation; importantly challenge any interpretation of reversible signal transfer as asymptotic locking or a mesh-derived physical selector. Check against 2026 polarization/Stokes analysis. Keep the next physical action-derived operator gate distinct from mere imposed B(z) engineering.
