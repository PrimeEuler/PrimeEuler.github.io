# v13.855 — Sandbox Bucket 2: PAIR-H bulk lemma — refined, correcting W2

**Date:** 2026-09-29
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — sandbox numerics + exact algebra, not certified
**Entry kind:** (PAIR-H)'s bulk lemma — the concrete analytic target named by v13.853 §7(1); verdict is **refined, not proved**, because the investigation **corrected** the W2 picture rather than confirming it
**Corrects:** v13.853 §2 (PAIR-H)'s "interval length" mechanism — refuted for I_0; replaced by test-function growth
**Confirms:** v13.853 §5 (R2 as the consistency condition that the same 0.48 governs both scales)

**Headline: bulk lemma refined.** The W2 picture — "the extra A in r_{0,A} comes from interval length in the moment integral; bulk and edge contribute comparably" — is **refuted** by direct bulk/edge splitting. The corrected picture: the I_0 moment pairing is **edge-localized** (the bulk interior contributes ≈0; the full Θ(Ae^A) comes from the right edge layer where the e^A-scale boundary mass meets the linearly growing test function g(y)~c_1|y|). The I_1 pairing is genuinely two-scale (bulk +0.26e^A, edge −0.73e^A, opposite signs). The macroscopic source limit is exact and linear: s_A(ηA)/(Ae^A)→L_1η+L_0=0.48(1−η). R2 consistency confirmed: L_0+L_1→0. The 0.48 value now has a concrete address: L_0=−c_1∫V∞^+ with c_1 set by −L'/L(1/2,χ_{12}).

---

## 1. Lemma A — Macroscopic source limit (EXACT)

s_A(x)=e^x+A_coef x+B_coef with A_coef=L_1e^A(1+o(1)), B_coef=L_0Ae^A(1+o(1)). Then for η∈(−1,1): **s_A(ηA)/(Ae^A) → L_1η+L_0**; under R2 (L_0+L_1=0): **→ L_0(1−η)**. For the derivative, uniformly on bulk compacts {x : e^x=o(e^A)}: **s_A'(x)/e^A → L_1**. Verified at A=6: L_0=+0.459, L_1=−0.471, L_0+L_1=−0.012; the macroscopic profile matches L_1η+L_0 to 3 decimals at η∈{−0.75,−0.5,−0.25,0,0.25,0.5}; s_A'/e^A is −0.47±0.01 across the bulk. **Correction to the v13.853 task statement:** the source ratio is **linear** L_0(1−η), not constant; the constant −0.48=−L_0 is the **derivative-source** limit s_A'/e^A→L_1, via R2.

## 2. Lemma B — Pairing localization (NUMERICAL, refines W2)

Split I_{0,A}=I_{0,A}^{bulk}(δ)+I_{0,A}^{edge}(δ), bulk |y|≤A−δ, edge A−δ<|y|≤A. For fixed δ≥3:
- (a) **I_{0,A}^{bulk}(δ)/(Ae^A)→0** (numerically |I_{0,A}^{bulk}|/(Ae^A)<0.005 at A=6).
- (b) **I_{0,A}^{edge}(δ)/(Ae^A)→L_0=+0.48** (captures 99.8% at A=6, δ=3).
- (c) The cumulative pairing density ∫_{−A}^y−gv stays within ±0.008·Ae^A for y≤A−3, then rises monotonically to +0.466·Ae^A over y∈[A−3,A]. **100% of I_{0,A} accumulates in the right edge layer** (for the + channel).
- (d) For I_{1,A}: bulk and edge are **both** Θ(e^A) with opposite signs (+0.26e^A bulk, −0.73e^A edge at A=6, δ=3). **The I_1 pairing is genuinely two-scale; the I_0 pairing is not.**

**Mechanism (heuristic, sandbox grade).** In ξ=A−y:
I_{0,A}^{right}/(Ae^A) = −∫_0^δ [g(A−ξ)/A]·[v_A(A−ξ)/e^A] dξ → **−c_1∫_0^∞V∞^+(ξ)dξ = L_0**,
where g(A−ξ)/A→c_1=−0.154 is the **transported test function** and V∞^+ is W1's edge profile. **The extra A comes from test-function growth (g~c_1A at the edge), NOT from integrating an O(e^A) density over O(A) width.** The bulk interior cancels because the oscillatory O(e^A) bulk response v_A averages to zero against the slowly-varying (even, O(|y|)) test function g. **This refutes W2's "interval length" mechanism** — the W2 claim that "the extra A comes from interval length in the moment integral" is incorrect for I_0; the bulk is e^A-scale in sup norm but contributes ≈0 to the pairing.

**Key analytic input (new):** the D12 screw kernel g(t)=R_{12}(t)−A_{12}(t) is **not** exponentially growing. Numerically (LightScrew, validated against W1 constants): g(t)=c_1|t|+c_0+O(1) oscillations, c_1≈−0.154, c_0≈−0.16 on [6,12], g exactly even. The linear drift comes from −A_{12}(t)~+1.29t partially cancelled by R_{12}(t)~−1.44t (the latter set by −L'/L(1/2,χ_{12}); analytic value not derived here).

## 3. R2 as the consistency condition (confirmed)

| A | L_0=B_coef/(Ae^A) | L_1=A_coef/e^A | L_0+L_1 |
|---|---|---|---|
| 3 | +0.429 | −0.477 | −0.048 |
| 4 | +0.460 | −0.467 | −0.008 |
| 5 | +0.468 | −0.466 | +0.002 |
| 6 | +0.459 | −0.471 | −0.012 |

The same 0.48 appears as: **bulk:** s_A'(x)/e^A→L_1=−0.48 (derivative-source, interior); **edge/moments:** I_{0,A}/(Ae^A)→L_0=+0.48 (pairing, boundary layer); **edge shape:** α∞=+0.48 (W1/W2, invariant trace data). R2 is the consistency condition that these are negatives of each other.

## 4. What was NOT obtained (refined open points)

1. **Analytic mechanism of bulk cancellation.** Why ∫_{|y|≤A−δ}g(y)v_A(y)dy≈0 exactly is not derived. Likely involves the oscillatory structure of the minimum-norm v_A (cf. v13.848 selection identity) against the even slowly-varying g. **Input that would fix it:** a rigorous oscillatory-integral or approximate-identity argument for the Tikhonov-selected v_A in the bulk.
2. **Extension to G_A,H_A.** This entry covers the moment pairings I_{0,A},I_{1,A} (which control the shape via r_{0,A},r_{1,A}). The actual (PAIR-H) pairings in v13.757 (18) involve the test object D̄e_{z̄}, whose exact definition/action (including boundary/distribution terms) was **not located** in the ledger (v13.739–v13.743 searched; v13.853 already noted the defect-pair definition is missing). Moment pairings are a faithful proxy for scaling; the G_A/H_A bulk lemma specifically needs D̄.
3. **Analytic value of 0.48.** Still unexplained (as in all prior Bucket 2 entries) — but now with a **concrete address**: L_0=−c_1∫V∞^+ with c_1 set by −L'/L(1/2,χ_{12}). Connecting c_1≈−0.154 to L_0=+0.48 via the edge integral is a concrete analytic target.
4. **The I_1 bulk/edge split** is δ-sensitive (unlike I_0). "Both Θ(e^A)" is robust, but the precise constants depend on the cutoff; a cleaner split (e.g. via the ξ-coordinate edge profile) would sharpen it.

## 5. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260929-001603-bucket2-pairh-bulk-lemma/` (report.md, STATUS.md; data: `bulk_split.json`, `bulk_scaling.json`, `profile_dump.log`; scripts: `light_screw.py` (memory-light D12Screw — built after the stock constructor OOM'd on the 7GB box), `bulk_split.py`, `profile_dump.py`, `bulk_scaling.py`)
- (8.5)-LS solves: λ=0, + channel, natural BCs, A=2–6, quadrature-validated moments I_{0,A}=1+B_coef, I_{1,A}=1+A_coef
- All conditional on λ_a>0 (v13.848). No positivity/RH/Hilbert–Pólya claim; prime ramp untouched.
