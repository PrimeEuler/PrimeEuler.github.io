"""SymPy exact checks for Lane A ledger v15.621, Gates 107–109."""
import sympy as s
x,y,p1,p2,k,C=s.symbols('x y p1 p2 k C', real=True,nonzero=True)
def bracket(f,h):
    return (s.diff(f,p1)*s.diff(h,x)-s.diff(f,x)*s.diff(h,p1)
           +s.diff(f,p2)*s.diff(h,y)-s.diff(f,y)*s.diff(h,p2))
F1=p1+k*y/2
F2=p2-k*x/2
sec={p1:-k*y/2,p2:k*x/2}
assert s.simplify(bracket(F1,F2)+k)==0
a,b=s.symbols('a b',integer=True)
f=s.Function('f')(x,y)
mode=f*s.exp(s.I*(a*p1+b*p2))
u=s.exp(s.I*(a*p1+b*p2))
assert s.simplify(bracket(F1,mode)/u-
                  (s.diff(f,x)-s.I*k*b*f/2))==0
assert s.simplify(bracket(F2,mode)/u-
                  (s.diff(f,y)+s.I*k*a*f/2))==0
sol=s.exp(s.I*k*(b*x-a*y)/2)
assert s.simplify(s.diff(sol,x)-s.I*k*b*sol/2)==0
assert s.simplify(s.diff(sol,y)+s.I*k*a*sol/2)==0
h=x*y
H=h-x/k*s.sin(F1)+y/k*s.sin(F2)+C*(2-s.cos(F1)-s.cos(F2))
assert s.simplify(bracket(F1,H).subs(sec))==0
assert s.simplify(bracket(F2,H).subs(sec))==0
n1,n2,m=s.symbols('n1 n2 m',integer=True)
dphi1=-2*s.pi*m*n2
dphi2=2*s.pi*m*(n1+1)
assert s.simplify(s.exp(s.I*dphi1)-1)==0
assert s.simplify(s.exp(s.I*dphi2)-1)==0
print("PASS: Fourier tangent conditions, exponential coefficients, engineered exception, 4pi vertex alias.")
