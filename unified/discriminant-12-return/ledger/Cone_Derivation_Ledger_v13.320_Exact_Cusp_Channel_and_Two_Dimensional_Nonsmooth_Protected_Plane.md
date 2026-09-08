# Cone Derivation Ledger v13.320
## Exact cusp channel and two-dimensional nonsmooth protected plane

### Scope
This checkpoint continues v13.319 in the Suzuki / Weil quadratic-form thread at a=1, even-v sector.  It corrects one asymptotic simplification in v13.319 and sharpens the active-tail reduction.

No RH/GRH, exact-kernel, lambda_1=0, or positivity conclusion is claimed.

---

## 1. Exact fixed-core cusp asymptotic
For odd modes m,n, m != n, v13.301 gives the exact cusp matrix entry

\[
C^{\rm cusp}_{mn}
=\frac{2}{\pi}\frac{n\,\operatorname{Si}(m\pi)-m\,\operatorname{Si}(n\pi)}{m^2-n^2}.
\]

For fixed low m and n -> infinity,

\[
C^{\rm cusp}_{mn}
=-\frac{2}{\pi}\frac{\operatorname{Si}(m\pi)}{n}+O_m(n^{-2}).
\]

This is the exact fixed-core leading coefficient.

### Correction to v13.319
v13.319 introduced the decomposition-level coefficient

\[
-\left(1+\frac{2}{\pi^2m}\right)\frac1n
\]

from

\[
C_{\rm cusp}=D_{\log}-H_{\rm odd}+K_{\rm cusp},
\qquad
(H_{\rm odd})_{mn}=\frac1{m+n},
\qquad
(K_{\rm cusp})_{mn}\sim-\frac{2}{\pi^2mn}.
\]

That coefficient is useful as a structural decomposition term but is not the exact fixed-m asymptotic coefficient: the compact correction still contains a residual O(1/n) contribution for fixed low m.  The correct asymptotic channel is the Si coefficient above.

---

## 2. Exact cusp remainder after channel subtraction
Subtract

\[
-\frac{2}{\pi}\frac{\operatorname{Si}(m\pi)}n.
\]

Then algebra gives

\[
\boxed{
R^{(c)}_{mn}
=-\frac{2}{\pi}\frac{1}{1-m^2/n^2}
\left(
\frac{m^2\operatorname{Si}(m\pi)}{n^3}
-\frac{m\operatorname{Si}(n\pi)}{n^2}
\right).
}
\]

Hence, for every fixed core mode m<=19,

\[
R^{(c)}_{mn}=O_m(n^{-2}).
\]

Therefore the projected remote-tail Hilbert-Schmidt norm is O(N^{-3/2}).

Using |Si(n pi)|<2 and N>19 gives the conservative coordinate bound

\[
|R^{(c)}_{mn}|
\le
\frac{2/\pi}{1-(19/N)^2}
\left(
\frac{m^2|\operatorname{Si}(m\pi)|}{n^3}
+\frac{2m}{n^2}
\right).
\]

Projected onto the first four high-precision core eigenvectors and combined in Hilbert-Schmidt norm, this yields approximately

| N | active cusp remainder HS bound |
|---:|---:|
| 237 | 0.0032082161 |
| 301 | 0.0022197225 |
| 401 | 0.0014313240 |
| 501 | 0.0010199514 |
| 701 | 0.0006129541 |
| 1001 | 0.0003578233 |

These displayed decimals are ordinary high-precision / floating evaluations of analytic inequalities, not interval-certified enclosures.

---

## 3. Exact active cusp channel
Let q^(j), j=1,...,4, denote the first four 60-digit eigenvectors of the low core n=1,3,...,19.  Define

\[
S_j
=-\frac{2}{\pi}
\sum_{m\le19,\ m\ \mathrm{odd}}
q_m^{(j)}\operatorname{Si}(m\pi).
\]

Numerically,

\[
\boxed{
S\approx
(-0.5852224134,
\ 0.5265860837,
\ 0.6307779422,
\ 0.7374339543).
}
\]

For comparison, the exact active prime channel from v13.318-v13.319 is

\[
L\approx
(1.3465633763,
-0.9226606081,
-0.7161152964,
-0.3705007563).
\]

Their normalized inner product is

\[
\boxed{\cos\angle(L,S)\approx-0.8786010811.}
\]

The singular values of the 4x2 channel matrix [L S] are approximately

\[
\boxed{2.14956738,\qquad0.50542592.}
\]

Thus the two channels are strongly aligned but genuinely independent.

---

## 4. Two-dimensional protected active plane
Because span{L,S} has dimension two inside the four-dimensional active space, its orthogonal complement has dimension two:

\[
\boxed{
\mathcal P_2
=\{x\in\mathcal A_4:\langle x,L\rangle=\langle x,S\rangle=0\}.
}
\]

On this plane, the leading 1/n terms of both nonsmooth remote couplings vanish exactly.  Therefore

\[
\boxed{
\|P_{\ge N}B_{\rm prime}P_{\mathcal P_2}\|_{HS}=O(N^{-3/2}),
\qquad
\|P_{\ge N}C_{\rm cusp}P_{\mathcal P_2}\|_{HS}=O(N^{-3/2}).
}
\]

A numerical orthonormal basis for this protected plane in the four active coordinates is

\[
p_1\approx(0.04278442,-0.43176555,0.82458405,-0.36305530),
\]

\[
p_2\approx(-0.55379161,-0.74448056,-0.23283506,0.29129261).
\]

This basis is descriptive; the invariant content is the orthogonal complement of span{L,S}.

---

## 5. Interpretation
The active remote nonsmooth tail is now structurally reduced to

\[
\boxed{
\text{prime rank-one channel}
\oplus
\text{cusp rank-one channel}
\oplus
O(N^{-3/2})\text{ remainders}.
}
\]

Equivalently, two of the four active combinations are asymptotically protected from both leading nonsmooth channels.

This is stronger than the v13.319 two-channel heuristic because the cusp channel has now been identified from the exact Si formula and the remainder has an explicit O(n^-2) identity.

The next target is the smooth archimedean remainder in the same active basis.  v13.312 gives the coordinate bound |R_mn| <= C_r/(k_m k_n), but the active projection may again reveal one low-rank leading channel plus a faster remainder.  Determining that will show whether the two-dimensional nonsmooth protected plane survives, shrinks to one dimension, or remains effectively protected after the smooth tail is included.

---

## Proof-status guardrails
- Exact cusp matrix formula: source-derived / previously established.
- Exact fixed-core Si asymptotic channel and algebraic remainder identity: analytic.
- O(N^-3/2) projected cusp remainder: analytic from the displayed bound.
- Numerical channel vectors / singular values / protected basis: high-precision numerical evaluations, not interval-certified.
- No exact zero mode, kernel dimension, lambda_1=0, RH, or GRH conclusion.
