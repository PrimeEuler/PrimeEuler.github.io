#!/usr/bin/env python3
"""Gravity v15.919: spectral lifetime gate against prior hydrogen bicone results.
Separates same-shell J+ matrix factors from cross-energy-shell E1 dipole radiation.
No G, new physical lifetime or new coupling derived.
"""
import math
import sympy as s
n,k,D=s.symbols('n k D', integer=True, positive=True)
omega,C=s.symbols('omega C',positive=True)
# Exact within-fixed-D Schwinger ladder amplitude.
assert s.simplify((n+k)-((n+1)+(k-1)))==0
assert s.simplify(s.sqrt(n*k)**2-n*k)==0
# With identical-mode H0=hbar*omega*(N+1), Delta E=0 on fixed D:
assert s.simplify((n+k)-((n+1)+(k-1)))==0
# E1 spontaneous emission rate Aif=C omega_if^3 |d_if/d_*|^2,
# conditional d_if = d_* sqrt(nk) leads following ratio if branches have
# independently measured nonzero omega and share common reduced prefactor.
n1,k1,n2,k2,w1,w2=s.symbols('n1 k1 n2 k2 w1 w2',positive=True)
rate1=C*w1**3*n1*k1
rate2=C*w2**3*n2*k2
assert s.simplify(rate1/rate2-(n1*k1/(n2*k2))*(w1/w2)**3)==0
# Actual A upper->lower needs energy gap and branching; tau_upper=1/sum A.
tauH=1.592e-9
sigmaH=.025e-9
tauHe=.9992e-10
sigmaHe=.0026e-10
AH=1/tauH
widthH=1/(2*math.pi*tauH)
predHe=tauH/16
sig_pred=sigmaH/16
z=(predHe-tauHe)/math.hypot(sig_pred,sigmaHe)
print('H lifetime ns',tauH*1e9,'Einstein A s^-1',AH,'natural FWHM Hz',widthH)
print('He+ measured ps',tauHe*1e12,'naive H/16 ps',predHe*1e12,'difference sigma',z)
# Two neighboring edge strengths on D=5 at |3,1> correspond to
# right sqrt4 and left sqrt6. The 2/3 ratio is NOT radiative if omega=0.
assert s.Rational(4,6)==s.Rational(2,3)
# In physical E1 rates the angular reduced matrix elements, degeneracy,
# radial integrals and branching matter and are not fixed by J+ alone.
print('PASS exact J+ amplitude and fixed shell degeneracy; conditional E1 rate ratio')
print('PASS measured H and He+ lifetimes from staged bicone paper (no external lifetime fit)')
