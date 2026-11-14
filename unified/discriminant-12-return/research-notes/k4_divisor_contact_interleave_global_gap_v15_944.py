#!/usr/bin/env python3
"""v15.944: genuine divisor-contact sums of hyperbola interleaving curvature.
Arithmetic and geometry only; no gravitational dynamics or Casimir operator match.
"""
import sympy as s
n,k=s.symbols('n k',positive=True)
D=lambda t:t+n/t
X=lambda t:(n-t*t)/(2*t)
delta=s.factor(X(k+s.Rational(1,2))-(X(k)+X(k+1))/2)
assert s.simplify(delta+n/(4*k*(k+1)*(2*k+1)))==0
assert s.simplify((n+1)-D(k)-(k-1)*(n-k)/k)==0
assert s.apart(1/(k*(k+1)*(2*k+1)),k)==1/k+1/(k+1)-4/(2*k+1)
def divisors(nn):return s.divisors(nn)
def offset(nn,kk):return delta.subs({n:nn,k:kk})
def norm_sum(nn):
    return sum((-4*kk*(kk+1)*(2*kk+1)*offset(nn,kk)
                for kk in divisors(nn)),s.Integer(0))
def raw_sum(nn):
    return sum((offset(nn,kk) for kk in divisors(nn)),s.Integer(0))
def diameter_gap(nn):
    return sum(((nn+1)-(kk+nn//kk) for kk in divisors(nn)),s.Integer(0))
def cutoff_raw(N):
    return sum((raw_sum(nn) for nn in range(1,N+1)),s.Integer(0))
def cutoff_swapped(N):
    return -sum((s.Rational((N//kk)*(N//kk+1),8*(kk+1)*(2*kk+1))
                 for kk in range(1,N+1)),s.Integer(0))
for nn in range(1,1001):
    div=divisors(nn)
    assert norm_sum(nn)==nn*len(div)
    assert diameter_gap(nn)==(nn+1)*s.divisor_count(nn)-2*s.divisor_sigma(nn,1)
    assert (diameter_gap(nn)==0)==(nn==1 or s.isprime(nn))
    assert raw_sum(nn)==-s.Rational(nn,4)*sum(
        (s.Rational(1,kk*(kk+1)*(2*kk+1)) for kk in div),s.Integer(0))
    assert raw_sum(nn)<0
for NN in (1,2,4,10,20,50,100):
    assert cutoff_raw(NN)==cutoff_swapped(NN)
for nn in (1,2,3,4,6,8,9,12,16,24,36,60):
    print('n',nn,'d',s.divisor_count(nn),'sigma',s.divisor_sigma(nn,1),
          'diam_gap',diameter_gap(nn),'raw_offset',raw_sum(nn))
print('PASS: n 1..1000: weighted count, raw sum, diameter gap, primality, cutoff rearrangement')
