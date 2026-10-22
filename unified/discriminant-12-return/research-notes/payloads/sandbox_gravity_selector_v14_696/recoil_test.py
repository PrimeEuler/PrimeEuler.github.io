"""Two-body (proton pushes back) differences vs tonight's one-body
numbers. Jeremy: interested in the difference, though it wont be much."""
import numpy as np
import scipy.constants as C

r = C.m_e/C.m_p                       # mass ratio 5.446e-4
mu = C.m_e*C.m_p/(C.m_e + C.m_p)
kap = C.e**2/(4*C.pi*C.epsilon_0)
a0 = C.physical_constants['Bohr radius'][0]

print('=== (a) spectrum: fixed proton vs two-body ===')
E_fixed = C.m_e*kap**2/(2*C.hbar**2)/C.e
E_2body = mu*kap**2/(2*C.hbar**2)/C.e
print(f'fixed proton : E1 = -{E_fixed:.6f} eV')
print(f'two-body     : E1 = -{E_2body:.6f} eV')
print(f'difference   : {E_fixed-E_2body:.6f} eV  (rel {1-mu/C.m_e:.3e} ~ m_e/m_p)')

print()
print('=== (b) GR perihelion advance per orbit ===')
dphi_1body = 6*np.pi*C.G*C.m_p/(C.c**2 * a0)
a_rel = a0 * (C.m_e/mu)               # relative-orbit scale from mu
dphi_2body = 6*np.pi*C.G*(C.m_e + C.m_p)/(C.c**2 * a_rel)
print(f'one-body (M=m_p, a=a0)          : {dphi_1body:.6e} rad')
print(f'two-body (M=m_e+m_p, a=a_rel)   : {dphi_2body:.6e} rad')
print(f'ratio = {dphi_2body/dphi_1body:.12f}  -> difference at leading order: '
      f'{"EXACTLY ZERO" if abs(dphi_2body/dphi_1body - 1) < 1e-9 else dphi_2body/dphi_1body - 1}')
print('why: source mass and orbit scale both shift by (1 + m_e/m_p); they cancel.')
print(f'next corrections ~ nu*(v/c)^2 ~ {r*C.alpha**2:.1e} relative')
a_p = a_rel * r/(1 + r)
print(f"proton's own barycentric orbit: a_p = {a_p:.3e} m "
      f'(a scaled copy, same advance angle, rotated pi)')

print()
print('=== (c) reciprocal spin precession (hyperfine) ===')
nu_hfs = 1420405751.768               # measured 21-cm frequency, Hz
print(f'hyperfine beat (the two spins precessing about F): {nu_hfs:.3f} Hz '
      f'= {C.h*nu_hfs/C.e:.3e} eV')
mu_ratio = (2.79284734*C.physical_constants['nuclear magneton'][0]) / \
           (1.00115965*C.physical_constants['Bohr magneton'][0])
print(f'magnetic moments mu_p/mu_e = {mu_ratio:.4e} = 1/{1/mu_ratio:.1f}')
print("proton's spin precession in the electron's field is slower than the")
print("electron's in the proton's by this ratio -- small, but not 1e-4 small")

print()
print('=== (d) pairing arithmetic with mu instead of m_e ===')
Mpl = np.sqrt(C.hbar*C.c/C.G)
for name, m in (('m_e', C.m_e), ('mu ', mu), ('m_p', C.m_p)):
    aG = (m/Mpl)**2
    print(f'alpha_G({name}) depth (1/2)|ln| = {0.5*abs(np.log(aG)):.6f}')
print('spread across all choices of the paired mass: ~6.2 in the half-log,')
print('but m_e<->mu (the actual recoil choice) shifts it by only '
      f'{0.5*np.log(1+r):.2e}')
