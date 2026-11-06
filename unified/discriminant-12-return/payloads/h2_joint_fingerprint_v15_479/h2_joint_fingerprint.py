"""
H2 head-on: the joint fingerprint is over-determined
(2026-11-06, sandbox; door II's one remaining empirical
question after v15.478 merged H1 into H2).

The candidate digit-reader (charged-lepton masses) now
carries TWO target values in the same sector:
  Q = 2/3   (the cone's constant; v15.468, geometry v15.472)
  delta = 2/9 rad (the residual phase; v15.472, in-band)
with ONE imprecise input: m_tau = 1776.86 +- 0.12 MeV
(m_e, m_mu are exact for this purpose). Two equations,
one unknown -- the system is over-determined. This build
solves each equation separately for m_tau:
  m^(Q):     Q(m_tau) = 2/3
  m^(delta): delta(m_tau) = 2/9
If the roots disagree, the joint fingerprint is dead. If
they agree, it is a consistent over-determined story with
a sharp falsifiable prediction: refined m_tau measurements
must converge to the joint root; convergence elsewhere
kills both targets together.
SELECTION EFFECTS, stated first: delta's target 2/9 was
noticed BECAUSE the measured delta is 0.2222...; Q's target
is the cone's constant but Koide's relation is itself
famous for hitting it. The non-trivial content is only
the JOINT consistency: two independently-noticed near-
values, simultaneously satisfiable at one m_tau, deep
inside the measurement error. Grade stays COINCIDENCE;
what changes is that the coincidence now has a kill
condition and a precision horizon (sec. 2).

Also: the sector census completed to (theta, delta) with
candidates PRE-REGISTERED here before computation --
theta in {45 deg (seat), 54.7356 deg (single-axis)};
delta in {0, 2/9, pi/6, pi/4, 2/3} rad. Quark inputs are
the record's indicative running masses (v15.468):
up (2.16, 1270, 172690), down (4.67, 93.4, 4180) MeV.
"""
from mpmath import mp, mpf, sqrt as msqrt, findroot, pi as mpi
mp.dps = 50
me, mmu = mpf('0.51099895'), mpf('105.6583755')

def Q_of(mt):
    s = msqrt(me) + msqrt(mmu) + msqrt(mt)
    return (me + mmu + mt) / s**2
def delta_of(mt):
    s = [msqrt(me), msqrt(mmu), msqrt(mt)]
    W = sum(s[k] * mp.e ** (-2 * mpi * mp.j * k / 3) for k in range(3)) / 3
    return mp.atan2(mp.im(W), mp.re(W)) % (2 * mpi / 3)

print("=" * 76)
print("1. the two roots: does one m_tau satisfy both targets?")
print("=" * 76)
mQ = findroot(lambda x: Q_of(x) - mpf(2) / 3, mpf('1777'))
md = findroot(lambda x: delta_of(x) - mpf(2) / 9, mpf('1777'))
print(f"  m^(Q)     = {mp.nstr(mQ, 10)} MeV   (delta there = "
      f"{mp.nstr(delta_of(mQ), 9)}; 2/9 = {mp.nstr(mpf(2)/9, 9)})")
print(f"  m^(delta) = {mp.nstr(md, 10)} MeV   (Q there = "
      f"{mp.nstr(Q_of(md), 9)}; 2/3 = {mp.nstr(mpf(2)/3, 9)})")
print(f"  roots differ by {mp.nstr(abs(mQ - md), 4)} MeV; measured")
print(f"  m_tau = 1776.86 +- 0.12: roots sit "
      f"{mp.nstr((mQ - mpf('1776.86')) / mpf('0.12'), 4)} sigma and "
      f"{mp.nstr((md - mpf('1776.86')) / mpf('0.12'), 4)} sigma above central.")

print()
print("=" * 76)
print("2. falsification horizon (sensitivities at the joint root)")
print("=" * 76)
h = mpf('0.001')
dQ = (Q_of(mQ + h) - Q_of(mQ - h)) / (2 * h)
dd = (delta_of(mQ + h) - delta_of(mQ - h)) / (2 * h)
print(f"  dQ/dm_tau = {mp.nstr(dQ, 4)} /MeV;  d(delta)/dm_tau = "
      f"{mp.nstr(dd, 4)} /MeV")
for sig in ('0.12', '0.05', '0.02'):
    s = mpf(sig)
    print(f"  sigma(m_tau) = {sig}: sigma_Q = {mp.nstr(abs(dQ) * s, 3)}, "
          f"sigma_delta = {mp.nstr(abs(dd) * s, 3)} -- if the central")
    print(f"      value stayed at 1776.86, Q would miss 2/3 by "
          f"{mp.nstr(abs(Q_of(mpf('1776.86')) - mpf(2)/3) / (abs(dQ) * s), 3)} sigma_Q.")
print("  the joint fingerprint is decidable at sigma(m_tau) ~")
print("  0.02-0.03 MeV -- roughly a 5x improvement, the scale")
print("  tau-factory programs aim at. Until then it stands as a")
print("  consistent over-determined coincidence with a stated")
print("  kill condition: m_tau converging outside ~1776.97 +- 0.03")
print("  (with errors that small) kills both targets together.")

print()
print("=" * 76)
print("3. sector census (theta, delta), pre-registered candidates")
print("=" * 76)
import math
def census(m1, m2, m3):
    s = [math.sqrt(m1), math.sqrt(m2), math.sqrt(m3)]
    Q = (m1 + m2 + m3) / sum(s) ** 2
    th = math.degrees(math.acos(1 / math.sqrt(3 * Q)))
    import cmath
    W = sum(s[k] * cmath.exp(-2j * math.pi * k / 3) for k in range(3)) / 3
    de = math.atan2(W.imag, W.real) % (2 * math.pi / 3)
    return Q, th, de
cands_d = {'0': 0.0, '2/9': 2 / 9, 'pi/6': math.pi / 6,
           'pi/4': math.pi / 4, '2/3': 2 / 3}
for name, ms in (("charged leptons", (0.51099895, 105.6583755, 1776.86)),
                 ("up quarks      ", (2.16, 1270.0, 172690.0)),
                 ("down quarks    ", (4.67, 93.4, 4180.0))):
    Q, th, de = census(*ms)
    hit_th = "SEAT 45" if abs(th - 45) < 0.01 else (
        "axis 54.74" if abs(th - 54.7356) < 0.05 else "no target")
    hit_de = [k for k, v in cands_d.items() if abs(de - v) < 0.005]
    print(f"  {name}: Q = {Q:.6f}, theta = {th:8.4f} deg ({hit_th}), "
          f"delta = {de:.5f} rad (candidates hit: {hit_de or 'none'})")
print("  leptons alone sit on the seat angle, and alone carry a")
print("  candidate-hitting phase. The census closes the sector")
print("  map: the fingerprint is charged-lepton only in BOTH")
print("  coordinates (angle and phase), as the neutrino test")
print("  already showed in Q alone (v15.472).")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("H2 is neither discharged nor killed; it is now a")
print("PREDICTION. The joint fingerprint (Q = 2/3 and delta =")
print("2/9 in the charged-lepton masses) is over-determined")
print("and internally consistent: its two roots for m_tau")
print("agree with each other far inside the measurement error,")
print("at m_tau ~ 1776.97, +0.9 sigma from the current central")
print("value. Coincidence grade is retained (selection effects")
print("stated in the header) -- but the coincidence is no")
print("longer inert: it has a kill condition (m_tau settling")
print("elsewhere at sigma ~ 0.02-0.03 MeV resolution) and a")
print("horizon. That is the strongest form the digit-reader's")
print("evidence can take without new data: door II's last")
print("empirical question now waits on a measurement, not on")
print("more machinery.")
