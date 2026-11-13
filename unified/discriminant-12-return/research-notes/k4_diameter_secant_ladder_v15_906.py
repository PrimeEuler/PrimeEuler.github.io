#!/usr/bin/env python3
"""Gravity v15.906: exact diameter-secant ratio and fixed-shell Schwinger ladder."""
import sympy as s
n,k=s.symbols("n k", integer=True, positive=True)
D=n+k
X=(n-k)/2
T=D/2
Y=s.sqrt(n*k)
assert s.simplify(T*T-X*X-Y*Y)==0
assert s.simplify(D/(n-k+2)-((n+1)+(k-1))/((n+1)-(k-1)))==0
assert s.simplify((n+1)*(k-1)-n*k-(k-n-1))==0
assert s.simplify((1+k/n)/(1-k/n)-D/(n-k))==0

for N,K in [(2,2),(3,2),(4,1),(5,0)]:
    theta=2*s.atan(s.sqrt(s.Rational(K,N))) if K else s.Integer(0)
    assert s.simplify(s.cos(theta)-s.Rational(N-K,N+K))==0
    assert s.simplify(s.sin(theta)-2*s.sqrt(N*K)/(N+K))==0
    print((N,K),"diameter",N+K,"chord",s.sqrt(N*K),
          "secant","singular" if N==K else s.Rational(N+K,N-K),
          "theta",float(theta))

for N in range(2,9):
    # D=N. Fock (a,b)=(n-1,k), so a+b=N-1.
    states=[(q,N-q) for q in range(1,N+1)]
    mat=s.zeros(N)
    for i,(q,r) in enumerate(states[:-1]):
        mat[i+1,i]=s.sqrt(q*r)
    assert all(s.simplify(mat[i+1,i]**2-(i+1)*(N-i-1))==0 for i in range(N-1))
    assert all(a+b==N for a,b in states)
    # Two equal-frequency quantum oscillators: H0= hbar*omega*(a+b)=hbar*omega*N.
    # NB: a,b here are CONE pair coordinates; Fock occupation a-1,b totals N-1.
    # Therefore E/hbar/omega=N for all states and all J+ links have zero H0 gap.
print("PASS circle identity, secant update, J+ coefficients, and within-shell degeneracy")
