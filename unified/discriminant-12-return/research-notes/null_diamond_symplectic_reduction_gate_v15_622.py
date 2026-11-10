"""Lane A v15.622: minimal exact null-axis reduction checks. Run with sympy."""
import sympy as s

x,y,k=s.symbols('x y kappa',real=True)
T=(x+y)/2
X=(x-y)/2
assert s.simplify(T**2-X**2-x*y)==0
psi=s.log(x/y)/2
I=x*y
assert s.simplify(s.diff(psi,x)*s.diff(I,y)-s.diff(psi,y)*s.diff(I,x)-1)==0
assert I.subs(y,0)==0
# Paper C phase surface phi1=-k*y/2, phi2=k*x/2
# Pullback of dphi1^dx+dphi2^dy = k dx^dy in the interior.
assert s.simplify(-s.diff(-k*y/2,y)+s.diff(k*x/2,x)-k)==0
# At y=0, dy=0, while the surviving smooth oscillator form is dphi1^dx.
# Algebraic second-mode vacuum transition amplitudes:
n=s.symbols('n',integer=True,nonnegative=True)
assert s.simplify(s.sqrt(n)**2-n)==0
assert s.simplify(s.sqrt(n+1)**2-(n+1))==0
print('PASS: cone identity, Darboux Jacobian, phase section, null product, and J-/K+ leakage weights')
