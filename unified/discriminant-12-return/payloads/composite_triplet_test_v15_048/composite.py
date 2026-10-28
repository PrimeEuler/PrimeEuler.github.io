"""Composite-triplet test: phi^I := chi^dagger sigma^I chi vs the AM gravity triplet.
Readings: (i) dynamics = spinor action (v14.990 family) -- chi's stress-energy is v15.014's;
(ii) dynamics = AM functional W = C * A_B[phi] with composite phi -- C is a coefficient of W."""
import sympy as sp

r, th, ph = sp.symbols('r theta phi', positive=True)
# --- the label-mimicking texture: hedgehog spinor with chi^dagger sigma chi = position vector
eta = sp.Matrix([sp.cos(th / 2), sp.exp(sp.I * ph) * sp.sin(th / 2)])
chi = sp.sqrt(r) * eta
def bloch(k):
    s = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])][k]
    return sp.simplify(sp.expand_complex((chi.H * s * chi)[0]))
print("hedgehog: Bloch vector =", [sp.trigsimp(bloch(k)) for k in range(3)], " = (x, y, z): the composite reproduces the label field pointwise")
d_r = sp.diff(chi, r); d_t = sp.diff(chi, th); d_p = sp.diff(chi, ph)
gn2 = sp.simplify((d_r.H * d_r)[0] + (d_t.H * d_t)[0] / r**2 + (d_p.H * d_p)[0] / (r**2 * sp.sin(th)**2))
print("|grad chi|^2 =", sp.simplify(sp.factor(sp.expand_complex(gn2)) / 1), "= (2 + cos th)/(2 r (1 + cos th)) -> kinetic density (1/2)|grad chi|^2 ~ 1/r, theta-dependent,")
print("   string-singular at theta = pi (Wu-Yang patch needed): NOT a homogeneous source")

print("\n--- reading (i): homogeneous chi, amplitude on the v15.014 coasting tracker r = sqrt(2) ln tau")
import numpy as np
for tau in [10, 100, 1000, 3000]:
    print(f"   tau={tau:>5}: C_eff := |phi| = |chi|^2 = 2 (ln tau)^2 = {2 * np.log(tau)**2:8.2f}  (drifts; a constant C is required)")

print("\n--- reading (ii): C factors out of W for ANY phi, composite or not:")
C, AB = sp.symbols('C A_B')
print("   W = C * A_B[phi] identically -- compositeness of phi cannot reach the coefficient C.")
print("   homogeneous chi: d_i phi = 0 -> B = 0 -> A_B = 0 -> W = 0 (the AM energy is spatial-gradient energy).")
print("   homogeneous nonzero Bloch vector also picks a direction: anisotropic, not the FLRW source.")
print("   textured chi (labels): kinetic density ~ 1/r from part 1 -- inhomogeneous. Both sub-readings fail.")
