"""Sandbox exploration: where does discreteness live on the two-factor carrier?
Carrier B (Schwinger Fock): pair SU(1,1) {K0, K+, K-} vs the direct-sum squeeze
generator p_s = D_u - D_v, D = (i/2)(a^dag^2 - a^2) per mode. Exact rational/sqrt
matrix arithmetic in a truncated Fock space (cutoff 7 per mode); bracket checks
are restricted to states away from the cutoff edge."""
import sympy as sp

N = 7  # states 0..6 per mode
a = sp.zeros(N)
for n in range(1, N):
    a[n - 1, n] = sp.sqrt(n)
ad = a.T
num = ad * a
I1 = sp.eye(N)
def T(x, y): return sp.kronecker_product(x, y)
Nu, Nv = T(num, I1), T(I1, num)
K0 = (Nu + Nv + sp.eye(N * N)) / 2
Kp = T(ad, ad); Km = T(a, a)
D1 = (ad * ad - a * a) * sp.I / 2
ps = T(D1, I1) - T(I1, D1)
d_op = Nu - Nv

def idx(nu, nv): return nu * N + nv
def comm_norm_on_states(A, B, states):
    C = A * B - B * A
    return max(abs(C[idx(*s), idx(*t)]) for s in states for t in states)

interior = [(i, j) for i in range(4) for j in range(4)]
print("[K0,K+] - K+  max|.| on interior:", comm_norm_on_states(K0, Kp, interior) -
      max(abs(Kp[idx(*s), idx(*t)]) for s in interior for t in interior) * 0 -
      0)  # placeholder replaced below
def check(expr, label):
    print(label, "max|.| =", max(abs(expr[idx(*s), idx(*t)]) for s in interior for t in interior))
check(K0 * Kp - Kp * K0 - Kp, "[K0,Kp]-Kp      :")
check(K0 * Km - Km * K0 + Km, "[K0,Km]+Km      :")
check(Km * Kp - Kp * Km - 2 * K0, "[Km,Kp]-2K0     :")
Cas = K0 * K0 - (Kp * Km + Km * Kp) / 2
print("pair SU(1,1) Casimir on |n, n+d> (expect (d^2-1)/4):")
for d in range(4):
    vals = set()
    for n in range(0, 4):
        vals.add(sp.simplify(Cas[idx(n, n + d), idx(n, n + d)]))
    print(f"  d={d}: {vals}   expected {sp.Rational(d * d - 1, 4)}")
print("K0 eigenvalue on |n, n+d> (expect n + (d+1)/2):",
      [sp.simplify(K0[idx(n, n + 1), idx(n, n + 1)]) for n in range(3)])
print("Km |n, n+d> lowers BOTH occupations (pair annihilation, d preserved):")
for (n, d) in [(2, 1), (3, 0)]:
    col = Km[:, idx(n, n + d)]
    nz = [( (i // N, i % N), col[i]) for i in range(N * N) if col[i] != 0]
    print(f"  |{n},{n+d}> ->", nz, " expect coeff sqrt(n(n+d)) =", sp.sqrt(n * (n + d)))
print("p_s = D_u - D_v selection rules (nonzero transitions from basis states):")
for s in [(2, 2), (3, 1), (0, 0)]:
    col = ps[:, idx(*s)]
    nz = [((i // N, i % N), sp.simplify(col[i])) for i in range(N * N) if col[i] != 0]
    print(f"  from {s}: ->", nz)
check(ps * d_op - d_op * ps, "[p_s, Nu-Nv]    : (nonzero => sector label NOT preserved by squeeze flow)")
check(ps * K0 - K0 * ps, "[p_s, K0]       : (nonzero => pair number not preserved either)")
# parity: p_s changes each occupation by +-2 only -> n_u + n_v mod 2 and d mod 2 preserved
par = (Nu + Nv) % 2 if False else None
bad = 0
for s in interior:
    col = ps[:, idx(*s)]
    for i in range(N * N):
        if col[i] != 0:
            t = (i // N, i % N)
            if (t[0] + t[1] - s[0] - s[1]) % 2 != 0: bad += 1
print("transitions violating (nu+nv) mod 2 conservation:", bad)
