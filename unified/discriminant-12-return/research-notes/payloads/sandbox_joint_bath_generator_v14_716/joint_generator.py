"""JOINT (T, eps) BATH GENERATOR (2026-10-22): sandbox return to the
v14.713 HANDOFF (gravity lane), also answering the sandbox handoff in
gravity v14.710.

Task (v14.713): derive the full orbit-averaged two-dimensional generator
for (T, eps=e^2) from the exact high-speed joint velocity SDE, including
the mixed covariance d[T,eps]_t/dt; carry the finite-temperature
Fokker-Planck (Rosenbluth/Maxwellian, EFT v3.4) corrections; separate the
BPS bound-preserving (survival-conditioned) and killed (cemetery)
channels; seek a quasi-stationary eccentricity law, or report if
nonexistent / conditioning-dependent.

Conventions (EFT v3.4, half-covariance): dv_i dv_j = 2 D_ij dt with
D = D_par vhat vhat^T + D_perp (I - vhat vhat^T); generator
L f = b.grad f + D : Hess f.  Hot/high-speed limit: D = D0 I, friction
neglected.  Finite temperature (v3.4 corrected Maxwellian, equal mass):
  A(v) = 2 K Psi(chi)/v^2      (friction coefficient, drift -A v)
  D_par(v) = K G(chi)/v
  D_perp(v)  = K/(2v) [erf(chi) - G(chi)]
  chi = v/(sqrt(2) sigma),  Psi = erf(chi) - 2 chi/sqrt(pi) e^{-chi^2},
  G(chi) = Psi/(2 chi^2),   Theta = mu/(2 T sigma^2),  chi^2 = Theta * z,
  z = T v^2 / mu (draft's speed variable).
Orbital elements: h = v^2/2 - mu/r < 0, T = -mu/(2h), u = |r x v|^2,
eps = 1 + 2 h u / mu^2, u = mu T (1 - eps).
Source data taken as given (verified in v14.705/v14.710/R333):
  hot: Lh drift 3 D0, C_hh = 2 D0 v^2, C_hL = 2 D0 L;
  eps drift A_eps = C (1 - 2 eps), C_eps eps = 2 C eps (1-eps),
  C = 10 D0 T / mu;  <LT> = 14 D0 T^2/mu, <C_TT> = 8 D0 T^3/mu (v14.713).
"""
import numpy as np
import sympy as sp
from scipy.special import erf

rng = np.random.default_rng(20261022)

# =====================================================================
# PART 1 (symbolic): instantaneous cross-covariance rate, hot + finite-T
# d[T,eps]/dt = 2 (grad_v T)^T D (grad_v eps),
# grad_v T = T_h v,  T_h = 2 T^2/mu,
# grad_v eps = a v + b grad_v u, a = 2u/mu^2, b = 2h/mu^2,
# v . grad_v u = 2u (u = r^2 v^2 - (r.v)^2), and D v = D_par v
# (v is an eigenvector of the Rosenbluth tensor), so
#   v^T D grad_v eps = D_par (a v^2 + 2 b u) = D_par (2u/mu^2)(v^2 + 2h)
#   =>  rate = (4 T_h u D_par / mu^2) (v^2 + 2h).      (*)
# Friction is a drift: it contributes NOTHING to any covariance rate.
# =====================================================================
T, mu, D0, u, h = sp.symbols('T mu D0 u h', positive=True)
Th = 2*T**2/mu
rate_hot = 4*Th*u*D0/mu**2  # times (v^2 + 2h)
eps = sp.symbols('eps')
rate_hot_elem = sp.simplify(rate_hot.subs(u, mu*T*(1-eps)))
print('PART 1: instantaneous cross-cov rate (hot) =')
print('   ', rate_hot_elem, '* (v^2 + 2h)')
# orbit average: <v^2> = mu/T (Kepler), 2h = -mu/T exactly on the orbit,
# u and T_h are orbit constants  =>  <v^2 + 2h> = 0  =>  averaged rate 0.
print('   orbit average: <v^2+2h> = mu/T - mu/T = 0  =>  <d[T,eps]/dt> = 0 (hot)')

# =====================================================================
# PART 2 (numeric): pointwise Monte Carlo check of ALL THREE covariance
# rates at frozen r, hot and finite-T, from the velocity SDE itself.
# Pointwise rate formulas (D_par, D_perp evaluated at the frozen v):
#   C_TT   = 2 D_par v^2 T_h^2
#   C_Teps = (4 T_h u D_par / mu^2)(v^2 + 2h)                      (*)
#   C_ee   = 2[ a^2 D_par v^2 + 4 a b D_par u
#               + 4 b^2 u (D_par u + D_perp (r.v)^2) / v^2 ]
# (last line from (grad u)^T D (grad u)
#   = 4u [ D_par u/v^2 + D_perp (r^2 - u/v^2) ],  r^2 - u/v^2 = (r.v)^2/v^2)
# =====================================================================
def Gfun(chi):
    chi = np.asarray(chi, dtype=float)
    out = np.empty_like(chi)
    small = chi < 1e-3
    out[small] = 2*chi[small]/(3*np.sqrt(np.pi))*(1 - 3*chi[small]**2/5)
    c = chi[~small]
    Psi = erf(c) - 2*c/np.sqrt(np.pi)*np.exp(-c**2)
    out[~small] = Psi/(2*c**2)
    return out

def rosenbluth(vnorm, K, sigma):
    chi = vnorm/(np.sqrt(2)*sigma)
    Dpar = K*Gfun(np.array([chi]))[0]/vnorm
    Dperp = K/(2*vnorm)*(erf(chi) - Gfun(np.array([chi]))[0])
    return Dpar, Dperp

def mc_cov(rvec, vvec, mu_, K, sigma, hot, dt=2e-4, n=400_000):
    vnorm = np.linalg.norm(vvec)
    if hot:
        Dpar = Dperp = 1.0  # D0 = 1
    else:
        Dpar, Dperp = rosenbluth(vnorm, K, sigma)
    vhat = vvec/vnorm
    Dmat = Dpar*np.outer(vhat, vhat) + Dperp*(np.eye(3) - np.outer(vhat, vhat))
    Lchol = np.linalg.cholesky(2*Dmat*dt)
    dv = (Lchol @ rng.standard_normal((3, n))).T
    vn = vvec + dv
    rnorm = np.linalg.norm(rvec)
    hn = 0.5*np.sum(vn**2, axis=1) - mu_/rnorm
    Tn = -mu_/(2*hn)
    Lv = np.cross(np.broadcast_to(rvec, vn.shape), vn)
    un = np.sum(Lv**2, axis=1)
    en = 1 + 2*hn*un/mu_**2
    h0 = 0.5*vnorm**2 - mu_/rnorm
    T0 = -mu_/(2*h0)
    u0 = np.sum(np.cross(rvec, vvec)**2)
    e0 = 1 + 2*h0*u0/mu_**2
    dT = Tn - T0; de = en - e0
    return (np.mean(dT*de)/dt, np.mean(dT*dT)/dt, np.mean(de*de)/dt,
            T0, u0, h0, e0, vnorm**2)

def analytic_rates(rvec, vvec, mu_, K, sigma, hot):
    vnorm = np.linalg.norm(vvec); v2 = vnorm**2
    rnorm = np.linalg.norm(rvec)
    h0 = 0.5*v2 - mu_/rnorm
    T0 = -mu_/(2*h0); Th_ = 2*T0**2/mu_
    u0 = np.sum(np.cross(rvec, vvec)**2)
    rdv = float(rvec @ vvec)
    if hot:
        Dpar = Dperp = 1.0
    else:
        Dpar, Dperp = rosenbluth(vnorm, K, sigma)
    a = 2*u0/mu_**2; b = 2*h0/mu_**2
    C_TT = 2*Dpar*v2*Th_**2
    C_Te = 4*Th_*u0*Dpar/mu_**2*(v2 + 2*h0)
    C_ee = 2*(a*a*Dpar*v2 + 4*a*b*Dpar*u0
              + 4*b*b*u0*(Dpar*u0 + Dperp*rdv**2)/v2)
    return C_Te, C_TT, C_ee

print('\nPART 2: pointwise MC covariance rates vs analytic (frozen r):')
mu_ = 1.0
states = [ (np.array([1.3, 0.2, 0.0]), np.array([0.1, 0.72, 0.15])),
           (np.array([0.7, -0.5, 0.3]), np.array([0.55, 0.45, -0.2])),
           (np.array([2.0, 0.0, 0.4]), np.array([-0.2, 0.42, 0.1])) ]
for i, (rv, vv) in enumerate(states):
    for hot, K, sigma in [(True, None, None), (False, 1.0, 0.9)]:
        mc = mc_cov(rv, vv, mu_, K, sigma, hot)
        an = analytic_rates(rv, vv, mu_, K, sigma, hot)
        tag = 'hot ' if hot else 'finT'
        print(f'  state{i} {tag}: C_Teps MC {mc[0]:+.4f} vs analytic {an[0]:+.4f} | '
              f'C_TT MC {mc[1]:.4f} vs {an[1]:.4f} | C_ee MC {mc[2]:.4f} vs {an[2]:.4f}')

# =====================================================================
# PART 3: orbit averages by eccentric-anomaly quadrature.
# r = T(1 - e cosE), v^2 = (mu/T)(1+e cosE)/(1-e cosE),
# (r.v)^2 = mu T e^2 sin^2 E, Kepler weight (1 - e cosE) dE / 2pi.
# =====================================================================
def orbit_avg(fun, e, nE=200_001):
    E = np.linspace(0, 2*np.pi, nE)
    w = (1 - e*np.cos(E))/(2*np.pi)
    return np.trapz(fun(E)*w, E)

def rates_at(E, e, T_, mu_, K, sigma, hot):
    r = T_*(1 - e*np.cos(E))
    v2 = (mu_/T_)*(1 + e*np.cos(E))/(1 - e*np.cos(E))
    v = np.sqrt(v2)
    rdv2 = mu_*T_*e*e*np.sin(E)**2
    u_ = mu_*T_*(1 - e*e)
    h_ = -mu_/(2*T_)
    Th_ = 2*T_**2/mu_
    if hot:
        Dpar = np.full_like(E, 1.0); Dperp = np.full_like(E, 1.0)
    else:
        chi = v/(np.sqrt(2)*sigma)
        Dpar = K*Gfun(chi)/v
        Dperp = K/(2*v)*(erf(chi) - Gfun(chi))
    a = 2*u_/mu_**2; b = 2*h_/mu_**2
    C_TT = 2*Dpar*v2*Th_**2
    C_Te = 4*Th_*u_*Dpar/mu_**2*(v2 + 2*h_)
    C_ee = 2*(a*a*Dpar*v2 + 4*a*b*Dpar*u_
              + 4*b*b*u_*(Dpar*u_ + Dperp*rdv2)/v2)
    return C_TT, C_Te, C_ee

print('\nPART 3: hot orbit averages (mu=T=D0=1) vs closed forms:')
for e in [0.0, 0.3, np.sqrt(2/3), 0.95]:
    eps_ = e*e
    Cval = 10.0
    avg = [orbit_avg(lambda E, k=k: rates_at(E, e, 1.0, 1.0, None, None, True)[k],
                     e) for k in range(3)]
    print(f'  e={e:.4f}: <C_TT> {avg[0]:.6f} (exact 8) | <C_Teps> {avg[1]:+.2e} '
          f'(exact 0) | <C_ee> {avg[2]:.6f} (exact 2C eps(1-eps) = '
          f'{2*Cval*eps_*(1-eps_):.6f})')

print('\nPART 3b: finite-T cross-covariance identity check:')
print('  <D_par (v^2+2h)>  vs  (2 e mu/T) * mean_E[D_par cosE]  (uniform E mean);')
print('  Kepler identity: (1/r - 1/T)(1 - e cosE) = e cosE / T pointwise in E')
for (e, Theta) in [(0.5, 0.1), (np.sqrt(2/3), 0.32464127), (0.3, 1.0)]:
    T_ = mu_ = 1.0; K = 1.0
    sigma = np.sqrt(mu_/(2*T_*Theta))
    lhs = orbit_avg(lambda E: rates_at(E, e, T_, mu_, K, sigma, False)[1], e) \
        / (4*(2*T_**2/mu_)*(mu_*T_*(1-e*e))/mu_**2)  # divide out prefactor -> <Dpar w>
    E = np.linspace(0, 2*np.pi, 200_001)
    v = np.sqrt((mu_/T_)*(1 + e*np.cos(E))/(1 - e*np.cos(E)))
    Dpar = K*Gfun(v/(np.sqrt(2)*sigma))/v
    rhs = (2*e*mu_/T_)*np.trapz(Dpar*np.cos(E), E)/(2*np.pi)
    print(f'  e={e:.4f} Theta={Theta}: lhs {lhs:+.6e}  rhs {rhs:+.6e}  '
          f'ratio {lhs/rhs if rhs != 0 else float("nan"):.6f}')

print('\nPART 3c: finite-T correlation coefficient rho_Teps = '
      '<C_Teps>/sqrt(<C_TT><C_ee>) (K cancels):')
print('   e \\ Theta |  0.01     0.1      0.32464   1.0      3.0      10.0')
for e in [0.2, 0.5, np.sqrt(2/3), 0.95]:
    row = []
    for Theta in [0.01, 0.1, 0.32464127, 1.0, 3.0, 10.0]:
        sigma = np.sqrt(1.0/(2*Theta))
        av = [orbit_avg(lambda E, k=k: rates_at(E, e, 1.0, 1.0, 1.0, sigma, False)[k],
                        e, nE=40_001) for k in range(3)]
        row.append(av[1]/np.sqrt(av[0]*av[2]))
    print(f'   e={e:.4f}  | ' + '  '.join(f'{x:+.4f}' for x in row))

# =====================================================================
# PART 4: the orbit-averaged hot joint process and quasi-stationarity.
# Averaged generator factorises:
#   Lbar = Lbar_T + C(T) J_eps,
#   Lbar_T f = (14 D0 T^2/mu) f' + (4 D0 T^3/mu) f''
#     (drift <LT>, half of <C_TT> as the f'' coefficient),
#   J_eps g = (1-2eps) g' + eps(1-eps) g'',  C(T) = 10 D0 T/mu.
# In y = -h the averaged energy process is
#   dy = -3 D0 dt + sqrt(4 D0 y) dW   (BESQ dimension delta = -3,
#   time scaled by D0): hits y=0 (escape, h=0) a.s. in finite time,
#   E[t_esc] = y0/(3 D0).
# eps is a Jacobi diffusion run on the stochastic clock
#   tau(t) = int_0^t C(T_s) ds = int 5 D0 / y_s ds,
# with a Brownian motion INDEPENDENT of the energy process (Part 1/3:
# averaged cross-covariance is exactly 0).  Along paths that survive
# (y bounded away from 0 for long), tau grows; if tau -> inf the eps law
# relaxes to the Jacobi invariant law (uniform in eps) regardless of
# the scale process.  Simulation tests exactly this, and whether the
# SCALE law among survivors is tight (joint QSD) or escapes.
# Channels: KILLED = cemetery at escape (unconditional moments decay
# with survival probability); BOUND-PRESERVING (BPS, survival-
# conditioned) = statistics of survivors only.
# =====================================================================
print('\nPART 4: averaged joint SDE simulation (mu=D0=1, T0=1, y0=0.5):')
N = 30_000
dt = 2.5e-4
t_max = 1.6
steps = int(t_max/dt)
rng2 = np.random.default_rng(710)
y = np.full(N, 0.5)
eps_s = np.full(N, 2.0/3.0)
tau = np.zeros(N)
alive = np.ones(N, dtype=bool)
t_esc = np.full(N, np.nan)
check_times = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
check_steps = {int(round(tc/dt)): tc for tc in check_times}
W_exact = (8*np.log(2) - 4)/3
print(f'  {"t":>5} {"surv%":>7} {"E[eps|surv]":>11} {"sd[eps|surv]":>12} '
      f'{"E[W|surv]":>9} {"medT|surv":>9} {"medTau|surv":>11} {"E[eps;kill]":>11}')
for k in range(1, steps + 1):
    idx = np.where(alive)[0]
    if len(idx) == 0:
        break
    yy = y[idx]
    Cval = 5.0/yy
    tau[idx] += Cval*dt
    y[idx] = yy - 3.0*dt + np.sqrt(4.0*np.maximum(yy, 0.0)*dt)*rng2.standard_normal(len(idx))
    ee = eps_s[idx]
    dW = rng2.standard_normal(len(idx))
    ee = ee + Cval*(1 - 2*ee)*dt + np.sqrt(2*Cval*np.clip(ee, 0, 1)*(1 - np.clip(ee, 0, 1))*dt)*dW
    eps_s[idx] = np.clip(ee, 0.0, 1.0)
    dead = idx[y[idx] <= 0]
    if len(dead):
        alive[dead] = False
        t_esc[dead] = k*dt
    if k in check_steps:
        tc = check_steps[k]
        sv = np.where(alive)[0]
        ee = eps_s[sv]
        W = 4*np.sqrt(ee)/(3*(1 + np.sqrt(ee)))  # W(eps) = 4e/(3(1+e)), e=sqrt(eps)
        medT = np.median(0.5/np.maximum(y[sv], 1e-12))
        yq = np.percentile(y[sv], [25, 50, 75])
        print(f'  {tc:5.2f} {100*len(sv)/N:7.2f} {np.mean(ee):11.4f} '
              f'{np.std(ee):12.4f} {np.mean(W):9.4f} {medT:9.2f} '
              f'{np.median(tau[sv]):11.2f} {np.sum(ee)/N:11.4f}'
              .replace('nan', '  -  '))
print(f'  uniform law targets: E[eps]=0.5, sd=sqrt(1/12)={np.sqrt(1/12):.4f}, '
      f'E_pi[W]=(8 ln2 - 4)/3={W_exact:.4f}')
esc = t_esc[~np.isnan(t_esc)]
print(f'  escape: {100*len(esc)/N:.1f}% escaped by t={t_max}; '
      f'mean escape time (escaped only) {np.mean(esc):.4f}; '
      f'BESQ prediction y0/(3 D0) = {0.5/3:.4f} (censored at t_max)')
sv = np.where(alive)[0]
if len(sv):
    print(f'  survivors at t={t_max}: y quartiles '
          f'{np.percentile(y[sv], [25, 50, 75]).round(2)} (start 0.5): '
          f'survivor scale runs to y -> inf (T -> 0), it does not settle')

# Doob h-transform of the averaged scale process (symbolic): for the
# BESQ generator L f = 2y f'' + delta f' (time in units of 1/D0),
# h(y) = y^alpha is harmonic iff alpha [2(alpha-1) + delta] = 0, i.e.
# alpha = 1 - delta/2.  The h-transformed generator has drift
# delta + 4 alpha = 4 - delta: BESQ(delta) conditioned to survive
# forever is BESQ(4 - delta).  Here delta = -3, so the conditioned
# scale process is BESQ(7): y ~ 7 t, T -> 0, and the eps clock
# tau = int 5/y dt ~ (5/7) ln t -> inf, logarithmically.
yy, dl = sp.symbols('y delta', positive=True)
alpha = 1 - dl/2
harm = sp.simplify(2*yy*sp.diff(yy**alpha, yy, 2) + dl*sp.diff(yy**alpha, yy))
print(f'\nPART 4b: h-transform check: L[y^alpha] / y^(alpha-1) with '
      f'alpha=1-delta/2 -> {sp.simplify(harm/yy**(alpha-1))} (0 = harmonic); '
      f'conditioned drift delta+4alpha = {sp.simplify(dl + 4*alpha)} = 4-delta; '
      f'for delta=-3: BESQ(7)')

print('\nVERDICT pieces:')
print(' * Hot averaged cross-covariance is EXACTLY ZERO: the shared')
print('   velocity noise cancels in <v^2+2h>=0 (virial). The joint')
print('   averaged generator factorises, Lbar_T + C(T) J_eps, with no')
print('   mixed derivative. v14.713 timescale obstruction stands')
print('   (T is not slow), but the coupling is one-way: T drives the')
print('   eps clock, eps does not drive T.')
print(' * Finite temperature breaks the cancellation: D_par(v)')
print('   decreases with v, weighting pericentre differently, giving a')
print('   NEGATIVE cross-covariance / correlation (Part 3c), vanishing')
print('   as Theta -> 0 and at e=0 and eps=1. Friction contributes')
print('   nothing to any covariance (drift only).')
print(' * No joint stationary law (hot): averaged energy is BESQ(-3),')
print('   escape (h=0) is almost-sure in finite mean time y0/(3 D0).')
print(' * Quasi-stationary SHAPE law EXISTS as a marginal in the')
print('   survival-conditioned (BPS bound-preserving) channel: eps is')
print('   a Jacobi diffusion on the clock tau(t)=int C(T) dt with an')
print('   independent Brownian motion; the conditioned scale process')
print('   is BESQ(4-delta)=BESQ(7) (Part 4b h-transform), so survivor')
print('   y ~ 7 D0 t, tau ~ (5/7) ln t -> inf, and the eps law relaxes')
print('   to the uniform Jacobi law (E[eps]=1/2, sd=1/sqrt(12),')
print('   E[W]=(8 ln2-4)/3) -- confirmed by Part 4 simulation.')
print(' * But NO joint quasi-stationary law: under conditioning the')
print('   scale marginal is not tight (y runs to inf, T -> 0; Part 4')
print('   survivor quartiles), and unconditionally the scale is')
print('   killed at y=0. The eps QSD is a marginal statement only and')
print('   is conditioning-dependent in exactly this sense.') 
print(' * Killed (cemetery) channel: unconditional moments decay with')
print('   the survival probability; they are NOT the survivor moments.')
print('   This is exactly the v3.4 BPS bound-vs-kill distinction; the')
print('   draft fold endpoints differ at O(1/L_C) between the channels')
print('   [draft-reported numerics, not recomputed here].')
print(' * Xi link: none. The cross-covariance is a property of the')
print('   stochastic (T,eps) process; Xi is a static field-response')
print('   ratio. Concurs with v14.708/v14.710 negatives.')
