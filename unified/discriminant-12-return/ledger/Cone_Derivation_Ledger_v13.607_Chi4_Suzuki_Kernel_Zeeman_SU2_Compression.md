# Cone Derivation Ledger v13.607 — chi_-4 Suzuki Screw Kernel on the Zeeman SU(2) Carrier

Date: 2026-09-21

Status: new construction / numerical prototype. The arithmetic kernel is explicit; the finite Suzuki characteristic and zero-convergence test are not yet built. No GRH claim.

## 0. Coordination

The live ledger was checked through v13.606 before this write. This entry opens the requested Dirichlet-L lane while preserving the v13.606 magnetic-driver guardrails.

Relevant prior facts:
- v13.285 freezes Suzuki v2 equation (1.3) for the zeta screw function.
- v13.282 freezes the Section-8 continuous-kernel formulation.
- v13.606 freezes the Zeeman carrier and its exact SU(2) weighted path.

## 1. Character and completion

Use the primitive real odd character modulo 4,

[
\chi_{-4}(n)=0\ (2\mid n),\qquad
\chi_{-4}(n)=+1\ (n\equiv1\pmod4),\qquad
\chi_{-4}(n)=-1\ (n\equiv3\pmod4).
]

Then (L(s,\chi_{-4})=\beta(s)).  The primitive completed factor has conductor (q=4) and odd parity, so the critical-line gamma argument is

[
a=\frac{1+1/2}{2}=\frac34.
]

Unlike zeta, this nonprincipal primitive L-function is entire, so there is no zeta (s(s-1)) pole-cancellation term.

## 2. chi_-4 screw kernel

The source-normalized primitive-character analogue of Suzuki v2 (1.3) is

[
\boxed{
\begin{aligned}
g_{-4}(t)
={}&
\sum_{n\le e^{|t|}}
\frac{\chi_{-4}(n)\Lambda(n)}{\sqrt n}
(|t|-\log n)\\
&-\frac{|t|}{2}
\left[
\psi(3/4)+\log(4/\pi)
\right]\\
&-\frac14\left[
\Phi(1,2,3/4)
-e^{-3|t|/2}\Phi(e^{-2|t|},2,3/4)
\right].
\end{aligned}}
]

The two changes relative to the zeta control are both load-bearing:

1. every prime-power ramp is twisted by (\chi_{-4}(n));
2. the archimedean/conductor term changes from (a=1/4,q=1) to (a=3/4,q=4).

There is no separate zeta pole term.

Immediate invariants are

[
g_{-4}(0)=0,\qquad g_{-4}(t)=g_{-4}(-t).
]

Prime-power breakpoints remain at (|t|=\log(p^r)), but their slope jumps carry the signs (\chi_{-4}(p)^r). In particular the prime 2 channel vanishes.

## 3. Exact Zeeman carrier

For spin (j), in the (J_z) basis,

[
J_z|j,m\rangle=m|j,m\rangle,
]

and

[
\boxed{
\langle j,m+1|J_x|j,m\rangle
=\frac12\sqrt{(j-m)(j+m+1)}.
}
]

Thus the arithmetic kernel is compressed onto the exact magnetic weighted path already frozen in v13.606; no independent-edge interpretation is introduced.

For a finite interval ([-A,A]), use the ordered Zeeman nodes

[
x_m=A\,m/j
]

and quadrature weights (w_m). The literal symmetric kernel compression is

[
\boxed{
(G^{(-4)}_j)_{mn}
=
\sqrt{w_mw_n}\,
g_{-4}(x_m-x_n).
}
]

This is a finite real symmetric matrix carried by the same ((2j+1))-dimensional Hilbert space as (J_z,J_x).

## 4. Implementation

Added

`research-notes/suzuki_chi4_zeeman_kernel_compression.py`.

The script implements:
- (\chi_{-4});
- all prime powers up to the finite kernel horizon;
- the signed von-Mangoldt ramps;
- the (a=3/4,q=4) Hurwitz-Lerch archimedean term;
- exact finite (J_z,J_x) matrices;
- a symmetric sampled/Galerkin compression (G^{(-4)}_j);
- checks of (g(0)), evenness, SU(2) Casimir closure, and matrix symmetry.

A local independent carrier check at (j=6) gave SU(2) Casimir infinity-norm residual about (7.1\times10^{-15}), consistent with binary64 roundoff.

## 5. Critical guardrail

The eigenvalues of (G^{(-4)}_j) are **not** the claimed beta-zero ordinates.

Suzuki's spectral zeros arise from the self-adjoint-extension characteristic built from the finite operator/deficiency problem. Therefore this checkpoint completes only

[
\boxed{
L(s,\chi_{-4})\text{ arithmetic}
\to
g_{-4}
\to
G^{(-4)}_j\text{ on the Zeeman SU(2) carrier}.
}
]

The next required chain is

[
G^{(-4)}_j
\to
\text{finite deficiency vectors}
\to
W^{(-4)}_j(\theta;z)
\to
\text{zeros of the finite characteristic}
\to
\gamma_n^{(-4)}\ ?.
]

Until that characteristic is constructed and a convergence experiment is run, no statement that a Zeeman-compressed eigenvalue equals or converges to an (L(s,\chi_{-4})) zero is promoted.

## 6. Next gate

Build the finite Suzuki deficiency/characteristic layer using this exact (g_{-4}) compression, preserving the Zeeman carrier. Then compare the first positive zeros of the finite characteristic, for increasing (j) and interval scale (A), against independently computed critical-line zeros of (L(s,\chi_{-4})).

That comparison is the first non-tautological spectral test.
