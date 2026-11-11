#!/usr/bin/env python3
"""v15.727: minimally coupled canonical spectator scalar, coasting K4 FLRW.
Signature (-,+,+,+). The scalar's quadratic stress is the external source
at O(epsilon^2) around a zero scalar background, not a solution of the
coupled K4 metric/solid perturbations.
"""
import sympy as s
t,x,z=s.symbols('tau x z',positive=True,real=True)
a=t/s.sqrt(3)
chi=s.Function('chi')(t,x,z)
dt,dx,dz=[s.diff(chi,u) for u in (t,x,z)]
box=-s.diff(chi,t,2)-3*dt/t+(s.diff(chi,x,2)+s.diff(chi,z,2))/a**2
g=s.diag(-1,a*a,a*a,a*a)
gi=s.diag(-1,a**-2,a**-2,a**-2)
coords=[t,x,s.Symbol('y'),z]
dchi=s.Matrix([dt,dx,0,dz]);grad=gi*dchi
kin=(dchi.T*grad)[0]
T=s.Matrix(4,4,lambda i,j:s.expand(grad[i]*grad[j]-gi[i,j]*kin/2))
assert s.simplify(T[0,0]-(dt**2+(dx**2+dz**2)/a**2)/2)==0
Gamma={(l,m,n):s.simplify(sum(gi[l,j]*(
 s.diff(g[j,n],coords[m])+s.diff(g[j,m],coords[n])
 -s.diff(g[m,n],coords[j]))/2 for j in range(4)))
 for l in range(4) for m in range(4) for n in range(4)}
for nu in range(4):
 div=s.expand(sum(s.diff(T[mu,nu],coords[mu]) for mu in range(4))
  +sum(Gamma[mu,mu,lam]*T[lam,nu]+Gamma[nu,mu,lam]*T[mu,lam]
  for mu in range(4) for lam in range(4)))
 assert s.simplify(div-grad[nu]*box)==0,nu
# This source generally has nonzero isotropic spatial stress; it is not
# the tracefree T_ij template used in v15.716-v15.725.
spatialtrace=s.simplify(a*a*sum(T[i,i] for i in range(1,4)))
assert s.simplify(spatialtrace-(3*dt**2-(dx**2+dz**2)/a**2)/2)==0
# Pointwise anisotropic gradient-stress invariant.
vx,vz=s.symbols('v_x v_z',real=True)
v=s.Matrix([vx,0,vz]);v2=(v.T*v)[0]
Q=v*v.T-s.eye(3)*v2/3
assert s.simplify(s.trace(Q*Q)-s.Rational(2,3)*v2**2)==0
# Nonparallel wave components p=(2,0,0), q=(0,0,1)
# give an anisotropic cross-stress at K=p+q with T/V/S projections.
p=s.Matrix([2,0,0]);q=s.Matrix([0,0,1]);K=p+q
n=K/s.sqrt((K.T*K)[0]);I=s.eye(3);Proj=I-n*n.T
S=p*q.T+q*p.T
Sf=S-I*s.trace(S)/3
TT=s.simplify(Proj*Sf*Proj-Proj*s.trace(Proj*Sf)/2)
V=s.simplify(Proj*Sf*n*n.T+n*(n.T*Sf*Proj))
SC=s.simplify(Sf-TT-V)
norm=lambda M:s.simplify(s.trace(M*M))
assert (Sf-TT-V-SC).applyfunc(s.simplify)==s.zeros(3)
assert (norm(TT),norm(V),norm(SC))==(s.Rational(32,25),s.Rational(72,25),s.Rational(96,25))
# t^(-1)u(log t,x,z) reduces the on-shell wave equation to
# u_ss -3 Delta(u)-u=0.
ss=s.symbols('s',real=True);u=s.Function('u')(ss,x,z)
w=u.subs(ss,s.log(t))
lhs=s.simplify(t**3*(-s.diff(w/t,t,2)-3*s.diff(w/t,t)/t
 +3*(s.diff(w/t,x,2)+s.diff(w/t,z,2))/t**2))
rhs=(u-s.diff(u,ss,2)+3*(s.diff(u,x,2)+s.diff(u,z,2))).subs(ss,s.log(t))
assert s.simplify(lhs-rhs)==0
print('PASS canonical scalar: source from action; positive local energy')
print('PASS exact covariant conservation iff scalar KG equation')
print('PASS 2/3 STF stress and nonzero cross-wave S/V/T projectors')
print('PASS nonzero spatial trace prohibits reuse of tracefree-only Ward')
print('PASS logarithmic-time wave equation')
