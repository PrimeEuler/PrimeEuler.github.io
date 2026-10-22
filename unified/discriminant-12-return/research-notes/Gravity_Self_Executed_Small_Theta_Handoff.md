# Gravity self-executed handoff: controlled hot-limit Maxwellian covariance and normalized quadrature

2026-10-22. This lane performs the outstanding v14.721 sandbox-labeled analytical/numerical assignment directly because Suzuki certification has priority on sandbox compute. No request or handoff to sandbox is issued. Source: EFT v3.4 Rosenbluth \(D_\parallel=\mathcal K\Psi(\chi)/(2\chi^2 v)\), \(\chi^2=\Theta(Tv^2/\mu)\); parent v14.720–721.

## Normalization and asymptotics [D]

From
\[
\Psi(\chi)=\frac4{\sqrt\pi}\chi^3\int_0^1t^2e^{-\chi^2t^2}dt,
\quad
D_\parallel(v)=\frac{2\mathcal K}{\sqrt\pi}\sqrt{\frac{\Theta T}{\mu}}\int_0^1t^2e^{-\Theta Tv^2t^2/\mu}dt,
\]
define
\[
D_*=\frac{2\mathcal K}{3\sqrt\pi}\sqrt{\frac{\Theta T}{\mu}}.
\]
For fixed bound Kepler eccentricity \(e<1\), \(\Theta\to0^+\) gives
\[
D_\parallel(v)=D_*\left[1-\frac35\Theta\frac{Tv^2}{\mu}+\frac3{14}\Theta^2\frac{T^2v^4}{\mu^2}+O_e(\Theta^3)\right].
\]
Using Kepler's exact time moments, \(\langle v^2\rangle=\mu/T\), \(\langle v^4\rangle=(\mu/T)^2(4/q-3)\) where \(q=\sqrt{1-e^2}\), gives
\[
\boxed{\bar a_{T,e^2}
=-\frac{96}{5}\frac{D_*T^2}{\mu}q(1-q)\Theta
+O_e(D_*\Theta^2).}
\]
Consequently \(\bar a_{T,e^2}\sim-\mathrm{const}_e\,\mathcal K\,\Theta^{3/2}\), strictly negative for fixed \(0<e<1\). The error bound is asymptotic at fixed e; near e→1 the Kepler velocity maxima invalidate uniformity in e and require a boundary layer.

## Independent normalized integration [N]

Producer \`research-notes/gravity_small_theta_normalized.py\` evaluates the exact **absolute** Maxwellian \(D_\parallel\) integral at \(\mu=T=\mathcal K=1\), with a cancellation-free small-\(\chi\) moment expansion and independently numerical eccentric-anomaly quadrature. The exact divided by the above leading asymptote:

| e | Theta=0.001 | Theta=0.01 | Theta=0.04 |
|---|---:|---:|---:|
| 0.2 | 0.99924 | 0.99244 | 0.97016 |
| 0.6 | 0.99871 | 0.98717 | 0.95001 |
| sqrt(2/3) | 0.99734 | 0.97389 | 0.90165 |
| 0.95 | 0.99117 | 0.91752 | 0.73112 |

Ratios approach 1 as Theta falls, including at the bath's special drift-zero eccentricity. These are **not** measurement predictions: the covariance concerns diffusing orbit elements rather than the rotor's external potential gradient.

## Disposition of outstanding sandbox-labeled gravity requests

Completed locally: the v14.721 requested small-Theta expansion and fully normalized covariance quadrature, including signs, absolute prefactors, and asymptotic limitation. Prior sandbox v14.716 already computed finite-temperature cross correlation and hot joint generator; audit v14.718 independently verified its mathematical core. Thus do not re-dispatch those closed items.

Still **not** closed: a rigorously specified BPS finite-hard-jump killed/bound-preserving *full forward solver*, escape-conditioned finite-temperature law, and the experimental \(\Xi\) bridge. The necessary physical jump operator and boundary prescription cannot be replaced by an invented absorber or inferred from the Fokker–Planck small-Theta series. These are reserved for gravity-lane self-work only, not queued to the compute-constrained Suzuki sandbox.

No G derived or inserted; no far-tail/Suzuki object touched.
