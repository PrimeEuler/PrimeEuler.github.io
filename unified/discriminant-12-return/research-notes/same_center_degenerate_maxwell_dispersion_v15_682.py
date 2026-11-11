#!/usr/bin/env python3
"""v15.682: same-center degenerate Maxwell-mode dispersion ratio.

Ideal PEC cube [-pi/2,pi/2]^3, c=1.  Two exact degenerate solenoidal
Maxwell modes are compared in the high-frequency TT/free-fall magnetostatic
limit.  The ordinary-GR source structure follows the general linearized
Maxwell effective current; replacing K=omega by a timelike K is explicitly
a conditional K4 dispersion insertion, not a completed K4 detector model.
"""
import sympy as s

pi=s.pi
t,x,y,z=s.symbols("t x y z", real=True)
K,mu,B0=s.symbols("K mu B0", positive=True, real=True)
V=pi**3

# ------------------------------------------------------------------
# Exact TT effective current for:
#   wave along +x, cross tensor h_yz=h_zy=H(t,x),
#   static uniform B=B0 zhat.
# Eq. J_eff^mu = -d_nu(h^nu_rho F^{rho mu}-h^mu_rho F^{rho nu})
# for trace h=0 gives only J_eff^z=-B0 d_x H.
# ------------------------------------------------------------------
H=s.Function("H")(t,x)
coords=[t,x,y,z]
hmat=s.zeros(4)
hmat[2,3]=H
hmat[3,2]=H
F=s.zeros(4)
F[1,2]=B0
F[2,1]=-B0

Jeff=[]
for a in range(4):
    expr=0
    for nu in range(4):
        inside=sum(
            hmat[nu,rho]*F[rho,a]-hmat[a,rho]*F[rho,nu]
            for rho in range(4)
        )
        expr += -s.diff(inside,coords[nu])
    Jeff.append(s.simplify(expr))

assert Jeff[:3] == [0,0,0]
assert s.simplify(Jeff[3]+B0*s.diff(H,x)) == 0

# ------------------------------------------------------------------
# Exact PEC cube modes E_mn = 2 zhat cos(mx)cos(ny), m,n odd.
# They are divergence-free, satisfy E_tangent=0 on every wall,
# and omega_mn^2=m^2+n^2.  B=(i/omega) curl E.
# Gué et al. normalization: int |E|^2 dV=int |B|^2 dV=V.
# ------------------------------------------------------------------
def mode(m,n):
    om=s.sqrt(m*m+n*n)
    Ez=2*s.cos(m*x)*s.cos(n*y)
    Bx=-2*n*s.cos(m*x)*s.sin(n*y)/om  # common phase i omitted in |B|^2
    By= 2*m*s.sin(m*x)*s.cos(n*y)/om
    return om,Ez,Bx,By

def vol(expr):
    return s.integrate(expr,
        (x,-pi/2,pi/2),(y,-pi/2,pi/2),(z,-pi/2,pi/2))

om17,E17,B17x,B17y=mode(1,7)
om55,E55,B55x,B55y=mode(5,5)
omega=5*s.sqrt(2)
assert om17 == omega and om55 == omega
assert s.simplify(vol(E17**2)-V) == 0
assert s.simplify(vol(E55**2)-V) == 0
assert s.simplify(vol(B17x**2+B17y**2)-V) == 0
assert s.simplify(vol(B55x**2+B55y**2)-V) == 0
assert s.simplify(vol(E17*E55)) == 0

# Tangential E vanishes at x/y walls; B normal vanishes there.
for wall in (-pi/2,pi/2):
    assert s.simplify(E17.subs(x,wall)) == 0
    assert s.simplify(E55.subs(x,wall)) == 0
    assert s.simplify(E17.subs(y,wall)) == 0
    assert s.simplify(E55.subs(y,wall)) == 0
    assert s.simplify(B17x.subs(x,wall)) == 0
    assert s.simplify(B55x.subs(x,wall)) == 0
    assert s.simplify(B17y.subs(y,wall)) == 0
    assert s.simplify(B55y.subs(y,wall)) == 0

# For H=h exp[i(omega t-Kx)], Jeff_z=i K B0 H.
# The dimensionless TT bulk coupling has a common factor i(K/omega);
# it cancels in the ratio.  Keep only the normalized geometry integral.
def G(Ez):
    return s.simplify(vol(Ez*s.exp(-s.I*K*x))/V)

G17=s.simplify(G(E17))
G55=s.simplify(G(E55))

G17_closed=8*s.cos(pi*K/2)/(7*pi**2*(K**2-1))
G55_closed=-8*s.cos(pi*K/2)/(pi**2*(K**2-25))
# SymPy returns removable-special-point Piecewise branches at K=+-1,+-5.
# Verify the generic antiderivatives at the physical massless operating point;
# all subsequent algebra uses the displayed elementary closed forms.
assert s.simplify((G17-G17_closed).subs(K,omega)) == 0
assert s.simplify((G55-G55_closed).subs(K,omega)) == 0

ratio=s.simplify(G17_closed/G55_closed)
ratio_closed=(25-K**2)/(7*(K**2-1))
assert s.simplify(ratio-ratio_closed) == 0

# Ordinary massless comparator: K=omega=sqrt(50).
R0=s.Rational(25,343)
assert s.simplify(-ratio_closed.subs(K,omega)-R0) == 0  # ratio is negative

# Conditional timelike dispersion K^2=omega^2(1-mu^2), mu=m_T/omega.
# In the neighborhood of mu=0, |ratio|=(K^2-25)/(7(K^2-1)).
K2=50*(1-mu**2)
Rmu=s.simplify((K2-25)/(7*(K2-1)))
D=s.simplify(Rmu/R0)
Dclosed=s.simplify((1-2*mu**2)/(1-s.Rational(50,49)*mu**2))
assert s.simplify(D-Dclosed) == 0
assert s.limit((D-1)/mu**2,mu,0) == -s.Rational(48,49)

print("omega_17=omega_55 =",omega)
print("massless |eta_17/eta_55| =",R0)
print("normalized timelike ratio D(mu) =",Dclosed)
print("D(mu)=1-(48/49) mu^2+O(mu^4)")
print("PASS: exact same-center degenerate Maxwell mode ratio has O(m_T^2/omega^2) slope")
