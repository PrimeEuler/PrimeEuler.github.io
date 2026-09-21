# Cone Derivation Ledger v13.621 — Friedrichs-Adapted Galerkin Carrier and Unitary SU(2) Transport

Date: 2026-09-21

Status: construction implemented and numerically tested. This repairs the specific bare-Jz-node defect isolated in v13.620, but is not yet an independent Galerkin solve of the Fredholm equation.

## 0. Collision/relevance check

The live ledger was re-fetched immediately before this write. v13.620 is still the current tip, so v13.621 is free. The directly relevant chain is v13.614–v13.616 and v13.620.

## 1. Domain-adapted finite spaces

On [0,A], define orthonormal bases

\[
e_n(x)=\sqrt{2/A}\cos((n+1/2)\pi x/A),\qquad n=0,\ldots,N-1,
\]

\[
o_n(x)=\sqrt{2/A}\sin((n+1)\pi x/A),\qquad n=0,\ldots,N-1.
\]

They satisfy identically

\[
e_n(A)=0,\qquad o_n(0)=o_n(A)=0.
\]

Hence every finite expansion satisfies the Section-8 parity endpoint conditions

\[
q_e(A)=0,\qquad q_o(0)=q_o(A)=0
\]

without sampled endpoint penalties.

## 2. First test: represent the stabilized breakpoint solution

The degree-14, q=12 breakpoint solution from the v13.620 family was projected in L2 onto the above basis. The projective characteristic was recomputed from the projected functions and compared with the original breakpoint characteristic at z=1,3,6,10, normalized at z*=0.5.

Finite lambdas inherited from the common j=10 finite pair:

- A=1.5: lambda=-0.9941426
- A=2.0: lambda=-0.9924506
- A=2.5: lambda=-0.9939186

Breakpoint diagnostics at degree 14/q12:

- A=1.5: cond(e,o)=(1.177376e4,3.127981e3), residuals=(5.35e-14,1.15e-14)
- A=2.0: cond(e,o)=(6.713486e3,2.053302e3), residuals=(2.02e-14,5.33e-15)
- A=2.5: cond(e,o)=(7.972665e3,2.918518e3), residuals=(7.73e-14,7.99e-15)

## 3. Convergence of the Friedrichs representation

Maximum projective characteristic difference over z=1,3,6,10:

| N | spin (2N-1)/2 | A=1.5 | A=2.0 | A=2.5 |
|---:|---:|---:|---:|---:|
| 2 | 1.5 | 5.8381e-2 | 1.6516e-1 | 1.8583e-1 |
| 4 | 3.5 | 5.2959e-2 | 9.5963e-2 | 5.1385e-2 |
| 6 | 5.5 | 3.1428e-2 | 2.3344e-2 | 4.1677e-2 |
| 8 | 7.5 | 1.7633e-2 | 1.3701e-2 | 6.0171e-2 |
| 10 | 9.5 | 1.0805e-2 | 8.6657e-3 | 1.7783e-2 |
| 12 | 11.5 | 7.4255e-3 | 7.1012e-3 | 1.0001e-2 |
| 16 | 15.5 | **3.8713e-3** | **4.6844e-3** | **4.4704e-3** |

The A=2.5 N=8 excursion is nonmonotone at z=10, but refinement through N=16 resolves it. Across all three A values the endpoint-adapted representation reaches sub-5e-3 maximum projective error by N=16.

At N=16 the componentwise differences are:

- A=1.5: (1.6686,0.3380,3.5403,3.8713)e-3
- A=2.0: (3.3447,4.6844,4.6091,0.0863)e-3
- A=2.5: (3.2858,0.3683,3.8398,4.4704)e-3

This is qualitatively different from the O(1)-O(10) discrepancy of the bare Jz-node carrier in v13.620.

## 4. Unitary SU(2) transport

The 2N coefficient space was mapped by an explicit unitary DFT matrix U into a standard spin

\[
j=(2N-1)/2
\]

carrier. Standard Jz and Jx were constructed there, and all characteristic rows/observables were transported covariantly.

The transported characteristic agrees with the coefficient-space characteristic to roughly 1e-12–1e-11 in the largest tests. The SU(2) Casimir residual is 0 to 2.84e-14 across the sweep.

Thus

\[
\boxed{\text{domain-faithful finite space}\xrightarrow{U}\text{spin-j SU(2) carrier}}
\]

is numerically lossless at roundoff scale.

This establishes an important structural point: v13.620 rejected bare Jz nodal sampling, not SU(2) as a finite carrier.

## 5. Numerical decision

The repaired lane passes its first representation/transport gate:

\[
\boxed{\text{Friedrichs-adapted parity basis reproduces the breakpoint characteristic under refinement.}}
\]

and

\[
\boxed{\text{unitary transport to a standard SU(2) spin carrier preserves it to roundoff.}}
\]

At N=16 the normalized characteristic error is <4.7e-3 for every tested A, versus O(1)-O(10) for the bare-node construction.

## 6. Scope guardrail / next gate

This experiment projects the already-computed breakpoint Fredholm deficiency solution into the adapted basis. It therefore establishes **representation adequacy and SU(2) transport invariance**, not yet an independent Galerkin solution of the integral equation.

The next nontrivial gate is to assemble the chi_-4 Fredholm operator and source terms directly in the e_n/o_n basis, solve for Galerkin coefficients without using the breakpoint solution as input, and compare that independently solved characteristic against the breakpoint control.

Only after that direct solve passes should zero-branch/A-robustness tests be resumed.
