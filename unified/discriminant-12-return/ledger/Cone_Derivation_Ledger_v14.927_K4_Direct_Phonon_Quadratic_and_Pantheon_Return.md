# Cone Derivation Ledger v14.927 — Direct elastic phonon quadratic action and Pantheon full-covariance return

Date 2026-10-26. Parents v14.923–926, separate Sandbox v14.926_Pantheon_Full_Covariance_Return, k4 metric v14.818–825. Research note research-notes/K4_Elastic_Direct_Phonon_Quadratic_Action_and_Fullcov_Return.md, commit 110467a671f536153ad5d533710c81506f0f80e0. Prewrite HEAD 110467a671f536153ad5d533710c81506f0f80e0. Owner per-gate preservation active; Suzuki quarter parked; independent Suzuki/far-tail untouched.

[D] For S_m=−∫√−g C b^(2/3)(1+ηJ), B=FᵀF−vvᵀ in a local orthonormal frame, F_i^I=δ_i^I+∂iπ^I, v=dot π, b=sqrt(det B), J=tr(B²)/(tr B)²−1/3. At a locally frozen isotropic background rho=C>0, both direct plane-wave perturbation sectors have positive time-kinetic coefficient rho/3. For transverse π_y=f(t,x), det F=1, J=2(f')²/9+O(3), L2,T=(rho/3)[(dot f)²−(2η/3)(f')²]. For longitudinal π_x=f(t,x), det F=1+f', J=8(f')²/27+O(3), L2,L=(rho/3)[(dot f)²−(−1/3+8η/9)(f')²] after discarding the linear boundary derivative. Thus cT²=2η/3, cL²=−1/3+8η/9 and for 3/8<η≤3/2 both sectors have positive kinetic and positive subluminal principal gradients. This directly corroborates v14.926, not just reliance on generic isotropic elasticity formula.

[CAUTION / NOTE CLEANUP] The companion research note includes an explicitly caveated unsimplified attempted generic spatial L2 expression; DO NOT use that intermediate line as a result. Only the fully calculated transverse and longitudinal quadratic expressions above are promoted. Full cosmological metric+solid scalar/vector/tensor constraint elimination and Hamiltonian positivity NOT performed. Potential curvature/time-dependent instabilities untested. Physical graviton propagation remains a conditional consequence of treating g independently via Einstein-Hilbert, not selected uniquely by AMGM.

[V, separate observational handoff landed] Sandbox parallel ledger v14.926_Pantheon_Full_Covariance_Return with payloads/pantheon_fullcov_v14_926/ documents 1580-row direct-data likelihood comparison, raw released covariance A: delta chi2 k4−flatΛCDM=+103.1252; diagonal-restored covariance B: +61.3380, both favor flatΛCDM with one additive magnitude normalization. Data diagonal mismatch is explicit and independent audit outstanding. Do NOT claim sigma or definitive physical exclusion; background coasting shape is observationally disfavored on both covariance constructions. See Sandbox ledger for hashes and numerical details.

[O] Full metric–matter cosmological perturbations; independently sourced eta and κ; assess physical viability of K4 background given SN distance result. No G from cone. Important avoid allowing a stable high-k matter action to be confused with empirical agreement of global FLRW geometry.

Flags: local_phonon_quadratic_kinetic=POSITIVE; high_k_gradient_window=(3_over_8,3_over_2]; full_SVT_cosmological_stability=OPEN; eta_selected=FALSE; physical_metric_selected=FALSE; k4_fullcov_SN_vs_LCDM=DISFAVORED; independent_covariance_audit=OPEN; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-phonon-quadratic-plus-pantheon-return
parent: v14.927
status: open
action: Verify second-variation plane-wave transverse and longitudinal coefficients/positive kinetic signs and strict eta bounds; independently inspect Sandbox v14.926 full-covariance model-comparison provenance, duplicate-version filenames and covariance construction distinction.
deliverable: scoped audit verdict.
NEXT: Derive lapse/shift-reduced full SVT quadratic system; specifically investigate whether AM-GM optical cone might be a local geometry rather than globally coasting FLRW, with independent spacetime identification and testable differences.
