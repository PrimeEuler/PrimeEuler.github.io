"""Gravity as e's monopole partner -- sandbox test (2026-10-21).
Jeremy: gravity causes the quantization of e; gravity would be the
monopole pair with e; the non-degeneracy of the Larmor precession is
the balancing point of G and e.
A) Pairing arithmetic vs ledgered anchors (v14.621: psi=45.310004305;
   gravity arc: alpha_G,e = 1.75181e-45, depth 51.52784).
B) Shell winding balance: on S^2_T at ring T=j+1/2, latitude X=m+1/2:
   phase/pointing fraction (m+1/2)/(j+1/2) vs holonomy (curvature)
   fraction = solid angle/2pi = (j-m)/(j+1/2). Sum?
C) Hydrogen's two precessions per orbit: spin-orbit (e-side) vs
   GR perihelion (G-side); ratio and its log vs psi anchors."""
import numpy as np
import scipy.constants as C

print('=== A) pairing arithmetic ===')
alpha = C.alpha
D = C.e**2/(4*C.pi*C.epsilon_0*C.G*C.m_e*C.m_p)     # Dirac number
psi = 0.5*np.log(D)
print(f'Dirac number D        = {D:.6e}')
print(f'psi = (1/2) ln D      = {psi:.9f}   (ledgered 45.310004305)')
Mpl = np.sqrt(C.hbar*C.c/C.G)
aGe = (C.m_e/Mpl)**2
print(f'alpha_G,e             = {aGe:.6e}   (arc value 1.75181e-45)')
print(f'depth (1/2)|ln a_G,e| = {0.5*abs(np.log(aGe)):.5f}   (arc value 51.52784)')
print(f'monopole partner: eg = hbar/2 (n=1) -> alpha_m = 1/(4 alpha) = {1/(4*alpha):.4f}')
print(f'  i.e. the (e,g) pair locks the PRODUCT: alpha * alpha_m = 1/4 exactly')
print(f'  the (e,G) pair as measured locks nothing small: alpha/alpha_G,e = {alpha/aGe:.3e}')

print()
print('=== B) shell winding balance (fractions of the full loop) ===')
for j in (0, 1, 2, 3):
    T = j + 0.5
    for m in range(-j, j+1):
        X = m + 0.5
        pointing = X/T                 # cos(alpha): e-side pointing fraction
        holonomy = (j - m)/T           # solid angle / 2pi: curvature fraction
        print(f'j={j} m={m:+d}: pointing {pointing:+.4f} + holonomy {holonomy:.4f} '
              f'= {pointing + holonomy:.4f}')
print('sum is exactly 1 on every loop: phase/pointing + curvature exhaust the loop')

print()
print('=== C) hydrogen: two precessions per orbit (n=1, circular) ===')
a0 = C.physical_constants['Bohr radius'][0]
# GR perihelion advance per orbit: 6 pi G M / (c^2 a)  (M = proton mass)
dphi_GR = 6*np.pi*C.G*C.m_p/(C.c**2 * a0)
# spin-orbit: Thomas-corrected SO precession per orbit ~ pi * (Z alpha)^2 / n^3 * (2pi-scale)
# use the standard per-orbit SO angle: dphi_SO = 2 pi * ( (Z alpha)^2 / (2 n^3) ) * (3/2 - ...) --
# keep to the robust scale: fine-structure precession per orbit = 2pi * alpha^2 / 2 (order)
dphi_SO = np.pi * alpha**2
print(f'GR perihelion / orbit   = {dphi_GR:.3e} rad')
print(f'SO precession / orbit   ~ {dphi_SO:.3e} rad (scale pi alpha^2)')
r = dphi_GR/dphi_SO
print(f'ratio G-side / e-side   = {r:.3e};  (1/2)|ln ratio| = {0.5*abs(np.log(r)):.4f}')
print(f'compare: psi = {psi:.4f}, depth a_G,e = {0.5*abs(np.log(aGe)):.4f}')
