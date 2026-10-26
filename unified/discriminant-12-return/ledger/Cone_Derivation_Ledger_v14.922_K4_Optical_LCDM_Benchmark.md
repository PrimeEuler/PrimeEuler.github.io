# Cone Derivation Ledger v14.922 — Four-factor optical distance versus observationally informed ΛCDM benchmark

Date 2026-10-26. Parent v14.921 (conditional luminosity-distance law); v14.916 gravity scope pivot; v14.818/820/821 k4 geometry. Research note research-notes/K4_Optical_Distance_vs_Planck_LCDM_Benchmark.md commit c784f90fc3797da733ccedcde0edd314433e5e68. Prewrite HEAD c784f90fc3797da733ccedcde0edd314433e5e68. Additive gravity lane; Suzuki-quarter correspondence PARKED, Suzuki/far-tail untouched. Owner protocol: ledger every substantive gate.

[D] For conditional k4 linearly coasting metric, d_C=H0 D_L/c=(1+z)ln(1+z). For Planck 2018 base flat ΛCDM Ωm=0.315, ΩΛ=0.685, d_Λ=(1+z)∫0^z[Ωm(1+u)^3+ΩΛ]^(-1/2)du. Identical H0 cancels in shape ratio. Observational benchmark sources: Planck 2018 parameter results https://www.aanda.org/articles/aa/abs/2020/09/aa33910-18/aa33910-18.html and DESI DR2 https://journals.aps.org/prd/abstract/10.1103/tr6y-kpc6 .

[N] Direct scipy quad, rounded values:
z=.1: d_C=.1048412, d_Λ=.1073576, C/Λ−1=−2.344%, Δμ=−.0515 mag;
z=.3: .3410735, .3613742, −5.618%, −.1255 mag;
z=.5: .6081977, .6580727, −7.579%, −.1711 mag;
z=1: 1.3862944, 1.5293588, −9.355%, −.2133 mag;
z=2: 3.2958369, 3.5828174, −8.010%, −.1813 mag;
z=3: 5.5451774, 5.8508289, −5.224%, −.1165 mag.
Reproducer in note.

[D] Low redshift d_C=z+z²/2+O(z³) versus benchmark q0=3Ωm/2−1=−.5275, d_Λ=z+.76375z²+O(z³). Difference is an expansion-history shape prediction, not a parameter-free demonstration of real gravity. Current comparison is theoretical curve versus cosmological fit benchmark, NOT raw supernova likelihood and NO sigma/exclusion level. Do not infer ΛCDM is exact or exclude evolving dark energy from this calculation.

[O] Next gate: direct observational fit with released Type Ia SN redshifts, distances, covariance (including nuisance normalization), plus BAO where appropriate. Separate structural gate remains identifying a covariant action/source selecting factor-Hessian geometry without frozen local spin-2 modes. No Newton G, physical metric, matter-gravity dynamics derived.

Flags: k4_benchmark_LambdaCDM=NUMERIC_CALCULATED; lowz_shape_difference=EXACT; direct_observational_fit=NOT_DONE; empirical_agreement=UNTESTED; physical_gravity=NOT_DERIVED; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-optical-observational-benchmark
parent: v14.922
status: open
action: Independently recalculate dimensionless distance integrals, low-z expansion and percentage/magnitude residuals; verify comparison to Planck base ΛCDM is not mislabeled as a direct observational likelihood and that model is physically conditional.
deliverable: scoped verdict.

NEXT: perform direct SN distance-covariance comparison, and separately work on action/source selection.
