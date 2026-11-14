# Cone Derivation Ledger v15.944 — Actual divisor-contact sums of quarter-interleaved hyperbola offsets and the global n+1 diameter deficit

**Date:** 2026-11-13 Eastern. **Lane:** Gravity / factor lattice. **Parents:** v14.767 power/map and scale covariance; `research-notes/Gravity_Shifted_Divisor_Hyperbola_Seats.md` (distinct translated-lattice count); v15.625 formal Casimir residue families; v15.932 quarter rows on fixed-diameter transition circles; v15.943 fixed-product hyperbola interleaving and Casimir midpoint -1/16; v15.942 negative physical Taub–NUT/angular bridge. **Prewrite HEAD:** f6b8fe55a67d09bfccb01f2e0f61ee589645b0a0 (reproducer). v15.944 target checked absent. Additive-only, Audit/Sandbox/Suzuki/frozen objects untouched.

**User's authorization:** Sum the v15.943 normalized quarter-row offsets over *actual integer factor contacts*, compare with the established d(n), D(N) counts and global n+1 endpoint transition diameter, check nontrivial arithmetic beyond these data.

**Status:** [D] exact finite divisor-sum identities and 1..1000 integer verification; [D] geometric prime-vs-composite diameter-deficit criterion, equivalent to elementary divisor inequality; [N] new independent arithmetic information or physical EM/G quarter selector; [O] physical action assigning measurement weight to each contact and a distinguishing gravitational response.

## Gate 718 — divisor contacts are not the full continuum of quarter-row intersections

Hold **xy=n>0** on a fixed-product factor hyperbola. The original integer lattice contacts are **(n/k,k), k|n**, with (d(n)) ordered contacts and diameter (D_n(k)=k+n/k). The original factor-row parabola at k has secant coordinate (X_n(k)=(n-k²)/(2k)), and the interleaved geometric half-row at k+1/2 has exact midpoint X-defect

**δ_n(k)=X_n(k+1/2)−[X_n(k)+X_n(k+1)]/2=−n/[4k(k+1)(2k+1)].**

A half-integer row is NOT itself an additional integer factor contact. Restricting **the reference row k** to divisors of n is a choice that samples the local continuous interleave relative to genuine EM contacts, not a new shifted-quarter arithmetic lattice. In particular it must not be confused with the previously studied translated congruence-class seats a=1/4 or a=1/2.

## Gate 719 — normalized global sum is exactly n times d(n)

Define the normalized global offset

**A(n)=−4Σ_(k|n) k(k+1)(2k+1) δ_n(k).**

Every summand is exactly n, so **A(n)=n d(n)**. Thus A(n)/n=d(n), and **Σ_(1≤n≤N) A(n)/n=D(N)** is the original summatory divisor function. This is an exact *geometric realization* of d and D from the quarter interleave; it is not new arithmetic beyond the set of divisors.

Without the k-dependent correction, the raw offset sum is a distinct but completely determined rational divisor transform:

**S(n)=Σ_(k|n) δ_n(k)=−(n/4) Σ_(k|n) [k(k+1)(2k+1)]⁻¹**.

The kernel has the exact partial-fraction decomposition **1/[k(k+1)(2k+1)]=1/k+1/(k+1)−4/(2k+1)**. This S(n) generally does not equal a multiple of d(n) alone; it encodes factor sizes through a fixed arithmetic weight. It introduces no independent physical quarter-sector input.

An exact cutoff rearrangement is

**Σ_(n≤N) S(n)=−Σ_(k≤N) floor(N/k)[floor(N/k)+1]/[8(k+1)(2k+1)].**

This follows by writing n=mk and summing m over 1..floor(N/k). The usual divisor hyperbola / floor-sum machinery evaluates it directly. The structure is an arithmetic convolution, not a new physical frequency or fundamental interaction.

## Gate 720 — global n+1 endpoint diameter deficit and primality

Unlike the *fixed-diameter* circle slice, the fixed-product hyperbola's contact diameter D_n(k) is not constant. The endpoint factors (n,1), (1,n) have **D=n+1**. Every *proper interior* factor 1<k<n has **D_n(k)<n+1**, since

**(n+1)−D_n(k)=(k−1)(n−k)/k>0.**

Sum this nonnegative deficit across all integer divisor contacts:

**G(n)=Σ_(k|n)[(n+1)−(k+n/k)]
=(n+1)d(n)−2σ₁(n)**,

because Σ_(k|n)k=Σ_(k|n)n/k=σ₁(n). For all integers n≥2,

**G(n)=0 iff n is prime; G(n)>0 iff n is composite**,

with special case G(1)=0. The proof is elementary: primes have only the endpoints; composites contribute at least one strictly positive interior divisor, while endpoints contribute zero.

Examples: n=2 d=2,σ=3,G=0; n=4 d=3,σ=7,G=1; n=6 d=4,σ=12,G=4; n=9 d=3,σ=13,G=4; n=12 d=6,σ=28,G=22; n=60 d=12,σ=168,G=396. This is a useful **geometrically transparent global interior-contact discriminator**, but algebraically it is the standard σ/d divisor data, not a novel test of primality independent of divisor enumeration.

## Gate 721 — structural role of the formal Casimir midpoint and scale

v15.943 proved the purely geometric fixed polynomial `C(j)=j(j+1)` has midpoint defect **ΔC=−1/16** on the odd-quarter interleaved shell, and **δ_n(k)=[4n/(k(k+1)(2k+1))] ΔC**. Therefore the global normalized sum reweights the same constant geometric curvature at every divisor contact. This explains why the normalized global count returns n d(n) *without* assigning the odd-quarter geometry its own gravitational operator or transition amplitude.

The physical factor scale u changes secant offsets by u, while dimensionless A(n) requires dividing out u. Neither the raw nor normalized sum selects u=1/2 over u=1 or identifies it with G; similarly the diameter deficit scales as u and its dimensionless normalization is fixed by u, not by an independent field. The half-interleaved parabola never becomes a separate physical divisor contact simply by drawing it between integer contacts. The distinct q2 formal odd-quarter Casimir is preserved; no SU2 or gravitational Casimir equality is assumed.

## Reproducibility and frontier

**Reproducer:** `research-notes/k4_divisor_contact_interleave_global_gap_v15_944.py`, additive commit **f6b8fe55a67d09bfccb01f2e0f61ee589645b0a0**. Actually executed locally with exact SymPy: for all **n=1..1000**, verifies contact-offset weight A(n)=nd(n), diameter deficit G(n)=(n+1)d(n)−2σ(n), and G(n)=0 iff prime (apart from n=1); verifies exact S(n) identity and sign; tests summatory rearrangement for N=1,2,4,10,20,50,100. All PASS. Independent Audit pending.

**Verdict:** The user's global n+1 geometric idea is exact and, upon *actual divisor contact restriction*, yields two complementary global quantities: normalized curvature returns n·d(n), while the endpoint-circle diameter deficit returns (n+1)d(n)−2σ(n), vanishing precisely for primes. This is a genuine new *representation within Cone geometry* of familiar arithmetic, not a derived physical gravity/EM observable or arithmetic information beyond the divisor set.

**NEXT:** Examine whether the *geometry itself* or a physically sourced action assigns a nontrivial parity/coset weight to the interleaved half rows, instead of imposing one. Until then, parity-weighting or a Dirichlet character would be additional assumptions and likely repackage ordinary congruence-restricted divisor sums. Also assess whether any global variational functional involving G(n) produces a non-tautological selector of mesh u; report null and stop if only homogeneous scale covariance remains.

**HANDOFF Audit/Muse:** Independently verify 1..1000 integer tests, especially G(1)=0 exception, difference between real hyperbola row k+1/2 and actual integer contact, `σ(n)` multiplicity convention, floor-sum formula, and the lack of a physical sector selector.
