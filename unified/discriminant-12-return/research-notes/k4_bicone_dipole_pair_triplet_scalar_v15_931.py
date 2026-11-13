#!/usr/bin/env python3
"""Gravity v15.931: two Schwinger cones glued at equal spin j, rotational
triplet and singlet pair annihilators, and multi-shell E1 comparison.
Auxiliary four-boson amplitudes are not physical radial dipoles.
"""
import sympy as s
from sympy.physics.wigner import clebsch_gordan

def Lops(n):
    z=s.zeros(n*n);p=s.zeros(n*n)
    for a in range(n):
        for b in range(n):
            c=a*n+b
            z[c,c]=s.Rational(2*a+2*b-2*(n-1),2)
            if a<n-1:p[(a+1)*n+b,c]=s.sqrt((a+1)*(n-1-a))
            if b<n-1:p[a*n+b+1,c]=s.sqrt((b+1)*(n-1-b))
    return z,p

def coupled(n,l,m):
    j=s.Rational(n-1,2);v=s.zeros(n*n,1)
    for a in range(n):
        for b in range(n):
            m1=s.Rational(2*a-(n-1),2)
            m2=s.Rational(2*b-(n-1),2)
            v[a*n+b]=clebsch_gordan(j,j,l,m1,m2,m)
    return v

def pair(n,kind):
    z=s.zeros((n-1)**2,n*n)
    if n<2:return z
    terms={'minus':[(1,1,s.Integer(1))],
           'zero':[(1,2,1/s.sqrt(2)),(2,1,1/s.sqrt(2))],
           'plus':[(2,2,s.Integer(1))],
           'scalar':[(1,2,1/s.sqrt(2)),(2,1,-1/s.sqrt(2))]}[kind]
    for a in range(n):
        for b in range(n):
            for i,k,c in terms:
                aa=a-int(i==1);bb=b-int(k==1)
                if 0<=aa<n-1 and 0<=bb<n-1:
                    ua=a if i==1 else n-1-a
                    vb=b if k==1 else n-1-b
                    z[aa*(n-1)+bb,a*n+b]+=c*s.sqrt(ua*vb)
    return z

for n in range(1,5):
    z,p=Lops(n)
    assert p*z-z*p==-p
    for l in range(n):
        for m in range(-l,l+1):
            v=coupled(n,l,m)
            assert (v.T*v)[0]==1 and z*v==m*v
for n in range(2,5):
    zs,ps=Lops(n);zt,pt=Lops(n-1)
    S=pair(n,'scalar');rm=pair(n,'minus');r0=pair(n,'zero');rp=pair(n,'plus')
    assert pt*S-S*ps==s.zeros((n-1)**2,n*n)
    assert pt.T*S-S*ps.T==s.zeros((n-1)**2,n*n)
    assert pt*rm-rm*ps==-s.sqrt(2)*r0
    assert pt*r0-r0*ps==-s.sqrt(2)*rp
    assert pt*rp-rp*ps==s.zeros((n-1)**2,n*n)
    for op,charge in [(rm,-1),(r0,0),(rp,1),(S,0)]:
        assert zt*op-op*zs==charge*op

def amp(f,op,i):
    return s.simplify((f.T*op*i)[0])
assert amp(coupled(1,0,0),pair(2,'zero'),coupled(2,1,0))==1
assert amp(coupled(2,0,0),pair(3,'zero'),coupled(3,1,0))==s.sqrt(2)
assert amp(coupled(1,0,0),pair(2,'scalar')*pair(3,'zero'),coupled(3,1,0))==s.sqrt(2)
assert amp(coupled(1,0,0),pair(2,'zero')*pair(3,'zero'),coupled(3,1,0))==0
R21=s.Rational(128,243)*s.sqrt(6)
R31=s.Rational(27,128)*s.sqrt(6)
R32=s.Rational(27648,15625)*s.sqrt(3)
assert s.simplify(R31/(s.sqrt(2)*R21)-6561*s.sqrt(2)/32768)==0
assert s.simplify(R32/(s.sqrt(2)*R21)-s.Rational(26244,15625))==0
print('PASS SO4 coupled states, rotational triplet/singlet covariance,')
print('2p->1s=1, 3p->2s=sqrt2, 3p->1s=sqrt2 via S R0;')
print('distinct Coulomb/auxiliary radial factors still unselected')
