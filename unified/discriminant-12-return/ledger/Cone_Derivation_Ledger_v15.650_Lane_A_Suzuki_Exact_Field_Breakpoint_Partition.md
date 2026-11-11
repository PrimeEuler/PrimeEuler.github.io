# Cone Derivation Ledger v15.650 — Lane A Suzuki: exact finite x-partition and sparse breakpoint update geometry

**Date:** 2026-11-10. **Track:** Lane A original Suzuki five-frequency commutator in chosen counting-measure crossed-product representation. **Parents:** v15.420, v15.497–502, v15.643–645, v15.649. **Status:** [D] exact combinatorial field partition and uniform update-support bound; [N] exact integer replay R=1..6; [O] rigorously propagated uniform spectral norm upper certificate.

## Fresh pre-write state

Master HEAD immediately before additive witness was `b2800f84550a485ea5fa070c8db20479d6c221f2`. Witness committed separately at `0757ad2d9f7e340ce57d55490b4594275994061f`. The neighboring gravity lane's use of version v15.647 and earlier corrected Suzuki v15.648/649 are respected. This v15.650 file is additive and source/frozen payloads are untouched.

## 1. Exact four-corner coefficient identity

For each unordered q<r from Q={2,3,4,5,7}, signs sigma,tau=±1, and valid row h in F_R=[-R,R]^4 such that the column h-g remains in F_R, use the audited physical translation g=tau v_r-sigma v_q, where v2=e2,v3=e3,v4=2e2,v5=e5,v7=e7.

The v15.420 coefficient is G=(D_sigma(y;A)D_tau(y;B) + D_-tau(z;B)D_-sigma(z;A)), with y=x+h·L+sigma A, z=x+h·L-tau B, A=log q, B=log r, and period-two sawtooth s(u)=1-(u mod 2).

Define four lattice corners:

- c0=h;
- c1=h+sigma v_q;
- c2=h-tau v_r;
- c3=h+sigma v_q-tau v_r=h-g.

Writing a=s(x+c3·L), b=s(x+c1·L), c=s(x+c0·L), d=s(x+c2·L), **the exact coefficient is**

`G=(c-b)(a-b)+(c-d)(a-d)`.

Every individual sawtooth term has slope -1 between its period-two jumps, so all differences and G are **constant on any open interval not containing a cut of one of those four corners**. The v15.497 finite matrix field is therefore literally piecewise constant in x—not merely approximable by piecewise-constant samples.

## 2. Exact finite candidate cut set

For R>=1, as q,r,sigma,tau,h range over valid matrix entries, the union of their four integer corners is exactly

`K_R={ (k2,k3,k5,k7) in Z^4 : -R-1<=k2<=R+1, and -R<=k3,k5,k7<=R }`.

Proof (inclusion): every pair except (2,4) uses independent coordinate axes for v_q and v_r. When both endpoints h and c3=h-g lie inside F_R, c1 and c2 share each coordinate with one of the endpoints, hence stay inside F_R. For (q,r)=(2,4), only the first coordinate moves. Its four values are n, n+sigma, n-2tau, n+sigma-2tau; if both n and n+sigma-2tau belong to [-R,R], the two intermediate coordinates lie within [-R-1,R+1]. Other three coordinates remain those of h, in [-R,R].

Proof (surjectivity): every h in F_R can serve as c0 for a valid pair (3,5) by choosing signs that shift its 3- and 5-coordinates inward, which is possible for R>=1. Every extra corner with first coordinate R+1 arises from h2=R, q=2,r=4,sigma=tau=+1, where c1 has first coordinate R+1 and c3 has first coordinate R-1; likewise -R-1 arises by sigma=tau=-1, h2=-R. The other three coordinates are unconstrained inside the box. No other corners occur.

Therefore

`|K_R|=(2R+3)(2R+1)^3`.

At R=16 the number is **1,257,795**. This is an exact number of distinct *candidate sawtooth cut labels*, not a claim that every cut produces a nonzero matrix entry jump.

The candidate breakpoint on the parameter circle x mod 2 indexed by k is `x=-k·L (mod 2)`, with `L=(log2,log3,log5,log7)`. All such points are **distinct modulo 2**: a collision for k!=k' would imply a nontrivial rational product of prime powers equals `e^{2m}` for some integer m. If m=0 prime factorization forces k=k'; for m!=0 Hermite–Lindemann makes `e^{2m}` transcendental, impossible. Hence these |K_R| cuts partition the parameter circle into exactly |K_R| open arcs; every finite-field matrix B_R(x) is constant on each arc. Some arcs may have identical matrices due to cancellation; they are a guaranteed exhaustive partition.

## 3. Uniform sparse update at each cut

For a fixed cut label k, any affected physical word must contain k as one of its four corners. For each of the 40 signed support words and each of the four possible corner positions, the row h is determined uniquely by k. Hence **at most 160 directed sparse matrix entries change** when the parameter crosses any one candidate cut, independently of R. The difference between adjacent field matrices has rank at most 160 (sum of at most 160 rank-one matrix-unit terms). This is a bound on UPDATE SUPPORT, not on the magnitude of the spectral norm change; rank 160 alone does not certify a small perturbation.

## 4. Replay, resource implications, and next step

Exact integer script `research-notes/lane_a_v15_650_exact_corner_breakpoint_census.py`, commit `0757ad2d9f7e340ce57d55490b4594275994061f`, enumerates all source-faithful valid edges for radii 1 through 6 and verifies **set equality**, not just the counts, with the formula for K_R. Observed counts (R, sites, directed nonzeros, candidate cuts, max entries per cut):

- R=1: (81, 1188, 135, 100);
- R=2: (625, 14700, 875, 156);
- R=3: (2401, 66836, 3087, 160);
- R=4: (6561, 199260, 8019, 160);
- R=5: (14641, 468996, 17303, 160);
- R=6: (28561, 948428, 32955, 160).

Thus R=16 requires ~1.26 million interval states, not an unstructured search over a continuum. Exact sorted cuts and adjacency can be generated once. A feasible **candidate** is to propagate a rigorous spectral enclosure across these cuts using certified sparse low-rank updates and occasional fully certified anchor factorizations/positive-polynomial bounds. It is not yet shown that low-rank updates can be aggregated affordably or that they meet the threshold.

**Acceptance gate unchanged:** rigorously enclose `C_16=ess sup_x||B_{F16}(x)||<4.10` (both spectral signs, all arcs). Together with independent verification of corrected v15.645 `E_16<0.142`, audited v15.499 would imply `||X||<4.242`, below the five-frequency cross budget 4.24903015. No norm pass is presently claimed.

Protected unchanged original Suzuki seed, C_S_32000, thresholds 3e-5 and .002, v14.405/406 scoped PASS, v14.814 later far FAIL, exactly-once transport/charge and frozen hashes. Noncanonical chosen ell2, full-K transfer inconclusive, no source-native Phi, physical coupling, whole-residual, stationary or capacity claim.
