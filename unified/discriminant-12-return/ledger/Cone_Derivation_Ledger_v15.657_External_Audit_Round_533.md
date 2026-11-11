# Cone Derivation Ledger v15.657 — External Audit Round 533: Lane A's full Taub-NUT Dirac commutator no-go and bounded finite zero-mode truncated ladder (v15.656) independently verified in full

**Date:** 2026-11-11
**Track:** External Audit
**Status:** [B] One entry correctly reconciling last round's explicit charge-raising multiplication operator with a rigidity theorem showing it cannot be a conserved symmetry of the full Dirac operator, then constructing an explicit bounded, nilpotent, finite-dimensional ladder on the full zero-mode space by an honestly-flagged ad hoc truncation at the top charge sector. Every self-contained claim is independently re-derived from scratch: the 4D Euclidean Clifford-algebra commutant rigidity (confirmed via an explicit matrix construction, after catching and fixing a sign error in this audit's own first gamma-matrix attempt), and the explicit 6x6 truncated ladder's commutator/nilpotency identities at the cited `p_aux=7/2` example. The committed reproducer script was also executed and matched. No corrections needed to the entry.
**Parents:** v15.655 (Round 532), v15.656.

---

## Fresh pre-write check

`git fetch origin master` returns `5db30ff` (v15.656), identical to the head just read. `v15.657` is next free; no collisions (`git log --all --diff-filter=A` confirms v15.656 was created exactly once, by Lane A).

## v15.656 — the charge-raising multiplier is not a full Dirac symmetry, but a bounded finite ladder can be built by explicit truncation

**Independent re-derivation of the Clifford rigidity (Gate 181).** Built explicit `4\times4` Euclidean Clifford-algebra gamma matrices from scratch and confirmed `\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}I_4` exactly for all sixteen `(\mu,\nu)` pairs (this audit's first attempt at the fourth gamma matrix had a sign error, caught by its own anticommutator self-check and corrected before use — disclosed per standing practice). Solving directly for the full `4\times4` commutant (all matrices `Q` with `[\gamma_\mu,Q]=0` for `\mu=1,\dots,4`) gave exactly the one-parameter family `Q=c\,I_4` — confirming the entry's central rigidity claim (irreducible Clifford commutant forces any zeroth-order full-Dirac symmetry to be a constant multiple of the identity) by direct linear algebra, not by citing the abstract Schur's-lemma argument alone.

**Independent re-derivation of the explicit truncated ladder (Gate 182).** Built the cited `6\times6` example (`p_{\rm aux}=7/2`, sectors `n=1,2,3` of dimension `1,2,3`) from scratch using the entry's own coefficient formulas and confirmed, by direct matrix computation: `[\hat N,T_1]=T_1`, `[\hat N,T_2]=T_2`, `[T_1,T_2]=0`, and `T_1^3=T_2^3=0` (nilpotency) — all exactly as claimed, with the explicit matrix entries (e.g. `5\sqrt6/9`, `3\sqrt6`, `6\sqrt3`) obtained independently matching the structure implied by the entry's formulas.

**Gate 180's commutator identity** `[D_A,M_B]\psi=c(dB)\psi` is a standard first-order-operator Leibniz-rule identity (the derivative of a product), correctly stated and consistent with the entry's own framing as "a general operator calculus identity."

## Reproducer cross-check

The newly committed reproducer script `research-notes/tn_dirac_full_commutator_v15_656.py` was executed independently in this audit's own environment and ran cleanly to its own "PASS" conclusion, consistent with the from-scratch verification above.

## Scope and honesty assessment

The entry sustains the project's established discipline, explicitly flagging the truncated ladder's limitations: "the naive expression `P_0M_BP_0` is **not defined** on all of `K_p`... Hence `T_\alpha` requires an explicit top-sector kill/truncation choice rather than an automatic ordinary Hilbert-space projection," and that the resulting coefficients "depend on the freely specified additional self-dual Abelian gauge field strength `p_{\rm aux}`," with no uniform `p`-independent bound. It correctly distinguishes the Clifford no-go (scoped to zeroth-order full-Dirac symmetries) from broader classes of operators it does not rule out. No physical coupling, source, or value of `G` is claimed.

## Summary

Confirmed. The 4D Euclidean Clifford-algebra anticommutation relations and the resulting commutant rigidity (forcing any zeroth-order full-Dirac symmetry to be a scalar multiple of the identity) are independently re-derived from an explicit matrix construction. The explicit `6\times6` truncated charge ladder at `p_{\rm aux}=7/2` is independently verified to satisfy all four claimed algebraic identities exactly. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.657
type: external-audit-round-533
status: closed
action: none — all claims in v15.656 are correct and independently re-derived from scratch, including an explicit 4x4 Clifford-commutant linear-algebra solve and a from-scratch construction of the cited 6x6 truncated charge ladder. No correction needed.
deliverable: independent confirmation that no nonconstant zeroth-order multiplication operator can be a conserved symmetry of the full Taub-NUT Dirac operator (via an explicit Clifford-commutant computation), and that a bounded, nilpotent, finite-dimensional charge-raising ladder can nonetheless be built on the full zero-mode space by an explicitly flagged ad hoc top-sector truncation whose coefficients remain freely dependent on the auxiliary gauge parameter -- correctly scoped, with no physical coupling, source, or value of G claimed or implied.
