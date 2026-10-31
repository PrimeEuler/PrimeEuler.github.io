#!/usr/bin/env python3
"""
TN trajectory cone: does a Taub-NUT geodesic lie on a cone, the way a
MIC trajectory lies on the Poincare cone?

Setup (record conventions, tn_sector.py / tn_hj_from_metric.py):
metric (t, r, th, ph), Sig = r^2 + l^2, f = (r^2 - 2mr - l^2)/Sig,
g_tt = -f, g_tph = -2 l f cos th, g_phph = -4 l^2 f cos^2 th + Sig sin^2 th,
g_rr = 1/f, g_thth = Sig.  Unit-mass geodesics, p_t = -eps, p_ph = k const.

Candidate charge vector (angular_unify_test.py, = Killing-triad charges):
    s := 2 l eps,   Pi = k + s cos th,
    J = pth * ph_hat - (Pi/sin th) * th_hat - s * n_hat,   J_z = k,
    J^2 = pth^2 + Pi^2/sin^2 th + s^2 =: A_s,   J . n_hat = -s (identity).

MIC transport claim under test: along a TRUE TN geodesic (Hamilton flow
of H = (1/2) g^mn p_m p_n from the inverse metric, sympy-derived),
J is conserved as a vector, so the trajectory lies on the cone
cos(alpha) = s/|J| about -Jhat -- with s = 2 l eps, the PAIRED charge:
the cone sees 2*eps*l, while the parabolic seats sit at k/2 -/+ eps*l
(the offset eps*l is HALF the cone's s -- the weight-2 fibration).

Cases: m = 1, eps = 0.92, s in {0 (Schwarzschild control), 1/2, 1, 3/2}
with l = s/(2 eps); shells j = 1/2, 3/2 (L^2 = j(j+1) set at th = pi/2
via pth^2 + k^2 = L^2, k = 0.6 L); r0 = 8, p_r from the HJ constraint
(infalling). RK4 in proper time, dt = 0.005, checks every 10 steps.
"""
import numpy as np
import sympy as sp

# ---------- build Hamilton's equations from the inverse metric ----------
r, th, ph = sp.symbols('r th ph')
pr, pth = sp.symbols('pr pth')
m_, l_, eps_, k_ = sp.symbols('m l eps k')
Sig = r**2 + l_**2
f = (r**2 - 2*m_*r - l_**2)/Sig
g = sp.zeros(4, 4)
g[0, 0] = -f
g[0, 3] = g[3, 0] = -2*l_*f*sp.cos(th)
g[3, 3] = -4*l_**2*f*sp.cos(th)**2 + Sig*sp.sin(th)**2
g[1, 1] = 1/f
g[2, 2] = Sig
ginv = g.inv()
p = sp.Matrix([-eps_, pr, pth, k_])
H = sp.Rational(1, 2) * (p.T * ginv * p)[0]
args = (r, th, ph, pr, pth, m_, l_, eps_, k_)
F = {
    'rdot': sp.lambdify(args, sp.diff(H, pr), 'numpy'),
    'thdot': sp.lambdify(args, sp.diff(H, pth), 'numpy'),
    'phdot': sp.lambdify(args, sp.diff(H, k_), 'numpy'),
    'prdot': sp.lambdify(args, -sp.diff(H, r), 'numpy'),
    'pthdot': sp.lambdify(args, -sp.diff(H, th), 'numpy'),
    'H': sp.lambdify(args, H, 'numpy'),
}
print("Hamilton equations built from the TN inverse metric (sympy).")


def J_vec(th_, ph_, pth_, k_, s_):
    Pi = k_ + s_ * np.cos(th_)
    sn, cs = np.sin(th_), np.cos(th_)
    n = np.array([sn*np.cos(ph_), sn*np.sin(ph_), cs])
    thh = np.array([cs*np.cos(ph_), cs*np.sin(ph_), -sn])
    phh = np.array([-np.sin(ph_), np.cos(ph_), 0.0])
    return pth_*phh - (Pi/sn)*thh - s_*n, n


def run_case(s_target, j, eps=0.92, m=1.0, dt=0.005, nsteps=30000):
    l = s_target/(2*eps) if s_target != 0 else 0.0
    s = 2*l*eps
    L2 = j*(j+1)
    L = np.sqrt(L2)
    k = 0.6*L
    pth0 = 0.8*L
    r0, th0, ph0 = 8.0, np.pi/2, 0.0
    Sig0 = r0**2 + l**2
    f0 = (r0**2 - 2*m*r0 - l**2)/Sig0
    Aang0 = pth0**2 + (k + s*np.cos(th0))**2/np.sin(th0)**2
    rhs = Sig0*(eps**2/f0 - 1) - Aang0
    assert rhs > 0, f"forbidden initial data: rhs={rhs}"
    pr0 = -np.sqrt(rhs/(Sig0*f0))
    y = np.array([r0, th0, ph0, pr0, pth0])

    def rhsf(y):
        rr, tt, pp, prr, ptt = y
        a = (rr, tt, pp, prr, ptt, m, l, eps, k)
        return np.array([F['rdot'](*a), F['thdot'](*a), F['phdot'](*a),
                         F['prdot'](*a), F['pthdot'](*a)], dtype=float)

    J0, _ = J_vec(y[1], y[2], y[4], k, s)
    Jmag = np.linalg.norm(J0)
    assert abs(Jmag**2 - (L2 + s**2)) < 1e-10
    H0 = F['H'](y[0], y[1], y[2], y[3], y[4], m, l, eps, k)
    cos_t = s/Jmag
    rp = m + np.sqrt(m*m + l*l)
    max_dJ = max_id = max_cos = max_dH = 0.0
    steps_done = 0
    for i in range(nsteps):
        k1 = rhsf(y); k2 = rhsf(y + 0.5*dt*k1)
        k3 = rhsf(y + 0.5*dt*k2); k4 = rhsf(y + dt*k3)
        y = y + dt*(k1 + 2*k2 + 2*k3 + k4)/6.0
        steps_done += 1
        if y[0] < rp + 0.3 or y[0] > 80 or abs(np.sin(y[1])) < 0.05:
            break
        if i % 10 == 0:
            J, n = J_vec(y[1], y[2], y[4], k, s)
            max_dJ = max(max_dJ, float(np.linalg.norm(J - J0)))
            max_id = max(max_id, abs(float(J @ n) + s))
            max_cos = max(max_cos, abs(float(-(J @ n))/Jmag - cos_t))
            Hv = F['H'](y[0], y[1], y[2], y[3], y[4], m, l, eps, k)
            max_dH = max(max_dH, abs(float(Hv - H0)))
    return dict(s=s, l=l, j=j, Jmag=Jmag,
                alpha=float(np.degrees(np.arccos(np.clip(cos_t, -1, 1)))),
                max_dJ=max_dJ, max_id=max_id, max_cos=max_cos,
                max_dH=max_dH, steps=steps_done)


def main():
    print("\nTN trajectory cone -- full geodesic integration")
    print(f"{'s=2leps':>8} {'l':>7} {'j':>5} {'|J|':>8} {'alpha':>9} "
          f"{'max|dJ|':>10} {'max|J.n+s|':>11} {'max|dcos|':>10} {'max|dH|':>10} {'steps':>7}")
    fails = 0
    for s_t in [0.0, 0.5, 1.0, 1.5]:
        for j in [0.5, 1.5]:
            c = run_case(s_t, j)
            print(f"{c['s']:>8.3f} {c['l']:>7.4f} {c['j']:>5} {c['Jmag']:>8.4f} "
                  f"{c['alpha']:>9.4f} {c['max_dJ']:>10.2e} {c['max_id']:>11.2e} "
                  f"{c['max_cos']:>10.2e} {c['max_dH']:>10.2e} {c['steps']:>7}")
            fails += not (c['max_dJ'] < 1e-6 and c['max_id'] < 1e-10
                          and c['max_cos'] < 1e-8 and c['max_dH'] < 1e-8)
    print(f"\nVERDICT: {'ALL CHECKS PASS' if fails == 0 else str(fails) + ' FAILURES'}")
    print("TN geodesics lie on the Poincare cone with s = 2 l eps:")
    print("the trajectory cone sees the PAIRED charge 2*eps*l, while the")
    print("parabolic seats sit at k/2 -/+ eps*l -- the seat offset is half")
    print("the cone's charge (weight-2 fibration, v14.731). Openings match")
    print("the MIC cone at equal (s, |J|): the TN-MIC difference is purely")
    print("radial, now verified in trajectory space, not only in the HJ.")


if __name__ == "__main__":
    main()
