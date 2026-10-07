# Cone Derivation Ledger v14.102 — External Audit Request to Sandbox: Bicone Ladder-Algebra Code, and the e²/α Circularity Question

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [REQUEST] Direct ask to Sandbox, routed through the ledger (no live cross-session channel is available to this audit thread — confirmed via `ListAgents`/`list_sessions`, which show no other reachable Claude session on this account). Jeremy has confirmed Lane A is back on the certification/Suzuki track and that this bicone/SO(4,2) hydrogen-dipole line is Sandbox's, with the bicone construction itself being Jeremy's own. This entry asks Sandbox for two specific things needed to close out the verification of v14.097/v14.099/v14.101, with full credit and context given to whose construction this is.
**Parents:** v14.097, v14.098, v14.099, v14.100, v14.101.
**Collision check:** immediately before this write, live HEAD was `afc200064bc103906c87bccd87c753f32fe50772` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.101. No collision. Re-checked immediately before commit (see §4).

---

## 1. Context

Rounds 180–182 independently verified every *arithmetic* claim in v14.097/v14.099 (the target dipole value, the `|C|/a₀=256/(243√2)` identity, the e²-from-Lyman-α numerics) by at least two independent methods each, including rebuilding the parabolic hydrogen wavefunctions from scratch. That part of the record is solid.

Two things remain open, and both need Sandbox specifically, since this is Sandbox's track and the bicone construction is Jeremy's own — this audit thread does not want to guess at or reconstruct someone else's construction when the source can just supply it.

## 2. Request 1: commit the bicone ladder-algebra verification

v14.097 §2–§3 describes two results as "machine-verified":

1. The Schwinger-boson bicone bilinears `M[i,j,m]=⟨1s|aᵢbⱼ|2p,m⟩` exhibiting the exact vector selection rule `δ_{q,−m}` with value `+1`.
2. The obstruction: `ab`-type (and `a†b†`-type) bilinears failing the `[L_±,·]` ladder relations needed to be genuine `SO(3)` vector operators under `L=J^a+J^b`, "for every σ-pairing tried."

Both are cited only to `workspace/d12/explorations/bicone-dipole/REPORT.md` — a path not in this repository. Nothing backing either claim is committed, so unlike every other claim in this project this round, this audit thread cannot independently check it by execution or hand re-derivation from what's available.

**Ask:** commit the actual verification — even a short script (sympy symbolic Schwinger-boson operators, or explicit finite-dimensional matrix realizations of `J^a_±`, `J^b_±`, `L_±=J^a_±+J^b_±`, and the `aᵢbⱼ` bilinears) that computes `[L_±, a_ib_j]` for each σ-pairing and shows it fails to close into the proper vector-operator commutation relation. Likewise for the `δ_{q,-m}` selection-rule claim in §2. This is exactly the kind of check this thread has done for every other claim this session (e.g. the nilpotent-frequency lemma in Round 179, the parabolic matrix element in Round 182) — it just needs the code to exist in the repo to do it for the bicone construction too.

## 3. Request 2: address the a₀ circularity in the e²/α claim

v14.097/v14.099 state the e²-from-transitions chain achieves `e²=2.569×10⁻³⁸ C²` (0.07% agreement) "with ZERO Schrödinger input," and that "the program's kinematics funds α≈1/137 given one spectral line."

Working through the formula `e² = 9πε₀ℏc³A/(ω³a₀²Y_geom²)`: `Y_geom` (the dimensionless `768/(243√6)` ratio) is genuinely independent of `e²` — that part of the claim is clean. But `a₀` is not a geometry-only or independently-measured input here; the standard Bohr radius is defined as `a₀=4πε₀ℏ²/(mₑe²)`, so its tabulated (e.g. CODATA) numerical value already has some prior value of `e²`/`α` baked into it. Plugging that `a₀` back into the formula and solving for `e²` is a **consistency check** — it confirms `Y_geom` and the other inputs are mutually consistent with the `e²` already embedded in `a₀`, to 0.07% — rather than an independent determination of `e²`/`α` "from one spectral line" with no prior knowledge of the fine-structure constant.

This doesn't make the 0.07% agreement meaningless — it's a real, nontrivial confirmation that `Y_geom` is correct — but it's a narrower claim than "determines α."

**Ask:** either (a) point to a source for `a₀` in meters that is independent of any prior spectroscopic/QED determination of `α` (e.g. a direct length measurement), in which case the "determines α from one spectral line" claim would be justified and this thread will audit that path too; or (b) if no such independent `a₀` exists in this calculation, consider restating the result as what it actually is — a consistency check on the geometric dipole ratio `Y_geom`, not a fresh determination of the fine-structure constant.

## 4. What this does not affect

Nothing above touches the already-verified numerics (Rounds 180–182) or the μ₃₂ₖ/Lane-A Suzuki-Xi program, which is unrelated to this track.

---

HANDOFF-NOTE
target: sandbox
type: audit-request
parent: v14.102
status: open
action: (1) Commit the bicone ladder-algebra verification code backing v14.097 S2-S3 (the delta_{q,-m} selection rule and the ab-bilinear SO(3)-tensor-failure obstruction), so it can be independently checked the way everything else in this project has been. (2) Clarify the a0 source for the e^2/alpha claim: either point to an alpha-independent measurement of a0 in meters, or restate the claim as a consistency check on Y_geom rather than a fresh determination of alpha. Full credit to Jeremy for the bicone construction itself -- this is a request for the supporting verification code, not a dispute of the construction.
constraints: This is a request, not a correction -- nothing promoted in v14.097-v14.101 is being withdrawn or disputed on numerical grounds.
