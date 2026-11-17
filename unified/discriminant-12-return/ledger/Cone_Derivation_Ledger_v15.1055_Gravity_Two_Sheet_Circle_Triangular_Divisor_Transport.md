# Cone Derivation Ledger v15.1055 — Two-sheet arithmetic transport and signed-null floor obstruction

Date: 2026-11-16 (Eastern). Lane: Gravity/Cone. Status: [D] exact discrete circle pushforward and signed floor identity, [N] no sourced physics or quarter-boundary projector. Last checked live HEAD before script creation: 447fc4b7783dc0cffe958573a019694c0011e4bf; script added at 491e2424fd7560e69eeb2090b79b28d0fb86f98e. Additive only; no audit, Suzuki, sandbox, muse or foundational objects modified.

Prior work / redundancy: v13.197 proves continuous factor-plane staircase pushforwards, v13.199 proves the inverse weighted two-dimensional angular measure dx dy=2cos(theta)dX dY, v13.691 identifies the secant n/k and its floor count, canonical v15.1053 builds secant-to-circle projective compactification, v15.1054 reconciles a concurrent double-labeled ledger and explicitly derives two-sheet quotient. This gate does NOT claim discovery of a new estimator for D(n), and it distinguishes the one-dimensional atomic counting pushforward below from the earlier two-dimensional area Jacobian.

## Gate 858 — jointly transport the discrete triangle and divisor counting measures

For integer n>=1, A=(n+1)/2, and integer k=1,...,n, define the T-sector circle coordinate
x_k=A (k²-n)/(k²+n), y_k=2Ak sqrt(n)/(k²+n).
Then x_k²+y_k²=A², x_k increases strictly with k, and the inverse is k²=n(A+x_k)/(A-x_k). The sampled parabola intersections are distinct; no circle-grid sample labels are merged.

Define two atomic measures on the common semicircle:
mu_T=sum_{k=1}^n (n+1-k) delta_{(x_k,y_k)},
mu_D=sum_{k=1}^n floor(n/k) delta_{(x_k,y_k)}.
Their total masses are exactly mu_T(circle)=Triang(n)=n(n+1)/2 and mu_D(circle)=D(n)=sum floor(n/k). Moreover mu_T-mu_D is a nonnegative atomic measure: n+1-k-floor(n/k)>=0 since (k-1)(n-k)>=0. Its total mass is Triang(n)-D(n). The same base locations carry BOTH counts, but with different integer weights. For n=11 their masses are 66,29,37. Here 'atomic weight' means column count; it is not ordinary length, unweighted circle area or a physical energy density.

For any ordered sampled subset B, the same equality holds by restricting each sum to k whose circle points belong to B. Thus the entire *discrete* staircase is transported, not only its total number. This is simply the pushforward of labeled counting measures by an injective map on each sheet.

## Gate 859 — two-sheet lift and lost sign bit

For u=k>0 and |v|=n/k, sign epsilon=sgn(v), let R=sqrt(|uv|). On the T sheet epsilon=+1, define T=(u+|v|)/2,X=(u-|v|)/2 and circle (A X/T,A R/T). On the X sheet epsilon=-1 define T=(u-|v|)/2,X=(u+|v|)/2 and circle (A T/X,A R/X). Both yield the identical (x_k,y_k). The two-sheet carrier is (epsilon,x_k,y_k), and forgetting epsilon is a two-to-one quotient. The unsigned measures mu_T and mu_D push to the identical positions and weights on either sheet. They do NOT dynamically move or tunnel between sheets; choosing the signed reflection is an external identification, and the map is not a sourced time evolution.

The oriented positive factor n/k is T-X on the T sheet and X-T on the X sheet. More generally it is epsilon*(T-X). Therefore D(n)=sum floor(epsilon*(T-X)) on either physical sheet when the same discrete k labels are retained.

## Gate 860 — exact obstruction if orientation is forgotten

On the X sheet, blindly reusing the T-sheet null coordinate T-X produces -n/k. Integer floor does not commute with this sign flip:
floor(-n/k)=-floor(n/k)-1 if k does not divide n, and =-n/k if k divides n.
Writing d(n)=#{1<=k<=n: k divides n}, the wrong-orientation sum is
sum_{k=1}^n floor(-n/k)=-D(n)-(n-d(n)).
For n=11, d(11)=2, and the wrong-orientation count is -29-(11-2)=-38. This is NOT the ordinary D(n). The extra n-d(n) records precisely the number of nondivisor sample rows. The circle alone cannot choose the correct signed factor orientation without the sheet bit. This is an exact arithmetic manifestation of the v15.1054 two-to-one fold, not evidence of a new interaction or chirality.

## Gate 861 — guardrails / next physical test

The v13.199 inverse angular Jacobian 2cos(theta) applies to a 2D continuous region under (u,v)->(X,R), and recovers ordinary factor-plane area from a weighted planar image. Present delta-measures are a distinct 1D *discrete row* pushforward under fixed-n radial normalization; using that Jacobian directly for atomic weights would be incorrect. The equally spaced n+1 circle ladder has nonuniform k_j=sqrt(n j/(n+1-j)), so the lattice rows and equally spaced circle samples are not identical except at special locations.

Testing n=1..200 with exact Python Fraction rational arithmetic passed: monotonic/invertible x_k, triangle/divisor/complement totals, nonnegative row difference, and signed-floor correction; n=11 totals verified. Script: research-notes/k4_signed_circle_discrete_counts_v15_1055.py (commit 491e2424fd7560e69eeb2090b79b28d0fb86f98e). Independent Audit pending.

Bottom line: The shared circle carries the full positive triangular/divisor staircase as weighted discrete samples on BOTH signed sheets. The quotient forgets one sign bit, which must be supplied to recover oriented null-coordinate arithmetic. No rank-two open-quarter boundary projection, dynamical sheet mixing, selected frequency, G-free constant or GR/Maxwell-distinguishable observable arises from this bookkeeping. A future source-first gate could search for a physically derived operator on the doubled circle whose action is defined independently of these row weights and whose matrix elements match v15.602's rank-two q2 boundary operator without postselection.
