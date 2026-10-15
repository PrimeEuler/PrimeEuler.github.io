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

## 6. Addendum (2026-10-13): the pair encoding

Jeremy's extension: everything on the $n+1$ divisions, via the ratio
$(n+k)/(n-k)$ for $k \le n$. The encoding generalizes from the pair
$(n, 1)$ to an arbitrary pair $(n, k)$ [D]:

$$
z_{n,k} \;=\; \frac{(n-k) + 2i\sqrt{nk}}{\,n+k\,}, \qquad |z_{n,k}| = 1
$$

by $(n-k)^2 + (2\sqrt{nk})^2 = (n+k)^2$; the angle is
$2\arctan\sqrt{k/n}$. Section 1 is the slice $k = 1$. At level $n$,
the values $k = 0, 1, \dots, n$ give exactly $n+1$ points sweeping
the quarter circle from $(1, 0)$ to $(0, 1)$: every pair of division
indices is a point on the circle.

The pair carries its own rapidity $\psi_{n,k} = \tfrac12 \ln(n/k)$
[D]:

$$
\tanh\psi_{n,k} = \frac{n-k}{n+k}, \qquad
\cosh\psi_{n,k} = \frac{n+k}{2\sqrt{nk}} = \frac{\mathrm{AM}}{\mathrm{GM}}
\ \text{of the pair } (n, k), \qquad
\operatorname{sech}\psi_{n,k} = \frac{\mathrm{GM}}{\mathrm{AM}},
$$

and Jeremy's ratio is its hyperbolic cotangent,
$\dfrac{n+k}{n-k} = \coth\psi_{n,k}$ — the boost ratio between the
two division scales. Rapidities add over chains,
$\psi_{n,k} + \psi_{k,j} = \psi_{n,j}$, while the coth factors
multiply: the division lattice is a group in rapidity. The seed
contact of §4 sharpens accordingly [D]:
$\log(m/4) = 2\psi_{m,4}$ — the seed's denominator is the pair
rapidity of $(m, 4)$. Verified symbolically (sympy) 2026-10-13;
deposited as ledger v14.367.

## 7. Addendum (2026-10-13): T(n) − D(n) = A(n) at the hyperbola, and the binary of d(n)

Jeremy's identification: the encoding of §§1–6 is staged on the same
hyperbola family as the Paper A content identity

$$
A(n) = T(n) - D(n), \qquad T(n) = \frac{n(n+1)}{2}, \quad
D(n) = \sum_{k \le n} d(k),
$$

the integrated form of the front recursion
$A(n{+}1) = A(n) + (n+1) - d(n+1)$ (inflow $n+1$ from the growing
triangle's new row, outflow $d(n+1)$ across the front) [D, classical].
$D(n)$ counts the lattice points under the hyperbola $xy \le n$
(Dirichlet), so the identity lives on the hyperbola family
$xy = \mathrm{const}$ — the same family the pair encoding parametrizes
by rapidity, the pair $(n, k)$ having hyperbola constant
$n/k = e^{2\psi_{n,k}}$ [D]. The encoding is thus a coordinate system
on the very curves the divisor content is counted under [I].

The binary of the divisor function: $d(n) \bmod 2$ is the square
indicator — $d(n)$ is odd iff $n$ is a perfect square, since divisors
pair off $(x, n/x)$ except at the self-paired $x = \sqrt n$ [D,
classical; verified to $n = 2000$]. The squares are also exactly the
stations where the encoding goes rational (§2, Euclid points). In
Jeremy's phrase, the binary of $d(n)$ encodes the zero frequency:
the self-paired divisor at the hyperbola's vertex is the unpaired
(DC) mode of the pairing, and $d(n) \bmod 2$ is its detector [I].

The V4 overlay [I]: the divisor content under the hyperbola is
indexed by the four units $U(12) = \{1, 5, 7, 11\}$ — the four
hyperbola sections $X = (r-1)/2 \in \{0, 2, 3, 5\}$ of the Totient
note's apparatus — and the Klein-four character group of $U(12)$
($\chi_{12}$ and its companions) is the Fourier overlay on that
content, carrying the proved complementarity
$\phi_+(r) + \phi_-(r) = 1 \bmod 12$ and the genus split
$\{1, 11\}$ split / $\{5, 7\}$ inert in $\mathbb{Q}(\sqrt3)$
(Totient note, Props. 4.2/4.3, machine-verified). On the encoding's
ruler this is the 12-division case, level $n = 11$: the V4 stations
live on the same divisions.

## 8. Addendum (2026-10-15): the Cayley form

Jeremy's repackaging of §§1 and 6. The components of the encoding
read

$$\operatorname{Re} z_n = 1 - \frac{2}{n+1}, \qquad
\operatorname{Im} z_n = \frac{\sqrt n}{(n+1)/2} = \frac{\mathrm{GM}}{\mathrm{AM}}$$

[D — the imaginary part is the geometric over the arithmetic mean of
$n$ and $1$], and the point itself is a single Cayley transform:

$$z_n = \frac{\sqrt n + i}{\sqrt n - i}, \qquad
z_{n,k} = \frac{\sqrt n + i\sqrt k}{\sqrt n - i\sqrt k}
= \frac{1 + i\,e^{-\psi_{n,k}}}{1 - i\,e^{-\psi_{n,k}}}$$

[D; verified symbolically]. Consequences:

- $|z_{n,k}| = 1$ is manifest: the point is a complex number over
  its own conjugate, a pure phase by construction.
- $z_{n,k} = \left(\frac{\sqrt n + i\sqrt k}{\sqrt{n+k}}\right)^2$:
  the station is the *square* of the normalized $(\sqrt n, \sqrt k)$
  direction, so its angle is $\varphi_{n,k} = 2\arctan\sqrt{k/n}$,
  and the inverse Cayley transform returns the rapidity directly,
  $\frac{1 + z_{n,k}}{1 - z_{n,k}} = i\sqrt{n/k} = i\,e^{\psi_{n,k}}$,
  i.e. $\cot(\varphi_{n,k}/2) = e^{\psi_{n,k}}$ [D]. Chains multiply
  the real Cayley arguments $e^{-\psi}$ — rapidities adding, as in
  §6 — and $\varphi = \pi/2 - \mathrm{gd}\,\psi$ is the Cayley map's
  angle law, the transposed Gudermannian of the literature scan [D].
- The full pair ratio of §6 has no separate point; it is the secant
  of the same station angle:

$$\frac{n+k}{n-k} = \coth\psi_{n,k} = \frac{1}{\operatorname{Re} z_{n,k}}
= \sec\varphi_{n,k} = \frac{|w|^2}{\operatorname{Re}(w^2)},
\qquad w = \sqrt n + i\sqrt k$$

[D]. In Cayley language it is the *real* transform
$\frac{1+x}{1-x}$ at $x = k/n$, where $z_{n,k}$ is the *imaginary*
transform at $\sqrt x$: one ratio, read on the real axis as $\coth$
and on the circle as the station [I].

*Marking: [D] derived/verified identity · [I] interpretation ·
[O] open/probe-pending.*
