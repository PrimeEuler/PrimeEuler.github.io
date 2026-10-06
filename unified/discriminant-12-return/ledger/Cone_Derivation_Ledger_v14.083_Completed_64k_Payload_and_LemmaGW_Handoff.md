# Cone Derivation Ledger v14.083 — Completed 64k Fixed-FFT Payload and Lemma G/W Sandbox Handoff

**Date:** 2026-10-06  
**Track:** Lane A / sandbox coordination  
**Status:** [N] all 32k/64k capacity-only and full finite-data jobs completed successfully; [N] 64k fixed-FFT payload extracted; [D] symmetric 64k absolute budget fails on the actual finite data; [I] favorable one-sided sign pattern persists; [O] Lane A finite-section floor `mu_32k`; [O] Sandbox Lemma G/W oscillatory quadratic-form bound.  
**Parents:** v14.075–v14.082.  
**Collision check:** immediately before this write, live HEAD was `c2918bc2cff8752fa4abd6caea99044e059d308c`; live ledger max was v14.082. No collision.

---

## 1. All fixed-FFT 32k/64k jobs are complete

Both workflows are now fully green:

- capacity-only fixed full-lattice FFT replay at 32k/64k in both parities;
- full fixed-FFT finite-data producer at 32k/64k in both parities.

The 64k full jobs retain the same calibrated operator/refinement path used at 8k/16k and 32k.

---

## 2. 64k finite-data payload

### even-v

[
C_{e,64k}
=
7.47828676618939746873374322589197699866148632817897333194794
	imes10^{-30},
]

[
L_{e,64k}
=
1.32325993947717481570891015808665884764162594642100950556344
	imes10^{16},
]

[
A_{e,64k}=C_{e,64k}L_{e,64k}^2
=
1309.46062670398118713318930325557312972139479460502590241241,
]

[
M_{e,11}
=
18058.4692056993990241055456500674050048966255216563848514547.
]

Post-refinement source residual:
[
1.62043	imes10^{-25}.
]

Post-refinement (M_{11}) residual:
[
6.37200	imes10^{-22}.
]

### odd-v

[
C_{o,64k}
=
2.15605528873542574860579130421946635327920614796315433714297
	imes10^{-25},
]

[
L_{o,64k}
=
-7.73882606587562694258131265556797173246388563129520277874925
	imes10^{13},
]

[
A_{o,64k}
=
1291.24919871488756170050103705679275590081298413992253755461,
]

[
M_{o,11}
=
17354.7126388213777354186766319899356642245686307440084497067.
]

Post-refinement source residual:
[
3.76175	imes10^{-26}.
]

Post-refinement (M_{11}) residual:
[
6.21955	imes10^{-22}.
]

The inherited theorem input remains

[
gamma_{64k}=1.
]

---

## 3. Derived 64k paired quantities

The amplitude difference is

[
oxed{
Delta A_{64k}
=
A_{o,64k}-A_{e,64k}
approx
-18.2114279890936254.
}
]

The direct (M_{11}) difference is

[
M_{o,11}-M_{e,11}
approx
-703.756566878021289.
]

Using the reconciled constant

[
C_D=-4.395585571978897
]

gives

[
oxed{
C_S(64k)
=
C_D-(M_o-M_e)
approx
+699.3609813060424.
}
]

These are midpoint finite-data values. Their signs are extremely far from zero; theorem use still requires the same outward finite-data discipline as v14.081.

---

## 4. Consequence for the symmetric 64k budget

Sandbox v14.073's illustrative symmetric 64k admissible budgets were approximately

[
|Delta A|<0.11,
qquad
|C_S|<262.
]

The actual 64k midpoint values are

[
|Delta A_{64k}|approx18.21,
qquad
|C_S(64k)|approx699.36.
]

Therefore the symmetric absolute-value 64k route does **not** close on actual finite data.

This is not a new obstruction to the one-sided route, because the signs are favorable:

[
Delta A_{64k}<0,
qquad
C_S(64k)>0,
]

so, with (K_{p,64k}>0),

[
T^{(1)}_{64k}<0,
qquad
T^{(2)}_{64k}<0.
]

The same favorable sign structure seen at 32k persists at 64k.

---

## 5. 32k to 64k finite-shell midpoint

From the completed capacity-only replays,

[
eta_{e,32k	o64k}
=
rac{C_{e,32k}}{C_{e,64k}}-1
approx
9.79218108783	imes10^{-4},
]

[
eta_{o,32k	o64k}
=
rac{C_{o,32k}}{C_{o,64k}}-1
approx
9.66373334348	imes10^{-4},
]

hence

[
oxed{
E^{mid}_{32k	o64k}
approx
-1.28447744352	imes10^{-5}.
}
]

Guardrail: midpoint diagnostic only. No outward shell interval or infinite-tail inference is promoted here.

---

## 6. Active blockers after v14.082

External Audit Round 176 identifies the same two primitives for both the symmetric and one-sided formulations:

1. **Lane A:** finite-section Euclidean floor (mu_{32k}), sufficient to obtain a valid 32k operator radius. v14.080 gives the target
   [
   	heta_{e,32k}^{max}=1.174454	imes10^{-5},
   ]
   corresponding roughly to
   [
   mu_{32k}gtrsim1.2	imes10^{-31}.
   ]

2. **Analytic:** Lemma G or Lemma W for the oscillatory (R_{osc}) quadratic form, especially the slow q=7 off-diagonal channel.

All other pieces of the one-sided 32k framework already fit numerically with large headroom per v14.081.

---

## 7. Ownership split

Lane A now owns:

[
oxed{mu_{32k}}
]

via the finite-section graph-Schur/protected-subspace machinery analogous to v14.034.

Sandbox should work independently on the analytic oscillatory primitive.

---

HANDOFF  
target: sandbox  
type: analytic-lemma  
parent: v14.083  
status: open  
action: Attack the v14.079/v14.081 missing Lemma G or Lemma W for the q=7-dominated oscillatory quadratic form. The target is now the one-sided 32k framework, where the rigorous remainder only needs to fit the approximately (1.37	imes10^{-5}) margin once Lane A supplies (mu_{32k}). Exploit the exact q=7 sum-of-products / Toeplitz-Hankel structure and the self-consistent equation (S_pw_p=u_p); seek a bound directly on (|langle w_o,R_{osc}w_eangle|) rather than a global operator norm or first-variation SBP estimate.  
deliverable: theorem bound or sharpened quantified obstruction, with a deterministic producer/reproducer for every numerical phase constant  
constraints: preserve q-channel cancellation; no raw (|R_{osc}|_2|w_o||w_e|) fallback as final result; no inference from the observed numerical 0.6% margin consumption alone; do not modify Lane A's (mu_{32k}) computation; independent audit required before promotion.

---

## 8. Result

[
oxed{
egin{aligned}
&	ext{All fixed-FFT 32k/64k jobs complete successfully.}\
&Delta A_{64k}approx-18.21143,qquad
C_S(64k)approx+699.361.\
&	ext{Thus the symmetric absolute 64k budget fails, but the favorable one-sided signs persist.}\
&E^{mid}_{32k	o64k}approx-1.28448	imes10^{-5} 	ext{(diagnostic only).}\
&	ext{The project is now concentrated on exactly two primitives: Lane A }mu_{32k}
	ext{ and Sandbox Lemma G/W.}
end{aligned}
}
]
