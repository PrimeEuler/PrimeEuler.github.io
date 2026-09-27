# Cone Derivation Ledger v13.829 — External Audit Round 110

Date: 2026-09-27

Auditor: External audit thread (Claude, independent instance).

Scope: v13.828 — the explicit `2×2` quadratic matrix polynomial for the numerical grouped `P4` residue, its uniform inner-window Loewner enclosure, and the resulting combined bound on the exact grouped residue.

Verdict: **PASS. Fully verified.**

## 1. Algebra checked by hand

`K(δ)=K_0-δK_1` gives `Ĝ(δ)=K(δ)^TK(δ) = K_0^TK_0 - δ(K_0^TK_1+K_1^TK_0) + δ²K_1^TK_1`, matching the claimed `G_0-δG_1+δ²G_2` decomposition exactly by direct expansion — confirmed by hand, not just accepted.

## 2. Numerics: independently recomputed from the raw `K_0`/`K_1` matrices, then cross-checked against the script

I typed the reported `K_0,e`/`K_1,e` and `K_0,o`/`K_1,o` matrices into a clean numpy session myself (not reusing any of the source thread's code) and recomputed `G_0`, `G_1`, `G_2`, then evaluated `Ĝ(δ)` and its eigenvalues at `δ=-0.02,0,+0.02` in both sectors. **Every single reported number matched exactly**: all six `G_0/G_1/G_2` matrices, all six endpoint matrices, and all six eigenvalue pairs (e.g. even-v `δ=+0.02`: eigenvalues `3.29277257534×10⁻⁸, 1.74539913531×10⁻⁴`, reproduced digit-for-digit). I also independently confirmed the claim that the `+0.02` endpoint carries the larger operator norm in both sectors (`9.870×10⁻⁵ > 6.815×10⁻⁵` odd-v, and correspondingly for even-v), which is what licenses the convexity argument in §5.

I then separately ran `suzuki_grouped_residue_numerical_evaluation.py` directly; it completes with `PASS numerical grouped-residue polynomial/enclosure` and reports `poly/direct defect = 0.0` (or `~10⁻²⁰`, floating-point noise) at every tested point — i.e. the script itself cross-checks the polynomial-evaluation shortcut against direct re-evaluation, and that internal check also passes.

## 3. Final combined bounds

The §8 corollary arithmetic (`1.75×10⁻⁴ + 0.0086 = 0.008775` even-v, `1.00×10⁻⁴ + 0.0152 = 0.0153` odd-v) is simple addition and checks out.

## 4. Scope and a genuinely useful observation

Correctly guarded (no individual-channel, simplicity, sign, or RH/GRH claim). Worth flagging as a good piece of reasoning rather than just a number: §7 notes that the certified uncertainty here (`~10⁻⁴`) is now completely dominated by the `P4`-subspace approximation error (`~10⁻²`) from v13.826, not by the numerical-center evaluation itself. That's a real, actionable diagnosis of where the next accuracy bottleneck is (tightening the `P4` subspace certificate, not refining this quadratic), and it's the kind of self-directed prioritization that's been characteristic of this program since the Round 103–105 correction.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.828 fully confirmed — independently recomputed from raw matrices by hand (exact match on all reported numbers) and separately confirmed by direct script execution.} \widehat G_e(\delta)\prec1.75\times10^{-4}I_2, \widehat G_o(\delta)\prec1.00\times10^{-4}I_2 \textbf{ uniformly on } |\delta|\le0.02\textbf{, giving the combined exact-residue bounds } G_e\prec0.008775I_2, G_o\prec0.0153I_2.}
\]
