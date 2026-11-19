# Cone Derivation Ledger v15.1228 — Compact Maxwell Cauchy packet exact first-time K4 scalar tidal jet, Yukawa evolution, and finite-arm spatial-proxy slope

**Date:** 2026-11-19 Eastern. **Gravity/Cone track. Status:** [D] source-first exact first time derivative of the *full electric-Riemann scalar tracefree Fourier coefficient* for the original compact Maxwell initial Cauchy packet, including physical Maxwell parity/conformal time evolution, the sourced solid mode P''' and pressure-corrected Bardeen constraints; [D] real-space noncompact Yukawa-kernel first-time response and the first derivative of the fixed-time spatial two-arm proxy for a specified unit-width benchmark; [N] these coefficients are conventional Einstein–Maxwell+same K4 relativistic-solid, not a quarter-grid/gravity novelty; [O] complete 3D Maxwell+K4 propagation beyond the first Taylor jet, k=0 cosmological mode, and causal photon/free-mirror/emitter-clock/endpoint detector. **Immediately prewrite live HEAD:** d315aceb528b62e64d67021c8b2d61f7aedcf224. Gravity v15.1227 already belongs to Lane A's concurrent correctly placed R4 extension. v15.1228 target checked unused. Additive-only: no edits to Lane A/Suzuki, Audit, Sandbox/Muse, certified v14.935 actions or historical scripts.

## Precedents and precise contribution
The actual compact divergence-free vacuum-Maxwell Cauchy data were frozen in v15.1078: `Psi=A f(x/a)f(y/b)f(z/c)`, `E=(partial_y Psi,-partial_x Psi,0)`, `B=0`, `f(u)=(1-u²)^3` on |u|<1 and zero elsewhere. The nonzero longitudinal Fourier stress, Ward initial jets and transverse TT were v15.1081/1085. Gravity v15.1226 repaired a sign dictionary and a **missing J_Phi''** bug from v15.1222, restoring the Einstein isotropic Ricci trace and deriving the *initial* K4 scalar STF convolution `S_K4(z,1)=-(9R0/2)[g+Y*g]`, with compact longitudinal source `g(z/c)=(1-(z/c)²)^6` and 1D kernel `Y(z)=exp(-|z|)/2`. The former v15.793/v15.1196/v15.1226 finite-arm quantity is an **equal-time curvature spatial-averaging proxy**, not a physical photon path.

**New question solved here:** how does the *same K4 scalar full electric Riemann STF* start changing in cosmic time due to the *real Maxwell free evolution*, with no arbitrary pump clock or fitted source time profile? Does the previously derived Yukawa spatial channel persist at first time order? What is the first derivative of the specified compact spatial proxy?

## Gate 1172 — correct second conformal Maxwell source jet and parity
The free conformal Maxwell equations from initial `B(0)=0` imply `E(ξ)` is *even* and `B(ξ)` is *odd* in conformal time ξ about the initial slice, for the fixed spatial source. Hence conformal `rho(ξ)` and spatial pressure trace are even, while the longitudinal Poynting flux is odd. For the transversely integrated Fourier mode k along z, ordinary Maxwell stress conservation provides
**R_ξ(0)=0, R_ξξ(0)=−k² R(0)**,
and the conformal momentum first derivative is fixed by `Tzz=R` on the initial slice. Since coasting `ξ=sqrt3 ln τ`, and the archived ADM source coefficients are `J_Phi=J_psi=J τ^(−1) f(ξ)` after fixing τ0=1 (the signed amplitude J includes the negative physical Maxwell coupling), the source Taylor data are exactly
**J_Phi(1)=J_psi(1)=J**,
**J_Phi'(1)=J_psi'(1)=−J**,
**J_Phi''(1)=J_psi''(1)=(2−3k²)J**.
For the longitudinal shift source `J_B(τ)=τ^(−1)M(ξ)` with **M(0)=0** and conformal parity M odd, the pressure Ward and Maxwell momentum jet imply
**J_B(1)=0, J_B'(1)=sqrt3 k²J**, and
**J_B''(1)=−3 J_B'(1)=−3sqrt3 k²J**.
The last equality follows by twice differentiating τ^(−1)M(sqrt3 ln τ) at τ=1 and using M(0)=M''(0)=0. **Do not mistake it for −9k²J**: that was a factor-of-sqrt3 typo in the first *uncommitted* scratch script and failed the exact regression; only the corrected code passed and was committed.

These are **genuine physical source time jets** at a Cauchy slice where Maxwell is already present, not a zero-past-source retarded switch-on. They are a nonzero-longitudinal-k, transversely integrated projection; the full 3D Maxwell field has additional Fourier orientations and k=0 source stress.

## Gate 1173 — K4 scalar initial acceleration and jerk
Use the complete pressure-corrected v15.728–729 scalar equation, with `beta_S=(8η_s(1+k²)−3k²)/3`:
**P''+3P'/τ+beta_S P/τ²=3sqrt3 J_psi/(2k²τ³)−9(τ J_B'+J_B)/(2k⁴τ³)**.
Impose **P(1)=P'(1)=0**, but keep source-forced constraint contacts. Direct substitution of the full Maxwell jets yields
**P''(1)=−3sqrt3 J/k²**, and differentiating the *full sourced equation before substituting values* yields
**P'''(1)=21sqrt3 J/k²**.
Both are independent of η_s at this instant because η_s enters through `beta_S P` and its first derivative `beta_S P'`, which vanish for the declared initial solid displacement and velocity. This does **not** make the subsequent K4 dynamics η_s-independent.

## Gate 1174 — full-Riemann scalar STF first-time Fourier jet
Reconstruct the physical metric lapse from the traceful v15.729 Bardeen expression
**Phi_N=[τ²P''+2τP']/[3(1+k²)]+sqrt3(J_Phi+J_psi)/[2τ(1+k²)]−3J_B'/[2k²(1+k²)]**.
The *full electric-Riemann STF* (not just Weyl) is `S(τ,k)=−k²Phi_N/a²=−3k²Phi_N/τ²`. Differentiate **before substituting the source jets**. Exact independent SymPy reduction gives
**S(1,k)=3sqrt3 J(k²+2)/[2(1+k²)]** (recovers v15.1226),
**S'(1,k)=−3sqrt3 J(7k²+10)/[2(1+k²)]**,
and the nonzero-ratio formula
**S'(1,k)/S(1,k)=−(7k²+10)/(k²+2)**.
The ratio tends to −5 as k→0 through positive k, and −7 for k→infinity; the original reduction itself is not valid at k=0 and the latter is a mathematical UV Fourier limit, not a claim about a laboratory signal. For the illustrative k²=1/2 the ratio is −27/5=−5.4. Both the source redshift and the longitudinal gravitational/solid constraint contacts contribute, so simply using a^-4 for the *STF tidal field* would be wrong.

The independent Einstein trace identity proved v15.1226, `A_iso=−sqrt3 (J_Phi+J_psi)/(2τ³)` when pressure Ward holds, gives **A_iso'(1)=−4 A_iso(1)** for the free Maxwell Cauchy initial data. This uses the *complete* source derivatives, preserving the v15.1226 repair of v15.1222. The different −4 (isotropic) and `−(7k²+10)/(k²+2)` (STF) rates are a conventional geometric response distinction, not an arithmetic q2 selector.

## Gate 1175 — explicit first-time real-space scalar Yukawa response
For a transverse-integrated longitudinal source with **physical positive conformal energy R0 g_c(z)**, signed ADM source `J(z)=−sqrt3 R0 g_c(z)` at tau0=1, the Fourier multipliers give the exact first-order expansion in `δτ=τ−1`:
**S_K4(z,τ)=−(9R0/2)[g_c(z)+(Y*g_c)(z)] +δτ (9R0/2)[7g_c(z)+3(Y*g_c)(z)] +O(δτ²)**,
where `Y(z)=e^(−|z|)/2` in the normalized K4 comoving length unit. In contrast the isotropic trace is initially local in this projection:
**A_iso(z,τ)=3R0 g_c(z)−12R0 g_c(z) δτ+O(δτ²)**.
The exact first-time STF response retains the noncompact exponential constraint tail; its first-order coefficient differs between local compact g and nonlocal Yukawa Y*g. This is an *initial-value perturbative Fourier inversion* on the longitudinal continuum with nonzero-k field equations; the source Fourier k=0, total cosmological backreaction and full three-dimensional curvature are not solved by the inversion.

## Gate 1176 — derivative of the *fixed-time spatial* two-arm benchmark
Retain exactly the v15.1226 geometry (dimensionless width c=1, R0=1, z-arm 0..L=1 and transverse x-arm at z=0), the *mathematical fixed-time spatial curvature averaging* `Delta_E=(Abar−Acenter)+(2/3)Sbar+(1/3)Scenter`. Write
**G=∫_0^1(1−u²)^6du=1024/3003**,
**Y0=(Y*g)(0)=∫_0^1 e^(−u)(1−u²)^6du**,
**Ybar=∫_0^1(Y*g)(z)dz=∫_0^1(1−u²)^6[1−e^(−1)cosh u]du**.
Using the same source without any fitting:
- `Scenter(1)=−(9/2)(1+Y0)≈−5.75817327327807`, `Sbar(1)=−(9/2)(G+Ybar)≈−2.48533697813872`.
- `Scenter'(1)=+(9/2)(7+3Y0)≈35.2745198198342`, `Sbar'(1)=+(9/2)(7G+3Ybar)≈13.5938730722783`.
- `Acenter(1)=3,Abar(1)=3G,Acenter'(1)=−12,Abar'(1)=−12G`.
- Consequently **Delta_E(1)=−5.55330538687482**, recovering v15.1226, and **Delta_E'(1)=+28.7288472295555**, with **Delta_E'(1)/Delta_E(1)=−5.1732878399693**.
These are source-normalized Fourier/proxy quantities in the coasting K4 length/time units; the arm length here is held at **fixed comoving coordinate** in the mathematical proxy, not a dynamically maintained physical baseline. The first-order approximation must not be extrapolated indefinitely; no photon null-ray propagation, moving end mirrors, emitter clock, event identification, finite arm spatial-curvature-to-optical conversion or noise is included.

## Reproducibility and Audit
**Standalone exact reproducer:** `research-notes/k4_compact_maxwell_first_tidal_time_jet_v15_1228.py`, additive SHA **d315aceb528b62e64d67021c8b2d61f7aedcf224**. The committed text reproduces the local independently executed Python/SymPy code; it ran **PASS** for the Maxwell source jet, P'' and P''' formulas, first-time STF coefficient and ratio, isotropic redshift, Yukawa real-space profile and two exact spatial proxy values. The first local scratch attempt used a wrong extra sqrt3 in JB'' and failed; this was fixed *before* committing and the corrected script is the recorded artifact. No previously certified file touched.

**AUDIT HANDOFF:** independently check Maxwell E-even/B-odd parity in conformal time for the actual compact Cauchy data, the a^-1 source-volume scaling, JB''=-3 JB' and Ward derivative, correct ordering of `J_Phi''` substitution, P''' and Phi_N' direct derivation, S'/S ratio, real-space Yukawa inverse Fourier, and width-one G/Y kernel integrals. Retest against the *original* v15.1226 initial source solution, and preserve the distinction between this early-time curvature spatial proxy and a fully causal photon/mirror/clock observable.

**NEXT:** propagate the actual 3D compact free-Maxwell packet for a finite time interval (including the induced B field), compute the full conserved 3D Tμν source at each time, solve K4 S/V/T Einstein+solid constraints with compatible k=0/background and solid initial modes, then insert the resulting metric into the already established v15.811/v15.821 photon/mirror/clock/emission-event functional. A Cone-versus-matched ordinary Einstein–Maxwell+same-solid detector residual remains identically zero absent an independently action-derived quarter-grid Q=1/16 coupling. This gate adds no new coupling, G derivation or physical gravity Casimir.
