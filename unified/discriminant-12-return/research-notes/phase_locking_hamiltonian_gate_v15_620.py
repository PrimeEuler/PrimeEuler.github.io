"""Symbolic reproducer for Lane A v15.620 (Gates 104–106). Requires sympy."""
import sympy as s
x,y,p1,p2,k,C,g,w1,w2=s.symbols('x y p1 p2 k C g w1 w2', real=True,nonzero=True)
F1=p1+k*y/2
F2=p2-k*x/2
section={p1:-k*y/2,p2:k*x/2}
def pb(f,h):
    return s.diff(f,p1)*s.diff(h,x)-s.diff(f,x)*s.diff(h,p1)+s.diff(f,p2)*s.diff(h,y)-s.diff(f,y)*s.diff(h,p2)
assert s.simplify(pb(F1,F2)+k)==0
Hhop=w1*(x-1)+w2*y-2*g*s.sqrt((x-1)*y)*s.cos(p1-p2)
assert s.simplify(pb(x+y,Hhop))==0
drift=s.trigsimp(pb(p1-p2,Hhop).subs(section))
assert s.simplify(drift-(w1-w2-g*(y-x+1)*s.cos(k*(x+y)/2)/s.sqrt((x-1)*y)))==0
h=x*y
H=h-s.diff(h,y)/k*s.sin(F1)+s.diff(h,x)/k*s.sin(F2)+C*(2-s.cos(F1)-s.cos(F2))
assert s.simplify(pb(F1,H).subs(section))==0
assert s.simplify(pb(F2,H).subs(section))==0
assert s.simplify(pb(x,H).subs(section)-x/k)==0
assert s.simplify(pb(y,H).subs(section)+y/k)==0
a,b=s.symbols('a b')
expr=[s.simplify(pb(F,H).subs({p1:a-k*y/2,p2:b+k*x/2})) for F in (F1,F2)]
M=s.Matrix([[s.diff(v,z).subs({a:0,b:0}) for z in (a,b)] for v in expr])
assert s.simplify(M-s.Matrix([[-1/k,-C*k],[C*k,1/k]]))==s.zeros(2)
assert s.simplify(M.det()-(C**2*k**2-1/k**2))==0
for K,Q in ((1,2),(2,1),(s.Rational(1,2),5)):
    print('kappa',K,'C',Q,'omega',s.sqrt(M.det().subs({k:K,C:Q})))
print('Verified exact invariance, hopping obstruction, and transverse eigenvalues.')
