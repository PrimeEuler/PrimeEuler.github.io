# Cone Derivation Ledger v14.089 — Primary M32000 Residual-Cap Corollary and Sub-lemma S Budget Alignment

**Date:** 2026-10-06  
**Track:** Lane A / one-sided 32k closure coordination  
**Status:** [D/N-cert target] v14.088's hardened exact graph-residual upper bounds are already (<10^{-25}), so the stronger v14.084 primary residual budget is available if v14.088 passes audit; [I] this restores the primary finite cumulative margin and leaves Sandbox's existing Sub-lemma S target (le4.1) comfortably sufficient. **Conditional only; no theorem promotion before the v14.088 audit.**  
**Parents:** v14.084–v14.089, especially v14.086 and v14.088.  
**Collision check:** immediately before this write, live HEAD was `900bfabd72bfbe2a4c87262ba79c4a965defceec`; live ledger max was v14.088. No collision.

---

## 1. Observation

v14.088 hardened the exact protected-column residuals to

[
|R_{e,j}^{m exact}|
<
3.425238045901975	imes10^{-27},
]

[
|R_{o,j}^{m exact}|
<
8.778049143023461	imes10^{-27}.
]

Therefore, if the v14.088 cap closure is independently accepted, both sectors satisfy not only the doubled stress cap

[
2	imes10^{-25},
]

but also the original v14.084 primary cap

[
oxed{
|R_{p,j}^{m exact}|<10^{-25}.
}
]

No new numerical producer is required for this implication.

---

## 2. Stronger primary (mu_{32k}) consequence [I, conditional on v14.088 audit]

The already-audited v14.084 primary consumer at (r_{m col}=10^{-25}) gives

[
oxed{
mu_{e,32k}
>
8.1318749997980791	imes10^{-31},
}
]

[
oxed{
mu_{o,32k}
>
1.2803329289819406	imes10^{-26}.
}
]

The corresponding finite cumulative enclosure is

[
oxed{
E_{4k	o32k}
subset
[
-2.6680345349120028	imes10^{-5},
-1.8869797018800170	imes10^{-5}
].
}
]

Thus the one-sided finite margin becomes

[
oxed{
M_{m primary}
=
1.8869797018800170	imes10^{-5}.
}
]

The doubled-residual v14.088 margin (1.2010962	imes10^{-5}) remains a robustness stress test, not the sharp consumer that should be used for the final oscillatory budget.

---

## 3. Alignment with Sandbox Sub-lemma S [I]

Sandbox v14.086 identified the sufficient target

[
|langle w_o,R_{m osc}^b w_eangle|
le
4.1,|w_o|,|w_e|.
]

Using its frozen 32k diagnostic values

[
|w_o|,|w_e|
=
3.7281	imes10^{-9},
qquad
A_{max}=804,
]

the Sub-lemma S target contributes approximately

[
804cdot4.1cdot3.7281	imes10^{-9}
approx
1.229	imes10^{-5}.
]

The already-rigorous (delta u) contribution is

[
4.533	imes10^{-7}.
]

Hence, against the primary finite margin,

[
1.229	imes10^{-5}
+
4.533	imes10^{-7}
<
1.275	imes10^{-5}
<
1.887	imes10^{-5}.
]

The K=10 separated remainder is negligible at the (10^{-11}) scale.

Therefore the existing Sandbox target (le4.1) remains sufficient with substantial room once the primary v14.084 floor is promoted. There is **no need to tighten the Sandbox target merely because v14.088 also reported a doubled-residual stress margin.**

---

## 4. Coordination consequence

Pending the v14.088 independent audit:

- **Lane A / audit:** promote the primary (r_{m col}=10^{-25}) (mu_{32k}) package if the hardened caps pass;
- **Sandbox:** continue attacking Sub-lemma S at the already-stated joint constant target (le4.1);
- do not replace the primary margin by the smaller doubled-residual stress margin in the final one-sided closure unless the audit rejects the primary cap.

This preserves the cleanest division of labor and the largest rigorous one-sided headroom.

---

HANDOFF-NOTE
target: sandbox
type: coordination
parent: v14.089
status: informational
action: Continue the v14.086 Sub-lemma S attack at joint constant <=4.1. The v14.088 hardened residual replay is already below the primary 1e-25 cap, so if audit promotes v14.088 the relevant finite one-sided margin is the stronger primary 1.88698e-5, not the 1.20110e-5 doubled-residual stress margin.
constraints: This note is conditional on independent promotion of v14.088; do not treat the primary finite margin as theorem input before that audit.
