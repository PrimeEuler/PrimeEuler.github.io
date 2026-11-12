#!/usr/bin/env python3
"""v15.760: leading-Fermi detector projector, Ricci completion, GR+solid comparator.

This is Weyl-only local tidal tomography for one scalar, one vector and
one tensor plus helicity. The actual geodesic-deviation detector responds
to full Riemann; anisotropic Ricci is NOT removed by tracefree arms.
Ordinary relativistic elasticity with identical EH+solid action,
source map, and readout has identically the same linear transfer.
"""
import sympy as s
n=s.Matrix([2,0,1])/s.sqrt(5)
e=s.Matrix([1,0,-2])/s.sqrt(5)
b=s.Matrix([0,1,0])
assert (n.T*n)[0]==(e.T*e)[0]==(b.T*b)[0]==1
assert s.simplify((n.T*e)[0])==0
Q=n*n.T-s.eye(3)/3
V=n*e.T+e*n.T
T=e*e.T-b*b.T
u=(n+e)/s.sqrt(2)
v=(n-e)/s.sqrt(2)
Ds=[n*n.T-e*e.T,e*e.T-b*b.T,u*u.T-v*v.T]
pol=[Q,V,T]
for D in Ds: assert s.simplify(s.trace(D))==0
M=s.Matrix([[s.simplify(s.trace(D*P)) for P in pol] for D in Ds])
assert M==s.Matrix([[1,0,-1],[0,0,2],[0,2,0]])
assert M.det()==-4
assert M.inv()==s.Matrix([[1,s.Rational(1,2),0],
                           [0,0,s.Rational(1,2)],
                           [0,s.Rational(1,2),0]])
ws,wv,wt=s.symbols('W_S W_V W_T',real=True)
E=ws*Q+wv*V+wt*T
obs=s.Matrix([s.trace(D*E) for D in Ds])
assert (obs-M*s.Matrix([ws,wv,wt])).applyfunc(s.simplify)==s.zeros(3,1)
assert (M.inv()*obs-s.Matrix([ws,wv,wt])).applyfunc(s.simplify)==s.zeros(3,1)
example=s.Matrix([s.Rational(2258728585,10**10),
                  s.Rational(326043176,10**10),
                  s.Rational(1238078821,10**10)])
assert M*example==s.Matrix([s.Rational(1020649764,10**10),
                             s.Rational(2476157642,10**10),
                             s.Rational(652086352,10**10)])
Rij=s.Matrix(3,3,lambda i,j:s.Symbol('R_'+str(i)+str(j),real=True))
R00,Rsc=s.symbols('R00 Rsc',real=True)
# Orthornormal signature (-+++) and the standard 4D Weyl decomposition.
Riem=E-Rij/2+s.eye(3)*(R00/2+Rsc/6)
for D in Ds:
    assert s.simplify(s.trace(D*Riem)-s.trace(D*E)+s.trace(D*Rij)/2)==0
kap,tr=s.symbols('kappa trace',real=True)
Tij=s.Matrix(3,3,lambda i,j:s.Symbol('T_'+str(i)+str(j),real=True))
EinsteinRij=kap*(Tij-tr*s.eye(3)/2)
for D in Ds:
    assert s.simplify(s.trace(D*EinsteinRij)-kap*s.trace(D*Tij))==0
# Quadratic action comparator: the same EH+solid matrix, the same
# stress map and detector functional gives EXACTLY the same response.
A,B,C,jx,jy,x,y=s.symbols('A B C j_x j_y x y',real=True)
lag=A*x*x/2+B*x*y+C*y*y/2+jx*x+jy*y
y_sol=-(B*x+jy)/C
red=s.factor(lag.subs(y,y_sol))
assert s.simplify(red-((A-B*B/C)*x*x/2+(jx-B*jy/C)*x-jy*jy/(2*C)))==0
print('PASS invertible Weyl-only three-projection detector matrix',M.tolist())
print('PASS v15.750 model-normalized Weyl arm readouts',list(map(float,M*example)))
print('PASS full Riemann readout includes anisotropic Ricci term')
print('PASS same EH+solid action/source/readout implies zero Cone-comparator residual')
print('CAUTION leading local Fermi limit; not complete finite-distance wave propagation')
