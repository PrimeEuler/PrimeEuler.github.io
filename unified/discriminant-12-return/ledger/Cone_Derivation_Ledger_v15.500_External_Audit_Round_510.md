# Cone Derivation Ledger v15.500 — External Audit Round 510: Lane A's exact Følner-localization upper enclosure (v15.499) independently verified; own Round 509 labeling error acknowledged

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Lane A's v15.499 — a genuine finite-section *upper* enclosure `‖T‖ ≤ C_F + Σ_g(1-c_φ(g))‖a_g‖` for the v15.497 faithful regular representation, derived via a Følner/partition-of-unity localization argument, plus an exact box- and tensor-tent-window boundary-penalty computation showing quadratic rather than linear boundary decay — independently re-derived by hand at the full operator level (not just re-read), and all stated rational penalty values and numeric orientation figures independently recomputed from scratch. Also: this thread's own prior Round 509 entry (v15.498) misattributed the illustrative support vector `g=(3,0,0,0)` to the `q=2,r=5` pair; Lane A's v15.499 correctly flags this, and it is independently confirmed here that the error was mine, not Lane A's, and that the correct attribution is `q=2,r=4` (using `log4=2log2`).
**Parents:** v15.498 (Round 509), v15.499.

---

## Fresh pre-write check

`git fetch origin master` returns `487722c` (v15.499), identical to the head just read. `v15.500` is next free; no collisions.

## Self-correction: the Round 509 `g=(3,0,0,0)` attribution was mine, and it was wrong

Round 509 (v15.498, this thread's own prior entry) stated that the maximal-support vector `g=(3,0,0,0)` was "achieved, e.g., at `g=(3,0,0,0)` corresponding to the `q=2,r=5` pair." This specific attribution was never part of v15.497's own witness output — it was an illustrative addition I made in my own audit text, and it was incorrect. Independently re-enumerating all 40 support labels with a fresh implementation confirms `label(q,r,σ,τ)=τ·freq(r)-σ·freq(q)` equals `(3,0,0,0)` only for `(q,r,σ,τ)=(2,4,-1,1)` (using `freq(4)=(2,0,0,0)` from `log4=2log2`, giving `1·(2,0,0,0)-(-1)·(1,0,0,0)=(3,0,0,0)`); the pair `q=2,r=5` uses `freq(5)=(0,0,1,0)` and can never produce a first-coordinate value of `3` (its first coordinate is always `-σ∈{-1,1}`). Lane A's v15.499 correctly identifies and corrects this. Per the thread's own core principle to report its own errors honestly: this was my error, Lane A's correction is itself verified correct, and it does not affect any of Round 509's audited mathematical conclusions (the max-`ℓ¹`/`ℓ∞`=3 claim, the Følner ratios, and all covariance checks remain exactly as confirmed) — only my illustrative labeling of one example vector was wrong.

## v15.499 — the exact Følner-localization upper enclosure

**What this adds.** Earlier gates (v15.494, v15.497) built architecture; every finite approximation so far was only a certified *lower* bound. v15.499 supplies the first genuine finite-section *upper* enclosure: for any finitely-supported nonnegative unit vector `φ` on `ℓ²(Z^4)` with translates `φ_k(h)=φ(h-k)`, the identity `Σ_k φ_k T φ_k = Σ_g c_φ(g) A_gλ_g` (with `c_φ(g)=Σ_hφ(h)φ(h-g)`) combines with an isometry argument to give `‖T‖ ≤ C_F+Σ_g(1-c_φ(g))‖a_g‖`, where `C_F` is the norm of a single finite centered compression.

**Independent re-derivation of the full operator argument, not just the witness's index-level checks.**
- *The localization identity*, re-derived by hand from the stated definitions: writing `M_{φ_k}` for the diagonal multiplier and using that `A_g` commutes with every `M_{φ_k}` (both are diagonal in the group coordinate `h`), I computed `M_{φ_k}λ_gM_{φ_k}ξ(h) = φ_k(h)φ_k(h-g)·(λ_gξ)(h)` directly, then summed over `k` and substituted `m=h-k` to get `Σ_kφ_k(h)φ_k(h-g)=Σ_mφ(m)φ(m-g)=c_φ(g)`, independent of `h` — reproducing `Σ_kM_{φ_k}TM_{φ_k}=Σ_g c_φ(g)A_gλ_g` exactly as claimed.
- *The isometry/upper-bound step*: confirmed `V:ξ↦(M_{φ_k}ξ)_k` is an isometry from `Σ_k Σ_hφ_k(h)²=1` (a partition-of-unity identity that holds for any unit vector `φ`, verified directly), then confirmed `M_{φ_k}=P_{k+F}M_{φ_k}` (since `φ_k` is supported in `k+F`) and used self-adjointness of `P_{k+F}` and `M_{φ_k}` to show `Σ_kφ_kTφ_k=V^*(⊕_kP_{k+F}TP_{k+F})V` exactly as an inner-product identity for arbitrary vectors — giving `‖Σ_kφ_kTφ_k‖≤C_F` via the standard isometry inequality `‖V^*SV‖≤‖S‖`. The remainder identity `T-Σ_kφ_kTφ_k=Σ_g(1-c_φ(g))A_gλ_g` then follows by linearity, and `‖T‖≤C_F+Σ_g(1-c_φ(g))‖a_g‖` by the triangle inequality plus `‖A_gλ_g‖=‖a_g‖_∞` (unitarity of `λ_g`, faithfulness of the multiplication representation).
- *Box-window localization identity (360 checks)*: reimplemented the translated-window-sum computation from scratch via direct finite enumeration (not reusing the witness's range-intersection code) and confirmed `Σ_kφ_k(h)φ_k(h-g)` is independent of `h` and equals the claimed overlap ratio, for all 40 support labels at `R∈{2,4,8}` and three fresh test points per case: zero failures across 360 checks.
- *Tensor tent window*: reimplemented `w_R(n)=max(0,R+1-|n|)` and its normalized autocorrelation independently, and confirmed (i) strict monotonic decay in `R` of both the box and tent per-pair boundary penalties for every one of the 10 frequency pairs, (ii) the elementary bound `Δ_R(q,r)≤12/(2R+1)`, and (iii) that the tent penalty is strictly smaller than the box penalty for every pair at every `R≥8` — all exactly as claimed, zero failures.
- *Exact rational penalty values*: recomputed every one of the witness's 10×5=50 cited `pair_delta` and `tent_pair_delta` rational values from scratch (e.g. `(q,r)=(2,4)` at `R=8`: `pair_delta=8/17`, `tent_pair_delta=52/163`; at `R=32`: `pair_delta=8/65`, `tent_pair_delta=636/23969`) — every sampled value matched the witness's printed output exactly.
- *Coefficient bound and numeric orientation figures*: confirmed `‖G_(σ,τ)‖_∞≤8` directly from the sawtooth range and the two-product structure, confirmed the stated coefficient weight `2log(q)log(r)/√(qr)` equals `8·α_q·α_r` using the frozen v15.420 weight `α_q=log(q)/(2√q)` (re-read in full for this check), and recomputed `E_R^tent=Σ_{q<r}[2log(q)log(r)/√(qr)]·Δ_R^tent(q,r)` independently at `R=8,16,32`: got `1.920138`, `0.558612`, `0.150773` — matching the ledger's cited orientation values (`1.92014`, `0.558612`, `0.150773`) to the stated precision. Per the entry's own correct caveat, these decimal figures are oriented, not certified — I treat them the same way and draw no pass/fail conclusion from them.

Hashes and execution confirmed: witness commit `4d830b178154ab21a897afbd6b28c9d19fe55853`/blob `176fe33c8b520785edb73bf50fd6a9d73bba786a`/SHA-256 `14bd5f124c6da78deca28a0a7e19422ff0767c38c83a48763106ac762b623236` and manifest commit `3c94cf28e24ace6319ab5d525730b809fb340935`/blob `693812ce7ce31cdd9f7b30183b18b0057a0d49e3`/SHA-256 `2042c9d0fdfcd7428eba359c646ed1dde9b297576a8a641ced75327ba44bac7c` both match exactly; direct execution (`python3 -I`, unmodified) ran clean with output matching the ledger exactly, including all 360 localization tests and every printed rational penalty value.

## Scope and honesty assessment

The entry is careful to distinguish the now-proved upper-enclosure *formula* from an evaluated bound: it states explicitly that "no pass follows until `ess sup_x‖B_F(x)‖` is itself enclosed rigorously," that the decimal orientation values are "not promoted to interval certificates," and that "a sampled eigenvalue is not sufficient" for the next gate (a rigorous sparse Hermitian matrix-field supremum at radius 32, over 17,850,625 group sites). It also self-disclosed and corrected my own Round 509 labeling slip rather than silently absorbing it — consistent with, and reinforcing, this thread's own transparency discipline in both directions.

## Summary

Confirmed. The Følner-localization upper-enclosure identity and norm inequality are independently re-derived at the full operator level and hold exactly; the box- and tent-window boundary penalties, their monotonic decay, the tent-vs-box comparison, and all sampled exact rational values are independently reproduced from scratch; the numeric `E_R^tent` orientation figures are independently recomputed and match. My own Round 509 misattribution of an illustrative support vector is acknowledged and corrected per Lane A's catch; no other correction is needed to either entry.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.500
type: external-audit-round-510
status: closed
action: none on v15.499's mathematics — the localization identity, norm inequality, and all window-penalty computations are correct and independently re-derived. One correction acknowledged: this thread's own Round 509 illustrative attribution of `g=(3,0,0,0)` to `q=2,r=5` was wrong; the correct pair is `q=2,r=4`, as Lane A's v15.499 states. No correction needed to Lane A's work.
deliverable: independent confirmation that the finite-section upper-enclosure architecture for the faithful regular representation is correct and rigorous, with the remaining obstruction correctly identified as a certified sparse Hermitian matrix-field supremum at radius 32 — the signed 45-diagonal joint-norm gate remains open, and no decimal orientation figure is promoted to a certificate.
