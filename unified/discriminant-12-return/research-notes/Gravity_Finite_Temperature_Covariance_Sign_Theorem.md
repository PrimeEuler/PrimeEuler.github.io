# Gravity: strict negative finite-temperature scale–eccentricity covariance

2026-10-22. Parents v14.716, v14.718, v14.720. Source: deposited Kepler_Cone_Revised_EFT_Draft_v3_4_Elevated_Hot_Benchmark.tex. Python cross-check: gravity_finite_temp_covariance_sign.py.

## Exact sign theorem [D]

For a finite, positive Maxwellian velocity dispersion \(\sigma\), the EFT's longitudinal half-covariance is \(D_\parallel(v)=\mathcal K G(\chi)/v\), where \(\chi=v/(\sqrt2\sigma)\), \(G(\chi)=\Psi(\chi)/(2\chi^2)\), and \(\Psi(\chi)=\operatorname{erf}\chi-(2\chi/\sqrt\pi)e^{-\chi^2}\).

The exact integral identity
\[
\Psi(\chi)=\frac4{\sqrt\pi}\int_0^\chi t^2 e^{-t^2}\,dt
=\frac{4\chi^3}{\sqrt\pi}\int_0^1 u^2 e^{-\chi^2u^2}\,du
\]
therefore gives
\[
D_\parallel(v)=\frac{\mathcal K}{\sqrt{2\pi}\sigma^3}\int_0^1u^2e^{-v^2u^2/(2\sigma^2)}\,du.
\]
The prefactor follows by substituting \(1/(2\chi^2 v)\Psi(\chi)\); in particular it is positive, and
\[
D_\parallel'(v)=-\frac{\mathcal K v}{\sqrt{2\pi}\sigma^5}\int_0^1u^4e^{-v^2u^2/(2\sigma^2)}\,du<0
\]
for \(v>0,\sigma>0,\mathcal K>0\). [Check the displayed prefactor carefully against the original v3.4 units; only positivity and monotonicity are used in the theorem.]

For a bound ellipse \(0<e<1\), \(v(E)^2=(\mu/T)(1+e\cos E)/(1-e\cos E)\). Applying the Kepler time measure \((1-e\cos E)dE/(2\pi)\) to v14.720's exact joint covariance yields
\[
\overline a_{Tz}=\frac{8T^3(1-e^2)}{\mu^2}
\cdot\frac{2e\mu}{T}\frac1{2\pi}
\int_0^{2\pi}\cos E\,D_\parallel(v(E))\,dE.
\]
For \(c=\cos E>0\), \(v(c)>v(-c)\), and strict monotonicity gives \(D_\parallel(v(c))<D_\parallel(v(-c))\). Pairing the two halves, the integral is strictly negative. Hence
\[
\boxed{\overline a_{T,e^2}<0\qquad(0<e<1,\ \sigma\in(0,\infty),\ \mathcal K>0).}
\]
For circular e=0 the integral vanishes. The constant-longitudinal-diffusion hot limit has equality zero. No claim about endpoint e→1 or strong finite-jump modifications is made.

This is an analytic upgrade to v14.716's numerical negative covariance table, not a fundamentally novel gravitational law: decreasing longitudinal diffusion with speed preferentially weights the lower-speed portion of the orbit.

## Scope

The theorem concerns the local Rosenbluth/Fokker–Planck velocity-diffusion tensor transformed to the *secular* two-coordinate (T,e²) generator. It does not assert negative drift, independence, stationary statistics, or negative correlation for the actual full jump process; a covariance's sign alone cannot determine those properties. The finite-temperature escape boundary and survivor-conditioned two-dimensional law remain open. Xi and G remain unaltered/unpredicted.

**Next:** derive a mathematically controlled finite-temperature **small-Theta expansion** of this cross covariance, then validate against quadrature; independently audit the integral prefactor and distinguish Fokker–Planck from BPS exact-hard-jump covariance. No far-tail touched.
