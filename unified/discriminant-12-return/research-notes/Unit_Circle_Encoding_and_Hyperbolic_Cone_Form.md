# The Unit-Circle Encoding and Its Hyperbolic (Cone) Form

*Sandbox research note — Discriminant-12 Return / Cone project.*
*Formulation: Jeremy (station discretization 2026-10-11; complex encoding
assembled and corrected in conversation 2026-10-13). Write-up: sandbox
(LIttle Euler), 2026-10-13. Status: the identities of §§1–3 are exact
[D]; the seed contact of §4 is an interpretation [I] with an open
finite probe [O]. No seed or residual claim is made by this note.*

## 1. The encoding

For integer $n \ge 1$ put

$$
z_n \;=\; \Bigl(1 - \frac{2}{n+1}\Bigr) \;+\; i\,\frac{\sqrt{n}}{(n+1)/2}
\;=\; \frac{(n-1) + 2i\sqrt{n}}{\,n+1\,}.
$$

The picture is division units: the unit circle has diameter $2$; divide
the diameter into $n+1$ equal parts of length $2/(n+1)$. The point sits
one division in from the rim — real part $1 - 2/(n+1)$ — and rises to
the circle; in division units its lattice position is $(1, \sqrt{n})$.

It is exactly on the circle for every $n$ [D]:

$$
|z_n|^2 = \frac{(n-1)^2 + (2\sqrt{n})^2}{(n+1)^2}
       = \frac{n^2 + 2n + 1}{(n+1)^2} = 1,
$$

the Pythagorean identity $(n-1)^2 + (2\sqrt n)^2 = (n+1)^2$. Its angle
is $\varphi_n = 2\arctan(1/\sqrt{n})$, sweeping monotonically from
$90^\circ$ at $n=1$ down toward the rim point $(1,0)$ as $n \to \infty$.

The imaginary part is Jeremy's station radius (2026-10-11): for the pair
$(n, 1)$, $\mathrm{GM}/\mathrm{AM} = \sqrt{n}\,/\,\frac{n+1}{2}
= 2\sqrt{n}/(n+1)$ — the radius of station $n$ in the unit-circle toy
(the hardware lineage of the V4 waveguide build sheet).

## 2. Stations and special points

- $n = 1$: $z_1 = (0, 1)$, the top of the circle; station radius $1$
  (the mouth).
- $n = 3$: $z_3 = \tfrac12 + i\tfrac{\sqrt3}{2}$, the exact $60^\circ$
  point — the 30-60-90 station, radius $\sqrt3/2$.
- $n = k^2$: $(n-1,\ 2\sqrt n,\ n+1) = (k^2-1,\ 2k,\ k^2+1)$ is Euclid's
  triple, so the encoding hits the rational Pythagorean points:
  $n=4 \to (3/5, 4/5)$, $n=9 \to (4/5, 3/5)$, $n=16 \to (15/17, 8/17)$.
- The rim defect is source-shaped [D]: $1 - \mathrm{Re}\,z_n
  = \dfrac{2}{n+1}$, and the chord to the rim is
  $|1 - z_n| = \dfrac{2}{\sqrt{n+1}}$.

## 3. The hyperbolic (cone) form

On the cone the circular functions lift to hyperbolic ones
($\sin \to \sinh$, Jeremy's helix dictionary). Give mode $n$ the
rapidity

$$
\psi_n = \tfrac12 \ln n, \qquad e^{\psi_n} = \sqrt{n},
$$

so a cone boost of mode $n$ is multiplication by $\sqrt n$. The point
$(\cosh\psi_n, \sinh\psi_n)$ on the unit hyperbola
$\cosh^2 - \sinh^2 = 1$ is [D]

$$
\cosh\psi_n = \frac{n+1}{2\sqrt n} = \frac{\mathrm{AM}}{\mathrm{GM}},
\qquad
\sinh\psi_n = \frac{n-1}{2\sqrt n}.
$$

The two pictures are one point read in the two signatures [D]:

$$
\tanh\psi_n = \frac{n-1}{n+1} = \cos\varphi_n,
\qquad
\operatorname{sech}\psi_n = \frac{2\sqrt n}{n+1} = \sin\varphi_n.
$$

The circle's height is the hyperbola's sech; the station radius
$\mathrm{GM}/\mathrm{AM}$ is $\operatorname{sech}\psi_n$; its reciprocal
$\mathrm{AM}/\mathrm{GM}$ is $\cosh\psi_n$. The AM–GM inequality
$\cosh\psi_n \ge 1$ is the statement that the station sits inside the
circle, with equality only at $n = 1$.

## 4. Contact with the infinite seed

The project's infinite seed is $y_m = \Phi(m)/\log(m/4)$ (v14.250).
Since [D]

$$
\log(m/4) \;=\; 2\,(\psi_m - \ln 2),
$$

the seed's denominator is exactly twice the rapidity of mode $m$
measured from the origin $m = 4$: the seed is $\Phi$ per unit rapidity
[I]. The encoding therefore supplies canonical candidate modifications
of the seed in the cone's own coordinate [O]:

- **sech-damped seed:** $y_m \cdot \operatorname{sech}\psi_m
  = y_m \cdot \dfrac{2\sqrt m}{m+1}$;
- **tanh modulation:** $y_m \cdot \tanh\psi_m
  = y_m \cdot \dfrac{m-1}{m+1}$ (a near-identity at seed modes, since
  $\varphi_m$ is small there);
- **rim-defect seed:** $y_m := \dfrac{2}{(m+1)\log(m/4)}$, replacing
  $\Phi$ by $1 - \mathrm{Re}\,z_m$ — the same $1/(m \log m)$ size class
  as $\Phi(m)/\log(m/4)$ at the bank start $m = b$.

A finite probe of these candidates (production Regions 2–3 machinery,
unchanged bank support and tail, composed-residual metric against the
frozen v14.353 residual buffers) was commissioned by Jeremy and is
running in the sandbox as of this note's deposit. Its outcome decides
whether §4 is machinery or only a dictionary; this note claims the
dictionary only.

## 5. Provenance

Station radii $\sqrt n / \frac{n+1}{2}$ on $n+1$ divisions of the unit
circle: Jeremy, 2026-10-11 (unit-circle toy lineage; workspace record).
Complex encoding: assembled 2026-10-13 in conversation; Jeremy's
corrections fixed the real part first to $2/(n+1)$ (diameter $2$,
$n+1$ divisions) and finally to $1 - 2/(n+1)$. All identities above
verified symbolically the same day. A repo-wide search on 2026-10-13
found no prior occurrence of this dictionary (no sinh/cosh/tanh/sech/
rapidity/"unit circle" anywhere in the repository).

*Marking: [D] derived/verified identity · [I] interpretation ·
[O] open/probe-pending.*
