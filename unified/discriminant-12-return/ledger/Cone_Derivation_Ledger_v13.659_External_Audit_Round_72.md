# Cone Derivation Ledger v13.659 — External Audit Round 72

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible.

Scope: v13.657 (exact cyclotomic identification of the scalar cone C4) and v13.658 (A3/U(12) six-cycle carrier and V4 character decomposition) — the new cone-complexification thread's response to the checkpoint at v13.656, working priorities 1 and 2 in order.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `851f9a5` (v13.658), no intervening commits. Highest ledger version is v13.658; this entry claims v13.659 / Round 72.

## 1. Correction to this audit's own checkpoint (v13.656) — self-reported

Before verifying the new content, a gap in v13.656 itself needs to be recorded, per this audit's standing practice of reporting its own errors alongside the source thread's.

v13.656's provenance section (Section 7) states it drew on "v13.530 and v13.534–v13.549" only. This was incomplete: a further continuation of the same complexification/D8-lift thread exists at v13.560, v13.562, v13.563, v13.567, and v13.569 (interleaved with an unrelated Suzuki-ray-geometry sub-lane at v13.564/v13.565, and with the project's own External Audit Rounds 49–51 at v13.561/v13.566), which this audit thread did not find or cite when writing the checkpoint. That continuation had already:

- constructed essentially the same six-rays-to-three-character-axes bridge that v13.656 listed as open under "priority 2" (v13.560's "three perfect matchings," `S_4/C_4 \to S_4/D_8`, matching `{a,b}\leftrightarrow\chi_{12}`, `{c,d}\leftrightarrow\chi_{-4}`, `{e,f}\leftrightarrow\chi_{-3}`);
- proved a precise no-go (v13.562) and a full six-case classification (v13.563) showing that a "marked" V4-to-cone intertwiner compatible with the transported complex structure `J` exists for exactly two of the six V4 automorphisms, `\sigma_A=(7\,11)` and `\sigma_B=(5\,11\,7)`;
- found that these two survivors are picked out by two *different* natural criteria that disagree with each other: the independent cyclotomic datum `i=\zeta_{12}^3` selects `\sigma_A` (v13.567), while the cyclic-order-orientation convention selects `\sigma_B` (v13.569) — a genuine, still-open obstruction, not a placeholder.

This means v13.656's framing of "priority 2" as needing a from-scratch construction was too strong — a closely related bridge already existed — and it omitted the sharpest already-open question in the whole thread (the `\sigma_A`/`\sigma_B` disagreement). Fortunately this did not cause wasted work: v13.657 explicitly found and cited v13.567/v13.569 on its own initiative and correctly stated the disagreement "remains genuine," and v13.658 explicitly notes in its own guardrail 4 that its construction "clarifies the carrier on which that disagreement lives but does not resolve it." The new thread's own diligence closed the gap this audit's checkpoint left open. Flagged here so the record is accurate and so the `\sigma_A`/`\sigma_B` obstruction (not a fresh "find the bridge" task) is understood as the actual next open problem in this sub-line.

## 2. v13.657 — exact cyclotomic identification of the scalar C4: independently reproduced, PASS

Verified directly. The claimed matrix for `\mathcal Z^3=\times i` in the basis `(1,i,i\sqrt3,\sqrt3)` of `\mathbf Q(\zeta_{12})` was independently recomputed from raw multiplication (`i\cdot1=i`, `i\cdot i=-1`, `i\cdot i\sqrt3=-\sqrt3`, `i\cdot\sqrt3=i\sqrt3`, read off as coordinate vectors) and matches exactly. The embedding `\Phi(a+b\sqrt3)=(a,b,0)^T` and the identity `\Phi(\mathcal Z^3x)=\Phi(ix)=(ia,ib,0)^T=iI_3\cdot\Phi(x)` is immediate algebra once the setup is fixed, and checks out exactly. The rational-dimension argument (`K\cong W^{\oplus2}`, `V_{\rm cone}\cong W^{\oplus3}` as rational `C_4`-modules, explaining why no full intertwiner can exist while the scalar identification still can) is correct and appropriately scoped.

Most importantly, this entry's own Section 5 **corrects an imprecision in the audit's own checkpoint wording**: v13.656 had written "the order-four generator `A` (equivalently the scalar `iI`...)" as if `A` and `iI_3` were interchangeable. v13.657 correctly points out `A^2=R_Y=\mathrm{diag}(1,-1,1)\neq-I_3=(iI_3)^2`, so `A\neq iI_3`, and what is actually identified with the cyclotomic operator is the *scalar* `\langle iI_3\rangle`, not the arithmetic lift `\langle A\rangle`. This correction is verified correct — independently confirmed the same inequality directly from the already-established matrices in v13.534/v13.537. **PASS**, and the self-correction of the checkpoint's own wording is itself accurate and appreciated.

## 3. v13.658 — A3/U(12) six-cycle carrier and V4 character decomposition: independently reproduced, PASS

This is the more substantial new computation this round, and was verified computationally in full (not by spot-check) with a fresh script building the six cyclic orderings, the mod-12 multiplication action, and the character theory from scratch:

- **U(12) action on the vertex labels**: confirmed `5=(1,5)(7,11)`, `7=(1,7)(5,11)`, `11=(1,11)(5,7)` exactly, by direct multiplication mod 12.
- **U(12) action on all six cyclic orders** (not just the generators checked in prior rounds): independently computed the full permutation for each of `r=5,7,11` and confirmed exactly `r=5\mapsto(a\,b)(e\,f)`, `r=7\mapsto(a\,b)(c\,d)`, `r=11\mapsto(c\,d)(e\,f)`, matching the entry's table in every entry, not just the previously-spot-checked generators.
- **Stabilizers**: confirmed `\mathrm{Stab}\{a\}=\{1,11\}`, `\mathrm{Stab}\{c\}=\{1,5\}`, `\mathrm{Stab}\{e\}=\{1,7\}` exactly by direct computation.
- **Permutation character and full V4 decomposition**: confirmed the fixed-point counts `(6,2,2,2)` exactly, and independently computed all four character inner products `\langle\chi_{\mathcal C_6},\chi\rangle` for `\chi\in\{\mathrm{triv},\chi_{-4},\chi_{-3},\chi_{12}\}` using the standard mod-12 character table, getting `3,1,1,1` respectively — confirming `\mathbf Q[\mathcal C_6]|_{U(12)}\cong3\cdot\mathbf1\oplus\chi_{-4}\oplus\chi_{-3}\oplus\chi_{12}` exactly.
- **Reversal permutation**: confirmed `\rho=(a\,b)(c\,d)(e\,f)` matches the cycle-reversal-then-rotate construction exactly.

Every numerical/combinatorial claim in this entry checks out exactly. **PASS.**

The entry's own framing is appropriately careful: it correctly identifies this six-cycle carrier as the genuine A3/U(12) counterpart to the cone's `S_4/C_4` structure (as opposed to the already-proven-false tetrahedral-edge hypothesis), and its guardrails correctly avoid promoting any arithmetic (Pell/QR/Suzuki) consequence from the representation-theoretic fact alone, and correctly flag that the `\sigma_A`/`\sigma_B` obstruction from v13.567/v13.569 remains unresolved rather than claiming this construction resolves it.

## 4. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.656 (this audit's own checkpoint) | provenance covers the relevant prior work | found incomplete — missed v13.560/562/563/567/569 | **self-reported gap, no propagated harm** |
| v13.657 | scalar `C_4=\langle iI_3\rangle` identified with cyclotomic `\mathcal Z^3` | independent re-derivation from raw multiplication | **PASS, exact** |
| v13.657 §5 | correction that `A\neq iI_3` (checkpoint wording was too strong) | independently confirmed `A^2\neq(iI_3)^2` | **correction verified accurate** |
| v13.658 | six-cycle carrier = full U(12) permutation action + V4 character decomposition | independent full computational reconstruction (not spot-check) | **PASS, exact** |

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `851f9a5`. No new commits landed while writing this entry. `git ls-tree` confirms v13.659 remains free.

## 6. Pointer for the next round

Per v13.657/v13.658's own stated next target (v13.656 priority 3, now re-scoped): test whether the shared six-cycle/U(12) carrier and the scalar-`C_4` bridge induce any genuine Pell or QR equivariance, explicitly allowed to return negative, and separately, whoever picks up the `\sigma_A`/`\sigma_B` disagreement (v13.567 vs v13.569) should treat it as the sharp open problem it is, not attempt to re-derive the six-cycle bridge again.
