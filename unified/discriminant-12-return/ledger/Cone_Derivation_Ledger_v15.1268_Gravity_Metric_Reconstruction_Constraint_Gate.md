# Cone Derivation Ledger v15.1268 — Metric-reconstruction readiness and independent-constraint gate after shared-Nyquist Maxwell weld

**Date:** 2026-11-20 Eastern. **Lane:** Gravity/Cone. **Status:** [D] review of exact archived gauge and metric-to-curvature requirements; [O] byte-original v15.1267 wrapper replay and independent full ADM constraints; [O] time-dependent 4-metric and causal photon/mirror/clock detector. **Prewrite inspected HEAD:** e93a79e6139b4c08a7e827e467835cc3c2000aae. New target path v15.1268, no modification of previously certified sources, Audit, Muse/Sandbox, or Suzuki.

## Gate 1211 — what the corrected numerical result does and does not prove

The historical v15.1266 combined wrapper first failed its strict Maxwell mean matching. The additive v15.1267 shared Nyquist-plane source prescription was tested using **locally equivalent source implementations** at N=32,40,48 and gave the reported pointwise R00 trace residuals 1.33e-15, 1.78e-15, 1.78e-15. The **exact newly committed v15.1267 Python wrapper** still awaits external independent execution. The trace test remains a consequence of the sourced tidal transfer plus the homogeneous Friedmann solution; it is not a test of the other Einstein equations.

The two parent files were re-inspected: `k4_compact_maxwell_full_grid_mean_subtracted_riemann_v15_1262.py` computes P,V,T and their time derivatives but only returns the final electric tidal tensor and condensed diagnostics. Its `Phi` and `Bv` are on-shell source-dependent derived potentials; the homogeneous v15.1264 code returns u, beta, beta_dot and diagonal tidal curvature. No existing combined file emits four-metric histories on a common mesh.

## Gate 1212 — explicit gauge-and-constraint obligation

Archived v15.787 uses the coasting background `a(tau)=tau/sqrt(3)` with sign convention (-+++). Its scalar Newtonian metric is `g00=-(1+2 Phi_N)`, `gij=a²(1-2 Psi_N)delta_ij`. Its vector gauge has `g0i=-a B_i`, and TT spatial perturbation `gij=a²(delta_ij+gamma_ij)`. The homogeneous v15.1264 Bianchi-I sector requires additionally the isotropic scale perturbation u and tracefree beta_i. A first-order single-gauge spatial composition to be independently checked is therefore

`g_ij = a² [(1+2u-2 Psi_N)delta_ij + 2 diag(beta_i) + gamma_ij]`

with corresponding `g00` and `g0i` above. **This is a metric reconstruction target, not a demonstrated time-dependent solution.** In particular, verify the exact definition of u against v15.1264's Hamiltonian perturbation and the scalar/vector source-to-potential gauge conventions before equating this target with a solved metric. Retain all common-scale and perturbative-order factors. Bianchi-I homogeneous perturbations and nonzero Fourier modes must not be gauge-fixed inconsistently.

The correct scalar source-to-Bardeen map, including spatial pressure source and the scalar Ward identity, is archived in v15.729; its `Phi_N` and `Psi_N` must be applied with the **same source normalizations and Fourier conventions** as v15.1262, not by matching superficially similar variable names. The v15.787 independent metric-to-Riemann calculation gives necessary unit tests for the reconstruction:
- scalar longitudinal STF electric tide coefficient `-k² Phi_N/a²`, while Weyl uses `k²(Phi_N+Psi_N)/(2a²)`;
- transverse vector electric tide `-i k(Bv'+Bv/tau)/(2a)`;
- TT electric tide `-(gamma''+2gamma'/tau)/2`.
These are **necessary curvature checks**, not sufficient conditions for the Einstein Hamiltonian and momentum constraints. A purely electric-curvature inverse cannot determine the full metric uniquely.

## Gate 1213 — falsification-first execution order

1. Clean-checkout replay of byte-original v15.1266 (expect the documented finite FFT mismatch) and v15.1267 (expect strict three-grid pass); check Nyquist source Hermiticity and `q·Ehat=0` before Maxwell evolution; independently verify nonzero and homogeneous mean pressure and Maxwell energy conservation rather than merely the total trace.
2. Extend the solver *additively* to return per-time `Phi_N, Psi_N, B_i, gamma_ij, u, beta_i`, not just Riemann; preserve existing parents untouched; lock one shared gauge and initial-value convention. The current v15.1262 run retains P,V,T internally, so a guarded in-memory return exposure or a separate faithful source reproducer is required.
3. Rebuild linearized `G00,G0i,Gij` from the resulting metric and independently build the **same** Maxwell plus elastic-solid `T_ab`. Report max, RMS, and Fourier-mode normalized residuals for Hamiltonian, momentum, traceless spatial and trace sectors on all grids/time slices. Check continuity/constraint propagation.
4. Only after those constraints pass, integrate physical emission-clock proper time, both null legs, mirror geodesics and detection against identical GR+same-K4-solid initial and boundary data. Distinguish periodic finite-box physics from isolated packet physics and test spatial/time convergence.

**Negative/novelty status:** neither the `1/4` arithmetic mesh nor Maxwell Nyquist regularization inserts an independently justified Cone gravitational interaction. The exactly matched Einstein–Maxwell+identical-K4 comparator remains zero-difference. No new detector prediction claimed.

**AUDIT:** review the precise v15.729 source Ward and v15.787 metric gauge conventions, determine whether v15.1262's source symbol mapping is fully identical, independently run v15.1267, and require Hamiltonian/momentum checks before approving full spacetime or optical claims.
