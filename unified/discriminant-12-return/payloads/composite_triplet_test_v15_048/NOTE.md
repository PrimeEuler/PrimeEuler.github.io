# Composite-triplet test: is the AM source's amplitude the Bloch amplitude of a pair spinor? (Sandbox)

**Question (Jeremy, 2026-10-28).** The pair spinor's Bloch triplet
n = chi^dagger sigma chi has amplitude |n| = |chi|^2 — slaved by
purity, and = 1 at the hbar-circle normalization (|chi|^2 = 1,
T = 1/2). The gravity source is a triplet with amplitude C
(W = C A_B, kappaC = 1 a matching). If the gravity triplet WERE the
Bloch triplet of a pair spinor, would C be derived (= kappa^-1 by
construction) instead of matched? Parents: v14.989/v14.996 (AM
triplet and its SVT certificate), v14.990 (spinor), v15.014
(spinor-source test), v15.046 (the door pointer). **Verdict:
NO — the route closes, with a sharper diagnosis: C is a
constitutive coefficient of the action functional, not a field
norm, and compositeness slaves field norms only.**

## The two readings, both fail [D]

The identification needs a dynamics. There are two candidates, and
they fail for different exact reasons.

**(i) Dynamics = the spinor action.** Then the source is chi
itself; v15.014 already fixed its stress-energy (stiff at V = 0;
coasting only on the chargeless exponential tracker). The
composite's amplitude on that tracker is
C_eff(tau) := |phi| = |chi|^2 = 2 (ln tau)^2 — 10.6 at tau = 10,
128 at tau = 3000: it DRIFTS logarithmically. The AM source needs
a constant C. (A homogeneous nonzero Bloch vector also picks a
preferred direction — anisotropic, not the FLRW source at all.)

**(ii) Dynamics = the AM functional with composite phi.** Then
W[phi] = C * A_B[phi] and **C factors out identically for any phi,
composite or elementary** — the substitution cannot reach it.
Sub-cases: homogeneous chi gives d_i phi = 0, hence B = 0,
A_B = 0, W = 0 — the AM energy is entirely spatial-gradient
energy of labels, and a homogeneous composite has none. The
label-mimicking texture exists and is exact: the hedgehog spinor
chi = sqrt(r)(cos(th/2), e^{i ph} sin(th/2)) has
chi^dagger sigma chi = (x, y, z) pointwise — but its kinetic
density is (1/2)|grad chi|^2 = (2 + cos th)/(4 r (1 + cos th))
~ 1/r, angle-dependent and string-singular at th = pi (the
Wu–Yang patch structure of the monopole bundle): an inhomogeneous
1/r energy, not the homogeneous C/a^2 source.

## Diagnosis [D/I]

Amplitude slaving (|n| = tr chi chi^dagger) constrains a FIELD
VALUE — the pointwise norm of a bilinear. The triplet's C is not a
field value: in W = C A_B it is the coefficient of the gradient
invariant — an elastic modulus, a material constant of the action.
Field compositeness can slave the former and is structurally
incapable of touching the latter. The "1 = 1" rhyme is thereby
located: the spinor's normalized triplet amplitude is a statement
about a field at the hbar-circle normalization; kappaC = 1 is a
statement about an action coefficient in gravitational units.
Different categories.

**Residue for the park (v14.916):** the mechanism the weld waits
for must slave an ACTION COEFFICIENT, not a field norm — a sharper
requirement than the record had. The spectrum comparison against
the v14.996 certificate (P = 3H, Q tau^2 = 3k^2 + 4) is not
reached: it presupposes a background identification, which fails
upstream in both readings. Scope: pointwise composite
phi^I = chi^dagger sigma^I chi, the deposited spinor action
family, and the AM functional as deposited. G not derived;
Suzuki quarter parked.

**Payload:** composite.py, this NOTE.
