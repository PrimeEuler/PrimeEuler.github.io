# Cone Derivation Ledger v15.996 — K4 pure-plus cubic parity and actual second-order Maxwell Legendre transform

**Date:** 2026-11-14 US Eastern. **Gravity lane.** **Owner:** continue nonlinear K4/Maxwell source search after v15.993, with open q2 boundary T and genuine field action. **Status:** [D] exact K4 solid transverse-shear scalar invariant to sixth order, b→−b parity, pure-plus cubic absence in symmetric one-polarization ansatz; [D] exact second-order metric Maxwell canonical Hamiltonian source in a selected two-mode cavity, including its nontrivial momentum inversion; [N] no bare a1†³ a3 term, and no mode-conversion or lower-mode squeezing in that b² coefficient; [O] full mixed-helicity, inhomogeneous, ADM-constrained nonlinear K4 and actual physical boundary coupling.

**Parents and redundancy:** v14.928/935 frozen EH+elastic-solid K4 with invariant J(B)=tr(B²)/(tr B)²−1/3 and isotropic FLRW material background; v15.833 exact K4 diffeomorphism Ward; v15.695 genuine curved Maxwell action L=1/2 exp(2b)(dot A_y²−A_y'²); v15.991 original-unit q2 open two-circle T; v15.992/993 quartic operator and shell mismatch; v15.995 exact leading linear bF² mode projection and Fourier-diagonal tensor-exchange zero. Audit Round 584/v15.994 commit f4294536e796d0a2e2424ca51c127f85ba94c521 verified v15.991–993 with no corrections. **Prewrite live HEAD:** 21c0a5d5220e8329b69bd294b90a399d251e777c, exact reproducer; target absent. Additive only; prior certified/Audit/Suzuki/Sandbox/Muse objects preserved.

## Gate 826 — purely plus-polarized cubic K4 solid source is forbidden by transverse interchange symmetry

Choose the physical plus-only isotropic tensor ansatz γ=diag(2b,−2b,0) with metric spatial g_ij proportional to diag(exp(2b),exp(−2b),1). For frozen isotropic K4 solid material B^IJ∝diag(exp(−2b),exp(2b),1), with detB independent of b. The archived elastic scalar invariant becomes

**J(b)=[exp(4b)+exp(−4b)+1]/[exp(2b)+exp(−2b)+1]²−1/3.**

Exactly **J(−b)=J(b)**, and its series is

**J(b)=8b²/9−8b⁴/9+112b⁶/135+O(b⁸)**.

The full Einstein–Hilbert plus isotropic solid action is invariant under x↔y combined with the corresponding exchange of material labels, which maps b→−b and leaves a pure b(z,t) spatial profile in this ansatz invariant otherwise. Thus all *pure-plus* odd vertices, notably b³, vanish for this background. The b² coefficient reproduces v14.928 J=(1/9)trγ²+... since trγ²=8b². This is a **restricted single-plus polarization symmetry**, NOT an assertion that all 3-graviton interactions of GR or K4 vanish: cross-polarization, longitudinal/constraint, scalar/vector and inhomogeneous couplings need independent treatment.

In particular, the hypothetical three-plus-mode nonlinear graviton vertex which would mix k=0,2,4 through b³ is absent in this symmetric ansatz. This strengthens the single-tensor-exchange negative from v15.995 but is not a universal nonlinear gravity prohibition.

## Gate 827 — real second-order b²F² term has k=0 and k=4 harmonic pieces

Reuse the exact *same* v15.995 fixed-wall A_y model on z∈[0,π] with modes e_1=sqrt(2/π) sin z, e_3=sqrt(2/π) sin(3z), and b(t,z)=B(t)cos(2z). Expand the actual Maxwell kinetic factor exp(2b)=1+2b+2b²+... and define

**C_2=(∫cos(2z)e_i e_j)=[[-1/2,1/2],[1/2,0]]**,
**D_2=(∫cos(2z)e_i'e_j')=[[1/2,3/2],[3/2,0]]**.

At b² order the spatial weight is cos²(2z)=(1+cos4z)/2, giving

**C_22=[[1/2,−1/4],[−1/4,1/2]]**,
**D_22=[[1/2,3/4],[3/4,9/2]]**.

This is a genuine gauge-consistent *quadratic photon source* from the nonlinear metric dependence, and it contains mixed spatial profiles even though the background has one b harmonic. However, the LAGRANGIAN source overlaps are not yet the quantum interaction Hamiltonian. The photonic canonical momenta themselves change with b.

## Gate 828 — Legendre transform cancels an apparent physical conversion

The exact quadratic two-mode photon Lagrangian kinetic matrix to this order is **G(B)=I+2B C_2+2B² C_22**. Its inverse is

**G⁻¹=I−2B C_2+B²(4 C_2²−2 C_22)+O(B³)**.

The potential quadratic matrix is **diag(1,9)+2B D_2+2B² D_22**. Thus the *canonical Hamiltonian's* B² coefficient is

**V^(2)=p^T(2 C_2²−C_22)p+q^T D_22 q**

with **2C_2²−C_22=[[1/2,−1/4],[−1/4,0]]**.

Using q_m=(a_m+a_m†)/sqrt(2ω_m), p_m=−i sqrt(ω_m/2)(a_m−a_m†), ω1=1,ω3=3, the exact degree-two polynomial in commuting Weyl/leading normal symbols is

**V^(2)=[4a1a1†+2sqrt(3)(a1a3+a1†a3†)+3(a3²+2a3a3†+(a3†)²)]/4**.

In particular **coeff_(a1†²)=0**, **coeff_(a1†a3)=0**, while **coeff_(a1†a3†)=sqrt(3)/2≠0**. Normal-order corrections produce only lower-degree or constants and do not change the selection. A naive Lagrangian-only reading of b² overlaps would misidentify a nonzero mode-conversion process; the momentum inversion cancels it. No *bare* quartic **O4=(a1†)³a3** can arise at this order because V^(2) is exactly quadratic in the photon operators at prescribed metric.

The nonzero b² pair terms show the nonlinear Maxwell coupling is NOT trivially zero; it simply has the wrong operator structure for the desired original-unit-step open-q2 T in this tested mode geometry.

## Gate 829 — implications for physical open-boundary exchange

The original q2 boundary T survives unchanged as a rigorous geometric cross-shell operator, T†T=2E and j→j+1/2. v15.995 excludes the requested O4 from leading homogeneous single-tensor exchange in the specified (1,3) photon-mode truncation; the present gate excludes a *pure-plus cubic metric self-interaction* and shows the canonical second-order Maxwell contact term has different photon selection. Neither result closes the complete nonlinear K4+Maxwell question, which could involve mixed tensor polarization, scalar/constraint mediation, nonlinear mode mixing, material interfaces or inhomogeneity. An effective coupling, when found, must still reproduce the shell-dependent boundary normalization 1/[2sqrt(L(L+2))], rather than inserting this factor by hand.

**Exact local reproducer:** `research-notes/k4_nonlinear_plus_metric_v15_996.py`, additive commit **21c0a5d5220e8329b69bd294b90a399d251e777c**. SymPy PASS for exact K4 invariant parity and expansion through b⁶, 1D Maxwell overlaps, full canonical inverse G and B² Hamiltonian coefficients including canceling conversion. Independent Audit pending.

**NEXT / HANDOFF Audit and Muse:** independently verify x↔y symmetry only for the pure plus/isotropic sector; check the solid invariant coefficient 8/9; test canonical second-order Legendre transform rather than raw b² Lagrangian as Hamiltonian; check quantum ordering; compare with the true 3+1 cavity and mixed-helicity K4 response. If searching a positive path, derive an actual three-mode (mixed-helicity) or inhomogeneous metric coupling before assigning a nonzero q2 boundary source. Never equate the k0/k4 harmonic decomposition of cos²(2z) with an independently propagating 0↔4 graviton mixing kernel.
