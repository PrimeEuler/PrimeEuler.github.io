"""
Independent re-derivation of odd_sector_analytic.md's Route A/C/D/E, using
MY OWN g(t) (fem_screw_audit.py from Round 134) and a from-scratch P1 Galerkin
assembly directly on (0,A), NOT reusing r_gate.py's assemble() or any sandbox
projection code. Built to cross-check the claim:
  T_- = odd sector, kernel k_-(x,y) = [g(x-y) - g(x+y)] + min(x,y), lam=-1.
Checks: (A) kernel identity spot-check, (C) no negative eigs + eigenvector
frequency tracking the mesh, (E) Picard-sum growth for the x-source.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh
import sys
sys.path.insert(0, '.')
import fem_screw_audit as fsa

A = 2.0


def build_T_minus(Nsub, g):
    """Direct element-Gauss assembly of T_- on (0,A), P1, dofs = nodes 1..Nsub
    (node 0 dropped: Dirichlet; node Nsub kept: natural Neumann)."""
    h = A / Nsub
    xs = h * np.arange(Nsub + 1)
    q = 8
    u, w = leggauss(q)

    # gather per-element quadrature points/weights once
    elems = []
    for e in range(Nsub):
        x0, x1 = xs[e], xs[e + 1]
        xg = 0.5 * (x0 + x1) + 0.5 * h * u
        wg = 0.5 * h * w
        elems.append((e, xg, wg))

    ndof = Nsub  # nodes 1..Nsub
    T = np.zeros((ndof, ndof))

    # kernel k_-(x,y) = g(x-y) - g(x+y) + min(x,y)
    for (ea, xg, wg) in elems:
        pe_a = (xs[ea + 1] - xg) / h   # hat for node ea
        pe1_a = (xg - xs[ea]) / h      # hat for node ea+1
        for (eb, yg, wgb) in elems:
            pe_b = (xs[eb + 1] - yg) / h
            pe1_b = (yg - xs[eb]) / h
            X, Y = np.meshgrid(xg, yg, indexing='ij')
            Kxy = g(X - Y) - g(X + Y) + np.minimum(X, Y)
            Wxy = np.outer(wg, wgb)
            cell = Wxy * Kxy
            # 4 node combinations for this element pair
            contribs = [
                (ea, eb, np.sum(cell * np.outer(pe_a, pe_b))),
                (ea, eb + 1, np.sum(cell * np.outer(pe_a, pe1_b))),
                (ea + 1, eb, np.sum(cell * np.outer(pe1_a, pe_b))),
                (ea + 1, eb + 1, np.sum(cell * np.outer(pe1_a, pe1_b))),
            ]
            for (ia, ib, val) in contribs:
                if ia >= 1 and ib >= 1:
                    T[ia - 1, ib - 1] += val
    return T, xs


def mass_matrix(Nsub):
    h = A / Nsub
    ndof = Nsub
    M = np.zeros((ndof, ndof))
    # standard P1 mass on nodes 1..Nsub (node 0 Dirichlet-dropped)
    for i in range(ndof):
        M[i, i] += 2.0 * h / 3.0 if i < ndof - 1 else h / 3.0  # last node half-element (Neumann boundary dof)
    for i in range(ndof - 1):
        M[i, i + 1] += h / 6.0
        M[i + 1, i] += h / 6.0
    return M


def x_source(xs):
    # b_x,i = int x * phi_i dx over (0,A), node 0 dropped
    h = xs[1] - xs[0]
    Nsub = len(xs) - 1
    q = 8
    u, w = leggauss(q)
    ndof = Nsub
    bv = np.zeros(ndof)
    for e in range(Nsub):
        x0, x1 = xs[e], xs[e + 1]
        xg = 0.5 * (x0 + x1) + 0.5 * h * u
        wg = 0.5 * h * w
        pe = (x1 - xg) / h
        pe1 = (xg - x0) / h
        fv = xg
        if e >= 1:
            bv[e - 1] += np.sum(wg * pe * fv)
        bv[e] += np.sum(wg * pe1 * fv)
    return bv


print("Building independent g(t) (cached)...")
g = fsa.make_g('lambda', 2.0 * A + 1.0)

results = {}
for Nsub in [100, 200, 400]:
    T, xs = build_T_minus(Nsub, g)
    M = mass_matrix(Nsub)
    w, V = eigh(T, M)
    neg = np.sum(w < -1e-10)
    mu_min = w[0]
    mu_2nd = w[1]
    v0 = V[:, 0]
    # dominant frequency via FFT of the eigenvector (uniform nodes 1..Nsub)
    spec = np.abs(np.fft.rfft(v0))
    dom_freq = np.argmax(spec[1:]) + 1
    bx = x_source(xs)
    # Picard sum in M-orthonormal eigensystem: coefficients c_j = v_j^T M bx (V is M-orthonormal from eigh(T,M))
    coeffs = V.T @ (M @ bx)
    picard_terms = coeffs**2 / w**2
    picard_partial = np.cumsum(picard_terms)
    results[Nsub] = dict(neg=neg, mu_min=mu_min, mu_2nd=mu_2nd, dom_freq=dom_freq,
                          picard_last=picard_partial[-1], picard_mid=picard_partial[len(picard_partial)//2])
    print(f"Nsub={Nsub:5d} dofs={Nsub:5d} neg_eigs={neg} mu_min={mu_min:.4e} mu_2nd={mu_2nd:.4e} "
          f"dom_freq={dom_freq} (Nyquist~{Nsub//2}) picard[mid]={results[Nsub]['picard_mid']:.3e} "
          f"picard[last]={results[Nsub]['picard_last']:.3e}", flush=True)

print("\nDone.")
