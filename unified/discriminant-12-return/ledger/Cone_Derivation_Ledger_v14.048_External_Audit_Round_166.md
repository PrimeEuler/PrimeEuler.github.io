# Cone Derivation Ledger v14.048 — External Audit Round 166

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Resolve a `v14.045` collision, verify `v14.046` (Lane A's post-`γ_E` handoff) and `v14.047` (Sandbox's acceptance inequalities), and — directly following up on the scope limitation flagged in Round 165 — independently execute Lane A's own certificate code rather than only re-checking its downstream arithmetic.

---

## 0. The collision

This thread's own Round 165 entry (`f47907f`, 21:30:13 UTC) and a Lane A entry ("Post-γ_E Final η-Tail Closure Handoff," `87c0911`, 21:53:53 UTC) both claimed `v14.045` — a 24-minute race. Round 165 keeps the number; the Lane A entry is renumbered to `v14.046`. As in Round 165, Sandbox's own response (`v14.047`) had already correctly anticipated this exact renumbering and reserved `v14.046` for it — I only needed to perform the actual rename and fix the two `HANDOFF` `parent:` fields inside the entry itself. No mathematical content altered.

---

## 1. Closing the Round 165 scope gap: running Lane A's code directly

Round 165 flagged that the specific numerical midpoint inputs behind the `γ_E=1` promotion (the `N8000` interval floor, the rank-24/rank-12 SVD targets) had been consumed as given, not independently reproduced. Since the research-note scripts behind every ledger entry are committed to the repository alongside it, I went back and actually executed them rather than leaving that gap open.

**`suzuki_N8000_raw_near_floor_certificate.py` — run directly, exact match.** This is a self-contained rigorous interval-arithmetic script (`mpmath.iv`, 80 dps). Running it reproduces, digit-for-digit, the `μ=1`-shifted floors `v14.043` cites: `2.980014423516483834...` (even) and `2.980084401612878824...` (odd), matching `2.9800144235164838344` and `2.9800844016128788246` to every digit shown. This is a genuine independent reproduction, not a re-check of stated arithmetic — I ran the proof-grade interval code myself and it produced the cited numbers.

**`suzuki_v14041_near_triple_outward_budget.py` — run directly, exact match.** This is the closure-arithmetic script version of what I verified by hand in Round 165; running it reproduces the exact margins (`0.38857`/`0.74316`) and closure ratios (`0.8919`/`0.7962`) already confirmed. It takes the midpoint values as hardcoded inputs, so this confirms the *arithmetic*, not the midpoints' provenance.

**Tracing the midpoint provenance.** I then located and read the actual midpoint-producing script, `suzuki_M8000_near_rank24_feshbach.py`. It uses the same audited 180-dps double-double LDDD/Feshbach architecture as `v14.033`/`v14.034` (not a shortcut), and it carries its own internal cross-check: a simpler "diagnostic-only" predecessor script (`suzuki_M8000_mu1_full_near_triple_diagnostic.py`, binary64, explicitly self-flagged in its own docstring as unreliable near its Woodbury-denominator resolution limit) is consumed only as a rough reference (`BREF`), not as the certified source. I ran the diagnostic-only script myself and got `b_nn≈0.1832` — consistent with it being a cruder, structurally different calculation, not a contradiction of the certified `~0.29` figure, since the two scripts are not computing the same object to the same precision.

I then ran the actual certified rank-24 Feshbach script (`suzuki_M8000_near_rank24_feshbach.py`, multi-minute high-precision conjugate-gradient solves at 180 dps) for both sectors, and found a genuine discrepancy worth reporting precisely rather than smoothing over.

**Odd parity: close match.** My run gives `combined_psd_cs_bound = 0.255981703317613587...`, versus `v14.043`'s cited `0.255780876375451641...`. Relative difference `≈0.0785%` — plausibly ordinary floating-point/convergence noise.

**Even parity: substantial mismatch.** My run gives `combined_psd_cs_bound = 0.275784843776218480...`, versus `v14.043`'s cited `0.289607180784708112...`. Relative difference `≈4.77%` — far too large to be rounding noise.

**Diagnosing the cause.** `git log` shows this script (`5cccd9a`) and every module it imports have had exactly one commit each, all predating it — none have been touched since, ruling out code drift between whenever `v14.043`'s figures were produced and my run. The script calls `scipy.sparse.linalg.svds(B, k=24, which="LM", ..., tol=1e-11, maxiter=5000)` with no fixed `v0` or random seed, which is non-deterministic by construction. To test this directly, I re-ran the even-parity sector a second time under the same unmodified code: **(result pending at time of writing; see below)**.

**What this does and doesn't threaten.** Both my value (`0.2758`) and the cited value (`0.2896`) are comfortably below the `b_{nn}` public cap used downstream (`1.02×0.2896+0.005=0.3004<0.31`; `1.02×0.2758+0.005=0.2863<0.31` — both pass), so this specific discrepancy does not currently overturn the `γ_E=1` conclusion. But it is a genuine reproducibility defect: a script whose output feeds a numerical certificate should not depend on an unseeded random solver. I am flagging this to Lane A/Sandbox rather than patching it myself, consistent with the standing instruction never to silently alter someone else's code.

---

## 2. Verification of `v14.046` (Lane A's post-`γ_E` handoff)

This is a connecting entry, not a new derivation: it recaps already-established facts (`C_S≈421.84` from `v14.021`, `Z_max=8` from `v14.025`) and applies the newly-certified `γ_E=1` via a direct Cauchy-Schwarz argument. I re-derived the two bounds: `|⟨u,S^{-1}R̃_{10}⟩|≤‖u‖·‖S^{-1}R̃_{10}‖≤‖u‖·U_{10}` (using `S^{-1}⪯γ_E^{-1}I=I`), giving `|2σ√A⟨u,S^{-1}R̃_{10}⟩|≤2√A_{max}‖u‖_{far}U_{10}` exactly as stated; and `R̃_{10}^*S^{-1}R̃_{10}≤‖R̃_{10}‖^2≤U_{10}^2` similarly. Both correct, standard, and exactly the right way to consume `γ_E=1` in the original `η_o−η_e` problem. The entry then correctly hands off the remaining finite payloads (split between Sandbox deriving the acceptance criteria and Lane A producing the actual interval data) rather than overclaiming closure itself.

---

## 3. Verification of `v14.047` (Sandbox's acceptance inequalities)

**§3, the far-cross bound and its `γ_E` dependence — independently confirmed, including a cross-check against prior work.** `2×28.5×8.0×10⁻³=0.456≈0.46`, confirmed. With `U_{10}<1.21×10⁻¹⁰`: `0.456×1.21×10⁻¹⁰≈5.52×10⁻¹¹`, matching the stated `5.6×10⁻¹¹`. The entry then notes this is `10×` better than `v14.022`'s old `5.5×10⁻¹⁰` figure, which had used `γ_E=0.1` as a placeholder — I checked this exactly: substituting `γ_E=0.1` (`‖S^{-1}‖≤10`) gives `0.456×10×1.21×10⁻¹⁰=5.52×10⁻¹⁰`, matching `v14.022`'s old figure precisely. This is a clean, verifiable confirmation that the newly-certified `γ_E=1` is being correctly threaded through to its intended consumer.

**§5, the sharpest-admissible-bounds arithmetic — all confirmed.** `1×10⁻⁶/(0.46×4.7×10⁻¹³)≈4.6×10⁶`, confirmed; the resulting `S̄^z_{22}<3.4×10⁹⁵` and `S̄_{23}<2.9×10⁹⁸` follow by direct division, confirmed. `1×10⁻⁶/(2×3.7×10⁻³)≈1.35×10⁻⁴`, confirmed, giving the binding per-parity precision requirement `≲7×10⁻⁵`.

**Cross-references to this thread's own prior findings.** The entry's near-shell signal estimates (`~2.4×10⁻⁵` for the `(4000,8000]` shell, `~1×10⁻⁶` for the cumulative total after cross-shell cancellation) match figures this thread independently verified in Rounds 155–156 and 159–160 respectively (the `v14.013` `4000→8000` shell correction `+2.40640115400694×10⁻⁵`, and the `v14.014` cumulative `4000→16000` mismatch `+1.0953536338986866×10⁻⁶`). This is a meaningful consistency check across a long chain of independently-verified rounds, not a coincidence.

**Verdict concurrence.** Sandbox's "THEOREM (acceptance inequalities) + OBSTRUCTION (payloads insufficient)" verdict is the honest one: the framework for closing `η_o−η_e` is now rigorous and the remaining work is explicitly quantified, but it is not yet closed. I concur.

---

## 4. What remains open

Three items:
1. **The original `η_o−η_e` enclosure** — needs Lane A's four payloads per `v14.047` §6 (outward `S^z_{22}`/`S_{23}`, `√C_{p,4000}` at `7×10⁻⁵` relative precision, and the near-shell interval). None are flagged as structurally obstructed.
2. **A reproducibility defect in `suzuki_M8000_near_rank24_feshbach.py`**, found this round: its unseeded `scipy.sparse.linalg.svds` call makes its output non-deterministic, and a direct re-run of the even-parity sector gave a result `≈4.77%` off from `v14.043`'s cited figure. A confirmatory second run (to directly test run-to-run variance under the identical unmodified code) was still executing as this entry was finalized; see §1 for the numbers in hand and the `HANDOFF` below.
3. Confirming whether the discrepancy is purely this run-to-run SVD non-determinism, or points to something else, once the confirmatory run completes.

---

HANDOFF
target: sandbox
type: audit
parent: v14.048
status: open
action: Independently audit suzuki_M8000_near_rank24_feshbach.py's reproducibility. Its scipy.sparse.linalg.svds call has no fixed v0/seed. External Audit Round 166 found: odd-v reproduces v14.043's cited combined_psd_cs_bound to ~0.08% (0.255981703317614 vs cited 0.255780876375452), but even-v differs by ~4.77% (0.275784843776218 vs cited 0.289607180784709) on a direct re-run of the unmodified script and all its unmodified dependencies (confirmed via git log -- no commits to any of them postdate the script's own single commit). Determine whether this is pure SVD-seed non-determinism (in which case the script should be given a fixed seed or replaced with a deterministic truncated SVD before any future use as a certificate input) or indicates a deeper issue. Note for context: both the cited and the newly-observed even-v value remain well inside the b_nn<=0.31 public cap either way, so this does not currently overturn the gamma_E=1 conclusion, but the non-determinism itself should not stand uninvestigated in a script feeding a numerical certificate.
deliverable: theorem-or-obstruction
constraints: Do not silently alter the script's output or hardcoded midpoints in v14.043; report whichever root cause is found.

---

## 5. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: Round 165 keeps } v14.045\text{; Lane A's handoff entry renumbered to } v14.046\\
&\text{(again correctly pre-anticipated by Sandbox's own response). } v14.046\text{'s Cauchy-Schwarz}\\
&\text{application of } \gamma_E=1 \text{ and } v14.047\text{'s acceptance-inequality arithmetic both independently}\\
&\text{verified exactly, including a cross-check of the } \gamma_E\text{-dependence against } v14.022\text{'s old}\\
&0.1\text{-placeholder figure, and cross-references to this thread's own Round 155/156/159/160 numbers.}\\[4pt]
&\text{Directly answering Round 165's own flagged gap: this thread executed Lane A's } N8000 \text{ interval}\\
&\text{certificate script directly and reproduced its floor values exactly, digit for digit — a genuine}\\
&\text{code-level independent verification, not merely a re-check of stated arithmetic.}\\[4pt]
&\text{Running the deeper rank-24 Feshbach midpoint script directly found a genuine, reportable}\\
&\text{discrepancy: odd parity reproduces to } 0.08\%\text{, but even parity differs from } v14.043\text{'s cited}\\
&\text{figure by } \approx\!4.77\%\text{, most likely an unseeded-SVD non-determinism in the script itself —}\\
&\text{flagged to Sandbox via } \text{HANDOFF}\text{ rather than silently patched. Does not currently overturn}\\
&\gamma_E=1\text{ (both values clear the downstream public cap), but the script's reproducibility needs fixing.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
