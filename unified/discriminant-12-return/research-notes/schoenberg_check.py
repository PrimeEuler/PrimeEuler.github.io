import numpy as np

# 1) Conditional negative definiteness of q(Y)=Y^2: check S = -2|sum c_j Y_j|^2 for random c (sum c_j=0), Y
rng = np.random.default_rng(0)
for trial in range(5):
    N = 6
    Y = rng.uniform(-5,5,N)
    c = rng.normal(size=N) + 1j*rng.normal(size=N)
    c[-1] = -np.sum(c[:-1])  # enforce sum c_j = 0
    S = 0j
    for j in range(N):
        for k in range(N):
            S += np.conj(c[j])*c[k]*(Y[j]-Y[k])**2
    pred = -2*abs(np.sum(c*Y))**2
    print(f"trial {trial}: S={S:.6f}  predicted(-2|sum c_j Y_j|^2)={pred:.6f}  match={np.allclose(S,pred)}  S<=0? {S.real<=1e-9}")

print()
# 2) Schoenberg conclusion: e^{-t(Y_j-Y_k)^2} should be positive semidefinite as a matrix, any finite point set, any t>0
for t in [0.3, 1.0, 3.0]:
    Y = rng.uniform(-5,5,8)
    M = np.exp(-t*(Y[:,None]-Y[None,:])**2)
    eigs = np.linalg.eigvalsh(M)
    print(f"t={t}: min eig of [e^-t(Yj-Yk)^2] = {eigs.min():.3e}  (should be >= -eps)")

print()
# 3) Generator check: A e_m = -m^2 e_m vs (1/4pi^2) d^2/dtheta^2 e_m
import sympy as sp
theta, m = sp.symbols('theta m', real=True)
em = sp.exp(2*sp.pi*sp.I*m*theta)
d2 = sp.diff(em, theta, 2)
ratio = sp.simplify(d2/em)
print("d^2/dtheta^2 e_m / e_m =", ratio, " => coefficient on (1/(4pi^2)) gives:", sp.simplify(ratio/(4*sp.pi**2)))
