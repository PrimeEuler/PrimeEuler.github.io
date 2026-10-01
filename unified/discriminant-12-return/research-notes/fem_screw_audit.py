"""Independent re-implementation of make_g('lambda', tmax) from this session's
earlier (Round 127-131) build. Cached grid computed once at import time."""
import numpy as np
import mpmath as mp

mp.mp.dps = 20
_psi_quarter = float(mp.digamma(mp.mpf(1)/4))
_logpi = float(mp.log(mp.pi))

_NMAX = 100000
_is_comp = np.zeros(_NMAX+1, dtype=bool); _is_comp[0:2]=True
for i in range(2,int(_NMAX**0.5)+1):
    if not _is_comp[i]: _is_comp[i*i::i]=True
_primes = np.where(~_is_comp[2:_NMAX+1])[0]+2
_Lam = np.zeros(_NMAX+1)
for p in _primes:
    pk=p
    while pk<=_NMAX:
        _Lam[pk]=np.log(p)
        pk*=p
_ns = np.arange(2, _NMAX+1)
_logns = np.log(_ns)

def _F_of_at(at_mpf):
    z = mp.e**(-2*at_mpf)
    return mp.e**(-at_mpf/2) * mp.lerchphi(z, 2, mp.mpf(1)/4)
_F0 = _F_of_at(mp.mpf(0))

def _g_scalar(at):
    arch = -4*(np.exp(at/2) + np.exp(-at/2) - 2)
    lin = -(at/2)*(_psi_quarter - _logpi)
    Fat = _F_of_at(mp.mpf(at))
    lerch = -(1/4)*float(_F0 - Fat)
    if at <= 0:
        psum = 0.0
    else:
        cap = np.exp(at)
        mask = _ns <= cap
        if not mask.any():
            psum = 0.0
        else:
            w = _Lam[2:_NMAX+1][mask]
            terms = w/np.sqrt(_ns[mask])*(at-_logns[mask])
            psum = terms.sum()
    return arch+lin+lerch+psum

# cache: build once per tmax value actually requested
_cache = {}

def make_g(variant, tmax):
    assert variant == 'lambda'
    key = round(tmax, 3)
    if key not in _cache:
        tgrid = np.linspace(0, tmax+0.5, 1201)
        gvals = np.array([_g_scalar(t) for t in tgrid])
        _cache[key] = (tgrid, gvals)
    tgrid, gvals = _cache[key]
    def g(t):
        t = np.asarray(t, dtype=float)
        return np.interp(np.abs(t), tgrid, gvals)
    return g
