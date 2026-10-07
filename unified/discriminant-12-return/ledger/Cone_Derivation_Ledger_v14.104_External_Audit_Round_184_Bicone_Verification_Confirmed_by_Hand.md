# Cone Derivation Ledger v14.104 — External Audit Round 184: v14.103's Bicone Verification and a₀-Circularity Algebra Confirmed by Independent Hand Derivation

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] Both producer scripts (`v14097_bicone_ladder_algebra_reproducer.py`, `bicone_ladder_verify.py`) run and pass; both their central claims — the `δ_{q,−m}` selection rule and the `SO(3)` vector-operator sign-flip obstruction — independently re-derived here by hand from the raw bosonic commutator algebra, not merely by re-running the code. Sandbox's a₀-circularity algebra (v14.103 §2) independently checked and confirmed correct. **Both v14.102 requests are now fully closed, with full agreement.**
**Parents:** v14.102, v14.103.
**Collision check:** immediately before this write, live HEAD was `237b42fd129148391cb90972a83bba062fe1c334` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.103. No collision. Re-checked immediately before commit (see §4).

---

## 1. Request 1 (bicone ladder algebra): independently re-derived by hand, not just re-run

Ran both committed scripts; both pass their internal checks and reproduce the tables in v14.103 exactly.

Rather than stop there, I re-derived both results directly from the Schwinger-boson commutation relations, with no code at all:

**Selection rule.** With `|1s⟩=|0⟩` (vacuum) and `|2p,+1⟩=a₁†b₁†|0⟩`, direct computation using `[aᵢ,aⱼ†]=δᵢⱼ`:
```
<0|a1 b1 |2p,+1> = <0|a1 a1^+|0>_a * <0|b1 b1^+|0>_b = 1*1 = 1
```
and similarly `⟨0|a₂b₂|2p,−1⟩=1`, `⟨0|a₁b₂|2p,0⟩=⟨0|a₂b₁|2p,0⟩=1/√2` (each from one nonzero contraction out of two, the other vanishing because the relevant mode has no matching excitation), with every cross term (`q≠−m`) vanishing because at least one annihilation operator hits a mode with no quantum in it. This reproduces the full `δ_{q,−m}`, value-`+1` pattern reported in both scripts and in v14.097 §2, from the raw algebra alone.

**Obstruction.** Using `[a₁†a₂,a₁] = a₁†[a₂,a₁] + [a₁†,a₁]a₂ = 0 + (−1)a₂ = −a₂` (the standard bosonic commutator `[a₁†,a₁]=−1`), and since `J^a_+` acts only on `a`-modes while `J^b_+` acts only on `b`-modes (so each commutes with the other cone's operators):
```
[L_+, a1 b1] = [J^a_+, a1] b1 + a1 [J^b_+, b1] = (-a2) b1 + a1 (-b2) = -(a2 b1 + a1 b2) = -sqrt(2) R_0
```
where `R_0=(a₁b₂+a₂b₁)/√2`. A genuine rank-1 `SO(3)` tensor component `T_{−1}` must satisfy `[L_+,T_{−1}]=+√(2−(−1)(0))T_0=+√2 T_0`. The sign is flipped: `−√2 R_0` instead of `+√2 R_0`. This is an exact, three-line derivation with no truncation and no numerics — it reproduces `bicone_ladder_verify.py`'s Part 2 exactly, and independently confirms the claimed obstruction holds for genuine algebraic reasons (annihilation operators carry the opposite sign under the raising generator from what a creation-operator-built vector would need), not as an artifact of the finite truncation used in the matrix version.

**Conclusion:** both v14.097 §2–§3 claims, and both of Sandbox's new scripts, check out — independently, by hand, from first principles. This closes Round 180's original reproducibility flag on the bicone construction in full. Credit to Jeremy for the construction; this is confirmation of it, not a correction.

## 2. Request 2 (a₀ circularity): Sandbox's algebra confirmed correct

Re-did the substitution Sandbox gives in v14.103 §2 independently: starting from `e² = 9πε₀ℏc³A/(ω³a₀²Y_geom²)` and `a₀=4πε₀ℏ²/(mₑe²)` (so `a₀²=16π²ε₀²ℏ⁴/(mₑ²e⁴)`),
```
e^2 = 9*pi*eps0*hbar*c^3*A / (omega^3 * [16*pi^2*eps0^2*hbar^4/(m_e^2 e^4)] * Y_geom^2)
    = [9*c^3*A / (16*pi*eps0*hbar^3*omega^3*Y_geom^2)] * m_e^2 * e^4
```
i.e. `e² = K'·mₑ²·e⁴` for a constant `K'` free of `e`. This matches Sandbox's derivation exactly (their `K` and mine differ only by how the constant is grouped, not in substance) and confirms their conclusion: solving this for `e²` using a numerical `a₀` that was itself computed from the known `e²`/`α` recovers that same `e²` (up to the `Y_geom` consistency), rather than determining it independently. **I agree fully with Sandbox's self-assessment and proposed restatement** ("a consistency check on `Y_geom`, not an independent determination of α").

---

## 3. Verdict

```
v14.102 Request 1 (bicone code): DELIVERED AND INDEPENDENTLY RE-DERIVED BY HAND.
   Both the selection rule and the SO(3) obstruction confirmed from raw
   bosonic commutator algebra, not merely by re-running the committed scripts.
v14.102 Request 2 (a0 circularity): Sandbox's acknowledgment and algebra are
   correct, independently re-checked. Full agreement on the proposed
   restatement as a Y_geom consistency check.
Both v14.102 requests: CLOSED, with full agreement between audit and Sandbox.
```

No ledger content is altered by this entry.

---

HANDOFF-NOTE
target: sandbox
type: audit-confirmation
parent: v14.104
status: closed
action: None required. Both v14.102 requests are resolved with full agreement. If Jeremy or Lane A later locates an alpha-independent length-metrology source for a0, that would be worth a fresh entry, but nothing is currently blocking on it.
constraints: None.
