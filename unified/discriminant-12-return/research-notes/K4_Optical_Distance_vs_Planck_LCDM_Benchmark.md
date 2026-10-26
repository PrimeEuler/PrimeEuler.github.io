# Four-factor Hessian optical curve versus Planck flat-LambdaCDM benchmark

Date 2026-10-26. Parents v14.818, v14.820–821, v14.916–921. Per user preserve every substantive gate. Additive gravity lane only, Suzuki/quarter weld parked.

## Hypotheses and comparison [D/N]
Conditional physically interpreted k=4 metric: spatially flat linearly coasting a(τ)=τ/√3. If standard photons follow this metric with number conservation, dimensionless luminosity distance d_C(z)=H0 D_L/c=(1+z)ln(1+z). Fixed spatially flat ΛCDM Planck 2018 benchmark Ωm=0.315, ΩΛ=0.685, negligible radiation at redshift <=3: d_LCDM(z)=(1+z)∫0^z [Ωm(1+u)^3+ΩΛ]^-1/2 du. Identical H0 cancels in dimensionless ratios. Planck 2018 base ΛCDM source: https://www.aanda.org/articles/aa/abs/2020/09/aa33910-18/aa33910-18.html (H0=67.4±0.5, Ωm=0.315±0.007 under base model). DESI DR2 BAO source: https://journals.aps.org/prd/abstract/10.1103/tr6y-kpc6 (2025) and https://data.desi.lbl.gov/doc/papers/dr2/ (2026 updates). These observationally informed parameters are NOT independent direct distance data fit and do NOT establish model exclusion by themselves.

## Reproducible numeric results [N]
Using scipy.integrate.quad:
 z   d_C       d_LCDM   100(d_C/d_LCDM−1)   Δμ=5log10(d_C/d_LCDM)
0.1 0.1048412 0.1073576 −2.344  −0.0515
0.3 0.3410735 0.3613742 −5.618  −0.1255
0.5 0.6081977 0.6580727 −7.579  −0.1711
1.0 1.3862944 1.5293588 −9.355  −0.2133
2.0 3.2958369 3.5828174 −8.010  −0.1813
3.0 5.5451774 5.8508289 −5.224  −0.1165

Reproducer:
\`\`\`python
import numpy as np
from scipy.integrate import quad
Om=0.315
for z in [0.1,0.3,0.5,1.,2.,3.]:
    dl_c=(1+z)*np.log1p(z)
    dl_l=(1+z)*quad(lambda u: 1/np.sqrt(Om*(1+u)**3+(1-Om)),0,z,epsabs=1e-12)[0]
    print(z,dl_c,dl_l,100*(dl_c/dl_l-1),5*np.log10(dl_c/dl_l))
\`\`\`

## Low-z analytic diagnostic [D]
For flat ΛCDM at present q0=3Ωm/2−1=−0.5275, d_LCDM=z+(1−q0)z²/2+O(z³)=z+0.76375z²+O(z³). Cone metric q0=0 and d_C=z+z²/2+O(z³). Hence the difference begins at order z² and represents unequal acceleration history, not a normalization artifact. Neither H0 common rescaling nor the exact 3+1 Hessian signature forces agreement with real cosmological acceleration.

## Scientific scope
This is a THEORY-vs-THEORY benchmark with empirical inputs, not a fit to Pantheon+ / DES / BAO likelihoods, and therefore no measured exclusion confidence claimed. No physical selection action, independent spin-2 sector (v14.825 obstruction), measured gravitational source, G, or physics identification has been established. To test observation directly use redshift, distance-modulus data plus full covariance, calibrate absolute magnitude/H0 nuisance consistently, compare chi² and held-out residuals against flat ΛCDM; additionally compare BAO D_M/r_d and H(z)r_d separately, using consistent sound-horizon physics. Current gravity branch should not add free dark energy parameters merely to hide failure.

Next: construct direct observational falsification table/likelihood with properly cited released supernova data and covariances, while continuing separate action/physical-source gate.
