"""SVT return part 6: final cross-checks.
(1) Vector: omega^2(k) from the REDUCED action (post shift-elimination) vs the
    closed form m_T^2 + c_T^2 k_phys^2 = (8 eta/3) H^2 + (2 eta/3) k_phys^2.
(2) Scalar boundary sharpness: eta just below/above 3/8 at very high k,
    via Ceff/A22 from the frozen EL system (same extraction as statespace)."""
import sympy as sp
import numpy as np
import pickle

# ---- (1) vector reduced action
Lv = sp.sympify(pickle.load(open('vector_reduced.pkl', 'rb'))['Lred_vector'])
f, f_t = sp.symbols('f f_t')
a_s, adot_s, C_s, kap_s, eta_s, k_s = sp.symbols('a adot C kappa eta k')
Kf = sp.diff(Lv, f_t, 2); Gf = -sp.diff(Lv, f, 2)
print("VECTOR  eta=0.75 (H=1 units: a=adot=1/sqrt3, C=kappa=1)")
for kpoH in [0.1, 1.0, 10.0, 100.0]:
    subs = {a_s: 1/np.sqrt(3), adot_s: 1/np.sqrt(3), C_s: 1, kap_s: 1, eta_s: 0.75, k_s: kpoH/np.sqrt(3)}
    w2_num = float(Gf.subs(subs))/float(Kf.subs(subs))
    w2_pred = 8*0.75/3 + (2*0.75/3)*kpoH**2
    print(f"  k_phys/H={kpoH:6.1f}  omega^2 numeric={w2_num:12.4f}   predicted={w2_pred:12.4f}   ratio={w2_num/w2_pred:.6f}")

# ---- (2) scalar boundary
tau = sp.symbols('tau', positive=True)
Lred = sp.sympify(pickle.load(open('scalar_reduced.pkl', 'rb'))['Lred'])
psi_s, P_s, psi_t, P_t = sp.symbols('psi P psi_t P_t')
Lbg = Lred.subs({a_s: tau/sp.sqrt(3), adot_s: 1/sp.sqrt(3), C_s: 1, kap_s: 1})
PSI, PP = sp.Function('psi'), sp.Function('P')
Lf = Lbg.subs({psi_s: PSI(tau), P_s: PP(tau), psi_t: sp.diff(PSI(tau), tau), P_t: sp.diff(PP(tau), tau)})
def EL(L, q): return sp.expand(sp.diff(sp.diff(L, sp.diff(q, tau)), tau) - sp.diff(L, q))
E1, E2 = EL(Lf, PSI(tau)), EL(Lf, PP(tau))
ps, pp_, psd, ppd, psdd, ppdd = sp.symbols('ps pp psd ppd psdd ppdd')
def frz(E):
    E = E.subs({sp.diff(PSI(tau), tau, 2): psdd, sp.diff(PP(tau), tau, 2): ppdd,
                sp.diff(PSI(tau), tau): psd, sp.diff(PP(tau), tau): ppd, PSI(tau): ps, PP(tau): pp_})
    return sp.expand(E.subs(tau, 1))
E1f, E2f = frz(E1), frz(E2)
def scalar_w02(eta_v, kpoH):
    subs = {eta_s: eta_v, k_s: kpoH/sp.sqrt(3)}
    e1 = sp.expand(E1f.subs(subs)); e2 = sp.expand(E2f.subs(subs))
    al = -float(e1.coeff(pp_))/float(e1.coeff(ps))
    A22 = float(e2.coeff(ppdd)); Ceff = float(e2.coeff(pp_)) + float(e2.coeff(ps))*al
    return Ceff/A22
print("SCALAR boundary (omega_0^2 = Ceff/A22, H=1):")
for eta_v, kpoH in [(0.37, 1000.0), (0.375, 1000.0), (0.40, 1000.0), (0.374, 100.0), (0.376, 100.0)]:
    w02 = scalar_w02(eta_v, kpoH)
    pred = 8*eta_v/3 + (-sp.Rational(1,3) + 8*eta_v/9)*kpoH**2
    print(f"  eta={eta_v:.3f} k/H={kpoH:7.1f}  omega_0^2={w02:14.2f}   closed-form={float(pred):14.2f}")
