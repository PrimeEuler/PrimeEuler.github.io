# Cone Derivation Ledger v15.681 — Gravity lane: finite-cavity normalization audit and translation-invariant dispersion ratio

**Date:** 2026-11-11 US Eastern. **Parents:** v15.679 traveling K4 tensor/EM phase matching and static-field seed; v15.680 finite fixed-wall cavity, seeded omega_c resonance, traveling 2:1 null and conditional K4 opening. **External audit:** Round 540 commit b18a21051d19bd3ed4215afe9eadf386e916644b independently hand-derived and re-executed v15.676/678/679/680 and reported no ledger correction required. **Status:** [D] independent field-normalization reproducer, exact two-length same-frequency cavity overlap ratio, common-center translation audit and timelike small-mass expansion; [N] the tempting O(m_T^2/omega^2) relative phase is ordinary propagation/placement phase, not an internal cavity discriminator; [C] the remaining translation-invariant amplitude ratio is a fixed-wall toy and is only O(m_T^4/omega^4); [O] full 3D covariant same-center mode geometry, K4 source/eta selection, and any Cone quarter/half temporal-frequency selector. **Immediately prewrite live HEAD:** 4ffd5e23b2b11b416e951df16708d5c10e14abfa. Collision checks found no v15.681 ledger entry. Frozen Suzuki certificates and prior audited objects untouched.

**Comparator literature:** Berlin et al., *Phys. Rev. D* 105 (2022) 116011, DOI 10.1103/PhysRevD.105.116011, emphasizes proper-detector-frame/gauge-consistent cavity GW electrodynamics and resonant static-B conversion. Gué, Krokotsch, Moortgat-Pick, *JCAP* 08 (2026) 058, DOI 10.1088/1475-7516/2026/08/058, gives a covariant eigenmode-overlap framework with dynamic elastic boundaries and EM backreaction for arbitrary detector geometries. The calculations below remain a narrower fixed-wall analytical diagnostic.

## Gate 211 — independent normalization check preserves v15.680's physical result

Re-derive the v15.680 first-mode cavity with z in [0,pi], c=omega_c=1, f=sqrt(2/pi)sin z, static transverse magnetic bias A_y^(0)=B0 z, and prescribed shear b=h exp[i(Kz-Omega t)]. The exact first-order bulk equation remains

**(partial_t^2-partial_z^2)a_y = 2 B0 partial_z b.**

For a=A(t)sin z and modal damping 1/Q, define

**J(K)=(2/pi) integral_0^pi sin(z)e^(iKz) dz = (2/pi)[1+e^(i pi K)]/(1-K^2).**

Then the steady magnetic and electric peak amplitudes are cleanly separated as

**|delta B|/|B0| = 2 h |K J(K)| / D,**

**|delta E|/|B0| = Omega |delta B|/|B0|,**

with **D=sqrt[(1-Omega^2)^2+(Omega/Q)^2]**. At the physical first-mode traveling resonance K=Omega=1, |J|=1 and both normalized amplitudes equal **2Qh**. Thus the v15.680 ledger formula and numeric table are unchanged. The older v15.680 reproducer contained an ambiguous symbolic helper proportional to K Omega while its numeric function used the magnetic-field normalization; that helper was only asserted at Omega=1. The new additive v15.681 reproducer separates B and E explicitly rather than modifying the audited v15.680 object.

## Gate 212 — same-frequency two-cavity ratio cancels strain and bias amplitude

Try to manufacture a dimensionless discriminator that does not require the unknown strain amplitude. Use two aligned fixed-wall cavities tuned to the **same EM angular frequency omega**:

- cavity 1: n=1 mode, L1=pi/omega;
- cavity 2: n=2 mode, L2=2pi/omega.

Let the gravitational/shear wave have r=K/omega. On exact EM resonance, after dividing each measured magnetic response by its calibrated static bias B0,n and quality factor Q_n, the common factors 2h r cancel. The remaining complex overlap is

**J_n(r) = [2/(n pi)] [1-(-1)^n e^(-i n pi r)]/(1-r^2).**

Therefore

**X_21 = J_2/J_1 = [1-e^(-i pi r)]/2 = i e^(-i pi r/2) sin(pi r/2).**

For a massless traveling GR comparator r=1, |X_21|=1. Superficially the phase of X_21 changes at first order in 1-r, which would look much more sensitive than the v15.680 amplitude opening.

## Gate 213 — translation audit removes the apparent O(m_T^2) internal phase

The two left-end coordinate intervals [0,L1] and [0,L2] do **not** have the same center. Their centers differ by

**Delta z=(L2-L1)/2=pi/(2 omega).**

A plane wave contributes the ordinary propagation phase exp(-i K Delta z)=exp(-i pi r/2), exactly the r-dependent phase appearing in X_21. Re-reference both cavities to one common physical center. The ratio becomes

**X_21^(center)=e^(+i pi r/2) X_21 = i sin(pi r/2).**

Hence the leading r-dependent phase is **not** a translation-invariant internal cavity observable. It is baseline/placement propagation phase. The invariant magnitude is only

**Xi_21(r)=|X_21|=sin(pi r/2)** for 0<r<=1.

For a timelike dispersion r=sqrt(1-mu^2), mu=m_T/omega,

**Xi_21 = 1 - (pi^2/32) mu^4 + O(mu^6).**

Using the existing conditional K4 local tensor mass m_T^2=(8 eta/3)H^2 gives

**Xi_21 = 1 - (2 pi^2 eta^2/9)(H/omega)^4 + O[(H/omega)^6].**

So after eliminating unknown strain, static-bias strength and calibrated Q, the first genuinely translation-invariant two-length amplitude discriminator is **quartically** suppressed in H/omega. The apparent quadratic phase advantage was not internal cavity physics.

## Gate 214 — verdict against promoting the ratio to a new Cone observable

The normalized ratio Xi_21 is dimensionless, G-free, and experimentally distinguishable in principle, but it **does not pass the Cone novelty/selector gate**:

1. it measures the generic wave dispersion ratio r=K/omega, so any non-null/massive/medium-modified propagation law can change it;
2. the K4 value still depends on eta and H, neither selected by the quarter/half Cone lattice;
3. the translation-invariant K4 difference is O[(H/omega)^4], even smaller than the O[(H/omega)^2] local vertex opening already found in v15.679-v15.680;
4. a real cavity requires proper-detector-frame fields, elastic moving walls, material response, EM backreaction and a full 3D geometry before the fixed-wall ratio could be interpreted experimentally.

Thus this gate is a **useful negative result**: amplitude normalization can be canceled, but the first tempting O(m_T^2) phase observable is ordinary propagation phase, and the internal same-frequency two-cavity amplitude ratio does not rescue the quarter-grid pump as a parameter-free gravity prediction.

**Reproducibility:** additive scripts research-notes/finite_cavity_two_resonances_v15_681.py (commit 34d3f3e614b1784ca6761374ef02e80bd6e7d9dc) and research-notes/finite_cavity_dispersion_ratio_v15_681.py (commit 4ffd5e23b2b11b416e951df16708d5c10e14abfa). The first independently reproduces the seeded omega_c resonance, separates magnetic/electric transfer normalization, and verifies the exact traveling 2:1 null with K4 small-mass opening. The second proves the exact two-cavity ratio, removes the center-offset propagation phase, and verifies the quartic invariant amplitude expansion. No figures and no protected Suzuki modifications.

**HANDOFF:** independent audit/sandbox/gravity should verify the field-normalization separation, the exact J2/J1 identity, the common-center translation removal, and the quartic small-mass coefficient. In particular, reject any future claim that the left-end phase difference is an internal detector observable unless a physical baseline is explicitly part of the experiment.

**NEXT:** move from separated 1D cavities to **two degenerate or near-degenerate 3D EM eigenmodes sharing the same physical cavity and center**, so ordinary translation phase cancels by construction. Use the 2026 covariant eigenmode-overlap framework (including elastic boundaries) to ask whether a polarization/shape ratio exists with O(m_T^2/omega^2) sensitivity while canceling h, B0, Q and detector placement. If that also collapses to a generic dispersion or material-response observable, close the finite-cavity branch as conventional inverse-Gertsenshtein engineering rather than a new Cone gravitational law.
