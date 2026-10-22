#!/usr/bin/env python3
"""
Cone phase-response obstruction gate.

At rho=1 the phase-integral states reproduce standard associated Legendre
states up to statewise nonzero constants/phases, so normalization leaves
only a diagonal unitary rephasing.

At rho!=1 the eccentric family is not orthogonal in the standard sphere
inner product. Exact witness:
    <I_00,I_20> = (2/3)(1-rho^2)
with the common azimuthal 2*pi factor omitted.
"""
from math import comb
import numpy as np

def fourier_cos_moment(k, m):
    if m < 0 or k < m or (k-m) % 2:
        return 0.0
    return comb(k, (k-m)//2)/(2.0**k)

def Ijm_x(x, j, m, rho):
    x=np.asarray(x,dtype=float)
    s=np.sqrt(np.maximum(0.0,1.0-x*x))
    out=np.zeros_like(x,dtype=complex)
    for k in range(j+1):
        mu=fourier_cos_moment(k,m)
        if mu == 0:
            continue
        out += comb(j,k)*x**(j-k)*(1j*rho*s)**k*mu
    return out

def normalized_gram(m,rho,jmax=6,nq=160):
    x,w=np.polynomial.legendre.leggauss(nq)
    js=list(range(m,jmax+1))
    vals=np.array([Ijm_x(x,j,m,rho) for j in js])
    norms=np.sqrt(np.sum(np.abs(vals)**2*w,axis=1))
    vals=vals/norms[:,None]
    G=np.einsum("ax,bx,x->ab",np.conj(vals),vals,w)
    return js,G

print("=== exact low-state witness ===")
for rho in (1.0,0.8,0.5):
    exact=(2.0/3.0)*(1.0-rho*rho)
    x,w=np.polynomial.legendre.leggauss(80)
    numeric=np.sum(np.conj(Ijm_x(x,0,0,rho))*Ijm_x(x,2,0,rho)*w)
    print(f"rho={rho}: <I00,I20> numeric={numeric.real:.15g}, exact={exact:.15g}")
    assert abs(numeric.real-exact) < 2e-14

print("\n=== normalized Gram matrices ===")
for m in (0,1,2):
    for rho in (1.0,0.8,0.5):
        js,G=normalized_gram(m,rho,jmax=6)
        off=np.max(np.abs(G-np.eye(len(js))))
        print(f"m={m}, rho={rho}: max|G-I|={off:.12g}")
        if rho == 1.0:
            assert off < 2e-12
        else:
            assert off > 1e-3

print("\n=== rho=1 state-ray equivalence ===")
print("v14.696: I_jm=(-i)^m [j!/(j+m)!] P_j^m.")
print("Normalization removes the positive amplitude; (-i)^m is unitary rephasing.")
print("Consistently transformed angular matrix elements and response functions")
print("therefore equal standard SO(3).")

print("\nVERDICT")
print("rho=1 phase integration cannot by itself generate a new angular observable;")
print("rho!=1 is not a quantum eigenbasis in the standard spherical metric.")
print("A prediction requires an independently justified metric/Hamiltonian/coupling.")