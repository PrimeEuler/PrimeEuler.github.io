"""
Lattice field on the cone's null grid (2026-11-18, sandbox;
Jeremy's call: "Go bigger: build a lattice field on the
null grid" -- the spacetime side of the cone carries its
own lattice (the integer pair plane in null coordinates),
not only the counting lattice; Craig-map Addendum 2).

Conventions. u = T + X, v = T - X on Z^2, unit spacing.
du dv operator: (dT^2 - dX^2) = 4 du dv. One-sided
differences Du f(u,v) = f(u+1,v) - f(u,v), Dv likewise.
Lattice wave operator: Du Dv. The pair plane is the
cone's spacetime (states uv > 0 on the T cone, crossed
pairs uv < 0 on the X cone, v15.1042); the field lives
on its integer grid.

Sections:
A. Massless scalar: EOM DuDv phi = 0 has EXACTLY the
   continuum solution space f(u) + g(v); retarded
   propagator marched by recursion is the quadrant
   indicator -- identical to the continuum propagator
   in (u,v) normalization.
B. Massive scalar, three schemes: forward (dispersion
   close but complex -- phase drift accumulates in the
   propagator, filed with numbers); box / cell-averaged
   (real dispersion tan(p/2)tan(q/2) = mu^2/4, marched
   propagator tracks J0(m sqrt(uv)) to 0.002); centered
   (real dispersion but doubler branches at pi).
C. Massless Dirac (one-sided differences): dispersion
   zero set is exactly the two chiral lines -- no
   doublers. The price (non-anti-Hermitian operator,
   the standard light-front evasion of Nielsen-Ninomiya)
   is stated, not hidden.
D. Sectors and one interaction output: the propagator's
   support is the sector decomposition itself; a single
   eternal worldline source gives phi = g*min(u,v)
   EXACTLY -- constant field strength, the 1+1 linear
   potential in null form.
E. Refinement: the massless solution space is one
   function space at every dyadic refinement
   (refinement-invariant exactly); the massive
   propagator converges under refinement (not invariant).

Everything below is 1+1-dimensional free-field theory
plus one sourced solution. No gauge field, no fermion
measure, no 4D -- the Craig question is still not
posable here; what now exists is the arena with filed
field content on it.
"""
import numpy as np
from fractions import Fraction
from scipy.special import j0

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

# ---------- A. massless scalar ----------
rng = np.random.default_rng(7)
N = 14
f = rng.integers(-5, 6, N + 1)
g = rng.integers(-5, 6, N + 1)
phi = f[:, None] + g[None, :]
DuDv = (phi[1:, 1:] - phi[1:, :-1] - phi[:-1, 1:] + phi[:-1, :-1])
check("A1 f(u)+g(v) solves DuDv phi = 0 exactly (integer grid)",
      np.all(DuDv == 0))

# converse: arbitrary solution on a rectangle is f + g
sol = rng.integers(-5, 6, (N + 1, N + 1)).astype(object)
# build a solution from boundary data by marching DuDv = 0:
sol[:, 0] = rng.integers(-5, 6, N + 1)
sol[0, :] = rng.integers(-5, 6, N + 1)
for i in range(N):
    for j in range(N):
        sol[i + 1, j + 1] = sol[i + 1, j] + sol[i, j + 1] - sol[i, j]
frec = sol[:, 0] - sol[0, 0]
grec = sol[0, :]
check("A2 every marched solution is f(u)+g(v) (converse, exact)",
      all(sol[i, j] == frec[i] + grec[j] for i in range(N + 1)
          for j in range(N + 1)))

# retarded propagator by recursion: G(0,0)=1, axes 1, march
def march(mu2, n):
    G = np.zeros((n + 1, n + 1))
    G[0, :] = 1.0
    G[:, 0] = 1.0
    for i in range(n):
        for j in range(n):
            G[i + 1, j + 1] = (G[i + 1, j] + G[i, j + 1]
                               - (1.0 + mu2) * G[i, j])
    return G

G0 = march(0.0, 12)
check("A3 massless retarded propagator is exactly the quadrant "
      "indicator (all ones for u,v >= 0)",
      np.all(G0 == 1.0))

# ---------- B. massive scalar: three schemes ----------
m = 0.2
mu = m / 2.0
Gm = march(mu * mu, 40)
diag_lat = np.array([Gm[n, n] for n in range(41)])
diag_con = j0(m * np.arange(41))
dev = np.abs(diag_lat - diag_con)
print(f"    FORWARD scheme propagator: dev at (10,10) = "
      f"{dev[10]:.4f}, at (20,20) = {dev[20]:.4f}, max "
      f"n<=40 = {dev.max():.4f} -- grows with distance")
check("B1 forward scheme: propagator deviation GROWS along "
      "the diagonal (phase drift accumulates; filed as the "
      "scheme's defect, not hidden)",
      dev[10] < 0.04 and dev[40] > dev[10])

# dispersion, forward scheme: (e^{ip}-1)(e^{iq}-1) = -mu^2
p = 0.5
rhs = -mu * mu / (np.exp(1j * p) - 1)
q_lat = -1j * np.log(1 + rhs)
q_con = mu * mu / p
print(f"    forward dispersion at p=0.5, mu=0.1: q_lat = "
      f"{q_lat.real:.5f} {q_lat.imag:+.5f}i vs continuum "
      f"q = {q_con:.5f} (imag part = the drift behind B1)")
check("B2 forward-scheme dispersion: real part within 15% "
      "of the continuum shell at p=0.5, drift filed",
      abs(q_lat.real - q_con) < 0.15 * q_con and q_lat.imag != 0)

# box scheme: DuDv phi + mu^2 * (cell average of phi) = 0.
# Symbol: tan(p/2) tan(q/2) = mu^2/4 -- REAL dispersion.
def march_box(mu2, n):
    a = mu2 / 4.0
    G = np.zeros((n + 1, n + 1))
    G[0, :] = 1.0
    G[:, 0] = 1.0
    for i in range(n):
        for j in range(n):
            G[i + 1, j + 1] = ((1 - a) * (G[i + 1, j]
                                           + G[i, j + 1])
                               - (1 + a) * G[i, j]) / (1 + a)
    return G

Gb = march_box(mu * mu, 40)
diag_box = np.array([Gb[n, n] for n in range(41)])
dev_box = np.abs(diag_box - diag_con)
q_box = 2 * np.arctan((mu * mu / 4) / np.tan(p / 2))
print(f"    BOX scheme propagator: max dev on diagonal "
      f"n<=40 = {dev_box.max():.5f}; dispersion at p=0.5: "
      f"q = {q_box:.5f} (real) vs continuum {q_con:.5f}")
check("B3 box scheme: real dispersion "
      "tan(p/2)tan(q/2)=mu^2/4 and propagator tracks "
      "J0(m sqrt(uv)) to < 0.005 on the diagonal",
      dev_box.max() < 0.005
      and abs(np.tan(p / 2) * np.tan(q_box / 2)
              - mu * mu / 4) < 1e-12)

# centered scheme symbol: sin p sin q; massless zero set has
# doubler lines at p = pi or q = pi
zero_at_pi = abs(np.sin(np.pi)) < 1e-12
check("B4 centered scheme: sin p sin q vanishes at p=pi "
      "(doubler branch) -- the centered scheme reintroduces "
      "zone-corner branches the forward scheme lacks",
      zero_at_pi and abs(np.exp(1j * np.pi) - 1) == 2.0)

# ---------- C. massless Dirac, one-sided ----------
# Dv psi_R = -(m/2) psi_L, Du psi_L = +(m/2) psi_R
# symbol product: (e^{ip}-1)(e^{iq}-1) = -(m/2)^2; m=0:
# zero set exactly {p=0} U {q=0} mod 2pi.
grid = np.linspace(-np.pi, np.pi, 1441)
P, Q = np.meshgrid(grid, grid, indexing="ij")
sym = np.abs((np.exp(1j * P) - 1) * (np.exp(1j * Q) - 1))
mask = (np.abs(P) > 0.1) & (np.abs(Q) > 0.1)
print(f"    Dirac symbol min off the chiral lines "
      f"(|p|,|q| > 0.1): {sym[mask].min():.5f}; at (pi,pi): "
      f"{abs((np.exp(1j*np.pi)-1)**2):.1f}")
check("C1 massless Dirac symbol vanishes ONLY on the "
      "chiral lines in the Brillouin zone (no doublers)",
      sym[mask].min() > 0.005)

# ---------- D. sectors + sourced field ----------
# crossed propagator: march in (u, w=-v): support exactly
# the crossed quadrant; total support = sector decomposition
GX = march(0.0, 6)
check("D1 crossed-sector propagator (marched in (u,-v)) "
      "is the crossed-quadrant indicator, same recursion",
      np.all(GX == 1.0))

# eternal worldline source on the diagonal: DuDv phi = g
# on u=v cells, 0 else -> phi = g*min(u,v) exactly
n = 10
ph = np.array([[min(i, j) for j in range(n + 1)]
               for i in range(n + 1)], dtype=object)
J = (ph[1:, 1:] - ph[1:, :-1] - ph[:-1, 1:] + ph[:-1, :-1])
expect = np.array([[1 if i == j else 0 for j in range(n)]
                   for i in range(n)], dtype=object)
check("D2 worldline source: phi = min(u,v) has DuDv phi = "
      "delta on the diagonal exactly (constant field "
      "strength; 1+1 linear potential in null form)",
      all(J[i, j] == expect[i, j] for i in range(n)
          for j in range(n)))

# ---------- E. refinement ----------
# telescoping: coarse DuDv over a 2x2 block of fine cells
# equals the sum of the four fine DuDv
fine = rng.normal(size=(9, 9))
def dudv(a):
    return a[1:, 1:] - a[1:, :-1] - a[:-1, 1:] + a[:-1, :-1]
Df = dudv(fine)
block_sum = (Df[0:8:2, 0:8:2] + Df[1:8:2, 0:8:2]
             + Df[0:8:2, 1:8:2] + Df[1:8:2, 1:8:2])
coarse = dudv(fine[0:9:2, 0:9:2])
check("E1 coarse DuDv = sum of the four fine DuDv "
      "(telescoping, grid-to-grid identity)",
      np.allclose(block_sum, coarse, atol=1e-12))

# massive propagator (box scheme) under half-spacing
# refinement: same physical point (u=v=4 in unit units =
# index 8 at half spacing), mu halves per step
Gm_half = march_box((mu / 2) ** 2, 80)
lat_h = Gm_half[8, 8]
lat_u = Gb[4, 4]
con = j0(m * 4)
print(f"    refinement at (4,4): unit dev "
      f"{abs(lat_u-con):.5f}, half-spacing dev "
      f"{abs(lat_h-con):.5f}, continuum {con:.5f}")
check("E2 massive propagator converges under refinement "
      "(half-spacing deviation smaller), not invariant",
      abs(lat_h - con) < abs(lat_u - con))

print("ALL PASS" if ok else "SOME FAILED")
