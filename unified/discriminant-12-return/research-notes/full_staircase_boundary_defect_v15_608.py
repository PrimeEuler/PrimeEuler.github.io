"""Exact full-staircase pushforward of continuum AM-GM boundary Casimir defect.

Run with Python 3 and sympy. Adds no physical operator or shell selection.
"""
import sympy as s
x,y,n=s.symbols("x y n",positive=True)
J=(x+y)/(4*s.sqrt(x*y))
Ecorner=x*y+(x+y)/2
Erow=y*(x+1)/2
Ecol=x*(y+1)/2

corner=s.simplify(s.integrate(s.integrate(s.expand(J*Ecorner),(y,0,1)),(x,0,1)))
row=s.simplify(s.integrate(s.integrate(s.expand(J*Erow),(y,0,1)),(x,1,n)))
col=s.simplify(s.integrate(s.integrate(s.expand(J*Ecol),(y,1,n)),(x,0,1)))
B=s.simplify(corner+row+col)
assert corner == s.Rational(4,9)
assert s.simplify(row-col)==0
assert s.simplify(B-s.sqrt(n)*(3*n**2+8*n+9)/45)==0

def W(k,h):
    k=s.Integer(k);h=s.Integer(h)
    return (s.sqrt(h)*(k**s.Rational(3,2)-(k-1)**s.Rational(3,2))+
            h**s.Rational(3,2)*(s.sqrt(k)-s.sqrt(k-1)))/3

for N in (1,2,3,5,11,20):
    WT=s.Add(*(W(k,N+1-k) for k in range(1,N+1)))
    WD=s.Add(*(W(k,N//k) for k in range(1,N+1)))
    print(N,"B",s.N(B.subs(n,N),14),"WT",s.N(WT,14),
          "WD",s.N(WD,14),"B/WT",s.N(B.subs(n,N)/WT,14),
          "B/WD",s.N(B.subs(n,N)/WD,14))
assert abs(float(B.subs(n,11))-33.90327563474409)<1e-11
print("exact symbolic tests passed")
