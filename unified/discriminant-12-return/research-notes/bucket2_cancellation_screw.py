"""
D12 screw function, derived source-faithfully from ledger v13.258 / v13.772.

g_12(t) = R_12(t) - A_12(t),  t >= 0, then extended EVEN: g(t) = g_12(|t|).

R_12(t) = sum_{log m <= t} c_m (t - log m),  c_m = Lambda(m) chi_12(m) / sqrt(m)
        (prime ramp; ledger v13.772 says "untouched" -- we do not modify it)

A_12(t) = (t/2)(PSI_Q + LOG_12_PI) + (1/4)(ZETA_2_Q - e^{-t/2} Phi(e^{-2t},2,1/4))
        (archimedean part, exact closed form from v13.258)

Kinks of g' (distributional data, derived in phase1_kinks.py):
  For the even extension, at t = +/- log m (m a prime power with chi_12(m)!=0):
      jump of g' = +c_m   (both sides)
  i.e. -g''_dist = -g''_reg - sum_m c_m [delta(t - log m) + delta(t + log m)].

This module provides:
  - exact R_12 and its derivative (step function, no smoothing)
  - A_12 via vectorized Lerch series with integral tail correction
  - g on a kink-aligned grid + cubic spline (kinks are grid nodes, so no
    smoothing across kinks)
  - validation of the spline against mpmath Lerch at random points
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import expn

# ---- ledger constants (v13.258) ----
PSI_Q = -3.9170715877437315
LOG_12_PI = 1.340535241617135
ZETA_2_Q = 16.45371108
Q = np.sqrt(12 / np.pi)

# ---- Dirichlet character mod 12: chi_12 = chi_4 * chi_3 ----
def chi_12(m):
    r = m % 12
    table = {1: 1, 5: -1, 7: -1, 11: 1}
    return table.get(r, 0)

def prime_powers(tmax):
    """All prime powers m = p^k with log m <= tmax. Returns (m, log m, c_m)."""
    import sympy as sp
    out = []
    for p in sp.primerange(2, int(np.exp(tmax)) + 2):
        pp = p
        while pp <= np.exp(tmax):
            if chi_12(pp) != 0:
                c = float(sp.log(pp)) * 0  # placeholder
                lam = float(sp.log(pp))    # log(pp^k)=k log p, but Lambda(p^k)=log p
                # Lambda(m): log p for prime powers
                Lm = float(sp.log(p))
                cm = Lm * chi_12(pp) / np.sqrt(pp)
                out.append((pp, float(np.log(pp)), cm))
            pp *= p
    out.sort(key=lambda t: t[1])
    ms = np.array([t[0] for t in out], dtype=float)
    lms = np.array([t[1] for t in out])
    cms = np.array([t[2] for t in out])
    return ms, lms, cms

class D12Screw:
    def __init__(self, tmax, n_lerch=100000, n_base=20001, n_cluster=64):
        self.tmax = tmax
        self.ms, self.lms, self.cms = prime_powers(tmax)
        # cumulative sums for exact R_12
        self.cum_c = np.cumsum(self.cms)
        self.cum_clog = np.cumsum(self.cms * self.lms)
        self._n_lerch = n_lerch
        self._build_grid(n_base, n_cluster)
        self._build_spline()

    # ---------- exact R_12 ----------
    def R12(self, t):
        t = np.asarray(t, dtype=float)
        idx = np.searchsorted(self.lms, t, side='right') - 1
        C = np.where(idx >= 0, self.cum_c[np.clip(idx, 0, len(self.cum_c)-1)], 0.0)
        D = np.where(idx >= 0, self.cum_clog[np.clip(idx, 0, len(self.cum_clog)-1)], 0.0)
        return t * C - D

    def R12_prime(self, t):
        """Exact (a.e.) derivative: step function sum_{log m <= t} c_m."""
        t = np.asarray(t, dtype=float)
        idx = np.searchsorted(self.lms, t, side='right') - 1
        return np.where(idx >= 0, self.cum_c[np.clip(idx, 0, len(self.cum_c)-1)], 0.0)

    # ---------- A_12 via Lerch ----------
    def _lerch(self, t):
        """L(t) = e^{-t/2} Phi(e^{-2t}, 2, 1/4), vectorized with tail correction."""
        t = np.asarray(t, dtype=float)
        z = np.exp(-2.0 * t)
        a = 0.25
        N = self._n_lerch
        # partial sum in chunks to bound memory
        S = np.zeros_like(t)
        chunk = 5000
        n = np.arange(N, dtype=float)
        # vectorize over terms in chunks: S += sum_n z^n/(n+a)^2
        # use log-space for z^n when z close to 1 to avoid underflow issues (not needed)
        for start in range(0, N, chunk):
            nn = np.arange(start, min(start + chunk, N), dtype=float)
            # z^nn for all t: exp(nn * log z)
            lz = np.log(np.maximum(z, 1e-300))
            pw = np.exp(np.outer(lz, nn))          # (Mt, chunk)
            S += (pw / (nn + a) ** 2).sum(axis=1)
        # tail correction: integral approximation of sum_{n>=N} z^n/(n+a)^2
        # tail ~= mu e^{mu a} E_2(mu (N+a)), mu = -log z = 2t
        mu = -np.log(np.maximum(z, 1e-300))
        tail = np.where(mu > 1e-12,
                        mu * np.exp(mu * a) * expn(2, mu * (N + a)),
                        1.0 / (N + a))
        S += tail
        return np.exp(-t / 2.0) * S

    def A12(self, t):
        t = np.asarray(t, dtype=float)
        return ((t / 2.0) * (PSI_Q + LOG_12_PI)
                + 0.25 * (ZETA_2_Q - self._lerch(t)))

    def A12_prime(self, t):
        """Exact (a.e.) derivative of A_12.
        A_12'(t) = (PSI_Q+LOG_12_PI)/2 - (1/4) L'(t),
        L(t) = e^{-t/2} Phi(e^{-2t},2,1/4),
        L'(t) = -(1/2) e^{-t/2} Phi - 2 e^{-t/2} sum_{n>=1} n z^n/(n+1/4)^2.
        Smooth on (0, infty); ~ (1/2) log(1/(2t)) as t -> 0+."""
        t = np.asarray(t, dtype=float)
        z = np.exp(-2.0 * t)
        a = 0.25
        N = self._n_lerch
        Phi = np.zeros_like(t)
        S1 = np.zeros_like(t)
        chunk = 5000
        lz = np.log(np.maximum(z, 1e-300))
        for start in range(0, N, chunk):
            nn = np.arange(start, min(start + chunk, N), dtype=float)
            pw = np.exp(np.outer(lz, nn))
            Phi += (pw / (nn + a) ** 2).sum(axis=1)
            if start > 0 or True:
                nn1 = nn[nn >= 1]
                if len(nn1):
                    pw1 = np.exp(np.outer(lz, nn1))
                    S1 += ((nn1 * pw1) / (nn1 + a) ** 2).sum(axis=1)
        mu = -np.log(np.maximum(z, 1e-300))
        # tail corrections
        tail_phi = np.where(mu > 1e-12,
                            mu * np.exp(mu * a) * expn(2, mu * (N + a)),
                            1.0 / (N + a))
        # tail of sum n z^n/(n+a)^2 ~= E_1(mu(N+a)) - a mu e^{mu a} E_2(mu(N+a))
        tail_s1 = np.where(mu > 1e-12,
                           expn(1, mu * (N + a)) - a * mu * np.exp(mu * a) * expn(2, mu * (N + a)),
                           np.log((N + a)) + 1.0)  # ~ harmonic tail at z=1 (not used near 0)
        Phi += tail_phi
        S1 += tail_s1
        Lp = np.exp(-t / 2.0) * (-0.5 * Phi - 2.0 * S1)
        return 0.5 * (PSI_Q + LOG_12_PI) - 0.25 * Lp

    def g12_prime(self, t):
        """Exact (a.e.) derivative of one-sided g_12: step - A_12'."""
        t = np.asarray(t, dtype=float)
        return self.R12_prime(t) - self.A12_prime(t)

    # ---------- g ----------
    def g12(self, t):
        """g_12(t) for t >= 0 (one-sided ledger formula)."""
        return self.R12(t) - self.A12(t)

    def g(self, t):
        """Even extension: g(t) = g_12(|t|)."""
        return self.g12(np.abs(np.asarray(t, dtype=float)))

    # ---------- kink-aligned grid + spline ----------
    def _build_grid(self, n_base, n_cluster):
        pts = [0.0]
        # geometric cluster near 0 for the t log t singularity
        lo, hi = 1e-10, self.tmax
        cluster = np.geomspace(lo, hi, n_cluster)
        pts.extend(cluster.tolist())
        pts.extend(np.linspace(0, self.tmax, n_base).tolist())
        # every kink location log m <= tmax is a grid node
        pts.extend(self.lms[self.lms <= self.tmax].tolist())
        g = np.array(sorted(set(pts)))
        g = g[(g >= 0) & (g <= self.tmax)]
        self.grid = g

    def _build_spline(self):
        # Spline ONLY the smooth part A_12 (kinks live entirely in R_12).
        # A single C^2 spline through g would Gibbs-overshoot at the kinks.
        vals = self.A12(self.grid)
        self.A12_spline = CubicSpline(self.grid, vals, bc_type='not-a-knot')

    def g_fast(self, t):
        """Fast g: EXACT R_12 (step-function antiderivative, no smoothing)
        minus spline of the smooth archimedean part A_12. Kink-faithful by
        construction: jumps of g' are represented exactly."""
        t = np.abs(np.asarray(t, dtype=float))
        return self.R12(t) - self.A12_spline(t)

    # ---------- validation ----------
    def validate_vs_mpmath(self, n_pts=25, seed=0, dps=30):
        """Compare spline against mpmath lerchphi at random points."""
        from mpmath import mp, mpf, lerchphi, e as me
        mp.dps = dps
        rng = np.random.default_rng(seed)
        ts = rng.uniform(0, self.tmax, n_pts)
        # avoid exact kink points
        errs = []
        for t in ts:
            tt = mpf(str(t))
            z = me ** (-2 * tt)
            Phi = lerchphi(z, 2, mpf('0.25'))
            L = me ** (-tt / 2) * Phi
            A = (tt / 2) * (mpf(str(PSI_Q)) + mpf(str(LOG_12_PI))) \
                + mpf('0.25') * (mpf(str(ZETA_2_Q)) - L)
            R = mpf(str(self.R12(np.array([t]))[0]))
            g_ref = R - A
            g_num = self.g_fast(np.array([t]))[0]
            errs.append(abs(float(g_ref) - g_num))
        return ts, np.array(errs)
