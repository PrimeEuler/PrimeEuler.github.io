# Cone Derivation Ledger v15.793 — Gravity: finite-arm spatial sampling exposes isotropic tidal curvature leakage and detector-rank loss

**Date:** 2026-11-12 US Eastern. **Parents:** v15.750 evolved compact canonical matter; independently audited v15.760 three-arm local Fermi electric-Weyl tomography and matched GR+solid null; v15.761 anisotropic Ricci; v15.787 directly derived full S/V/T Fermi electric Riemann (with confirmed original reproducer shape defect); v15.788 independently audited complete compact-source three-channel curvature; additive v15.792 repair of the original v15.787 reproducer. **Prewrite live HEAD:** dc49135554481f3cc7dcf8691948cc367225e34d. Proposed path checked absent; Suzuki and historical sources untouched.

**Status:** [D] exactly calculated spatial line-averaged plane-Fourier full tidal curvature contractions at finite arm separation; [D] explicit isotropic full-Riemann leakage into nominally tracefree differential-arm scalar channel; [D] conditional loss of invertibility at finite wavelength; [C] a finite-arm true detector measurement; [N] any new Cone-specific interaction, coupling or experimental prediction.

## Gate 407 — define a finite-separation spatial-sampling proxy explicitly

Consider a local orthonormal frame at one time and plane-Fourier full electric Riemann curvature of the form

**R_ij(x)=e^(i k n·x) [ (R_tr/3)δ_ij + S(n_i n_j−δ_ij/3)+V(n_i e_j+e_i n_j)+T(e_i e_j−b_i b_j)]**,

where (n,e,b) is an orthonormal basis and only the three selected helicities appear. For an arm from x=0 of proper spatial length L and direction u, define the *mathematical proxy*

**A_u(L)=(1/L)∫_0^L u_i u_j R_ij(su) ds**.

This is a spatial average at fixed time. It is **not** an exact Fermi finite-arm geodesic-deviation observable: full finite-separation geodesic connections, mirror dynamics and causal light-travel transfer are omitted. If q=kL and μ=n·u, the integral has the elementary complex Fourier transfer

**F(q μ)=∫_0^1 e^(i q μ v)dv = e^(i q μ/2) sinc(q μ/2)**,

with F(0)=1.

## Gate 408 — exact three-arm spatial response and isotropic leakage

Reuse the v15.760 local arm pairs: first (n,e); second (e,b); third ((n+e)/sqrt2,(n−e)/sqrt2). Define the difference of each pair's spatial-averaged projections, A_i=A_u−A_v. Let F_1=F(q), F_3=F(q/sqrt2). For source coefficient vector (S,V,T) and R_tr=tr(R), direct exact index contraction gives

**(A1,A2,A3)^T = M(q)(S,V,T)^T + ((F_1−1)R_tr/3,0,0)^T**,

where

**M(q)=[[(2F_1+1)/3,0,−1], [0,0,2], [0,2F_3,0]]**.

At the local limit q→0, F_1=F_3→1, the isotropic-leakage vector vanishes and

**M(0)=[[1,0,−1],[0,0,2],[0,2,0]]**,

exactly reproducing the audited v15.760 three-arm tensor matrix for the restricted S/V/T basis. At finite q, however,

**A1 contains (F_1−1)R_tr/3**.

Thus *even the isotropic electric-Riemann curvature* leaks into a nominal differential-arm tracefree combination when the two arms sample **different spatial wave phases**. It is mathematically unsafe to invert the local Weyl/tracefree matrix M(0) against these finite-arm proxy readouts without also determining the isotropic contribution or changing the readout geometry. This is a sampling-geometry effect, not an extra K4 gravity coupling.

## Gate 409 — exact finite-arm response rank warning

The determinant of the S/V/T response *conditional on independently known R_tr* is

**det M(q)=−4(2F(q)+1)F(q/sqrt2)/3**.

The vector channel in this particular arm geometry is suppressed when

**q=2π sqrt2 m**, m=1,2,...,

because F(q/sqrt2)=0 and the response matrix loses rank. Thus the existence of a vector gravitational mode does not guarantee vector detectability for arbitrary finite arm length and wavevector geometry even if the source excites it.

For q=1, the longitudinal-arm sampling factor is **F(1)=sin(1)+i[1−cos(1)]≈0.84147+0.45970i**, giving an isotropic contribution **(F(1)−1)R_tr/3≈(−0.05284+0.15323i)R_tr**. Such complex Fourier phases are not directly measured complex accelerations; real fields are formed by pairing ±k.

This is a **negative detector-selection control**, rather than a physically complete instrument response. A physical light interferometer has an additional frequency-dependent **time-of-flight** transfer, unlike this fixed-time proxy; that is separated in v15.794.

**Reproducer:** research-notes/k4_finite_arm_spatial_curvature_sampling_v15_793.py, additive commit **124063adf0258c8ec32c1247623a5e04419da960**. The finite-arm matrix, local limit, trace leakage, vector null and determinant formulas were independently tested in an equivalent local SymPy calculation to PASS. New committed script still awaits external independent audit. Original v15.760–788 objects preserved.

**HANDOFF — independent audit:** independently derive the finite spatial-averaging integral including the isotropic Ricci contribution, local-limit matrix and finite arm determinant. Ensure this proxy is **not** misreported as a complete photon/mirror detector transfer. Check v15.792 additive repair script against original historical v15.787.

**NEXT:** compare this fixed-time averaging toy transfer with causal null-ray sampling, then extend to fully perturbed FLRW K4 scalar/vector/tensor photon propagation and free mirrors. Matched EH+solid detector difference remains identically zero unless Cone supplies an independently justified new physical operator.
