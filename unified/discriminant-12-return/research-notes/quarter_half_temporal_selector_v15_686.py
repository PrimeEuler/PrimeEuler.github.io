#!/usr/bin/env python3
"""v15.686: quarter/half lattice versus temporal resonance selector.

This reproducer isolates what follows from the established q=2 shell labels
alone and what requires an additional physical dictionary.

Established static increments:
    gravity-candidate minimal odd rung: du_G = 1/4
    EM half-grid increment:            du_EM = 1/2

It proves:
  * an affine ENERGY dictionary gives Omega_G/omega_EM = 1/2 if the same
    conversion scale is used, not the primary parametric value 2;
  * an affine LENGTH/WAVELENGTH dictionary with common propagation speed gives
    the inverse ratio Omega_G/omega_EM = 2;
  * independent Hamiltonian normalizations make the ratio arbitrary;
  * the q=2 geometric Casimir used as a Hamiltonian gives shell-dependent
    transition ratios, not a universal 2:1;
  * the exact parity grading makes one quarter rung sector-odd and two quarter
    rungs sector-even.

These are algebraic dictionary tests, not a physical identification of the
Cone shell coordinate with energy, length, or time.
"""
import sympy as s

L, aG, aE, Lam, c, hbar = s.symbols(
    "L a_G a_EM Lambda c hbar", positive=True, real=True
)

duG=s.Rational(1,4)
duE=s.Rational(1,2)

# Gate 232: common affine energy map E=Lambda*u.
OmegaG=s.simplify(Lam*duG/hbar)
omegaE=s.simplify(Lam*duE/hbar)
assert s.simplify(OmegaG/omegaE-s.Rational(1,2))==0
assert s.simplify(2*duE/duG-4)==0  # four quarter units reach pump energy 2*EM.

# With independent sector energy normalizations, the ratio is arbitrary.
ratio_general=s.simplify((aG*duG)/(aE*duE))
assert s.simplify(ratio_general-aG/(2*aE))==0
# For any desired positive r, choosing aG=2 r aE realizes it.

# Gate 233: if the same labels are physical wavelengths and speed is common,
# omega = 2*pi*c/lambda, so the ratio is inverse.
lambdaG,lambdaE=s.symbols("lambda_G lambda_EM", positive=True)
ratio_wave=s.simplify((c/(duG))/(c/(duE)))
assert ratio_wave==2

# Gate 234: geometric q=2 shell Casimir C=L(L+4)/16.
C=lambda x:s.expand(x*(x+4)/16)
dC1=s.simplify(C(L+1)-C(L))      # odd quarter shell shift
dC2=s.simplify(C(L+2)-C(L))      # half-grid/two-rung shift
assert dC1==(2*L+5)/16
assert dC2==(L+3)/4
casimir_gap_ratio=s.simplify(dC1/dC2)
assert casimir_gap_ratio==(2*L+5)/(4*(L+3))
assert s.simplify(casimir_gap_ratio-2)!=0

# Exact q=2 grading: chi_L=(-1)^L.  One rung flips it; two preserve it.
for ell in range(32):
    chi=(-1)**ell
    assert (-1)**(ell+1)==-chi
    assert (-1)**(ell+2)==chi

# Taub-NUT fixed-l spectrum from the certified quarter-pair chain:
# E_k = hbar*c*k/(4*l), so Delta k=1 is half the Delta k=2 frequency.
l=s.symbols("l", positive=True)
Omega_k1=c/(4*l)
Omega_k2=c/(2*l)
assert s.simplify(Omega_k1/Omega_k2-s.Rational(1,2))==0

print("static lattice ratio du_G/du_EM =",duG/duE)
print("common affine ENERGY dictionary: Omega_G/omega_EM =",OmegaG/omegaE)
print("common wavelength dictionary:     Omega_G/omega_EM =",ratio_wave)
print("independent Hamiltonians:          Omega_G/omega_EM =",ratio_general)
print("q=2 Casimir one/two-rung gap ratio =",casimir_gap_ratio)
print("Taub-NUT k=1/k=2 gap ratio =",s.simplify(Omega_k1/Omega_k2))
print("PASS: the bare quarter/half lattice does not uniquely select temporal 2:1")
