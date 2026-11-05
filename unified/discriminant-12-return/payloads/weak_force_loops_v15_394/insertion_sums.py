"""
Loop program, step 4 (2026-11-04 evening, sandbox): insertions.
Determinants (steps 1-3) are functions of eigenvalues alone.
Amplitudes are not: they are traces with insertions,
Tr[R V], Tr[(R V)^2], ... -- matrix elements joined by resolvents.
Same model class as steps 2-3 (D diagonal log(n/4); B Hilbert-like
0.3/(m+n-1)); z = -3.5.

 (a) The insertion trace Tr[R_K(z) V] for a rank-1 vertex
     V = |v><v|, v_n = 2^{-n/2} (decaying): computed directly and
     as an eigen-sum sum_j <psi_j|V|psi_j>/(mu_j - z); agreement
     and convergence in the section size.
 (b) Eigenvalues insufficient, demonstrated: K' = U K U^T with U
     a rotation in the (3,5) mode plane has IDENTICAL eigenvalues
     (hence identical xi, identical every determinant) but a
     DIFFERENT insertion trace. No spectral-shift-only formula
     can produce an amplitude.
 (c) The GIM template as an insertion sum over the generation
     direction: replicas g (the frame's c -> c+3g states, sharing
     (n2, tau, Y mod 2)), CKM-like weights lambda_g with
     sum lambda_g = 0 (completeness over the generation
     direction, imported), loop function the Inami-Lim Y(x).
     Checks: degenerate masses -> A = 0 exactly; mass-difference
     form exact; top dominance a mass fact.
"""
import numpy as np

Z = -3.5

def build(N):
    n = np.arange(1, N + 1)
    d = np.log(n / 4.0)
    B = 0.3 / (n[:, None] + n[None, :] - 1)
    return d, np.diag(d) + B

print("=" * 76)
print("(a) insertion trace Tr[R_K V], rank-1 vertex, direct vs eigen-sum")
print("=" * 76)
for N in [100, 200, 400]:
    d, K = build(N)
    v = 2.0 ** (-np.arange(1, N + 1) / 2.0)
    V = np.outer(v, v)
    R = np.linalg.inv(K - Z * np.eye(N))
    direct = np.trace(R @ V)
    mu, psi = np.linalg.eigh(K)
    me = (psi.T @ v) ** 2                      # <psi_j|V|psi_j> = |<psi_j|v>|^2
    eigensum = np.sum(me / (mu - Z))
    ref = np.sum(v ** 2 / (d - Z))             # Tr[R_D V], closed form
    print(f"  N={N:>4}: direct = {direct:+.10f}, eigen-sum = {eigensum:+.10f}, "
          f"agree {abs(direct - eigensum) < 1e-9};  Tr[R_D V] = {ref:+.10f}")

print()
print("=" * 76)
print("(b) isospectral twist: same eigenvalues, different insertion trace")
print("=" * 76)
N = 200
d, K = build(N)
v = 2.0 ** (-np.arange(1, N + 1) / 2.0)
V = np.outer(v, v)
theta = 0.7
U = np.eye(N)
c, s = np.cos(theta), np.sin(theta)
i, j = 2, 4                                     # modes n=3 and n=5 (0-based 2,4)
U[i, i], U[i, j], U[j, i], U[j, j] = c, -s, s, c
Kp = U @ K @ U.T
mu = np.linalg.eigvalsh(K); mup = np.linalg.eigvalsh(Kp)
tK = np.trace(np.linalg.inv(K - Z * np.eye(N)) @ V)
tKp = np.trace(np.linalg.inv(Kp - Z * np.eye(N)) @ V)
print(f"  max eigenvalue difference K vs K' : {np.max(np.abs(mu - mup)):.2e}")
print(f"  Tr[R_K  V] = {tK:+.10f}")
print(f"  Tr[R_K' V] = {tKp:+.10f}   (difference {abs(tK - tKp):.4f}, plainly nonzero)")
print("  -> xi and every determinant coincide; the amplitude does not.")
print("     Insertions see eigenvectors. This is the survey's point,")
print("     demonstrated on our own spectrum class.")

print()
print("=" * 76)
print("(c) GIM template: insertion sum over the generation direction")
print("=" * 76)
def Y_IL(x):                                    # Inami-Lim Y(x), standard form
    return x / 8.0 * ((x - 6) / (x - 1) + (3 * x + 2) / (x - 1) ** 2 * np.log(x))
MW = 80.379
masses = np.array([0.0022, 1.27, 172.7])        # u, c, t (GeV, imported values)
x = (masses / MW) ** 2
# CKM-like weights for B_d mixing: lambda_i = V_ib V_id*; unitarity sum = 0.
lam = np.array([0.009664 - 0.000779j, -0.009000 + 0.000000j, -0.000664 + 0.000779j])
print(f"  completeness: sum lambda_i = {np.sum(lam):+.2e}  (0 = unitarity, imported)")
A = np.sum(lam * Y_IL(x))
A_diff = lam[1] * (Y_IL(x[1]) - Y_IL(x[0])) + lam[2] * (Y_IL(x[2]) - Y_IL(x[0]))
print(f"  A = sum lambda_i Y(x_i)          = {A:+.6e}")
print(f"  mass-difference form             = {A_diff:+.6e}   (identical: {np.allclose(A, A_diff)})")
A_deg = np.sum(lam * Y_IL(np.array([x[0], x[0], x[0]])))
print(f"  degenerate masses -> A           = {A_deg:+.2e}   (GIM cancellation exact)")
frac = np.abs(lam * Y_IL(x)) / np.abs(A)
print(f"  |term| shares u/c/t: {frac[0]:.2e} / {frac[1]:.2e} / {frac[2]:.3f}"
      "  (top dominance = a mass fact)")
print("  Frame reading: the sum runs over the c -> c+3g replicas at fixed")
print("  (n2, tau, Y mod 2); cancellation is completeness over that")
print("  direction. Weights and masses remain imported (generation door).")
