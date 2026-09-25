# Cone Derivation Ledger v13.808 — External Audit Round 103

Date: 2026-09-25

Auditor: External audit thread (Claude, independent instance).

Scope: v13.803 through v13.807 (5 entries) — a V4/unit-core test on the compact resonance cluster, an endpoint-pencil inertia gate with analytic remote-tail floors, an anisotropic interface test deciding to reuse the M=3999 structured machinery, a fresh M=3999/4000 midpoint effective-core computation, and a frozen six-direction remote residual-Gram replay.

Verdict: **No mathematical errors found anywhere I could independently verify — including after fixing bugs in the code.** But this round's headline finding is not mathematical: **4 of the 6 new research scripts in this batch fail to run as committed**, due to trivial-but-real signature/import bugs. Three were fixable with a one-line correction and, once fixed, reproduced every claimed number exactly. The fourth — the script computing the batch's single largest numerical claim (the two-million-mode remote residual Gram matrices in v13.807) — has a non-trivial `ImportError` I did not attempt to patch, per the standing rule against silently repairing another thread's code to manufacture a passing result. That specific claim is therefore **unverified this round**, not confirmed.

## 0. Acknowledgment of Round 102 fixes

Before this batch, the source thread corrected both findings from Round 102: v13.798's relative-agreement figure now reads `9.06×10⁻⁵⁶`/`9.15×10⁻⁵⁸` (matching what I independently computed), and v13.798–800 have restored LaTeX. Confirmed by direct inspection (`grep -c '\boxed'` on all three files, and reading the corrected figure inline). Good response.

## 1. v13.803 — V4/unit-core test: fully verified, script runs clean

I ran `suzuki_form_core_v4_unit_core_resonance_diagnostic.py`'s `report(cutoff=96, dps=55)` directly (after installing `scipy`). Every number — class-projection fractions (9.45%/6.63%), generalized eigenvalues, Hadamard off-diagonal fractions, all nine leakage/commutator figures across both parity sectors — **matched exactly**. This entry correctly tests and rejects the tempting "four resonances = four `U(12)` character channels" hypothesis on real evidence rather than forcing the pattern, and repurposes the class-average structure as a finite conditioning device instead. Good, honest work, and the one script in this batch (besides v13.807's hash-verifier) that ran without modification.

## 2. v13.804 — endpoint-pencil inertia: math confirmed, script broken as committed

Running `suzuki_endpoint_v4_inertia_certificate_diagnostic.py`'s `report()` crashes immediately: `ns, A_mp = parity_components(max_mode, sector)` tries to unpack 2 values from a function (imported from `suzuki_form_core_bulk_subtracted_resonance.py`) that returns 6 (`ns, cusp, prime, arch, pole, full`). The analytic tail-floor portion of the report (computed before that line) does run and matches the entry's `γ_{0.10,±}(257)`, `γ_{0.10,±}(401)` etc. exactly. After patching the one line in a scratch copy (`ns, _c,_p,_a,_pl, A_mp = parity_components(...)`), the rest of the script runs and reproduces **every** claimed figure exactly: the `ind_-(F_ρ^±)=(4,0)` finite inertia table, all four `λ_min(C)` class-block values (`2.3694`/`2.2949` etc.), all `K/Cmin` ratios, all Schur-gap ratios, all `min|λ(S)|` values, and all band-cross-norm ratios.

## 3. v13.805 — anisotropic interface test: math confirmed with one minor discrepancy

`suzuki_endpoint_anisotropic_interface_diagnostic.py` imports the same broken `parity_components` call pattern and fails the same way. After the identical one-line patch, it ran (this one took several minutes — dense `mpmath` matrices through mode 1023) and reproduced:
- N_R=257 even-v: `raw δ_crit_band=0.53335369663667`, `V4 δ_crit_band=0.49139260558858` — **matches** the entry's `≈0.533354`/`≈0.491393` exactly.
- N_R=257 odd-v: `raw=0.20373590...`, `V4=0.17421430...` — **matches** `≈0.203736`/`≈0.174214` exactly.

**Minor discrepancy found**: at N_R=401 even-v, the script gives `V4 δ_crit_band = 0.6323059367503225`, but the entry claims `≈0.632637` — a difference in the 4th significant figure (~0.05% relative). This propagates into the "remaining room" figure: script implies `0.678827-0.632306≈0.04652`, versus the entry's stated `≈0.04619`. This is far smaller than Round 102's finding and **does not change the qualitative conclusion** (N_R=401 is tight either way, and the entry's own decision to move to M=3999 stands regardless) — but the specific figure should be corrected.

## 4. v13.806 — fresh M=3999/4000 midpoint cores: math confirmed, different script bug

`suzuki_endpoint_M3999_midpoint_effective_core.py`'s `report()` calls `effective_core(core, buffer_)`, but `effective_core` requires a third `sector` argument (available as a loop variable but not passed) — `TypeError: missing 1 required positional argument`. This one uses plain `numpy`/binary64 (not `mpmath`), so after the one-line fix it ran in seconds and reproduced **every** figure exactly: both pole-free buffer minimum pivots (`0.46608173927253421` at mode 29 even-v; `0.51112941830003888` at mode 40 odd-v), both Woodbury denominators, all twenty effective-core eigenvalues, and `inertia(S_±)=(4,0,6)` in both parity sectors.

## 5. v13.807 — frozen six-direction inputs and remote Gram: partially verified, one claim unverified

`suzuki_endpoint_M3999_frozen_six_direction_inputs.py` **ran correctly as committed**, no fix needed, and independently confirmed both SHA-256 payload hashes (`af158c4f...`, `c983603a...`), both determinant diagnostics, and both Gram-orthonormality figures exactly.

`suzuki_endpoint_M3999_frozen_six_direction_remote_gram.py` — the script that computes the batch's most substantial new numerical claim, the two `6×6` normalized residual Gram matrices accumulated through two million modes (`H_{e,2M}`, `H_{o,2M}`, their eigenvalues, the far-tail envelope bounds, and the "dominant direction is the `1/n` channel" alignment figures in §4) — **fails to import**: `ImportError: cannot import name 'structured_ldl_solve' from suzuki_endpoint_M3999_midpoint_effective_core`. That module (which I read directly) defines separate `structured_ldl` and `ldl_solve` functions, not a combined `structured_ldl_solve`. Unlike the three bugs above, this is not an unambiguous one-line fix — reconstructing the intended combined call would mean writing new code on the source thread's behalf, which the standing audit rule (never silently patch another thread's work to manufacture a passing result) rules out. **I am therefore not able to confirm or deny the correctness of v13.807's Gram-matrix numbers this round; they should be treated as unverified, not as passed.**

## 6. Assessment: is this the M16001 pattern again?

The user asked earlier in this session whether Lane A's growing Feshbach/protected-subspace machinery was heading toward a repeat of the old, sprawling `M16001` numerical-certificate program. This round gives a concrete, relevant data point: this is now the second consecutive audited batch (after Round 102's LaTeX corruption and precision-figure error) where committed "reproducible" research artifacts did not actually run cleanly — and this time the ratio is worse (4 of 6 broken, one not fixable without rewriting code). The mathematics itself has held up in every case I could check, including after fixing bugs — so this is not (yet) a correctness crisis. But it is exactly the kind of erosion in commit hygiene that, left unaddressed, is how a pile of stale, unverifiable "certificate" scripts accumulates. Recommend the source thread run each new research-notes script once, end-to-end, before committing it — not just execute the underlying computation interactively and then write a separate, untested `report()`/`main()` wrapper for the commit.

## Self-audit note

No error of my own found this round. Where I patched a script to continue verification, I did so only for unambiguous, single-line signature/unpacking mismatches with exactly one sensible fix, and I verified the result rather than assuming it — consistent with, not in tension with, the standing rule against silently manufacturing passing results.

## Result

\[
\boxed{\textbf{PASS (math): v13.803–806 fully confirmed; v13.807's frozen-input hashes confirmed. UNVERIFIED: v13.807's remote-Gram numbers (import bug, not independently fixable). FLAG: 4/6 new scripts broken as committed; one minor (~0.05\%) numerical discrepancy in v13.805.}}
\]

Requested from the source thread: (1) fix the `structured_ldl_solve` import in `suzuki_endpoint_M3999_frozen_six_direction_remote_gram.py` and re-report the `H_{e,2M}`/`H_{o,2M}` figures so they can be independently checked; (2) fix the `parity_components` unpacking in `suzuki_endpoint_v4_inertia_certificate_diagnostic.py` and `suzuki_endpoint_anisotropic_interface_diagnostic.py`, and the missing `sector` argument in `suzuki_endpoint_M3999_midpoint_effective_core.py`; (3) recheck the N_R=401 even-v `δ_crit,V4` figure in v13.805 against the script's own output (`0.632306` vs. the stated `0.632637`).
