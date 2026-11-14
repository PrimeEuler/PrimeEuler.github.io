# Cone Derivation Ledger v15.948 — Quarter parabola remainders encode D(2n) and a two-scale half-cell digit

**Date:** 2026-11-13 Eastern. **Track:** Gravity/legacy Cone arithmetic. **Parents:** original v13.690 §7 exact parabola half-offset reconstruction; v14.368 triangle/divisor partition; v15.932 half/quarter interleave; v15.943–944 hyperbola midpoint offsets and divisor contact sums; v15.947 return to exact T(n)=D(n)+A(n) in upper half-disk. **Audit:** Round 576, v15.945, verified v15.940–944 without mathematical corrections, flagged v15.940 numbering collision, which is repaired additively in v15.946. **Fresh HEAD prewrite:** 83bfe793f30cb4ce98d27a3ac3aae195739bc970 (new exact script); target v15.948 checked absent; no earlier files edited, Suzuki frozen/production untouched.

## Gate 722 — distinguish quarter *remainder* refinement from quarter divisor lattice

For integers n≥1, k=1..n, take original hyperbola/parabola displacement **v_k=(n−k²)/(2k)**. Its nonnegative fractional residue modulo 1/2 satisfies **2(v_k mod 1/2)={n/k}** (since k integral). The original identity is **B_half(n):=2Σ_(k≤n)(v_k mod 1/2)=nH_n−D(n)**, with D(n)=Σ floor(n/k) and H_n=Σ1/k. Here T(n)=n(n+1)/2 is the full triangular upper-half-disk *station count*, D(n) the actual product≤n hits and A(n)=T(n)−D(n) the misses. A quarter remainder is not a new integer-factor contact, and this construction does not move/scale the entire lattice.

Choose half-sized remainder cell: **B_quarter(n):=2Σ_(k≤n)(v_k mod 1/4)=(1/2)Σ_(k≤n){2n/k}**. The identity follows from 4v_k=2n/k−2k and does NOT assign an independent gravitational coupling or quarter Casimir operator.

## Gate 723 — exact binary digit and two-scale summatory divisor identity

For x=n/k, the elementary fractional part identity is **{x}−{2x}/2= floor(2{x})/2**, a binary half-cell digit. Hence

**B_half−B_quarter=E(n)/2**,

where **E(n):=# {1≤k≤n : {n/k}≥1/2}=Σ_(k≤n)[floor(2n/k)−2 floor(n/k)]**.

Now **Σ_(k≤n) floor(2n/k)=D(2n)−n**, because every integer row n<k≤2n contributes exactly 1. Therefore

**E(n)=D(2n)−2D(n)−n**, **E(n)≥0** integer.

Equivalently, this quarter remainder reconstructs the *doubled hyperbolic product cutoff* exactly:

**D(2n)=2nH_n+n−2B_quarter(n)
=2nH_n+n−4Σ_(k≤n)(v_k mod 1/4).**

This is the main new explicit bridge in the current sequence. The original half-offset gives D(n); the quarter-refined remainder with the SAME n parabola rows gives D(2n) together with the known n extra rows, and their difference counts the binary digit distribution. This is a re-expression of standard floor-sum identities, not independent arithmetic beyond D at n and 2n.

## Gate 724 — geometry, count values, selector status

The binary digit E(n) is the number of row indices k whose hyperbola height n/k lies at least halfway between consecutive integer grid rows. It partitions the original half-offset **remainder bands** into lower/upper subcells; it is NOT a partition into physically distinct gravity/EM points of the T(n) triangular integer-factor lattice. Each factor station continues to be counted exactly once by T(n), and the hit/miss partition T=D+A remains unchanged. The quarter grid creates additional nonintegral probe stations only if those are explicitly introduced as a new carrier. Interleaving a factor grid at physical scale u=1/2 and merely measuring fractions modulo 1/4 are mathematically distinct operations; comparing them requires an additional scale transport.

Sample triples (n,D(n),D(2n),E(n)): (3,5,14,1), (5,10,27,2), (6,14,35,1), (9,23,58,3), (12,35,84,2), (20,66,158,6), (30,111,261,9). No G, α, fitted source, physical clock, or gravitational response enters. Although E(n) tracks a nontrivial cross-scale distribution, the identity is classical arithmetic and holds for any hypothetical field interpretation; it does not select EM vs G sectors.

## Verification and next gate

**Reproducer:** `research-notes/k4_quarter_remainder_two_scale_divisor_v15_948.py`, commit **83bfe793f30cb4ce98d27a3ac3aae195739bc970**. Local exact Fraction checks over n=1..1000: original D(n) half remainder, refined D(2n), binary digit E(n), T(n)=D(n)+A(n) station partition, all PASS. **Independent Audit pending.**

**Next:** Without conflating remainder refinement with an actual physical quarter-factor lattice, test whether the two-scale E(n) admits a natural mirror-even/odd decomposition under (a,b)↔(b,a) when mapped into the full T(n) station set, and whether any such decomposition survives standard integer-floor algebra or gives a nontrivial sector-coupling prediction. Otherwise close the pure counting bridge; a genuinely physical operator must be sourced separately.

**HANDOFF Audit/Muse:** Verify the 2n vs n scaling exactly, the tail Σ_(k=n+1)^(2n) floor(2n/k)=n, the half-cell threshold for nonintegral rows, the T(n) stations vs quarter-probe distinction, and the precise meaning of the binary E(n) count.
