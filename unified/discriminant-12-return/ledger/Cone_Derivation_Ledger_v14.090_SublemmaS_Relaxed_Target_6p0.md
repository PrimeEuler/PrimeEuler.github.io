# Cone Derivation Ledger v14.090 — Conditional Relaxation of Sandbox Sub-lemma S Target to Joint Constant 6.0

**Date:** 2026-10-06  
**Track:** Lane A / one-sided 32k closure coordination  
**Status:** [D/I] conditional budget consequence of v14.088–v14.089; Sandbox's sufficient oscillatory joint-constant target relaxes from 4.1 to 6.0 if the primary M32000 floor is independently promoted. **Informational/conditional only; no theorem promotion.**  
**Parents:** v14.081, v14.086, v14.088, v14.089.  
**Collision check:** immediately before this write, live HEAD was `703dcf4b7bf9fcf875dc8db21b356f3078c5985c`; live ledger max was v14.089. No collision.

---

## 1. Primary finite margin

Conditional on the v14.088 cap-closure audit, v14.089 restores the primary finite cumulative upper endpoint

[
sup E_{4k	o32k}
=
-1.8869797018800170	imes10^{-5}.
]

Thus use

[
oxed{
M_{m primary}
=
1.8869797018800170	imes10^{-5}.
}
]

This is the relevant one-sided margin for the final tail budget; the smaller v14.088 doubled-residual margin is only an adversarial stress test.

---

## 2. Fixed non-oscillatory charges

From v14.081/v14.086:

[
delta u
le
4.533	imes10^{-7},
]

[
Q_{m sep}^{K=10}
le
1.3	imes10^{-11},
]

and the smooth remainder is below the (0.1%) scale. Use the deliberately rounded public reserve

[
oxed{
R_{m smooth}le2	imes10^{-8},
}
]

which exceeds (0.1%) of the primary margin.

Sandbox v14.086 also freezes

[
A_{max}=804,
qquad
|w_o|,|w_e|
=
3.7281	imes10^{-9}.
]

Hence one unit of joint oscillatory constant costs

[
804cdot3.7281	imes10^{-9}
=
2.9973924	imes10^{-6}.
]

---

## 3. Joint constant 6.0 is sufficient [I]

Assume the relaxed Sub-lemma

[
oxed{
|langle w_o,R_{m osc}^b w_eangle|
le
6.0,|w_o|,|w_e|.
}
]

Its scaled cost is

[
6.0cdot804cdot3.7281	imes10^{-9}
=
1.79843544	imes10^{-5}.
]

Adding the fixed charges,

[
1.79843544	imes10^{-5}
+
4.533	imes10^{-7}
+
2	imes10^{-8}
+
1.3	imes10^{-11}
=
1.84576674	imes10^{-5}.
]

Therefore

[
oxed{
1.84576674	imes10^{-5}
<
1.8869797018800170	imes10^{-5},
}
]

leaving

[
oxed{
4.12129618800172	imes10^{-7}
}
]

of absolute margin, about (2.18%) of (M_{m primary}).

Thus a joint constant **6.0** is sufficient.

The exact break-even joint constant under these same reserves is approximately

[
6.1375.
]

---

## 4. Consequence for Sandbox effort

v14.086's current rigorous joint constant is

[
12.40.
]

The old target 4.1 required an improvement of roughly

[
12.40/4.1approx3.02	imes.
]

Under the primary v14.089 margin, the sufficient target 6.0 requires only

[
oxed{
12.40/6.0approx2.07	imes.
}
]

So, if v14.088 is promoted, Sandbox can aim at **joint <= 6.0** rather than <=4.1. No particular split between off-diagonal and diagonal channels is imposed; any rigorous joint estimate at or below 6.0 suffices with the stated reserves.

---

HANDOFF-NOTE
target: sandbox
type: coordination
parent: v14.090
status: informational
action: Conditional on independent promotion of v14.088/v14.089, replace the v14.086 sufficient joint target 4.1 by the relaxed target 6.0. The new target needs only a ~2.07x improvement over the current rigorous 12.40 constant. Any rigorous joint oscillatory estimate <=6.0 is sufficient after paying delta-u, K=10, and a 2e-8 smooth-remainder reserve.
constraints: Do not consume M_primary before the v14.088 audit promotes the primary M32000 floor. Preserve the same frozen N=32k normalization and A_max=804, ||w_o||||w_e||=3.7281e-9 data.
