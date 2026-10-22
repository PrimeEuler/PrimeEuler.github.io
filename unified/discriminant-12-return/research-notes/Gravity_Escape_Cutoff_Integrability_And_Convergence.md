# Gravity: cutoff convergence and finite zero-angle hard-escape rate

Date 2026-10-22. Parents v14.725–726. User reserved the Suzuki sandbox; this is entirely executed in the gravity lane. Producer gravity_escape_convergence_16k4.py, rerun locally with numpy/scipy, four seeded 2^16-point scrambled Sobol sequences each configuration. Absolute Rutherford normalization is still **bare**, not BPS matched.

## Convergence diagnosis [N]

With μ=T=σ=1 and nK0 factored out, the replicate-mean rates ± between-replicate standard error are:

| e | theta min .4 | .2 | .1 | .05 |
| --- | --- | --- | --- | --- |
| 0 | 4.9106±.0094 | 4.9548±.0353 | 4.9996±.0815 | 5.1698±.2246 |
| .55 | 4.5369±.0162 | 4.7490±.0362 | 4.7328±.0956 | 4.8940±.1850 |
| .82 | 4.1014±.0076 | 4.3462±.0267 | 4.3728±.0518 | 4.4596±.1160 |

The estimator samples theta via the normalized Rutherford t^−2 importance distribution. At small theta_min, escape is rarer but event weights are larger: at e=.82 the fractions of positive events drop from .2735 at .4 radians to .0060 at .05 radians. Therefore convergence deteriorates even with more samples. Do **not** read noisy nonmonotonic rate estimates as physical negative probability or infer a precise theta→0 extrapolation from these numbers.

## Analytic cutoff integrability at fixed nonradial ellipse [D]

At a physical Kepler phase r, incoming test particle has speed v<vesc=sqrt(2μ/r). An equal-mass elastic scatter through relative angle theta changes test velocity by
\[
|\Delta v|=|v'-v|=g\sin(\theta/2).
\]
If an outcome escapes, triangle inequality demands
\[
g\sin(\theta/2)\ge v_{\rm esc}-|v|.
\]
For any **fixed** ellipse with e<1, the velocity gap has positive uniform lower bound at periapsis,
\[
\delta_e=\min_E\left[\sqrt{2\mu/r(E)}-|v(E)|\right]
=\sqrt{\frac{\mu}{T(1-e)}}\left(\sqrt2-\sqrt{1+e}\right)>0.
\]
(Proof: with x=T/r, difference \(\sqrt{\mu/T}[\sqrt{2x}-\sqrt{2x-1}]\) decreases with x; x largest at periapsis.)

Consequently, an escaping event at angle theta requires
\[
g\ge\delta_e/\sin(\theta/2),\qquad
|w|\ge\delta_e/\sin(\theta/2)-v_{\max}.
\]
For Maxwellian w with fixed dispersion sigma, its probability tail decays at least Gaussian in the required large |w|, i.e. as \(\exp[-c_e/\theta^2]\) for sufficiently small theta. This suppresses the Rutherford angular algebraic divergence (sin^−4(theta/2)) and its relative-speed prefactor g^−3. Near g=0 the positive escape gap also excludes contributions. Therefore the positive bare Maxwellian escape integral is **finite as theta_min→0 for each fixed bound e<1**. This is a mathematical integrability statement, not a numerical zero-cutoff value, uniform bound as e→1, or a BPS-matched hard/soft prescription. The divergence of the *full total elastic Rutherford encounter rate* at grazing angles does not carry over to its hard-*escape* observable at fixed e.

## Consequences and remaining physics

The mathematical finiteness does not authorize adding full hard kernel on top of full BPS FP: hard/soft double-counting remains forbidden. The global finite-temperature survivor density/QSD remains open, because the deposited EFT only supplies fold-local matched corrections rather than the global matched soft and jump kernel. Next gravity-local method: integrate out rare escape angles analytically or use conditional importance sampling with a high-speed Maxwellian tail, then verify absolute bare hazard with a deterministic one-dimensional reduction where possible. Still no source-derived Xi correction or G derivation.
