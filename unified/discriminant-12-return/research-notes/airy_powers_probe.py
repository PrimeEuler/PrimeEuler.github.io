#!/usr/bin/env python3
"""Airy comb and the two powers of the machine — consolidated probe.

Sandbox probe, 2026-10-18 (LIttle Euler). Reproduces every number cited in
the research-note addendum "Airy_Comb_and_the_Two_Powers_Addendum.md":

  A. Neutron-bouncer chain from constants: eps0 = (hbar^2 m_n g^2/2)^(1/3),
     Airy-zero comb, transition frequencies vs qBounce reported values.
  B. Quarter laws: Airy zeros vs [(3pi/2)(n-1/4)]^(2/3); J1 zeros vs pi(s+1/4).
  C. Small-rational check on transition ratios (expected: chance level).
  D. Jeremy's GM-wrap construction == Cayley pair form (machine precision).
  E. Power laws: wrapped angle phi_n ~ n^(-1/2); |a_m| ~ m^(2/3);
     composed ratio |a_n| phi_n^(4/3) -> (36 pi^2)^(1/3) (forced arithmetic).
  F. Symbolics (sympy): evolute of y = x^2/2 is semicubical 27X^2 = 8(Y-1)^3;
     parabolic segment = 2/3 of circumscribing parallelogram, area ~ h^(3/2);
     cone:sphere:cylinder volumes 1/3:2/3:1; sphere area = 2/3 cylinder total;
     paraboloid (f=1/2) area = (2pi/3)[(2H+1)^(3/2) - 1].
"""
import numpy as np
from scipy.special import ai_zeros, jn_zeros
from fractions import Fraction

print("== A. Bouncer comb from constants ==")
hbar, mn, g, eV = 1.054571817e-34, 1.67492749804e-27, 9.80665, 1.602176634e-19
eps0 = (hbar**2 * mn * g**2 / 2) ** (1/3) / eV * 1e12  # peV
az, *_ = ai_zeros(12)
a = -az
print(f"eps0 = {eps0:.4f} peV")
for (p, q) in [(3, 1), (2, 1), (7, 1), (9, 2)]:
    nu = eps0 * 1e-12 * (a[p - 1] - a[q - 1]) / 4.135667696e-15
    print(f"  nu |{q}>->|{p}> = {nu:8.1f} Hz")
print("  reported (TU Wien thesis, 2026): |1>->|7> ~ 1120 Hz, |2>->|9> ~ 1142 Hz")

print("== B. Quarter laws ==")
for n in range(1, 13):
    asym = (1.5 * np.pi * (n - 0.25)) ** (2 / 3)
    print(f"  Airy n={n:2d} |a_n|={a[n-1]:.6f} asym={asym:.6f} rel.err={abs(asym-a[n-1])/a[n-1]*100:.3f}%")
jz = jn_zeros(1, 8)
for s in range(1, 9):
    law = np.pi * (s + 0.25)
    print(f"  J1 s={s} j={jz[s-1]:.6f} pi(s+1/4)={law:.6f} rel.err={abs(law-jz[s-1])/jz[s-1]*100:.3f}%")

print("== C. Transition ratios vs small rationals (denominator <= 36) ==")
base = a[2] - a[0]
for (p, q) in [(2, 1), (4, 1), (3, 2), (7, 1), (5, 3)]:
    r = (a[p - 1] - a[q - 1]) / base
    best = Fraction(r).limit_denominator(36)
    print(f"  ({q}->{p}): {r:.5f}  nearest {best} off by {abs(float(best)-r)/r*100:.2f}%  (chance level)")

print("== D. GM-wrap == Cayley pair form ==")
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(8):
    n, k = rng.uniform(0.3, 40, 2)
    AM, off, gm = (n + k) / 2, (n - k) / 2, np.sqrt(n * k)
    zc = (np.sqrt(n) + 1j * np.sqrt(k)) / (np.sqrt(n) - 1j * np.sqrt(k))
    worst = max(worst, abs(complex(off / AM, gm / AM) - zc))
print(f"  worst |wrap - cayley| over 8 random pairs: {worst:.2e}")

print("== E. Power laws ==")
ns = np.arange(200, 4000)
phi = 2 * np.arctan(1 / np.sqrt(ns))
print(f"  phi_n slope: {np.polyfit(np.log(ns), np.log(phi), 1)[0]:.4f} (expect -1/2)")
az4, *_ = ai_zeros(4000)
ms = np.arange(200, 4000)
print(f"  |a_m| slope: {np.polyfit(np.log(ms), np.log(-az4[199:3999]), 1)[0]:.4f} (expect +2/3)")
ratio = (-az4[199:3999]) * phi ** (4 / 3)
print(f"  |a_n| phi_n^(4/3): n=200 {ratio[0]:.4f} -> n=3999 {ratio[-1]:.4f}; (36 pi^2)^(1/3) = {(36*np.pi**2)**(1/3):.4f}")

print("== F. Symbolics ==")
import sympy as sp
t = sp.symbols('t', real=True)
x, y = t, t**2 / 2
xp, yp, xpp, ypp = sp.diff(x, t), sp.diff(y, t), sp.diff(x, t, 2), sp.diff(y, t, 2)
den = xp * ypp - yp * xpp
Xc = sp.simplify(x - yp * (xp**2 + yp**2) / den)
Yc = sp.simplify(y + xp * (xp**2 + yp**2) / den)
print(f"  evolute of y=x^2/2: X(t) = {Xc}, Y(t) = {Yc}  (cusp at (0,1))")
X, Y = sp.symbols('X Y')
F = sp.factor(sp.resultant(X - Xc, Y - Yc, t))
print(f"  implicit: {F} = 0   i.e. 27 X^2 = 8 (Y-1)^3,  Y-1 = (3/2)|X|^(2/3)")
h, f, xx = sp.symbols('h f xx', positive=True)
w = sp.sqrt(4 * f * h)
seg = sp.integrate(h - xx**2 / (4 * f), (xx, -w, w))
print(f"  segment area = {sp.simplify(seg)}; parallelogram = {sp.simplify(2*w*h)}; ratio = {sp.simplify(seg/(2*w*h))}")
r = sp.symbols('r', positive=True)
print(f"  volumes cone:sphere:cyl = 1/3 : 2/3 : 1; sphere area / cylinder total area = "
      f"{sp.simplify(4*sp.pi*r**2/(2*sp.pi*r**2 + 2*sp.pi*r*(2*r)))}")
H = sp.symbols('H', positive=True)
rr = sp.sqrt(2 * H)
A = sp.pi * rr / (6 * H**2) * ((rr**2 + 4 * H**2) ** sp.Rational(3, 2) - rr**3)
print(f"  paraboloid area (f=1/2): {sp.simplify(A)}")
print("DONE")
