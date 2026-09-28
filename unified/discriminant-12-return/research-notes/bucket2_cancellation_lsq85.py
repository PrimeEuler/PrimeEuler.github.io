"""
Direct (8.5) regularized least-squares solver.

Suzuki v2 p.30: "(8.5) is an ordinary Fredholm integral equation of the
first kind. This observation suggests a numerical approach. One may
compute v_+/- by solving this Fredholm equation numerically."

(8.5): int_{-A}^{A} k(x,y)(-v(y)) dy = C e^{+-x} + A_pm x + B_pm,
       k(x,y) = g(x-y) - lam*N(x,y),
       N(x,y) = (x^2+y^2)/(4A) - |x-y|/2 + A/6.

We solve for (v_h in V_h, A_pm, B_pm) by regularized least squares on
collocation points. This avoids the P1 weak-form instability entirely
(the weak form's discrete spectrum blows up like -1/h from a spurious
high-frequency endpoint mode; see report). The residual IS the gate.

V_h is either full P1 (natural) or P1-Dirichlet, so the Horn A comparison
(Dirichlet vs natural at fixed lam) is clean.

Regularization: Tikhonov alpha*||v_h||^2_{L^2} (mass norm). Alpha is
scanned; results must be alpha-insensitive in the converged regime.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss


def N_kernel(x, y, A):
    return (x ** 2 + y ** 2) / (4 * A) - np.abs(x - y) / 2 + A / 6


class Lsq85:
    def __init__(self, screw, A, N, lam, M_coll=None, q=12, dirichlet=False):
        self.screw, self.A, self.N, self.lam = screw, A, N, lam
        self.h = 2 * A / N
        self.nodes = np.linspace(-A, A, N + 1)
        self.q = q
        self.dirichlet = dirichlet
        Mc = M_coll or 4 * N
        self.xs = np.linspace(-A, A, Mc)
        self._assemble()

    def _K_row(self, x):
        """Row of K: int k(x,y) phi_i(y) dy for all P1 basis phi_i."""
        s, N, A, h, q, lam = self.screw, self.N, self.A, self.h, self.q, self.lam
        xi, w = leggauss(q)
        xe = self.nodes[:-1]
        row = np.zeros(N + 1)
        # g-term: int g(x-y) phi_i(y) dy. phi_i supported on elements i-1,i.
        # per-element Gauss, accumulate to the two nodes.
        for e in range(N):
            a_e, b_e = xe[e], xe[e] + h
            # split at y=x for the |x-y| kink in N (and g cusp at x=y handled
            # by fine quadrature; g is continuous)
            if a_e < x < b_e:
                segs = [(a_e, x), (x, b_e)]
            else:
                segs = [(a_e, b_e)]
            for (l, r) in segs:
                if r - l < 1e-15:
                    continue
                yqq = l + (r - l) * (xi + 1) / 2.0
                wqq = w * (r - l) / 2.0
                kval = s.g_fast(x - yqq) - lam * N_kernel(x, yqq, A)
                tt = (yqq - a_e) / h
                # phi_e = 1-tt, phi_{e+1} = tt
                row[e] += ((kval * (1 - tt)) * wqq).sum()
                row[e + 1] += ((kval * tt) * wqq).sum()
        return row

    def _assemble(self):
        N = self.N
        K = np.zeros((len(self.xs), N + 1))
        for j, x in enumerate(self.xs):
            K[j, :] = self._K_row(x)
        if self.dirichlet:
            K = K[:, 1:-1]
            ndof = N - 1
        else:
            ndof = N + 1
        self.K = K
        # mass matrix for regularization (on the active DOFs)
        h = self.h
        M = np.zeros((ndof, ndof))
        if self.dirichlet:
            np.fill_diagonal(M, 2 * h / 3)
            np.fill_diagonal(M[1:], h / 6)
            np.fill_diagonal(M[:, 1:], h / 6)
        else:
            np.fill_diagonal(M, 2 * h / 3)
            M[0, 0] = h / 3
            M[-1, -1] = h / 3
            np.fill_diagonal(M[1:], h / 6)
            np.fill_diagonal(M[:, 1:], h / 6)
        self.Mm = M
        # affine columns [x_j, 1]
        self.X = np.vstack([self.xs, np.ones_like(self.xs)]).T

    def solve(self, z, alpha=1e-8):
        """Solve min ||K c + X[a;b] + d||^2 + alpha*c'Mm c, d_j = e^{z x_j}.

        (8.5): K(-v) = e^{zx} + A x + B  =>  K c + X[A;B] + d = 0 with c = -v.
        We solve for c (= -v_h) then flip sign. Actually simpler: solve for
        v directly: -K v + ... let me define clearly below.
        """
        K, X, d = self.K, self.X, np.exp(z * self.xs)
        # unknowns [v; A; B]:  -K v - X[A;B] - d = 0  =>  [K, X][v;A;B] = -d
        Mx = np.hstack([K, X])                      # M x (ndof+2)
        rhs = -d
        # Tikhonov on v only: augment with sqrt(alpha)*L, L'L = Mm
        L = np.linalg.cholesky(self.Mm)
        Z = np.zeros((self.Mm.shape[0], 2))
        Maug = np.vstack([Mx, np.hstack([np.sqrt(alpha) * L, Z])])
        raug = np.concatenate([rhs, np.zeros(self.Mm.shape[0])])
        sol, *_ = np.linalg.lstsq(Maug, raug, rcond=None)
        ndof = self.Mm.shape[0]
        v, Acoef, Bcoef = sol[:ndof], sol[ndof], sol[ndof + 1]
        # residual (the gate)
        H = K @ v + X @ np.array([Acoef, Bcoef]) + d   # = K v + Ax + B + e^{zx}
        num = np.linalg.norm(H)
        den = np.linalg.norm(d - 1 - z * self.xs)
        gate = num / den
        sgn = 1.0 if np.real(z) > 0 else -1.0
        I1 = Acoef + sgn * 1.0
        I0 = Bcoef + 1.0
        # expand v to full nodal vector for reporting
        if self.dirichlet:
            vfull = np.zeros(self.N + 1)
            vfull[1:-1] = v
        else:
            vfull = v
        return {'v': vfull, 'A': float(Acoef), 'B': float(Bcoef),
                'gate': float(gate), 'I1': float(I1), 'I0': float(I0),
                'alpha': alpha}
