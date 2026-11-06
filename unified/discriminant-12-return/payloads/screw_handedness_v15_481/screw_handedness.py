"""
The screw overlay's handedness (2026-11-06, sandbox;
door I's last named hiding place, v15.473; Jeremy's pick).

The screw has TWO faces in the record, and they must not
be conflated:
 FACE 1 (v13.258): the half-line Laplace screw. Suzuki's
   transform int_0^inf g_F(t) e^{izt} dt = (1/z^2)
   (xi_F'/xi_F)(1/2 - iz), and Phi_F = -g_F with the
   explicit ramp formula (for chi_12: Phi_12 = A_12 - R_12,
   R the prime-power ramp sum). This face IS one-sided.
 FACE 2 (v13.753): the whole-line helix screw. Suzuki's
   screw function there is REAL and EVEN, and the physical
   object is the increment kernel G_g(u,v) = g(u-v) - g(u)
   - g(-v) + g(0) -- the Weil form's kernel, carried by
   the rapidity helix with carriers e^{itu}.

Tests:
 1a. Phi_12 from the entry's own formula at +-t: measure
     the one-sidedness (ramps exist only for t > log 2).
 1b. The mirror prescription (1/2 + iz in place of
     1/2 - iz): by the functional equation xi(s) = xi(1-s),
     L(1/2 + iz) = -L(1/2 - iz) identically (L = xi'/xi),
     so the mirrored transform is the NEGATIVE of the
     original: the "opposite-handed" Laplace screw is -g_F,
     whose positivity criterion is the criterion negated.
     Verified numerically on the actual xi_12. The sign in
     Suzuki's formula is fixed by landing on the
     Euler-product side (Re s > 1): analyticity, and the
     asymmetry is the transform's arrow (the retardation
     species of the v15.473 census), on the log-scale axis
     -- not a spatial winding.
 2.  Face 2: for even g the increment kernel is invariant
     under the rapidity reflection (u,v) -> (-u,-v) -- the
     factor swap in this layer -- by two lines of algebra
     (verified on a model even g; the general step uses
     only evenness). The Fourier-convention sign (the only
     other place a sense could hide) cancels for even
     spectral weight: e^{+itw} and e^{-itw} syntheses agree
     (cosine pairing; v13.753 itself records "no residual
     sign... the sole Fourier-convention factor is 1/(2pi)").
Verdict in the printout: no handedness survives in either
face; door I's screw hiding place is CLOSED.
"""
import mpmath as mp
mp.mp.dps = 40

print("=" * 76)
print("1a. Phi_12 (v13.258 formula) at +-t: the Laplace face is one-sided")
print("=" * 76)
def chi12(n):
    r = n % 12
    return 1 if r in (1, 11) else (-1 if r in (5, 7) else 0)
def Lam(n):
    # von Mangoldt via factorization (small n)
    import sympy as sp
    f = sp.factorint(n)
    return mp.log(list(f)[0]) if len(f) == 1 else mp.mpf(0)
def R12(t):
    if t < mp.log(2):
        return mp.mpf(0)
    N = int(mp.e ** t) + 1
    return mp.fsum(Lam(n) * chi12(n) / mp.sqrt(n) * (t - mp.log(n))
                   for n in range(2, N + 1) if chi12(n) != 0)
def A12(t):
    return (t / 2) * (mp.digamma(mp.mpf(1) / 4) + mp.log(12 / mp.pi)) \
        + mp.mpf(1) / 4 * (mp.zeta(2, mp.mpf(1) / 4)
                           - mp.e ** (-t / 2) * mp.lerchphi(mp.e ** (-2 * t), 2, mp.mpf(1) / 4))
def Phi12(t):
    return A12(t) - R12(t)
for t in (1.0, 3.0, 6.0):
    neg = Phi12(mp.mpf(-t))
    print(f"  t={t}: Phi_12(+t) = {mp.nstr(Phi12(mp.mpf(t)), 8)} (real), "
          f"R_12(-t) = {mp.nstr(R12(mp.mpf(-t)), 3)} (ramps absent);")
    print(f"      naive continuation to -t is non-real (Im = "
          f"{mp.nstr(mp.im(neg), 6)}): the archimedean term's")
    print("      Lerch piece is a half-line formula -- off the half-line")
    print("      it needs a branch prescription before it is a function")
    print("      at all. The criterion is stated for the + side only.")

print()
print("=" * 76)
print("1b. the mirror prescription is the NEGATION (functional equation)")
print("=" * 76)
chi_arr = [0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1]
def xi12(s):
    return (12 / mp.pi) ** (s / 2) * mp.gamma(s / 2) * mp.dirichlet(s, chi_arr)
def Llog(s):
    return mp.diff(lambda x: mp.log(xi12(x)), s)
for z in (mp.mpf('0.8') + mp.mpf('0.3') * 1j, mp.mpf('1.7') - mp.mpf('0.4') * 1j,
          mp.mpf('2.3') + mp.mpf('1.1') * 1j):
    lhs = Llog(mp.mpf(1) / 2 + 1j * z) + Llog(mp.mpf(1) / 2 - 1j * z)
    print(f"  z = {z}: L(1/2+iz) + L(1/2-iz) = {mp.nstr(lhs, 3)}  (~0: FE)")
print("  hence int with (1/2+iz) = - int with (1/2-iz): the mirror")
print("  screw is -g_F. Flipping the transform's sign negates the")
print("  function and its positivity criterion -- not an alternative")
print("  handedness but the same object read on the FE-reflected")
print("  side. The recorded sign is the Euler-product side's.")

print()
print("=" * 76)
print("2. the helix face (v13.753): even g, mirror-invariant kernel")
print("=" * 76)
import sympy as sp
u, v = sp.symbols('u v', real=True)
g = lambda x: x**4 + 3 * x**2 + 1          # model even screw-shaped g
G = lambda a, b: g(a - b) - g(a) - g(-b) + g(0)
print(f"  G_g(u,v) - G_g(-u,-v) for even model g: "
      f"{sp.simplify(G(u, v) - G(-u, -v))}  (identical: the general")
print("  step uses only g(-x) = g(x): G(-u,-v) = g(-(u-v)) - g(-u)")
print("  - g(v) + g(0) = g(u-v) - g(u) - g(-v) + g(0) = G(u,v).)")
f = mp.quad(lambda tt: mp.e ** (-tt**2) * mp.e ** (1j * tt * mp.mpf('1.3')),
            [-mp.inf, mp.inf])
f2 = mp.quad(lambda tt: mp.e ** (-tt**2) * mp.e ** (-1j * tt * mp.mpf('1.3')),
             [-mp.inf, mp.inf])
print(f"  Fourier conventions on even weight e^(-t^2): synthesis with")
print(f"  e^(+itw) = {mp.nstr(f, 8)}, with e^(-itw) = {mp.nstr(f2, 8)}")
print("  (equal, real: the convention's sign cancels for even g,")
print("  exactly as v13.753 records: no residual sign.)")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("The screw overlay holds no factor asymmetry. Its")
print("Laplace face is one-sided, but the mirror prescription")
print("is its own negation via the functional equation -- the")
print("sign is fixed by the Euler-product side, and the")
print("asymmetry species is the transform's arrow (retardation,")
print("already censused at v15.473), living on the log-scale")
print("axis, not a spatial winding. Its helix face is built")
print("from a real EVEN screw function whose increment kernel")
print("-- the Weil kernel itself -- is invariant under the")
print("rapidity reflection: the two winding directions of the")
print("helix carry the same kernel. Door I's screw hiding")
print("place is CLOSED. With v15.473's census, the only")
print("remaining place a swap-odd output could hide is the")
print("absent frame<->canonical dictionary (v15.468 sec.4).")
print("Jeremy's bet stands resolved: factor-asymmetric results")
print("fill the record in the side-pick species; no swap-odd")
print("output exists in the grid, the operator, the sectors,")
print("or the screw.")
