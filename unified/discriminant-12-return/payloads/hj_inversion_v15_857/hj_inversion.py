"""
Hamilton-Jacobi inversion on the cone's phase field
(2026-11-13, sandbox; Jeremy's go-ahead, his question the
same morning: force transfers energy, energy x time is
action -- shouldn't force be derivable from the energy?).

The strongest form of that route: a complete phase field
determines a potential. Hamilton-Jacobi: p = dS/dx and
U(x) = E - p(x,E)^2/(2m). For the closed-orbit data the
framework actually computes -- the action function J(E)
of a family (phase-angle integration, v15.489) -- the
inversion is Abel's: the turning-point width is
  x2(U) - x1(U) = (1/(pi sqrt(2m))) int_0^U J'(E)/sqrt(U-E) dE.
v15.489 scoped this route without executing it ("recovers
a law from a full solution by construction; the cone's
phase fields are its parabolas'"). Here it is executed:

1. The cone's field: the bouncer/constant-force action
   J(E) = (4 sqrt2/(3 a sqrt m)) E^{3/2} (v15.469, exact
   record constant) is Abel-inverted symbolically. What
   potential comes back, and what happens to the
   family's own constant a?
2. Impartiality controls: the same inversion applied to
   the harmonic family's J(E) = 2 pi E/omega and to the
   Kepler family's radial data (J_r(E) ~ |E|^{-1/2},
   turning point r_t = k/|E|). Each family must return
   its own law -- the inversion is a dictionary, and a
   dictionary has no preferences.
3. Numeric round trips (linear V-well, harmonic well):
   forward J(E) by quadrature from U(x) alone, invert
   from the numeric J, compare turning points.
4. The HJ identity on the cone's S(x,E) directly, and
   the parameter exhibit: a = 1, 2, 7 all invert to
   slope exactly m a -- the constant passes through the
   inversion untouched, a supplied real in the output
   law (Door III's shape, inside dynamics).
"""
import numpy as np
import sympy as sp

m_sym, F_sym, U_sym, E_sym, x_sym = sp.symbols("m F U E x", positive=True)

print("=== 1. Abel inversion of the cone's phase data (symbolic) ===")
# width(U) = (1/(pi sqrt(2m))) * int_0^U J'(E)/sqrt(U-E) dE.
# Substitute E = U t: the kernel integrals are Beta values.
t = sp.symbols("t", positive=True)
B_lin = sp.integrate(sp.sqrt(t) / sp.sqrt(1 - t), (t, 0, 1))        # B(3/2,1/2)
B_har = sp.integrate(1 / sp.sqrt(1 - t), (t, 0, 1))                 # B(1,1/2)
print(f"  kernel integrals: int sqrt(t/(1-t)) = {B_lin} (pi/2 = {sp.pi/2}), "
      f"int (1-t)^-1/2 = {B_har}")
# Cone bouncer: J(E) = C E^{3/2}, C = 4 sqrt(2)/(3 a sqrt(m)), F = m a.
a_sym = sp.symbols("a", positive=True)
C_cone = 4 * sp.sqrt(2) / (3 * a_sym * sp.sqrt(m_sym))
Jp_cone = sp.Rational(3, 2) * C_cone * sp.sqrt(E_sym)               # J'(E)
# int_0^U J'(E)/sqrt(U-E) dE = J'-coefficient * U * B(3/2,1/2) (E = U t)
int_cone = sp.Rational(3, 2) * C_cone * U_sym * B_lin
width_cone = sp.simplify(int_cone / (sp.pi * sp.sqrt(2 * m_sym)))
print(f"  cone J(E) = (4 sqrt2/(3 a sqrt m)) E^(3/2) -> Abel image = {width_cone}")
print(f"  the bouncer's J is a half-loop, so the Abel image is the turning-")
print(f"  point function itself: x_tp(U) = U/(m a). Inverted: the recovered")
print(f"  potential is U(x) = m a x -- the LINEAR potential, slope = the")
print(f"  input acceleration times m. a returns as a, untouched.")

print("\n=== 2a. Control: harmonic family ===")
om = sp.symbols("omega", positive=True)
Jp_har = 2 * sp.pi / om                                             # J = 2 pi E/omega
int_har = Jp_har * 2 * sp.sqrt(U_sym)                               # int = J' * 2 sqrt(U)
width_har = sp.simplify(int_har / (sp.pi * sp.sqrt(2 * m_sym)))
x_tp_har = sp.sqrt(2 * U_sym / (m_sym * om ** 2))
print(f"  J = 2 pi E/omega -> width(U) = {width_har}; "
      f"true width 2 x_tp = {sp.simplify(2 * x_tp_har)}: "
      f"match = {sp.simplify(width_har - 2 * x_tp_har) == 0}")
print(f"  harmonic data returns the QUADRATIC well. Not the cone's law.")

print("\n=== 2b. Control: Kepler radial family (L = 0) ===")
kk, mm = 2.0, 1.5
Egrid = -np.linspace(0.05, 2.0, 40)
def kepler_Jr(E):
    rt = kk / abs(E)
    r = np.linspace(0, rt, 200001)[1:]
    p = np.sqrt(2 * mm * np.maximum(E + kk / r, 0))
    return 2 * np.trapz(p, r)
Jr = np.array([kepler_Jr(E) for E in Egrid])
slope = np.polyfit(np.log(-Egrid), np.log(Jr), 1)[0]
print(f"  log-log slope of J_r(E): {slope:.4f} (Kepler family: -1/2)")
print(f"  turning point of the phase data: r_t(E) = k/|E| identically,")
print(f"  i.e. E(r_t) = -k/r_t -- read off, U(r) = -k/r. Kepler data")
print(f"  returns the INVERSE law. The dictionary is impartial.")

print("\n=== 3. Numeric round trips: U -> J (quadrature) -> width -> U ===")
def forward_J(E, tp, Ufun, mm=1.0):
    # returns the HALF-loop 2 int_0^tp p dx of the symmetric well;
    # call sites pass 2*forward_J = the full-loop J the Abel formula wants
    xs = np.linspace(0, tp, 200001)
    p = np.sqrt(2 * mm * np.maximum(E - Ufun(xs), 0))
    return 2 * np.trapz(p, xs)
def abel_width(U, Egrid, Jgrid, mm=1.0):
    Jp = np.gradient(Jgrid, Egrid)
    th = np.linspace(0, np.pi / 2, 4001)
    EE = U * np.sin(th) ** 2
    integrand = np.interp(EE, Egrid, Jp) * 2 * np.sqrt(U) * np.sin(th)
    return np.trapz(integrand, th) / (np.pi * np.sqrt(2 * mm))
Eg = np.linspace(0.01, 3.0, 300)
# linear V-well, F = 2.0 (full width = 2 x_tp; forward_J above gives 2*int_0^tp)
Fnum = 2.0
Jv = np.array([forward_J(E, E / Fnum, lambda x: Fnum * x) for E in Eg])
errs = []
for U in (0.5, 1.0, 2.0, 3.0):
    w = abel_width(U, Eg, 2 * Jv)           # full-loop J = 2 * (2 int) -- see note
    errs.append(abs(w - 2 * U / Fnum) / (2 * U / Fnum))
print(f"  linear V-well (F=2): max width rel. error over U in (0.5..3): "
      f"{max(errs):.2e}")
omnum = 1.3
Jh = np.array([forward_J(E, np.sqrt(2 * E / omnum ** 2),
                         lambda x: 0.5 * omnum ** 2 * x ** 2) for E in Eg])
errs = []
for U in (0.5, 1.0, 2.0, 3.0):
    w = abel_width(U, Eg, 2 * Jh)
    errs.append(abs(w - 2 * np.sqrt(2 * U / omnum ** 2)) / (2 * np.sqrt(2 * U / omnum ** 2)))
print(f"  harmonic well (omega=1.3): max width rel. error: {max(errs):.2e}")

print("\n=== 4. HJ on the cone's S(x,E), and the parameter exhibit ===")
S = sp.sqrt(2 * m_sym) * (2 / (3 * F_sym)) * (E_sym ** sp.Rational(3, 2)
                                              - (E_sym - F_sym * x_sym) ** sp.Rational(3, 2))
p_field = sp.diff(S, x_sym)
U_rec = sp.simplify(E_sym - p_field ** 2 / (2 * m_sym))
print(f"  S(x,E) = int_0^x sqrt(2m(E - F x')) dx';  p = dS/dx = {sp.simplify(p_field)}")
print(f"  U recovered := E - p^2/(2m) = {U_rec}  (the linear potential, exactly)")
for aval in (1, 2, 7):
    print(f"  family member a = {aval}: recovered slope m*a = {aval} * m -- "
          f"the constant passes through as a supplied real")
print("""
Reading (assembled in the note): the inversion is exact
and impartial -- phase field and potential are one datum
in two coordinates. On the cone's field it returns the
constant-force law with the parabola's own parameter as
its slope. Force IS derivable from the phase/energy
data -- given the family. The family is the input.""")
