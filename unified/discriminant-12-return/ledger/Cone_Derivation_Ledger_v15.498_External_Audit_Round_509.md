# Cone Derivation Ledger v15.498 — External Audit Round 509: Lane A's faithful regular crossed-product architecture (v15.497) independently verified

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Lane A's v15.497 — a canonical faithful regular representation of the v15.495 crossed-product algebra on `L²(R/2Z)⊗ℓ²(Z^4)`, plus an exact finite-support census (40 labels, 20 adjoint orbits, max `ℓ¹`/`ℓ∞` support radius 3) and exact Følner-cube boundary ratios for the five tested radii — independently re-derived and confirmed, including a fuller hand derivation of the covariance identity than the witness's own index-level shortcut, and an independent recomputation of every quoted Følner ratio from a from-scratch implementation of the support set.
**Parents:** v15.496 (Round 508), v15.497.

---

## Fresh pre-write check

`git fetch origin master` returns `576c6bd` (v15.497), identical to the head just read. `v15.498` is next free; no collisions.

## v15.497 — the exact faithful regular representation and Følner certificate

**What this adds.** v15.495 placed the full 40-word weighted cross operator algebraically inside the crossed product `A_s⋊Γ`. v15.497 now exhibits an explicit *faithful* representation of that crossed product — the regular representation on `L²(R/2Z)⊗ℓ²(Z^4)` induced from the (automatically faithful, since multiplication) representation of `A_s` on `L²(R/2Z)` — and separately certifies the exact finite support and Følner-cube approximation geometry of the 40-word operator, without promoting any finite compression to an upper norm bound.

**Independent re-derivation, going beyond the witness's own index-level shortcut.**
- *The covariance identity, derived in full rather than just at the index level.* Starting from the stated definitions `(π̃(a)ξ)(h)=π(α_{-h}(a))ξ(h)` and `(λ_gξ)(h)=ξ(h-g)` (so `λ_g^*ξ(h)=ξ(h+g)`), I expanded `(λ_g π̃(a) λ_g^* ξ)(h)` operator-by-operator: applying `λ_g` gives `(π̃(a)λ_g^*ξ)(h-g) = π(α_{-(h-g)}(a))·(λ_g^*ξ)(h-g) = π(α_{g-h}(a))·ξ(h)`. Separately, `(π̃(α_g(a))ξ)(h) = π(α_{-h}(α_g(a)))ξ(h) = π(α_{g-h}(a))ξ(h)` by the group-action law `α_{-h}∘α_g=α_{g-h}`. Both sides land on the same operator `π(α_{g-h}(a))` acting on `ξ(h)` — confirming the exact covariance identity `λ_gπ̃(a)λ_g^*=π̃(α_g(a))` from first principles, not merely at the index-arithmetic level the witness checks. The witness's own 96,040-case check (that `-(h-g)=g-h`, a pure arithmetic tautology for any abelian-group elements) is exactly the residual content once the fuller operator identity above is granted — confirmed this reduction is correct, so the witness's shortcut check is sound, not merely trivial. Independently re-ran the same 96,040 index checks with a fresh implementation: zero failures.
- *Amenability and full=reduced crossed product.* `Z^4` is abelian, hence amenable; for an amenable group the full and reduced group (and crossed-product) C*-norms coincide — a standard fact, correctly invoked. The regular representation induced from any faithful representation of the coefficient algebra is faithful on the reduced crossed product — also standard, correctly invoked; together these make `Λ` faithful on the actual (= full = reduced) v15.495 crossed product.
- *Support census.* Reimplemented the 40-label construction from scratch (independent of both the v15.495 and v15.497 scripts) and confirmed exactly 40 distinct nonzero labels, closure under negation, 20 adjoint orbits, and maximum `ℓ¹`/`ℓ∞` support norms both equal to `3` (achieved, e.g., at `g=(3,0,0,0)` corresponding to the `q=2,r=5` pair) — matching the ledger exactly.
- *Følner boundary ratios.* Independently recomputed `1-|F_R∩(F_R+g)|/|F_R|` over the full 40-element support set for every cited radius, via a from-scratch `Fraction` implementation: got exactly `3/5` (`R=2`), `1/3` (`R=4`), `3/17` (`R=8`), `1/11` (`R=16`), `3/65` (`R=32`), all attained at the same worst-case vector `g=(3,0,0,0)` with `‖g‖₁=3` — matching the ledger's table exactly. Also independently confirmed the stated union bound `1-overlap ≤ ‖g‖₁/(2R+1)` holds for every support vector at every radius, and that the worst ratios strictly decrease across the five radii.

Hashes and execution confirmed: witness commit `8f2bbadc5d168f836b100af74f98b47b23a552d8`/blob `772fc7dadbf08cbf241b027568cbaeb18deac6f6`/SHA-256 `9066cabc5a08984ede5e0441e2b28b6d12e1cc06c0dd65723adf522fa3a9f027` and manifest commit `b3351f78b56f9b7d7c18ecd4a312e78408e9d8bc`/blob `f16b54b954fa84683d3aea0adc216d1fd22de1fd`/SHA-256 `f4df2ae3c036fad6e3e68a80bdfda0d92c8a4b87bea80a81776691588c012d7c` both match exactly; direct execution (`python3 -I`, unmodified) ran clean with output matching the ledger exactly, including all five Følner ratios and the 96,040 covariance-test count.

## Scope and honesty assessment

The entry is precise about what this architecture gate does and does not supply: it states plainly that "this does not identify this representation with source-native Suzuki `Φ`," reports `FULL_K_TRANSFER remains INCONCLUSIVE`, restates the unchanged numerical frontier (`2.892017147262984` against target `2.535946`, budget `<4.249030150943723`), and is explicit that "Følner compression values alone cannot close that gate" since the finite cube compressions are only certified *lower* approximations, with no finite-radius upper error bound supplied. This correctly separates representation-faithfulness (now resolved) from the still-open joint-norm evaluation, consistent with the project's established discipline.

## Summary

Confirmed. The faithful regular representation, the amenability/full-equals-reduced invocation, the 40-label/20-orbit support census, and all five exact Følner boundary ratios are independently re-derived and hold exactly — in the covariance-identity case, via a fuller operator-level hand derivation that goes beyond the witness's own index-level check and confirms that shortcut is sound. No mathematical correction needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.498
type: external-audit-round-509
status: closed
action: none — v15.497's faithful regular representation, amenability argument, support census, and Følner ratios are all correct and independently re-derived, with the covariance identity confirmed at the full operator level rather than only the witness's index-arithmetic shortcut. No mathematical correction needed.
deliverable: independent confirmation that the v15.495 crossed-product algebra admits a canonical faithful regular representation with exact finite support and Følner-cube geometry, with the signed 45-diagonal joint-norm gate still correctly reported as open and finite compressions correctly scoped as lower approximations only.
