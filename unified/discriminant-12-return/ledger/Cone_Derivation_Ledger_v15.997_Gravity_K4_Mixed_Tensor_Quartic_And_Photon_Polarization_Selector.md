# Cone Derivation Ledger v15.997 — Mixed K4 tensor polarizations: quartic physical source for spatial-mode mixing, but detector polarization veto

**Date:** 2026-11-14 US Eastern. **Gravity lane.** User authorized continuation of v15.995–996 physical source search for original-unit open quarter boundary T; maintain the *actual* frozen EH+K4 solid+Maxwell source rather than make up a cross-circle coupling.

**Status:** [D] exact isotropic K4 transverse material invariant for both tensor polarizations and its quartic cross coupling; [D] explicit nonzero cross-tensor 0↔4 harmonic overlap in an assumed spatially patterned background; [D] leading Maxwell linear coupling to cross graviton vanishes in previous single-y-photon reduction; [N] no source-free cubic tensor mixer in restricted 1D unimodular 2pol ansatz; [C] hypothetical background-induced cross-tensor mixing requires an on-shell source and full constraint equations; [O] mixed-EM-polarization detector, on-shell background, full Einstein constraints, boundary selection and actual T amplitudes.

**Audit/redundancy/HEAD:** v14.928/935 source action S_m=−∫√−g C b_solid^(2/3)(1+η J(B)); v15.833 gauge Ward; v15.695 curved-Maxwell source (repaired at v15.701); v15.602/628 original-unit quarter defective ladder and parity-preserving cross-shell T; v15.991–993 correct open-boundary and quartic occupation selection; v15.995 single-y 1D mode projection, diagonal-TT-exchange selection; v15.996 plus-only odd-cubic null and second-metric-order Legendre cancellation. Most recent independent Audit Round 584, v15.994 commit f4294536e796d0a2e2424ca51c127f85ba94c521, verified v15.991–993 with no mathematical corrections. v15.995–996 pending. **Immediately prewrite live HEAD** dbd942b2703ae6b804479b1d8aaa16309600d8e1 (two new reproducible scripts); target checked absent, additive-only; no Audit, Suzuki, Lane A, Sandbox, Muse or frozen objects edited.

## Gate 830 — two physical transverse shear polarizations of the *actual* isotropic K4 solid

On a fixed locally isotropic background, restrict the transverse spatial metric to G_perp=exp(2S), with S=[[b,c],[c,−b]] and longitudinal zz entry unity. b and c are plus/cross polarizations of the same transverse 1D tensor ansatz; this is a **restricted ansatz**, not a proof that the unreduced fully dynamical ADM tensor plus constraints closes nonlinearly. S²=(b²+c²)I, so transverse metric eigenvalues exp(±2r), r²=b²+c², and detG_perp=1.

The physical frozen K4 material invariant **J(B)=tr(B²)/(trB)²−1/3** becomes

**J(r)=[1+2cosh(4r)]/[1+2cosh(2r)]²−1/3**.

Exact expansion:

**J(r)=8r²/9−8r⁴/9+112r⁶/135+O(r⁸)**.

Consequently there is no cubic term in the material potential of b,c, but a definite quartic **J_4=−(8/9)(b⁴+2b²c²+c⁴)**, whose mixed coefficient is **−16b²c²/9**. This is directly from the frozen constitutive action, not a newly postulated quartic physical potential. In the local action L_solid=−C η J (suppressing positive background scale/volume factors), the mixed local Lagrangian term is **+(16/9)Cη b²c²**.

For the homogeneous isotropic 1D pure-tensor sigma kinetic term, write A_mu=G^-1 ∂mu G and expand with S and V_mu=∂mu S. The leading coefficients are A1=2V_mu, A2=2[V_mu,S], and tr(A1 A2+A2 A1)=0 identically. This checks the *sigma-type kinetic* cubic null in this 1D transverse ansatz. Combined with the even elastic material potential, it supplies no cubic bbc mode mixer **within this restricted geometry**. Not a theorem against all Einstein–Hilbert cubic interactions in full 3+1, mixed directions, constraint-mediated terms, nonisotropic media or all polarizations.

## Gate 831 — a physically derived quartic background-dependent cross-polarization harmonic mixer is nonzero

Assume *conditionally* a real plus-polarized spatial background b0(z)=B cos(2z), z∈[0,π]. It is not yet established as a constraint-consistent sourced/on-shell K4 geometry. Expand the mixed solid interaction to quadratic order in a small cross perturbation c:

**ΔL_solid^(c²) = +(16/9)Cη B²cos²(2z)c²** times the suppressed positive local measure.

Let normalized real tensor spatial modes be e0=1/sqrtπ and e4=sqrt(2/π)cos4z. The exactly computed overlap is

**I_04=∫_0^π e0 e4 cos²(2z) dz = sqrt2/4 ≠ 0.**

Because c² has a 2c0c4e0e4 term, the solid *Lagrangian* mixed-mode coefficient is

**ΔL_(c0 c4) = (8 sqrt2/9)Cη B² c0c4** (again up to physical measure/scale factors).

Thus the **actual K4 quartic solid constitutive term** can yield a nonzero 0↔4 *cross-tensor* quadratic mode mixer about an externally supplied inhomogeneous b0 background. This is an explicit positive action-level structural path beyond the v15.995 homogeneous Fourier-diagonal tensor propagator. It does *not* mean the full gauge-complete K4 wave kinetic/constraint system has this same coefficient without additional terms or possible cancellation. Its strength is proportional to B² and the independently unselected Cη and hence is **not universal**.

## Gate 832 — the previous single-y-photon cavity cannot read this cross-tensor mixer at first order

The earlier v15.995/v15.996 Maxwell cavity uses only A_y(t,z). The transverse metric inverse is exp(−2S). Its yy component is

**g^yy=cosh(2r)+(b/r)sinh(2r)**,

which has expansion

**g^yy=1+2b+2(b²+c²)+(4/3)b(b²+c²)+...**.

Every term is **even in c**, and in particular **∂g^yy/∂c at c=0 is zero**. Since the retained field strengths F_ty and F_zy involve only y, the Maxwell action to first order in c contains no cross-tensor y-only vertex. By contrast the inverse off-diagonal metric has **g^xy=−2c+...**, and could enter if the actual photon field has both x and y polarizations (or further genuine components/medium). Thus the new c0↔c4 material mixing does not automatically connect to the old y-only source vertices V_0,V_4 or supply the wanted O4=(a1†)³a3. This is a **polarization selection obstruction**, not a universal zero for multi-polarization Maxwell systems.

## Gate 833 — physical and mathematical verdict

**Positive:** Nonzero background-induced off-diagonal cross-tensor mixing is present in the frozen K4 constitutive action, with exact quartic coefficient −16/9 and spatial harmonic overlap sqrt2/4. This represents a physically motivated mechanism *conditional on a real inhomogeneous on-shell background* rather than a guessed offdiagonal tensor propagator.

**Negative:** Neither the restricted isotropic two-polarization pure tensor sector nor the single-y Maxwell projection yields the original q2 open-boundary physical coupling by itself. The source b0, true tensor propagator after constraints, photon polarizations, mode normalization, couplings and the q2 shell-dependent amplitude 1/[2sqrt(L(L+2))] are still required. The boundary map T remains exact as a geometric operator with T†T=2E, parity L→L+2 unchanged, but has not been obtained as a physical Maxwell/K4 matrix element. No parameter-free, G-independent gravity/tidal observable or inferred rest mass is established.

**Exact witnesses locally run to PASS:**
- `research-notes/k4_mixed_tensor_quartic_v15_997.py`, commit **6f6e9b5975f8982804b45b5f880ecef6e4eeb3c0**: symbolic S², 1D sigma cubic trace, full material J expansion, b²c² cross, I04 and local solid Lagrangian coefficient.
- `research-notes/k4_mixed_tensor_cross_photon_selection_v15_997.py`, commit **dbd942b2703ae6b804479b1d8aaa16309600d8e1**: inverse metric yy and cross derivative, nonzero gxy cross channel.

**NEXT:** construct a gauge-complete two-photon-polarization Maxwell readout in the same real b0-sourced K4 geometry, with full 3+1 boundary conditions; solve Einstein–solid constraints for b0, compute dressed c0/c4 propagator and check the induced physical O4 matrix element and all-shell ratio. In particular check whether a cross-polarized tensor in a 1D cavity with two photons of different transverse polarizations actually supplies both squeeze and conversion vertices at needed harmonics. If it fails, report a rigorous channel-specific negative rather than assuming extra mode mixing.

**HANDOFF Audit/Muse:** verify exact J(r) formula/coefficient, EH sigma kinetic restricted cubic trace and its limited interpretation, I04 normalization, local Lagrangian sign vs Hamiltonian after constraints, and absent single-y linear cross coupling. Insist on real sourced b0 and a gauge-complete measurable photon readout before promoting this to a dynamical EM↔quarter source.
