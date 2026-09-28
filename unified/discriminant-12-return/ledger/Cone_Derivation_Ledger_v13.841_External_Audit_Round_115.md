# Cone Derivation Ledger v13.841 — External Audit Round 115

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: three items since Round 114's push. (1) v13.838's post-audit corrections (commit `3ddf03c`) — both Round 114 findings addressed. (2) Lane A's widening of the `suzuki_tail_P4_block_energy_refinement.py` caps in response to Round 113's thin-margin finding (commit `795975c`). (3) v13.840, the sandbox's second Bucket 2 contribution — a kink-faithful distributional realization of `T_a`, numerically determined boundary ratios, and a reported clean failure of the v13.773 edge criteria.

Verdict: **(1) and (2) confirmed. (3): PASS on every independently checkable claim — citation fidelity, the analytic jump-structure derivation, internal arithmetic consistency, and appropriate epistemic hedging. The core numerical results (the specific ratio values and growth rates) could not be independently re-executed, exactly as in Round 114, and the entry does not ask that they be treated as more than [N].**

## 1. v13.838 corrections — both addressed correctly

Diffed `3ddf03c` directly. Finding 1 (the `D̄` vs. `\bar{e}` quote) is now transcribed correctly, matching what I read from the PDF myself in Round 114. Finding 2 (the "confirms v13.773 §5 verbatim" overstatement) is reworded to "supports the diagnosis... by an independent numerical route," which is the accurate characterization. Both fixes are precise, minimal, and don't touch anything beyond what I flagged.

## 2. Lane A cap-widening — confirmed working

Diffed `795975c`: all four caps in `suzuki_tail_P4_block_energy_refinement.py` widened by 5–7%. Re-ran the script directly: still PASS, same underlying computed values as Round 113 (the numerics didn't change, only the fail-closed thresholds), now with real headroom instead of the sub-0.1% margins I flagged (e.g. even-v energy residual `0.0054187` against the new cap `0.0058`, ~7% headroom, versus the old `0.00542`, ~0.02%). This is exactly the fix I recommended. One small housekeeping note for a future entry: v13.835's own boxed prose still shows the old tight cap values (`0.00542`, `0.0544`, etc.) — cosmetically stale now that the script is more conservative, though the actual proven bounds are unaffected either way.

## 3. v13.840 — distributional `T_a`, numerical ratios, edge-criteria failure

Same audit posture as Round 114: the scripts live outside this repo (`~/workspace/d12/lane_b/sandbox/runs/...`), so I cannot re-execute the FEM/Galerkin computation the way I re-run Bucket 3's committed scripts. What follows is everything I *could* independently check.

**Weak-form construction, checked conceptually.** `T_a = A_a` at `λ=0`, and the claim `a(u,v)=∫∫g(x-y)u'(y)v'(x)dydx = ⟨T_a u,v⟩` for `u,v∈H^1_0(-a,a)` via integration by parts is the standard Friedrichs-extension weak formulation — a legitimate, textbook way to realize a positive symmetric operator's self-adjoint extension numerically. This is the right tool for the job *provided* the form domain is actually `H^1_0`, which is precisely the caveat the entry itself raises as Horn A (see below) rather than glossing over.

**The even-extension jump claim, verified by hand.** §1 claims the jump of `g'` at `t=-log m` equals the jump at `t=+log m` (both `+c_m`, not `∓c_m`). I checked this analytically rather than trusting the sandbox's numerical check: since `g` is even (established fact from this ledger's own earlier work, e.g. v13.735/753), `g'` is odd, so `g'(-t)=-g'(t)`. The jump of `g'` at `-log m` is `g'(-log m+ε)-g'(-log m-ε) = -g'(\log m-ε)-(-g'(\log m+ε)) = g'(\log m+ε)-g'(\log m-ε)`, which is *exactly* the jump at `+log m` — not its negative. The sandbox's claim is correct, and it's a genuine (if short) derivation from evenness, not an assumption; their independent `9.3×10⁻¹⁰}`-level numerical check is consistent with what the algebra requires.

**The `λ_a`/invertibility citation, checked against the primary source.** The entry says Suzuki proves `T_a` invertible only for `λ<λ_a`, sign of `λ_a` unknown (their Lemma 6.2 reference). I pulled page 21 of the PDF directly: "Since `λ<λ_a`, the operator `T_a` is invertible on `L²(-a,a)`" is the exact hypothesis used right before Lemma 6.2 is stated, and nothing on that page (or the lemma itself, which only asserts deficiency indices `(1,1)`) establishes the sign of `λ_a`. The citation is accurate, and it correctly identifies that the sandbox's `λ=0` computation is *not* unconditionally justified by Suzuki's own invertibility lemma — it's contingent on `λ_a>0`, which is exactly the positivity-flavored open question this ledger has circled since the Bucket 1/2 split in v13.833.

**The "`Dom(A_a)` larger than `H^1_0`, containing constants" citation — traced to my own prior finding.** This is the load-bearing fact behind Horn A. I checked where it comes from: it's not fabricated — it's exactly what I verified directly against the PDF myself in **Round 101** (v13.796 §1): "`𝔇(A_a) ⊋ 𝔇(B_a) = H_0^1(-a,a)`, containing constants (page 3–4)." The sandbox entry cites this correctly and draws the right consequence from it: since constants aren't in `H^1_0`, an `H^1_0`-Galerkin weak solution is solving a strictly more constrained (Dirichlet) problem than `A_a` actually is, so the computed ratios are not automatically Suzuki's true `v_±` ratios. This is a real, well-grounded caveat, not a hedge inserted for cover.

**Internal arithmetic, spot-checked.** Recomputed the normalized columns of the §3 table myself from the raw `r_1^+,r_0^+` values rather than trusting the printed ratios: at `A=6`, `-193.092/e^6 = -193.092/403.429 = -0.4786` (table: `-0.479`, matches); `1147.834/(6·403.429) = 0.4742` (table: `0.474`, matches). At `A=5`: `-69.464/e^5=-69.464/148.413=-0.4681` (table: `-0.468`); `354.154/(5·148.413)=0.4773` (table: `0.477`). All checked entries are internally consistent — the table wasn't assembled with a transcription slip between the raw and normalized columns, whatever one makes of the underlying FEM computation itself.

**Validation-gate methodology.** The self-consistency gate (checking the FEM solution of (8.4) also satisfies (8.5) mod affine, independently derivable identities) is a sound falsifiability design, and the entry discloses that it did its job once already — catching and discarding a run with a misread `z`-convention before the reported results. That kind of disclosed near-miss is a good sign for the numerics' trustworthiness even though I can't rerun them myself.

**Appropriately scoped throughout.** The `λ=-1` spot-check is disclosed as invalid (an unimplemented `N(x,y)` term) rather than silently dropped or misreported as a negative result. The entry picks neither horn of its own fork, correctly notes the failure is about a form-domain/invertibility question this ledger already knows is open, and explicitly doesn't touch Bucket 1 or Bucket 3.

## 4. What I could not verify

The specific numerical outputs — `r_1^+≈-8.75`, `r_0^+≈+27.28` at `A=3`, the `O(N^{-2.3})` convergence rate of the validation gate, the Richardson extrapolation, and the raw growth-rate table's underlying FEM solve — rest on scripts not committed to this repo. I have not run them and am not asserting they're correct in the way I assert for a Bucket 3 result I've re-executed myself. The entry's own `[N]`, not `[N-cert]`, tagging is the right classification, and this round's PASS should be read as "every independently checkable claim holds," not "the numerics are certified."

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{Confirmed: both Round 114 corrections to v13.838 are accurate, and Lane A's cap-widening in response to Round 113 works as intended.} \textbf{v13.840: every independently checkable claim (the evenness-derived jump structure, the } \lambda_a\textbf{/invertibility citation, the } \mathrm{Dom}(A_a)\supsetneq H^1_0\textbf{ citation — traced to my own Round 101 finding — and the table's internal arithmetic) holds. The core FEM numerics remain sandbox-side and unverified by this audit, honestly tagged [N] throughout. Bucket 2's fork (wrong object vs. wrong test) is real and well-posed, not yet resolved.}}
\]
