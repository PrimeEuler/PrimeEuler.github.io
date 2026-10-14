#!/usr/bin/env python3
"""D12 screws sampled on the station lattice — after the re-audit passed.

g_chi(t) = R_12(t) + arch(t) - (t/2) log 12          (Suzuki g for L(s, chi_12); = -Phi_12)
g_K(t)   = g_zeta(t) + g_chi(t)                       (Dedekind screw of Q(sqrt3))
         = pole(t) + (ramp_zeta + R_12)(t) + 2 arch(t) - (t/2) log 12
arch(t) is Suzuki's zeta archimedean term from the repo calibration script,
served from the shared arch_cache.json (keys quantized to 1e-9).
Finite PSD of the chi Gram is the finite GRH(chi_12) echo; of the K Gram,
the finite GRH-for-Q(sqrt3) echo. [N] finite statements only.
"""
import json, math, os
import numpy as np
from suzuki_riemann_screw_calibration import pole_term, prime_ramp

# R_12 implemented locally (importing the audit module would rerun its quadrature)
_CHI = {1: 1, 5: -1, 7: -1, 11: 1}
def _chi12(n):
    return 0 if math.gcd(n, 12) != 1 else _CHI[n % 12]

def _prime_powers_chi(T):
    horizon = int(math.floor(math.exp(T)))
    sieve = np.ones(horizon + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(math.sqrt(horizon)) + 1):
        if sieve[p]:
            sieve[p * p:horizon + 1:p] = False
    out_pp = []
    for p in np.flatnonzero(sieve).astype(int):
        pk = int(p)
        while pk <= horizon:
            c = _chi12(pk)
            if c:
                out_pp.append((pk, c * math.log(int(p)) / math.sqrt(pk)))
            if pk > horizon // int(p):
                break
            pk *= int(p)
    return sorted(out_pp)

_PP = _prime_powers_chi(5.0)  # covers |t| <= log 128 with room
def R12(t):
    T = abs(t)
    return sum(c * max(T - math.log(n), 0.0) for n, c in _PP if math.log(n) <= T)

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, 'arch_cache.json')) as fh:
    ARCH = {round(float(k), 9): v for k, v in json.load(fh).items()}

def arch(t):
    return ARCH[round(abs(t), 9)]

def g_chi(t):
    T = abs(t)
    return R12(T) + arch(T) - (T / 2) * math.log(12)

def g_K(t):
    T = abs(t)
    return pole_term(T) + prime_ramp(T) + R12(T) + 2 * arch(T) - (T / 2) * math.log(12)

def g_K_archpiece(t):
    T = abs(t)
    return 2 * arch(T) - (T / 2) * math.log(12)

def g_K_ramppiece(t):
    T = abs(t)
    return prime_ramp(T) + R12(T)

def gram(gfun, N):
    u = [math.log(n) for n in range(1, N + 1)]
    G = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            G[i, j] = gfun(u[i] - u[j]) - gfun(u[i]) - gfun(u[j])
    return G

def eig_report(G):
    w = np.linalg.eigvalsh((G + G.T) / 2)
    return {'lambda_min': float(w[0]), 'lambda_2': float(w[1]), 'lambda_3': float(w[2]),
            'lambda_max': float(w[-1]),
            'n_negative_beyond_1e-9': int(np.sum(w < -1e-9)),
            'n_negative_beyond_1e-7': int(np.sum(w < -1e-7))}

out = {}
for N in (32, 64):
    out[f'chi_N{N}'] = eig_report(gram(g_chi, N))
    out[f'K_N{N}'] = eig_report(gram(g_K, N))
out['K_pieces_N32'] = {
    'pole_only': eig_report(gram(lambda t: pole_term(t), 32)),
    'ramp_only': eig_report(gram(g_K_ramppiece, 32)),
    'arch_doubled_only': eig_report(gram(g_K_archpiece, 32)),
}

# zero-mass identity for g_K (N=32)
N = 32
u = np.array([math.log(n) for n in range(1, N + 1)])
Kk = np.array([[g_K(u[i] - u[j]) for j in range(N)] for i in range(N)])
Gk = gram(g_K, N)
rng = np.random.default_rng(20261014)
f = rng.standard_normal(N); f -= f.mean()
out['K_zero_mass_identity_absdiff'] = float(abs(f @ Kk @ f - f @ Gk @ f))

print(json.dumps(out, indent=1))
with open(os.path.join(HERE, 'd12_gram_results.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
