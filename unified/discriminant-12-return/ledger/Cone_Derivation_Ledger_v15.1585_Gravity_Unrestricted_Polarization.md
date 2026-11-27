# Gravity v15.1585 — Unrestricted polarization, numerical dual and nonlinear feasibility

2026-11-27 Eastern. Parent v15.1584 (50f5b112d6eacda705e85bb52ea110a2c7b65126). Additive source a052e82be14f8d8c9f99a3ea089bdd0ef9134df7. Independent Audit pending. Continuation labels 1529–1533.

## Unrestricted finite-cell problem
Same vertex, kernels and normalized leading deficit as v15.1584. Q=-iK Hermitian, H PSD. Maximize E†QE subject to E†HE<=b and |E_j|<=1 independently. Exact cell Volterra moments at 8N midpoint nodes. SLSQP analytic derivatives in real and imaginary coordinates, scale 1000, starts f=2,5,9,15, ftol 1e-11, maxiter 500. No angle constraint. Executed local equivalent source with OPENBLAS_NUM_THREADS=1; committed source consolidates duplicate runs. Angles are half unwrapped complex phase difference between first and last cell centers, not optical polar rotation.

N32 sweep (budget, P, sampled axis rotation deg, min amplitude):
.001 .0019556408716620904 88.82670654520294 .2777057598580983
.002 .003558993183373141 88.89590763646277 .4486203073573194
.003 .004982472029490698 88.90343419765573 .6245136331118807
.004 .00616910377641596 88.4631435354294 1
.005 .006282470545418375 87.72061211559118 1
All best success flags true. Last budget slack H=.004316869137286047. At b=.003 N64 P=.004982722751255743 angle=89.45670477554391 min amplitude=.6257550653086117; N128 P=.004982784374133959 angle=89.72968381591602 min amplitude=.6252265095814571. All deficits equal budget within floating-point tolerance, not exact feasibility. Angular gap roughly halves, consistent with sampling error, not a continuum proof. At N128 t=.496, relative axis 44.5363 degrees, amplitude .62546; near endpoints amplitude 1.

## Dual test
KKT: QE=lambda HE+diag(mu)E; lambda,mu>=0, lambda(Hvalue-b)=0, mu_j(|E_j|²-1)=0. S=lambda H+diag(mu)-Q. If S PSD, P<=lambda*b+sum(mu). Equality with feasible primal proves finite-dimensional global maximum. Fit lambda by real least squares on cells with amplitude<1-1e-5, clip mu nonnegative and zero on free cells. Shift diagonal by max(0,-sampled min eigenvalue) for numerical upper estimate. No interval eigenvalue or quadrature certification. N32/64/128 at b=.003:
lambda 1.342731153880954 / 1.3430349544729734 / 1.3431434655612629;
min eig 3.2378e-15 / 2.4352e-14 / -2.9051e-14;
upper .004982472029582563 / .004982722752654133 / .004982784374842798;
gap 9.1865e-14 / 1.3984e-12 / 7.0884e-13;
max stationarity residual 7.6024e-11 / 4.7193e-11 / 4.5238e-11.
Strong numerical finite-grid evidence only; no rigorous global or continuum certificate.

## Nonlinear replay
N128 full Jacobi cellwise solve_ivp rtol 1e-11 atol 1e-13. eta=.2,.1,.05 unscaled normalized deficits .0030000840740757036,.003000021602472813,.0030000059865198376. Brent solve common amplitude scale on [.99,1], subtract 1e-8 safety margin. Scales .9999859783386852,.9999963896345889,.9999989922662018. Corrected normalized (polar angle, area deficit):
.2 (.00498260245434512,.002999999940003772)
.1 (.004982738524481655,.002999999939978792)
.05 (.0049827725290756564,.002999999939889974).
Numerical feasibility at sampled strengths; not interval-certified or full nonlinear optimum. Relative improvement ~9.06% versus earlier sampled steady comparator, not matched-grid certified comparator.

## Next
Derive continuum KKT integral equations and endpoint limits, test whether antipodal endpoint selection is enforced or accidental, refine budget sweep and bound quadrature/eigenvalue errors; seek a counterexample to quarter-turn universality. Spin-2 sign reversal identity is standard; no new Cone-specific gravitational law, G derivation or quarter-grid weld claimed. Other open lanes unchanged.
