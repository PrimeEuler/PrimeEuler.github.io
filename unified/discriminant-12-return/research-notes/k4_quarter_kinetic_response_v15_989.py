#!/usr/bin/env python3
"""Cone v15.989: central quarter Casimir vs dynamical transverse operator
on canonical separate D and 2D Schwinger carriers. Units hbar=1.
No sourced intersector map is assumed. Exact SymPy verified D=2..10.
"""
import sympy as s
I=s.I
for D in range(2,11):
    def gen(dim):
        j=s.Rational(dim-1,2)
        p=s.zeros(dim); z=s.diag(*[j-n for n in range(dim)])
        for n in range(dim-1): p[n,n+1]=s.sqrt((n+1)*(dim-n-1))
        m=p.T
        x=(p+m)/2;y=(p-m)/(2*I)
        return j,x,y,z,p
    je,xe,ye,ze,pe=gen(D)
    jq,xq,yq,zq,pq=gen(2*D)
    Ke=[xq/2,yq/2,zq/2]
    Cq=s.simplify(Ke[0]**2+Ke[1]**2+Ke[2]**2)
    cq=jq*(jq+1)/4
    assert Cq==cq*s.eye(2*D)
    assert Ke[0]*Ke[1]-Ke[1]*Ke[0]==I*Ke[2]/2
    assert Cq*xq-xq*Cq==s.zeros(2*D)
    assert Cq*zq-zq*Cq==s.zeros(2*D)
    Qq=s.simplify(Ke[0]**2+Ke[1]**2)
    assert Qq==cq*s.eye(2*D)-Ke[2]**2
    assert Qq*xq-xq*Qq != s.zeros(2*D)
    assert all(Qq[a,b]==0 for a in range(2*D) for b in range(2*D) if a!=b)
    ce=je*(je+1)
    block=s.diag(ce*s.eye(D), Cq)
    projector=s.diag(s.eye(D),s.zeros(2*D))
    assert block*projector==projector*block
    Htid=s.diag(xe,xq)
    assert Htid*projector==projector*Htid
    assert Htid*block==block*Htid
    assert (2*jq+1)==2*D and (2*je+1)==D
    for m in [jq-s.Integer(k) for k in range(2*D-1)]:
        gap=s.simplify((cq-(m-1)**2/4)-(cq-m**2/4))
        assert gap==s.simplify((2*m-1)/4)
print('PASS canonical EM+q2 carrier, central Casimir no effect on tidal transitions, noncentral Q=standard anisotropy; D=2..10')
