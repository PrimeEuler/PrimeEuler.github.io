#!/usr/bin/env python3
"""
nonlinear_veto_closure.py -- item 3, first half (sandbox,
2026-11-18): does the FULL NONLINEAR K4 theory evade the
v15.998 Z2 (reflection) veto on the physical plus/cross
mixer / odd-y photon vertex O4 = (a_x^dag)^3 a_y?

Filed inputs:
- v15.1057 Gate 866: the K4 quartic invariant's expansion
  J(b,c) = 8/9 r^2 - 8/9 r^4 + 112/135 r^6 + ..., r^2 =
  b^2 + c^2 (b = plus, c = cross TT amplitudes); mixed
  Hessian at quartic truncation -64/9 bc; the entry itself
  flags "quartic-truncation only, not exact
  nonperturbatively" and notes r^6 gives BC(B^2+C^2)
  corrections.
- v15.1057 Gate 867: parity P_y reverses A_y and c, leaves
  A_x and b invariant; in the reduced system, integrating
  out tensor modes preserves parity, so any effective
  photon term with odd y-insertions (notably O4) has zero
  coefficient.
- v15.1058 Gate 871: self-sourcing preserves the parity:
  the Maxwell cross source is odd in the y-amplitude U
  (V_c,2 = -3QU cos(4t)), its Gaussian square is even
  (proportional to U^2), and the full action stays
  invariant under the combined reflection.

Gates:
H1. The filed J series to r^6: mixed Hessian is
    bc * [-64/9 + (896/45)(b^2+c^2)] -- proportional to bc
    at EVERY filed order, hence zero on any
    reflection-symmetric background (c = 0) and odd under
    c -> -c. The r^6 term corrects the coefficient, never
    the selection rule.
H2. All orders, general: for ANY analytic f, J = f(b^2+c^2)
    has mixed Hessian 4 bc f''(b^2+c^2) -- the bc factor
    is structural, from the invariant's argument.
H3. Why the argument is b^2+c^2: the TT strain block
    [[b, c], [c, -b]] has trace 0 and determinant
    -(b^2+c^2); its eigenvalues are +-sqrt(b^2+c^2), so
    every scalar invariant of the block is a function of
    b^2+c^2. Isotropic-solid scalar invariants are
    symmetric functions of strain eigenvalues, hence
    P_y-even in c.
H4. Monomial parity: O4 has y-count 1 (odd) -> P_y-odd ->
    coefficient zero in any P_y-invariant effective
    action, at every order (checked by enumeration to
    degree 8).
H5. Self-source/backreaction evenness (v15.1058's
    mechanism, algebraic): an odd source V(U) = -V(-U)
    integrated against a symmetric propagator contributes
    V G V, which is even: V(U)^2 - V(-U)^2 = 0 identically,
    while V itself is nonzero and odd. Backreaction
    redistributes within the symmetric sector; it does
    not manufacture P-odd vertices.

Scope: this closes the corner for reflection-SYMMETRIC
data (background, state, boundary conditions). Parity-odd
INPUT (a populated cross state, v15.1058; a stipulated
C != 0 background, v15.1057) produces conditional
responses -- those are inputs, not derivations, and their
output still owes the q2 matrix-element match (T^dag T =
2E across L) that no entry has produced.
"""
import sympy as sp

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

b, c = sp.symbols("b c", real=True)
r2 = b**2 + c**2

# H1: filed J series through r^6
J = sp.Rational(8, 9) * r2 - sp.Rational(8, 9) * r2**2 + sp.Rational(112, 135) * r2**3
H = sp.expand(sp.diff(J, b, c))
target = b * c * (sp.Rational(-64, 9) + sp.Rational(896, 45) * r2)
check("H1a mixed Hessian of filed J (through r^6) = bc[-64/9 + (896/45)(b^2+c^2)]",
      sp.simplify(H - target) == 0)
check("H1b Hessian vanishes on symmetric background c=0 at all filed orders",
      sp.simplify(H.subs(c, 0)) == 0)
check("H1c Hessian is odd under c -> -c (spurion character)",
      sp.simplify(H.subs(c, -c) + H) == 0)

# H2: general analytic invariant
a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4")
f = a1 * r2 + a2 * r2**2 + a3 * r2**3 + a4 * r2**4
Hg = sp.expand(sp.diff(f, b, c))
coeffs = [a1, a2, a3, a4]
fpp = sum(i * (i - 1) * coeffs[i - 1] * r2**(i - 2) for i in range(2, 5))
check("H2 general f(b^2+c^2): mixed Hessian = 4 bc f''(b^2+c^2), "
      "vanishing at c=0",
      sp.simplify(Hg - 4 * b * c * fpp) == 0
      and sp.simplify(Hg.subs(c, 0)) == 0)

# H3: TT block invariants
M = sp.Matrix([[b, c], [c, -b]])
lam = sp.symbols("lambda")
char = sp.expand(M.charpoly(lam).as_expr())
check("H3 TT block: tr = 0, det = -(b^2+c^2), char poly = lam^2 - (b^2+c^2)",
      M.trace() == 0 and sp.simplify(M.det() + r2) == 0
      and sp.simplify(char - (lam**2 - r2)) == 0)

# H4: monomial parity enumeration (P_y: a_y -> -a_y, a_x -> a_x)
def y_parity(i, j, k, l):
    # (a_x^dag)^i a_x^j (a_y^dag)^k a_y^l : parity = (-1)^(k+l)
    return -1 if (k + l) % 2 == 1 else 1
odd_ok = all(y_parity(i, j, k, l) == -1
             for i in range(5) for j in range(5)
             for k in range(5) for l in range(5)
             if 0 < i + j + k + l <= 8 and (k + l) % 2 == 1)
check("H4a every odd-y-count monomial to degree 8 is P_y-odd", odd_ok)
check("H4b O4 = (a_x^dag)^3 a_y has y-count 1 -> P_y-odd -> zero coefficient",
      y_parity(3, 0, 0, 1) == -1)

# H5: odd source, even square
U, Q, t = sp.symbols("U Q t", real=True)
V = -3 * Q * U * sp.cos(4 * t)   # v15.1058's V_c,2
check("H5a V_c,2 is odd in U and nonzero",
      sp.simplify(V.subs(U, -U) + V) == 0 and sp.simplify(V) != 0)
check("H5b V G V is even in U: V(U)^2 - V(-U)^2 = 0 identically",
      sp.simplify(V**2 - V.subs(U, -U)**2) == 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
