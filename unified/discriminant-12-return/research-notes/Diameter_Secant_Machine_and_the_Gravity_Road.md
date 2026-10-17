# The Diameter–Secant Machine and the Gravity Road

*Sandbox research note — Discriminant-12 Return / Cone project.*
*Formulation: Jeremy (diameter/secant reading of the pair form; the
double-paraboloid = dumbbell-on-a-fiber identification; the spun-top /
vector-model reading; the mass–frequency precession proposal — all in
conversation, 2026-10-17). Write-up: sandbox (LIttle Euler), 2026-10-17.
Status: §1 is exact [D] and was numerically verified at deposit; §§2–3
mix sourced experimental fact [D] with identification [I]; the open
items are tagged [O]. Companion interactive page deposited alongside
(`Diameter_Secant_Machine.html`). This note makes no derivation claim
for $G$; §3 is a status assessment, and its two open items are stated
as open.*

## 1. The machine [D]

The pair form of the unit-circle encoding (research note
*Unit_Circle_Encoding_and_Hyperbolic_Cone_Form*, §§6–8; ledger
v14.366/v14.367/v14.441) is
$z_{n,k} = \bigl((n-k) + 2i\sqrt{nk}\bigr)/(n+k)$,
$\psi_{n,k} = \tfrac12 \ln(n/k)$,
$(n+k)/(n-k) = \coth\psi_{n,k} = \sec\varphi_{n,k} = 1/\mathrm{Re}\,z_{n,k}$,
$\varphi_{n,k} = 2\arctan\sqrt{k/n}$.
Jeremy's geometric reading (2026-10-17) is the altitude theorem drawn
on the pair's own circle:

- Draw the circle of **diameter $n+k$**. The vertical secant line
  splits the diameter into segments $n$ and $k$; it therefore sits at
  centre-offset $(n-k)/2$, and its **half-chord is $\sqrt{nk}$** —
  Thales' altitude, the geometric mean of the two segments.
- Hence $(n+k)/(n-k)$ is **sum over difference of the split**: the
  trigonometric secant of the angle is the position ratio of the
  secant line.
- The radius to the chord's end is the AM, and it decomposes as
  $\mathrm{AM}^2 = \mathrm{offset}^2 + \mathrm{GM}^2$. The AM–GM
  inequality is the statement that a half-chord never exceeds the
  radius, with equality iff the secant is centred ($n = k$).
- The secant's foot, lifted to (AM, offset) coordinates, lies on the
  rectangular hyperbola $u^2 - v^2 = nk$, rapidity-parametrised, whose
  light-cone coordinates are the pair itself: $u + v = n$,
  $u - v = k$. A rest mass sits at the vertex ($v = 0$,
  $u = \sqrt{nk}$); the seed already treats mass this way,
  $\log(m/4) = 2\psi_{m,4}$ (encoding note §4).
- At fixed $k$ the chord's endpoint walks the parabola
  $h^2 = 2k\,(d + k/2)$ in (offset, half-chord) coordinates — vertex
  at $-k/2$, focal length $k/2$. At $k = 1$: vertex $-1/2$,
  $f = 1/2$, the V4 numbers.

Jeremy's compression, verbatim: *"GM factor hyperbolas define the
cone, their shadow is a chord on the circle, and the half chord
centers the AM."* Pedigree: every component is classical (Thales'
semicircle, Euclid's mean proportional, Ptolemy's half-chords); the
literature scan of the parent encoding (ledger v14.414) found the
components near-miss/classical and the assembly not found. The hinge
between the circle and hyperbola readings is the Gudermannian, in
the transposed form $\varphi = \pi/2 - \mathrm{gd}\,\psi$ recorded
by that scan. The same diagram hosts the standard kinematics:
rapidity chains = relativistic velocity composition on the mass
shell $u^2 - v^2 = nk$; the parabola family = Galilean trajectories;
the assembly precessing = the Larmor / vector model of §2.

## 2. The same cast in the laboratory

The double paraboloid in meridian profile is an hourglass — two
lobes pinched at one centre. **A Cavendish dumbbell is that
silhouette made solid, and the torsion fibre is its axis** (Jeremy,
2026-10-17) [I]. The balance is an angular instrument living on the
ladder's winding coordinate; spun, the dumbbell is a **symmetric
top**, the one rotor whose orientation wavefunctions are exactly the
spherical objects (Wigner $D^j_{mk}$), and its precession cones are
the ladder rungs — sphere circles in the planes $x = m/J$ of radius
$\sqrt{1 - (m/J)^2}$ (axis lock, 2026-09-28/29). None of this is
metaphor about the current literature; it is a description of it [D]:

- The most precise $G$ (Gundlach–Merkowitz 2000, 14 ppm) was
  measured with the torsion balance on a **continuously rotating
  turntable**, fibre held untwisted by feedback, attractor masses
  rotating around it. "Spin it like a gyroscope" is the state of
  the art, not a conceit.
- The levitated-rotor groups have built the dumbbell itself: a
  silica rotor of **two fused 150 nm spheres** whose librational
  motion — "simultaneously a perfect linear and torsional pendulum"
  — was cooled to its quantum ground state in two axes (Vienna /
  TU Wien / Ulm, *Nature Physics*; single-axis and three-mode
  feedback results from ETH Zürich, Novotny–Frimmer). Stated aims:
  quantum torque sensing, rotational matter-wave interferometry.
- Gravity Probe B already flew the gyroscope as a gravity readout
  (geodetic and frame-dragging precession), with $GM$ products and
  GR factors as its observables.

One design consequence [D mechanics, I as proposal]: a uniform
field torques a rotor's orientation only through a centre-of-mass
offset. The groups' dumbbell is symmetric by construction; an
**asymmetric dumbbell** (unequal spheres, CM displaced by $l$) is a
quantum pendulum in Earth's field, libration frequency
$\sqrt{Mgl/I}$ — qBounce's angular sibling (Airy replaced by
Mathieu). A mass/frequency combo (choice of $I$, $l$, drive
frequency) that makes precession commensurate with the rung comb
$E_j = \hbar^2 j(j+1)/2I$ is the precise form of Jeremy's
"precess over the sphere with our nodes and antinodes" [I].

## 3. The $G$ assessment

**The $\alpha$ precedent** [D, staged bicone-dipole note]: the
elimination worked because $\alpha$ is dimensionless and hydrogen
supplied a measured observable (the H($2p$) lifetime) whose factor
was the cone's own SO(4,2) dipole matrix element:
$1/\alpha = 137.4 \pm 2.2$, no $\alpha$ input. (The note's §3
KS-bridge repair is a separate staged item.)

**The wall** [D]: $G$ is dimensionful; no geometry outputs
kilograms. The only legitimate targets are dimensionless:
$\alpha_G(m) = Gm^2/\hbar c$ ($\approx 5.9 \times 10^{-39}$ for the
proton) and Dirac's force ratio
$e^2/(4\pi\varepsilon_0 G m_p m_e) \approx 2.3 \times 10^{39}$.
Mass is *not* the obstacle: §1 gives it a home (hyperbola vertex;
rapidity against the reference 4).

**The data map** [D]: atom-interferometric $G$ with calibrated
source masses (Rosi et al. 2014, $\sim 1.5\times10^{-4}$) isolates
$G$ against a *classical* Newtonian geometry integral; qBounce
measures Airy-state transition frequencies (now to
$|1\rangle\to|7\rangle \approx 1120$ Hz) with Earth's $g$ as the
fit parameter — the source is the planet, so it is not a $G$
measurement; the torsion corpus (CODATA relative uncertainty
$2.2\times10^{-5}$) is discordant and its factor is apparatus
mechanics. There is no gravitational hydrogen: no two-body
gravitational bound system with measured levels.

**The two missing pieces** [O]:
(i) a *hierarchy generator* — the cone's arithmetic natively makes
small rationals, roots and mild exponentials ($137$ is at home);
$10^{39}$ in ladder variables means rapidity $\psi \approx 45$,
for which no structure in the current toolset exists;
(ii) a *factorised observable* — a measured number of the form
(cone/Wigner factor) × (gravitational coupling), the way the H($2p$)
lifetime was (SO(4,2) factor) × $\alpha$-physics. The QGEM/BMV
programme (Bose; Marletto–Vedral) is the institutional search for
exactly such an observable (gravity-mediated entanglement);
§2's asymmetric quantum pendulum above a calibrated source mass
would be a rotor-shaped instance. Neither exists as data.

**Verdict.** What the cone unifies today is *form*: one cast —
cone, paraboloid pair, chord and hyperbola, dumbbell on an axis —
recurs from Euclid through hydrogen's representation theory to the
current $G$ and quantum-rotor laboratories. Unification of *law*
stands open at exactly the two points named. Form first is the
historical order (Apollonius to Kepler/Newton: ~1,800 years).

## Deposit record

Files: this note and `Diameter_Secant_Machine.html` (interactive:
$n$/$k$ sliders; circle/secant panel; $u^2-v^2=nk$ hyperbola panel
with light-cone readouts; 3D cone with canonical mesh, section
circle at $T=\mathrm{AM}$, chord as the hyperbola's shadow).
Workspace originals in `d12/explorations/unit-circle-secant/`.
§1 identities verified numerically at deposit over a grid of
$(n,k)$; the page's three panels were rendered and inspected
locally before deposit.
