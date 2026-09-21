# Cone Derivation Ledger v13.629 — chi_-4 Friedrichs Free/Endpoint versus Kernel Zero Shifts

Date: 2026-09-21

Status: operational finite-A decomposition executed. The dominant ordered zero branch is identified as an endpoint/free box branch; the chi_-4 screw kernel produces finite, mode-dependent perturbations but does not remove the box scaling.

## 0. Live collision/relevance check

The live ledger was checked before construction and again immediately before this write. It had advanced through v13.628 (External Audit Round 66), so v13.629 is free. Round 66 does not overturn v13.627; its attempted independent zero-branch rerun timed out and was explicitly inconclusive. It does flag an unrelated M16001 script bug, which does not enter this chi_-4 calculation.

## 1. Operational decomposition

The full finite kernel is
[
k_{full}(x,y)=g_{-4}(x-y)-\lambda N_A(x,y).
]

Define the free/endpoint control by deleting only the arithmetic screw term while retaining the same interval, endpoint-adapted Friedrichs bases, nuisance equations, finite lambda, Neumann inverse term, and characteristic:
[
k_0(x,y)=-\lambda N_A(x,y).
]

This is an operational decomposition of the finite problem. Because inversion is nonlinear, it is NOT a claim that the full characteristic or its zeros decompose additively.

At N=16, assembly q=160, define ordered shifts
[
\delta r_k(A)=r_k^{full}(A)-r_k^{0}(A).
]

## 2. Free branch

The free roots are extremely close to n pi/A. For the first root,
[
A r_1^0/\pi=(1.00002232, 1.00002241, 1.00002252)
]
for A=(1.5,2,2.5).

Thus the box law isolated in v13.627 is already present before g_-4 is turned on:
[
oxed{r_n^0(A)\approx n\pi/A.}
]

## 3. Kernel-induced ordered zero shifts

### A=1.5

| k | free | full | shift |
|---:|---:|---:|---:|
|1|2.094442|2.095841|+0.001400|
|2|4.188890|4.204076|+0.015186|
|3|6.284395|6.088038|-0.196357|
|4|8.379912|8.380863|+0.000951|
|5|10.477508|10.310665|-0.166843|
|6|12.575131|12.869070|+0.293939|
|7|14.675812|14.716063|+0.040251|
|8|16.776597|16.510443|-0.266154|
|9|18.881439|18.467635|-0.413804|
|10|20.986688|21.286283|+0.299595|

### A=2.0

| k | free | full | shift |
|---:|---:|---:|---:|
|1|1.570832|1.571642|+0.000811|
|2|3.141669|3.147949|+0.006279|
|3|4.713304|4.754602|+0.041298|
|4|6.284949|6.080065|-0.204885|
|5|7.858161|7.883314|+0.025153|
|6|9.431397|9.790948|+0.359552|
|7|11.006935|10.592619|-0.414316|
|8|12.582556|12.839393|+0.256837|
|9|14.161231|13.942563|-0.218668|
|10|15.740218|16.058575|+0.318356|

### A=2.5

| k | free | full | shift |
|---:|---:|---:|---:|
|1|1.256665|1.256929|+0.000264|
|2|2.513337|2.514819|+0.001482|
|3|3.770649|3.780789|+0.010140|
|4|5.027973|5.074155|+0.046182|
|5|6.286555|6.069127|-0.217427|
|6|7.545160|7.509693|-0.035467|
|7|8.805615|8.802174|-0.003441|
|8|10.066141|10.210674|+0.144532|
|9|11.329120|11.334194|+0.005074|
|10|12.592354|12.890925|+0.298572|

Mean absolute ordered shift over the first ten roots:
- A=1.5: 0.16945
- A=2.0: 0.18462
- A=2.5: 0.07626

The largest absolute shifts are 0.41380, 0.41432, and 0.29857 respectively.

## 4. Decision

The low ordered branch is overwhelmingly endpoint/free in origin. In particular the first root shift is only
[
(1.40\times10^{-3}, 8.11\times10^{-4}, 2.64\times10^{-4})
]
while its location follows pi/A.

The arithmetic kernel becomes a non-negligible mode-dependent perturbation higher in the list, with both signs and occasional O(0.1-0.4) shifts, but it does not convert the ordered finite-A spectrum into an A-invariant arithmetic zero list.

Therefore:
[
oxed{\text{the catastrophic }1/A\text{ drift is a free/endpoint box branch, not a discretization artifact and not created by }g_{-4}.}
]

The meaningful next question is not whether the first ordered finite-A zero equals a beta zero. It is whether an arithmetic object can be isolated after factoring/subtracting the free endpoint characteristic or by following a renormalized branch in the A->infinity limit.

## 5. Guardrails

1. Zero shifts are ordered-root differences, not perturbation-theory labels through possible avoided crossings.
2. The decomposition is operational: delete g_-4 while retaining -lambda N_A and all endpoint/nuisance structure. Inverse operators and zeros do not add linearly.
3. The chi_-4 screw-kernel normalization caveat remains active.
4. No beta-zero or GRH consequence is promoted.

## 6. Reproducer

research-notes/suzuki_chi4_friedrichs_free_kernel_zero_shifts.py
