"""DRIFT COEFFICIENTS (2026-10-22): sandbox return to the v14.708 HANDOFF.
Task: starting from the deposited EFT v3.4, derive the hot-limit drift
coefficients from the bath/collision operator (no hand-fit fixed point),
test physically motivated perturbations, and check whether any derived
interaction alters the rank-1/rank-2 Xi response (v14.700).
Conventions per v3.4: s = 1 - q, q = L sqrt(-2h)/mu in (0,1];
hot limit = isotropic velocity diffusion, per-component kick variance
rate 2 D0 (<|dv|^2>/dt = 6 D0), friction neglected."""
import sympy as sp

q, T, mu, D0 = sp.symbols('q T mu D0', positive=True)
h = -mu/(2*T)
L2 = mu*T*q**2
v2_avg = mu/T                              # Kepler time average <v^2>
r2_avg = T**2/sp.Integer(2)*(5-3*q**2)     # <r^2> = T^2 (1 + 3 e^2/2), e^2 = 1-q^2

# --- bath generator data on (h, L), hot limit (v3.4 S: covariances) ---
A_h = 3*D0            # energy drift: (1/2)<|dv|^2>/dt
# drifts/covariances as they enter Ls (draft's displayed generator):
#   Ls = q D0 [ -5/(2h) - r^2/L^2 + v^2/(4h^2) ]
# term attribution: A-part = s_h A_h + C_hL s_hL = -5q D0/(2h) with
# A_h = 3 D0 and C_hL = 2 D0 L; B-part = s_L A_L, A_L = D0 r^2/L (Ito
# curvature of L=|rxv|); C-part = (1/2) C_hh s_hh, C_hh = 2 D0 v^2.
Ls = q*D0*(-sp.Rational(5,2)/h - r2_avg/L2 + v2_avg/(4*h**2))
Ls = sp.simplify(Ls)
target = 5*D0*T/(2*mu*q)*(3*q**2-1)
print('generator assembly <Ls> =', Ls)
print('equals (5 D0 T / 2 mu q)(3q^2-1):', sp.simplify(Ls-target) == 0)

# --- attribution of the (15 q^2 - 5) numerator, units of T/(2 mu q^2) ---
print('\ncoefficient attribution (numerator 15 q^2 - 5):')
print('  energy drift + cross-covariance (s_h A_h + C_hL s_hL): +10 q^2')
print('  energy Ito term (1/2 C_hh s_hh, via <v^2>):             +2 q^2')
print('  L-curvature drift (s_L A_L, via <r^2>):            -5 + 3 q^2')
print('  total: 15 q^2 - 5  ->  ratio 3:1, zero at q^2 = 1/3')

# --- Hamilton-Modak independent route ---
eps, C = sp.symbols('eps C', positive=True)
qq = sp.sqrt(1-eps)
A_eps = C*(1-2*eps); D_eps = 2*C*eps*(1-eps)
s_of_eps = 1-qq
A_s = A_eps*sp.diff(s_of_eps, eps) + sp.Rational(1,2)*D_eps*sp.diff(s_of_eps, eps, 2)
A_s_q = sp.simplify(A_s.subs(eps, 1-q**2))
print('\nHamilton-Modak Ito route: A_s =', A_s_q, ' (target C(3q^2-1)/(4q))')
print('  match:', sp.simplify(A_s_q - C*(3*q**2-1)/(4*q)) == 0)
print('  with C = (5T/3mu)*6D0 = 10 D0 T/mu -> identical absolute coefficient:',
      sp.simplify(A_s_q.subs(C, 10*D0*T/mu) - target) == 0)

# --- perturbations: channel weights (1+d) on L-channel, (1+n) on energy channels ---
d, n = sp.symbols('d n')
num = (10*(1+n) + 2*(1+n) + 3*(1+d))*q**2 - 5*(1+d)
for name, subs in [('L-channel x1.5 (d=0.5)', {d: sp.Rational(1,2), n: 0}),
                   ('L-channel x0.5 (d=-0.5)', {d: sp.Rational(-1,2), n: 0}),
                   ('energy channels x1.25 (n=0.25)', {d: 0, n: sp.Rational(1,4)})]:
    nn = num.subs(subs)
    root = sp.solve(nn, q**2)[0]
    print(f'  {name}: zero at q^2 = {sp.nsimplify(root)} = {float(root):.4f} -> e^2 = {float(1-root):.4f}')
print('\nVERDICT pieces:')
print(' * (3q^2-1) is DERIVED, not fit: two independent routes agree in')
print('   absolute coefficient. The 3:1 ratio decomposes as (10+2+3):5')
print('   across the generator channels above.')
print(' * It is NOT protected: channel-weight perturbations move the zero')
print('   continuously (see above); finite temperature moves it along the')
print('   draft F_s(q,Theta)=0 curve to the fold (0.59619, 0.32464)')
print('   [draft numerics, reported]; the planar sector differs outright.')
print(' * Xi test: the bath drift acts on (h,L) statistics of a Kepler')
print('   orbit; Xi (v14.700) is the static rank-1/rank-2 response of a')
print('   rotor to Phi\', Phi\'\'. Disjoint objects; no derived bath term')
print('   enters beta1 or beta2. Bath granularity of a source would add')
print('   noise to a Xi measurement (v14.702 budget), not a correction')
print('   to the mean response ratio. NEGATIVE for a Xi alteration.')
