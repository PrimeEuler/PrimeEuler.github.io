# Cone Derivation Ledger v15.573 — Lane A: AM–GM factor-zero alignment explains quarter-shell open ladders

Date: 2026-11-09. Parents: v13.583, v15.140, v15.143, v15.279, v15.572. Status **[D] exact algebraic reformulation of the established representation-boundary theorem**; **[Audit]** no new physical SU(2), gravity constant or carrier mapping. Live prewrite HEAD d9bd1f5e264f8036feccb72a23ca9e6b6cdb55e0. Collision search found no existing v15.573. Additive, no Suzuki/far-tail changes.

## 1. User's AM/GM insight: means encode shell and offset; products encode transitions

For J_+ at magnetic coordinate m in shell j, define a=j-m and b=j+m+1. Then

AM=(a+b)/2=j+1/2=:R,
X=(b-a)/2=m+1/2,
GM=sqrt(ab)=sqrt((j-m)(j+m+1)),

so GM^2=R^2-X^2. An upward transition has zero amplitude exactly when a=0 (m=j, X=R) or b=0 (m=-j-1, X=-R). A lowering transition has its corresponding upper/lower zero factors. These are boundary factor zeros of the nonnegative AM–GM cone, not generally positive interior factor pairs.

On the *refined* quarter-grid m_i=-j+i/2 with i=0,...,4j, the original J_+ increases m by 1, i.e. changes i by 2; therefore the parity class i mod2 is preserved. The lower extreme state -j has index 0; the upper extreme +j has index 4j. The zero-factor endpoints can be reached by one ladder chain iff 4j is even, equivalently 2j is an integer. For odd-quarter j=(2n-1)/4, 4j is odd: zero-factor endpoints occupy different parity chains and neither chain reaches both. This is the exact v15.140 closure criterion re-derived purely as an AM–GM factor-zero alignment test plus mesh/step parity, **not a newly independent theorem**.

## 2. Universal missing-zero distance and escape weight

For an odd-quarter shell, the upward-open chain's topmost retained state has m=j-1/2, so its transition center is X=m+1/2=j, half a unit below the factor-zero center R=j+1/2. Its AM–GM factors are

a=R-X=1/2, b=R+X=2j+1/2.

The squared amplitude of the omitted outgoing transition is exactly

ab=(1/2)(2j+1/2)=j+1/4,

agreeing with the universal boundary escape weight of v15.140 and the D/E formulas of v15.572. Lower-open chain is its mirror using J_-; its missing factor is also 1/2. Thus the word "offset" has a literal meaning: the endpoint misses the required factor zero by **one half-unit in factor/transition-center coordinate**. It is not that the AM is zero: R remains positive; rather **one of the two factors fails to reach zero**.

## 3. Exact spot checks

j=1/4: 2 nodes, 0 closed chains, missing-outward amplitude squared=1/2.
j=1/2: 3 nodes, one closed chain, plus the known open isolated refined fragment.
j=3/4: 4 nodes, 0 closed chains, missing-outward amplitude squared=1.
j=1: 5 nodes, one closed chain plus one open refined fragment.
j=5/4: 6 nodes, 0 closed chains, missing-outward amplitude squared=3/2.
j=3/2: 7 nodes, one closed chain plus one open refined fragment.
j=7/4: 8 nodes, 0 closed chains, missing-outward amplitude squared=2.
j=2: 9 nodes, one closed chain plus one open refined fragment.

Rational arithmetic independently tested all rows. The algebra proves the result for every allowed j in (1/4)Z>=0.

## 4. Essential distinctions

- AM–GM factorization encodes the original ladder transition weight, but **AM–GM alone does not choose** the refined mesh or the J_+ step; both are inputs from the audited cone/SU(2) construction. Once fixed, nonclosure is forced without arbitrary cutoff.
- No new Lie group SU(2) is derived. Open odd-quarter fragments have nonzero [J_+,J_-]-2J_z boundary defect and cannot be full unitary SU(2) irreducibles. v15.572 provides the exact boundary operators D and E.
- This explains arithmetic/geometric offset nonalignment; it does not yet select a physical gravitational state space or map odd quarters to the bicone/Suzuki operator.

## Next discriminating gate

Derive an AM–GM/factor-coordinate definition of a half-step bridge interchanging the two parity chains and check its adjoint, positivity, involution/closure, and commutators against the defective J operators without adding a chosen boundary projection. Test j=3/4,5/4 and arbitrary odd quarters; do not silently replace the original step-1 J operator by a different SU(2) ladder.

HANDOFF target: external-audit; type: factor-zero/offset-parity alignment; status: open; action: verify zero-factor endpoint criterion iff 4j even, universal a=1/2 and escape amplitude j+1/4, and the distinction between an AM–GM identity and the independently selected mesh/step. No production writes.
