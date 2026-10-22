# THE G LEVER: average the GR 1/r^3 perturbation on the cone (the Note's unfinished step).
# Central perturbations conserve energy and L, so e is secularly fixed: on the cone the
# point can only ROTATE about the T axis. The Lie-Poisson bracket with H = eps*T generates
# exactly that: dX/dt = {X,eps T} = eps*Y, dY/dt = {Y,eps T} = -eps*X  (bracket {T,X}=-Y etc).
import mpmath as mp
mp.mp.dps = 15
# 1) bracket flow check: pure rotation, T and X^2+Y^2 conserved
X, Y, T, eps, dt = mp.mpf('0.6'), mp.mpf('0.8'), mp.mpf('1.0'), mp.mpf('0.37'), mp.mpf('0.001')
import math
ang = 0.0
for i in range(2000):
    X, Y = X + eps*Y*dt, Y - eps*X*dt
print(f"bracket flow H=eps*T: after t=2, (X,Y)=({mp.nstr(X,6)},{mp.nstr(Y,6)}), radius^2={mp.nstr(X*X+Y*Y,8)} (pure rotation, angle drifted, T fixed)")
# 2) time average <1/r^3> over one Kepler orbit vs cone formula  (A,B epicycle radii)
#    <1/r^3>_t = 1/(a^3 (1-e^2)^{3/2});  cone: a=A+B, 1-e^2 = ((A-B)/(A+B))^2
def avg_inv_r3(A, B):
    a = A+B; e2 = 4*A*B/(A+B)**2
    f = mp.quad(lambda E: (1-e2*mp.cos(E)**2)**0 , [0, 2*mp.pi]) # placeholder replaced below
    # time average: dt ∝ (1 - e cosE) dE ; r = a(1 - e cosE)
    e = mp.sqrt(e2)
    num = mp.quad(lambda E: (a*(1-e*mp.cos(E)))**(-3) * (1-e*mp.cos(E)), [0, 2*mp.pi])
    den = mp.quad(lambda E: (1-e*mp.cos(E)), [0, 2*mp.pi])
    return num/den, 1/(a**3*(1-e2)**mp.mpf('1.5'))
for (A,B) in [(5.728e10, 6.2e8), (3.0, 1.0), (2.0, 1.9)]:
    num, formula = avg_inv_r3(A,B)
    print(f"  A={A:.3g} B={B:.3g}: <1/r^3> numeric={mp.nstr(num,6)}  formula={mp.nstr(formula,6)}")
# 3) Mercury: Delta-varpi per orbit = 6 pi mu / (c^2 p), p = a(1-e^2) = (A-B)^2/(A+B) = (2T-2Y)/sqrt(2T+2Y)
mu, c = mp.mpf('1.32712440018e20'), mp.mpf('299792458')
a_m, e_m = mp.mpf('5.7909e10'), mp.mpf('0.20563')
b_m = a_m*mp.sqrt(1-e_m**2); A, B = (a_m+b_m)/2, (a_m-b_m)/2
T_, Y_ = (A*A+B*B)/2, A*B
p_cone = (2*T_-2*Y_)/mp.sqrt(2*T_+2*Y_)
dphi = 6*mp.pi*mu/(c**2 * p_cone)
arcsec_per_century = dphi * (mp.mpf(180)/mp.pi) * 3600 * mp.mpf('415.2')
print(f"Mercury: p from cone coords = {mp.nstr(p_cone,7)} m (direct a(1-e^2)={mp.nstr(a_m*(1-e_m**2),7)})")
print(f"precession = {mp.nstr(dphi,5)} rad/orbit = {mp.nstr(arcsec_per_century,5)} arcsec/century  (the famous ~43)")
