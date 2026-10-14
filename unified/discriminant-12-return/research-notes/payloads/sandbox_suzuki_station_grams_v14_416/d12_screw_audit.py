#!/usr/bin/env python3
"""Normalization re-audit of the v13.258 D12 character screw vs Suzuki eq. (1.3).

Checks (guardrail from v13.285):
  A. chi_12 table -> L(1, chi_12) vs class-number value log(2+sqrt3)/sqrt3.
  B. Two independent transcriptions of A_12(t) agree:
       (i)  direct from v13.258 sec.3 formula (mpmath),
       (ii) -g_Gamma(t) + (t/2) log 12  [conductor only in the linear term].
  C. Phi_12 knot structure: R_12 = 0 below log 5; derivative jumps of Phi_12
     at log 5, log 7, log 11, log 25 equal -Lambda(n) chi_12(n)/sqrt(n).
  D. Small-t singularity: Phi_12(t) + (1/2) t log t has a finite linear
     coefficient as t -> 0 (sign test of Phi_12 = -g_chi convention).
  E. Laplace identity (v13.258 sec.5) at z=3:
       int_0^inf Phi_12(t) e^{-3t} dt  =?=  (1/9) * (Lambda_12'/Lambda_12)(7/2),
     RHS log-derivative from (1/2)log(12/pi) + (1/2)psi(7/4) + L'/L series.
"""
import json, math
import mpmath as mp
from suzuki_riemann_screw_calibration import archimedean_term  # = g_Gamma(t) of zeta

mp.mp.dps = 50

CHI = {1: 1, 5: -1, 7: -1, 11: 1}
def chi12(n):
    if math.gcd(n, 12) != 1:
        return 0
    return CHI[n % 12]

out = {}

# A. L(1, chi_12)
s = mp.nsum  # not used; plain partial sums with Euler-Maclaurin-free tail bound is slow at s=1.
# Use mpmath dirichlet if available, else partial sum to 200k with alternating-block estimate.
try:
    chi_seq = [0] * 12
    for r, v in CHI.items():
        chi_seq[r] = v
    L1 = mp.dirichlet(1, chi_seq)  # analytic continuation via mpmath
    out['L1_mpmath_dirichlet'] = float(L1)
except Exception as e:
    out['L1_mpmath_dirichlet'] = f'unavailable: {e}'
out['L1_class_number'] = float(mp.log(2 + mp.sqrt(3)) / mp.sqrt(3))

# B. A_12 two ways
def A12_direct(t):
    T = mp.mpf(t)
    psi = mp.digamma(mp.mpf('0.25'))
    C = mp.zeta(2, mp.mpf('0.25'))
    lerch = mp.lerchphi(mp.e ** (-2 * T), 2, mp.mpf('0.25'))
    return float((T / 2) * (psi + mp.log(12 / mp.pi)) + mp.mpf('0.25') * (C - mp.e ** (-T / 2) * lerch))

def A12_mirror(t):
    return -archimedean_term(t, dps=50) + (t / 2) * math.log(12)

out['A12_two_way'] = {str(t): {'direct': A12_direct(t), 'mirror': A12_mirror(t),
                               'absdiff': abs(A12_direct(t) - A12_mirror(t))}
                      for t in (0.3, 1.0, 2.0, 3.5)}

# C. R_12 and Phi_12
def prime_powers_chi(T):
    import numpy as np
    horizon = int(math.floor(math.exp(T)))
    sieve = np.ones(horizon + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(math.sqrt(horizon)) + 1):
        if sieve[p]:
            sieve[p * p:horizon + 1:p] = False
    out_pp = []
    for p in np.flatnonzero(sieve).astype(int):
        pk = int(p)
        while pk <= horizon:
            c = chi12(pk)
            if c:
                out_pp.append((pk, c * math.log(p) / math.sqrt(pk)))
            if pk > horizon // p:
                break
            pk *= p
    return sorted(out_pp)

_PP14 = prime_powers_chi(14.0)  # computed once; reused by every R12 call
def R12(t):
    T = abs(t)
    # breakpoints beyond e^14 contribute < 1e-13 under the e^{-3t} weight
    return sum(c * max(T - math.log(n), 0.0) for n, c in _PP14 if math.log(n) <= min(T, 14.0))

def Phi12(t):
    return A12_mirror(abs(t)) - R12(t)

out['R12_below_log5'] = R12(math.log(5) - 1e-9)
out['R12_zero_for_t_lt_log5_expected'] = 0.0

def jump(func, T, h=2e-5):
    return (func(T + h) - func(T)) / h - (func(T) - func(T - h)) / h

out['Phi12_jumps'] = {}
for n in (5, 7, 11, 25):
    pred = -chi12(n) * (math.log(5) if n in (5, 25) else math.log(n)) / math.sqrt(n)
    if n == 25:
        pred = -chi12(25) * math.log(5) / 5.0
    out['Phi12_jumps'][f'log{n}'] = {'measured': jump(Phi12, math.log(n)), 'predicted': pred}

# D. small-t: (Phi12(t) + 0.5 t log t)/t should converge; with -0.5 sign it must not
rows = []
for t in (0.2, 0.1, 0.05, 0.02, 0.01):
    v = Phi12(t)
    rows.append({'t': t,
                 'plus_half_coeff': (v + 0.5 * t * math.log(t)) / t,
                 'minus_half_coeff': (v - 0.5 * t * math.log(t)) / t})
out['small_t_fit'] = rows

# E. Laplace identity at z=3, s=7/2
z = 3.0
s_val = 0.5 + z
lhs = mp.quad(lambda tt: (A12_mirror(float(tt)) - R12(float(tt))) * mp.e ** (-z * tt), [0, 14])
# L'/L(s, chi) = -sum Lambda(n) chi(n) n^{-s} over prime powers, s=7/2 (fast tail)
NMAX = 20000
import numpy as np
sieve = np.ones(NMAX + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(math.sqrt(NMAX)) + 1):
    if sieve[p]:
        sieve[p * p:NMAX + 1:p] = False
LpL = 0.0
for p in np.flatnonzero(sieve).astype(int):
    lp = math.log(p); pk = int(p)
    while pk <= NMAX:
        c = chi12(pk)
        if c:
            LpL -= c * lp * pk ** (-s_val)
        if pk > NMAX // p:
            break
        pk *= p
LamLogDer = 0.5 * math.log(12 / math.pi) + 0.5 * float(mp.digamma(mp.mpf(s_val) / 2)) + LpL
rhs = LamLogDer / z ** 2
out['laplace_z3'] = {'lhs_integral': float(lhs), 'rhs': rhs, 'absdiff': abs(float(lhs) - rhs)}

print(json.dumps(out, indent=1, default=str))
with open('d12_audit_results.json', 'w') as fh:
    json.dump(out, fh, indent=1, default=str)
