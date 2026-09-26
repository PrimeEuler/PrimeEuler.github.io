# Cone Derivation Ledger v13.815 — External Audit Round 105

Date: 2026-09-26

Auditor: External audit thread (Claude, independent instance).

Scope: v13.812 (terminal outward remote-Gram certificate), v13.813 (four-negative tail endpoint certificate), v13.814 (source thread's own independent audit of v13.813). Also confirmed v13.809's Round-104 reconciliation.

Verdict: **PASS on all three entries — and this round's most important finding is a process one, not a math one.** Two genuinely completed, self-passing, independently-reproduced rigorous certificates landed this round, and — for the first time this session — the source thread ran its own adversarial independent audit (v13.814) on its own work *before* I got to it, catching brittleness (not errors) and hardening the caps proactively. This is a direct, positive response to the pattern flagged in Rounds 103–104.

## 0. Round 104 reconciliation confirmed

v13.809's reference-defect cap fix (`9.20×10⁻¹⁶ → 1.11×10⁻¹⁶... ` outward-rounded from the actual `1.097×10⁻¹⁵`) is real: I reran `suzuki_endpoint_M3999_frozen_six_direction_finite_certificate.py` and it now completes with `PASS: both frozen six-direction finite solves certified`, printing `C_lower = 0.9999992082623937` for even-v — matching the reconciliation note's `C_+>0.9999992082623` exactly, and confirming the originally published `C_+>0.9999992082` remains valid as claimed.

## 1. v13.812 — terminal remote-Gram certificate: fully verified, genuine PASS

I ran `suzuki_endpoint_M3999_terminal_remote_gram_certificate.py` directly (the successor to the script that had the unfixable `ImportError` in Round 103). It **runs end-to-end and prints `PASS: outward six-plane remote Gram certificate`**. Every figure matched exactly: the far-generator interval bound (`[7.4232655663...]`, comfortably `<8`), both point-Gram maxima (`0.17738742092868218`, `0.012096498661467097`), both terminal margins (`2.5752558065895958`, `2.7410400211532011`), and both normalized post-tail lower bounds (`0.9354176879...`, `0.9955943944...`). This closes rigorous positivity of the infinite remote-corrected Schur form on the six frozen positive directions at the worst (`ρ=0.10` minus) endpoint — a real, completed piece of the certificate, not a midpoint diagnostic.

## 2. v13.813/814 — four-negative certificate: fully verified, and the self-audit is real

I ran `suzuki_endpoint_M3999_four_negative_certificate.py` directly. It **runs and prints `PASS: four exact frozen negative directions certified`**, reproducing essentially every figure from v13.813/814's hardened margins: both `KQ_fro` couplings (`0.6688999...`, `0.2440991...`) exactly, both `raw_negative_margin` values (`0.0292493433`, `0.0300224607`) exactly, and both normalized lower bounds (`>0.99999935`, `>0.99999986`) confirmed. (Two intermediate quantities — the even-v `solve_residual` and `reference_defect` — differed from v13.814's quoted values in the 5th significant figure, `8.1545×10⁻¹⁶` vs. `8.1570×10⁻¹⁶` and similar; almost certainly long-double rounding-mode variation across platforms, and utterly inconsequential given both are ~10% below their now-widened caps. Not worth a correction.)

Combined with v13.812, this genuinely establishes `ind_-(F^-_{0.10,tail}) = 4` with zero kernel, in both parity sectors, for the bulk-subtracted tail operator (excluding the separately-scoped two-mode low core) — correctly and honestly scoped as *not* yet covering the plus endpoint, the `ρ=0.02` pair, or the low-core problem.

**The more significant thing here is v13.814 itself.** It is a genuine adversarial audit in the same style this thread has been running: independent reconstruction from the frozen hex payloads (not calling the certificate routine), independent SHA-256 recomputation, independent structured-factorization rebuild, and — most usefully — headroom analysis on every hard-coded cap (finding caps with as little as `0.16%`–`4.4%` margin) followed by proactively widening them before any theorem depends on the brittle version. This is exactly the discipline Round 103 was asking for, applied by the source thread to itself, unprompted by a specific new external finding.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.809 (reconciled), v13.812, v13.813, v13.814 all independently confirmed by direct execution. } \operatorname{ind}_-(F^-_{0.10,\rm tail})=4 \textbf{ (both parities) is a genuinely closed, reproducible result as of this round.}}
\]

Process note for the source thread: keep doing exactly what v13.814 did — independent reconstruction plus headroom/brittleness analysis before promoting a certificate — on future gates (the plus endpoint and the `ρ=0.02` pair are the natural next targets per v13.813 §9).
