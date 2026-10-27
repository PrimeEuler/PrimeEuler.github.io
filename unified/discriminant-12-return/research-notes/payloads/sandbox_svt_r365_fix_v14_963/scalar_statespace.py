"""SVT return part 5d: scalar stability via exact state-space eigenvalues.
Frozen EL system at tau0 (H=1/tau0): E1 (psi-eq, no 2nd derivs), E2 (P-eq).
Case B00 != 0: state X=(psi, P, Pdot), psi-dot from E1, P-ddot from E2.
Eigenvalues lam of dX/dtau = S X; mode ~ e^{lam tau}; adiabatic frequency^2
reported as -lam^2 for oscillatory pairs; growth = Re(lam) > friction base."""
import sympy as sp
import numpy as np
import pickle

tau = sp.symbols('tau', positive=True)
Lred = sp.sympify(pickle.load(open('scalar_reduced.pkl', 'rb'))['Lred'])
psi_s, P_s, psi_t, P_t = sp.symbols('psi P psi_t P_t')
a_s, adot_s, C_s, kap_s = sp.symbols('a adot C kappa')
eta_s, k_s = sp.symbols('eta k')
Lbg = Lred.subs({a_s: tau/sp.sqrt(3), adot_s: 1/sp.sqrt(3), C_s: 1, kap_s: 1})
PSI, PP = sp.Function('psi'), sp.Function('P')
Lf = Lbg.subs({psi_s: PSI(tau), P_s: PP(tau), psi_t: sp.diff(PSI(tau), tau), P_t: sp.diff(PP(tau), tau)})
def EL(L, q):
    return sp.expand(sp.diff(sp.diff(L, sp.diff(q, tau)), tau) - sp.diff(L, q))
E1, E2 = EL(Lf, PSI(tau)), EL(Lf, PP(tau))
ps, pp_, psd, ppd, psdd, ppdd = sp.symbols('ps pp psd ppd psdd ppdd')
def freeze(E, t0):
    E = E.subs({sp.diff(PSI(tau), tau, 2): psdd, sp.diff(PP(tau), tau, 2): ppdd,
                sp.diff(PSI(tau), tau): psd, sp.diff(PP(tau), tau): ppd,
                PSI(tau): ps, PP(tau): pp_})
    return sp.expand(E.subs(tau, t0))
E1f, E2f = freeze(E1, 1), freeze(E2, 1)

def analyze(eta_v, kpoH):
    subs = {eta_s: eta_v, k_s: kpoH/sp.sqrt(3)}
    e1 = sp.expand(E1f.subs(subs)); e2 = sp.expand(E2f.subs(subs))
    chk = [abs(float(e1.coeff(psd))), abs(float(e1.coeff(ppd))), abs(float(e2.coeff(psd)))]
    assert max(chk) < 1e-6, f"unexpected first-deriv terms {chk}"
    C00 = float(e1.coeff(ps)); C01 = float(e1.coeff(pp_))
    A22 = float(e2.coeff(ppdd)); B21 = float(e2.coeff(ppd))
    C20 = float(e2.coeff(ps)); C21 = float(e2.coeff(pp_))
    # R365 robustness fix: C00, C01 and C20 are symbolically exactly zero
    # (psi is auxiliary and drops out of E2), so alpha = -C01/C00 is a 0/0
    # ratio of float noise. Guard the degenerate case instead of dividing:
    # when C00 vanishes, C01 and C20 must vanish with it and Ceff = C21.
    if abs(C00) < 1e-9:
        assert abs(C01) < 1e-9 and abs(C20) < 1e-9, \
            f"degenerate constraint with live coupling C01={C01} C20={C20}"
        Ceff = C21
    else:
        alpha = -C01/C00                  # psi = alpha * P  (pure constraint)
        Ceff = C21 + C20*alpha
    disc = B21**2 - 4*A22*Ceff
    if disc >= 0:
        lam = [(-B21 + np.sqrt(disc))/(2*A22), (-B21 - np.sqrt(disc))/(2*A22)]
    else:
        lam = [complex(-B21, np.sqrt(-disc))/(2*A22), complex(-B21, -np.sqrt(-disc))/(2*A22)]
    return lam, A22, B21, Ceff

print(f"{'eta':>6} {'k/H':>6}  eigenvalues lambda (H=1 units)")
for eta_v in [0.0, 0.2, 0.375, 0.5, 0.75, 1.0, 1.5]:
    for kpoH in [0.01, 0.1, 1.0, 10.0, 100.0]:
        lam, A22, B21, Ceff = analyze(eta_v, kpoH)
        w2 = [(-z)**2 if isinstance(z, complex) else None for z in lam]
        desc = []
        for z in lam:
            if isinstance(z, complex):
                desc.append(f"lam={z.real:+.3f}{z.imag:+.3f}j -> w2={(-z*z):+.2f}")
            else:
                desc.append(f"lam={z:+.3f} (pure growth/decay)")
        print(f"{eta_v:6.3f} {kpoH:6.1f}  A22={A22:+.3f} B21={B21:+.3f} Ceff={Ceff:+.3f} | " + " ; ".join(desc))
    print()
