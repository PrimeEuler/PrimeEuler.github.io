#!/usr/bin/env python3
"""Gravity v15.1177: quarter Casimir, shell-shift parity, holonomy intertwiner gate.
Prior: v15.602, .626-.631, .955, .1176. Formal geometric C is not
SU2 central spin Casimir; twisted boundary sectors are chosen carriers.
The existing v15.602 T changes L by 2 and preserves parity; the
auxiliary W changes L by 1 and exchanges it. e^(i theta/4) maps twist
beta to beta+1/4, not a scalar endomorphism on a fixed S1 bundle.
A nonzero covariantly constant intertwiner between 1D flat bundles
with different holonomy is impossible without compensating connection.
"""
import sympy as s
I=s.I
for L in range(21):
    C=lambda x:s.Rational(x*(x+4),16)
    chi=lambda x:(-1)**x
    assert s.simplify(s.exp(16*s.pi*I*C(L))-chi(L))==0
    assert chi(L+2)==chi(L) and chi(L+1)==-chi(L)
    assert C(L+1)-C(L)==s.Rational(2*L+5,16)
    assert C(L+2)-C(L)==s.Rational(L+3,4)
N=15
W=s.zeros(N); T=s.zeros(N)
for x in range(N-1):W[x+1,x]=1
for x in range(N-2):T[x+2,x]=1
C=s.diag(*[s.Rational(x*(x+4),16) for x in range(N)])
parity=s.diag(*[(-1)**x for x in range(N)])
assert parity*W+W*parity==s.zeros(N)
assert parity*T-T*parity==s.zeros(N)
assert W.T*W==s.diag(*([1]*(N-1)+[0]))
assert W*W.T==s.diag(*([0]+[1]*(N-1)))
assert all((C*W-W*C)[x+1,x]==s.Rational(2*x+5,16) for x in range(N-1))
th,beta=s.symbols("th beta",real=True)
psi=s.exp(I*(beta+2)*th)
shift=s.exp(I*th/4)*psi
assert s.simplify(shift.subs(th,th+2*s.pi)/shift-
                  s.exp(2*s.pi*I*(beta+s.Rational(1,4))))==0
Dpsi=s.diff(psi,th)
assert s.simplify(Dpsi.subs(th,th+2*s.pi)/Dpsi-
                  s.exp(2*s.pi*I*beta))==0
holonomy_ratio=s.exp(2*s.pi*I*s.Rational(1,4))
assert holonomy_ratio==I and holonomy_ratio!=1
# Parallel intertwiner with holonomies U2 = i U1 would satisfy
# U2*t=t*U1; because U1 is invertible, t=0.
a,t=s.symbols("a t",nonzero=True)
assert s.solve(s.Eq(I*a*t,a*t),t)==[]
print("PASS C-shell grading, even T vs odd W, finite-boundary isometry")
print("PASS quarter-twist domain changes; no nonzero flat parallel map")
print("NO physical quarter coupling from local spin connection alone")
