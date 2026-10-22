# EFT play: the hot-bath fixed point in cone coordinates — 2026-10-21 (sandbox)

DICTIONARY (derived from the corpus's epicycle radii, machine-verified):
epicycle radii A=sqrt(x), B=sqrt(y) with x=T+X, y=T-X, Y=sqrt(xy); ellipse
semi-axes a=A+B, b=|A-B|. Then
  e^2 = 4AB/(A+B)^2 = 2Y/(T+Y),    q^2 = 1 - e^2 = (T-Y)/(T+Y),
verified against direct ellipse geometry on 2000 random ellipses
(max error 6e-16). So v3.4's shape coordinate q is a cone function:
q = sqrt((T-Y)/(T+Y)).

THE FIXED POINT IS A RAY PAIR. v3.4's hot-bath attractor q0 = 1/sqrt(3)
(q0^2 = 1/3) becomes (T-Y)/(T+Y) = 1/3, i.e. Y = T/2, i.e. the cone
direction
  X : Y : T = sqrt(3) : 1 : 2,
two generators of the cone (X = +/- (sqrt3/2) T, Y = T/2). Null-coordinate
ratio on the ray: (T+X)/(T-X) = (2+sqrt3)/(2-sqrt3) = 7 + 4 sqrt(3)
= 13.92820323... The bath does not select a point or a scale; it selects
a DIRECTION — every orbit, whatever its size (T free), is driven to the
same ray. (Figure fig_eft_play.png: flow + cone with canonical mesh.)

FLOW CHECK: the reduced hot-limit shape flow dq/dt = -C(3q^2-1)/q
(the sign structure of v3.4's <Ls> with s = 1-q) attracts from every
start: e from 0.997, 0.954, 0.527, 0.141 all -> e0 = sqrt(2/3) = 0.816497.

THE G LEVER (lever.py). Carrying out the EFT Note's unfinished averaging
for a CENTRAL perturbation: energy and L are conserved, e is secularly
fixed, so on the cone the point can only rotate about the T axis — and
the Lie-Poisson bracket generates exactly that from H = eps*T
(dX/dt = eps*Y, dY/dt = -eps*X; numerically a pure rotation). The GR
1/r^3 term is such a perturbation: its entire secular effect is that
rotation, at per-orbit angle
  Delta-varpi = 6 pi mu / (c^2 p),   p = (2T-2Y)/sqrt(2T+2Y)
(semi-latus rectum in cone coordinates; time-average <1/r^3> =
1/(a^3 (1-e^2)^{3/2}) verified numerically against the cone form).
Mercury through the cone formula: 5.0187e-7 rad/orbit = 42.98
arcsec/century — the famous 43. So the lever shape exists in the EFT:
a motion that does nothing but turn, whose rate is the coupling.
Honest split: astronomy's rotation levers GM (the product); the lever
on G itself remains the lab hardware (seat null / precession product).

READING FOR THE CONSTANTS HUNT: this is dynamical selection running
inside the corpus — kinematics (cone) + contents (the bath) strike a
balance at a pure number, and the selected object is a ray, the cone's
spin-0-shaped locus (fixed direction, free scale). Same grammar as the
Balance Principle note: structure exact, the number a balance against
contents. Not a fundamental constant; a template with a worked example.
