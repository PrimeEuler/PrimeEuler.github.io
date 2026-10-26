# Finite-Larmor harmonic truncation: Gaussian-weighted Bessel convergence test

Date 2026-10-25. Parents v14.872–879. Additive bicone note; no Suzuki/far-tail edits.

The rotating translation factor h(k,t)=exp[-ik_perp R cos(Ωt-φk)] has harmonic coefficients b_n=(-i)^n J_n(k_perp R)e^{-in φk} up to phase convention, hence |b_n|²=J_n(k_perp R)², and Σ_{n∈Z}|b_n|²=1 pointwise.

For isotropic Gaussian momentum weight exp(-a² k²), define dimensionless β=R/a, and probability harmonic weights
W_n(β)=(1/(π^(3/2)))∫_{R³}d³p exp(-p²) J_n(β p_perp)²,
so W_-n=W_n, Σ W_n=1. With x=p² and μ=cos θ:
W_n=(1/Γ(3/2))∫_0∞ dx x^(1/2) exp(-x) (1/2)∫_-1^1 dμ J_n(β sqrt[x(1-μ²)])².
The omitted total weight at harmonic cutoff N is T_N=1-W_0-2Σ_{n=1}^N W_n. This measures convergence of Gaussian-weighted harmonic source phase only, NOT convergence of retarded Maxwell kernel or pole.

Computed with scipy roots_genlaguerre(70,0.5) radial and numpy leggauss(180) angular (Gauss quadrature), values:
beta=0.5: T2=7.30251571e-5, T4=1.418355583e-8, T8≈4.16e-17.
beta=1: T2=0.003419007762, T4=1.040550889e-5, T8=1.315997311e-11.
beta=2: T2=0.07447503234, T4=0.003161856287, T8=9.136604132e-7; T12=5.023070848e-11.

Reproducer (standalone):
\`\`\`python
import numpy as np
from scipy.special import jv, roots_genlaguerre, gamma
from numpy.polynomial.legendre import leggauss
mu, w = leggauss(180)
x, wx = roots_genlaguerre(70, 0.5)
for beta in [0.5,1.,2.]:
    y=beta*np.sqrt(x[:,None])*np.sqrt(1-mu[None,:]**2)
    wn=np.array([np.sum(wx[:,None]*w[None,:]*jv(n,y)**2)/(2*gamma(1.5)) for n in range(14)])
    print(beta,[(N,1-wn[0]-2*sum(wn[1:N+1])) for N in [2,4,8,12]])
\`\`\`
This is not an error bound on a full retarded kernel: frequency-channel denominators can amplify weak high harmonics near poles, and the velocity term in J_n contains Bessel index shifts. Finite Ωa/c and R/a still need to be specified for retarded dynamical pole continuation. No finite-Ω pole is claimed. No Higgs or gravitational source inferred.
