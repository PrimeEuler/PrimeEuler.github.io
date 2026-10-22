# Drift coefficients — sandbox return to the v14.708 HANDOFF (2026-10-22)

Producer: drift_coefficients.py (sympy; re-run clean after deposit edits).

DERIVATION (from the deposited EFT v3.4, no hand-fit): the hot-limit
generator on (h, L) — A_h = 3 D0 (energy drift of isotropic diffusion),
C_hh = 2 D0 v^2, C_hL = 2 D0 L, A_L = D0 r^2/L (Ito curvature of
L = |r x v|) — applied to s = 1 - q and time-averaged with the exact
Kepler averages <v^2> = mu/T, <r^2> = (T^2/2)(5 - 3q^2), L^2 = mu T q^2,
h = -mu/2T, assembles EXACTLY to the draft's boxed result:
  <Ls> = (5 D0 T / 2 mu q)(3q^2 - 1),   zero q0^2 = 1/3, e0^2 = 2/3.

ATTRIBUTION of the numerator 15q^2 - 5 (units T/(2 mu q^2)):
  energy drift + cross-covariance (s_h A_h + C_hL s_hL): +10 q^2
  energy Ito term (1/2 C_hh s_hh via <v^2>):               +2 q^2
  L-curvature drift (s_L A_L via <r^2>):              -5 + 3 q^2
The -5 (the "-1" of (3q^2-1)) comes entirely from the constant part
of <r^2> through the L-curvature channel; the 15 mixes all three.

SECOND ROUTE (independent): Hamilton-Modak A_eps = C(1-2eps),
D_eps = 2C eps(1-eps); Ito to s = 1 - sqrt(1-eps) gives
A_s = (C/4q)(3q^2-1) symbolically; with C = (5T/3mu)*<|dv|^2>/dt
= 10 D0 T/mu the ABSOLUTE coefficient is identical. The (3q^2-1)
is derived twice over, not fit.

PERTURBATIONS (channel weights, physically motivated stand-ins for
distribution changes): L-channel x1.5 -> q^2 = 5/11 (e^2 = 0.5455);
L-channel x0.5 -> q^2 = 5/27 (e^2 = 0.8148); energy channels x1.25
-> q^2 = 5/18 (e^2 = 0.7222). The zero moves CONTINUOUSLY: the 3:1
ratio is a property of the Maxwellian hot limit's channel balance,
not protected by cone geometry (concurring with v14.708's general-
drift point, e^2 = 1 - b/a). The draft's own stronger perturbations
agree: finite temperature moves the zero along F_s(q, Theta) = 0 to
the fold (0.59619, 0.32464) [draft numerics]; the planar sector has
a different response structure entirely.

XI TEST: NEGATIVE. The bath drift is a stochastic process on a
Kepler orbit's (h, L); Xi (v14.700) is the static rank-1/rank-2
response of a rotor to an external Phi', Phi''. No derived bath term
enters beta1 or beta2; source granularity would add measurement
noise (v14.702 budget), not a mean-response correction. No
independently derived interaction alters Xi beyond standard
gradiometry. G_derived = false.
