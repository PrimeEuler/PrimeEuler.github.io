# Cone Derivation Ledger v15.007 — Metric ADM momentum and quadratic global zero-mode balance

Date 2026-10-27. Parent v15.003, v15.005, audit v15.006. Research note research-notes/K4_Gravitational_Canonical_Momentum_Quadratic_Balance.md commit c37da30c5d2fad0cd4b16d12bf0208d40c28b263. Live prewrite HEAD c37da30c5d2fad0cd4b16d12bf0208d40c28b263. Additive gravity only; protected other lanes untouched, Suzuki quarter weld PARKED.

[D] ADM metric h=a²(δ+ε), lapse N=1+α, contrav shift N^i=β^i, extrinsic Kij=(dot hij−Di Nj−Dj Ni)/(2N). Canonical Πij=√h(K^ij−h^ijK)/(2κ). Linear result Π1^ij=(a/2κ)[2Hεij+dotεij/2−(∂iβj+∂jβi)/2 +δij(2Hα−H trε−dot(trε)/2+∂kβk)]. Retains shift covariant derivative terms. Uniform pure conformal perturbation check matches exact homogeneous Π.

[D] Exact ADM momentum constraint is H_i=−2∂k(hijΠjk)+Πjk∂i hjk+pI∂iφI=0. Upon spatial integration with vanishing divergence boundary flux, homogeneous h0, Π0 and p0=0, the quadratic order integrated condition becomes ∫[a²Π1^jk ∂iεjk+pI1∂iπI+p_i2]=0. pI1=(2C/3)a³(dotπI−βI), p_i2 full second-order canonical matter momentum from v15.005. Nonlinear scalar matter and gravitational pieces jointly determine zero-mode solvability. Does not establish their automatic cancellation, pointwise local constraint or small nonzero-K uniform inverse bounds.

[O] Full Fourier K≠0 second-order gravitational momentum source includes divergence involving Π2 and h2 and must be computed in gauge; near-zero momentum estimates and nonlinear future stability remain open. Torus winding or boundary flux caveat for φI=zi.

Flags: gravitational_Pi_first_order=DERIVED; full_quadratic_global_balance=EXACT_CONDITIONAL_BOUNDARY; shifted_covariant_derivatives=RETAINED; all_low_K_inverse_bounds=OPEN; full_nonlinear_stability=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: ADM-metric-momentum-quadratic-global-balance
parent: v15.007
status: open
action: Independently verify Π1 including shifts and conformal check, integrated quadratic constraint and required p_i2, and flag dependence on boundary/zero mode.
deliverable: scoped verdict.

NEXT: derive local second-order momentum source symbol including divergence and solve low-K constraints in regular gauge. 
