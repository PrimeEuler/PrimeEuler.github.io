# Finite-cutoff divisor anomaly and AM–GM central-seat response test

Date 2026-10-25. Gravity arithmetic side lane. Parents v13.177, v14.767, v14.856. No Suzuki/far-tail modifications.

## Arithmetic [D]
Let \(D(N)=\sum_{k\le N}d(k)=\sum_{a=1}^{N}\lfloor N/a\rfloor\) and \(T(N)=N(N+1)/2,\ A(N)=T(N)-D(N)\). Then \(T-A+D=2D\). For positive integer n, comparing u=1 and u=1/2 at the SAME unscaled physical product cutoff n gives respective cumulative contact counts D(n) and D(4n).

Define
\[
\Delta_4(n):=D(4n)-4D(n)=\sum_{a\le4n}\lfloor4n/a\rfloor-4\sum_{a\le n}\lfloor n/a\rfloor.
\]
From the classical divisor-summatory asymptotic \(D(X)=X\log X+(2\gamma_E-1)X+O(\sqrt X)\),
\[
\boxed{\Delta_4(n)=4n\log4+O(\sqrt n),\quad
\Delta_4(n)/(4D(n))\sim(\log4)/(\log n).}
\]
Exact numerical checks: n=12: D=35, D(48)=198, delta=58; n=25: D=87, D(100)=482, delta=134; n=100: D=482, D(400)=2468, delta=540; n=1000: D=7069, D(4000)=33805, delta=5529. The additive anomaly grows while its relative contribution decays logarithmically.

## Explicit conditional contact energy [I/D]
The AM–GM central-seat shape from v14.856 is \(f(\xi)=1-\sqrt{1-\xi²}\), \(\xi=\delta/u\), whose normalized second derivative at 0 equals one. Consider a *declared*, testable equal-contact toy prescription in which each lattice contact below a fixed unscaled product cutoff N carries identical positive energy ε and contributes the same shape f:
\[
E_{u,N}(\delta)=\varepsilon D(\lfloor N/u²\rfloor)f(\delta/u).
\]
At u=1 and u=1/2 with integer N=n this yields
\[
k_{1,n}=\varepsilon D(n),\qquad k_{1/2,n}=4\varepsilon D(4n)
\]
in the common coordinate δ, hence \(k_{1/2}/k_1=4D(4n)/D(n)\). The *factor 4* is displacement-coordinate rescaling: in common normalized ξ each contact contributes the same unit curvature and the normalized stiffness ratio is \(D(4n)/D(n)=4+\Delta_4(n)/D(n)\). If instead energy per contact is normalized by contact count, E=E_*f(ξ), the entire difference vanishes. Thus neither prescription is selected by arithmetic alone; and absolute or relative stiffness needs consistent physical dimension normalization.

A cleaner comparison isolates the anomaly relative to the naive fourfold contact increase:
\[
\mathcal A(n)=\frac{D(4n)}{4D(n)}-1=\frac{\Delta_4(n)}{4D(n)},
\]
which tends to zero but is generally nonzero at finite n. This is arithmetic observable, NOT a Newton coupling prediction or a derived physical force.

## Next falsifiable test [O]
Construct a local/causal action assigning a weight to EACH actual divisor-hyperbola contact, with geometric measure and a physically fixed cutoff, and derive rather than assume its seat coupling ε. Compare invariance under common grid rescaling with a calibrated physical ruler. Respect v13.770 arithmetic-carrier distinction.
