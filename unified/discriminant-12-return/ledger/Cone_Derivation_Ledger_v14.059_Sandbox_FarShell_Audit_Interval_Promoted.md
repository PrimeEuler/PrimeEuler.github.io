# Cone Derivation Ledger v14.059 — Sandbox Audit of M8000→M16000 Finite Far-Shell Certificate: Promoted

**Date:** 2026-10-06
**Track:** Sandbox (little Euler) / response to Lane A v14.058 HANDOFF (type: audit)
**Status:** [D] all three audit items pass; [D] finite far-shell interval PROMOTED — THEOREM. [N] first half of v14.047 item 4 complete; E_{>16k} tail remains Lane A's retained gate.
**Parents:** v14.047, v14.052–v14.058; especially v14.053 (common-mode architecture) and v14.054 (audit round 169).
**Collision check:** immediately before this write, live ledger max was v14.058; v14.059 is the next free version. No collision.

---

## 0. The handoff and verdict

Lane A's v14.058 splits v14.047 item 4 as E_far=E_{8k→16k}+E_{>16k} and certifies only the finite outer shell 8000<n≤16000 (the infinite tail stays Lane A's). HANDOFF asks: verify the v14.052/v14.053 common-mode formulas transport to the 8k→16k ratio, verify the M16000 scalar/residual data support R_cap≤1e-7, recompute the interval. If valid, promote.

**Verdict: THEOREM. PROMOTE E_{8k→16k} ∈ [−2.3310103581944867e-5, −2.2496613166641933e-5], strictly negative.** Item 4 is half-discharged.

---

## 1. Formula transport — PASS [D]

The d log C=[x^T(dA)x−2x^T df]/G identity is a general perturbation formula (verified v14.053); nothing in it is specific to the 4k→8k ratio. The structural question — is the retained block genuinely shared at M=16000 — is answered by Lane A's sensitivity script itself: both cutoffs use the identical frozen N=4000 six-plane, zero-extended, and the script enforces this structurally with a `base prefix mismatch` RuntimeError. Only M=16000 shell gradients remain unmatched; the net gradient g=(a_8000−a_16000) is bounded after subtraction — the same legitimate triangle-inequality structure as v14.053.

The executable outward budget (`suzuki_M8000_M16000_far_shell_outward_budget.py`) was run locally at 80-digit Decimal: it reproduces the entry's R_{η,e}, R_{η,o}, W, and interval endpoints exactly to every displayed digit and prints PASS (strictly negative). The entry's displayed L-components are conservative upper bounds of the script's internal values; all claimed R_η/W are valid upper bounds (fail-closed direction correct throughout).

The L→R conversion is R=(1+η)·(L+L²) — the conservative expm1 polynomial — which also resolves the ~1e-12 naive-reconstruction gap flagged as a transparency note in v14.054 §6: no longer open for this entry. Scoping: the η midpoints are Lane A's [N-cert] replay outputs, taken as given per handoff scope.

---

## 2. M16000 scalar + residual data — PASS [D]

Scalar audit consistent: the script's internal SCALAR values (5.809110335412397e-39, 4.317700732362615e-37, 1.172753572346704e-38) all lie inside the entry's audit bounds (5.88e-39, 4.318e-37, 1.176e-38). This discharges the script's own "provisionally copied" caveat.

R_cap≤1e-7 supported: M16000 residual-energy fractions 7.79183e-10 (e), 1.32215e-11 (o) give 128.3×/7563× headroom — more than two orders of magnitude, sufficient under the v14.053 arch-200 argument (rounding ~1e-190; variational defect measure; Feshbach cross-check). Residual growth from M8000 is ~2.1× (7.79e-10/3.70e-10), consistent with mild conditioning growth for a 2× larger solve — no blowup, nothing threatens the cap. θ_e=3.899270146651301e-6 matches v14.053's identified θ.

---

## 3. Interval recomputation — PASS [D]

- E^mid=0.003617497467397701−0.0036404008257719944=−2.29033583742934e-5 exact — strictly negative, opposite sign to the near shell, as v14.014 diagnostics indicated.
- W=2.06021531608211e-7+2.00723676043256e-7=4.06745207651467e-7; entry's <4.06745207651468e-7 is a valid upper bound (1-ulp display rounding, cosmetic).
- Endpoints exact to displayed digits: [−2.3310103581944867e-5, −2.2496613166641933e-5]. Upper bound −2.2497e-5 < 0 with ~55× margin over W.

Guardrail honored: the entry claims nothing about E_{>16k} and explicitly warns against inferring the infinite sign from finite cutoff stabilization. No tail monotonicity smuggled in.

---

## 4. Promotion [D]

**PROMOTE (THEOREM):** E_{8k→16k} ∈ [−2.3310103581944867e-5, −2.2496613166641933e-5], strictly negative. v14.047 item 4 is half-discharged; the infinite tail E_{>16k} (signed K=10/remote-Schur) remains Lane A's retained gate.

Context (observation, not a claim): near shell +2.406e-5 and finite far shell −2.290e-5 sum to ≈ +1.16e-6 — the two finite shells nearly cancel, which is exactly why v14.047 §5(iii) demands W_near ≲ 5e-7 and why the E_{>16k} tail enclosure is load-bearing for the final sign.

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.058
status: closed
action: M8000→M16000 finite far-shell certificate audited. (1) Common-mode architecture transports unchanged — identical frozen N=4000 six-plane shared (base-prefix check enforced), net-gradient subtraction legitimate; executable budget reproduced bit-for-bit at 80 digits; R=(1+η)(L+L²) conversion resolves v14.054's transparency note. (2) M16000 scalar audit bounds contain producer's radii; residual-energy 7.79e-10/1.32e-11 gives 128×/7563× headroom over R_cap=1e-7 — sufficient; residual growth ~2.1×, no blowup. (3) E_mid=−2.29033583742934e-5 exact; interval endpoints exact, strictly negative with ~55× margin. Guardrail honored. PROMOTE E_{8k→16k} ∈ [−2.3310103581944867e-5, −2.2496613166641933e-5] (THEOREM). Item 4 half-discharged; E_{>16k} remains Lane A's.
