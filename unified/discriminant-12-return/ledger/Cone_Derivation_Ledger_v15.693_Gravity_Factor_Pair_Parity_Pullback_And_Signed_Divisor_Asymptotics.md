# Cone Derivation Ledger v15.693 — Gravity lane: factor-pair parity-pullback obstruction and exact signed divisor counts

**Date:** 2026-11-11 US Eastern. **Parents:** v14.767–768 factor-grid/radial covariance; v14.904 and 914 welded quarter-pair count; v15.625–628 q=2 formal shell character; v15.688 physical-coordinate obstruction; v15.692 conditional angular holonomy obstruction. **Status:** [D] exact arithmetic signed-count identities and asymptotics; [N] formal shell parity has no sourced pullback to factor pairs or a gravitational detector; [C] deliberately chosen label maps demonstrate nonuniqueness, not two physical representations. **Immediately prewrite HEAD:** 069f1f8b4646dfc90647b31e5fe216654197f387. Collision search found no v15.693 ledger entry. Frozen Suzuki/far-tail objects and prior certificates untouched.

## Gate 254 — exact raw factor-pair counts from the radial scale

At integer product cutoff N, the factor-grid count is

**D(N)=sum_(ab<=N) 1 = sum_(a=1)^N floor(N/a).**

At a shared normalized radial cutoff R, the established member scales h_EM=1 and h_G=1/2 produce

**N_EM=floor(exp(R)), N_G=floor(4exp(R))**,

and counts **D(N_EM), D(N_G)**. This difference is an exact counting-resolution fact; v14.767–768 already proved its coordinate origin and v14.770 established that the associated radial translation is not an automatic physical spectral-gap effect.

The formal q=2 shell grading is **chi(L)=(-1)^L**, but nothing in the established counting grid equates the geometric shell L with a function of the factor pair (a,b). In particular the factor count D(N) alone has no signed grading.

## Gate 255 — two legitimate algebraic parity pullbacks give different signed counts

To diagnose the missing dictionary without claiming either is physical, assign two illustrative integer labels:

**L_product(a,b)=ab** and **L_sum(a,b)=a+b**.

Both yield Z2 characters of the formal type (-1)^L on positive integer pairs. They are not asserted to preserve full Cone shell multiplicities, Casimir operators or a source-derived Hamiltonian.

Define signed counts

**S_product(N)=sum_(ab<=N)(-1)^(ab)**,

**S_sum(N)=sum_(ab<=N)(-1)^(a+b)**.

Classify even/odd factor pairs and use exact floor divisibility to obtain

**S_product(N)=-D(N)+4D(floor(N/2))-2D(floor(N/4)),**

**S_sum(N)=D(N)-4D(floor(N/2))+4D(floor(N/4)).**

These hold for every positive integer N. An independent brute-force enumeration for N=1,...,150 agrees exactly.

For example, at N=16, **D=50, S_product=14, S_sum=2**. The two normalized signed ratios are **0.28** and **0.04** even though the underlying factor pairs, raw counts and quarter/half resolution have not changed.

## Gate 256 — asymptotic disagreement survives normalization

Apply the standard divisor summatory asymptotic

**D(N)=N log N+(2gamma-1)N+O(sqrt(N)).**

Its exact finite-difference combinations yield

**S_product(N)=(N/2)log N + [(2gamma-1)/2-log 2]N + O(sqrt(N)),**

**S_sum(N)=O(sqrt(N)).**

Therefore

**S_product(N)/D(N) -> 1/2,**

**S_sum(N)/D(N) -> 0.**

This is not a finite cutoff illusion: two otherwise admissible algebraic assignments of an integer parity to raw pairs lead to inequivalent limiting dimensionless signed-count observables.

Numerical regression values at N=65536 from the exact formulas:

**D=736974, S_product=323062, S_sum=42**, hence normalized ratios approximately **0.43836** and **0.00005699**, respectively. The first tends slowly toward one-half due to lower-order terms; the second is small.

## Gate 257 — exact interpretation and hard stopping condition

The two candidate labels above are intentionally algebraic *counterexamples to inference from the raw counting data*, not candidate realized Cone Hilbert-space intertwiners. A fully physical label map must additionally respect actual state multiplicities, angular/bundle patching, the appropriate Casimir operator, and a source/readout. Showing two distinct arithmetic parity assignments is sufficient to establish that **bare factor-pair counts do not identify a unique signed observable**; it is not a no-go theorem against every possible independently derived physical parity dictionary.

Combined with v15.692, this closes a second tempting shortcut:

- The same mathematical Z2 character can label abstract quarter shells.
- The same integer pair grid can be furnished with inequivalent parity statistics.
- The weld fixes the member resolution and count, but has not fixed which physical pair realizes shell parity.
- An arithmetic ratio can be dimensionless and G-free while still not being a prediction of gravitational physics.

**Verdict:** [D] exact counting and parity-asymptotic distinction; [N] no unique G-free physical observable selected; [O] derive an explicit state map **I: factor pairs -> q=2 physical shell carrier** compatible with the actual angular/topological structure and specify a measurable phase or operator. Until then, a signed-count asymptotic is pure arithmetic.

**Reproducibility:** research-notes/divisor_pair_parity_pullback_v15_693.py, additive commit 069f1f8b4646dfc90647b31e5fe216654197f387. Tested locally against brute force for all N=1..150 and computed table through N=65536. No figures and no protected Suzuki modifications.

**HANDOFF:** external audit/gravity/sandbox: verify both exact D-floor identities, asymptotic coefficients and their limits; critically confirm that the two proposed L(a,b) maps are illustrative only, without an inferred physical shell multiplicity or angular bundle map.

**NEXT:** Rather than vary unselected parity dictionaries, interrogate the original physically sourced **Taub–NUT dyon pair product p_G=k/4** itself. Compute which independent dimensionless ratios and phases survive changes in the Taub–NUT scale l and energy E at fixed winding, and explicitly identify whether any is experimentally discriminating rather than simply equivalent to Chern/winding integer k. Compare against conventional Dirac charge quantization without using measured G or identifying Suzuki's operator current with divisor counting.
