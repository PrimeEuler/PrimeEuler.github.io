"""External audit (Round 146) independent numerical check of v13.952's
L(s,chi_12) claims.

chi_12 is the primitive mod-12 Kronecker character (12/.): +1 for n=1,11
(mod 12), -1 for n=5,7 (mod 12), 0 otherwise (even character).

L(s,chi_12) = 12^(-s) * [zeta(s,1/12) - zeta(s,5/12) - zeta(s,7/12) + zeta(s,11/12)]
via the Hurwitz zeta decomposition of the Dirichlet L-function.

Checks:
  1. L(2,chi_12) =? 0.9497031...
  2. The 8 claimed critical-line zero ordinates refine to genuine roots of
     Re(L(1/2+it,chi_12)) via Newton/secant refinement, with |L| tiny there.

Fresh implementation, not reusing anything from the ledger entry or any
unposted sandbox script.
"""
from mpmath import mp, mpf, mpc, zeta
from scipy.optimize import minimize_scalar

mp.dps = 30


def L_chi12(s):
    s = mpc(s)
    return mpf(12) ** (-s) * (
        zeta(s, mpf(1) / 12)
        - zeta(s, mpf(5) / 12)
        - zeta(s, mpf(7) / 12)
        + zeta(s, mpf(11) / 12)
    )


def abs2_on_critical_line(t):
    val = L_chi12(mpc(0.5, t))
    return float(val.real) ** 2 + float(val.imag) ** 2


if __name__ == '__main__':
    val = L_chi12(2)
    print(f"L(2,chi_12) = {val}  (claimed 0.9497031262940093425443846)")

    claimed = [3.8046, 6.6922, 8.8906, 11.1884, 12.9662, 15.1815, 16.6326, 18.8844]
    print("\nRefining claimed zero ordinates of L(1/2+it,chi_12) by minimizing |L|^2:")
    for g in claimed:
        res = minimize_scalar(abs2_on_critical_line, bounds=(g - 0.2, g + 0.2), method='bounded',
                               options={'xatol': 1e-12})
        t = res.x
        lval = L_chi12(mpc(0.5, t))
        print(f"  guess={g:7.4f}  refined t={t:.6f}  |L|={float(abs(lval)):.3e}")
