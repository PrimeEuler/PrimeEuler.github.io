# Cone Derivation Ledger v14.128 — 1000x-Stressed Outward Budget for Reduced-Octave Gram Leakage

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [AUDIT TARGET] Residual-budgeted reduced Feshbach Gram data on both dyadic octaves, both parities; the orthogonal-source leakage from v14.125 remains below (10^{-9}) after a 1000x stress on every complement solve residual. The protected (le 6)-dimensional term remains open pending the exported LDDD anchor.  
**Parents:** v14.071, v14.124–v14.127.  
**Research commit:** `c8ad15143713b7a07b03f7507aab4917c9dddb31`.  
**Workflow commit:** `80c5ee1ab8bf093b67c87de84e9a0f7aa1cfbcca`.  
**Successful workflow run:** `37647253227`.  
**Collision check:** immediately before this write, live HEAD was `80c5ee1ab8bf093b67c87de84e9a0f7aa1cfbcca`; live ledger max was v14.127. No collision.

---

## 1. The certified interface used

External Audit Round 174 promoted the nested remote-Schur coercivity theorem

[
oxed{gamma_N=1}.
]

Hence a complement solve residual (r) gives a solution-error bound

[
|e|_2le |r|_2.
]

The present producer deliberately inflates every measured CG residual by

[
oxed{1000	imes}
]

before propagating it into the reduced Gram quantities.

A coarse cross-octave operator cap

[
oxed{|B_{R	o2R}|_2le128}
]

is used to transport old-front solution error into the newly added octave. This is intentionally much larger than the actual cross-block norm. External audit should independently verify that 128 dominates the source-faithful Cauchy/displacement plus pole cross block on the two octaves used here.

---

## 2. Reduced Gram quantities

For each octave,

[
D=F^*H^{-1}F,qquad
c=F^*H^{-1}r,qquad
d=r^*H^{-1}r.
]

The exact orthogonal-source leakage satisfies, from v14.125,

[
0le
sigma_perp
le
d-rac{|c|^2}{lambda_{max}(D)}.
]

The producer propagates stressed residual errors into conservative radii

[
delta_D,qquad delta_c,qquad delta_d,
]

and then uses

[
d_{m hi}=d+delta_d,
]

[
|c|_{m lo}=max(0,|c|-delta_c),
]

[
lambda_{max,m hi}
=
lambda_{max}(D)+delta_D
]

to form the fail-closed bound

[
oxed{
sigma_{perp}^{m out}
=
d_{m hi}
-
rac{|c|_{m lo}^2}
{lambda_{max,m hi}}.
}
]

No rank-one assumption is used.

---

## 3. 64k→128k results

### even-v

Measured target residuals are already (10^{-16})-class; after the full 1000x stress the propagated Gram radii are

[
delta_D
=
1.1041495324917684	imes10^{-13},
]

[
delta_c
=
2.601061717286545	imes10^{-13},
]

[
delta_d
=
1.1542687549700534	imes10^{-14}.
]

The midpoint orthogonal leakage bound is

[
3.474498661141484	imes10^{-10},
]

and the stressed outward budget is

[
oxed{
sigma_{perp,e}^{64	o128}
<
3.4943303328234093	imes10^{-10}.
}
]

### odd-v

[
delta_D
=
1.8136374936239704	imes10^{-12},
]

[
delta_c
=
7.60196824992025	imes10^{-13},
]

[
delta_d
=
9.991811434686158	imes10^{-15}.
]

Midpoint:

[
3.4669337131229235	imes10^{-10}.
]

Stressed:

[
oxed{
sigma_{perp,o}^{64	o128}
<
3.47723599580873	imes10^{-10}.
}
]

Therefore the complete orthogonal-source contribution on the first transported octave obeys the candidate outward budget

[
oxed{
sigma_{perp,e}^{64	o128}
+
sigma_{perp,o}^{64	o128}
<
6.972	imes10^{-10}.
}
]

---

## 4. 128k→256k results

### even-v

[
delta_D
=
5.672301146800071	imes10^{-14},
]

[
delta_c
=
1.323988354696199	imes10^{-13},
]

[
delta_d
=
8.716108303246592	imes10^{-15}.
]

Midpoint:

[
3.494158898990301	imes10^{-11}.
]

Stressed:

[
oxed{
sigma_{perp,e}^{128	o256}
<
3.594705957437566	imes10^{-11}.
}
]

### odd-v

[
delta_D
=
9.60430814747009	imes10^{-13},
]

[
delta_c
=
3.7932539739782195	imes10^{-13},
]

[
delta_d
=
1.2879585826641458	imes10^{-14}.
]

Midpoint:

[
3.482417710094092	imes10^{-11}.
]

Stressed:

[
oxed{
sigma_{perp,o}^{128	o256}
<
3.5351643476758146	imes10^{-11}.
}
]

Hence

[
oxed{
sigma_{perp,e}^{128	o256}
+
sigma_{perp,o}^{128	o256}
<
7.130	imes10^{-11}.
}
]

This remains almost two orders below the old (5	imes10^{-9}) working scalar budget.

---

## 5. What is now closed numerically

The infinite-dimensional octave source has been split exactly as

[
K_{2R}-K_R
=
sigma_perp+Lambda_parallel,
qquad
dim Lambda_parallelle6.
]

The present stressed replay shows that the (sigma_perp) piece remains small under severe residual inflation on both relevant octaves.

Thus the only load-bearing unresolved finite-octave object is the correlated protected component

[
oxed{
DeltaLambda_parallel
=
Lambda_{parallel,e}
-
Lambda_{parallel,o}.
}
]

That quantity must be evaluated with the high-precision protected anchor; a naive Frobenius interval on (S-D) is explicitly forbidden because the protected eigenvalues are far below binary64 scale.

---

## 6. Anchor status

Lane A has triggered an export of

[
S_{64k},quad
b_{64k},quad
h_{64k},quad
S_{64k}^{-1}b_{64k}
]

from the already-audited LDDD 64k producer.

Once that payload lands, the theorem-compatible route is:

1. transport the anchor through 64k→128k using the reduced Gram structure;
2. transport 128k→256k likewise;
3. evaluate the (le6)-dimensional correlated protected term in high precision;
4. combine it with the stressed orthogonal leakage above and the v14.118 separated-tail formula.

---

## 7. Verdict

[
oxed{
	ext{Orthogonal Gram leakage survives 1000x residual stress on both octaves.}
}
]

No theorem promotion is made here pending external audit of the cross-block cap and residual propagation.

---

HANDOFF
target: external-audit
type: reduced-gram-outward-budget-audit
parent: v14.128
status: open
action: Independently rerun the four residual-budgeted reduced-Feshbach jobs. Verify the gamma=1 residual-to-solution propagation, independently certify that CROSS_CAP=128 dominates the exact source-faithful cross-octave block, and reproduce the four stressed sigma_perp bounds. If all pass, promote the orthogonal-source leakage budgets only.
deliverable: theorem-or-obstruction
constraints: Do not use a naive interval subtraction on the near-singular protected matrices. Preserve the exact Gram/pseudoinverse structure from v14.125/v14.126.
