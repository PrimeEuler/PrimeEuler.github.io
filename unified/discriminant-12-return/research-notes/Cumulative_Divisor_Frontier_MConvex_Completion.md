# Cumulative divisor frontier: M-convex obstruction and completion

Date 2026-10-24. Parents v14.807–810. Gravity/combinatorics lane; Suzuki work untouched.

## Cumulative homogeneous polynomial [D]
For N>=1 define
\[
C_N(X,Y,Z)=\sum_{a,b\ge1,\ ab\le N}X^aY^bZ^{N+1-a-b}.
\]
The exponent is nonnegative because a+b<=ab+1<=N+1. Coefficients are one per ordered factor pair, so \(C_N(1,1,1)=D(N)\), the exact cumulative divisor count.

For N>=3, its support contains \(\alpha=(1,N,0)\), \(\beta=(N,1,0)\). For the M-convex exchange from alpha in coordinate Y, beta offers a deficit in X only (their Z coordinates are equal), so the required exchange is \(\alpha-e_Y+e_X=(2,N-1,0)\). This would need \(2(N-1)\le N\), false for N>=3. Therefore support(C_N) is not M-convex and C_N is not Lorentzian for N>=3. The same argument works at ANY chosen common homogenizing degree M>=N+1: extreme points become (1,N,M-N-1), (N,1,M-N-1), same Z, and the required intermediate is missing.

## Minimal positive exceptions [D]
\(C_1=XY\) and \(C_2=XY(X+Y+Z)\) (at homogenization degree N+1). For N=2 the support is the three-point set \((1,1,1),(1,2,0),(2,1,0)\), which is M-convex; each first derivative is a quadratic with at most one positive Hessian eigenvalue, so C_2 is Lorentzian. N>=3 fails universally by support.

## M-convex completion and bookkeeping [D/O]
A simple superset of the factor-frontier support is the translated simplex
\[
S_N^{\rm full}=\{(a,b,N+1-a-b):a,b\ge1,\ a+b\le N+1\}.
\]
It is M-convex as the degree-(N-1) simplex shifted by (1,1,0). A Lorentzian positive-coefficient polynomial realizing it is
\[
P_N(X,Y,Z)=XY(X+Y+Z)^{N-1}.
\]
It is Lorentzian as a product of homogeneous real-stable linear factors with nonnegative coefficients (alternatively via standard Lorentzian closure under products). Its coefficients are multinomial rather than the unit coefficients of C_N.

The original divisor contact information is retained by an EXTERNAL mask
\[
m_N(a,b)=1_{\{ab\le N\}},
\]
and then \(D(N)=\sum_{a,b\ge1,\ a+b\le N+1}m_N(a,b)\). But P_N by itself does NOT encode those contacts. There is no established Lorentzian polynomial with positive support exactly the divisor frontier for N>=3. Completing the support inevitably includes additional product values; distinguishing original contact weights from fillers is a separate marked or multivariate problem.

## Next gate
Study Lorentzian or completely log-concave polynomials on an augmented variable space with a separate marker for product-shell membership, and determine whether exact coefficient extraction recovers D(N) without falsely asserting closure under truncation. Keep GR metric vs combinatorial Hessian distinct. No coupling prediction.
