"""
The rank-2 duck test (2026-11-07, sandbox; Jeremy's go-ahead).

The duck test of v14.628 asked, in the rotor sector, whether
the device<->model rhyme is FORCED: the model's ladder
coupling (axial rank-1 field, cos th; climb weights w_j) and
the device field's coupling (transverse rank-1 field,
sin th e^{i phi}; climb weights u_j) turned out to be one
skeleton -- u_j = w_j sqrt((j+2)/(j+1)) exactly, climb
products differing by exactly sqrt(J+1) -- because both are
components of one rank-1 tensor and SO(3) leaves no choice.

This run applies the identical test to the rank-2 (tidal)
channel of v14.630 -- the G channel: beta_2 = 2 G M_s I^2 /
(hbar^2 R^3) is the only coupling in the rotor anatomy that
carries G itself (rank-1's beta carries g). The rank-2
tensor's components, as operators on the rotor (bare angular
functions, the v14.628 test's normalization precedent; the
source-direction factors of the addition theorem ride with
the field amplitudes, as E_z / E_- did at rank 1):

  A0 = P2(cos th)              axial tidal (the v14.630 channel)
  A1 = sin th cos th e^{i phi} transverse tidal drive, Dm = +1
  A2 = sin^2 th e^{2 i phi}     transverse tidal drive, Dm = +2

Weight systems (m = 0, as at rank 1), computed exactly from
Wigner 3j symbols:
  climb:    v_j  = <j+2,0|A0|j,0>,  v1_j = <j+2,1|A1|j,0>,
            v2_j = <j+2,2|A2|j,0>
  diagonal: d_j  = <j,0|A0|j,0>,    d1_j = <j,1|A1|j,0>,
            d2_j = <j,2|A2|j,0>     (rank 2 has a diagonal
            channel; rank 1 had none)
TEST (the v14.628 criterion): the rhyme is identity at
rank 2 iff every transverse weight is the axial weight
times an exact closed-form factor in j (zero free
parameters), with climb products in closed form along the
two parity chains (rank 2 steps Dj = 2, so the even/odd
chains are independent, v14.630).

VALIDATION, three independent paths that must agree:
 (a) the 3j computation reproduces the record's axial
     weights exactly -- v_j = (3/2) w_j w_{j+1} and
     d_j = (3(w_j^2 + w_{j-1}^2) - 1)/2 (v14.630, themselves
     verified there against the explicit (3cos^2-1)/2
     matrix);
 (b) every weight is recomputed by composing rank-1 matrix
     elements only (A1 = S*C and A2 = S*S as angular
     functions, S = sin th e^{i phi}, C = cos th; A0 via
     (3C^2-1)/2), using
       <j+1,m|C|j,m>  = +sqrt(((j+1)^2-m^2)/((2j+1)(2j+3)))
       <j-1,m|C|j,m>  = +sqrt((j^2-m^2)/((2j-1)(2j+1)))
       <j+1,m+1|S|j,m> = -sqrt((j+m+1)(j+m+2)/((2j+1)(2j+3)))
       <j-1,m+1|S|j,m> = +sqrt((j-m-1)(j-m)/((2j-1)(2j+1)))
     (the Dj = -1 elements of S carry the OPPOSITE sign to
     the Dj = +1 elements -- the composition check caught
     exactly this in development; the 3j values fix it);
 (c) the fitted ratio laws are verified EXACTLY (sympy
     simplification of the squared differences) at every
     tabulated j, not only at the fit points.
Conversions: A0 = sqrt(4 pi/5) Y_20; A1 = -sqrt(8 pi/15)
Y_21; A2 = sqrt(32 pi/15) Y_22 (Condon-Shortley). The 3j
formula used is <jp mp|Y_2q|j m> = (-1)^mp sqrt((2j+1) 5
(2jp+1)/(4 pi)) (j 2 jp; 0 0 0)(j 2 jp; m q -mp) -- note
the third m-entry is -mp (the m-sum convention; with +mp
the transverse symbols vanish identically).
"""
import math
from functools import lru_cache

import sympy as sp
from sympy.physics.wigner import wigner_3j

# ---------------------------------------------------------------- exact 3j path
@lru_cache(maxsize=None)
def Y2(jp, mp, j, m, q):
    if mp != m + q:
        return sp.Integer(0)
    return ((-1) ** mp * sp.sqrt(sp.Rational((2 * j + 1) * 5 * (2 * jp + 1), 4) / sp.pi)
            * wigner_3j(j, 2, jp, 0, 0, 0)
            * wigner_3j(j, 2, jp, m, q, -mp))

C0 = sp.sqrt(4 * sp.pi / 5)
C1 = -sp.sqrt(8 * sp.pi / 15)
C2 = sp.sqrt(32 * sp.pi / 15)

@lru_cache(maxsize=None)
def v(j):  return C0 * Y2(j + 2, 0, j, 0, 0)
@lru_cache(maxsize=None)
def v1(j): return C1 * Y2(j + 2, 1, j, 0, 1)
@lru_cache(maxsize=None)
def v2(j): return C2 * Y2(j + 2, 2, j, 0, 2)
@lru_cache(maxsize=None)
def d(j):  return C0 * Y2(j, 0, j, 0, 0)
@lru_cache(maxsize=None)
def d1(j): return C1 * Y2(j, 1, j, 0, 1)
@lru_cache(maxsize=None)
def d2(j): return C2 * Y2(j, 2, j, 0, 2)

def w(j):  # rank-1 axial weights (v14.626), w_{-1} := 0
    return sp.Integer(0) if j < 0 else (j + 1) / sp.sqrt((2 * j + 1) * (2 * j + 3))

JMAX = 32
for fn in (v, v1, v2, d, d1, d2):
    for j in range(JMAX + 1):
        fn(j)

print("=" * 76)
print("(a) validation: 3j axial weights vs the record's formulas (v14.630)")
print("=" * 76)
ok = True
for j in range(0, 31):
    ok &= sp.simplify(v(j) - sp.Rational(3, 2) * w(j) * w(j + 1)) == 0
    ok &= sp.simplify(d(j) - (3 * (w(j) ** 2 + w(j - 1) ** 2) - 1) / 2) == 0
print(f"  v_j == (3/2) w_j w_{{j+1}}, d_j == (3(w_j^2+w_{{j-1}}^2)-1)/2 exactly,")
print(f"  j = 0..30: {ok}")
assert ok
print(f"  anchors: v_0 = {sp.simplify(v(0))} (record 1/sqrt(5)); "
      f"d_1 = {sp.simplify(d(1))} (record 2/5); d_0 = {sp.simplify(d(0))} (record 0)")
# nonzero guards: a transverse system that vanished identically would
# make every ratio check below vacuous -- refuse to proceed on zeros.
for name, fn, lo in (("v1", v1, 0), ("v2", v2, 0), ("d1", d1, 1), ("d2", d2, 2)):
    assert all(fn(j) != 0 and abs(float(fn(j))) > 1e-3 for j in range(lo, 13)), name
print("  nonzero guards: v1, v2 (j>=0), d1 (j>=1), d2 (j>=2) all nonzero: True")

# ------------------------------------------------------- composition path (float)
def Cup(j, m):
    return math.sqrt(((j + 1) ** 2 - m * m) / ((2 * j + 1) * (2 * j + 3)))
def Cdn(j, m):  # <j-1,m|C|j,m>, j >= 1
    return math.sqrt((j * j - m * m) / ((2 * j - 1) * (2 * j + 1))) if j >= 1 else 0.0
def Sup(j, m):
    return -math.sqrt((j + m + 1) * (j + m + 2) / ((2 * j + 1) * (2 * j + 3)))
def Sdn(j, m):  # <j-1,m+1|S|j,m>, j >= 1; zero unless m+1 <= j-1 or edge
    if j < 1 or j - m - 1 < 0:
        return 0.0
    return math.sqrt((j - m - 1) * (j - m) / ((2 * j - 1) * (2 * j + 1)))

def v_c(j):  return 1.5 * Cup(j, 0) * Cup(j + 1, 0)
def v1_cA(j): return Sup(j + 1, 0) * Cup(j, 0)          # S after C
def v1_cB(j): return Cup(j + 1, 1) * Sup(j, 0)          # C after S (must agree)
def v2_c(j): return Sup(j + 1, 1) * Sup(j, 0)
def d_c(j):  return (3 * (Cup(j, 0) ** 2 + Cdn(j, 0) ** 2) - 1) / 2
def d1_c(j): return Cdn(j + 1, 1) * Sup(j, 0) + (Cup(j - 1, 1) * Sdn(j, 0) if j >= 1 else 0.0)
def d2_c(j): return Sdn(j + 1, 1) * Sup(j, 0) + (Sup(j - 1, 1) * Sdn(j, 0) if j >= 1 else 0.0)

print()
print("=" * 76)
print("(b) composition path (rank-1 elements only) vs 3j path, j = 0..12")
print("=" * 76)
worst = 0.0
for name, f3, fc in (("v", v, v_c), ("v1", v1, v1_cB), ("v2", v2, v2_c),
                     ("d", d, d_c), ("d1", d1, d1_c), ("d2", d2, d2_c)):
    err = max(abs(float(f3(j)) - fc(j)) for j in range(13))
    worst = max(worst, err)
    print(f"  {name}: max |3j - composition| = {err:.2e}")
err1 = max(abs(v1_cA(j) - v1_cB(j)) for j in range(13))
print(f"  v1 two orderings (S after C vs C after S): max diff = {err1:.2e}")
print(f"  worst overall: {worst:.2e}")
assert worst < 1e-12 and err1 < 1e-12

# ------------------------------------------------------------------ ratio fits
jj = sp.symbols("j")

def identify_ratio_sq(num, den, lo, fit_hi=15, deg=3, shift=0):
    """Identify (num/den)^2 as a rational function of j by rational
    interpolation on exact-identified values, then verify EXACTLY
    against the raw 3j expressions at every j in lo..JMAX.
    With shift > 0 the fit is done in u = j - shift (the diagonal
    laws' denominators vanish at j = 0 -- j(j+1) -- so the
    constant-normalized ansatz only represents them shifted)."""
    if shift:
        num0, den0 = num, den
        num = lambda j, f=num0, s=shift: f(j + s)
        den = lambda j, f=den0, s=shift: f(j + s)
        cand = identify_ratio_sq(num, den, 0, fit_hi - shift, deg)
        return sp.cancel(cand.subs(jj, jj - shift)) if cand is not None else None
    pts = []
    for j in range(lo, fit_hi + 1):
        val = sp.nsimplify(sp.N((num(j) / den(j)) ** 2, 50), rational=True)
        pts.append((j, sp.Rational(val)))
    # Rational interpolation via the nullspace of the homogeneous
    # system over ALL fit points (a square subsystem can be singular
    # for special value patterns -- e.g. 1/(j(j+1)) makes the
    # j and j^2 columns affinely dependent -- so never solve square).
    for dn_ in range(deg + 1):
        for dd_ in range(deg + 1):
            na, nb = dn_ + 1, dd_
            rows = []
            for (j, val) in pts:
                rows.append([sp.Rational(j) ** k for k in range(na)] +
                            [-val * sp.Rational(j) ** k for k in range(1, nb + 1)] +
                            [-val])
            ns = sp.Matrix(rows).nullspace()
            for vec in ns:
                if vec[-1] == 0:
                    continue
                vec = vec / vec[-1]
                cand = sp.cancel(sum(vec[k] * jj ** k for k in range(na)) /
                                 (1 + sum(vec[na + k - 1] * jj ** k
                                          for k in range(1, nb + 1))))
                if all(sp.simplify((num(j) / den(j)) ** 2 - cand.subs(jj, j)) == 0
                       for j in range(lo, JMAX + 1)):
                    return cand
    return None

print()
print("=" * 76)
print("the test: transverse/axial ratio laws (identified, then verified")
print("exactly against the raw 3j weights at every j in range)")
print("=" * 76)
LAW = {}
for name, num, den, lo in (("climb q=1", v1, v, 0), ("climb q=2", v2, v, 0),
                           ("diag  q=1", d1, d, 1), ("diag  q=2", d2, d, 1)):
    cand = identify_ratio_sq(num, den, lo, shift=1 if name.startswith("diag") else 0)
    assert cand is not None, name
    sgn = 1 if float(num(lo if name != "diag  q=2" else 2) /
                     den(lo if name != "diag  q=2" else 2)) > 0 else -1
    # exact signed verification at small j (sqrt expressions)
    form = sgn * sp.sqrt(cand)
    ex = all(sp.simplify(num(j) - form.subs(jj, j) * den(j)) == 0
             for j in range(max(lo, 2 if name == "diag  q=2" else lo),
                            min(JMAX, 12) + 1))
    LAW[name] = (sgn, cand)
    print(f"  {name}: ratio = {form}")
    print(f"      (ratio)^2 verified exactly at j = {lo}..{JMAX}; "
          f"signed form verified exactly at small j: {ex}")
    assert ex

print()
print("  absolute transverse weights (ratio law x the record's axial forms):")
print("    v1_j = -(j+1) sqrt((j+2)(j+3)) / ((2j+3) sqrt((2j+1)(2j+5)))")
print("    v2_j = +sqrt((j+1)(j+2)(j+3)(j+4)) / ((2j+3) sqrt((2j+1)(2j+5)))")
print("    d1_j = -d_j / sqrt(j(j+1)),   d2_j = -2 d_j sqrt((j-1)(j+2)/(j(j+1)))")
print("  per-step limits: v -> 3/8, v1 -> -1/4, v2 -> +1/4;")
print("                   d -> 1/4, d1 -> 0 (-1/(4j)), d2 -> -1/2")

# ------------------------------------------------------------- climb products
def v_f(j):  return 1.5 * (j + 1) * (j + 2) / ((2 * j + 3) * math.sqrt((2 * j + 1) * (2 * j + 5)))
def R1_f(j): return -(2.0 / 3.0) * math.sqrt((j + 3) / (j + 2))
def R2_f(j): return (2.0 / 3.0) * math.sqrt((j + 3) * (j + 4) / ((j + 1) * (j + 2)))

print()
print("=" * 76)
print("climb products along the parity chains (float, from the closed forms)")
print("=" * 76)
# exact product identities at moderate N (direct product vs closed form)
for s in (0, 1):
    N = 30
    idx = [s + 2 * k for k in range(N)]
    p1 = math.prod(R1_f(j) for j in idx)
    g1 = (-(2.0 / 3.0)) ** N * math.exp(0.5 * (
        math.lgamma((s + 3) / 2 + N) - math.lgamma((s + 3) / 2)
        - math.lgamma((s + 2) / 2 + N) + math.lgamma((s + 2) / 2)))
    p2 = math.prod(R2_f(j) for j in idx)
    g2 = (2.0 / 3.0) ** N * math.sqrt((s + 2 * N + 1) * (s + 2 * N + 2) / ((s + 1) * (s + 2)))
    print(f"  chain {s}: Prod R1 (N=30) direct vs Gamma form: rel err "
          f"{abs(p1 - g1) / abs(g1):.2e};  Prod R2 vs telescope: {abs(p2 - g2) / abs(g2):.2e}")

C1c = {0: math.pi ** 0.25, 1: math.pi ** 0.25 * math.sqrt(3 * math.pi) / 4}
C0c = {0: math.sqrt(math.pi / 2), 1: math.sqrt(3 * math.pi / 8)}
C2c = {0: math.sqrt(math.pi), 1: math.sqrt(math.pi) / 2}
for s in (0, 1):
    for N in (200, 4000):
        idx = [s + 2 * k for k in range(N)]
        lv = sum(math.log(v_f(j)) for j in idx)
        l1 = sum(math.log(abs(v_f(j) * R1_f(j))) for j in idx)
        l2 = sum(math.log(v_f(j) * R2_f(j)) for j in idx)
        r0 = math.exp(lv - N * math.log(3 / 8)) / C0c[s]
        r1 = math.exp(l1 - N * math.log(0.25)) / (N ** 0.25 * C1c[s])
        r2 = math.exp(l2 - N * math.log(0.25)) / (N * C2c[s])
        print(f"  chain {s}, N={N}: Prod v / [sqrt-Wallis (3/8)^N] = {r0:.6f} of "
              f"candidate;  Prod|v1| / [C N^(1/4) (1/4)^N] = {r1:.6f};  "
              f"Prod v2 / [D N (1/4)^N] = {r2:.6f}")
print(f"  candidates: Prod v constants sqrt(pi/2) = {math.sqrt(math.pi/2):.6f} (even), "
      f"sqrt(3 pi/8) = {math.sqrt(3*math.pi/8):.6f} (odd)  [the record's, v14.630]")
print(f"              Prod v1 constants pi^(1/4) = {math.pi**0.25:.6f} (even), "
      f"pi^(1/4) sqrt(3 pi)/4 = {math.pi**0.25 * math.sqrt(3*math.pi)/4:.6f} (odd), "
      f"sign (-1)^N")
print(f"              Prod v2 constants sqrt(pi) = {math.sqrt(math.pi):.6f} (even), "
      f"sqrt(pi)/2 = {math.sqrt(math.pi)/2:.6f} (odd)")
print(f"  per-step at j=4000: v = {v_f(4000):.6f}, v1 = {v_f(4000)*R1_f(4000):.6f}, "
      f"v2 = {v_f(4000)*R2_f(4000):.6f}")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("""  IDENTITY at rank 2, in the v14.628 sense: every transverse
  tidal weight is the axial (v14.630) weight times an exact
  closed-form factor in j -- the four ratio laws above,
  verified exactly, zero free parameters -- and the climb
  products close in Gamma/telescoped form on both parity
  chains, with the rank-1 Wallis constant sqrt(pi/2)
  reappearing on the even chain. The rank-2-specific anatomy
  (parity-split chains; a diagonal channel rank 1 lacked,
  whose transverse weights are exact multiples of the axial
  diagonal) is part of the one skeleton, not an exception.
  Scope, as at rank 1: this is the tidal (P2) channel's
  coupling anatomy. beta_2's overall scale still carries the
  imported G; the finite-distance device coupling of
  v14.630 Part 3 mixes in n=4 terms and sits outside the
  rank-2 skeleton, as designed-in coil turns sat outside
  rank 1's.""")
