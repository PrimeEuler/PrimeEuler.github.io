#!/usr/bin/env python3
"""v15.1049: Discriminant-12 Pell boost versus two-polarization Maxwell
mode coefficient and separate Klein-four sign characters.
No identification of arithmetic V4, signed-pair V4, photon-polarization
V4, or q2 shell chi without independently supplied intertwiners.
"""
import sympy as s
z=s.symbols('z',real=True)
B=s.Matrix([[2,s.sqrt(3)],[s.sqrt(3),2]])
J=s.diag(1,-1)
assert s.simplify(B.det()-1)==0
assert s.simplify(J*B*J-B.inv())==s.zeros(2)
assert B.eigenvals()=={2+s.sqrt(3):1,2-s.sqrt(3):1}
assert s.simplify((2+s.sqrt(3))-(2-s.sqrt(3))-2*s.sqrt(3))==0
# The product sign is +,-,-,+ on the signed-pair V4.
signs=[(1,1),(-1,1),(1,-1),(-1,-1)]
assert [a*b for a,b in signs]==[1,-1,-1,1]
for a,b in signs:
 for c,d in signs:
  assert (a*c)*(b*d)==(a*b)*(c*d)
# Both eigenvalue multipliers are positive; Pell return preserves
# each factor sign and cannot send uv>0 to uv<0.
assert 2+s.sqrt(3)>0 and 2-s.sqrt(3)>0
U12={1:(1,1),5:(-1,-1),7:(-1,1),11:(1,-1)}
for x in U12:
 for y in U12:
  assert U12[(x*y)%12]==tuple(U12[x][i]*U12[y][i] for i in range(2))
# Physical Maxwell projection: x photon spatial mode m, y photon n,
# plus metric k=0 and cross metric k=m+n; z in [0,pi], c=hbar=1.
a,ad,d,dd=s.symbols('a ad d dd',commutative=True)
for m,n in [(1,3),(2,6),(3,9),(1,2),(1,4),(2,5)]:
 e1=s.sqrt(2/s.pi)*s.sin(m*z)
 e2=s.sqrt(2/s.pi)*s.sin(n*z)
 C=s.simplify(s.integrate(s.cos((m+n)*z)*e1*e2,(z,0,s.pi)))
 D=s.simplify(s.integrate(s.cos((m+n)*z)*s.diff(e1,z)*s.diff(e2,z),(z,0,s.pi)))
 assert C==-s.Rational(1,2) and D==s.Rational(m*n,2)
 q1=(a+ad)/s.sqrt(2*m);p1=-s.I*s.sqrt(s.Rational(m,2))*(a-ad)
 q2=(d+dd)/s.sqrt(2*n);p2=-s.I*s.sqrt(s.Rational(n,2))*(d-dd)
 plus=s.expand(p1**2-m*m*q1**2)
 cross=s.expand(2*(C*p1*p2-D*q1*q2))
 assert s.simplify(plus+m*(a*a+ad*ad))==0
 assert s.simplify(cross+s.sqrt(m*n)*(a*dd+ad*d))==0
 coeff=s.Poly(s.expand(plus*cross+cross*plus),ad,dd,a,d).coeff_monomial(ad**3*d)
 assert s.simplify(coeff-2*m*s.sqrt(m*n))==0
 assert s.simplify(coeff/m**2-2*s.sqrt(s.Rational(n,m)))==0
 assert s.simplify(cross.subs({d:-d,dd:-dd})+cross)==0
 assert s.simplify(plus.subs({d:-d,dd:-dd})-plus)==0
 print('m,n=',m,n,'raw=',coeff,'scaled=',s.simplify(coeff/m**2))
# The existing q2 projected T shifts L by +2, preserving (-1)^L.
for L in range(3,31):
 assert (-1)**(L+2)==(-1)**L
print('PASS: Pell ray gap, V4 characters, wedge no-transfer,')
print('cavity coefficient family and q2 parity; no sourced intertwiner')
