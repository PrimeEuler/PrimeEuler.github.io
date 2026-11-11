#!/usr/bin/env python3
"""v15.656 exact local full-Dirac Clifford commutant and projected charge ladder."""
import sympy as s
rho,p=s.symbols('rho p',positive=True)
n=s.symbols('n',integer=True,positive=True)
b=s.sqrt(rho)*s.exp(rho/2)
f=s.Function('f')(rho)
D=lambda m,g:s.diff(g,rho)+((p-m)/2-(m-1)/(2*rho)+1/(2*(1+rho)))*g
assert s.simplify(D(n+1,b*f)-b*D(n,f))==0
I=s.I
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]]);sz=s.diag(1,-1);Z=s.zeros(2)
def blk(A,B,C,D):return A.row_join(B).col_join(C.row_join(D))
gamma=[blk(Z,-I*t,I*t,Z) for t in (sx,sy,sz)]+[blk(Z,s.eye(2),s.eye(2),Z)]
for a in range(4):
 for c in range(4):
  assert gamma[a]*gamma[c]+gamma[c]*gamma[a]==(2 if a==c else 0)*s.eye(4)
q=s.symbols('q0:16');Q=s.Matrix(4,4,q)
eq=[]
for g in gamma:eq.extend(g*Q-Q*g)
assert s.linsolve(eq,q)==s.FiniteSet(tuple(q[15] if i in [0,5,10,15] else s.Integer(0) for i in range(16)))
# Local Clifford [D_A,M_b]=c(db); nonconstant b cannot commute with full Dirac.
assert s.simplify(s.diff(b,rho))!=0
P=s.Rational(7,2);labels=[(m,a) for m in (1,2,3) for a in range(m)]
ix={t:i for i,t in enumerate(labels)}
T1=s.zeros(6);T2=s.zeros(6);N=s.diag(*[m for m,a in labels])
for col,(m,a) in enumerate(labels):
 if m+1<P:
  c=s.sqrt((P-m)**(m+1)/(P-m-1)**(m+2))
  T1[ix[m+1,a+1],col]=c*s.sqrt(a+1)
  T2[ix[m+1,a],col]=c*s.sqrt(m-a)
assert N*T1-T1*N==T1 and N*T2-T2*N==T2
assert T1*T2==T2*T1
assert T1**3==s.zeros(6) and T2**3==s.zeros(6)
assert T1!=s.zeros(6) and T2!=s.zeros(6)
print('PASS v15.656: Clifford rigidity, noncommuting full Dirac multiplication, bounded finite prescribed truncated ladder.')
