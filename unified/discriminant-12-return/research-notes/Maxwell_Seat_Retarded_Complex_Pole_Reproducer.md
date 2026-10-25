# Frozen Gaussian Maxwell seat: numerical retarded poles

Date 2026-10-25. Parent v14.873. Additive bicone gravity lane.

For frozen rotating-center model in v14.873, write z=aω/c. Closed-form transverse inertia normalized to M(0) is F(z)=1+i sqrt(pi) z exp(-z²) erfc(-iz), with retarded analytic continuation. Ratio k_C/M(0)=c²/(4a²). Thus inverse response in normalized form D(z)=1/4-z² F(z). The denominator is derived under the regulated Gaussian charge/current source and Maxwell field integration, with NO extra mechanical inertia or support constraints.

Numerical complex-root search via mpmath at 25 digits, using multiple complex seeds and |D|<1e-16, found nearest oscillatory conjugate-reflection pair:
z=+0.4108337143730426-0.1700926343728676i,
z=-0.4108337143730426-0.1700926343728676i.
Residuals ~3e-28. More distant roots found at z≈2.481943799524348-1.259676390580487i and 3.116737597781059-2.05613069776429i; these are NOT claimed as complete set of all poles. For e^-iωt, Im z<0 means damped retarded response. Oscillation frequency ≈0.41083 c/a, decay rate ≈0.17009 c/a, quality ratio |Re z|/[2|Im z|]≈1.20767. This damped pole lies outside a parametrically small |z|<<1 expansion and therefore cannot be inferred reliably from constant M(0). It is not a proven stable physical mass-bearing eigenmode, because the prescribed charge sources require supporting stresses/inertia and there are causality/renormalization limitations with treating field-only effective actions as closed physical systems.

Reproducer:
\`\`\`python
import mpmath as mp
mp.mp.dps=30
def F(z):
    return 1+1j*mp.sqrt(mp.pi)*z*mp.exp(-z*z)*mp.erfc(-1j*z)
def D(z): return mp.mpf('0.25')-z*z*F(z)
for seed in [0.4-0.17j,-0.4-0.17j]:
    root=mp.findroot(D,(seed,seed+0.01),tol=mp.mpf('1e-25'))
    print(root,abs(D(root)))
\`\`\`

Finite rotation Ω_L: the conserved current from v14.872 produces a Floquet response matrix with ω+nΩ_L. The frozen root is the Ω_L→0 limit; without specifying Ω_L a/c, R/a, physical source/support dynamics, truncation and convergence, there is no unique finite-rotation pole numerical value. We do not invent one. A next numerical task is explicit Floquet truncation/finite Ω plus convergence and physical supports.

The source remains globally neutral, and results do not derive charge magnitude, gravity, G, Higgs or an independent scalar.
