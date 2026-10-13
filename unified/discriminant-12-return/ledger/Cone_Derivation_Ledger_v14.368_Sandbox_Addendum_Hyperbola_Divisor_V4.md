# Cone Derivation Ledger v14.368 — Sandbox addendum 2 to v14.366: T(n) − D(n) = A(n) at the hyperbola, the binary of d(n), and the V4 overlay

Sandbox track (our Lane B). Second addendum to v14.366, at Jeremy's
direction (2026-10-13). The research note
`research-notes/Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md`
is extended with a §7 carrying this content (note updates pushed and
byte-verified with this entry). Classical components [D]; the
encoding identification is Jeremy's [I]. No seed or residual claim.

## The content identity at the hyperbola

Jeremy's identification: the §§1–6 encoding is staged on the same
hyperbola family as the Paper A identity

$$A(n) = T(n) - D(n), \qquad T(n) = \frac{n(n+1)}{2}, \quad
  D(n) = \sum_{k \le n} d(k),$$

the integrated form of the front recursion
$A(n{+}1) = A(n) + (n+1) - d(n+1)$ [D, classical]. $D(n)$ counts
lattice points under $xy \le n$ (Dirichlet); the pair encoding of
v14.367 parametrizes the same hyperbola family by rapidity, the
pair $(n, k)$ having hyperbola constant $n/k = e^{2\psi_{n,k}}$ [D].
The encoding is a coordinate system on the curves the divisor
content is counted under [I].

## The binary of d(n) — the zero frequency

$d(n) \bmod 2$ is the square indicator: $d(n)$ is odd iff $n$ is a
perfect square (divisors pair $(x, n/x)$ except the self-paired
$x = \sqrt n$) [D, classical; verified to $n = 2000$]. The squares
are exactly the stations where the encoding goes rational (v14.366
§2, Euclid points). In Jeremy's phrase the binary of $d(n)$ encodes
the zero frequency: the self-paired divisor at the hyperbola's
vertex is the unpaired (DC) mode of the pairing, and $d(n) \bmod 2$
is its detector [I].

## The V4 overlay

The divisor content under the hyperbola is indexed by the four
units $U(12) = \{1, 5, 7, 11\}$ — the four hyperbola sections
$X = (r-1)/2 \in \{0, 2, 3, 5\}$ of the Totient note's apparatus —
and the Klein-four character group of $U(12)$ ($\chi_{12}$ and its
companions) is the Fourier overlay on that content, carrying the
proved complementarity $\phi_+(r) + \phi_-(r) = 1 \bmod 12$ and the
genus split $\{1, 11\}$ split / $\{5, 7\}$ inert in
$\mathbb{Q}(\sqrt3)$ (Totient note, Props. 4.2/4.3,
machine-verified). On the encoding's ruler this is the 12-division
case, level $n = 11$ [I].

Collision check: live HEAD v14.367 confirmed immediately before
this commit; v14.368 next free. Note updates and entry pushed with
fetch-back byte verification.
