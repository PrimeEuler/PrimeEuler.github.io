# Cone Derivation Ledger v14.698 — Sandbox erratum to v14.696: the §1.2 eccentricity producer was a docstring, and its cited example was wrong — corrected producer deposited, claim replaced by the state taxonomy

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.696 (the entry corrected here) and v14.697 (External Audit Round 330, which found the defect and verified the rest of v14.696 exactly). Filed by the sandbox on its own error, per the program's report-own-errors standard; Jeremy relayed the finding the same day.
**Status:** correction entry. It changes no certified object, no paper, and no other v14.696 verdict: R330 verified §2 (dwell), §3 (rephasing, extended independently to negative m), §4 (Stark), §5 (revivals), and the §1.4 negative-result numbers exactly. `G_derived = false` and all other v14.696 scope flags stand as deposited, with the one amendment at the end of this entry.

## The defect

v14.696 §1.2 cited producer `eccentric_test.py` for the eccentricity-deformation claim, quoting ratios "0.64–0.99 in θ" for the state (j=1, m=0). Two failures, both the sandbox's:

1. **The deposited file contained no code.** As pushed (SHA-256 in the v14.696 manifest, confirming the state is as-deposited, not a transmission artifact), `eccentric_test.py` was a 7-line docstring. The computation had been run inline in-session and never written to the file; the file saved only its summary. A cited producer that cannot be re-run is not a producer.
2. **The cited example was wrong as stated.** For (j=1, m=0) the integral is I_{1,0}(θ) = (1/2π) ∫ (cos θ + iρ sin θ cos χ) dχ = **cos θ exactly, at every ρ** — the k=1 term's moment vanishes. That state shows *no* deformation whatsoever; the quoted 0.64–0.99 range was measured against a squashed-*angle* Legendre comparison function (P₁⁰ of the eccentric angle), whose own θ-dependence produced the spread. The number did not describe deformation of the integral, and for the state named there is none. R330's from-scratch implementation established this; the sandbox has re-derived it independently (below) and concurs without reservation.

## The corrected producer and the corrected claim

`eccentric_test.py` is replaced in the payload by a complete producer: the integral evaluated exactly by the binomial/moment sum (moments 2^{−k} C(k, (k−m)/2), Fraction-exact, as in `rephasing_test.py`), with trapezoidal quadrature spot-checks agreeing to 12 digits, j ≤ 3, all m, at e = 0.6 (ρ = 0.5). Verified output (ratio |I_jm(θ; ρ)| / |P_j^m(cos θ)| over θ, |P| > 0.05 mask):

- **INVARIANT** (ratio = the e = 0 constant): (0,0), **(1,0)** — the latter exact, max |I_{1,0} − cos θ| = 0 over 999 angles at ρ = 0.5.
- **AMPLITUDE** (constant ratio, rescaled by ρ^m against the e = 0 constant j!/(j+m)!): (1,1) 0.2500, (2,1) 0.1667, (2,2) 0.0208, (3,2) 0.0125, (3,3) 0.0010.
- **SHAPE** (genuinely θ-dependent ratio): (2,0), (3,0), (3,1) — ranges sweep across the Legendre nodes (e.g. (2,0): 0.0027–5.56 on the stated mask; R330's independent implementation, differently masked, found ≈0.11–1.57 — same qualitative fact).

The corrected §1.2 statement is therefore: *eccentricity deforms the phase-integral family state by state, through the k ≥ 2 binomial moments and mixed-parity channels; single-moment m ≥ 1 states rescale by ρ^m; (1,0) is exactly invariant; the quantum lobes remain the e = 0 member of the family, recovered exactly.* The qualitative conclusion of v14.696 §1.2 — that the eccentric deformation is genuine and not a reparametrization — **stands**, on the (2,0), (3,0), (3,1) states; the specific numeric range quoted there is **retracted**. The foundations note in the payload (§2) is updated to the corrected statement.

## Minor corrections deposited in the same payload refresh

- **`hunt_k.py`** (R330 minor finding): the variable printed as "gap" was the nearest target's raw log value, not the difference. Fixed in place; the script now prints true gaps, and its BEST-single line reads k = 36 vs ψ, gap 2.100 — matching the value the arc had on record. No v14.696 text relied on the mislabeled line (R330 recomputed §1.4(a)'s exponents from the physical quantities directly: 63.67 / 71.10 / 139.79, exact).
- **`RESULTS.md`** (lab record): an intermediate aside read "ln 83.98, required k = 63.77" (and ln 93.65); corrected to ln 83.85, k = 63.67 (ln 93.64) — the values the ledger itself carried. The slip never propagated.
- **`revival_test.py`** (R330 completeness note): the σ = 0.8 run whose numbers v14.696 §5 cites (peak 0.9463 at t/T_rev = 1.0103) was not in the deposited script's parameter list; it is now — the producer reproduces every number §5 quotes.
- **`MANIFEST.sha256`** regenerated over the refreshed payload; changed files: `eccentric_test.py`, `hunt_k.py`, `revival_test.py`, `RESULTS.md`, `foundations_note.md`. All other payload files byte-identical to v14.696.

## Verification

The corrected producer runs clean and its table is reproduced in this entry from its own output; the (1,0) invariance is additionally an analytic identity (the k=1 moment vanishes), not only a numeric one. R330's independent checks of everything else in v14.696 stand and are not repeated here. Updated payload files were pushed to `research-notes/payloads/sandbox_gravity_selector_v14_696/` with fetch-back SHA-256 verification per file, under the same push discipline as the original deposit.

## Scope-flag amendment

v14.696's `eccentric_family = D_identity_N_deformation` is amended to `eccentric_family = D_identity_N_deformation_STATE_DEPENDENT` with the (1,0) invariance and the k ≥ 2 mechanism as stated above. All other v14.696 flags unchanged. This erratum closes R330's finding; the sandbox thanks the auditor — the missing producer would have let a wrong example stand behind a right conclusion, which is exactly what the audit exists to catch.
