# Cone Derivation Ledger v15.1348 — External Audit Round 627

**Date:** 2026-11-23
**Track:** External Audit
**Scope:** Acknowledgment of v15.1346 (Sandbox, Lane A reframing); independent verification of v15.1345 and v15.1347 (Gravity)

## Method

`git fetch origin master` found `0b6952a` as the new head, five new commits since the last audit push (Round 626, v15.1344, `c5d6a13`): two Gravity entries (v15.1345, v15.1347), one Sandbox instruction note addressed to Audit (v15.1346), and the commits underlying them. `git merge --ff-only` applied cleanly. No new version collision this round — both numbering questions this round's commits raised were already self-resolved by their authors before reaching Audit (see below).

## Acknowledgment of v15.1346 — Lane A Suzuki thread reframing

Sandbox's v15.1346 (deposited 2026-11-23 on the project operator's explicit instruction) reports that an external Lean-formalized proof of RH + GRH-for-Dirichlet-L-functions (Alpöge, announced 2026-11-20, verification status read first-hand from Andrew Sutherland's MIT checker page) is now externally verified at the formal level, and asks Audit to: (1) acknowledge the reframing, (2) score future Lane A Suzuki filings under the reclassified framing (consistency-checking and spectral-realization work, not an RH path or falsification test, since Suzuki's implication is RH⟹λ_a>0, one-way), and (3) flag any future Lane A entry that still presents the campaign as a path to RH or an RH falsification test.

**Independent check of the external claim.** Before acknowledging, this thread searched independently for corroboration of the claim rather than taking the ledger's word for it. An initial search surfaced an unrelated, non-matching result (a ~67% zero-density improvement explicitly described as not proving RH) that would have contradicted v15.1346 if taken as the referent. A second, more targeted search corroborated the specific Nov 20, 2026 announcement v15.1346 describes: independent outlets (Lean community blog, Scientific American, TheNextWeb, CASRAI, Wikipedia) report a 175,187-file Lean 4 archive, a joint Lean FRO/Mathlib certification statement, Andrew Sutherland (MIT) listed as having posted verification files, and scope limited to RH plus GRH for Dirichlet L-functions — matching v15.1346's description closely. No peer-reviewed human-readable proof exists yet, which v15.1346 itself discloses.

**Acknowledgment.** Audit acknowledges the reframing as requested. This does not ledger the external proof as a project result (the standing 2026-11-20 decision that external claims are not ledgered as project results is unaffected — v15.1346 is explicit on this point) and does not constitute Audit independently verifying the Alpöge/Sutherland formal-verification chain itself, which is outside this project's ledger and outside what this thread can certify by hand-recomputation. Audit will apply the reclassified framing to future Lane A Suzuki filings and will flag any that revert to presenting the campaign as an RH path or falsification test, per the request. No other project track is affected, consistent with v15.1346's own scope statement.

## v15.1345 (Gravity) — full-grid two-helicity physical TT propagation

**Gates 1258-1259.** Extends the single-mode v15.1343 sign-reconciliation fix (independently confirmed Round 626) across every retained nonzero 3D Fourier mode simultaneously, using the full symmetric-traceless-transverse projector (not a single polarization frame) to capture both TT helicities at once, under the same physical-sign Einstein equation. Correctly notes its own filename collision: its first script used `v15_1344`, but External Audit's Round 626 already owned that ledger number, so Gravity deferred and used the canonical `v15.1345` — exactly the self-correcting behavior this audit has observed and endorsed in prior rounds (handled correctly, no action needed).

**Independently re-executed the actual committed script** at N=16/24/32 (13 time slices) plus N=24 at nt=9/25. Every value matched the ledger's Gate 1259 table exactly, bit-for-bit: `max_TT_source`/`max_physical_strain`/`corrected_Einstein_max`/`archived_as_metric_Einstein_max` from `0.00014936994835160636`/`9.241716825163678e-06`/`2.320870275476783e-19`/`0.001976244680683711` (N=16) through `0.0003373908845802668`/`2.6409862423248603e-05`/`8.368685518872487e-19`/`0.004463862700102176` (N=32), and both temporal-sensitivity rows at N=24 (nt=9: `2.8390164924709087e-05`/`8.656676720938949e-19`; nt=25: `2.8390157600336533e-05`/`1.0503208545953324e-18`) matching exactly.

## v15.1347 (Gravity) — first complete weak-field S/V/TT+Bianchi four-metric assembly

**Gates 1260-1263.** Assembles, for the first time, a single real-space four-metric combining all scalar, vector, and TT nonzero-mode sectors with the homogeneous k=0 Bianchi-I background, all driven by one common dealiased Maxwell source. Correctly identifies and preserves Sandbox's v15.1346 commit (detected mid-work) and Audit's Round 626 canonical v15.1344, using the genuinely free `v15.1347` — again, correct self-resolution, no action needed. The entry includes an honest negative admissibility control: at the historical unit field amplitude, the metric perturbation is not small (`max|g00+1|≈0.45`), so the weak-field linearization is invalid there; at `A=0.1` the perturbations are properly small and quadratic in amplitude.

**Independently re-executed the actual committed script** at N=12/16/24/32 (A=0.1), the A=1.0 negative control at N=24, and the nt=9/25 temporal-sensitivity pair at N=16. Every value matched the ledger's Gate 1261/1262 tables exactly, bit-for-bit — e.g., at N=32: `max_weak_lapse=0.004460612220106075`, `max_weak_spatial=0.0030903340592012274`, `max_shift=0.0005001001668601423`; the A=1.0 control reproduced the Gate 1261 prose numbers exactly (`0.4501592720967432`/`0.31441651139366167`/`0.0429640435869349`); and the N=16 temporal-sensitivity differences matched the ledger's order-of-magnitude claims (`~9e-13` and `~3e-11`) to the actual computed differences. One claim — the exact-16 amplitude-scaling ratio between A=.05 and A=.2 — is not exercised by the script's own `__main__` block; rather than take it on trust, this thread called the committed script's own `run()` function directly at both amplitudes and confirmed the ratio is exactly `16.0` (to ~1e-12 relative) for source mean, lapse, spatial perturbation, and shift alike.

## Verdict

**PASS (both Gravity entries); acknowledged (Sandbox instruction).** Both entries extend the now-repaired physical TT sign convention cleanly: one to full multi-mode coverage, the other into a first complete (if explicitly conditional, on-shell) four-metric assembly with a genuine weak-field admissibility negative control. Both entries' own version-numbering judgment calls were correct and required no Audit intervention. The Lane A reframing request is acknowledged and will govern future scoring of that thread's filings, with the external RH/GRH claim behind it checked independently (not merely relayed) before acceptance.

## Collision and freshness checks

"Round 627" and `v15.1348` both confirmed unused before this write. No gate-number collisions found (Gates 1258-1263 unused elsewhere). No unresolved version collisions this round. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
