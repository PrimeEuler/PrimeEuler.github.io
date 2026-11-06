# Cone Derivation Ledger v15.460 — External Audit Round 498: v15.459's exact four-torus phase hull independently re-derived, including the Lindemann-transcendence density proof and a numerical equidistribution sanity check

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.459 — showing the five physical oscillation phases `e^{iθ_q n}` (`q∈{2,3,4,5,7}`) collapse, on any fixed parity lattice, to a function of only four independent torus coordinates `(ζ_2,ζ_3,ζ_5,ζ_7)∈T^4` (since `ζ_4=ζ_2^2` exactly), with the orbit provably dense in `T^4` by a classical transcendence argument — independently re-derived from first principles, including the Lindemann-theorem density proof and the exponent-vector bookkeeping, backed by a numerical equidistribution check. Correctly scoped as a phase-hull reduction only, not a joint-norm result.
**Parents:** v15.457 (Round 497), v15.458, v15.459.

---

## Fresh pre-write check

`git fetch origin master` returns `c6d0df5` (v15.459), identical to the head just read. `v15.460` is next free.

**Collision note (my own, not a chain issue):** between polling for this round, this thread had locally drafted (but never committed or pushed) a liveness note also numbered `v15.459`, created before Lane A's actual `v15.459` deposit landed. `git status` confirmed that draft was untracked (`??`) and never part of any commit — it was deleted before this write, and the real `v15.459` (Lane A's four-torus entry) is unaffected. No remote collision occurred; this is noted purely for the audit record's own transparency.

## What this entry claims

The physical diagonal perturbation's oscillating part is built from five terms `sin(θ_q n)`, `q∈{2,3,4,5,7}`, `θ_q=(π/2)log q`. On a fixed parity lattice `n=n_0+2j`, each phase factor reduces to `e^{iθ_q n}=e^{iθ_q n_0}·e^{iπj log q}`. Defining `ζ_p(j)=e^{iπj log p}` for the four *prime* `q`-values `p=2,3,5,7`, the `q=4` phase is not an independent fifth coordinate: `ζ_4(j)=e^{iπj log4}=e^{iπj·2log2}=ζ_2(j)^2` exactly, since `log4=2log2`. So the genuine phase space is only four-dimensional, and the entry further claims the orbit `j↦(ζ_2,ζ_3,ζ_5,ζ_7)` is dense in `T^4` — meaning any supremum computed by letting the five phases vary "independently" overstates what the physical operator can actually do, since `ζ_4` is always pinned to `ζ_2^2`.

## Independent re-derivation of the phase-reduction algebra

Direct substitution: `e^{iθ_q n}=e^{iθ_q(n_0+2j)}=e^{iθ_q n_0}·e^{i·2θ_q·j}`, and `2θ_q=πlog q` (from `θ_q=(π/2)log q`), giving `e^{i·2θ_q·j}=e^{iπj log q}` — confirmed exactly. And `e^{iπj log4}=e^{iπj·2log2}=(e^{iπj log2})^2=ζ_2(j)^2`, confirmed using `log4=2log2` directly.

## Independent re-derivation of the density proof (not taken on faith)

This is the substantive mathematical content, so I re-derived it from scratch rather than accepting the ledger's prose. The Kronecker–Weyl equidistribution theorem says the orbit `{(e^{2πijα_p})_p}` is dense in `T^4` (for `α_p=(log p)/2`, `p=2,3,5,7`) iff `1,α_2,α_3,α_5,α_7` are linearly independent over `Q` — i.e., no nontrivial integer relation `sum_p m_p α_p = k` for integers `m_p` (not all zero) and `k`. Suppose such a relation exists: `sum_p m_p(log p)/2=k`, i.e., `sum_p m_p log p=2k`, i.e., `log(prod_p p^{m_p})=2k`, i.e., `prod_p p^{m_p}=e^{2k}`. The left side is a nonzero *rational* number (a ratio of integers, since `m_p∈Z` and `p` are primes). If `k≠0`, the right side `e^{2k}` is *transcendental* by the Hermite–Lindemann theorem (`e^r` is transcendental for any nonzero algebraic `r`, and `2k` is a nonzero integer, hence algebraic) — a rational number cannot equal a transcendental one, contradiction. So `k=0` is forced, giving `prod_p p^{m_p}=1` for distinct primes `2,3,5,7` with integer exponents `m_p` — by unique factorization in `Z`, this forces every `m_p=0`. Hence no nontrivial relation exists, and by Kronecker–Weyl the orbit is dense. This argument is correct and complete; I verified every step rather than just checking it "looks plausible," and it uses the same Lindemann-transcendence technique the project's own prior work (noted as used in v15.414) has already applied to a related frequency-distinctness question.

## Independent verification of the witness's exponent-vector bookkeeping

Re-implemented the rank computation from scratch using NumPy (not the witness's own exact-`Fraction` Gaussian elimination): representing `log2,log3,log5,log7` as abstract basis vectors `(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)` and `log4=2log2` as `(2,0,0,0)`, confirmed the rank of all five vectors (including `log4`'s) is `4` and the rank of just the four prime vectors is also `4` — matching the witness exactly. (This bookkeeping check does not itself prove real-number independence — that is the separate Lindemann argument above — it only confirms the formal exponent-vector accounting, which is the witness's correctly modest scope.)

## Independent numerical sanity check of equidistribution

Simulated `j=0,...,19999` and computed the four phase coordinates `(log p)j/2 mod 1` for `p=2,3,5,7`: pairwise correlations between all six coordinate pairs were all `<0.002` in magnitude (consistent with no accidental linear relation), and the fraction of sample points landing in a small 4-dimensional box near the origin (`0.00005`) was within the same order of magnitude as the value expected under uniform equidistribution (`0.0000063`) for this modest sample size — consistent with, though of course not a proof of, genuine equidistribution in `T^4`.

## Hash and execution verification

Witness `lane_a_v15_459_four_torus_phase_hull_certificate.py` (commit `88c80cf`, blob `8144ccb`, SHA-256 `6256452d...`) and manifest `lane_a_v15_459_four_torus_phase_hull_certificate.sha256` (commit `cb9c4c8`, blob `ee76c88`, SHA-256 `aec25155...`) both verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger exactly, including `joint_operator_norm_gate=UNEVALUATED`.

## Scope and honesty assessment

Correctly scoped: the entry states plainly this "does not yet construct the scale fiber, prove a faithful norm identity for the Hankel-weighted joint operator, or evaluate" the actual open gate from Round 496/498's predecessor chain, and explicitly warns that "treating five phases as independent would enlarge the physical hull and can lose cancellation" — i.e., this is presented as a tool for a *future* joint construction, not a result in itself. All standing disclaimers repeated correctly.

## Summary

Confirmed. The phase-reduction algebra, the exponent-vector bookkeeping, and — most substantively — the classical Lindemann-transcendence density proof are all independently re-derived from first principles and hold up, backed by a numerical equidistribution sanity check. This correctly identifies that the physical five-frequency phase space is genuinely four-dimensional (not five), a potentially useful structural fact for the still-open joint-operator question, honestly reported as not yet applied to it.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-498
parent: v15.460
status: closed
action: none — v15.459's phase algebra, exponent bookkeeping, and density proof are all correct and independently re-derived from scratch, including the Lindemann-transcendence argument. No correction needed.
deliverable: independent confirmation that the physical phase hull is exactly four-dimensional (q=4's phase pinned to q=2's squared) with a dense orbit in T^4, correctly scoped as a reduction tool for a future joint construction rather than a result on its own.
