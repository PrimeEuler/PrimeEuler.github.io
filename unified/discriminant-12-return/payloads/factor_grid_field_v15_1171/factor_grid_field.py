"""
Lattice field on the k=4 factor grid (2026-11-18, sandbox;
Jeremy's call: extend the null-grid field (v15.1167) --
"factors, then tilt on top", part 1 of 2).

The record's k-factor Hessian metric (v14.953-955,
research note General_Kfactor_Hessian_Lorentzian_
Signature_vs_Ghost): for positive x_i, P = prod x_i,
the pullback of the affine Hessian of P gives
  ds^2 = P [ (sum d ln x_i)^2 - sum (d ln x_i)^2 ],
inertia (1, k-1). In log-factor coordinates y_i = ln x_i
this is ds^2 = 2P * sum_{i<j} dy_i dy_j: a CONSTANT
form (matrix A: 0 diagonal, 1 off-diagonal) times the
conformal factor 2P. Light cones are conformally
invariant, so the field built here is the conformal
representative's field on the grid Z^4 in y; the
physical metric's tau = 2 sqrt((k-1)/k) sqrt(P), at
k=4 a(tau) = tau/sqrt(3) (filed K4). The grid operator
is L = sum_{i<j} Du_i Du_j (one-sided differences),
the k=4 lift of v15.1167's Du Dv.

Checks: signature; the filed FLRW arithmetic; pair-plane
exactness (the 1+1 miracle survives on every factor
pair plane); a generic 4D cone wave is NOT a lattice
solution (full exactness dies, quantified); wave speed
and energy in orthonormal (s0, z) coordinates; the grid
diagonal is logarithmic proper time.
"""
import numpy as np
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

k = 4
A = sp.Matrix([[0 if i == j else 1 for j in range(k)]
               for i in range(k)])
ev = A.eigenvals()
check("F1 form A (0 diag, 1 off-diag) at k=4 has "
      "eigenvalues {3, -1, -1, -1}: signature (1,3)",
      ev == {3: 1, -1: 3})

# filed arithmetic: tau and a(tau) at k=4, R = -2/P
P = sp.symbols("P", positive=True)
tau = 2 * sp.sqrt(sp.Rational(k - 1, k)) * sp.sqrt(P)
a = sp.sqrt(sp.Rational(k, 4 * (k - 1))) * tau
R = -6 / tau**2
check("F2 filed K4 arithmetic: a(tau) = tau/sqrt(3) and "
      "R = -6/tau^2 = -2/P at k=4",
      sp.simplify(a - tau / sp.sqrt(3)) == 0
      and sp.simplify(R + 2 / P) == 0)

# lattice operator on Z^4, integer arithmetic
rng = np.random.default_rng(11)
N = 8
def L(phi):
    # every pair term evaluated on the common interior
    # block (all axes trimmed by one)
    shp = tuple(s - 1 for s in phi.shape)
    out = np.zeros(shp, dtype=phi.dtype)
    for i in range(4):
        for j in range(i + 1, 4):
            def sl(di, dj):
                s = [slice(0, -1)] * 4
                if di: s[i] = slice(1, None)
                if dj: s[j] = slice(1, None)
                return tuple(s)
            out += (phi[sl(1, 1)] - phi[sl(1, 0)]
                    - phi[sl(0, 1)] + phi[sl(0, 0)])
    return out

# pair-plane exactness: any phi(y1,y2) with D1D2 phi = 0,
# constant in y3,y4, solves L phi = 0 exactly
f = rng.integers(-5, 6, N + 1)
g = rng.integers(-5, 6, N + 1)
plane = (f[:, None] + g[None, :])
phi4 = np.zeros((N + 1, N + 1, 3, 3), dtype=int)
phi4[:, :, :, :] = plane[:, :, None, None]
check("F3 pair-plane exactness: a 1+1 massless solution "
      "on the (y1,y2) plane, constant in y3,y4, solves "
      "the k=4 lattice equation EXACTLY",
      np.all(L(phi4) == 0))

# generic cone wave: p* on the continuum cone, 3 active
# coordinates; continuum symbol 0, lattice symbol != 0
pst = [sp.Rational(1), sp.Rational(1), sp.Rational(-1, 2),
       sp.Rational(0)]
cont = sum(pst[i] * pst[j] for i in range(4)
           for j in range(i + 1, 4))
def lat_symbol(p):
    e = [complex(np.exp(1j * float(x)) - 1) for x in p]
    return sum(e[i] * e[j] for i in range(4)
               for j in range(i + 1, 4))
s1 = abs(lat_symbol(pst))
s01 = abs(lat_symbol([x * sp.Rational(1, 10) for x in pst]))
s02 = abs(lat_symbol([x * sp.Rational(2, 10) for x in pst]))
print(f"    cone wave p*=(1,1,-1/2,0): continuum symbol "
      f"{cont}; lattice |symbol| at p* = {s1:.4f}; "
      f"scaling |s(0.2p*)|/|s(0.1p*)| = {s02/s01:.2f} "
      f"(8 = cubic, the on-cone leading term)")
check("F4 full 4D exactness DIES: p* is exactly on the "
      "continuum cone but the lattice symbol is nonzero, "
      "vanishing only cubically as p -> 0",
      cont == 0 and s1 > 0.05 and 6.5 < s02 / s01 < 9.5)

# orthonormal coordinates: s0 = sum(y)/2, form becomes
# 3 ds0^2 - |dz|^2, so phi_{s0 s0} = 3 laplacian_z phi,
# wave speed sqrt(3). Leapfrog on a cubic z grid with a
# compact smooth pulse (support radius 4).
n = 41
c0 = n // 2
dt = 0.25
steps = 24
yy, xx, zz = np.mgrid[0:n, 0:n, 0:n]
rr = np.sqrt((yy - c0)**2 + (xx - c0)**2 + (zz - c0)**2)
cur = np.where(rr < 4, 0.5 * (1 + np.cos(np.pi * rr / 4)), 0.0)
prev = cur.copy()
def lap(a):
    return (np.roll(a, 1, 0) + np.roll(a, -1, 0)
            + np.roll(a, 1, 1) + np.roll(a, -1, 1)
            + np.roll(a, 1, 2) + np.roll(a, -1, 2) - 6 * a)
energies = []
for s in range(steps):
    nxt = 2 * cur - prev + 3 * dt**2 * lap(cur)
    nxt[0, :, :] = nxt[-1, :, :] = 0
    nxt[:, 0, :] = nxt[:, -1, :] = 0
    nxt[:, :, 0] = nxt[:, :, -1] = 0
    prev, cur = cur, nxt
    vel = (cur - prev) / dt
    gx = np.gradient(cur, axis=0); gy = np.gradient(cur, axis=1)
    gz = np.gradient(cur, axis=2)
    energies.append(float(np.sum(vel**2)
                          + 3 * np.sum(gx**2 + gy**2 + gz**2)))
t = steps * dt
prof = np.abs(cur[c0, c0, :])
speeds = {}
for thr in (1e-2, 1e-3, 1e-4):
    above = np.where(prof > thr)[0]
    speeds[thr] = (above.max() - c0 - 4) / t
print(f"    wave at t={t}: axis front net speeds by "
      f"absolute threshold: 1e-2 -> {speeds[1e-2]:.3f}, "
      f"1e-3 -> {speeds[1e-3]:.3f}, 1e-4 -> "
      f"{speeds[1e-4]:.3f} (continuum cone sqrt(3) = "
      f"1.732; spread = dispersive precursors, filed); "
      f"energy ratio max/min = "
      f"{max(energies)/min(energies):.2f}")
check("F5 (s0,z) wave: front at the 1e-3 level tracks "
      "the (1,3) cone speed sqrt(3) within 15%; discrete "
      "energy positive and bounded (no ghost, v14.955)",
      abs(speeds[1e-3] - np.sqrt(3)) < 0.25
      and max(energies) / min(energies) < 3
      and min(energies) > 0)

# grid diagonal = logarithmic proper time:
# y = (n,n,n,n): P = e^{4n}, tau = sqrt(3) e^{2n}
ns = np.arange(5)
taus = np.sqrt(3) * np.exp(2 * ns)
check("F6 diagonal of the factor grid is log-time: "
      "equal diagonal steps multiply tau by e^2 exactly",
      np.allclose(taus[1:] / taus[:-1], np.exp(2)))

print("ALL PASS" if ok else "SOME FAILED")
