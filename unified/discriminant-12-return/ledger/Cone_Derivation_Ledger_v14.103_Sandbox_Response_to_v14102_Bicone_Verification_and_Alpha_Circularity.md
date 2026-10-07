# Cone Derivation Ledger v14.103 — Sandbox Response to v14.102 Audit Requests: Bicone Verification Committed; a₀ Circularity Acknowledged

**Date:** 2026-10-07
**Track:** Sandbox / v14.102 audit-request response
**Status:** [D] bicone ladder-algebra verification committed and independently verified; [I] a₀ circularity in e²/α claim acknowledged — it is a consistency check on Y_geom, not an independent α determination, unless an α-independent a₀ source is supplied. No v14.097–v14.101 results withdrawn.
**Parents:** v14.097, v14.102.
**Collision check:** live ledger max v14.102 at write time; v14.103 is next-free. No collision.

---

## 1. Request 1: bicone ladder-algebra verification — DELIVERED [D]

Committed: `unified/discriminant-12-return/research-notes/bicone_ladder_verify.py`.

The script independently verifies both v14.097 §2–§3 claims by explicit computation:

**Selection rule (§2).** In the 16-dim truncated Fock space (0/1 quantum per mode;
exact for these matrix elements since |1s⟩,|2p,m⟩ have ≤1 quantum/mode):
```
M[i,j,m] = <1s|a_i b_j|2p,m>   [a1b1 a1b2 a2b1 a2b2]
  m=+1: +1.0000 +0.0000 +0.0000 +0.0000  OK
  m= 0: +0.0000 +0.7071 +0.7071 +0.0000  OK
  m=-1: +0.0000 +0.0000 +0.0000 +1.0000  OK
```
Nonzero pattern matches q(i,j)=−m (a₁b₁↔m=+1 since a₁ carries m=−1/2 as a dual
spinor). The Wigner–Eckhart δ_{q,−m} selection rule is CONFIRMED by direct
computation. The +1.0000 / 1/√2 values match v14.097.

**SO(3) obstruction (§3).** Analytic (exact bosonic algebra, no truncation):
```
[J^a_+, a1] = [a1^dagger a2, a1] = -a2    (since [a1^dagger,a1] = -1)
[L_+, a1b1] = -a2 b1 - a1 b2 = -sqrt(2) T_0
```
A proper SO(3) vector operator requires [L_+,T_{−1}] = +√2·T_0. The minus sign
is the obstruction: a_i are annihilation operators = dual/conjugate spinors,
not proper SU(2) tensors (the Schwinger spinor is a†, not a). The bilinears
transform with flipped ladder signs. OBSTRUCTION CONFIRMED.

This closes the reproducibility gap flagged in v14.098/v14.100/v14.102 for the
bicone ladder algebra specifically. The construction remains Jeremy's own; this
is independent verification, not reconstruction.

---

## 2. Request 2: a₀ circularity — ACKNOWLEDGED [I]

The audit (v14.102 §3) is correct. Working through the algebra:

Given a₀ := 4πε₀ℏ²/(mₑe²) [definition], the formula
```
e² = 9πε₀ℏc³A₂₁ / (ω³a₀²Y_geom²)    [with 1/3 factor per v14.101]
```
becomes, upon substituting a₀²:
```
e² = K·mₑ²·e⁴ / (16π²ε₀²ℏ⁴Y_geom²),   K = 9πε₀ℏc³A₂₁/ω³
```
so that solving for e² yields a relation determining Y_geom given e²,
not e² given Y_geom. The CODATA a₀ numerical value was computed using a
prior e²/α; plugging it back in recovers that prior e² up to the Y_geom
consistency. It is a **consistency check**, not an independent determination.

**What the 0.07% actually confirms.** Y_geom = 768/(243√6) is derived purely
from SO(4,2)/bicone geometry, independent of e². The 0.07% agreement of the
full chain (A₂₁, ω, CODATA constants, Y_geom) confirms that this geometric
ratio is correct — i.e., the SO(4,2) geometry matches physical reality to
0.07%. That is genuine and nontrivial. But it does not "determine α from
one spectral line"; it verifies Y_geom against the known α.

**On an α-independent a₀.** No such source is supplied here. The Bohr radius
as a tabulated length is inherently tied to α via a₀ = α/(2R_∞) (R_∞ measured
spectroscopically) and via the SI definitions themselves. Unless Jeremy or
Lane A can point to a direct length-metrology a₀ independent of spectroscopic
α, the honest statement is (b): restate as a consistency check on Y_geom.

**Proposed restatement.** "The SO(4,2)/bicone geometry predicts the
dimensionless dipole ratio Y_geom = 768/(243√6). Combined with the measured
Lyman-α (A₂₁, ω) and CODATA constants, this reproduces e² to 0.07%,
confirming the geometric prediction. This is a consistency check on Y_geom,
not an independent determination of the fine-structure constant."

---

## 3. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Bicone S2/S3 verification committed and independently confirmed.}\\
&\text{Selection rule }q=-m\text{ holds; SO(3) ladder sign-flip obstruction holds.}\\
&\text{[I] a₀ circularity acknowledged: e² chain is a consistency check on }Y_{\rm geom},\\
&\text{not an independent }\alpha\text{ determination. Proposed restatement above.}\\
&\text{Nothing in v14.097--v14.101 withdrawn or disputed on numerical grounds.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: external-audit
type: audit-response
parent: v14.103
status: closed
action: (1) bicone_ladder_verify.py committed; both S2/S3 claims independently verified. (2) a₀ circularity acknowledged with proposed restatement as Y_geom consistency check. If an α-independent a₀ source exists, Sandbox will audit that path on request.
