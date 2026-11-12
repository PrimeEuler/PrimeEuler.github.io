#!/usr/bin/env python3
"""Gravity v15.787: independently derive FULL electric Riemann, not only
electric Weyl, directly from perturbed coasting FLRW scalar/vector/tensor
metrics. Compare with independently audited v15.730 canonical source.
Standard EH+solid matched comparator has identically zero discrepancy.
"""
import sympy as s
t,z,k,eps=s.symbols('tau z k epsilon',positive=True,real=True)
a=t/s.sqrt(3);e=s.exp(s.I*k*z)
coords=[t,s.Symbol('x'),s.Symbol('y'),z]
Phi=s.Function('Phi_N')(t);Psi=s.Function('Psi_N')(t)
B=s.Function('B_V')(t);gamma=s.Function('gamma_T')(t)
g0=s.diag(-1,a*a,a*a,a*a)
gi0=s.diag(-1,a**-2,a**-2,a**-2,a**-2)

def R(i,j,pert):
    """eps*e^(ikz) coefficient R^i_(0j0); background is zero on coasting."""
    g=g0+eps*pert*e
    gi=gi0-eps*gi0*pert*gi0*e
    C={}
    for l in range(4):
        for m in range(4):
            for n in range(4):
                if m>n:
                    C[l,m,n]=C[l,n,m]
                    continue
                v=sum(gi[l,p]*(s.diff(g[p,n],coords[m])+
                    s.diff(g[p,m],coords[n])-s.diff(g[m,n],coords[p]))/2
                    for p in range(4))
                v=s.expand(v)
                C[l,m,n]=v.coeff(eps,0)+eps*v.coeff(eps,1)
    v=s.diff(C[i,0,0],coords[j])-s.diff(C[i,0,j],coords[0])
    v+=sum(C[i,h,j]*C[h,0,0]-C[i,h,0]*C[h,0,j]
           for h in range(4))
    return s.simplify(s.expand(v).coeff(eps,1)/e)

scalar=s.diag(-2*Phi,-2*a*a*Psi,-2*a*a*Psi,-2*a*a*Psi)
A=s.diff(Psi,t,2)+(2*s.diff(Psi,t)+s.diff(Phi,t))/t
assert s.simplify(R(1,1,scalar)-A)==0
assert s.simplify(R(3,3,scalar)-A+k*k*Phi/a**2)==0
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
fullTF=-k*k*Phi/a**2*Q
weyl=k*k*(Phi+Psi)/(2*a*a)
ricciTF=2*(weyl+k*k*Phi/a**2)*Q
assert (fullTF-weyl*Q+ricciTF/2).applyfunc(s.simplify)==s.zeros(3)

vector=s.zeros(4);vector[0,2]=vector[2,0]=-a*B
fullV=-s.I*k*(s.diff(B,t)+B/t)/(2*a)
assert s.simplify(R(2,3,vector)-fullV)==0
assert s.simplify(R(3,2,vector)-fullV)==0
assert s.simplify(fullV.subs(s.diff(B,t),0)+s.I*k*B/(2*a*t))==0

tensor=s.zeros(4);tensor[1,1]=a*a*gamma
tensor[2,2]=-a*a*gamma
fullT=-(s.diff(gamma,t,2)+2*s.diff(gamma,t)/t)/2
assert s.simplify(R(1,1,tensor)-fullT)==0
assert s.simplify(R(2,2,tensor)+fullT)==0

# Exact canonical two-wave v15.730 benchmark at tau=1, |K|^2=5.
bench={t:1,k:s.sqrt(5),Phi:s.Rational(191,1800),
       Psi:-s.Rational(1,72)}
rc=s.simplify((-k*k*Phi/a**2).subs(bench))
wc=s.simplify(weyl.subs(bench))
ric=s.simplify((2*(weyl+k*k*Phi/a**2)).subs(bench))
assert [rc,wc,ric]==[-s.Rational(191,120),
                     s.Rational(83,120),s.Rational(137,30)]
assert s.simplify(rc-wc+ric/2)==0
D=s.diag(-1,0,1)
assert s.trace(D*Q)==1
assert s.simplify(s.trace(D*fullTF).subs(bench)-rc)==0
assert s.trace(Q*Q)==s.Rational(2,3)
print("PASS direct Christoffels/Riemann for scalar, vector, tensor")
print("PASS tracefree electric Riemann = Weyl - Ricci_TF/2")
print("PASS static vector shift: full electric Riemann nonzero, electric Weyl zero")
print("PASS canonical source full STF=",rc,"Weyl=",wc,"Ricci_TF=",ric)
print("SCOPE: leading small-baseline Fermi, not finite-arm light propagation")
