# Augmented Lorentzian polynomial versus exact divisor-mask extraction

2026-10-24. Combinatorics/gravity lane, parents v14.807–811. No Suzuki or far-tail changes.

## Gate I. Exact coefficient-aware ambient recovery [D]

For N>=1 let H=N-1 and define the homogeneous Lorentzian polynomial
\[
P_N(X,Y,Z)=XY(X+Y+Z)^H.
\]
Write the support term for a,b>=1, a+b<=N+1 as \(X^aY^bZ^{N+1-a-b}\). Its coefficient is
\[
c_{a,b}=\frac{(N-1)!}{(a-1)!(b-1)!(N+1-a-b)!}>0.
\]
Define the unique-digit encoder
\[
p_N(t)=P_N(t,t^{N+2},1)
=\sum_{a,b}c_{a,b}t^{a+(N+2)b}.
\]
Since 1<=a<=N and 1<=b<=N, the exponents \(a+(N+2)b\) are pairwise distinct. Then the exact arithmetic functional
\[
\mathcal D_N[p_N]=\sum_{\substack{a,b>=1\\ ab<=N}}
\frac{[t^{a+(N+2)b}]p_N(t)}{c_{a,b}}
\]
equals the unweighted cumulative divisor count \(D(N)\). The indicator is carried by an explicit coefficient-selection functional, NOT intrinsic to the ambient Lorentzian polynomial. This is a faithful encoded bookkeeping method, not a claimed Lorentzian divisor frontier.

## Gate II. No-go for a Lorentzian marker slice [D]

Suppose a homogeneous Lorentzian polynomial F(X,Y,Z,T) of nonnegative coefficients has one coefficient slice in T equal to the exact cumulative frontier \(C_N(X,Y,Z)\) (up to a positive scalar), namely
\[
[T^k]F(X,Y,Z,T)=c\,C_N(X,Y,Z),\quad c>0.
\]
But taking a partial derivative \(\partial_T^k F\) preserves the Lorentzian class (when nonzero), as does restricting \(T=0\) by specialization/limits. Thus the left side is Lorentzian (up to the factor k!), whereas C_N is not Lorentzian for N>=3 by v14.811. Contradiction. More auxiliary variables and derivatives followed by specialization cannot evade the same closure obstruction when the extracted target is exactly C_N and the ambient polynomial is homogeneous Lorentzian.

This prevents a particularly natural proposal: hiding an otherwise non-M-convex fixed/cumulative divisor shell as a *single marker-variable coefficient* of a genuine positive Lorentzian polynomial. General signed linear combinations or non-Lorentzian projection operators can reproduce the count, but need not preserve the Lorentzian class; the ambient structure then does not yield a new arithmetic Lorentzian theorem.

## Next question [O]

Seek an intrinsically meaningful observable derived from the Lorentzian ambient (e.g., stable derivatives, averaged marginal, or a source-response), which correlates nontrivially with divisor counts without asserting exact support preservation. Explicitly state which postprocessing operations break closure. No claims about GR metric or G.
