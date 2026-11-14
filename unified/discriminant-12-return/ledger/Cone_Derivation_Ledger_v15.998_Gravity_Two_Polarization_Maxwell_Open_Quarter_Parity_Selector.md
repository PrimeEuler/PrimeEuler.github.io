# Cone Derivation Ledger v15.998 — Two-polarization Maxwell–K4 cavity: allowed plus/cross vertex pair and symmetry-vetoed open-quarter source

**Date:** 2026-11-14 US Eastern. **Lane:** Gravity. **Owner:** continue the two-electromagnetic-polarization physical source test after v15.997, checking specifically whether the sourced K4 mixed-tensor 0↔4 kernel activates the open q2 boundary T rather than declaring all nonlinear dynamics equivalent. **Status:** [D] exact canonical two-polarization Maxwell vertices and 1↔3 cavity overlaps; [D] exact cross-photon conversion, plus-photon squeezing and algebraically admissible O4 product; [D] cross-tensor-only K4 mixing cannot provide needed plus-to-cross propagator at c0=0; [D] exact reflection Z2 veto of odd-y photon terms in the symmetric background; [N] no on-shell source, no physical q2 T amplitude or G-free observable; [O] a genuine parity-breaking background, fully sourced/mode-reduced action and quarter two-circle experimental observable.

**Redundancy / live protocol:** v15.602 originally derives the q2 original-step open boundary T, T†T=2E, and v15.628 confirms its parity L→L+2; v15.991–993 distinguish T from closed co-scaled Casimir and show required two-mode occupation transition a1†³ a2 with shell-dependent geometric normalization. v15.695 gives real curved Maxwell action; v14.928/935 frozen EH+K4 solid; v15.995 projects one electromagnetic y polarization and shows Fourier-diagonal TT exchange zero for O4; v15.996 derives pure-plus nonlinear parity/second-order canonical Hamiltonian; v15.997 derives nonzero cross-tensor 0↔4 mixing from K4 quartic b²c² **in a stipulated plus background** but proves the old y-only Maxwell vertex does not read cross tensors linearly. Latest independently completed Audit seen is Round 584/v15.994, commit f4294536e796d0a2e2424ca51c127f85ba94c521, verifying v15.991–993. No Audit confirmation yet for v15.995–997. **Immediately prewrite master HEAD** ca1e8b96aaf2d39d6235e408374dcf3b5f2a2924, exact script. Target absent. Strict additive only; frozen Suzuki, Audit, Muse, Sandbox and prior certified objects preserved.

## Gate 834 — two real Maxwell polarizations and canonical metric coupling

Use the same transversely homogeneous fixed-wall cavity as v15.995, z∈[0,π], with vector potential A=(A_x,A_y,0) and transverse metric G=exp(2S), S=[[b,c],[c,−b]], and g00=−1,gzz=1. In the restricted ansatz, the Maxwell action per transverse area is

**L_EM=1/2∫ [dot A^T G^(−1) dot A−A' ^T G^(−1) A']dz**,

and the exact photonic canonical Hamiltonian at prescribed b,c is **H_EM=1/2∫ [p^T G p+A' ^T G^(−1) A']dz** (treating the z-dependent kernel and its inverse before truncation). Its first-order gravitational couplings are

**H_plus=∫ b[(p_x²−p_y²)−(A_x'²−A_y'²)]dz**,
**H_cross=2∫ c[p_x p_y−A_x'A_y']dz**.

These follow from the actual Maxwell kinetic term, not a guessed effective spin interaction. A fully gauge-constrained conducting 3D cavity and dynamic metric constraints are still open; the present spatial and polarization truncation is the same explicitly scoped 1D laboratory comparator used in earlier gates.

Choose a physical x-polarized standing photon mode e1(z)=sqrt(2/π)sin z, frequency ω1=1, and y-polarized e3(z)=sqrt(2/π)sin 3z, frequency ω3=3. Canonical oscillators (ℏ=1) obey q_n=(a_n+a_n†)/sqrt(2ω_n), p_n=−i sqrt(ω_n/2)(a_n−a_n†).

## Gate 835 — projected plus and cross vertices with correct momentum sign

For a cross-polarized tensor spatial mode c_k(t)cos(kz), the exact intermode overlap matrices yield

**(C13,D13)_(k=0)=(0,0)**,
**(C13,D13)_(k=2)=(1/2,3/2)**,
**(C13,D13)_(k=4)=(−1/2,3/2)**,
**(C13,D13)_(k=6)=(0,0)**,

where C13=∫cos(kz)e1e3 and D13=∫cos(kz)e1'e3'. Substituting into the true Hamiltonian gives

**V_cross,2=−sqrt3(a_x a_y+a_x† a_y†)** (pair creation/annihilation),
**V_cross,4=−sqrt3(a_x a_y†+a_x† a_y)** (interpolarization photon mode conversion).

The homogeneous k=0 cross mode has **no vertex between this particular mode-1 x photon and mode-3 y photon**. A homogeneous k=0 plus metric mode DOES squeeze x-mode 1:

**V_plus,0=−(a_x²+a_x†²)**.

Normal ordering changes only constants or lower-order terms, not these quadratic terms. All formulas reflect the actual Maxwell Hamiltonian, not only a Lagrangian field-overlap surrogate.

## Gate 836 — the right two physical vertices generate the required quartic SYMBOL but need a forbidden plus/cross metric propagator

The product of physical Maxwell vertices admits the desired normal-ordered monomial **O4=(a_x†)³ a_y**. Its highest-degree coefficient in the symmetrized product is exactly

**coeff_O4(V_plus,0 V_cross,4+V_cross,4 V_plus,0)=2sqrt3**.

This is a POSITIVE kinematical finding: *if* a physically sourced off-diagonal graviton propagator **D_(plus,0;cross,4)** existed, an effective four-photon term would be allowed, subject to its energy/mode/phase normalization. It is not a demonstration that such a propagator has been derived or that O4 equals the original q2 T.

The frozen isotropic K4 material invariant of v15.997 is **J(b,c)=J(sqrt(b²+c²))**, so **J(b,−c)=J(b,c)** at every b, and **∂²J/(∂b ∂c)|_(c=0)=0** exactly. On a *plus-only* b0(z)=Bcos2z background, the quartic term b²c² modifies a **cross–cross** tensor quadratic kernel and creates a legitimate c0↔c4 overlap. It does NOT create a plus0↔cross4 mixed quadratic kernel. The EH term in the stated isotropic reflection-invariant transverse ansatz respects the same c→−c parity. A cross-only pair of Maxwell vertices is also even under y-photon parity and cannot generate odd-y O4.

The mechanism proposed at the end of v15.997 therefore fails within the same reflection-symmetric b-only background *even after including a second photon polarization*: the required two vertices exist, but their physical tensor exchange has zero b–c propagator.

## Gate 837 — a stronger Z2 source-selection statement and exact scope

The spatial reflection y→−y maps **A_x→A_x**, **A_y→−A_y**, **b→b**, **c→−c**. With an isotropic K4 solid, conducting boundary conditions symmetric under this reflection, and zero imposed cross-polarized background/source, the K4+Maxwell action and background are invariant. Integrating out dynamical cross tensor c in a symmetry-preserving state cannot produce an *effective photon-only operator odd in the y field*, such as **(a_x†)³ a_y**, without an external parity-breaking spurion. This Z2 selection holds to all perturbative orders **within this restricted reflection-symmetric system**, stronger than a single exchange-order zero, and is independent of the detailed spatial kernel. It is a separate photon-polarization/reflection symmetry, NOT the formal q2 quarter-shell χ parity from v15.628.

A genuine cross-polarized background, anisotropic medium or non-reflection-symmetric boundary could break the selection and supply a b–c mixing, but its field equation/source, amplitude and physical photon mode overlaps must be derived. In a fully generic metric or nonsymmetric apparatus the Z2 veto need not hold. Also the target photons having orthogonal physical polarizations is a **chosen physical realization** of the two oscillator labels; it does not exclude same-polarization higher-order interactions in another realization.

## Gate 838 — original q2 boundary normalization remains a distinct hurdle

The operator T of v15.602/991 connects the original-unit-step open quarter shells j=L/4 and j'=j+1/2 with fixed boundary squared weight **w_L=(L+1)/4**, so its amplitude is sqrt[(L+1)/4]. The ordinary quartic O4 in a two-mode canonical Fock embedding has amplitude sqrt[L(L+1)(L+2)]. Even if the required parity-breaking plus/cross exchange were sourced, matching the entire T tower would still require a physical shell-dependent normalization **1/[2sqrt(L(L+2))]**. No coefficient from the frozen K4/Maxwell action currently selects this profile. Neither the nonzero conditional 2sqrt3 quartic symbol nor the previous tensor overlap sqrt2/4 is a physical q2 transition rate or a measured gravitational effect.

**Reproducer:** `research-notes/k4_twopol_quarter_boundary_v15_998.py`, commit **ca1e8b96aaf2d39d6235e408374dcf3b5f2a2924**. A matching local Python script actually executed with exact SymPy to PASS: k=0,2,4,6 overlaps, both quadratic photon-polarization vertices, symmetrized product O4 coefficient 2sqrt3, odd/even y-photon parity, isotropic K4 mixed b/c second derivative zero, and v15.997 cross–cross spatial overlap sqrt2/4. External independent Audit pending.

**Verdict:** We found the actual sourced Maxwell operators needed *individually*, but the frozen symmetric K4 background cannot correlate them at quadratic tensor order. The open quarter-ladder remains a nontrivial geometric two-circle boundary map, not a physically derived photon/graviton transition. This is a sharp symmetry-based negative with a conditional positive construction; no G-free dimensionless observable or fundamental frequency derived.

**NEXT / HANDOFF Audit/Muse:** independently verify exact x/y polarization Hamiltonian signs and k overlaps, y-reflection parity, absence of b–c Hessian in isotropic K4 plus background, and distinction from quarter-shell χ. Pursue a **fully sourced** cross-polarized or anisotropic K4 background (after constraints), if there is a physical rather than invented reason for it; alternatively investigate same-polarization photons and multi-spatial-mode couplings, where this specific Z2 veto need not apply. Preserve exact T boundary amplitudes and test shell-by-shell after any physical source is obtained.
