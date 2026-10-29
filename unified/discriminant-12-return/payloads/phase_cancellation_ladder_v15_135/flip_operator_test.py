"""
Flip test, operator level (sandbox, 2026-10-29).

Finite model of the gravity ladder: N = 4M sites on a ring, site n sits at
rung n/4. U = quarter-step ladder operator. The EM ladder is U^2 (half
steps). chi = (-1)^n is the parity (phase-offset) grading; P = (1+chi)/2.

Checks:
 1. [chi, H_EM] = 0 with H_EM = U^2 + U^-2  -> EM dynamics preserves the
    phase-offset sectors; {chi, U} = 0 -> the gravity step flips sector.
 2. U^2 has exactly two orbits (evens, odds), each an EM ring of N/2 sites;
    their H_EM spectra are identical and equal the half-lattice ring's.
 3. The odd copy is the EM lattice translated by 1/4 rung = half an EM
    period = a pi phase offset in EM's own phase variable.
 4. A chi-potential (the term a phase-locking dynamics would have to
    supply) splits the sector energies by 2*lambda and nothing else.
"""
import numpy as np

M = 6
N = 4 * M
tol = 1e-10

U = np.zeros((N, N))
for n in range(N):
    U[(n + 1) % N, n] = 1.0
Ud = U.T
chi = np.diag([1.0 if n % 2 == 0 else -1.0 for n in range(N)])
P = (np.eye(N) + chi) / 2
H1 = U + Ud                      # gravity hopping (quarter steps)
H2 = U @ U + Ud @ Ud             # EM hopping (half steps)

def nrm(A):
    return np.linalg.norm(A)

print("1) grading algebra")
print("   ||[chi, H_EM]||      =", nrm(chi @ H2 - H2 @ chi), " (EM preserves sectors)")
print("   ||{chi, U}||         =", nrm(chi @ U + U @ chi), " (gravity step flips sector)")
print("   ||[chi, H_grav]||    =", round(nrm(chi @ H1 - H1 @ chi), 6), " (nonzero: gravity mixes)")
print("   ||P U P||            =", nrm(P @ U @ P), " (no gravity step stays inside EM sector)")
print("   rank P               =", int(round(np.trace(P))), "of", N)

print("2) U^2 orbits")
def cycles(step):
    seen, out = set(), []
    for start in range(N):
        if start in seen:
            continue
        cyc, x = [], start
        while x not in seen:
            seen.add(x); cyc.append(x); x = (x + step) % N
        out.append(cyc)
    return out
orbits = cycles(2)
print("   number of U^2 orbits:", len(orbits), " lengths:", [len(o) for o in orbits])
print("   orbit parities:", [o[0] % 2 for o in orbits])

print("3) sector spectra vs half-lattice ring")
def sector_H(H, parity):
    idx = [n for n in range(N) if n % 2 == parity]
    return H[np.ix_(idx, idx)], idx
L = N // 2
A = np.zeros((L, L))
for i in range(L):
    A[(i + 1) % L, i] = 1.0
Hring = A + A.T
w_ring = np.linalg.eigvalsh(Hring)
for parity, name in [(0, 'even'), (1, 'odd ')]:
    Hs, idx = sector_H(H2, parity)
    w = np.linalg.eigvalsh(Hs)
    print(f"   {name} sector: max |eig - half-ring eig| = {np.max(np.abs(np.sort(w) - np.sort(w_ring))):.2e}",
          " positions:", [f"{n}/4" for n in idx[:4]], "...")
w_full = np.linalg.eigvalsh(H2)
print("   full H_EM spectrum = two identical copies:",
      np.allclose(np.sort(w_full), np.sort(np.concatenate([w_ring, w_ring])), atol=tol))

print("4) chi-potential (phase-lock term) at lambda = 0.3")
lam = 0.3
Hl = H2 - lam * chi
for parity, name in [(0, 'even'), (1, 'odd ')]:
    Hs, _ = sector_H(Hl, parity)
    H0, _ = sector_H(H2, parity)
    shift = np.linalg.eigvalsh(Hs) - np.linalg.eigvalsh(H0)
    print(f"   {name} sector energy shift: min {shift.min():+.6f}  max {shift.max():+.6f}")
print("   -> a chi term rigidly splits the two EM copies by 2*lambda;")
print("      it is exactly the lock a 'phase offset creates EM' dynamics must generate.")
print("ALL CHECKS DONE")
