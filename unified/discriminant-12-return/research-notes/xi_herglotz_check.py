"""External audit (Round 140) independent check of v13.929's Xi Weyl-target
identities, using mpmath's own zeta/gamma directly -- no reuse of this
project's Phi(tau)/g(t) machinery.

Checks:
  1. m_inf(i) = -C_inf * Xi'(i)/Xi(i) = i exactly, where
     C_inf = xi(3/2)/xi'(3/2), Xi(z) = xi(1/2 - i*z).
  2. Im(m_inf(z)) > 0 at several sample points in the upper half plane,
     consistent with (and only with, per the entry's theorem) RH.
"""
import mpmath as mp

mp.mp.dps = 25


def xi(s):
    return 0.5 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi(z):
    return xi(mp.mpf('0.5') - 1j * z)


def Xip(z, h=mp.mpf('1e-6')):
    return (Xi(z + h) - Xi(z - h)) / (2 * h)


def C_inf():
    h = mp.mpf('1e-8')
    xi32 = xi(mp.mpf('1.5'))
    xi32p = (xi(mp.mpf('1.5') + h) - xi(mp.mpf('1.5') - h)) / (2 * h)
    return xi32 / xi32p


def m_inf(z, C=None):
    C = C if C is not None else C_inf()
    return -C * Xip(z) / Xi(z)


if __name__ == '__main__':
    C = C_inf()
    print("C_inf = xi(3/2)/xi'(3/2) =", mp.nstr(C, 12))
    print("m_inf(i) [should be exactly i] =", mp.nstr(m_inf(1j, C), 12))

    print("\nIm(m_inf(z)) at sample points in the upper half plane:")
    for z in [0.5 + 0.3j, 2 + 1j, 5 + 0.5j, 10 + 2j, -3 + 0.7j]:
        z = mp.mpc(z)
        m = m_inf(z, C)
        print(f"  z={z}: m_inf(z)={mp.nstr(m, 10)}  Im>0? {mp.im(m) > 0}")
