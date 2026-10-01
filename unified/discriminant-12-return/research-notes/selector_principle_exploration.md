# Selector-Principle Exploration: the "positivity selects" heresy

**Date:** 2026-10-01 · **Track:** our Lane B (sandbox exploratory), NOT the ledger's Lane B ·
**Scope:** sandbox only — no ledger / repo / research-notes writes ·
**Status convention:** [D] derived/proved · [N] numerical (provisional until lifted claim-by-claim) ·
[I] interpretation · [O] open speculation. No RH claims anywhere in this file.

## 0. The heresy, stated precisely

Three operator fronts closed on 2026-10-01:

1. **Untwisted positivity route** (v13.896): the spring↔Suzuki positivity bridge is CLOSED in the
   full operator — indicator weights negative everywhere primes are active, and the knife-edge
   quantified (indicator captures 96% of the Λ lift yet lands negative).
2. **D̄_{a,θ} θ-hunt** (`expedition_dbar_theta.md`): rigidity — the lattice slides with θ, never
   deforms; Kim's "no θ(a)" sharpened to a no-go on deformability.
3. **Twisted channel** (`twisted_port_scope.md`): formal GO, substantive NO-GO — twisted form
   positive only for a ≲ 0.33, saturating at exactly −½log 12; fork dead end.

The heresy: **maybe no operator's eigenvalues are the zeros; instead, Weil positivity over all
admissible test functions IS the selection principle.** The zeros are not emitted by an operator
(they are not "eigenvalues"); they are *selected* — picked out, pinned down — by the requirement
that a positivity cone hold over every test function.

Disambiguation (do not confuse with the other selector): `selector_theory_derivation.md` covers the
**Guinand–Weil frequency-selection** mechanism — the spring's frequencies selected by the explicit
formula, RH-agnostic, [D]. That selector picks *frequencies of an oscillator*. This file's heresy
picks *the zero set itself*, via positivity. Different selector, different selected object.

The house creed applies verbatim: *"The cone does not force dynamics; it selects them. Show the
selection principle, or mark the dynamics 'permitted, not selected.'"* The Λ weights are
*permitted* (positivity holds, [N]); whether they are *selected* (unique, forced) is unshown. That
gap is the entire subject of this file.

## 1. Formalizations of "positivity selects" (F1–F7)

### F1. Positivity-cone boundary in weight space — the marginal geometry [N], selection gloss [O]

The concrete version. Consider the space of weight sequences c = (c_n); the screw form Q_c is
positive semidefinite on a convex cone of c's. The Λ weights c_n = Λ(n)/√n sit (numerically) on
the cone's boundary — λ₁ ≈ 0, the knife-edge. The *selection* reading: the boundary point is
distinguished; moving off it (indicator, no-prime-powers, noprime) breaks positivity. New
numerical anatomy from this exploration (§3): each prime-power kink is *individually load-bearing*
with exactly its von Mangoldt coefficient. But multicritical ≠ unique: many weight sequences could
satisfy λ₁ ≥ 0, and no uniqueness theorem is exhibited. Status: new concrete math [N]; the
selection gloss remains [O].

### F2. Li's criterion as selection [D theorem; selection reading adds nothing]

RH ⟺ λ_n ≥ 0 for all n, λ_n = Σ_ρ [1 − (1−1/ρ)^n] (Li 1997; Bombieri–Lagarias 1999). The λ_n are
explicit arithmetic numbers; one could say nonnegativity "selects" the zero multiset. But
Bombieri–Lagarias generalized the criterion to *arbitrary* multisets on Re(s) = 1/2 — it
characterizes critical-line multisets, it is not zeta-specific, and it does not select ζ's zeros
among zero multisets. It is RH restated, not a selection mechanism. [D] for the equivalence;
[I] for the assessment that the selection reading is empty here.

### F3. Variational principle over zero configurations [O — pure philosophy]

"Among all multisets {ρ}, ζ's zeros minimize some functional." No natural functional with a unique
minimizer is exhibited; any functional reverse-engineered from the answer is circular. This is the
heresy in its least disciplined form. Kept as a placeholder, not a program.

### F4. de Branges / Hermite–Biehler spaces [D space theory; RH application stalled]

A de Branges space is *defined* by positivity of its reproducing kernel (axioms A1–A3) — this is
literally "positivity selects the space," and the zeros of the structure function E lie in the
lower half-plane automatically. It is the closest existing realization of the heresy's logical
form inside complex analysis. But de Branges' own claimed RH proofs are not accepted by the
mathematical community, and our audit triage already pivoted this line to the finite-section
approach, leaving the "closest to a real operator" branch unsolved. The selection happens at the
level of the *space*; getting ζ's *specific* zeros still needs the hard step. Live functional
analysis, stalled as an RH route. [I] assessment.

### F5. Lee–Yang circle theorem — the existence proof that the heresy's *form* is real [D theorem; transfer [O]]

Lee–Yang (1952): ferromagnetic pair interaction (a *positivity* condition on the couplings) ⟹ all
zeros of the partition function lie on the unit circle. This is a genuine, proved
"positivity selects zeros" theorem — the heresy's logical shape, working, in the wild. Knauf
(1999) speculated on an RH connection. But the Lee–Yang proof uses the specific structure of the
Ising partition function (Asano contractions and the like); there is no general transfer
principle, and no route from it to ζ. Verdict: the best precedent for the heresy's *form*;
analogy only. [O] for any RH link.

### F6. de Bruijn–Newman threshold — the strongest selection-flavored theorem [D]

The heat-flow family H_t with H_0 ∝ Ξ: **de Bruijn (1950)** — ∃ finite Λ with H_t having only
real zeros ⟺ t ≥ Λ; **Newman (1976)** conjectured Λ ≥ 0; **Rodgers–Tao (2018)** proved Λ ≥ 0.
Hence RH ⟺ Λ ≤ 0 ⟺ **Λ = 0**: "RH, if true, is only barely so" (Newman). This is a genuine
SELECTION statement: among the natural deformation family {H_t}, ζ's zero set sits *exactly at
the critical threshold* — selected as the boundary case. Not eigenvalues; a threshold principle.
It is still an equivalence (proving Λ ≤ 0 is as hard as RH), but it is the most respectable
existing mathematics with the heresy's flavor: the zeros are distinguished as the marginal case
of a positivity-driven flow. [D] for the theorems; [I] for the reading.

### F7. Connes' absorption spectrum — the heresy in its most respectable clothing [I]/[O]

Connes' trace-formula program: the explicit formula as a trace formula, the zeros as an
*absorption* spectrum (missing lines) rather than emission (eigenvalues) — the sign-flipped
heresy. In this telling the selection principle IS the Weil distribution's positivity, and the
zeros are where the trace "absorbs." But this is Connes' program restated: the positivity of the
Weil distribution is exactly the missing step (Connes' own diagnosis — the analogue of the
Riemann–Roch/positivity step Weil used in function fields). The missing step is *named*, not
*supplied*. Verdict: the heresy at its most dignified; still needs the positivity proof.

### The function-field precedent — what "positivity selects" looks like when it works [D]

Weil's proof of RH for curves over 𝔽_q: positivity of the intersection pairing on C×C
(Castelnuovo–Severi / Hodge index theorem) applied to the Frobenius correspondence forces
|ω_i| = √q. This is THE paradigmatic "positivity selects zeros" theorem — a positivity principle
for a quadratic form on correspondences *selects* the zero locations. The number-field analogue
is precisely what's missing: no known positive-definite quadratic form on correspondences for
Spec ℤ (the transfer exercise in the literature reduces all blocked steps to this single
obstruction). So the heresy is not a new logical form — it is the *oldest* successful form, with
the number-field instance unproved. This is also Connes' diagnosis of his own program's missing
step. [D] for the function-field proof; [I] for the framing.

## 2. Literature verdicts (searched 2026-10-01)

| # | Claim | Verdict |
|---|-------|---------|
| F2 | Li's criterion (Li 1997; Bombieri–Lagarias 1999) | [D] equivalence; generalized to arbitrary critical-line multisets — not a zeta selection principle |
| F4 | de Branges/HB program | [D] space theory; de Branges' claimed RH proofs not accepted; line pivoted per audit triage |
| F5 | Lee–Yang circle theorem | [D] genuine "positivity selects zeros" theorem (Ising); Knauf 1999 RH speculation; no transfer |
| F6 | de Bruijn–Newman: Λ = inf{t : H_t real-rooted}; Rodgers–Tao Λ ≥ 0 | [D]; RH ⟺ Λ = 0 — the best selection-flavored theorem |
| F7 | Connes trace formula; Weil-positivity as the missing step | [D] as equivalence/diagnosis; the positivity step is the named gap |
| — | Weil function-field proof via intersection positivity | [D] the working precedent; Spec ℤ analogue blocked (Spec ℤ × Spec ℤ = Spec ℤ, dimensional mismatch) |

## 3. Experiment B: odd-sector marginal analysis of the Λ(n)/√n exactness [N]

### 3.1 Motivation

The prime-power ablation (`ablation_prime_powers.md`) found: at a = 2, |λ₁(minus_n)| = Λ(n)/√n
for n ∈ {8,9,16,25,27} (3–6 digits); n = 4 exactly √2×; n = 32 0.6% low; 49 unresolved. First-order
perturbation theory gives the wrong sign/magnitude. Mechanism open [O]. This pilot probes the
marginal geometry: is each minus_m ground state w_m a near-null direction of the FULL form, held
up by exactly its kink?

### 3.2 Setup

Sector-decomposed P1 FEM at a = 2, N = 1600 (script `/tmp/odd_sector_pilot.py`, 86 s runtime).
Q_full = G₂ − Σ_n Q^(n) (prime-power kink kernels, coefficients c_n = Λ(n)/√n);
Q_minus_m = Q_full + Q^(m) (kink m removed). Even/odd sectors solved separately via eigsh 'SA'.
Tests: A — odd vs even λ₁(minus_m) and the exactness ratio; B — overlaps ⟨w_m|w_₉⟩_M;
C — stripped-kink Rayleigh quotients K_n[w₉]/M; D — Q_full[w₉]/M (near-null test);
E — first-order sensitivities s_n = v_eᵀQ^(n)v_e/M on the full even ground state.

### 3.3 Results [N]

**Test A — exactness reproduced at higher resolution; parity NOT specialized.**

| m | λ₁ odd | λ₁ even | −c_m = −Λ(m)/√m | ratio |
|---|--------|---------|-----------------|-------|
| 4 | −0.490128 | −0.490129 | −0.346574 | **1.414210 = √2** (6 digits) |
| 8 | −0.245064 | −0.245064 | −0.245065 | 1.000000 |
| 9 | −0.366204 | −0.366204 | −0.366204 | 1.000000 |
| 16 | −0.173286 | −0.173285 | −0.173287 | 0.999998 |
| 25 | −0.321868 | −0.320305 | −0.321888 | 0.999938 |
| 27 | −0.211419 | −0.210425 | −0.211428 | 0.999956 |
| 32 | −0.121807 | −0.113072 | −0.122532 | 0.994078 |

Full form: λ₁ = 0.000000 in both sectors (numerical floor, as expected at a = 2).
Correction to the ablation's parity note: even- and odd-sector minima **coincide** to solver
tolerance for m ∈ {4,8,9,16} — the minus_m ground state is NOT parity-pure there (it is a mixture,
or the ground eigenspace spans both parities). For m ∈ {25,27,32} the sectors diverge
(1e-3…1e-2), so the degeneracy lifts for the higher towers — discretization or genuine, [O].
The ablation's "minus_n ground states odd (except minus_4, even)" needs reconciliation with this;
likely it referred to a dominant component or different parameters. [N, flagged.]

The n = 4 anomaly sharpens: |λ₁(minus_4)| = √2·Λ(4)/√4 = Λ(2)/√2 = c₂ exactly (6 digits).
Removing the n = 4 kink exposes the **n = 2 coefficient** — a tower structure: the 2-tower's
leading kink is "backed by" the n = 2 term. (Since Λ(4) = Λ(2) = ln 2, this reads
|λ₁| = ln 2/√2.)

**Test B — the marginal directions are shared across towers.** Overlaps ⟨w_m|w₉⟩_M (odd sector):
w₈·w₉ = **−0.9916**; w₁₆·w₉ = −0.7804; w₂₅·w₉ = −0.4563; w₂₇·w₉ = +0.3969; w₃₂·w₉ = −0.2664;
w₄·w₉ = +0.1898. The minus_8 and minus_9 ground states are nearly the SAME vector (up to sign):
the 2-tower and 3-tower leading kinks share one marginal direction.

**Test D — the minus_9 ground state is near-null for the FULL form:** Q_full[w₉]/M = 1.05e-7.
Since Q_full = Q_minus_9 − Q^(9), exactness forces w₉ᵀQ^(9)w₉/M = c₉ — the kink at 9 is EXACTLY
what holds w₉ up. The full form's positivity is marginal in direction w₉, and the load is carried
by a single kink with exactly the von Mangoldt coefficient.

**Test C — kink-kernel anatomy on w₉:** K_n[w₉]/M[w₉] (stripped kernels): K₉ = 1.000000 (exact,
by the D argument); K₈ = 0.976260 (w₉ nearly activates the n = 8 kink too — consistent with the
0.99 overlap); K₁₆ = 0.585907; K₄ = 0.309037; K₂₅ = 0.162666; K₂₇ = 0.114558; K₃₂ = 0.040641.
Each w_m maximally activates its own kink (K_m[w_m]/M = 1 in exactness cases, = √2 for m = 4 by
the c₂ finding) and partially activates its tower-neighbors.

**Test E — first-order sensitivities miss the structure:** s_n = v_eᵀQ^(n)v_e/M on the full even
ground state: s₄ = −0.398, s₈ = −0.134, s₉ = −0.169, s₁₆ = −0.027, s₂₅ = −0.0127, s₂₇ = −0.0060,
s₃₂ = −0.0014 — all negative (removing a kink lowers λ₁, as expected) but far below c_n and not
following the exact pattern. Perturbation theory around the full ground state does not see the
exactness; the exactness lives in the marginal directions w_m, not in v_e. Consistent with the
ablation's wrong-sign first-order finding.

### 3.4 What this means for the heresy [I]

The pilot gives F1 its first piece of concrete mathematics: **the Λ-weighted form sits at a
multicritical point of the positivity cone, and each prime-power kink is individually load-bearing
with exactly its von Mangoldt coefficient.** The marginal directions w_m are near-null for the
full form; each kink holds up its own direction with K_m[w_m]/M = 1; the 2- and 3-tower leading
kinks share a direction (overlap 0.99); the n = 4 kink is backed by the n = 2 coefficient.

This is the *beginning* of a selection argument — the Λ weights are not just "some positive
weights," they sit at a point where every prime power is exactly critical. But the creed's demand
stands: multicritical is *permitted*-flavored, not *selected*-flavored, until uniqueness (or a
rigidity theorem: any positive weights near this point must be close to Λ) is shown. The even/odd
degeneracy for the leading towers is a further structural hint — a hidden symmetry in the
marginal directions would be worth hunting, since a symmetry is the usual precursor to a
uniqueness proof. [O]

## 4. Experiment D (secondary, staged): extremal test-function anatomy — NOT RUN

The knife-edge variants (a = 0.4/0.5, λ₁ = +1.8e-4/+9.7e-7) were to be dissected for the extremal
test function's anatomy. Not executed — Experiment B consumed the budget and returned the more
valuable result. Staged as follow-up.

## 5. The gate: what would promote the heresy from philosophy to mathematics

1. **Uniqueness/rigidity:** prove (or numerically evidence, then prove) that the Λ weights are the
   UNIQUE — or rigid — multicritical point: any weight sequence with λ₁ ≥ 0 in a neighborhood
   must coincide with Λ(n)/√n. The pilot's exactness is step zero of this.
2. **A variational principle with a unique minimizer** (F3 made honest): exhibit a natural
   functional on weight sequences / zero configurations whose unique minimizer is the Λ weights /
   the zero set. Without uniqueness it is curve-fitting.
3. **The even/odd degeneracy explained:** if the marginal ground eigenspace has a structural
   parity doubling, find the symmetry. Symmetries precede uniqueness theorems.
4. **The n = 4 → c₂ tower finding derived:** why does removing the 4-kink expose the n = 2
   coefficient? An analytic derivation would constrain any future selection argument.

## 6. Verdict [I]

The heresy is a **genuine rephrasing with real mathematical content** — not a new logical form
(Weil's function-field proof is the working precedent; de Bruijn–Newman is the best
number-field selection-flavored theorem; Lee–Yang is the cleanest "positivity selects zeros"
specimen), but the pilot contributes **one piece of new concrete math**: the Λ-weighted screw
form is multicritical with each prime-power kink exactly load-bearing (K_m[w_m]/M = 1), the
2-/3-tower kinks sharing a marginal direction, the 4-kink backed by the n = 2 coefficient.

The selection gloss — that positivity *selects* the zeros, rather than merely *permitting* the
Λ weights — stays philosophy until the gate in §5 is passed. Per the creed: the Λ weights are
currently **permitted, not selected**. The three closed fronts say the eigenvalue routes keep
dying; this file says the positivity route has a precise marginal anatomy worth one more push,
aimed at uniqueness, not at another operator.

**No RH claims made. Nothing in this file enters the ledger, repo, or research notes without
Jeremy's explicit per-item authorization.**
