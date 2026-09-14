# Cone Derivation Ledger v13.426 — Rational Prime Base-Angle Certificate

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** numerical evaluation of exact rational bounds; **[Audit]** guardrail.

## 0. Synchronization and role

The repository head was checked immediately before assignment.  The latest numbered ledger entry was v13.425, so v13.426 was free.

This checkpoint addresses the remaining nontrivial scalar source in the odd-sector finite-high proof: the prime phases for

\[
q\in\{2,3,4,5,7\},
\qquad
n=2r,\quad 11\le r\le2000.
\]

For even n,

\[
\sin\!\left(\frac{n\pi\log q}{2}\right)
=
\sin(r\pi\log q),
\]

and similarly for cosine.

The aim here is not yet to close the full matrix certificate, but to reduce all prime base constants to exact rational interval arithmetic.

## 1. Rational enclosure for pi [D]

Use Machin's identity

\[
\boxed{
\pi=16\arctan(1/5)-4\arctan(1/239).
}
\]

For \(0<x<1\),

\[
\arctan x
=
\sum_{k=0}^{K}(-1)^k\frac{x^{2k+1}}{2k+1}+R_K,
\]

with alternating remainder bounded by the first omitted term.

Using K=12 for x=1/5 and K=3 for x=1/239 gives an exact rational interval for pi whose width is

\[
\boxed{<8.0\times10^{-20}.}
\]

No floating transcendental constant is required to establish this enclosure.

## 2. Rational enclosure for log q [D]

For every q>1 set

\[
x_q=\frac{q-1}{q+1}.
\]

Then

\[
\log q
=2\operatorname{atanh}(x_q)
=2\sum_{k\ge0}\frac{x_q^{2k+1}}{2k+1}.
\]

All terms are positive.  After summing through k=K, the tail satisfies

\[
0<R_K
\le
\frac{2x_q^{2K+3}}{(2K+3)(1-x_q^2)}.
\]

The exact rational choices

\[
K_2=12,\quad K_3=19,\quad K_4=26,\quad K_5=32,\quad K_7=46
\]

give interval widths

\[
\begin{array}{c|c}
q & \text{width of log q interval}\\
\hline
2 & 1.10\times10^{-14}\\
3 & 2.96\times10^{-14}\\
4 & 3.58\times10^{-14}\\
5 & 8.56\times10^{-14}\\
7 & 6.51\times10^{-14}
\end{array}
\]

and in every case

\[
\boxed{\operatorname{width}(\log q)<10^{-13}.}
\]

## 3. Base-angle intervals [D/N]

Define

\[
\alpha_q=\pi\log q.
\]

Since all intervals are positive, interval multiplication is monotone.  Combining the rational pi and log q enclosures yields

\[
\boxed{
\operatorname{width}(\alpha_q)<4\times10^{-13}
\quad\text{for all }q\in\{2,3,4,5,7\}.
}
\]

The exact widths are produced by

`research-notes/suzuki_prime_base_rational_certificate.py`.

## 4. Propagation to all r<=2000 [D]

Let

\[
R(\alpha)=
\begin{pmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{pmatrix}.
\]

The exact r-th prime phase is carried by \(R(\alpha_q)^r\).

For any approximate base rotation \(\widetilde R\), the telescoping identity gives

\[
\widetilde R^r-R^r
=
\sum_{j=0}^{r-1}
\widetilde R^j(\widetilde R-R)R^{r-1-j}.
\]

Hence, if

\[
\|\widetilde R-R\|_2\le\eta,
\]

then

\[
\boxed{
\|\widetilde R^r-R^r\|_2
\le
r\eta(1+\eta)^{r-1}.
}
\]

The rotation map is 1-Lipschitz in angle in operator norm, so the alpha interval radius bounds the pure base-angle contribution to eta.  With alpha width <4e-13 and r<=2000, the propagated base-interval scale is below

\[
\boxed{4\times10^{-10}.}
\]

This is over three orders of magnitude tighter than the deliberately loose micro-scale prime-sequence budget from v13.425.

## 5. Remaining finite trig step [Audit]

To turn this into a complete prime-channel enclosure, one still needs a proof-grade enclosure of

\[
\sin\alpha_q,
\qquad
\cos\alpha_q
\]

from the rational alpha intervals.  This is elementary: evaluate a finite Maclaurin polynomial at the rational midpoint and add

1. the Taylor remainder;
2. the alpha-interval radius by the 1-Lipschitz bound.

Because \(\alpha_q<\pi\log7<6.2\), degree about 35 already places the raw Taylor remainder below 10^-13.  Thus no argument reduction or external transcendental routine is necessary.

After that, finite recurrence arithmetic can be either exact/high-precision or separately outward-budgeted.  The allowed final prime errors remain at the low-micro scale, so substantial slack remains.

## 6. Proof-state consequence [Audit]

The finite-high certificate is now reduced to elementary pieces:

- archimedean analytic truncation: already dimension-free at 1.22e-13;
- even-mode arch polynomial recurrence: available from v13.423;
- cusp: reduced in v13.425 to short inverse-power series;
- pi/log q: exact rational intervals in this checkpoint;
- prime trig: finite rational Taylor enclosure plus recurrence arithmetic;
- factor arithmetic: v13.424, with floor >0.0012755.

No theorem is promoted yet.  The next useful checkpoint is the combined outward nominal generator and final operator budget.

---

**Checkpoint conclusion.** The five Suzuki prime base angles can be certified from exact rational arithmetic alone, with alpha widths below 4e-13.  Propagation through all r<=2000 contributes below 4e-10 before recurrence-rounding accounting, far beneath the source budget needed for finite-high positivity.
