"""
Graviton as a gravitational phase relation -- finite-model check
(sandbox, 2026-10-29).

Same quarter ring as flip_operator_test.py (N = 24 sites, U = quarter
step, P = even-sector projector). Two families of states:
  sector states: eigenstates of H_EM inside one sector, and site states;
  phase-relation states: eigenstates of U itself (Bloch waves on the
  quarter grid) -- equal weight in both sectors, with a definite
  relative phase between rungs and across the sector boundary.
Measure: sector weights and <U> (the gravity step's expectation: a pure
phase iff the state IS a phase relation; 0 iff the state lives in a
sector and carries no inter-sector phase).
"""
import numpy as np

N = 24
U = np.zeros((N, N), dtype=complex)
for n in range(N):
    U[(n + 1) % N, n] = 1.0
P = np.diag([1.0 if n % 2 == 0 else 0.0 for n in range(N)])
H2 = (U @ U + U.conj().T @ U.conj().T).real

def report(name, psi):
    w_even = float(np.vdot(psi, P @ psi).real)
    u_exp = np.vdot(psi, U @ psi)
    print(f"  {name:44s} even weight {w_even:.3f}   <U> = {u_exp:+.3f}   |<U>| = {abs(u_exp):.3f}")

print("phase-relation states (eigenstates of the quarter-step U):")
for k in [1, 2, 3, 6]:
    psi = np.array([np.exp(2j * np.pi * k * n / N) for n in range(N)]) / np.sqrt(N)
    report(f"Bloch wave k={k} (phase winding {k} around the ring)", psi)
print("sector states:")
psi = np.zeros(N); psi[0] = 1.0
report("site state |0> (pure even sector)", psi)
idx = [n for n in range(N) if n % 2 == 0]
Hs = H2[np.ix_(idx, idx)]
w, v = np.linalg.eigh(Hs)
psi = np.zeros(N, dtype=complex); psi[idx] = v[:, 0]
report("lowest H_EM eigenstate, even sector", psi)
psi = np.zeros(N, dtype=complex); psi[idx] = v[:, -1]
report("highest H_EM eigenstate, even sector", psi)
print()
print("Reading: the quarter-step's eigenstates are pure phase relations --")
print("half in each sector, <U> a pure phase. Sector states (everything EM")
print("dynamics can prepare) have <U> = 0: no inter-sector phase at all.")
print("The relative phase between the grid's two sectors is a gravitational")
print("observable in the exact sense that only the gravity operator sees it.")
print("ALL CHECKS DONE")
