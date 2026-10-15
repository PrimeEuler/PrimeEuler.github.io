#!/usr/bin/env python3
"""Thread 4 check script: chi_12 archimedean screw term vs parabolic/KS dipole.

All computations at mpmath dps=50 unless stated. Sections:
  1. Constants: zeta(2,1/4) = pi^2 + 8G ?  psi(1/4) = -gamma - pi/2 - 3 ln 2 ?
  2. A_12 two ways (v13.258 direct vs -g_Gamma,zeta + (t/2) log 12 mirror).
  3. Lerch tail series: e^{-t/2} Phi(e^{-2t},2,1/4) = sum_m e^{-(2m+1/2)t}/(m+1/4)^2
     and the ramp form T(t) = (1/4) sum_m (1 - e^{-2(m+1/4)t})/(m+1/4)^2.
  4. Density closed form: -T''(t) =?= e^{-t/2}/(1 - e^{-2t}) = sum_m e^{-(4m+1)t/2}.
  5. Small-t: (T(t) + (1/2) t log t)/t -> kappa = 1/2 + pi/4 + log 2 ?
             (A_12(t) + (1/2) t log t)/t -> c = (1 - gamma + log(6/pi))/2 ?
  6. Tail at the (2,1) station t = log 2; nsimplify probe for a closed form.
  7. KS-side comparison data: sech-psi series in s (exact rationals),
     Gaussian moments (2j-1)!!/3^j at a=3/2, tail coefficients 16/(4m+1)^2.
"""
import sys, json, math
sys.path.insert(0, '/home/hatch/workspace/d12/explorations/screw-stations')
import mpmath as mp
from fractions import Fraction
from suzuki_riemann_screw_calibration import archimedean_term  # g_Gamma(t) of zeta

mp.mp.dps = 50
A = mp.mpf('0.25')
out = {}

# ---------- 1. constants ----------
z214 = mp.zeta(2, A)
out['zeta(2,1/4)'] = mp.nstr(z214, 30)
out['pi^2+8G'] = mp.nstr(mp.pi**2 + 8*mp.catalan, 30)
out['zeta_const_absdiff'] = mp.nstr(abs(z214 - (mp.pi**2 + 8*mp.catalan)), 5)
psi14 = mp.digamma(A)
out['psi(1/4)'] = mp.nstr(psi14, 30)
out['-gamma-pi/2-3ln2'] = mp.nstr(-mp.euler - mp.pi/2 - 3*mp.log(2), 30)
out['psi_const_absdiff'] = mp.nstr(abs(psi14 - (-mp.euler - mp.pi/2 - 3*mp.log(2))), 5)

# ---------- 2. A_12 two ways ----------
def A12_direct(t):
    T = mp.mpf(t)
    return ((T/2)*(mp.digamma(A) + mp.log(12/mp.pi))
            + mp.mpf('0.25')*(z214 - mp.e**(-T/2)*mp.lerchphi(mp.e**(-2*T), 2, A)))

def A12_mirror(t):
    return -archimedean_term(float(t), dps=50) + (float(t)/2)*math.log(12)

out['A12_two_way'] = {str(t): {'direct': mp.nstr(A12_direct(t), 25),
                               'mirror': mp.nstr(A12_mirror(t), 25),
                               'absdiff': mp.nstr(abs(A12_direct(t)-A12_mirror(t)), 5)}
                      for t in ('0.3', '1.0', '2.0', '3.5')}

# ---------- tail ----------
def tail(t):
    """T(t) = (1/4)[zeta(2,1/4) - e^{-t/2} Phi(e^{-2t},2,1/4)] (the Lerch bracket)."""
    T = mp.mpf(t)
    return mp.mpf('0.25')*(z214 - mp.e**(-T/2)*mp.lerchphi(mp.e**(-2*T), 2, A))

# ---------- 3. series forms ----------
def tail_series_exp(t, M=400):
    """sum_m e^{-(2m+1/2)t}/(m+1/4)^2  (should equal e^{-t/2} Phi(e^{-2t},2,1/4))."""
    T = mp.mpf(t)
    return mp.nsum(lambda m: mp.e**(-(2*m + mp.mpf('0.5'))*T)/(m + A)**2, [0, M-1]) \
        if False else sum(mp.e**(-(2*m + mp.mpf('0.5'))*T)/(m + A)**2 for m in range(M))

def tail_ramp(t, M=2000):
    """(1/4) sum_m (1 - e^{-2(m+1/4)t})/(m+1/4)^2  (should equal T(t))."""
    T = mp.mpf(t)
    return mp.mpf('0.25')*sum((1 - mp.e**(-2*(m + A)*T))/(m + A)**2 for m in range(M))

out['series_check'] = {}
for t in ('0.4', '1.0', '2.0'):
    T = mp.mpf(t)
    lerch_val = mp.e**(-T/2)*mp.lerchphi(mp.e**(-2*T), 2, A)
    out['series_check'][t] = {
        'lerch': mp.nstr(lerch_val, 25),
        'exp_series': mp.nstr(tail_series_exp(t), 25),
        'absdiff': mp.nstr(abs(lerch_val - tail_series_exp(t)), 5),
        'tail_direct': mp.nstr(tail(t), 25),
        'tail_rampform': mp.nstr(tail_ramp(t), 25),
        'ramp_absdiff': mp.nstr(abs(tail(t) - tail_ramp(t)), 5)}

# ---------- 4. density closed form ----------
out['density_check'] = {}
for t in ('0.3', '1.0', '2.0'):
    T = mp.mpf(t)
    d2 = mp.diff(tail, T, 2)          # T''(t) by mpmath differentiation
    closed = mp.e**(-T/2)/(1 - mp.e**(-2*T))
    geo = sum(mp.e**(-(4*m+1)*T/2) for m in range(2000))
    out['density_check'][t] = {'-Tpp_numeric': mp.nstr(-d2, 25),
                               'closed_form': mp.nstr(closed, 25),
                               'geo_series': mp.nstr(geo, 25),
                               'absdiff_closed': mp.nstr(abs(-d2 - closed), 5),
                               'absdiff_geo': mp.nstr(abs(closed - geo), 5)}

# ---------- 5. small-t coefficients ----------
out['small_t_tail'] = {}
for t in ('0.1', '0.01', '0.001', '0.0001'):
    T = mp.mpf(t)
    out['small_t_tail'][t] = mp.nstr((tail(T) + mp.mpf('0.5')*T*mp.log(T))/T, 20)
out['kappa_candidate'] = mp.nstr(mp.mpf('0.5') + mp.pi/4 + mp.log(2), 20)
out['small_t_A12'] = {}
for t in ('0.1', '0.01', '0.001', '0.0001'):
    T = mp.mpf(t)
    out['small_t_A12'][t] = mp.nstr((A12_direct(T) + mp.mpf('0.5')*T*mp.log(T))/T, 20)
out['c_candidate'] = mp.nstr((1 - mp.euler + mp.log(6/mp.pi))/2, 20)

# ---------- 6. tail at the (2,1) station ----------
t21 = mp.log(2)
out['tail_at_log2'] = mp.nstr(tail(t21), 30)
out['A12_at_log2'] = mp.nstr(A12_direct(t21), 30)
out['tail_at_inf'] = mp.nstr(z214/4, 30)   # (pi^2 + 8G)/4
import sympy as sp
tv = sp.Float(str(tail(t21)), 30)
out['tail_log2_nsimplify'] = str(sp.nsimplify(tv, [sp.pi, sp.Catalan, sp.log(2),
                                                  sp.EulerGamma, sp.sqrt(2)]))

# ---------- 7. KS-side comparison data (exact rationals) ----------
# tail coefficients in s = e^{-t/2}:  s^{4m+1} * 16/(4m+1)^2
tail_coeffs = {4*m+1: Fraction(16, (4*m+1)**2) for m in range(5)}
# sech psi in s: 2s/(1+s^2) = 2 sum_j (-1)^j s^{2j+1}
sech_coeffs = {2*j+1: Fraction(2*(-1)**j) for j in range(7)}
# Gaussian moments at a=3/2: <u^{2j}> = (2j-1)!! / 3^j
def dfact_odd(j):
    r = 1
    for q in range(1, 2*j, 2):
        r *= q
    return r
gauss_moments = {j: Fraction(dfact_odd(j), 3**j) for j in range(5)}
out['coeff_table'] = {
    'tail_s_powers': {str(k): str(v) for k, v in tail_coeffs.items()},
    'sech_s_powers': {str(k): str(v) for k, v in sech_coeffs.items()},
    'gauss_moments_a3/2': {str(k): str(v) for k, v in gauss_moments.items()}}

print(json.dumps(out, indent=1))
with open('/home/hatch/workspace/d12/explorations/screw-stations/arch-ks/arch_ks_results.json', 'w') as fh:
    json.dump(out, fh, indent=1)
