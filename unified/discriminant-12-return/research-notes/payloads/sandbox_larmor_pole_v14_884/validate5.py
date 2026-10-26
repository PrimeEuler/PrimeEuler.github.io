import numpy as np, mpmath as mp, time
from kernel5 import Kernel5

def F(z):
    return 1+1j*np.sqrt(np.pi)*z*np.exp(-z*z)*complex(mp.erfc(-1j*z))

t0=time.time(); K = Kernel5(1.0); print(f"build {time.time()-t0:.1f}s, N={K.N}, nrad={len(K.p)}")
print("== alpha=0 vs F, incl. previous problem points ==")
for z in (0.3-0.1j, 0.4108337143730426-0.1700926343728676j, 1.2-0.4j, -0.7-0.05j,
          0.3+0.1j, 0.4108337143730426+0.1700926343728676j, 0.8+0.02j, 0.05-0.02j):
    got = K.Dhat(z, 0.0); want = -0.25 + z*z*F(z)
    print(f"z={z}: diff={abs(got-want):.2e}  got={got:.12f}")
print("== quasistatic anchor ==")
for beta in (1.0, 2.0):
    Kb = Kernel5(beta)
    for alpha in (0.02, 0.05):
        got = Kb.Dhat(0.0, alpha) + 0.25
        print(f"beta={beta} alpha={alpha}: got={got.real:.8f} pred={(alpha*beta)**2/5:.8f} ratio={got.real/((alpha*beta)**2/5):.6f}")
    del Kb
print("== grid convergence at finite alpha (beta=1, alpha=0.2, z near expected pole) ==")
z = 0.40-0.17j
print(" base      :", K.Dhat(z, 0.2))
Kf = Kernel5(1.0, nmu=56, nphi=104, nper=30)
print(" fine grid :", Kf.Dhat(z, 0.2))
Kh = Kernel5(1.0, nmu=28, nphi=48, nper=14)
print(" coarse    :", Kh.Dhat(z, 0.2))
print("== N convergence (beta=2, alpha=0.2) ==")
for N in (14, 22, 30):
    Kn = Kernel5(2.0, N=N)
    print(f" N={N}:", Kn.Dhat(z, 0.2))
    del Kn
