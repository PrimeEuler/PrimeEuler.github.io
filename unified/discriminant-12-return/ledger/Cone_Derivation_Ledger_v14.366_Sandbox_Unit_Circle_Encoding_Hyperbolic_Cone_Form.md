# Cone Derivation Ledger v14.366 — Sandbox: unit-circle encoding and its hyperbolic cone form deposited (Jeremy-directed documentation; identities [D], seed significance [O])

Sandbox track (our Lane B). At Jeremy's direction (2026-10-13) the
note

    research-notes/Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md

is deposited in the repository. This entry announces the deposit and
records the dictionary compactly. It is a documentation deposit, not
a handoff response; no handoff is closed by it, and no seed, residual,
or capacity claim is made.

## The encoding [D]

Jeremy's station discretization (2026-10-11): on $n+1$ divisions of
the unit circle (diameter 2, division length $2/(n+1)$), station $n$
has radius $\sqrt n\,/\,\frac{n+1}{2} = 2\sqrt n/(n+1)$, the GM/AM
ratio for the pair $(n, 1)$. Assembled as a complex encoding
(2026-10-13, Jeremy's corrections fixing the real part):

$$z_n = \Bigl(1 - \frac{2}{n+1}\Bigr) + i\,\frac{\sqrt n}{(n+1)/2}
     = \frac{(n-1) + 2i\sqrt n}{n+1}, \qquad |z_n| = 1 \ \text{identically},$$

by $(n-1)^2 + (2\sqrt n)^2 = (n+1)^2$. Angle
$\varphi_n = 2\arctan(1/\sqrt n)$; stations: $n=1 \to (0,1)$;
$n=3 \to (1/2, \sqrt3/2)$ (the $60^\circ$ / 30-60-90 station);
$n = k^2$ gives Euclid points $((k^2-1) + 2ki)/(k^2+1)$.
Rim defect $1 - \mathrm{Re}\,z_n = 2/(n+1)$; chord
$|1 - z_n| = 2/\sqrt{n+1}$.

## The hyperbolic (cone) form [D]

With rapidity $\psi_n = \tfrac12 \ln n$ (so $e^{\psi_n} = \sqrt n$: a
cone boost of mode $n$ is multiplication by $\sqrt n$):

$$\cosh\psi_n = \frac{n+1}{2\sqrt n} = \frac{\mathrm{AM}}{\mathrm{GM}},
\qquad \sinh\psi_n = \frac{n-1}{2\sqrt n},$$

$$\tanh\psi_n = \frac{n-1}{n+1} = \cos\varphi_n,
\qquad \operatorname{sech}\psi_n = \frac{2\sqrt n}{n+1}
      = \sin\varphi_n = \frac{\mathrm{GM}}{\mathrm{AM}}.$$

One point read in the two signatures ($\sin \to \sinh$, Jeremy's
helix dictionary); AM–GM is $\cosh\psi_n \ge 1$.

## Contact with the seed [I]/[O]

The infinite seed is $y_m = \Phi(m)/\log(m/4)$ (v14.250), and
$\log(m/4) = 2(\psi_m - \ln 2)$ identically [D]: the seed's
denominator is twice the rapidity above $m = 4$ — the seed is $\Phi$
per unit rapidity [I]. Named candidate modifications [O]:
$y_m \cdot \operatorname{sech}\psi_m$ (sech-damped seed),
$y_m \cdot \tanh\psi_m$ (near-identity at seed modes), and the
rim-defect seed $y_m := 2/((m+1)\log(m/4))$. A finite probe
(production Regions 2–3 machinery, composed-residual metric against
the frozen v14.353 residual buffers, v14.354 compensator applied)
was commissioned by Jeremy and is running in the sandbox; its result
will be reported separately and decides whether the dictionary is
also machinery.

## Provenance / verification

Formulation is Jeremy's throughout (2026-10-11 stations; 2026-10-13
encoding and corrections). All identities verified symbolically
(sympy) on 2026-10-13. A repo-wide code search the same day found no
prior occurrence of this dictionary in the ledger or research-notes
(zero hits for sinh/cosh/tanh/sech/rapidity/"unit circle").

Collision check: live HEAD v14.365 confirmed immediately before this
commit; v14.366 next free. Note and entry pushed with fetch-back
byte verification.
