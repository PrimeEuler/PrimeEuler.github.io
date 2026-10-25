# Divisor contacts as Schwinger angular momentum labels: energy-weighted seat test

2026-10-25. Gravity/divisor side lane. Parents v14.366–367, v14.620, v14.626, v14.856–857, and unified/Bath_Note.tex. Suzuki and far-tail untouched.

## Exact bookkeeping conditional on occupation assignment [D/I]
For integer pair a,b>=1, define boson occupation numbers n_1=a-1, n_2=b-1. The Schwinger two-oscillator dictionary then defines
\[
j(a,b)=(n_1+n_2)/2=(a+b-2)/2,\quad
m(a,b)=(n_1-n_2)/2=(a-b)/2,\quad |m|\le j.
\]
This is an EXACT mapping once the occupation-offset choice is fixed; it is NOT a theorem that each geometric divisor contact is an independently excited physical angular-momentum state. The unit-circle contact associated to (a,b) has
\[
z_{a,b}=(a-b+2i\sqrt{ab})/(a+b),\quad |z_{a,b}|=1.
\]
The unit-circle position depends only on a/b and is invariant under (a,b)->(ha,hb). The j-occupation assignment relies on integer labels a,b and must not automatically be recomputed from fractional physical x=ha,y=hb.

At fixed product N, distinct contacts can share j and differ in m; the multiplicity d(N) does not count independent j *levels*. Example N=12 gives ordered pairs (1,12),(2,6),(3,4),(4,3),(6,2),(12,1), with respective (j,m)=(11/2,-11/2),(3,-2),(5/2,-1/2),(5/2,1/2),(3,2),(11/2,11/2).

## Candidate rotor-weighted arithmetic moment [D/I]
Define
\[
W_2(N)=\sum_{ab\le N}j(a,b)(j(a,b)+1),\qquad
w_2(N)=\sum_{ab=N}j(a,b)(j(a,b)+1).
\]
These are exact finite arithmetic sums under the declared labeling. The shell N=12 yields \(w_2(12)=2(143/4+12+35/4)=113\). If a freely rotating body with moment of inertia I is independently attached to each contact, one might assign energy \(E_j=\hbar^2 j(j+1)/(2I)\). But selecting this spectrum and the moment of inertia I is NEW physical input; ħ alone is a quantum of action, not an energy-per-contact rule. The earlier rotor v14.626 exhibits j(j+1) in its free ladder, while the pendulum perturbation mixes j levels.

For a shared unscaled physical product cutoff N=n, the proposed half-grid u=1/2 samples contact set ab<=4n and unit grid u=1 samples ab<=n. Thus the weighted discrepancy
\[
\Delta_{4,W}(n)=W_2(4n)-4W_2(n)
\]
is an exact new arithmetic observable but NOT a physical stiffness or a universal normalized coupling. As opposed to D(N), W_2(N) weights large a+b heavily; a fourfold baseline may not capture its leading scaling. Before using a normalized anomaly, derive the appropriate asymptotic leading scale. A genuine seat energy would additionally require a specified operator coupling the angular-momentum sector to seat displacement, not simply E_j f(δ/u).

## Falsifiable next steps [O]
Compute W_2 exactly and its leading growth; test which matrix elements of the seat-balance operator (e.g. rank-1 cos θ or rank-2 anisotropy) are allowed by selection rules and whether their second-order ground-state response determines a seat stiffness. Audit separation between quantum state bookkeeping and physically independent contact modes. No Newton G or EM/G hierarchy derived.
