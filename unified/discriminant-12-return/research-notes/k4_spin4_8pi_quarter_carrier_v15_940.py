#!/usr/bin/env python3
"""v15.940: 8pi Fourier-phase carrier for quarter Casimir, tensored
with ordinary SU(2)xSU(2). Exact finite-cut tests; distinct from
physical angular SU(2) and from defective quarter ladder.
Infinite Hardy unilateral shift has an additional bottom boundary.
"""
import sympy as s

for N in (4,8,16,32):
    K=s.diag(*[s.Rational(k,4) for k in range(N)])
    C=K*(K+s.eye(N))
    W=s.zeros(N)
    for k in range(N-1):
        W[k+1,k]=1
    Chi=s.diag(*[(-1)**k for k in range(N)])
    U2=s.diag(*[s.I**k for k in range(N)])
    assert K*W-W*K==W/4
    assert Chi*W+W*Chi==s.zeros(N)
    assert C*W-W*C==W*(K/2+s.Rational(5,16)*s.eye(N))
    assert U2**2==Chi and U2**4==s.eye(N)
    assert U2*W==s.I*W*U2
    assert W.T*W==s.eye(N)-s.diag(*([0]*(N-1)+[1]))
    assert W*W.T==s.eye(N)-s.diag(1,*([0]*(N-1)))
    for k in range(N):
        assert C[k,k]==s.Rational(k*(k+4),16)
        assert s.simplify(s.exp(16*s.pi*s.I*C[k,k])-(-1)**k)==0
    jb=s.kronecker_product(s.diag(1,-1)/2,s.eye(2))
    kb=s.kronecker_product(s.eye(2),s.diag(1,-1)/2)
    spin=s.kronecker_product(jb,s.eye(N))
    kp=s.kronecker_product(kb,s.eye(N))
    phase=s.kronecker_product(s.eye(4),K)
    shift=s.kronecker_product(s.eye(4),W)
    assert phase*spin==spin*phase and phase*kp==kp*phase
    assert shift*spin==spin*shift and shift*kp==kp*shift
    if N==8:
        print('N',N,'Casimir residues',sorted({s.Mod(C[k,k],1) for k in range(N)}))

for k in range(1,32,2):
    assert s.exp(-4*s.pi*s.I*s.Rational(k,4))==-1
    assert s.exp(-8*s.pi*s.I*s.Rational(k,4))==1

# Spin4 phase tensor cannot remove preexisting open-boundary defect.
L=7
j=s.Rational(L,4)
M=s.diag(*[-j+s.Rational(i,2) for i in range(L+1)])
J=s.zeros(L+1)
for i in range(L-1):
    J[i+2,i]=s.sqrt(s.Rational((L-i)*(i+2),4))
E=s.simplify(j*(j+1)*s.eye(L+1)-M*M-(J*J.T+J.T*J)/2)
assert E.rank()==2
assert s.kronecker_product(E,s.eye(4)).rank()==8
print('PASS: 8pi carrier, Z4 character, quarter shift, Spin4 commutation, persistent defect')
