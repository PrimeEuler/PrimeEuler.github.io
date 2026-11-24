#!/usr/bin/env python3
"""Gravity v15.1382: two leading on-shell massless H2 waves plus
vacuum TT Weyl wave give nonclosed curvature-contracted area form.
This is leading in target amplitudes a*b, not full nonlinear sigma dynamics.
"""
import sympy as S
t,x,y,z,e,w,a,b,m,k=S.symbols("t x y z e w a b m k",real=True,nonzero=True)
co=[t,x,y,z];sg=[-1,1,1,1]
h=e*S.cos(w*(t-z))
pert=[[S.Integer(0) for j in range(4)] for i in range(4)]
pert[1][1]=h;pert[2][2]=-h
d=lambda f,i:S.diff(f,co[i])
d2=lambda f,i,j:S.diff(f,co[i],co[j])
R={}
for i in range(4):
 for j in range(4):
  for r in range(4):
   for s in range(4):
    v=(d2(pert[i][s],r,j)+d2(pert[j][r],s,i)-d2(pert[i][r],s,j)-d2(pert[j][s],r,i))/2
    if v!=0:R[i,j,r,s]=S.simplify(v)
u=a*S.sin(m*(t-x));v=b*S.sin(k*(t-y))
box=lambda f:-d2(f,0,0)+d2(f,1,1)+d2(f,2,2)+d2(f,3,3)
assert S.simplify(box(u))==0 and S.simplify(box(v))==0
B={(i,j):d(u,i)*d(v,j)-d(u,j)*d(v,i) for i in range(4) for j in range(4)}
K={(i,j):S.trigsimp(S.factor(sum(R.get((i,j,r,s),0)*sg[r]*sg[s]*B[r,s]
  for r in range(4) for s in range(4)))) for i in range(4) for j in range(4)}
dK={(i,j,l):S.trigsimp(S.factor(d(K[j,l],i)+d(K[l,i],j)+d(K[i,j],l)))
 for i,j,l in ((0,1,2),(0,1,3),(0,2,3),(1,2,3))}
assert any(expr!=0 for expr in dK.values())
for indices,expr in dK.items():print('dK',indices,'=',expr)
print('PASS leading-order on-shell internal waves and TT wave give nonclosed Weyl-H2 area')
print('OPEN full nonlinear sigma backreaction and coupling selection')
