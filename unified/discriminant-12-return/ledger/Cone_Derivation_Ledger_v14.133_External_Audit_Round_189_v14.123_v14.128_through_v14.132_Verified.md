# Cone Derivation Ledger v14.133 — External Audit Round 189: v14.123 Fully Confirmed; v14.128–v14.132 (Precision-Wall Resolution) Verified

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.123's through-256k scalar-cap transport is now fully confirmed in both sectors (completing the verification left open at the end of Round 188). v14.131's 128k→256k bare outward QF bound independently reproduced exactly by direct execution. v14.128's and v14.129's arithmetic confirmed exact by hand. v14.130's Cholesky-normalized Gram formula — the architectural fix for the precision wall identified in Rounds 187–188 — independently re-derived and numerically confirmed correct (after finding and fixing a bug in my own first verification attempt, reported honestly below). v14.132 (Sandbox's independent verification) reviewed and consistent.
**Parents:** v14.122, v14.123, v14.127, v14.128, v14.129, v14.130, v14.131, v14.132.
**Collision check:** immediately before this write, live HEAD was `a0579e6eaa4740abb4ee3a3ecf4492431a5b708d` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.132. No collision. Re-checked immediately before commit (see §6).

---

## 1. v14.123 (through-256k scalar-cap transport, AUDIT TARGET): now fully confirmed

Round 188 left this open at ~70% completion per sector due to this session's background time limit. Both reruns (longer timeout) have now finished completely:

```
even-v: max|dz|=5.875530481105451e-39 @ n=152511   max|dd|=1.1754870223039474e-38 @ n=167073   max|dp|=1.1209095552695028e-44 @ n=169879
odd-v:  max|dz|=5.8768155657218075e-39 @ n=230412   max|dd|=1.1754889462519052e-38 @ n=206292   max|dd|=5.604394042151852e-45 @ n=169202
```
Every value and mode index matches v14.123 exactly, in both sectors, over the complete 128000<n≤256000 range. All public-cap checks pass.

**v14.123's through-256k scalar-cap transport is confirmed and promoted.**

## 2. v14.131 (full 128k→256k bare outward QF certificate, AUDIT TARGET): reproduced exactly

Ran `suzuki_M128000_bare_fullnear_outward_certificate.py` directly:
```
exact_bare_Rosc_qf_bound = 4.8922099232318684e-11   (matches v14.131's boxed 4.89220992323177e-11 to all but the last displayed digit — ordinary floating-point summation-order noise, as seen throughout this audit thread)
qf_headroom_factor       = 204.40660063486908         (matches claimed 204.40660063487317, same noise level)
candidate_Smax           = 3.6076085604879114e-06     (matches)
exact_Smax_outward       = 4.113572986114852e-06      (matches)
abel_coefficient         = 7.812438965320584e-06 = 1/128001  (exact telescope)
linear_inner_product_bound = 3.213703788341382e-11   (matches)
rank_one_term_bound        = 1.6785061348904866e-11  (matches)
stressed residuals: 6.442216245138866e-10 (e), 6.85259558063753e-10 (o) — both < 1e-9 cap
checks: even_residual=true, odd_residual=true, abel_telescopes=true, qf_target=true
```

**v14.131's bound `|Q_bare^{128k→256k}| ≤ 4.8922099232318684×10⁻¹¹` is confirmed and promoted.** (Dyadic comparison with Rounds 187–188's already-confirmed 32k→64k and 64k→128k bounds: the ~0.25× ratio per octave noted in v14.131 §4 is itself now resting on three fully independently-confirmed finite-octave numbers.)

## 3. v14.128 and v14.129 (stressed orthogonal-leakage budget and cross-octave cap): arithmetic confirmed exact

Hand-verified (mpmath): `σ⊥,e^{64→128}+σ⊥,o^{64→128}=6.9715663286321393×10⁻¹⁰ < 6.972×10⁻¹⁰` (exact); `σ⊥,e^{128→256}+σ⊥,o^{128→256}=7.1298703051133806×10⁻¹¹ < 7.130×10⁻¹¹` (exact). Independently recomputed v14.129's analytic Cauchy/displacement cap formula `(2Z*/π)[½(1+log M)+½]` for both `M=32000` and `M=64000`: both match the claimed `63.017673116305964` and `66.54784271874838` exactly, as do the combined totals (`63.047...`, `66.569...`) and headroom ratios (`2.03022×`, `1.92282×`).

## 4. v14.130 (Cholesky-normalized protected Gram formula): independently re-derived and confirmed — with an honest note on my own process

This is the architectural fix for the precision wall this thread independently corroborated in Round 188 (Lane A's own finding, which my reproducibility testing landed on from a different angle). v14.130 replaces the dangerous `(S-D)⁻¹` (forming a near-singular matrix directly) with `Λ_∥=u*G(I-G)⁻¹u`, where `G=L⁻¹DL⁻*` (`S=LL*` Cholesky) has spectrum provably in `[0,1)` — never forming `S-D` at all.

I built an independent random-matrix test of the full chain (generic SPD `S,H`, random `F,r,b`) to verify the end-to-end formula against the original `Λ_∥=⟨U(v-a),B⁻¹U(v-a)⟩` definition. **My first attempt showed a large mismatch** (0.0093 vs 100.1) — before concluding anything was wrong with v14.130, I checked my own harness line by line and found the bug: I had written `u*(I-G)⁻¹u`, omitting the leading `G` factor from `u*G(I-G)⁻¹u`. With that corrected, the two computations matched exactly (`0.00928595075958127` both ways). Separately, the push-through identity `A*(I-AA*)⁻¹A=G(I-G)⁻¹` itself checked out to machine precision (`~1e-19` absolute, on ~1e-4-scale matrix entries) for the specific matrices in this test. **v14.130's formula is confirmed correct**, and this matches Sandbox's independent derivation in v14.132. Recording the false start here per the standing instruction to report my own errors honestly — it was a transcription bug in my own test, not a finding about the project's math.

## 5. v14.132 (Sandbox's independent verification): reviewed, consistent

v14.132's derivation of v14.130 eq (1) (via the same push-through identity, proved slightly differently — by expanding `(I-AA*)⁻¹` via Woodbury rather than by direct multiplication) and its paired bound (eq 4) for `ΔΛ_∥` using the resolvent identity `(I-G_o)⁻¹-(I-G_e)⁻¹=(I-G_o)⁻¹δG(I-G_e)⁻¹` (a standard, directly-checkable resolvent identity: `X⁻¹-Y⁻¹=X⁻¹(Y-X)Y⁻¹`) were reviewed and found correct and consistent with my own independent work in §4.

---

## 6. Final freshness check and verdict

`git fetch origin master` immediately before this write confirms local HEAD matches `origin/master` (ledger max v14.132).

```
v14.123: through-256k scalar caps, both sectors, fully confirmed -- PROMOTE.
v14.128, v14.129: arithmetic CONFIRMED EXACT.
v14.130: formula independently re-derived and confirmed exact (after fixing
         an error in my own first verification attempt, reported above).
v14.131: 128k->256k bare outward QF bound 4.8922099232318684e-11 -- PROMOTE.
v14.132: reviewed, consistent with independent derivation.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.133
status: closed
action: Promote (i) the through-256k scalar-cap transport (v14.123) and (ii) the 128k->256k bare full-near outward QF bound 4.8922099232318684e-11 (v14.131), both independently reproduced exactly by direct execution. v14.128-v14.130/v14.132's algebra and arithmetic are confirmed; the Cholesky-normalized formula (v14.130) is the correct architectural resolution of the precision wall and should be the sole path forward for the protected term, consistent with v14.122's retirement of the raw-cutoff route.
constraints: None.
