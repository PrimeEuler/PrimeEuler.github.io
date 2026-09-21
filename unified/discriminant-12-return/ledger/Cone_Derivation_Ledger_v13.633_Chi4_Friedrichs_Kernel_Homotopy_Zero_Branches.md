# Cone Derivation Ledger v13.633 — chi_-4 Friedrichs Kernel Homotopy Zero-Branch Continuation

Date: 2026-09-21

Status: direct homotopy continuation executed. The ordered shifts of v13.629 are genuine continuously tracked branch displacements for the first ten positive roots; no root exchanges occur in the tested homotopy.

## 0. Live collision/relevance check

The live ledger was checked before construction and again immediately before this write. It had advanced through v13.632 (External Audit Round 67), so v13.633 is free. Round 67 independently reproduces the free branch of v13.629 exactly and gives reduced-resolution convergence-consistent support for the full-kernel shifts. It introduces no contradiction relevant to this gate.

## 1. Homotopy

Use the same endpoint-adapted finite problem and finite lambda as v13.629, but scale only the arithmetic screw kernel:
[
k_	au(x,y)=	au g_{-4}(x-y)-lambda N_A(x,y),qquad 0le	aule1.
]

At N=16 and assembly q=160, solve at 21 equally spaced values tau=0,.05,...,1 for A=1.5,2,2.5. The first ten positive real zeros are matched between neighboring tau slices by minimum-distance assignment.

This removes the ordered-root-label ambiguity left open in v13.629.

## 2. Branch displacements

The tau=0 to tau=1 displacements reproduce the v13.629 ordered shifts exactly. Representative branches:

- A=1.5: delta r_1=+1.399516e-3, delta r_3=-1.963567e-1, delta r_9=-4.138039e-1.
- A=2.0: delta r_1=+8.10580e-4, delta r_6=+3.595515e-1, delta r_7=-4.143161e-1.
- A=2.5: delta r_1=+2.63534e-4, delta r_5=-2.174275e-1, delta r_10=+2.985716e-1.

The maximum single tau-step displacement over Delta tau=.05 remains small compared with the neighboring-root gap:
- A=1.5: largest branch step 7.3521e-2;
- A=2.0: 6.1715e-2;
- A=2.5: 4.9914e-2.

## 3. Crossing test

Across all 21 tau slices:
- no tracked-order exchange occurs for A=1.5,2.0,2.5;
- minimum adjacent positive-root gaps are respectively 1.79438, 0.801671, 0.994973.

Hence the continuation step is comfortably smaller than the nearest observed branch separation.

Therefore, for the first ten positive roots in this finite calculation,
[
oxed{delta r_k=r_k(1)-r_k(0)}
]
from v13.629 is not an artifact of root reordering: it is the actual continuously followed branch displacement under arithmetic-kernel turn-on.

## 4. Decision

The free endpoint modes persist continuously into the full chi_-4 characteristic. The arithmetic screw term deforms individual box branches, sometimes by O(0.1-0.4), but does not cause crossings or reorganize the first ten branches into a new A-independent ordering.

In particular the first branch remains almost entirely free:
[
delta r_1=(1.3995,0.8106,0.2635)	imes10^{-3}
]
for A=(1.5,2,2.5), while its base location is approximately pi/A.

Thus
[
oxed{	ext{the finite-A low zero branch is continuously connected to the endpoint box spectrum.}}
]

## 5. Guardrails

1. This is finite N=16, q=160 numerical continuation, not a proof for the continuous operator.
2. Only the first ten positive real zeros and tau in [0,1] were tested.
3. The chi_-4 screw-kernel normalization caveat remains active.
4. No beta-zero or GRH consequence is promoted.
5. The relevant remaining question is a renormalized/factored characteristic or A->infinity construction, not relabeling finite-A ordered roots.

## 6. Reproducer

research-notes/suzuki_chi4_friedrichs_kernel_homotopy.py
