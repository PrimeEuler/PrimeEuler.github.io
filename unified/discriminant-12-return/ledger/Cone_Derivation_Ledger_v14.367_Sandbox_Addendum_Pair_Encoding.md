# Cone Derivation Ledger v14.367 — Sandbox addendum to v14.366: the pair encoding z_{n,k} (all pairs on the n+1 divisions) [D]

Sandbox track (our Lane B). Addendum to v14.366, at Jeremy's
direction (2026-10-13). The research note
`research-notes/Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md`
is extended with a §6 carrying this content (note update pushed and
byte-verified with this entry). Identities [D], verified
symbolically (sympy) 2026-10-13. No new claim about the seed or any
residual; the v14.366 probe remains the open item [O].

## The pair encoding

Jeremy's suggestion: encode all on the $n+1$ divisions, with
something like $(n+k)/(n-k)$ for $k \le n$. The v14.366 encoding is
the pair $(n, 1)$; the general pair $(n, k)$ gives [D]

$$z_{n,k} = \frac{(n-k) + 2i\sqrt{nk}}{n+k}, \qquad |z_{n,k}| = 1,$$

by $(n-k)^2 + (2\sqrt{nk})^2 = (n+k)^2$, at angle
$2\arctan\sqrt{k/n}$. At level $n$, $k = 0, \dots, n$ yields exactly
$n+1$ points sweeping the quarter circle from $(1,0)$ to $(0,1)$:
every pair of division indices is a point on the circle.

## Rapidity of a pair

With $\psi_{n,k} = \tfrac12 \ln(n/k)$ [D]:

$$\tanh\psi_{n,k} = \frac{n-k}{n+k}, \qquad
  \cosh\psi_{n,k} = \frac{n+k}{2\sqrt{nk}}
    = \frac{\mathrm{AM}}{\mathrm{GM}} \text{ of } (n,k), \qquad
  \operatorname{sech}\psi_{n,k} = \frac{\mathrm{GM}}{\mathrm{AM}},$$

and Jeremy's ratio is the boost between the two division scales,
$(n+k)/(n-k) = \coth\psi_{n,k}$. Rapidities add over chains,
$\psi_{n,k} + \psi_{k,j} = \psi_{n,j}$, while the coth factors
multiply — the division lattice is a group in rapidity.

## Seed contact (sharpened)

$\log(m/4) = 2\psi_{m,4}$ [D]: the v14.250 seed's denominator is the
pair rapidity of $(m, 4)$ — mode $m$ measured against the fixed
division 4 in the pair coordinate.

Collision check: live HEAD v14.366 confirmed immediately before
this commit; v14.367 next free. Note update and entry pushed with
fetch-back byte verification.
