# Verbatim reproducer from research-notes/Maxwell_Seat_Retarded_Complex_Pole_Reproducer.md (v14.874)
import mpmath as mp
mp.mp.dps=30
def F(z):
    return 1+1j*mp.sqrt(mp.pi)*z*mp.exp(-z*z)*mp.erfc(-1j*z)
def D(z): return mp.mpf('0.25')-z*z*F(z)
for seed in [0.4-0.17j,-0.4-0.17j]:
    root=mp.findroot(D,(seed,seed+0.01),tol=mp.mpf('1e-25'))
    print(root,abs(D(root)))
print("claimed: +/-0.4108337143730426-0.1700926343728676i")
