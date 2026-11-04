"""
Type-conversion check (2026-11-04, sandbox).

Question: the cone HAS a native exact 2/3 -- from the parabolas
(v14.592): segment = 2/3 of its parallelogram, segment area ~ h^{3/2},
Airy comb E_N ~ (N-1/4)^{2/3}, evolute law Y-1 = (3/2)|X|^{2/3}.
Can that 2/3 CONVERT into a phase 2/3 -- a U(1) charge quantum of the
kind the hypercharge fit needs (beta = -2/3 with integer windings) --
via the dictionary candidate "cone coordinate = action = segment
area, phase = action/hbar" (v14.620: quantization = single-valuedness
of the phase winding)?

The gate is ADDITIVITY. A U(1) generator eigenvalue (a charge) is a
homomorphism from the state-composition operation: two systems with
indices M, N compose to index M+N and their charges ADD. Any candidate
charge Q(index) must satisfy Q(M+N) = Q(M) + Q(N) exactly -- which on
the integers forces Q = c * index, linear. Every parabola 2/3 is a
nonlinear function of its index. The checks below make this concrete.
"""
from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 50

print("=" * 76)
print("0. The native 2/3, re-verified (the conversion input)")
print("=" * 76)
# (a) Segment = 2/3 of parallelogram: parabola y = x^2/(4f), chord at height h.
#     Segment area (between chord y=h and parabola) vs parallelogram (width x height).
import sympy as sp
x, f, h = sp.symbols('x f h', positive=True)
half_width = 2 * sp.sqrt(f * h)                      # x where x^2/(4f) = h
seg = sp.integrate(h - x**2 / (4 * f), (x, -half_width, half_width))
para = (2 * half_width) * h
print(f"  segment area = {sp.simplify(seg)}; parallelogram = {sp.simplify(para)};")
print(f"  ratio = {sp.simplify(seg / para)}  (Archimedes 2/3, any f, h)")
print(f"  segment = (8/3) sqrt(f) h^(3/2): {sp.simplify(seg - sp.Rational(8,3)*sp.sqrt(f)*h**sp.Rational(3,2)) == 0}")
# (b) Evolute of the f=1/2 parabola: X = -t^3, Y = 1 + (3/2) t^2  =>  27 X^2 = 8 (Y-1)^3
for t in [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]:
    X = -t**3; Y = 1 + Fraction(3, 2) * t**2
    assert 27 * X**2 == 8 * (Y - 1)**3
print("  evolute identity 27X^2 = 8(Y-1)^3: exact at rational sample points")
print("  => Y - 1 = (3/2) |X|^{2/3}: the 2/3 as a Puiseux exponent. Input confirmed.")

print()
print("=" * 76)
print("1. ADDITIVITY GATE: can a 2/3-power quantity be a charge?")
print("    Charge axiom: Q(M+N) = Q(M) + Q(N). Candidates from v14.592:")
print("=" * 76)
def airy(N): return (mpf(N) - mpf(1) / 4) ** (mpf(2) / 3)   # E_N of the bouncer comb
def pure(N): return mpf(N) ** (mpf(2) / 3)
for name, Q in [("Airy comb E_N = (N-1/4)^{2/3}", airy), ("pure power N^{2/3}", pure)]:
    lhs = Q(1) + Q(2); rhs = Q(3)
    print(f"  {name}: Q(1)+Q(2) = {mp.nstr(lhs, 12)}  vs  Q(3) = {mp.nstr(rhs, 12)}"
          f"  -> additive? {abs(lhs - rhs) < mpf(10) ** -30}")
    print(f"      also Q(2)/Q(1) = {mp.nstr(Q(2) / Q(1), 12)} (a linear charge needs exactly 2)")
print("  t -> t^{2/3} is strictly subadditive on positives: (a+b)^{2/3} < a^{2/3}+b^{2/3}.")
print("  Any additive Q on the integers is Q(N) = cN -- linear, no 2/3 power.")
print("  => the Airy/spectral 2/3 CANNOT be a U(1) generator eigenvalue.")

print()
print("=" * 76)
print("2. Phase from area, both directions (phase = action/hbar, action = segment area)")
print("=" * 76)
def A(hh): return mpf(8) / 3 * hh ** (mpf(3) / 2)   # f = 1 units
print("  (a) Equal HEIGHT steps h = 1..6: phase increments Delta_theta ~ A(h+1)-A(h):")
deltas = [A(k + 1) - A(k) for k in range(1, 7)]
print("      " + ", ".join(mp.nstr(d, 8) for d in deltas))
print(f"      constant? {max(deltas) - min(deltas) < mpf(10) ** -30} -- increments GROW like (3/2)sqrt(h):")
print("      shells at equal heights do NOT carry a constant winding quantum.")
print("  (b) Equal ACTION steps (Bohr-Sommerfeld: theta_N = 2 pi N, charges = N):")
hs = [(mpf(3) * N / 8) ** (mpf(2) / 3) for N in range(1, 7)]  # invert A(h) = N (units)
print("      heights h_N ~ N^{2/3}: " + ", ".join(mp.nstr(v, 8) for v in hs))
print("      => the 2/3 lands on the HEIGHTS (geometry). The charges stay N in Z.")

print()
print("=" * 76)
print("3. The nearest genuine discrete '3': the evolute cusp is a cubic discriminant")
print("=" * 76)
# Discriminant of x^3 + a x + b is -(4a^3 + 27b^2); its zero set is the semicubical
# cusp: parametrize a = -3t^2, b = 2t^3 -> 4a^3 + 27b^2 = 0 exactly (Fractions).
for t in [Fraction(1, 3), Fraction(1), Fraction(2), Fraction(5, 2)]:
    a = -3 * t**2; b = 2 * t**3
    assert 4 * a**3 + 27 * b**2 == 0
print("  4a^3 + 27b^2 = 0 on a=-3t^2, b=2t^3: exact. The cusp curve IS the cubic's")
print("  discriminant locus; loops around it permute the cubic's 3 roots (monodromy")
print("  in S_3, Coxeter element of order 3). A real order-3 discrete structure --")
print("  but it permutes CRITICAL POINTS of an auxiliary cubic. No cone state is")
print("  a root of that cubic, and nothing in the record transports cone states")
print("  around the cusp. Nearest miss, not a grading.")
print()
print("VERDICT: conversion FAILS, structurally. Charges are additive labels;")
print("every parabola 2/3 is a nonlinear function of its index (spectral law,")
print("area ratio, Puiseux exponent). Nonlinear => not a homomorphism => not")
print("a charge. The 2/3 rides on energies, heights and areas -- never on the")
print("phase lattice. (Separately, the concrete Suzuki-side segment-area")
print("dictionary already dissolved on its own terms, 2026-10-18: the 2/3 warp")
print("has no foothold in the archimedean channel.)")
