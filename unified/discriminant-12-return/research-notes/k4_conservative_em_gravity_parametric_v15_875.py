#!/usr/bin/env python3
"""Gravity v15.875: two-oscillator conservative EM/gravity-like pump.

This is NOT the original K4+Maxwell action; all couplings, time scales
and initial phases are supplied. Bounded Hamiltonian:
 H=(px²+w_e² x²+pq²)/2 + w_g²(q+lam*x²/(2*w_g²))²/2.
The exact energy exchange is E_EMdot=lam*pq*x²/2 = -E_Gdot
when E_EM includes coupling and quartic terms. The energy partition
is conventional; H_total is unambiguous.

Initial weak pump q≈Q sin(2 w_e t+phase) gives first-cycle
Delta E_EM≈pi*lam*Q*x0² cos(phase)/2. Full model backreaction checked.

The GR proton-electron force-to-Coulomb ratio and simple quantum
variational hydrogen ground state are independent reference controls.
"""
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
from scipy.constants import epsilon_0,G,m_p,m_e,e,pi,hbar

x,px,q,pq,we,wg,lam=s.symbols('x px q pq we wg lam',real=True)
H=(px**2+we**2*x**2+pq**2)/2+wg**2*(q+lam*x**2/(2*wg**2))**2/2
vars=(x,px,q,pq)
rhs=s.Matrix([s.diff(H,px),-s.diff(H,x),s.diff(H,pq),-s.diff(H,q)])
assert s.simplify(sum(s.diff(H,z)*f for z,f in zip(vars,rhs)))==0
Eem=(px**2+we**2*x**2)/2+lam*q*x**2/2+lam**2*x**4/(8*wg**2)
Eg=(pq**2+wg**2*q**2)/2
assert s.simplify(H-Eem-Eg)==0
def derivative(F):
    return s.simplify(sum(s.diff(F,z)*f for z,f in zip(vars,rhs)))
assert s.simplify(derivative(Eem)-lam*pq*x*x/2)==0
assert s.simplify(derivative(Eg)+lam*pq*x*x/2)==0

we0,wg0,lam0,Q=1.,2.,.08,.25
def simulate(phase,periods=25):
    def energy(y):
        xx,p,qq,P=y
        return (0.5*(p*p+we0**2*xx*xx)+0.5*lam0*qq*xx*xx+
                lam0**2*xx**4/(8*wg0**2),0.5*(P*P+wg0**2*qq*qq))
    def ode(t,y):
        xx,p,qq,P=y
        return (p,-we0**2*xx-lam0*qq*xx-lam0**2*xx**3/(2*wg0**2),
                P,-wg0**2*qq-lam0*xx*xx/2)
    T=2*np.pi/we0
    times=np.linspace(0,periods*T,periods*40+1)
    sol=solve_ivp(ode,(0,times[-1]),
       (1.,0.,Q*np.sin(phase),wg0*Q*np.cos(phase)),
       t_eval=times,method='DOP853',rtol=2e-11,atol=2e-12)
    assert sol.success
    out=np.array([energy(y) for y in sol.y.T])
    em=out[:,0];grav=out[:,1]
    drift=float(np.max(abs(em+grav-em[0]-grav[0])))
    assert drift<2e-9
    return float(em[40]-em[0]),float(grav[40]-grav[0]),drift

for phase in (0.,np.pi/2,np.pi):
    dem,dgrav,drift=simulate(phase)
    predicted=np.pi*lam0*Q*np.cos(phase)/2
    assert abs(dem+dgrav)<2e-9
    assert abs(dem-predicted)<.002
    print('phase',phase,'Delta E_EM',dem,'Delta E_G',dgrav,
          'weak first-order',predicted,'conservation residual',drift)
assert simulate(0)[0]>0 and simulate(np.pi)[0]<0
ratio=4*pi*epsilon_0*G*m_p*m_e/e**2
assert 4.3e-40<ratio<4.5e-40
K=e**2/(4*pi*epsilon_0)
a0=hbar**2/(m_e*K)
Emin=-m_e*K**2/(2*hbar**2)
assert 5.2e-11<a0<5.4e-11
assert -2.3e-18<Emin<-2.1e-18
print('gravity/Coulomb proton-electron force ratio',ratio)
print('quantum Bohr radius (m)',a0,'ground variational energy (J)',Emin)
print('PASS conservative pump with opposite energy changes and QM baseline')
print('SCOPE toy Hamiltonian, not derived EM-gravity Cone coupling')
