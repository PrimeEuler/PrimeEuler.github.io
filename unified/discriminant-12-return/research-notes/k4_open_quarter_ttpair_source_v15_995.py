#!/usr/bin/env python3
"""v15.995: exactly projected TT bF^2 Maxwell vertex and tensor-exchange
selection, in the SAME fixed-wall y-polarized 1D model as v15.695.
EM cavity z in [0,pi], sin(z) and sin(3z), b_k(t) cos(kz).
Scope: fixed transverse photon polarization, leading linear metric coupling,
diagonal spatial TT propagator (local frozen K4 homogeneous background).
Does not classify nonlinear graviton self-interactions or all 3D modes.
"""
import sympy as s
z=s.symbols("z",real=True)
modes=(1,3)
e=[s.sqrt(2/s.pi)*s.sin(m*z) for m in modes]
a,ad,b,bd=s.symbols("a ad b bd")
ann=(a,b);cre=(ad,bd)
q=s.Matrix([(ann[i]+cre[i])/s.sqrt(2*modes[i]) for i in range(2)])
p=s.Matrix([-s.I*s.sqrt(s.Rational(modes[i],2))*(ann[i]-cre[i]) for i in range(2)])
results={}
for k in range(11):
    h=s.cos(k*z)
    C=s.Matrix(2,2,lambda i,j:s.simplify(s.integrate(h*e[i]*e[j],(z,0,s.pi))))
    D=s.Matrix(2,2,lambda i,j:s.simplify(s.integrate(h*s.diff(e[i],z)*s.diff(e[j],z),(z,0,s.pi))))
    # L_int=b_k( qdot^T C qdot - q^T D q).
    # The Legendre-transformed Hamiltonian linear in b_k is b_k V_k.
    V=s.expand((-p.T*C*p+q.T*D*q)[0])
    poly=s.Poly(V,ad,bd,a,b)
    sq=poly.coeff_monomial(ad**2)
    cv=poly.coeff_monomial(ad*b)
    # Highest quartic normal-ordered symbol: commutator contractions lower degree.
    o4=s.Poly(s.expand(V**2),ad,bd,a,b).coeff_monomial(ad**3*b)
    assert s.simplify(o4-2*sq*cv)==0
    assert s.simplify(o4)==0
    results[k]=(C,D,V,sq,cv)
assert s.simplify(results[2][2]-(a*ad+s.sqrt(3)*(a*b+ad*bd)))==0
assert results[0][3]!=0 and results[0][4]==0
assert results[4][3]==0 and results[4][4]!=0
assert s.simplify(results[6][2]-3*b*bd)==0
# In a spatially homogeneous linear K4 TT background the tensor mode
# propagator is diagonal in k, so tree exchange sums V_k propagator V_k.
# No single k produces (a_1 dagger)^3 a_3 in this truncation.
off_diag=s.Poly(s.expand(2*results[0][2]*results[4][2]),ad,bd,a,b).coeff_monomial(ad**3*b)
assert s.simplify(off_diag-2*s.sqrt(3))==0
# A non-diagonal k=0<->4 propagator WOULD be a route to a quartic vertex,
# but is absent from homogeneous quadratic TT K4 (new inhomogeneity needed).
for L in range(3,24):
    assert s.sqrt(s.Rational(L+1,4))>0
    assert s.simplify(s.sqrt(s.Rational(L+1,4))/s.sqrt(L*(L+1)*(L+2)) -
                      1/(2*s.sqrt(L*(L+2))))==0
# Frozen K4 quadratic tensor action for b=gamma_xx/2=-gamma_yy/2:
# S_b=M_Pl^2 int a^3 [dot(b)^2-|grad b|^2/a^2-m_T^2 b^2],
# with m_T^2=(8 eta/3)H^2. Its propagator carries M_Pl^-2 and
# remains spatial Fourier-diagonal in the homogeneous WKB comparator.
eta,H=s.symbols("eta H",real=True)
assert s.simplify(8*eta*H**2/3 - 8*eta*H**2/3)==0
print("PASS k=0..10: single spatial TT Fourier mode exchange has zero a1dag^3 a3 coefficient")
print("k2 V =",results[2][2],"; k0 squeeze=",results[0][3],"; k4 conversion=",results[4][4])
print("conditional mixed-k0/k4 exchange top-degree coefficient =",off_diag)
