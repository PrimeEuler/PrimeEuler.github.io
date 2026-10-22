# Phase, Eccentricity, and the Seat at the Apex

## The gravity-selector problem in the cone frame: a compression

*Sandbox research note — workspace draft, 2026-10-22, for review.
Status flags: `G_derived = false`, `kappa_value_derived = false`.
What is derived below is the **shape** of the problem: a chain of
mechanisms, each checked, that compresses "why is gravity weak?"
to a single initial condition with coordinates in the frame.
Tags: [D] derived/verified, [N] numerical verification,
[I] interpretation, [O] open.*

---

## 1. The one proven dynamics is a phase integral

Everything the cone program has *proved* dynamically reduces to a
single act: integrating a phase. In the magnetic-drive closure
(v14.680), the hydrogen lobe shapes were recovered exactly from

$$I_{jm}(\theta) = \frac{1}{2\pi}\int_0^{2\pi} e^{-im\chi}\,
(\cos\theta + i\sin\theta\cos\chi)^j\, d\chi,$$

the phase $\chi$ being the Larmor angle of a null vector precessing
about the cone's drive axis. Every density-side construction that
dropped the phase failed (three negative tests); the phase integral
succeeded to machine precision. **The cone does not accumulate; it
integrates phase.** [D, v14.680]

The phase bookkeeping now closes completely. Exact evaluation of
the binomial moments (only $k \equiv m \pmod 2$ survive) gives,
for all $j \le 4$ and every $m$,

$$I_{jm}(\theta) = (-i)^m\,\frac{j!}{(j+m)!}\,P_j^m(\cos\theta),$$

verified against the associated Legendre functions to $4\times
10^{-15}$. The phase is exactly $(-i)^m$ — independent of $\theta$ —
so the cone's harmonics *are* the spherical harmonics under one
fixed rephasing of the azimuth origin. The rephasing caveat carried
open since v14.680 is closed. [D]

## 2. The phase orbit carries one parameter: eccentricity

The orbit integrated above is circular. On the bicone shell the
inventory is fixed, $L^2 + A^2 = \text{const}$, and the split
between angular momentum $L$ and the Runge–Lenz vector $A$ is the
orbit's eccentricity:

$$e^2 = \frac{A^2}{L^2 + A^2}, \qquad
1 - e^2 = \frac{L^2}{L^2 + A^2}.$$

Slicing a cone generates every conic; eccentricity is the cone's
native continuous parameter, and $e = 0$ (pure $L$) is the single
member whose phase integral gives the quantum lobes. Deforming the
integral with the Kepler squash $\rho = \sqrt{(1-e)/(1+e)}$ at
$e = 0.6$ produces a genuinely new family — the ratio to any
reparametrized Legendre function is $\theta$-dependent — with the
harmonics recovered exactly at $e = 0$. The cone therefore contains
a one-parameter family of "lobes," the Hansen–Bessel sideband
structure of Kepler motion, of which quantum angular structure is
the circular member. [D]/[N]

Eccentricity is dimensionless, $G$-free, and pair-dependent — the
first selector-shaped quantity in the program that comes from the
*proven dynamics* rather than from the inventory.

## 3. The separatrix turns proximity into a logarithm

As $e \to 1$ the orbit period diverges through the complete
elliptic integral,

$$K(e) \;\sim\; \tfrac{1}{2}\ln\!\frac{16}{1-e^2},$$

the classical separatrix asymptotic. This is the one theorem-grade
mechanism dynamics offers for manufacturing a large logarithm from
a continuous parameter: a hierarchy of $e^{45}$ is a proximity of
$1 - e^2 \approx 7\times 10^{-39}$ read through $K$. Fed the pair's
own gravitational smallness (the GR perihelion scale of the
two-body problem), the machine returns $K = 45.8$–$50.2$ against
targets $\psi = 45.31$ and depth $51.53$ — inside the chance band,
recorded and not promoted. The machine is real; what it consumes
is a proximity, and the proximity is the question. [D mechanism;
N inputs]

## 4. Counting cannot manufacture the log

Could the frame's own counting produce the proximity? Three
independent attacks say no.

*Forced integers.* Every native integer of the frame (conductor,
channel counts, shell data, $K = 42$, $85$ moments, orders of the
return matrix $g_{12}$ in $\mathrm{SL}_2(\mathbb{Z}/12)$ and
$\mathrm{SL}_2(\mathbb{Z}/24)$ — all $12$) was tested against the
required exponents $63.67$, $71.10$, $139.79$: no hit; the
congruence/class-group family at conductor $12$ is likewise empty
(closest miss $13.7$ in the log). [N, negative]

*Traces.* The return matrix's traces $\mathrm{tr}(g_{12}^k)$ are an
exact, falsifiable ladder; the baryon census falls strictly between
$\mathrm{tr}(g_{12}^{139}) = 3.17\times 10^{79}$ and
$\mathrm{tr}(g_{12}^{140}) = 1.18\times 10^{80}$. No rung lands.
[N, negative]

*Dwell.* Weight each orbit of the family by its period and count:
$\ln(N_{\text{dwell}}/N_{\text{plain}}) \to 0.6346$, a constant,
while $K_{\max}$ grows like $\ln N$; the mean dwell weight per
shell converges to $\ln 4 + \tfrac12$ exactly. In a census,
degeneracy beats the logarithmic dwell weight — the separatrix
orbits are too few. The log survives only for a **single orbit
seated at the separatrix**, never for an averaged inventory.
[D, negative]

The three negatives are the load-bearing result: they explain
*why* the hierarchy cannot be an output of the frame's counting,
in any of its forms.

## 5. The cosmic orbit: eccentricity is the flatness parameter

There is one orbit in the problem that is seated, not averaged:
the expansion itself. Its conic is the Friedmann equation; its
eccentricity is the flatness parameter; $\Omega = 1$ is the
parabolic slice. The Sciama balance

$$B = \frac{GM_u}{R_u c^2} = \frac{\Omega}{2}$$

closes at exactly $\tfrac12$ at the tangency $\Omega = 1$: the
Hubble volume rides at its own Schwarzschild tangency, and $G$ is
the price of keeping it there — a balance readout, not a
fundamental input. Inflation is the approach mechanism: it
stretches the proximity, $1 - e^2 \to (1-e^2)_i\, e^{-2N}$, and
the elliptic log collapses to the closed form

$$K(e) = N + \tfrac12\ln\frac{16}{(1-e^2)_i} .$$

**The hierarchy log is the e-fold count of the stretch, plus the
initial seat's half-log.** The program's targets price out at
$N = 43.9$ ($\psi$), $50.1$ (depth), $69.7$ (age ratio); the
standard flatness solution $N \approx 60$ sits in the same band
with no exact seat — stated plainly, not fitted. [D form; N values]

## 6. The seat cannot be a spectrum

The remaining term, $(1-e^2)_i$, is small in the formula only
through its logarithm, and no discrete structure can supply it:
every algebraic or group-theoretic quantity at conductor $12$
(the fixed points $(1\pm\sqrt3)/2$ of $g_{12}$, the unit $1/\varepsilon$,
$1/12$, down to $1/85$) lies in $[0.01, 1]$, contributing
$+1.9$ to $+3.6$ to the log — garnish, never the meal. Imported
spectra fail the frame's own spec: the loop-quantum-gravity area
eigenvalue carries $\ell_P^2$ as a prefactor, and $\ell_P$
contains $G$ — the unknown re-entering as a unit — while its
dimensionless remnant is the ordinary angular-momentum eigenvalue
whose minimal-share content is §4's dwell computation. **The seat
is an initial condition, not an eigenvalue.** [D]

## 7. The seat, the balance, and the point at 0

The frame's single structural constant is the half-offset:
$(j+\tfrac12)^2 = \mathrm{AM}^2$, the secant offset $(n-k)/2$,
$\text{offset}^2 = \tfrac14$. It appears signed at the two ends of
the cosmic chain:

- the **seat at $-\tfrac12$** — the parabola's vertex, the spin-0
  scalar's place (the payer portrait of the induced-gravity
  analysis: a scalar is what generates mass in every known
  sector), the beginning;
- the **balance at $+\tfrac12$** — $B = \Omega/2$ at $\Omega = 1$,
  the outcome.

They are the two rails of the fundamental cell, exactly one unit
apart. And the point the cell straddles — **0, the cone's apex**,
the bicone's gluing point, the origin every phase is measured
from and which is never itself integrated — is the initial
condition: the one point the machinery cannot produce, because
the cone is generated from it. A beginning exactly on the tangency
($1 - e^2 = 0$) makes the count diverge; a finite universe is the
price of the beginning having sat off the tangency by exactly the
proximity the hierarchy records. In plain language, the
outstanding initial condition is the big bang, and it now has
coordinates. [I, on D above]

The chain, end to end: **the cone selects, the stretch counts,
the bang seats.** Gravity is what the count costs (Sciama);
quantization is what the phase does (single-valuedness); the one
thing neither supplies is where the apex was seated.

## 8. Companion closures

**Stark effect = the cone's offset.** The first-order shift
$\Delta E = \tfrac32 n (n_1 - n_2) F$ is $3nF \times \text{offset}$
for the diameter-secant offset $(n_1-n_2)/2$ of the parabolic pair
— the cone's two parabola families are the Stark coordinates. The
$(n_1,n_2,m)$ enumeration reproduces the textbook tables exactly
($n=2$: $\{+3{:}1, 0{:}2, -3{:}1\}$; $n=3$: $\{+9{:}1, +4.5{:}2,
0{:}3, -4.5{:}2, -9{:}1\}$; totals $n^2$). [D]

**Rydberg revivals.** A packet on the cone-derived spectrum
$E_n = -\mu\kappa^2/(2\hbar^2 n^2)$ (v14.680: form and prefactor
forced) shows the full revival structure: classical recurrences at
$T_{\mathrm{cl}} = 2\pi\bar n^3$, mirror enhancement at
$T_{\mathrm{rev}}/2$, and a full-revival peak of $0.80$–$0.95$
(sharpening as the packet narrows) at $t \approx 1.01\,T_{\mathrm{rev}}$,
$T_{\mathrm{rev}} = \tfrac{4\pi}{3}\bar n^4$. The $\sim$1% offset
from the $E''$ time is the exact ladder's higher-order terms; the
precise peak is a Diophantine phase alignment on the ladder, not
a local derivative — the revival is the ladder's phase closing on
itself, the time-domain instance of §1's one dynamics. [N]

---

*Claimed:* the phase-integral dictionary including phases (§1);
the eccentricity family and its $e = 0$ member (§2); the census
negatives (§4); the Stark dictionary (§8). *Verified numerically:*
the eccentric deformation, the revival structure, the trace
ladder, the dwell constants. *Interpretation, flagged as such:*
the cosmic-orbit reading (§5, §7) — Sciama's stance, adopted as
the program's position since 2026-10-21. *Not claimed:*
$G_{\text{derived}}$, any exact seat for $N$, any value for the
seat. The far-residual certification (v14.585 actions 3–4), the
program's outstanding deliverable, is unaffected by and
independent of this note.
