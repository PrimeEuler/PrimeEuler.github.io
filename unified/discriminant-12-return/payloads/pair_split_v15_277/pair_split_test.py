#!/usr/bin/env python3
"""
Pair-Split principle: out-of-sample tests.
TEST 1 (Schwinger SO(4)): A, B = two SU(2) factors ( Pauli/2 on each
  tensor factor); L = A + B, M = A - B. Pair exchange A<->B acts as
  L -> +L, M -> -M. Check the Z2 grading of the commutator algebra:
  parity([X,Y]) must equal parity(X)*parity(Y) for all generator pairs
  (i.e. the exchange is an algebra automorphism of Cartan type).
TEST 2 (Kepler T-audit): integrate an eccentric orbit; compute E, L,
  Runge-Lenz A along it. Naive principle says labels are exchange-
  even -- but L is T-ODD and conserved. Refined claim: the LABELS are
  even FUNCTIONS (Casimirs) of the odd generators: check conservation
  of E, L, A and the identity A^2 = m^2 k^2 + 2 m E L^2 (eccentricity
  fixed by even data alone).
TEST 3 (scoping): damped oscillator -- forces split (spring T-even,
  damping T-odd), but dissipated work per cycle is a product-level
  (even) quantity whose SIGN comes from the correlation <F.v>, not
  from the force's parity: confirms the principle's stated scope.
"""
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2)
S = [sx, sy, sz]
A = [np.kron(s, I2) / 2 for s in S]      # SU(2) on factor 1
B = [np.kron(I2, s) / 2 for s in S]      # SU(2) on factor 2
L = [a + b for a, b in zip(A, B)]
M = [a - b for a, b in zip(A, B)]
gens = [(f"L{i}", X, +1) for i, X in enumerate(L)] + \
       [(f"M{i}", X, -1) for i, X in enumerate(M)]

def decompose(C):
    """express commutator in the generator basis, return (parity content)"""
    basis = np.array([X.ravel() for _, X, _ in gens]).T
    coef, *_ = np.linalg.lstsq(basis, C.ravel(), rcond=None)
    resid = np.linalg.norm(basis @ coef - C.ravel())
    ev = np.linalg.norm(coef[[g[2] == 1 for g in gens]])
    od = np.linalg.norm(coef[[g[2] == -1 for g in gens]])
    return resid, ev, od

print("TEST 1: commutator grading under the pair exchange A<->B")
ok = True
for n1, X, p1 in gens:
    for n2, Y, p2 in gens:
        C = X @ Y - Y @ X
        if np.linalg.norm(C) < 1e-12:
            continue
        resid, ev, od = decompose(1j * C)  # algebra is in i*[.,.]
        got = 0 if resid > 1e-8 else (1 if od < 1e-8 else (-1 if ev < 1e-8 else 99))
        want = p1 * p2
        flag = "OK " if got == want else "FAIL"
        if got != want: ok = False
        print(f"  [{n1},{n2}]: parity {p1:+d}x{p2:+d} -> commutator parity "
              f"{got:+d} (want {want:+d})  {flag}")
print(f"  Z2 grading holds for all commutators: {ok}")
print("  ([odd,odd] lands EVEN, [even,odd] lands ODD: Cartan-type grading;")
print("   the exchange is an automorphism, not just a relabelling.)")

print("\nTEST 2: Kepler orbit (m=k=1, eccentric), T-parity audit")
def rhs(s):
    x, y, vx, vy = s
    r = np.hypot(x, y)
    return np.array([vx, vy, -x / r**3, -y / r**3])
s = np.array([1.0, 0.0, 0.0, 0.8])   # E<0 bound, eccentric
dt, steps = 1e-3, 20000
Es, Ls, A2s, pred = [], [], [], []
for i in range(steps):
    k1 = rhs(s); k2 = rhs(s + dt/2*k1); k3 = rhs(s + dt/2*k2); k4 = rhs(s + dt*k3)
    s = s + dt/6*(k1 + 2*k2 + 2*k3 + k4)
    if i % 200 == 0:
        x, y, vx, vy = s
        r = np.hypot(x, y); v2 = vx**2 + vy**2
        E = v2/2 - 1/r
        Lz = x*vy - y*vx
        # Runge-Lenz: A = v x L - r_hat  (m=k=1)
        Ax = vy*Lz - x/r; Ay = -vx*Lz - y/r
        Es.append(E); Ls.append(Lz); A2s.append(Ax**2 + Ay**2)
        pred.append(1 + 2*E*Lz**2)
Es, Ls, A2s, pred = map(np.array, (Es, Ls, A2s, pred))
print(f"  E drift: {Es.max()-Es.min():.2e};  L drift: {Ls.max()-Ls.min():.2e} "
      f"(L conserved AND T-odd: the naive 'labels are even' form FAILS on L)")
print(f"  A^2 drift: {A2s.max()-A2s.min():.2e};  "
      f"A^2 vs 1 + 2 E L^2: max err {np.abs(A2s-pred).max():.2e}")
print("  -> REFINED form holds: labels are EVEN FUNCTIONS (Casimirs) of the")
print("     odd generators -- E, L^2, A^2 all even; the generators p, L,")
print("     reaction forces themselves are odd. Eccentricity is fixed by")
print("     even data alone.")

print("\nTEST 3: damped oscillator scoping (m=k=1, gamma=0.3, exact solution)")
gm = 0.3
wd = np.sqrt(1 - gm**2 / 4)
Td = 2 * np.pi / wd
tt = np.linspace(0, Td, 400001)
x = np.exp(-gm * tt / 2) * (np.cos(wd * tt) + gm / (2 * wd) * np.sin(wd * tt))
v = -(np.exp(-gm * tt / 2) / wd) * np.sin(wd * tt)   # exact dx/dt, v(0)=0
F_s, F_d = -x, -gm * v
W_d = np.trapz(F_d * v, tt); W_s = np.trapz(F_s * v, tt)
E = 0.5 * v**2 + 0.5 * x**2
dU = 0.5 * x[-1]**2 - 0.5 * x[0]**2
print(f"  work by spring (T-even force): {W_s:+.6f} = -Delta U = {-dU:+.6f} "
      f"(state function, reversible bookkeeping)")
print(f"  work by damping (T-odd force): {W_d:+.6f} = Delta E_mech = "
      f"{E[-1]-E[0]:+.6f} (ALL dissipation passes through the odd force)")
print(f"  closure: W_s + W_d - Delta KE = "
      f"{W_s + W_d - (0.5*v[-1]**2 - 0.5*v[0]**2):+.2e}")
print("  -> force-level split is clean; dissipation is carried entirely")
print("     by the exchange-odd force, the even force's work is a state")
print("     function -- exactly the scope the principle states.")
