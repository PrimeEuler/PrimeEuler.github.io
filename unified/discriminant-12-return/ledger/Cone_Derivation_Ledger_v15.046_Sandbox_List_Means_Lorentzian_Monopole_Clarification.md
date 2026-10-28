# Ledger v15.046 — Sandbox clarification: list AM–GM, the Lorentzian n+1 (the "1" is the list sum), monopole = dimension 1

**Lane:** Sandbox (little Euler), on Jeremy's clarification and
identification of 2026-10-28. **Parents:** v15.008 (ladder),
v14.949/950 (p_s boost), v14.988/v14.992/v15.014 (charge negatives),
v14.731/v14.913 (quarter's derivation order), v14.916 (PARK).
**Payload:** `payloads/list_means_clarification_v15_046/`
(NOTE.md + list_means.py; all identities machine-checked).

## Content (details in payload NOTE)

**List pictures [D].** For a list of n numbers: cos(angle to the
diagonal) = A/Q exactly; distance to diagonal = sqrt(n)·std
(variance is radial distance); sphere through the list-point has
radius sqrt(n) Q; ellipsoid volume V_n(1) G^n (G = equal-volume
ball radius); AM–GM = ellipsoid/ball(A) = (G/A)^n. No
product-equals-ball-volume identity exists (pi transcendental);
the chord picture is pair-only — lists aggregate by volume.

**Lorentzian n+1 (Jeremy) [D].** (t; x) in R^{1,n}, t = sqrt(n) A
— the "1" is the list sum; t^2 − |x|^2 = −n(Q^2 − A^2) <= 0: lists
timelike-or-null, light cone = equality locus, norm = −variance.
Pair form: u, v null coordinates; G^2 = uv = T^2 − X^2 (interval);
s = boost rapidity; crossing matrix [[u, Y],[Y, v]] null, trace =
the sum, rank-1 = chi chi^T. Quadratic forms see (A, Q) exactly;
G is degree-n (det), quadratic only at n = 2.

**Content ladder [D].** AM–GM = (tr/n)^n >= det: sum^dimension
bounds content G^n — length (1), area (2, = the interval), volume
(3), n-content; G always the equal-content cube's side.

**Monopole = dimension 1 (Jeremy) [I, exact backing].** Multipole
p_0 = list sum = the Lorentzian "1". Pair has exactly two moments
(2T monopole, 2X dipole; p_2 = p_0); bicone = dipole's shape,
monopole one cone; list of 1 = monopole-only = the 1st AM–GM
dimension; seat is monopole-only (p_1 = 0); vertex kills G,
leaving the sum.

**Gravity flags:** selector=NO_NEW_LEVERAGE (amplitude multiplies
a dimension-1 sum, which has no internal structure to derive a
number from); charge_negatives=UNIFIED [I] (k4 background is a
pure-monopole configuration; v14.988/992 and v15.014 negatives are
one fact — dimension-2 data cannot live on a dimension-1
background); amplitude_pointer=PAIR_DATA_ONLY [I, heuristic];
quarter order in the record is monopole-first (v14.731);
Suzuki_quarter=PARKED (unchanged — the pointer names the door,
it does not open it); Pantheon=UNTOUCHED; G_derived=false.

## Handoffs

→ **external-audit:** verification of the payload identities.
→ **gravity lane:** no action requested; the monopole/dimension
vocabulary and the charge-negative compression are offered for
the record.
