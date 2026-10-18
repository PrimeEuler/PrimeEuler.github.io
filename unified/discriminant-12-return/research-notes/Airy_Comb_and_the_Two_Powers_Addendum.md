# Addendum: The Airy Comb and the Two Powers of the Machine

*Sandbox research note — Discriminant-12 Return / Cone project.
Addendum to "The Diameter–Secant Machine and the Gravity Road"
(ledger v14.550) and to the unit-circle encoding note (v14.366 et
seq.). Formulation: Jeremy (the GM-wrap description of the unwrap;
the cone-area question — conversation, 2026-10-18). Computations:
sandbox (LIttle Euler), 2026-10-18, consolidated in the producer
`airy_powers_probe.py` deposited alongside this addendum; every
number below is its output. Status: §§1–3 are computed or exact
[D]; the dictionary remark of §3 is a candidate, tagged [O]. No
derivation of $G$ is claimed; the hierarchy item of the parent note
remains open.*

## 1. The Airy comb is the bouncer's pure-number factor [D]

The neutron quantum bouncer (qBounce) has level scale
$\varepsilon_0 = (\hbar^2 m_n g^2/2)^{1/3} = 0.6016$ peV and levels
$E_n = \varepsilon_0 |a_n|$, $a_n$ the zeros of $\mathrm{Ai}$.
From constants and zeros alone the transition comb is
$\nu_{13} = 463.0$ Hz, $\nu_{1\to7} = 1120.5$ Hz,
$\nu_{2\to9} = 1141.7$ Hz — against the reported $\sim$1120 Hz and
$\sim$1142 Hz. The measured gravitational spectroscopy therefore
already has the factorised shape (pure-number factor) × (scale);
its factor is Airy-zero differences, and its source is the Earth,
which is why it returns $g$, not $G$.

The quarter is shared with the project's forms: the zeros obey
$|a_n| \approx [(3\pi/2)(n - \tfrac14)]^{2/3}$ (0.76% at $n=1$,
0.003% at $n=12$) — the Maslov/Langer quarter, the family of the
1/4 Casimir and of $(j+\tfrac12)^2$ — and the project signature
function's zeros obey $j_{1,s} \approx \pi(s + \tfrac14)$
(2.49% at $s=1$, 0.056% at $s=8$). Clean negative: dimensionless
ratios of Airy-zero differences sit near small rationals
(denominator $\le 36$) only at the 0.03–0.15% level chance
predicts. No free hit.

## 2. The unwrap, restated geometrically [D]

Jeremy's description: take every circle of diameter $n+k$; the
secant divides the diameter into its AM divisions $n$ and $k$;
wrap the circle onto the unit circle (divide by the AM,
$(n+k)/2$), carrying the point at the half-chord, the GM
$\sqrt{nk}$. The result is exactly the Cayley pair form
$z_{n,k} = (\sqrt n + i\sqrt k)/(\sqrt n - i\sqrt k)$ — worst
discrepancy $1.7\times10^{-16}$ over random pairs. The unwrapping
power 1/2 of the parent note is therefore not an algebraic
accident: *divide by the AM, rise by the GM* — the power map is
the geometric mean of the AM divisions.

## 3. Where the 2/3 lives [D], and the dictionary candidate [O]

The cone's own Archimedean share is 1/3 (volumes
cone : sphere : cylinder $= \tfrac13 : \tfrac23 : 1$); the 2/3 is
the sphere's (its surface is also exactly 2/3 of the
circumscribing cylinder's total area) and the parabolic
segment's: a segment is exactly **2/3 of its circumscribing
parallelogram**, any $f$, any chord height (symbolically
verified). The segment's area is $(8/3)\sqrt f\, h^{3/2}$ — the
**3/2** is height$^1$ times width$^{\sqrt h}$: $3/2 = 1 + 1/2$,
the second summand being the GM square root of §2.

The parabola carries a second, independent exact 2/3: its evolute
(the locus of curvature centres, envelope of its normals) for
$f = 1/2$ is the semicubical parabola
$27X^2 = 8(Y-1)^3$, cusp at $(0,1)$ — i.e.
$Y - 1 = \tfrac32 |X|^{2/3}$ (symbolically verified).

The mechanism tying the spectral 2/3 to the machine is then
classical: the bouncer's phase-space boundary is a parabola
($p^2 \propto E - mgz$), so its action is an Archimedean segment,
$\propto E^{3/2}$; Bohr–Sommerfeld with the Maslov quarter gives
$E_n \propto (n - \tfrac14)^{2/3}$, the asymptotics of §1. Hence
$2/3 = 1/(1 + \tfrac12)$: the Airy warp and the GM unwrap are the
same square root, once as a phase-space width, once as a mean.
Measured power laws agree: wrapped angles $\varphi_n \sim
n^{-0.4997}$, zeros $|a_m| \sim m^{0.6668}$. (Composing the two at
one index gives $|a_n|\,\varphi_n^{4/3} \to (36\pi^2)^{1/3}$; the
4/3 is forced by exponent arithmetic and is recorded as
bookkeeping, not signal.)

Dictionary candidate [O]: the pending $t \leftrightarrow x$ entry
of the Suzuki thread acquires a concrete candidate form — the
cone coordinate read as *action*, i.e. as parabolic-segment area,
with the warp $E \propto J^{2/3}$ as its spectral shadow. Unbuilt;
stated here as the pointer this addendum exists to record.
