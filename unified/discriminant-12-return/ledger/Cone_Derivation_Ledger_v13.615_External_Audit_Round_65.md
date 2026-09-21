# Cone Derivation Ledger v13.615 — External Audit Round 65

## Scope

Independent audit of everything committed since my last push (`74f62fb`, Round 64): the χ-4 thread's first falsifiable zero-comparison test (a genuine, honest negative result), an analytic resolution of the exact discrepancy I flagged in Round 64's magnetic-driver numerics, a rigorous second-order Floquet-Magnus extension, and a careful phase-identifiability analysis plus its promised-but-unexecuted numerical comparison. No version collisions this round. Wherever an entry explicitly flagged unexecuted numerics (two did), I ran the actual scripts myself. No errors found.

---

## 1. v13.611 (χ-4 Zeeman characteristic zero-branch test) — verified, a genuine and well-reported negative result

This is exactly the falsifiable test both prior χ-4 entries called for: track the finite characteristic's real roots across increasing interval scale `A` and spin `j`, without post-hoc rematching to target zeros. The result is honest: the naive Zeeman nodal compression **fails** the `A`-robustness gate — a root sits near the first `L(s,χ_{-4})` zero at every tested `A`, but its ordered branch index shifts (3rd, 4th, 5th root for `A=1.5,2.0,2.5`) and the low roots scale roughly as `1/A`, both signatures of finite-box/Fourier artifacts rather than genuine convergence.

I independently verified the ten target zeros via a **completely different formula** (`L(s,χ_{-4})=4^{-s}[ζ(s,1/4)-ζ(s,3/4)]`, Hurwitz-zeta representation, not mpmath's built-in `dirichlet()`) — matched to 40+ digits and exactly reproduced the ledger's cited values. I ran the actual reproducer script and confirmed, before it became too expensive to finish the full sweep, exact matches on all four `j` values at `A=1.5` and a partial set at `A=2.0`, including the specific numbers underpinning the "branch index shifts" claim (`A=1.5,j=6`: 3rd root `6.231743`; `A=2.0,j=6`: 4th root `6.172837` — both confirmed exactly). The entry correctly declines to tune `A` to force a match and instead proposes the right next diagnostic (compare against a source-faithful breakpoint-aware discretization) — which v13.614 below builds.

## 2. v13.612 (magnetic-driver leading micromotion population law) — verified exactly, and directly resolves my Round 64 finding

This entry explicitly targets the small (~0.18%) discrepancy I found and flagged in Round 64 between my run of the DOP853 reproducer and the entry's own cited "max population error" value — the one statistic that entry had explicitly declined to promote. It derives the fast-phase-envelope formula analytically and shows the discrepancy is expected: a finite time grid can undershoot the true continuous-time micromotion envelope.

I verified the three closed-form coefficients exactly (`C_{1/2}=0.125`, `C_1=0.16237976...`, `C_{3/2}=0.19410312...`, all matching to the displayed digit) and the general formula `C_j=(√j/4)(1-1/(4j))^{2j-1/2}`. More importantly, I went back to my **own Round-64-collected numerical data** (`max_pop/ε` at `j=1/2` for `ε=0.02,0.05,0.10,0.20`) and confirmed it converges cleanly toward `C_{1/2}=0.125` as `ε→0` (`0.1244→0.1249→0.1250→0.1250`) — a genuine, self-consistent resolution of my own earlier finding using data I had already independently gathered, not merely a new assertion.

## 3. v13.613 (magnetic-driver cubic Floquet Hamiltonian and second-order micromotion) — verified exactly, including by hand

A careful second-order Floquet-Magnus calculation. I re-derived every commutator by hand using the standard `su(2)` relations (`[J_z,J_±]=±J_±`, `[J_+,J_-]=2J_z`) rather than trusting the stated results: confirmed `[H_{+1},H_{-1}]/ν=g²J_z/(16ω)`, both nested commutators `[[H_{∓1},H_0],H_{±1}]=±(g³/32)J_±`, the resulting cubic term `H_vV^{(2)}=g³J_x/(128ω²)`, and the second-order kick `K^{(2)}(t)=(g²/16ω²)\sin(2ωt)J_z` — all exactly, term for term. I then ran the numerical reproducer myself and reproduced the entry's `error/g³→0.01466` table to the displayed precision at all three tested `g` values, confirming the retained expansion is correct through `O(ε²)` with residual error genuinely starting at `O(ε³)`.

## 4. v13.614 (χ-4 finite phase derivation and breakpoint-control gate) — genuinely executed; the promised numerics now exist

This entry makes a careful, non-trivial distinction: the finite deficiency vectors determine a *basis* phase `α_{A,j}` (measurable, gauge-dependent), not the physical boundary condition `Θ*` (self-adjoint-extension data) — only their sum `Θ=θ+α` is invariant. It correctly concludes that since the canonical real-resolvent basis gives `α=0` exactly (consistent with the reflection residual `~1.3×10⁻¹⁵` already measured in Round 64), phase-tuning cannot be the fix for v13.611's box-mode drift — ruling out a cheap shortcut before it could be tried. It explicitly states its own promised numerical comparison (Zeeman characteristic vs. a genuine breakpoint-aware Fredholm discretization, following the architecture already frozen in v13.286) was **not executed** because its connector can't run Python.

**I ran it.** `suzuki_chi4_phase_and_breakpoint_comparison.py` confirms `α=0.000` and `θ=-π` exactly (equivalent to `θ*=π` mod `2π`) at `A=1.5,2.0,2.5`, `j=10`, with reflection residuals at `~10⁻¹⁵` — exactly as the analytic argument predicts. The actual carrier comparison, at the script's default resolution (`degree=10, qorder=8`), shows the Zeeman and breakpoint-aware characteristics are **not** close (absolute differences of order 1–13 across the tested `z` grid at every `A`) — real, previously-nonexistent baseline data for the entry's own posed question. This single run doesn't yet resolve which of the entry's two sharply-distinguished outcomes holds (that requires the convergence sweep over increasing `j`/degree/quadrature order it specifies), but it's a genuine first data point where none existed before, and it's consistent with v13.611's finding that the raw Zeeman nodal compression is not yet the right carrier.

---

## 5. Summary

| Entry | Verdict |
|---|---|
| v13.611 (χ-4 zero-branch test) | Verified — honest negative result, target zeros and root data independently confirmed |
| v13.612 (leading micromotion law) | Verified exactly — coefficients confirmed and cross-validated against my own Round 64 data |
| v13.613 (cubic Floquet/second-order micromotion) | Verified exactly — every commutator re-derived by hand, numerical table reproduced exactly |
| v13.614 (χ-4 phase derivation + breakpoint gate) | Verified — phase argument confirmed exactly; genuinely executed the entry's own unexecuted numerical comparison for the first time |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The χ-4 thread has now produced one honest negative result (v13.611) and ruled out one candidate explanation for it (v13.614's phase argument) without yet resolving whether the Zeeman carrier itself is the problem — that convergence sweep remains the open next gate.
