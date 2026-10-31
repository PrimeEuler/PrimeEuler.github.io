# Ledger v15.230 — Sandbox return: TN trajectory cone [D]; apex bookkeeping; null-scale cross-ratio catalog

**Kind:** Sandbox return. §1 is a [D] verification; §2 is
bookkeeping with empirical inputs; §3 is a tagged catalog (no
derivations claimed).
**Origin:** Jeremy (2026-10-31): "lets hit the TN trajectory cone
and the apex bookkeeping — then look at the temptation and
cross-ratios among the null scales."
**Producers:** `tn_cone_test.py` (full TN geodesic integration),
`null_scales.py` (constants and ratios). Clean exits.
**Payload:** `payloads/tn_cone_null_scales_v15_230/` — TN_CONE.md,
tn_cone_test.py, tn_cone_output.txt, NULL_SCALES.md,
null_scales.py, null_scales_output.txt.

## 1. The TN trajectory cone [D]
Extends v15.229 (MIC) to the gravitational sector. Along true
Taub–NUT geodesics — Hamilton flow of H = (1/2) g^mn p_m p_n built
from the record's inverse metric (tn_hj_from_metric.py), m = 1,
eps = 0.92, RK4 in proper time — the record's charge vector
(J = pth ph_hat − (Pi/sin th) th_hat − s n_hat, Pi = k + s cos th,
**s = 2 l eps**) is conserved as a vector (worst |dJ| ≤ 8.3e-13,
8 cases), J·n_hat = −s holds identically (≤ 6.7e-16), and the
trajectory is confined to the cone cos(alpha) = s/|J| (angle
constant to 4.4e-16). Openings agree with the MIC table at equal
(s, |J|) to all printed digits (60.0000, 75.5225, 62.6883,
52.2388, 90 control; new point 30.0000 at s = 3/2, j = 1/2):
TN−MIC purely radial, now in trajectory space.
**The quarter's trajectory-level location:** the cone sees the
PAIRED charge 2 l eps; the parabolic seats sit at k/2 −/+ eps l,
so the seat offset is half the cone's s. A single trajectory
measures the pair; the quarter lives in the seat split and the
pair product (k/4)^2 (v14.731).

## 2. Apex bookkeeping: −1/2, 0, +1/2
Identity: GM/(R_H c^2) = Omega/2 exactly at R_H = c/H0 — H0 cancels
— so the Sciama balance with Planck 2018 inputs
(Omega_K = 0.0007 −/+ 0.0019) is **B = 0.4996 −/+ 0.0009**. B is
H0-independent (the Hubble tension moves R_H, 14.52 vs 13.39 Gly,
and M_H; it cannot move B). Geometric face: r_s(M_H) = Omega R_H;
at Omega = 1 the Hubble sphere sits at its own Schwarzschild
radius. Provenance: seat −1/2 [D, cone geometry]; cosmic +1/2
[empirical — Sciama's Machian reading would make it an identity
by defining G from the inventory; LCDM leaves it an initial
condition]; apex 0 [the arithmetic sum; no dynamics on record
performs the cancellation, and nothing identifies the two 1/2's].
The account is consistent and the apex remains open, now with
error bars.

## 3. Cross-ratio catalog of the null scales (tagged, not derived)
Producer-computed; headline rows (full table in the payload):
- c^2/g = 0.9687 ly and c/g = 0.9687 yr: ONE coincidence in two
  costumes (they differ by the edge factor c).
- a0/(cH0/2pi) = 1.15 (Planck H0) / 1.06 (SH0ES): the MOND
  coincidence — order-unity, and 10%-level H0-sensitive, which no
  derived identity would be.
- Log-depths ln(a_P/g) = 116.87, ln(a_P/a0) = 141.99,
  ln(R_H/l_P) = 140.30: NONE lands on the Dirac depth
  psi = 45.310004305 or 2 psi = 90.62. Checked, negative.
- Trap defused: ln(T_CMB/T_U(g)) = 45.67 sits near psi and is
  meaningless as a candidate identity — T_CMB is an epoch reading,
  not a constant; it sweeps all values as the universe cools.
Discipline recorded with the catalog: every row is an entry in a
map of where a selector would have to live, not a derivation; no
mechanism on record connects any pair of null scales.

## Scope
§1 upgrades the cone theorem to both sectors of the dyon pair.
§2–§3 change no gate and no classification entry (v15.069 stands;
G_derived = false). The selector wall (v14.621) is restated by §3
in its sharpest form yet: the null scales' depths are ~117–142 in
log, the Dirac depth is 45.31, and nothing on record bridges them.
