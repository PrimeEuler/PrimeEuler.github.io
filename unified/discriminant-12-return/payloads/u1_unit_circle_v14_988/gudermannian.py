"""U(1)/hbar-unit-circle test: the pair angle phi vs the shape coordinate s.
z_{n,k} = ((n-k) + 2i sqrt(nk)) / (n+k) lies on U(1). With s = (1/2) ln(n/k):
claim cos(phi) = tanh(s), sin(phi) = sech(s)  (Gudermannian bridge), so phi in
(0, pi) covers one orientation of the pair and phi -> 2pi - phi under n<->k.
Then dphi/ds = -sech(s), and the circle momentum L = -i hbar d/dphi is, in
s-coordinates, the DRESSED boost momentum cosh(s) * p_s (symmetrized)."""
import sympy as sp

n, k, s, m = sp.symbols('n k s m', positive=True)
z = ((n - k) + 2 * sp.I * sp.sqrt(n * k)) / (n + k)
print("|z|^2 =", sp.simplify(z * sp.conjugate(z.rewrite(sp.Abs)) if False else (n - k)**2 / (n + k)**2 + 4 * n * k / (n + k)**2))
cosphi = (n - k) / (n + k); sinphi = 2 * sp.sqrt(n * k) / (n + k)
# substitute n/k = e^{2s}: set n = k e^{2s}
sub = {n: k * sp.exp(2 * s)}
print("cos(phi) - tanh(s) =", sp.simplify(cosphi.subs(sub) - sp.tanh(s)))
print("sin(phi) - sech(s) =", sp.simplify(sinphi.subs(sub) - 1 / sp.cosh(s)))
phi = sp.acos(sp.tanh(s))
print("dphi/ds + sech(s) =", sp.simplify(sp.diff(phi, s) + 1 / sp.cosh(s)))
# measure: int_R sech(s) ds should equal pi (the phi-range of one orientation)
print("int sech(s) ds over R =", sp.integrate(1 / sp.cosh(s), (s, -sp.oo, sp.oo)))
# dressing factor at crossings: cosh(s) = (n+k)/(2 sqrt(nk)) = AM/GM
for (nv, kv) in [(1, 1), (1, 4), (4, 1), (1, 2), (3, 1), (5, 7), (11, 1)]:
    sv = sp.Rational(1, 2) * sp.log(sp.Rational(nv, kv))
    print(f"  pair ({nv},{kv}): s={float(sv):+.4f}  cosh(s)=AM/GM={float(sp.cosh(sv)):.4f}"
          f"  sech={float(1/sp.cosh(sv)):.4f}  phi={float(sp.acos(sp.tanh(sv))):.4f} rad")
# classical bracket check: {phi_tilde, L} with phi_tilde = pi - phi(s), L = cosh(s) p_s
# {f(s), g(s) p} = f'(s) g(s)  (with {s, p_s} = 1)
fprime = -sp.diff(phi, s)          # d(pi - phi)/ds
print("{phi_tilde, cosh(s) p_s} =", sp.simplify(fprime * sp.cosh(s)), " (expect 1: canonical pair)")
