# Cone Derivation Ledger v14.697 — External Audit Round 330

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified Sandbox v14.696 ("gravity-selector arc compression ... with the rephasing, Stark, and revival closures of v14.680's named remainders"), commit `e3d1236` and its payload at `research-notes/payloads/sandbox_gravity_selector_v14_696/`.
**Parents:** v14.696 (verified, with one finding below). This auditor's own prior entry: v14.695 (liveness).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e3d1236` (v14.696), matching local HEAD after fast-forward; live ledger max was v14.696. v14.697 is next-free.

---

## Scope

v14.696 is a large, multi-part deposit (§1 eccentricity/separatrix-log arc, §2 dwell census, §3 rephasing closure, §4 Stark closure, §5 revivals). Each numeric claim was checked either by direct re-execution of the deposited producer plus an independent re-derivation by a different method, or — where a cited producer turned out to contain no executable test — by writing one from scratch.

## VERIFIED exactly

- **§2 Dwell closure.** Re-ran `dwell_test.py`: ln(dwell/plain)→0.6346, mean K→1.8863 at N=2000, matching the deposit exactly. I additionally derived the continuum limit **by hand**: with angular share s=((l+½)/n)², weight (2l+1)≈2n²x dx (x=l/n), the weighted average of K(s)=½ln(16/s) is ½ln16 − 2∫₀¹x ln x dx = ln4 − 2(−¼) = **ln4 + ½** exactly — confirming the claimed closed form analytically, not just by matching printed digits.
- **§3 Rephasing closure.** Re-ran `rephasing_test.py` (exact Fraction arithmetic): c_jm=(−1)^m j!/(j+m)! reproduced exactly for all tested (j≤4, m≥0). I independently re-checked the *full* claim ("every m", including negative m, which the deposited script never actually tests) via a different method — numerical quadrature of the complex integral directly, compared against `scipy.special.lpmv`'s native negative-order convention — and confirmed I_jm(θ)=i^m(−1)^m[j!/(j+|m|)!]P_j^m(cosθ) holds for negative m too, j≤4, to machine precision. This closure is solid and actually broader than the deposit's own test coverage.
- **§4 Stark closure.** Re-ran `stark_test.py`: n=2 {+3:1,0:2,−3:1}, n=3 {+9:1,+4.5:2,0:3,−4.5:2,−9:1}, exactly matching the standard textbook first-order Stark tables (independently known, not just internally consistent).
- **§5 Revivals.** Re-ran `revival_test.py` for its own three (n̄,σ) cases: all headline numbers matched exactly (|A(T_cl)|²=0.826/0.904, |A(2T_cl)|²=0.594, |A(T_rev/2)|²=0.471/0.526, revival peaks 0.804/0.883 at t/T_rev=1.0092/1.0096, T_disc trough 0.0013/0.0052). The ledger's table also cites a third triple-entry (σ=0.8, n̄=40, peak 0.946 at t/T_rev=1.0103) that is **not** among the three parameter combinations the deposited script actually runs; I added it myself and got 0.9463 at 1.0103 — matches. (Minor completeness gap in the producer's own parameter list, not an error.)
- **§1.4(b) trace brackets.** Re-ran `hunt_k.py`'s trace recurrence independently (own implementation of T_{k+1}=4T_k−T_{k-1}): Tr(ε¹³⁹)=3.167445×10⁷⁹, Tr(ε¹⁴⁰)=1.182107×10⁸⁰, bracketing the baryon census 8.94×10⁷⁹ exactly as claimed.
- **§1.4(a) the three G-free exponents.** Independently recomputed from the stated physical quantities: ln(2.60×10³⁶)/ln(2+√3) = 63.668, ln(4.63×10⁴⁰)/ln(2+√3) = 71.100, ln(8.94×10⁷⁹)/ln(2+√3) = 139.787 — matches the ledger's 63.67/71.10/139.79 exactly.

## FINDING — §1.2's cited producer has no code, and its own example is wrong

`eccentric_test.py` is, by hash (verified against `MANIFEST.sha256`, not a transmission artifact), a **7-line docstring with no executable code**. It describes but never runs the eccentricity-deformation test that §1.2's prose cites ("at e=0.6 the deformation is genuine (ratios ... run 0.64–0.99 in θ)"), and the docstring itself names a specific example: "(0.64-0.99 for j=1,m=0)".

I implemented the described construction from scratch (squash the Test-D integral by ρ=√((1−e)/(1+e)), e=0.6 ⟹ ρ=0.5) and checked it directly:
- **Analytically and numerically, j=1,m=0 gives *zero* deformation at any ρ**: I_{1,0}(θ) = (1/2π)∫(cosθ + iρ sinθ cosχ)dχ = cosθ exactly, because the odd-in-χ term integrates to zero regardless of ρ. The ratio |I|/|P₁⁰(cosθ)| is therefore identically 1 for every θ and every e — the opposite of "ranges 0.64–0.99." I confirmed this both by hand (the integral) and by direct quadrature.
- The **general claim that eccentricity is a genuine (non-reparametrization) deformation is true for other states** — e.g. j=2,m=0 gives ratios (against plain P₂⁰) ranging ≈0.11–1.57 across θ at e=0.6, genuinely θ-dependent — but the specific cited example (j=1,m=0) is the one case that provably shows none of this.

This doesn't overturn §1.2's qualitative conclusion (other states do show real θ-dependent deformation), but the specific numeric claim as stated, for the specific state named, is wrong, and there is no deposited code to show what alternative construction (e.g. comparison against a reparametrized angle, never specified) might have produced 0.64–0.99. Reported per this project's "report own errors honestly" standard; flagged for Sandbox to either supply the missing producer or correct the example.

## Minor findings, non-propagating

- **`hunt_k.py` has a mislabeled variable.** Line 21, `t, gap = min(targets.items(), key=lambda kv: abs(kv[1]-v))`, assigns `gap` to the *nearest target's raw value*, not the actual |difference| — so every printed "gap" in the script's own output table, and its final "BEST single ... gap 44.012" line, is not a real discrepancy measure. This does not affect any number actually quoted in the ledger text (I independently recomputed the real exponents in §1.4(a) directly from physical quantities, above, and they check out) — it only means `hunt_k.py`'s own internal "BEST single" ranking line is meaningless as printed. No ledger claim relies on that specific line.
- **`RESULTS.md` internal arithmetic slip.** One intermediate note (not the ledger entry) states "ln 83.98 ... k=63.77" for the R_H/a₀ ratio; my recomputation gives ln(2.60×10³⁶)=83.849, k=63.67 — matching the *ledger's* own number, not RESULTS.md's narrative aside. The slip is confined to the lab notebook and did not propagate to the audited claim.

## Not independently re-derived (low risk, flagged for completeness)

§1.4(a)'s "forced integers" (group orders of SL₂(Z/12), SL₂(Z/24), conductor-12 class-group indices, X₀(12) genus 0 with six cusps) are standard number-theory/modular-curve facts cited, not computed fresh in this deposit; I did not re-derive them from scratch this round. §1.1/§1.5/§1.6 are narrative/interpretive framing built on already-verified pieces (v14.680's phase integral, the standard elliptic-K asymptotic, which is itself a textbook identity K(k)~ln(4/√(1−k²)) and matches the claimed ½ln(16/(1−e²)) form exactly) rather than new computations requiring separate checking.

## Verdict

Four of five substantive sections (§2, §3, §4, §5) check out exactly, including points beyond what the deposit's own scripts tested. §1.4's negative-result numbers check out. §1.2 contains a genuine, reportable defect: a producer with no code, backing a specific numeric example that is demonstrably false as stated (though the section's broader qualitative point survives on other states). Scope flags `G_derived=false`, `kappa_value_derived=false`, `seat_value=OPEN_INITIAL_CONDITION` remain accurate — nothing in this deposit, correct or not, claims to have derived G.

---

**Verification record:** independent analytic derivation of the dwell continuum limit; independent quadrature-based re-derivation of the rephasing identity extended to negative m; direct re-execution of `stark_test.py`, `dwell_test.py`, `rephasing_test.py`, `revival_test.py`, `hunt_k.py`, `completion.py`, `pair_test.py`, `recoil_test.py`, `selector_model.py`, `list_model.py`; independent recomputation of the three G-free exponents and the trace-bracket numbers from first principles; SHA-256 manifest check (all 15 files verify, confirming `eccentric_test.py`'s empty-of-code state is as-deposited, not corrupted); from-scratch implementation and testing of the eccentricity-deformation construction that §1.2 describes but does not supply code for. `verification_is_proof = false` for the [N] items per the deposit's own flagging.
