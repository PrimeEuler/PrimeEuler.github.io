# Cone Derivation Ledger v13.601 — External Audit Round 63

## Scope

Independent audit of everything committed since my last push (`03be361`, the parabola synthesis note): the off-resonant magnetic-driver binomial transfer law, and a general equal-spin theorem for the quantum-tetrahedron kernel/D8 structure covering *every* spin `j` at once. One version collision found and fixed (the user correctly flagged it — my own synthesis note and a new arrival both landed at v13.598). Every load-bearing claim in both entries independently re-derived or tested against fresh reconstructions, including cases neither entry itself checked. No errors found. This round contains the strongest generalization result in the tetrahedron thread to date.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.598_Off-Resonant_Magnetic-Driver_Binomial_Transfer.md` (commit `0d4053e`, 2026-09-19 19:34:15 -0400 = 23:34:15 UTC) collided with my own `Cone_Derivation_Ledger_v13.598_Synthesis_The_Parabola_Through_Three_Levels.md` (commit `03be361`, 21:33:50 UTC — earlier). Per the standing timestamp rule, the later file is renumbered regardless of which side of the audit relationship it came from; renumbered it to **v13.600** (v13.599 was independently taken in the interim by the tetrahedron theorem below) and fixed its two inbound cross-references in that entry. The tetrahedron-theorem entry itself correctly detected the collision in real time and sensibly advanced past it to v13.599 without trying to resolve it — the right call, since resolving numbering collisions is this audit's job, not something either parallel thread should have to referee mid-write.

## 2. v13.600 (ex-v13.598, off-resonant magnetic-driver binomial transfer law) — verified exactly, including untested cases

This extends v13.595/Round-62's resonant multiplet work to arbitrary detuning: it derives the exact tilted-propagator formula for `H_r=-ΔJ_z-γB_1J_x` and shows that, starting from the lowest-weight state, the full population distribution over a spin-`j` multiplet is **exactly binomial**, `P_{-j→-j+r}=\binom{2j}{r}p(t)^r(1-p(t))^{2j-r}`, with `p(t)=\frac{g^2}{Δ^2+g^2}\sin^2(\frac{t}{2}\sqrt{Δ^2+g^2})` — a clean consequence of the spin-`j` representation being the symmetric power of the fundamental spinor.

- **Exact propagator.** Independently verified the spin-1/2 propagator `U_{1/2}(t)=cI+ia(σ_x)s+ida(σ_z)s`-type closed form symbolically solves the Schrödinger equation `i\,dU/dt=HU` with `U(0)=I` exactly (sympy, exact zero residual) — a complete proof the formula is correct, not just plausible.
- **Binomial law, tested beyond the entry's own scope.** The entry verified its binomial formula against direct matrix exponentiation only for `j=1,3/2` at two specific detuning points. I independently checked it via `scipy.linalg.expm` at **four different test points** (including one at Δ=0 and one with negative coupling) for **`j=1/2,1,3/2,5/2`** — `j=5/2` was not checked in the entry at all. All discrepancies were at binary64 roundoff (`~10⁻¹⁶`), confirming the general law holds well beyond what was explicitly audited.
- **Resonance limit.** Confirmed the Δ→0 limit of the binomial formula exactly reproduces v13.595's resonant probability formulas (already independently verified in Round 62) — this was implicit in my Δ=0 test point above.

The entry's guardrails are correct: it's explicit that `p(t)` is a representation-level parameter inherited from the fundamental spinor, not evidence of independent Bernoulli edge transitions, and it correctly separates the circular-drive exact result from the (harder, RWA-requiring) linearly-polarized case it proposes as the next gate.

## 3. v13.599 (general equal-spin tetrahedron kernel parity and D8 decomposition theorem) — verified exactly, including two new spins beyond the entry's own checks

This is a genuine generalization, not a restatement: it gives a closed-form formula for the tetrahedron volume operator's tridiagonal entries `a_k=k²[(2j+1)²-k²]/(4√(4k²-1))` for arbitrary spin `j`, proves `dim ker Q_j = 1` for integer `j` and `0` for half-integer `j` via a clean bipartite-parity/rank argument, and proves the nonzero-volume sector always decomposes into `⌊j+1/2⌋` orthogonal standard D8 planes — unifying v13.591, v13.593, and v13.596 (`j=1/2,1,3/2`) into one theorem.

I treated the `a_k` formula, correctly flagged by the entry itself as "already low-spin-validated" rather than derived from first principles here, as the thing most worth stress-testing:

- **Formula reproduces all three previously-audited matrices exactly** (symbolic, `j=1/2,1,3/2`) — confirms consistency with prior work, but this alone doesn't validate the generalization.
- **The real test: `j=2` and `j=5/2`, never checked anywhere in this thread before.** I built the full four-spin tensor-product construction from raw spin matrices (same method as Rounds 60–62), independently found the `J=0` invariant subspace has dimension exactly `5` (`j=2`) and `6` (`j=5/2`) as predicted, projected the independently-built oriented-volume operator onto each, and compared its eigenvalues against the closed-form `a_k` formula's predicted tridiagonal matrix. **Match to `~10⁻¹⁴`** in both cases — genuine confirmation the formula is correct at spins it was never fit to, not just an internally-consistent guess. Kernel dimension came out `1` at `j=2` and `0` at `j=5/2`, exactly as the theorem predicts.
- **Positivity lemma (`a_k>0` for all valid `k`), the load-bearing fact the whole kernel-rank argument depends on**: verified this symbolically in general, not just by example — `(2j+1)²-k²≥(2j+1)²-(2j)²=4j+1>0` for `1≤k≤2j`, and `4k²-1>0` for `k≥1`, so `a_k>0` unconditionally. Confirmed by direct symbolic computation.
- **Kernel-rank counting** (bidiagonal `B` is square with nonzero diagonal for half-integer `j` → full rank → trivial kernel; rectangular `(n+1)×n` with full column rank for integer `j` → 1-dimensional kernel) is straightforward, correct linear algebra given the positivity lemma.
- **D8 spectral-flattening construction** (`R_j=-i\,\mathrm{sgn}(Q_j)`, `R_j²=-I`, `HR_jH=R_j^{-1}`) is the same functional-calculus argument independently verified for the `j=3/2` special case in Round 61, now applied abstractly — valid given the eigenvalue-pairing/anticommutation facts, which follow directly from `H` being a parity operator on a bipartite tridiagonal matrix.

This is careful work: it explicitly separates what only needs generic weighted-path bipartiteness (the kernel-parity argument) from what needs the specific tetrahedral coefficients (the actual volume spectrum), explicitly notes the raw `Q_j` is not the D8 generator except in the coincidental single-magnitude case, and explicitly declines to claim any operator equality with the magnetic-driver path despite both being connected SU(2) weighted paths — the same discipline held throughout this entire lane.

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.600 (ex-v13.598, off-resonant binomial transfer) | Verified exactly — propagator formula proven via the Schrödinger equation; binomial law confirmed at 4 independent test points for j=1/2 through 5/2 (j=5/2 untested by the entry itself) |
| v13.599 (general equal-spin tetrahedron theorem) | Verified exactly — closed-form `a_k` formula independently confirmed correct at j=2 and j=5/2 via fresh tensor-product reconstruction (never checked before), positivity lemma proven in general, kernel-dimension pattern confirmed at the new spins |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. Both entries correctly keep the magnetic-driver and quantum-tetrahedron lanes coordinated but logically separate, and v13.599 in particular turns three individually-checked special cases into a genuinely general, independently-stress-tested theorem.
