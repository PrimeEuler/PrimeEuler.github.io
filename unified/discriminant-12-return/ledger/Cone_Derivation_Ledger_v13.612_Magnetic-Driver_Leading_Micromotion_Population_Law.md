# Cone Derivation Ledger v13.612 — Magnetic-Driver Leading Micromotion Population Law

Date: 2026-09-21

Status: analytic continuation of v13.607, cross-checked against v13.609 external audit.

## 0. Collision and relevance check

Immediately before commit, the live ledger had advanced through v13.611 because the parallel chi_-4 lane occupied v13.608, v13.610, and v13.611, while v13.609 is External Audit Round 64. Thus v13.612 is the first free slot.

Relevant new material: v13.609 independently executed the v13.607 reproducer, confirmed the promoted j epsilon/4 and j epsilon^2/32 laws with the predicted correction scaling, and found that the unpromoted max-population statistic is sensitive to fast-time sampling. That observation is directly resolved below by taking the analytic fast-phase envelope.

## 1. First kick as a small transverse rotation

At bare resonance,
[
K^{(1)}(t)=rac{i g}{8omega}left(e^{2iomega t}J_+-e^{-2iomega t}J_-ight).
]
Relative to the stroboscopic slow motion, the rapidly varying kick changes the fundamental spin-1/2 transfer probability by
[
delta p(t)=rac{epsilon}{4}sqrt{p(1-p)},cosPhi(t)+O(epsilon^2),
qquad epsilon=|g|/omega,
]
where (p) is the instantaneous RWA transfer parameter and (Phi) is a fast phase. Because the fast phase winds O(1/epsilon) times during a pi pulse, its envelope is
[
|delta p|_{m env}=rac{epsilon}{4}sqrt{p(1-p)}+O(epsilon^2).
]

This explains why grid sampling of the literal maximum is slightly fragile: a finite time grid need not land on the fast-phase crest.

## 2. Lift to spin j by the exact SU(2) symmetric power

Write (n=2j). The RWA populations from the lowest-weight state are
[
P_r(p)=inom nr p^r(1-p)^{n-r}.
]
Therefore the leading micromotion perturbation is
[
delta P_r=P_r'(p),delta p+O(epsilon^2),
]
and its fast-phase envelope is
[
|delta P_r|_{m env}
=rac{epsilon}{4}sqrt{p(1-p)},|P_r'(p)|+O(epsilon^2).
]

Thus the entire higher-spin micromotion problem reduces to a one-variable binomial derivative. No independent edge-error model is involved.

## 3. Global maximum

For the endpoint population r=0,
[
P_0=(1-p)^n,
]
so
[
rac{|delta P_0|_{m env}}{epsilon}
=rac n4sqrt p,(1-p)^{n-1/2}.
]
The stationary point is
[
p_*=rac1{2n}=rac1{4j}.
]
Direct comparison with the interior-r extrema shows the global componentwise maximum is attained by an extremal population (r=0 or, by symmetry, r=n). Hence
[
oxed{
E_{m pop}^{max}
=C_j,epsilon+O(epsilon^2)
}
]
with
[
oxed{
C_j=
rac{sqrt{2j}}{4sqrt2}
left(1-rac1{4j}ight)^{2j-1/2}
=
rac{sqrt j}{4}
left(1-rac1{4j}ight)^{2j-1/2}.
}
]

For the spins used in v13.606/607:
[
C_{1/2}=rac18=0.125,
]
[
C_1=rac{3sqrt3}{32}=0.1623797632ldots,
]
[
C_{3/2}=0.1941031230ldots.
]

These are precisely the limiting slopes seen in the direct integration:
- j=1/2: E/epsilon -> 0.125;
- j=1: E/epsilon -> 0.16238;
- j=3/2: E/epsilon -> 0.19410.

The small finite-epsilon/grid discrepancy noted by v13.609 is therefore expected and is not a contradiction.

## 4. Large-j behavior

Using ((1-1/(4j))^{2j-1/2}	o e^{-1/2}),
[
oxed{
C_jsim rac{sqrt j}{4sqrt e}
}
qquad (j	oinfty).
]
So the maximum absolute population discrepancy grows only as (sqrt j,epsilon) at fixed small epsilon, not linearly with the number of ladder edges.

## 5. Reproducibility

Added:
`research-notes/magnetic_driver_micromotion_coefficient_v13_612.py`

which evaluates the closed coefficient and optimizing p for n=1,...,6. The existing v13.607 DOP853 script remains the direct time-domain cross-check.

## 6. Promotion and guardrail

Promoted for fixed j in the bare-resonance small-epsilon limit, with the maximum understood as the continuous-time/fast-phase envelope:
[
oxed{
E_{m pop}^{max}
=
rac{sqrt j}{4}
left(1-rac1{4j}ight)^{2j-1/2}epsilon
+O(epsilon^2).
}
]

Guardrail: a finite sampled time grid can undershoot this envelope by missing a micromotion crest. The formula is an asymptotic continuous-time maximum, not a promise that every finite numerical sampling reproduces the coefficient at finite epsilon.
