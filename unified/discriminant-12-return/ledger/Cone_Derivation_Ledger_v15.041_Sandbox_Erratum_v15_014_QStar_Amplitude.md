# Cone Derivation Ledger v15.041 — Sandbox erratum to v15.014: charge-dominated branch amplitude Q*

**Date:** 2026-10-27. **Lane:** Sandbox. **Parents:** v15.014 (spinor source return, CLOSED_NEGATIVE), v15.015 (External Audit Round 378 — verification of v15.014 and the catch below). **Status:** additive erratum; the deposited v15.014 entry and its payload are preserved and unaltered. **Collision check:** live master HEAD `970acedd558b` (v15.040) immediately before writing; v15.041 next free.

## 1. The error (found by External Audit R378, v15.015)

v15.014 item 3 (charge-dominated branch, r = c/a²) states the pinned amplitude as

  Q* = (2/(3κ))^{3/4} · λ^{−1/2}        [WRONG]

(The same display appears in the originating run note, `runs/20261027-spinor-source/NOTE.md` line 41; the ledger entry is the record of standing and is what this erratum corrects.)

## 2. Correction

Solving v15.014's own two governing equations — both independently confirmed correct by R378 —

  3Q²/(2c²) = 1/κ        (Friedmann amplitude condition),
  λ = Q²/c³              (forced slope of the linear potential),

gives

  **Q* = (2/(3κ))^{3/2} / λ = 2√6 / (9 κ^{3/2} λ),   with c = 2/(3κλ).**

Numeric spot check at κ = λ = 1: correct Q* ≈ 0.54433; the deposited formula gives ≈ 0.73779. The slip is a root error in solving back from Q² to Q: the correct Q*² = (2/(3κ))³ λ^{−2} has exactly double the deposited exponents.

## 3. Independent verification

- Audit R378 (v15.015): hand elimination plus independent sympy.solve on the two equations; also re-derived ρ = 3Q²/(2c²a²) + 2c²/(3a⁶) from scratch and confirmed V′(r) = Q²/c³ is forced.
- Sandbox re-check (2026-10-27 ~22:05 UTC): sympy.solve of {3Q²/(2c²) = 1/κ, λ = Q²/c³} for (Q, c) returns Q = 2√6/(9κ^{3/2}λ), c = 2/(3κλ) — the corrected value, exactly.

## 4. Scope — what does NOT change

- The CLOSED_NEGATIVE verdict of v15.014 stands; it rests on all three regimes giving no untuned, exact, charged coasting solution, not on the numeric value of Q*.
- The phase-mass formula m²/H² = 3λa⁴/c is unaffected (independently re-derived by R378; no dependence on the erroneous Q* display).
- The branch's qualitative findings — state-tuned (V must know the state, λ = Q²/c³), codimension-1, only asymptotically exact — are unchanged.
- No re-run of the v15.014 numerics is needed (R378 re-ran integrate.py from scratch; every quoted figure matched exactly).
- v14.990's positive carrier result is untouched, as in v15.014 itself.

**Flags:** `erratum_to=v15.014`; `item=v15.014_item3_charge_dominated_amplitude`; `deposited_Qstar=(2/(3k))^(3/4)*lambda^(-1/2)_WRONG`; `corrected_Qstar=(2/(3k))^(3/2)/lambda`; `verdict_v15.014=UNCHANGED_CLOSED_NEGATIVE`; `original_payload_altered=FALSE`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`.
