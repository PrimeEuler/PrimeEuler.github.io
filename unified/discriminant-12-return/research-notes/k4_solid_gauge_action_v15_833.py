#!/usr/bin/env python3
"""v15.833: exact linear gauge Ward of frozen v14.935 K4 solid action.

Original +--- action re-expressed in -+++ conformal variables:
S_m=-int sqrt(-g) C b^(2/3)(1+eta_s J);
B^IJ=g^mu nu partial_mu phi^I partial_nu phi^J, b=sqrt(det B).
Background phi^I=x^I, a=a0 exp(H eta), 3H²=kappa C.
Passive diffeo eta_new=eta+T, x_new=x+U^i, pi^I=-U^I.
"""
import sympy as s
eta,x,y,z=s.symbols("eta x y z",real=True)
q=[eta,x,y,z]
HH,C,kappa=s.symbols("H C kappa",positive=True,real=True)
T=s.Function("T")(*q)
U=s.Matrix([s.Function("U"+str(i))(*q) for i in range(3)])
Ud=U.applyfunc(lambda f:s.diff(f,eta))
D=s.Matrix(3,3,lambda i,j:s.diff(U[i],q[j+1]))
Phi=-s.diff(T,eta)-HH*T
V=Ud-s.Matrix([s.diff(T,q[i+1]) for i in range(3)])
h=-2*HH*T*s.eye(3)-D-D.T
pi=-U
P=s.Matrix(3,3,lambda i,j:s.diff(pi[i],q[j+1]))
# a² delta B^IJ: -h^IJ+partial_i pi^J+partial_j pi^I
E=-h+P+P.T
assert (E-2*HH*T*s.eye(3)).applyfunc(s.simplify)==s.zeros(3)
TF=E-s.eye(3)*s.trace(E)/3
assert TF.applyfunc(s.simplify)==s.zeros(3)
# J has no first-order contribution on isotropic background;
# J^(2)=tr(E_TF²)/9, hence identically zero along pure diffeo.
assert s.simplify(s.trace(TF*TF)/9)==0
rho_rel=s.Rational(2,3)*s.trace(E)/2 # delta rho/rho=(2/3)delta b/b
assert s.simplify(rho_rel-2*HH*T)==0
# Matter density L0=-C*a², delta L/L0=Phi+tr(h)/2+delta(b^(2/3))/b^(2/3)
rel_L=s.simplify(Phi+s.trace(h)/2+s.trace(E)/3)
assert s.simplify(rel_L+s.diff(T,eta)+s.trace(D)+2*HH*T)==0
# Stress from isotropic perfect-fluid limit of this elastic solid:
# rho=C/a², p=-rho/3; cov Tbg=diag(C,-C/3,-C/3,-C/3).
T00=s.simplify(C*(rho_rel+2*Phi))
T0=s.simplify(C*V+s.Rational(2,3)*C*s.diff(pi,eta))
Tij=s.simplify(-C*(rho_rel*s.eye(3)+h)/3)
assert s.simplify(T00+2*C*s.diff(T,eta))==0
expected0=-C*s.Matrix([s.diff(T,q[i+1]) for i in range(3)])+C*Ud/3
assert (T0-expected0).applyfunc(s.simplify)==s.zeros(3,1)
assert (Tij-C*(D+D.T)/3).applyfunc(s.simplify)==s.zeros(3)
stress=s.zeros(4)
stress[0,0]=T00
for i in range(3):
 stress[0,i+1]=stress[i+1,0]=T0[i]
 for j in range(3):stress[i+1,j+1]=Tij[i,j]
Tbg=s.diag(C,-C/3,-C/3,-C/3)
Gbg=s.diag(3*HH**2,-HH**2,-HH**2,-HH**2)
xi=s.Matrix([T,*list(U)])
Lie=lambda M:s.Matrix(4,4,lambda mu,nu:s.simplify(sum(
 M[alpha,nu]*s.diff(xi[alpha],q[mu])+M[mu,alpha]*s.diff(xi[alpha],q[nu])
 for alpha in range(4))))
assert (stress+Lie(Tbg)).applyfunc(s.simplify)==s.zeros(4)
assert (Gbg-kappa*Tbg).subs(kappa*C,3*HH**2).applyfunc(s.simplify)==s.zeros(4)
# For a diffeo-covariant EH + solid action:
# delta(G-kappa*T)=-Lie_xi(Gbg-kappa*Tbg)=0 on-shell.
ward=(-Lie(Gbg)+kappa*Lie(Tbg)).subs(kappa*C,3*HH**2)
assert ward.applyfunc(s.simplify)==s.zeros(4)
# Omitting pi=-U produces a false solid shear.
wrong=-h
wrongTF=wrong-s.eye(3)*s.trace(wrong)/3
subs={T:eta**3*s.cos(x+z),U[0]:eta**3*s.sin(y),
      U[1]:eta**3*s.cos(z),U[2]:eta**3*s.sin(x)}
W=wrongTF.subs(subs).doit().subs({
 eta:s.Rational(1,2),x:s.Rational(1,4),y:s.Rational(1,3),z:s.Rational(1,5)})
assert any(abs(float(s.N(v)))>1e-5 for v in W)
print("PASS internal B tracefree gauge cancellation and J^(2)=0")
print("PASS solid action pure diffeomorphism is a boundary term")
print("PASS all 10 solid covariant stress components = -Lie_xi(Tbg)")
print("PASS linear Einstein-solid gauge Ward on background 3H^2=kappa*C")
print("NEGATIVE frozen phonon creates fictitious internal shear")
