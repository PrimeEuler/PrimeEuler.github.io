#!/usr/bin/env python3
"""Exact c_phi,11 reduction from the g^11/g^12 Dyson-log coefficients."""
import sympy as s
pi=s.pi
N=5
def add(a,b): return [s.expand(a[i]+b[i]) for i in range(N+1)]
def mul(a,b): return [s.expand(sum(a[k]*b[i-k] for k in range(i+1))) for i in range(N+1)]
def inv(a):
    r=[0]*(N+1); r[0]=1/a[0]
    for n in range(1,N+1):
        r[n]=s.expand(-sum(a[k]*r[n-k] for k in range(1,n+1))/a[0])
    return r
def scale(a,c): return [s.expand(c*v) for v in a]
def powp(a,n):
    r=[s.Integer(1)]+[0]*N
    for _ in range(n): r=mul(r,a)
    return r
A=[1,-s.Rational(1,64),-s.Rational(3,2048),-s.Rational(341,3145728),-s.Rational(21745,3623878656),-s.Rational(8445707,41747082117120)]
Q=[s.Rational(1,8),s.Rational(1,128),s.Rational(61,196608),s.Rational(937,452984832),-s.Rational(5033593,5218385264640),-s.Rational(31839895957,300578991243264000)]
S=add(mul(A,A),[0]+mul(Q,Q)[:N])
F=[s.Integer(1)]+[0]*N
for n in range(1,N+1):
    F[n]=s.expand((S[n]-sum(F[k]*F[n-k] for k in range(1,n)))/2)
D=F.copy(); D[0]=0
q=scale(D,pi/4)
tanq=add(add(q,scale(powp(q,3),s.Rational(1,3))),scale(powp(q,5),s.Rational(2,15)))
T=mul(add([1]+[0]*N,tanq),inv(add([1]+[0]*N,scale(tanq,-1))))
B=mul(mul(Q,inv(F)),T)
coef_half=0
for k in range(6):
    coef_half += s.Rational((-1)**k,2*k+1)*powp(B,2*k+1)[5-k]
C=s.factor(2*coef_half) # c_phi,11(j)=j*C
print("c_phi_11(j) = j * (",s.collect(C,pi),")")
targets={s.Rational(1,2):s.Float('-8.57096738162e-8',30),s.Integer(1):s.Float('-1.71419347632e-7',30),s.Rational(3,2):s.Float('-2.57129021449e-7',30)}
for jj,t in targets.items():
    v=s.N(jj*C,30)
    print(jj,v,t,s.N(v-t,16))
