"""
Angular-sector unification test (gravity lane's proposed next test, 2026-10-22):

Can ONE worldline angular structure reproduce BOTH the electromagnetic
Dirac-monopole sector and the gravitational Taub-NUT sector?

Candidate single object, parameterised by one real number s (the Poincare
strength of the sector): with canonical (th, ph, pth, pph) and the twisted
covariant momentum

    Pi_ph = pph + s cos(th)          (physical component Pi_ph / sin(th)),

    J = pth * ph_hat  -  (Pi_ph / sin th) * th_hat  -  s * n_hat ,

i.e. mechanical angular momentum minus s along the radial direction.
This is the Noether charge vector of the first-order worldline action whose
angular Hamiltonian is A_s (below); s is its Wess-Zumino / minimal-coupling
coefficient.

Checks:
 1. J . n_hat = -s                         (exact, symbolic)
 2. J^2 = pth^2 + (pph + s cos th)^2/sin^2 th + s^2 =: A_s   (exact, symbolic)
    -- A_s is the angular HJ function of BOTH sectors:
       EM : MIC/monopole HJ with s = eg   (A_phi = -g cos th gauge)
       TN : Taub-NUT HJ  with s = 2 eps l (tn_sector.py, exact identity)
 3. Poisson brackets {J_i, J_j} close on the SU(2) algebra with ONE sign
    convention at every random phase-space point (symbolic derivatives,
    numeric evaluation), and {J_i, A_s} = 0.
 4. TN cross-check: the candidate J(s = 2 eps l) equals the Killing-triad
    charges Q_x, Q_y, Q_z of charges.py at random points (f(r) arbitrary
    numeric value -- the triad charges are f-independent in form).
 5. Seats: parabolic seat squares ((k -/+ s)/2)^2 specialise to MIC seats
    (s = eg) and TN seats k/2 +/- eps*l (s = 2 eps l) -- algebra asserts.
"""
import random
import sympy as sp

th, ph, pth, pph, s = sp.symbols('th ph pth pph s')
sin, cos = sp.sin, sp.cos

n_hat = sp.Matrix([sin(th) * cos(ph), sin(th) * sin(ph), cos(th)])
th_hat = sp.Matrix([cos(th) * cos(ph), cos(th) * sin(ph), -sin(th)])
ph_hat = sp.Matrix([-sin(ph), cos(ph), 0])

Pi = pph + s * cos(th)                      # covariant twisted momentum
J = pth * ph_hat - (Pi / sin(th)) * th_hat - s * n_hat
J = [sp.expand(x) for x in J]

print("1) J . n =", sp.simplify(J[0] * n_hat[0] + J[1] * n_hat[1] + J[2] * n_hat[2]))

A_s = pth**2 + Pi**2 / sin(th)**2 + s**2
J2 = sp.simplify(sum(x**2 for x in J))
print("2) J^2 - A_s =", sp.simplify(sp.together(J2 - A_s)))
print("   J_z =", sp.simplify(J[2]), " (azimuthal charge = pph, as in both sectors)")

# ---- 3) Poisson brackets: symbolic derivatives, numeric evaluation ----
qs = [th, ph]
ps = [pth, pph]
dJ = {(i, v): sp.diff(J[i], v) for i in range(3) for v in qs + ps}

def PB(F, G):
    return sum(sp.diff(F, q) * sp.diff(G, p) - sp.diff(F, p) * sp.diff(G, q)
               for q, p in zip(qs, ps))

brackets = {(i, j): PB(J[i], J[j]) for i in range(3) for j in range(3) if i < j}
bracketA = [PB(J[i], A_s) for i in range(3)]
f_br = {k: sp.lambdify((th, ph, pth, pph, s), v, 'math') for k, v in brackets.items()}
f_J = [sp.lambdify((th, ph, pth, pph, s), x, 'math') for x in J]
f_bA = [sp.lambdify((th, ph, pth, pph, s), v, 'math') for v in bracketA]

random.seed(20261022)
def eps3(i, j, k):
    return {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
            (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}[(i, j, k)]

sign_votes = {+1: 0, -1: 0}
worst_br, worst_A = 0.0, 0.0
for _ in range(300):
    pt = (random.uniform(0.25, 2.85), random.uniform(0, 6.28),
          random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-1.5, 1.5))
    Jv = [f(*pt) for f in f_J]
    for (i, j), f in f_br.items():
        k = 3 - i - j
        val = f(*pt)
        target = eps3(i, j, k) * Jv[k]      # {Ji,Jj} =? +eps_ijk Jk
        if abs(val - target) < 1e-8 * max(1.0, abs(target)):
            sign_votes[+1] += 1
        elif abs(val + target) < 1e-8 * max(1.0, abs(target)):
            sign_votes[-1] += 1
        worst_br = max(worst_br, abs(val - target))
    for f in f_bA:
        worst_A = max(worst_A, abs(f(*pt)))
print("3) bracket sign votes (+J_k / -J_k):", sign_votes,
      "| worst |{Ji,Jj} -/+ Jk| =", worst_br, "| worst |{Ji, A_s}| =", worst_A)

# ---- 4) TN cross-check vs Killing-triad charges (numeric, arbitrary f) ----
import math
def Q_killing(r_, l_, f_, th_, ph_, td, rd, thd, phd):
    Sig = r_**2 + l_**2
    g = {(0, 0): -f_, (0, 3): -2 * l_ * f_ * math.cos(th_), (3, 0): -2 * l_ * f_ * math.cos(th_),
         (3, 3): -4 * l_**2 * f_ * math.cos(th_)**2 + Sig * math.sin(th_)**2,
         (1, 1): 1 / f_, (2, 2): Sig}
    u = [td, rd, thd, phd]
    p = [sum(g.get((mu, nu), 0.0) * u[nu] for nu in range(4)) for mu in range(4)]
    xi = {'x': [2 * l_ * math.cos(ph_) / math.sin(th_), 0, -math.sin(ph_),
                -math.cos(ph_) * math.cos(th_) / math.sin(th_)],
          'y': [2 * l_ * math.sin(ph_) / math.sin(th_), 0, math.cos(ph_),
                -math.sin(ph_) * math.cos(th_) / math.sin(th_)],
          'z': [0, 0, 0, 1]}
    return {k: sum(xi[k][mu] * p[mu] for mu in range(4)) for k in xi}, p

def J_cand(th_, ph_, pth_, pph_, s_):
    Pi_ = pph_ + s_ * math.cos(th_)
    return [pth_ * (-math.sin(ph_)) - (Pi_ / math.sin(th_)) * math.cos(th_) * math.cos(ph_)
            - s_ * math.sin(th_) * math.cos(ph_),
            pth_ * (math.cos(ph_)) - (Pi_ / math.sin(th_)) * math.cos(th_) * math.sin(ph_)
            - s_ * math.sin(th_) * math.sin(ph_),
            pph_]

worst_Q = 0.0
for _ in range(300):
    r_ = random.uniform(2.0, 6.0); l_ = random.uniform(0.2, 1.2); f_ = random.uniform(0.3, 0.95)
    th_ = random.uniform(0.25, 2.85); ph_ = random.uniform(0, 6.28)
    td, rd, thd, phd = (random.uniform(-2, 2) for _ in range(4))
    Q, p = Q_killing(r_, l_, f_, th_, ph_, td, rd, thd, phd)
    eps_ = -p[0]
    Jv = J_cand(th_, ph_, (r_**2 + l_**2) * thd, p[3], 2 * eps_ * l_)
    for i, k in enumerate(['x', 'y', 'z']):
        worst_Q = max(worst_Q, abs(Jv[i] - Q[k]))
print("4) worst |J_candidate(s=2 eps l) - Q_Killing| over 300 pts:", worst_Q)

# ---- 5) seats specialisation (algebra) ----
k, eg, eps_, l_ = sp.symbols('k eg eps l')
seat = lambda s_: [((k - s_) / 2)**2, ((k + s_) / 2)**2]
print("5) MIC seats (s=eg)   :", [sp.expand(x) for x in seat(eg)])
print("   TN  seats (s=2el)  :", [sp.expand(x) for x in seat(2 * eps_ * l_)],
      " -> root separation:", sp.simplify(sp.sqrt(seat(2 * eps_ * l_)[1])
                                           - sp.sqrt(seat(2 * eps_ * l_)[0])))
print("\nALL CHECKS DONE")
