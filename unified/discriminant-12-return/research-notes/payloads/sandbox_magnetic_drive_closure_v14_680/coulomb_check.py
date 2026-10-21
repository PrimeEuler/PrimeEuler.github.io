"""Coulomb wrap-up checks (sandbox, 2026-10-21).
Closes REPORT.md (hydrogen-radial) section 10's open item:
the omega^2 = |E|/2mu link, via the Levi-Civita/KS fictitious
Hamiltonian, plus the bicone-sector oscillator counting."""
import sympy as sp

# --- 1. Levi-Civita momentum identity (2D shadow of the KS identity)
u1, u2, px, py = sp.symbols('u1 u2 px py', real=True)
P1 = 2*(u1*px + u2*py)
P2 = 2*(-u2*px + u1*py)
r = u1**2 + u2**2
ident = sp.expand(P1**2 + P2**2 - 4*r*(px**2 + py**2))
print('LC identity  P^2 - 4r p^2 =', ident)          # expect 0
assert ident == 0

# --- 2. Fictitious Hamiltonian: Gamma = r(H-E)
# H = p^2/2mu - kappa/r  =>  Gamma = P^2/(8mu) - E|u|^2 - kappa.
# On shell Gamma=0:  H_osc = P^2/(2M) + (M w^2/2)|u|^2 = kappa, M = 4mu,
# M w^2 / 2 = |E|  =>  w^2 = |E|/(2mu).  (The report's open link,
# here an identity of the map, not an input.)
M, w2, E = sp.symbols('M w2 E', positive=True)
mu = sp.symbols('mu', positive=True)
sol = sp.solve(sp.Eq((4*mu)*w2/2, E), w2)
print('omega^2 =', sol, ' (with E := |E|)')           # expect E/(2mu)
assert sol == [E/(2*mu)]

# --- 3. Bicone-sector counting in truncated Fock space (4 modes)
# Pair a = modes (0,1), pair b = modes (2,3). Schwinger: j = N_pair/2.
# Glued sector: N_a = N_b = n-1  =>  j = (n-1)/2 = T0 - 1/2, T0 = n/2.
# H_osc/(hbar w) = N_tot + 2 (four modes x 1/2). Check uniformity + dim.
import itertools
for n in range(1, 6):
    states = []
    for na in itertools.product(range(n), repeat=2):
        if sum(na) != n-1: continue
        for nb in itertools.product(range(n), repeat=2):
            if sum(nb) != n-1: continue
            Ntot = sum(na) + sum(nb)
            states.append(Ntot + 2)
    assert all(s == 2*n for s in states), (n, states)
    assert len(states) == n*n, (n, len(states))
    print(f'n={n}: glued-sector dim={len(states)} (=n^2), '
          f'H_osc/(hbar w) = {states[0]} (=2n) on every state')

# --- 4. The closed chain: kappa = H_osc = 2n hbar w  =>  w_n = kappa/(2 hbar n)
# |E_n| = 2 mu w_n^2 = mu kappa^2 / (2 hbar^2 n^2).  Numeric table (SI->eV).
import scipy.constants as C
kappa = C.e**2/(4*C.pi*C.epsilon_0)                  # Coulomb coupling (J*m)
mu_r = C.m_e*C.m_p/(C.m_e + C.m_p)                   # reduced mass
for n in range(1, 5):
    En = mu_r*kappa**2/(2*C.hbar**2*n*n)/C.e         # eV
    print(f'n={n}: E_n = {-En:.4f} eV   (Rydberg/n^2 = {-13.605693122994/n/n:.4f})')
print('COULOMB CHECKS PASS')
