"""External audit (Round 145) independent numerical check of v13.950's
Klein-Gordon/Chebyshev extremal family identity:

  hat(M_{a,Omega})(z) = cosh(a*sqrt(Omega^2 - z^2))

where M_{a,Omega} = (1/2)(delta_{-a}+delta_{a})
                     + (Omega*a/2) * I_1(Omega*sqrt(a^2-x^2))/sqrt(a^2-x^2) * 1_{|x|<a} dx

Also checks the stopband leakage claim: sup_{|t|>=Omega}|F_{a,Omega}(t)|
= sech(a*Omega), achieved exactly at the band edge t=Omega.

Fresh implementation, not reusing anything from the ledger entry itself.
"""
import numpy as np
from scipy import integrate, special


def M_hat(z, a, Omega):
    """Fourier transform of the proposed measure, direct quadrature."""
    atom_term = np.cos(z * a)  # (1/2)(e^{iza}+e^{-iza}), works for complex z

    def bessel_density(x):
        r = np.sqrt(max(a * a - x * x, 1e-300))
        return special.i1(Omega * r) / r if r > 1e-12 else Omega / 2

    re_part, _ = integrate.quad(lambda x: np.real(np.exp(1j * z * x)) * bessel_density(x), -a, a, limit=200)
    im_part, _ = integrate.quad(lambda x: np.imag(np.exp(1j * z * x)) * bessel_density(x), -a, a, limit=200)
    integral_term = (Omega * a / 2) * (re_part + 1j * im_part)
    return atom_term + integral_term


def F_direct(z, a, Omega):
    w = np.sqrt(Omega**2 - z**2 + 0j)
    return np.cosh(a * w)


if __name__ == '__main__':
    a, Omega = 2.0, 1.0
    print("Identity check: hat(M)(z) =? cosh(a*sqrt(Omega^2-z^2))  [a=2, Omega=1]")
    for z in [0.0, 0.5, 1.5, 3.0, 1j * 0.7, 2 + 1j]:
        z = complex(z)
        lhs = M_hat(z, a, Omega)
        rhs = F_direct(z, a, Omega)
        print(f"  z={z}:  M_hat={lhs:.6f}   direct={rhs:.6f}   "
              f"match={np.isclose(lhs, rhs, atol=1e-5)}")

    print("\nStopband leakage: sup_{|t|>=Omega}|F(t)| =? sech(a*Omega), at the band edge")
    sech_val = 1 / np.cosh(a * Omega)
    print(f"  sech(a*Omega) = {sech_val:.6f}")
    for t in [1.0, 1.01, 1.1, 1.5, 2.0, 3.0, 5.0, 10.0]:
        r = np.sqrt(max(t * t - Omega * Omega, 0))
        F = np.cos(a * r) / np.cosh(a * Omega)
        print(f"  t={t:5.2f}  F(t)={F:+.6f}  |F(t)|<=sech? {abs(F) <= sech_val + 1e-9}")
