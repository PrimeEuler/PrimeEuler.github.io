# Cone Derivation Ledger v14.812 — Lorentzian ambient with exact divisor coefficient recovery

Date 2026-10-24. Parents v14.807–811. Research note research-notes/Augmented_Lorentzian_Divisor_Marker_Extraction_NoGo.md commit d1c27199bb31902b7087fa1869d588dc6c099c20. Prewrite expected HEAD d1c27199bb31902b7087fa1869d588dc6c099c20. Gravity/combinatorics; Suzuki/far-tail untouched.

For N>=1 set \(P_N=XY(X+Y+Z)^{N-1}\). This is a homogeneous Lorentzian polynomial; coefficient at \((a,b,N+1-a-b)\) is \(c_{a,b}=(N-1)!/[(a-1)!(b-1)!(N+1-a-b)!]\). The univariate code \(p_N(t)=P_N(t,t^{N+2},1)\) assigns distinct exponents \(a+(N+2)b\) to each pair in the translated simplex. Hence
\[
\boxed{D(N)=\sum_{ab\le N}\frac{[t^{a+(N+2)b}]p_N(t)}{c_{a,b}}}.
\]
This is exact contact bookkeeping with a separately defined arithmetic coefficient mask; it does not make the factor-frontier polynomial Lorentzian or turn divisor arithmetic into Suzuki/Weil trace.

NEXT: test which more intrinsic extraction operations preserve Lorentzian properties. External audit handoff: verify exponent uniqueness and coefficients; no Suzuki production changes.