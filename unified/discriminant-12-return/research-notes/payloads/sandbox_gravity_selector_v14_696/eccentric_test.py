"""Eccentric phase integration (2026-10-22, Jeremy's line): squash the
Larmor orbit by the Kepler factor rho = sqrt((1-e)/(1+e)) in Test D's
integral I_jm = (1/2pi) int e^{-im chi} (cos th + i rho sin th cos chi)^j.
At e=0 the v14.680 constants (1, 1/2, 1, 1/3, 1/12) reproduce exactly.
At e=0.6 the ratio |I|/|P_j^m(cos th_ecc)| is theta-DEPENDENT
(0.64-0.99 for j=1,m=0): eccentricity is a genuine deformation of the
harmonic family, not an angle reparametrization."""
