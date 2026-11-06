"""
Koide geometry + the neutrino test (2026-11-06, sandbox;
door II follow-through on v15.468's coincidence-grade
fingerprint, at Jeremy's direction).

Three questions:
 1. GEOMETRY. The Koide combination Q = sum m/(sum sqrt(m))^2
    is a pure angle: for s = (sqrt(m1), sqrt(m2), sqrt(m3)),
    cos^2(angle between s and the democratic axis (1,1,1))
    = (sum s)^2/(3 sum m) = 1/(3Q). So Q = 2/3 iff the
    root-mass vector sits at exactly 45 degrees to the
    generation-democratic axis -- the seat angle. Q = 1/3 is
    the axis itself (degenerate masses), Q = 1 a single axis.
 2. CHARGED LEPTONS. Measured angle and the residual phase:
    on the Q = 2/3 cone, s = A(1,1,1) + perp part of fixed
    relative size, and the perp direction is one phase
    delta = arg[(1/3) sum_k s_k e^{-2 pi i k/3}], k ascending
    (e, mu, tau) -- the Koide phase. Extract it (with the tau
    mass uncertainty propagated) and report whether it is a
    recognizable constant. It is DATA either way: 3 masses,
    2 parameters (scale + phase), 1 constraint (Q itself).
 3. NEUTRINOS. With oscillation data fixed (dm21^2 = 7.4e-5,
    |dm3l^2| = 2.51e-3 NO / 2.49e-3 IO, eV^2), Q_nu as a
    function of the lightest mass: does Q = 2/3 occur for ANY
    lightest mass in either ordering? If the maximum over the
    whole range sits below 2/3, the fingerprint is not a
    lepton law -- it is a CHARGED-lepton datum, which is the
    sector where the constant's filed home lives (charge x
    acceleration: Larmor, tau_0; v15.469/v15.470).
"""
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, atan2 as matan2, pi as mpi

mp.dps = 50

print("=" * 76)
print("1. geometry: Q = 2/3 is the 45-degree (seat) angle -- exact algebra")
print("=" * 76)
print("  cos^2(theta) = (sum sqrt(m))^2/(3 sum m) = 1/(3Q):")
print("  Q = 1/3 -> theta = 0 (degenerate); Q = 2/3 -> cos^2 = 1/2,")
print("  theta = 45 deg; Q = 1 -> theta = 54.7356 deg (single axis).")
print("  on the Q = 2/3 cone the Koide family s_k = A(1 + sqrt(2)")
print("  cos(2 pi k/3 + delta)) satisfies Q = 2/3 for every delta:")
A_, d_ = mpf('7.3'), mpf('0.9')
s = [A_ * (1 + msqrt(2) * mp.cos(2 * mpi * k / 3 + d_)) for k in range(3)]
Qfam = sum(x * x for x in s) / (sum(s)) ** 2
print(f"  numeric check (A=7.3, delta=0.9): Q = {mp.nstr(Qfam, 12)}")

print()
print("=" * 76)
print("2. charged leptons: angle, phase, tau-uncertainty band")
print("=" * 76)
me, mmu = mpf('0.51099895'), mpf('105.6583755')
def analyze(mtau):
    s = [msqrt(me), msqrt(mmu), msqrt(mtau)]
    Q = (me + mmu + mtau) / (sum(s)) ** 2
    theta = mp.degrees(mp.acos(1 / msqrt(3 * Q)))
    W = sum(s[k] * mp.e ** (-2 * mpi * mp.j * k / 3) for k in range(3)) / 3
    delta = matan2(mp.im(W), mp.re(W)) % (2 * mpi / 3)
    amp_ratio = abs(W) / (s[0] * 0 + sum(s) / 3)   # |W| / A_mean
    return Q, theta, delta, amp_ratio
for mt, lab in ((mpf('1776.86'), 'central'), (mpf('1776.98'), '+0.12'),
                (mpf('1776.74'), '-0.12')):
    Q, th, de, ar = analyze(mt)
    print(f"  m_tau {lab}: Q = {mp.nstr(Q, 10)}, theta = {mp.nstr(th, 8)} deg,")
    print(f"      delta = {mp.nstr(de, 8)} rad = {mp.nstr(mp.degrees(de), 7)} deg,"
          f"  |W|/A = {mp.nstr(ar, 8)} (Q=2/3 surface: 1/sqrt(2) = "
          f"{mp.nstr(1/msqrt(2), 6)})")
print("  candidates for delta: pi/14 = 0.22440, 2/9 = 0.22222,")
print("  pi/6 = 0.52360, 0 -- reported as data, no endorsement.")

print()
print("=" * 76)
print("3. neutrinos: is Q = 2/3 reachable at all? (scan both orderings)")
print("=" * 76)
dm21 = 7.4e-5
def Q_of(masses):
    sm = sum(masses); ss = sum(np.sqrt(masses))
    return sm / ss**2
for name, fn in (
    ("NO (m1 lightest)", lambda x: (x, np.sqrt(x**2 + dm21),
                                    np.sqrt(x**2 + 2.51e-3))),
    ("IO (m3 lightest)", lambda x: (np.sqrt(x**2 + 2.49e-3 - dm21),
                                    np.sqrt(x**2 + 2.49e-3), x)),
):
    xs = np.concatenate(([0.0], np.logspace(-4, 0, 4000)))
    Qs = np.array([Q_of(fn(x)) for x in xs])
    i = int(np.argmax(Qs))
    print(f"  {name}: max Q = {Qs[i]:.6f} at m_lightest = {xs[i]:.4f} eV; "
          f"Q(m=0.05) = {Q_of(fn(0.05)):.4f}; Q -> 1/3 degenerate.")
    print(f"      2/3 = 0.666667: {'REACHABLE' if Qs[i] >= 2/3 else 'NOT REACHED anywhere in the ordering'}")
print("  oscillation uncertainties (~1-3%) move these maxima by <0.01;")
print("  the deficit is 0.08 (NO) and 0.17 (IO). Cosmology (sum < 0.12")
print("  eV aggressive bound) allows the NO maximum point (sum = 0.059")
print("  eV): the exclusion is Koide's own, not cosmology's.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("The fingerprint's geometry is the seat angle: Q = 2/3 says")
print("the charged-lepton root-mass vector lies on the 45-degree")
print("cone about the democratic axis, one phase of freedom left")
print("(delta, extracted above -- data, candidate-grade only).")
print("As a lepton law it is DEAD: neutrino Q caps at ~0.586 (NO)")
print("and ~0.500 (IO) for every lightest mass -- 2/3 is")
print("unreachable in the neutral sector. What survives is a")
print("CHARGED-lepton datum only (quarks already fail, v15.468),")
print("which is exactly the sector of the constant's filed home:")
print("charge x acceleration (Larmor/tau_0, v15.470). For H2 the")
print("reader's locus narrows to the charged-lepton mass sector;")
print("H2 is narrowed, not discharged -- still no mechanism")
print("derives any mass, and the phase is one more real datum.")
