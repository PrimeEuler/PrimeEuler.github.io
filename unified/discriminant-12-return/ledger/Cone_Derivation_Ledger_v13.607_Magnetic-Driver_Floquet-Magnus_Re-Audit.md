# Cone Derivation Ledger v13.607 — Magnetic-Driver Floquet/Magnus Re-Audit

Date: 2026-09-21

Status: independent re-audit of v13.606 checkpoint; numerical scan reproduced and Floquet-gauge sign issue resolved.

## 0. Collision check

Immediately before this entry, v13.606 was the latest numbered ledger entry found. v13.607 was free.

## 1. Exact rotating-frame problem

At bare resonance,
[
H(t)=H_0+V(t),qquad H_0=-rac g2J_x,
]
[
V(t)=-rac g4left(e^{i
u t}J_+ + e^{-i
u t}J_-ight),qquad 
u=2omega.
]
Thus
[
H_{+1}=-rac g4J_+,qquad H_{-1}=-rac g4J_-.
]

The exact dynamics remains a single SU(2) propagator in every spin-j representation.

## 2. Floquet convention and the apparent sign ambiguity

With the van-Vleck convention
[
U(t)=e^{-iK(t)}e^{-iH_{m vV}t}e^{iK(0)},
]
the first kick is
[
K^{(1)}(t)=sum_{m
e0}rac{H_m e^{im
u t}}{im
u}
=rac{i g}{8omega}left(e^{2iomega t}J_+-e^{-2iomega t}J_-ight).
]
In particular
[
K^{(1)}(0)=-rac{g}{4omega}J_y.
]

Using the Fourier ordering ([H_{+1},H_{-1}]/
u),
[
H_{m vV}
=-rac g2J_x+rac{g^2}{16omega}J_z
+O(g^3/omega^2).
]

This is the +J_z sign recorded in v13.606. It is not by itself the stroboscopic Floquet Hamiltonian at phase t=0, because (K(0)
e0).

Conjugating into the t=0 stroboscopic gauge,
[
H_{m strob}=e^{-iK(0)}H_{m vV}e^{iK(0)}
=-rac g2J_x-rac{g^2}{16omega}J_z
+O(g^3/omega^2).
]

Therefore the sign flips between these two legitimate Floquet gauges. The physical tilt magnitude is gauge-consistent:
[
|eta|=rac{|g|}{8omega}+O((g/omega)^3).
]

A direct one-fast-period numerical logarithm independently returned the negative stroboscopic coefficient (-g^2/(16omega)), confirming the convention accounting.

## 3. Why the checkpoint sample times are especially clean

For
[
T_pi=rac{2pi}{|g|},
]
the fast phase is
[

u T_pi=rac{4pi}{epsilon},qquad epsilon=|g|/omega.
]
For the sampled values (epsilon=0.02,0.05,0.1,0.2), both (T_pi/2) and (T_pi) are integer multiples of the fast period (pi/omega). Hence
[
K(T_pi/2)=K(0),qquad K(T_pi)=K(0)
]
for the periodic kick. These are stroboscopic observation times, so endpoint micromotion does not contaminate the quoted phase-spread and inversion coefficients.

This qualification is essential: for generic (epsilon), evaluating exactly at the nominal RWA (T_pi) need not be stroboscopic, and endpoint micromotion can alter finite-(epsilon) coefficients.

## 4. Phase-spread coefficient

At the half-pulse stroboscopic time the slow axis has tilt (|eta|). For the spin-j symmetric-power representation, the gauge-fixed phase range across the multiplet is
[
Deltaphi_j(T_pi/2)=2j|eta|+O(epsilon^3)
=oxed{rac j4epsilon+O(epsilon^3)}.
]

Thus the checkpoint coefficient j/4 survives the independent audit for the stated stroboscopic sequence.

## 5. Inversion-infidelity coefficient and remainder parity

For spin 1/2 under the stroboscopic effective axis,
[
P_{1/2}^{m inv}
=rac{1}{1+eta^2}
sin^2left[racpi2sqrt{1+eta^2}ight]
=1-eta^2+left(1-rac{pi^2}{16}ight)eta^4+O(eta^6).
]
The exact SU(2) symmetric-power identity gives
[
P_j^{m inv}=(P_{1/2}^{m inv})^{2j}.
]
Therefore
[
1-P_j^{m inv}
=2jeta^2+O(eta^4)
=oxed{rac{j}{32}epsilon^2+O(epsilon^4)}.
]

For this stroboscopic bare-resonance protocol, the cubic term is absent. This is also consistent with the exact invariance of transition probabilities under (gmapsto-g), implemented by a (pi) rotation about z.

## 6. Fresh numerical reproduction

A repository-side script was added:
`research-notes/magnetic_driver_floquet_reaudit_v13_607.py`.

It directly integrates the exact time-dependent rotating-frame Schrödinger equation with DOP853 and compares against the RWA for j=1/2,1,3/2 and epsilon=0.02,0.05,0.1,0.2.

The fresh run reproduces the v13.606 table (rounding at the shown digits), including:
- max population discrepancy O(epsilon);
- phase spread at T_pi/2 matching j epsilon/4;
- inversion infidelity matching j epsilon^2/32.

Representative exact rerun values:
- epsilon=.02, j=.5: maxpop 0.00249591256, phase 0.00250005284, infidelity 6.25038504e-6.
- epsilon=.10, j=1: maxpop 0.0163273543, phase 0.0250132110, infidelity 3.12945492e-4.
- epsilon=.20, j=1.5: maxpop 0.0392365510, phase 0.0751586357, infidelity 1.88512192e-3.

## 7. Promotion status

Promoted for the explicitly stated bare-resonance, stroboscopic protocol:
[
oxed{Deltaphi_j(T_pi/2)=rac j4epsilon+O(epsilon^3)}
]
and
[
oxed{1-P_{-j	o+j}(T_pi)=rac j{32}epsilon^2+O(epsilon^4)}.
]

The O(epsilon) maximum population discrepancy remains a micromotion statement; its detailed leading coefficient depends on which population component and time within the pulse realizes the maximum and is not promoted here as a universal closed-form coefficient.

Guardrail: do not silently extend the j/4 or j/32 finite-time formulas to generic nonstroboscopic epsilon values without retaining the kick operators at the endpoints.
