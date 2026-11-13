#!/usr/bin/env python3
"""Gravity v15.914 — full Fermi tidal oscillator, no fixed-shell RWA.
Numerical units: hbar=M=omega0=1; A=.04,B=.08 are tidal stiffnesses.
Initial Fock state |3,1>, associated to Cone (4,1), D=5.
Full model is conventional GR Fermi tidal comparator, not a new Cone action.
"""
import numpy as np
from scipy.linalg import eigh,expm

A,B=.04,.08
NMAX=13
basis=[(a,N-a) for N in range(NMAX+1) for a in range(N+1)]
lookup={s:i for i,s in enumerate(basis)}
L=len(basis)
ann=[]
for mode in range(2):
    z=np.zeros((L,L),complex)
    for col,pair in enumerate(basis):
        if pair[mode]:
            dest=list(pair); dest[mode]-=1
            z[lookup[tuple(dest)],col]=np.sqrt(pair[mode])
    ann.append(z)
q=[(z+z.conj().T)/np.sqrt(2) for z in ann]
p=[1j*(z.conj().T-z)/np.sqrt(2) for z in ann]
H0=np.diag([sum(state)+1 for state in basis])
Ht=.5*A*(q[0]@q[0]-q[1]@q[1])+B*(q[0]@q[1])
H=H0+Ht
Kdiff=(p[0]@p[0]-p[1]@p[1])/2
Pcross=p[0]@p[1]
parity=np.diag([(-1)**sum(s) for s in basis])
assert np.max(np.abs(H@parity-parity@H))<1e-12
for V in p:
    assert np.max(np.abs(V@parity+parity@V))<1e-12
vals,vecs=eigh(H)
initial=np.zeros(L,complex)
initial[lookup[(3,1)]]=1
def psi(t):
    return vecs@(np.exp(-1j*vals*t)*(vecs.conj().T@initial))
def avg(state,op):
    return np.vdot(state,op@state).real
def in_shell(state,N):
    return sum(abs(state[i])**2 for i,s in enumerate(basis) if sum(s)==N)
recs=[]
for t in (0,2,8,16,24):
    state=psi(t)
    assert abs(np.linalg.norm(state)-1)<2e-12
    assert abs(avg(state,p[0]))<2e-12 and abs(avg(state,p[1]))<2e-12
    rec=(t,avg(state,Kdiff),avg(state,Pcross),in_shell(state,4))
    recs.append(rec)
    print("time, K1-K2, p1p2/M, P(N=4):",*[round(float(x),9) for x in rec])
reference=[(0,1,0,1),(2,1.0656853878041328,.16992536107928752,.9834403716341634),
           (8,.8853473039921975,.2690406987441183,.9831752090226531),
           (16,.3601905229618627,.4418477918086938,.9914142009267556),
           (24,-.21127096603941176,.6706507288254427,.9952641441410612)]
for computed,expected in zip(recs,reference):
    assert max(abs(float(x)-float(y)) for x,y in zip(computed,expected))<2e-7
# Fixed-N RWA: exact projection H_tidal -> A J_z + B J_x.
ids=[lookup[(a,4-a)] for a in range(5)]
jp=np.zeros((5,5),complex)
for a in range(4):
    jp[a+1,a]=np.sqrt((a+1)*(4-a))
jx=(jp+jp.conj().T)/2
jz=np.diag(np.arange(5)-2)
assert np.max(abs(Ht[np.ix_(ids,ids)]-(A*jz+B*jx)))<1e-12
assert np.max(abs(Kdiff[np.ix_(ids,ids)]-jz))<1e-12
assert np.max(abs(Pcross[np.ix_(ids,ids)]-jx))<1e-12
for t in (2,8,16,24):
    state=psi(t)
    rwa=expm(-1j*t*(A*jz+B*jx))[:,3]
    difference=avg(state,Kdiff)-avg(rwa,jz)
    print("time",t,"full minus RWA kinetic imbalance",float(difference))
# Exact normal mode frequencies of H=1/2(p²+q^T(I+E)q), E=[[A,B],[B,-A]]
rho=np.hypot(A,B)
omegap,omegam=np.sqrt(1+rho),np.sqrt(1-rho)
assert rho<1
print("normal mode omega+ omega- beat",omegap,omegam,omegap-omegam)
print("PASS: full parity, zero physical mean velocities, Fock shell leakage, "
      "kinetic correlations, RWA projection, stable normal modes")
