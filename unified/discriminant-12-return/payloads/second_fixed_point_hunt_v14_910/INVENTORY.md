# Second-fixed-point hunt - inventory (auditor rec. point 1, 2026-10-26)

Weld rule to stress-test: a dictionary scale is fixed by matching the
lattice of the quantity it counts (h = 2q from the offset lattice).
Need: a number NOT used in building the rule, predicted by it.

## Quarters on the books (lanes themselves distinguish them)
- Q1 Casimir completion: (j+1/2)^2 - j(j+1) = 1/4 (v14.859, v13.595).
  Lane's own warning: NOT to be conflated with the u=1/2 factor grid.
- Q2 pair-product quantum q_G = 1/4 (dyon, v14.731) -> grid c = 4 (weld v14.904).
- Q3 Maslov action quarter (n - 1/4), bouncer (v14.592). Additive shift.

## Seat-thread inventory (partial)
- v14.856 [D]: parabolas at scale u, vertices -+u/2, seat (0,u);
  stiffness ratio between grids NOT universal (depends on chosen
  A(u)); normalized curvature identical (=1 both grids).
  Flag: normalized_sector_difference=NONE. => pure geometry does
  not select u; the weld's node=state premise is the extra input.
- v14.857 [D]: fourfold divisor anomaly Delta_4(n) = D(4n) - 4D(n)
  = 4n log 4 + O(sqrt n); relative anomaly ~ log4/log n -> 0.
  Downstream consequence of c=4, not an independent fixed point.
  Contact-weighted stiffness conditional [I/O].
- v14.859 [D]: transverse weight j(j+1) - m^2 = ab - (a+b)/2 under
  contact labels j=(a+b-2)/2, m=(a-b)/2 (pair sum/difference =
  seat coordinates again). W_perp(12) = 44 exact vs full Casimir
  weight 113 (v14.858). Contact->energy identification OPEN.

## Still to read
v14.858 (Schwinger J-weighted seat), v14.862 (two-vector modes,
exchange coupling lambda - auditor point 2 target), v14.870
(EM inertia shared seat), v14.863/864 (seat angle map / spin-0
Higgs seat), kernel entries v14.867-881, 896 (free params
g, R, a, Omega, kappa_s, mu_s - point 2 inventory).

## Seat-thread inventory (batch 2)
- v14.858 [D/I]: contacts (a,b) <-> Schwinger j=(a+b-2)/2, m=(a-b)/2
  via occupations (n1,n2)=(a-1,b-1). The per-member offset -1 is
  CONVENTIONAL (flag: EXACT_CONVENTIONAL_OFFSET;
  physical_contact_quantization=UNPROVED). W2(12)=113 exact.
  Weld-relevant: the (1,1) contact = j=0,m=0 = the unit pair /
  counting start of this dictionary too. Open in entry: W2
  asymptotics + correct 4n-vs-n normalisation (a place where the
  weld's c=4 could be TESTED: does W2(4n) vs 4W2(n) have the
  divisor-anomaly form or a different leading power? Casimir
  weighting changes scaling - a real second-fixed-point arena).
- v14.862 [D conditional]: exchange H=-lambda J1.J2 POSTULATED
  (bicone_coupling_derived=NO). E_L=-lambda[L(L+1)-2j(j+1)]/2;
  j=1/2: triplet -lambda/4, singlet +3 lambda/4 (pure SU(2)
  Casimir arithmetic - Q1-type quarters, NOT the pair-product
  quarter). Free params here: lambda (energy scale, postulated),
  Omega (drive), g (differential coupling). Auditor point 2 asks
  to pin lambda from the dyon side; dyon data are dimensionless
  lattice numbers, so a bridge needs an energy scale from the
  seat (Omega? Larmor?) - none pair-shaped so far. HONEST: no
  bridge candidate yet.
- v14.870 [I/D]: EM dipole at the seat: Coulomb curvature
  NEGATIVE (bare dipole does not stabilise); shared-seat EM/G
  equivalence UNPROVEN; next gate = Maxwell effective kernel
  from bicone Larmor geometry (= Chat's running kernel thread).

## Still to read
v14.863/864, kernel run v14.867-869, v14.871-881, v14.896
(free-parameter census for auditor point 2: g, R, a, Omega,
kappa_s, mu_s).

## Batch 3 (kernel census, 2026-10-26)
- v14.873/877: kernel coupling g = 2qR/u (q = blob CHARGE here,
  R orbit radius, u seat scale); curvature k_C = g^2/(24 pi^1.5
  eps0 a^3) > 0 for the OVERLAPPING-blob source (contrast
  v14.870's separated dipole, negative). Source POSTULATED.
- v14.896: support/pole structure numerically verified (audit
  v14.885 of sandbox v14.884); source_support_dynamics still
  POSTULATED; G_Higgs NOT_DERIVED.
- Free continuous parameters across the kernel thread: charge q,
  blob size a, orbit R, drive Omega, susceptibilities kappa_s,
  mu_s; plus v14.862's lambda, Omega, g_diff. NONE is a lattice
  or counting quantity -> offset-lattice matching has no grip.
  Only contact: the seat scale u (dictionary scale; weld forces
  u = 1/2 at the gravity seat - already the thread's choice).
- CONCLUSION: see NOTE.md - no independent second fixed point
  in the current record; W2 gate closed by computation
  (zeta(3)/6 law, normalization 64); two standing predictions
  P1 (k-factor scale) and P2 (W2 cutoff) extracted.
