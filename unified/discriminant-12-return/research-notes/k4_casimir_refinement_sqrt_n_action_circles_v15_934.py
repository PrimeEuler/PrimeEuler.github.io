#!/usr/bin/env python3
"""v15.934 Gravity: Casimir hierarchy, n+1 transition circle, sqrt(n)
decelerated-rest chord. Unit-step refinements are NOT co-scaled ladder
representations. Exact dimensionless geometry, not a field frequency.
"""
import sympy as s
h,n,j,k=s.symbols('h n j k',positive=True)
Rrest=h*s.sqrt(n)
Rcas=h*s.sqrt(n*(n+2))/2
Rtrans=h*(n+1)/2
assert s.simplify(Rtrans**2-Rcas**2-h**2/4)==0
assert s.simplify(Rtrans**2-Rrest**2-h**2*(n-1)**2/4)==0
assert s.simplify(Rcas**2-Rrest**2-h**2*n*(n-2)/4)==0
assert s.simplify(j*(j+h)-(j+h/2)**2+h**2/4)==0
assert s.simplify(j*(j+h)-j*(j+h/k)-j*h*(1-1/k))==0
assert s.simplify((j*(j+h)).subs(j,n*h/2)-h**2*n*(n+2)/4)==0

def spin_matrices(N):
    J=s.zeros(N+1)
    M=s.diag(*[-s.Rational(N,2)+i for i in range(N+1)])
    for i in range(N):
        J[i+1,i]=s.sqrt((N-i)*(i+1))
    return M,J

for nn in range(1,15):
    M,Jp=spin_matrices(nn)
    Jm=Jp.T
    assert Jp*Jm-Jm*Jp==2*M
    for qq in range(1,7):
        hh=s.Rational(1,qq)
        Mp=hh*M; P=hh*Jp; Q=hh*Jm
        assert P*Q-Q*P==2*hh*Mp
        assert Mp*P-P*Mp==hh*P
        C=Mp*Mp+(P*Q+Q*P)/2
        assert s.simplify(C-hh**2*s.Rational(nn*(nn+2),4)*s.eye(nn+1))==s.zeros(nn+1)
for nn in range(1,51):
    for qq in range(1,9):
        hh=s.Rational(1,qq)
        a,b,c=[s.simplify(r*r).subs({n:nn,h:hh}) for r in (Rrest,Rcas,Rtrans)]
        assert c>b
        assert (b<a if nn==1 else b==a if nn==2 else b>a)
        assert c>=a
q,L=s.symbols('q L',integer=True,positive=True)
jq=L/(2*q)
Cformal=s.factor(jq*(jq+1))
Ccoscaled=s.factor(jq*(jq+1/q))
assert s.factor(Cformal-Ccoscaled)==L*(q-1)/(2*q*q)
assert s.simplify((Cformal-Ccoscaled).subs(q,2)-L/8)==0
em={s.Mod(s.Rational(z,2)*(s.Rational(z,2)+1),1) for z in range(16)}
quarter={s.Mod(s.Rational(z,4)*(s.Rational(z,4)+1),1) for z in range(1,32,2)}
assert em=={0,s.Rational(3,4)}
assert quarter=={s.Rational(5,16),s.Rational(13,16)}
assert not(em & quarter)
print('PASS: closed co-scaled SU2 matrices n=1..14 q=1..6; 400 radii cases;')
print('formal vs co-scaled quarter Casimir, separated EM/odd-quarter residues')
for nn in [1,2,3,4,8]:
    print('n',nn,'(rest^2, Casimir^2, transition^2) =',
          *[s.simplify(r*r).subs({n:nn,h:1}) for r in (Rrest,Rcas,Rtrans)])
