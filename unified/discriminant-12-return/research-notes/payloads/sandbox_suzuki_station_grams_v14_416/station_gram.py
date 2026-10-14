#!/usr/bin/env python3
"""Station-sampled Suzuki screw kernel — exploratory sandbox computation.

Samples Suzuki's increment kernel G_g(u,v) = g(u-v) - g(u) - g(v)
(g even, g(0)=0) on the dictionary station lattice u_n = log n = 2*psi_n.
Kernel arguments on pairs are the pair rapidities: u_n - u_k = log(n/k) = 2*psi_{n,k}.

Checks (all finite, [N]):
  1. Eigenstructure of the station Gram matrix (screw property on points
     <=> all finite Grams PSD; for g_zeta this is Suzuki's RH-equivalent
     condition restricted to this finite point set -- necessary only).
  2. Zero-mass identity: for sum f = 0, f^T K f == f^T G f exactly
     (K = stationary kernel g(u_n-u_k)) -- discrete echo of v13.753 sec.7.
  3. Piecewise Grams (pole / prime / archimedean / pole+arch): which pieces
     carry the finite positivity.
  4. Knot derivative jumps at log 3, log 4 vs Lambda/sqrt predictions.
  5. Conical screw dilation covariance: chord(u,u+h) = e^u * chord(0,h)
     for the constant-pitch conical screw (log coordinate stationarity).
"""
import json, math
from fractions import Fraction
import numpy as np
from suzuki_riemann_screw_calibration import pole_term, prime_ramp, archimedean_term

N = 32
_cache = {}
def arch(t):
    key = round(abs(t), 12)
    if key not in _cache:
        _cache[key] = archimedean_term(abs(t), dps=50)
    return _cache[key]

def g_full(t):  return pole_term(t) + prime_ramp(t) + arch(t)
def g_pole(t):  return pole_term(t)
def g_prime(t): return prime_ramp(t)
def g_arch(t):  return arch(t)
def g_noPrime(t): return pole_term(t) + arch(t)

def gram(gfun, N):
    u = [math.log(n) for n in range(1, N + 1)]
    G = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            G[i, j] = gfun(u[i] - u[j]) - gfun(u[i]) - gfun(u[j])
    return G

def eig_report(G):
    w = np.linalg.eigvalsh((G + G.T) / 2)
    return {
        'lambda_min': float(w[0]), 'lambda_max': float(w[-1]),
        'n_negative_beyond_1e-9': int(np.sum(w < -1e-9)),
        'n_negative_beyond_1e-7': int(np.sum(w < -1e-7)),
        'smallest5': [float(x) for x in w[:5]],
    }

out = {}
G = gram(g_full, N)
out['full'] = eig_report(G)
for name, gf in [('pole', g_pole), ('prime', g_prime), ('arch', g_arch), ('pole+arch', g_noPrime)]:
    out[name] = eig_report(gram(gf, N))

# zero-mass identity (exact algebra, numerical verification)
rng = np.random.default_rng(20261014)
u = np.array([math.log(n) for n in range(1, N + 1)])
K = np.array([[g_full(u[i] - u[j]) for j in range(N)] for i in range(N)])
f = rng.standard_normal(N); f -= f.mean()
out['zero_mass_identity_absdiff'] = float(abs(f @ K @ f - f @ G @ f))
f2 = rng.standard_normal(N)  # nonzero mass: identity must FAIL (gauge terms live)
out['nonzero_mass_identity_absdiff'] = float(abs(f2 @ K @ f2 - f2 @ G @ f2))

# knot jumps
def jump(T):
    h = 2e-5
    dl = (g_full(T) - g_full(T - h)) / h
    dr = (g_full(T + h) - g_full(T)) / h
    return dr - dl
out['knot_jumps'] = {
    'log3': {'measured': jump(math.log(3)), 'predicted_Lambda/sqrt': math.log(3) / math.sqrt(3)},
    'log4': {'measured': jump(math.log(4)), 'predicted_Lambda/sqrt': math.log(2) / 2.0},
}

# conical screw dilation covariance: point(u) = e^u (sin a cos(b u), sin a sin(b u), cos a)
a, b = 0.6, 1.3
def pt(uu):
    return np.array([math.exp(uu) * math.sin(a) * math.cos(b * uu),
                     math.exp(uu) * math.sin(a) * math.sin(b * uu),
                     math.exp(uu) * math.cos(a)])
errs = []
for uu in (0.0, 0.7, 1.9):
    for h in (0.3, 1.1):
        lhs = np.linalg.norm(pt(uu + h) - pt(uu))
        rhs = math.exp(uu) * np.linalg.norm(pt(h) - pt(0.0))
        errs.append(abs(lhs - rhs))
out['cone_screw_dilation_covariance_maxerr'] = float(max(errs))

print(json.dumps(out, indent=1))
with open('results.json', 'w') as fh:
    json.dump(out, fh, indent=1)
