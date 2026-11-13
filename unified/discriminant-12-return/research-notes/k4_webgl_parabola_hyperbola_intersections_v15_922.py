#!/usr/bin/env python3
"""Gravity v15.922: exact intersections of legacy WebGL factor parabolas
Y²=(k/t)²+2(k/t)X and hyperbola T²-X²=N, Y²=N.
The code's original cone uses scale u=1/t; hyperbola Y=sqrt(N) is
NOT divided by t. Restrict k to divisors of N*t² for integer pair points.
"""
import math
import sympy as s
N,k,t,X=s.symbols("N k t X",positive=True)
b=k/t
x=s.simplify((N-b*b)/(2*b))
height=s.sqrt(N)
T=s.simplify((N+b*b)/(2*b))
a=s.simplify(N/b)
assert s.simplify(x-(a-b)/2)==0
assert s.simplify(T-(a+b)/2)==0
assert s.simplify(T*T-x*x-N)==0
assert s.simplify(b*b+2*b*x-N)==0
assert s.simplify(b*b-2*b*(-x)-N)==0
for n0 in [1,4,12,16,25,36]:
    for t0 in [1,2,3]:
        P=n0*t0*t0
        divisor_pairs=[]
        points=[]
        for k0 in range(1, math.isqrt(P)+1):
            if P%k0: continue
            a0=P//k0
            # Physical scale u=1/t0, hence b=k0/t0,
            # a=a0/t0, yielding product N.
            X0=s.Rational(a0-k0,2*t0)
            T0=s.Rational(a0+k0,2*t0)
            assert T0*T0-X0*X0==n0
            divisor_pairs.append((a0,k0))
            points.extend([X0] if a0==k0 else [X0,-X0])
        assert len(points)==int(s.divisor_count(P))
        assert len(set(points))==len(points)
        if n0==12 and t0==1:
            assert divisor_pairs==[(12,1),(6,2),(4,3)]
            assert sorted(points)==[-s.Rational(11,2),-2,-s.Rational(1,2),s.Rational(1,2),2,s.Rational(11,2)]
        print(f'N={n0}, t={t0}: integer-lattice mirrored intersections={len(points)} = d({P}); positive row pairs={divisor_pairs}')
print('PASS: exact unscaled and t-scaled intersections, doubled ± branches, square-seat nonduplication, d(N*t²)')
