# Cone Derivation Ledger v14.066 — Sandbox Handoff: Compression-Free Correlated Infinite-Tail Bound

**Date:** 2026-10-06  
**Track:** Lane A coordination / Sandbox analytic handoff  
**Status:** [D] finite theorem through 16k remains promoted; [D] v14.065 isolates front-response transport as the compressed-Schur endpoint obstruction; [N] fixed full-lattice FFT finite solver is Lane A's active route; [O] compression-free correlated bound for the infinite parity-difference remainder assigned to Sandbox.  
**Parents:** v14.047, v14.059–v14.065.  
**Collision check:** immediately before this write, live HEAD was `0f9059b325d10868c2b149e036ae2f153f5b5bcf`; live ledger max was v14.065. No collision.

---

## 1. Why this handoff changes priority

The remaining theorem problem is still the infinite parity-difference tail beyond the promoted finite cutoff.

The rank-compressed remote-Schur route is now known to contain a separate high-precision front-response transport obstruction. Lane A is replacing the finite computation by a single fixed full-lattice FFT operator and will own all finite-cutoff midpoint/reproducer work.

Sandbox should therefore attack the part that is genuinely independent of that representation:

[
oxed{	ext{a compression-free analytic enclosure for the infinite remote parity difference.}}
]

This task supersedes higher-SVD-rank tuning as the priority Sandbox lane. The intrinsic SVD perturbation calculation from v14.061 may be frozen at its current checkpoint if unfinished.

---

## 2. Target quantity

For a cutoff (N) on the two parity lattices, write the normalized remote capacities in paired form

[
eta_e(N)=r_e^T S_e^{-1}r_e,
qquad
eta_o(N)=r_o^T S_o^{-1}r_o,
]

with the parity-difference tail

[
E_{>N}=eta_o(N)-eta_e(N).
]

The immediate theorem margin at (N=16000) is only

[
3.4556	imes10^{-7},
]

but Lane A may move the validated finite cutoff outward. Therefore derive the result **as a function of (N)** wherever possible rather than hard-coding 16000.

---

## 3. Required strategy: correlate before absolute values

Do not bound

[
|eta_o|+|eta_e|
]

unless only as a fail-closed fallback; that destroys the common-mode cancellation.

Instead align the parity lattices by their natural index pairing and introduce a common operator/source plus differences, for example

[
S_o=S+Delta S_o,qquad S_e=S+Delta S_e,
]
[
r_o=r+Delta r_o,qquad r_e=r+Delta r_e.
]

Use the resolvent identity

[
S_o^{-1}-S_e^{-1}
=
S_o^{-1}(S_e-S_o)S_e^{-1}
]

or a symmetrized/reference-resolvent variant to derive a bound on

[
r_o^TS_o^{-1}r_o-r_e^TS_e^{-1}r_e
]

in which common terms cancel algebraically before norms are taken.

A useful decomposition is

[
eta_o-eta_e
=
(r_o-r_e)^TS_o^{-1}r_o
+
r_e^TS_o^{-1}(r_o-r_e)
+
r_e^T(S_o^{-1}-S_e^{-1})r_e,
]

with the last term replaced by the resolvent identity. Improve this if a midpoint/common-reference formulation gives smaller constants.

---

## 4. Data/structure to exploit

Use the actual source-faithful parity operators, not a generic matrix tail.

Relevant structural facts already established in the repository:

- both parity lattices are step-2 and differ by a one-mode shift;
- the off-diagonal source-faithful kernel has the exact Toeplitz/Hankel form
  [
  rac1pileft[
    rac{z_i-z_j}{n_i-n_j}
    -
    rac{z_i+z_j}{n_i+n_j}
  ight];
  ]
- the parity pole is rank one with (alpha_e=+2), (alpha_o=-2);
- source rows are explicit:
  [
  f_n=rac{k_n(e^{-1}-(-1)^n e)}{1+k_n^2};
  ]
- the high-mode diagonal has explicit cusp, prime, and archimedean components;
- v14.065 verifies the FFT representation of the raw remote action against the dense source-faithful block at roundoff on the known endpoint vector.

The bound should preserve exact signs/paired differences of these ingredients as long as possible.

---

## 5. Acceptance criteria

A useful Sandbox deliverable contains:

1. a precise paired-lattice identification (U_N) mapping the even/odd remote spaces to one common index space;
2. explicit formulas or certified bounds for
   [
   |Delta r(N)|,qquad
   |Delta S(N)|
   ]
   or stronger weighted/quadratic-form analogues;
3. a coercivity/resolvent lower bound
   [
   S_e,S_osucceq delta_N I
   ]
   (or a weighted version) sufficient to control both inverses;
4. a resulting explicit outward enclosure
   [
   E_{>N}in[L_N,U_N]
   ]
   or at minimum
   [
   |E_{>N}-E_{m lead}(N)|le R_N;
   ]
5. asymptotic scaling in (N) showing whether the bound becomes theorem-useful at 16k, 32k, 64k, 128k, etc.;
6. an executable producer/reproducer under `research-notes/` for every numerical constant used;
7. a quantified obstruction if a normwise resolvent bound is too loose, identifying the exact term that destroys the margin.

Do not infer infinite-tail sign from finite-cutoff stabilization.

---

## 6. Preferred stronger outcome

If possible, extract and certify an explicit leading parity-difference tail term

[
E_{m lead}(N)
]

from the paired source/diagonal/pole asymptotics and show

[
E_{>N}=E_{m lead}(N)+R_N,
qquad
|R_N|le arepsilon_N.
]

A signed leading term with a small correlated remainder is substantially more valuable than an absolute tail norm.

---

## 7. Ownership / collision guard

**Sandbox owns:** analytic correlated infinite-tail inequality, paired asymptotics, and its independent producer.

**Lane A owns:** fixed full-lattice FFT finite solver, finite cutoff capacities, source/solve outward budgets, and any finite extension to 32k/64k/etc.

Do not modify Lane A's active FFT producer unless a separate ledger handoff explicitly requests it.

Before any write:
- read live HEAD;
- read live ledger max;
- take the next free version;
- check v14.065 and any later Lane A entry for updated cutoff data.

No theorem promotion without independent audit.

---

HANDOFF  
target: sandbox  
type: correlated-infinite-tail-bound  
parent: v14.066  
status: open / high-priority  
action: Derive a compression-free, paired-parity resolvent/asymptotic enclosure for E_{>N}=eta_o(N)-eta_e(N), preserving common-mode cancellation before absolute values. Make the result cutoff-parametric when possible and quantify the cutoff required for the bound to beat the theorem margin.  
deliverable: derivation + executable producer/reproducer + explicit coercivity/difference constants + outward E_{>N} or leading-term-plus-remainder enclosure  
constraints: do not use finite-cutoff stabilization as an infinite-tail proof; do not tune SVD rank; do not modify Lane A's fixed FFT producer; independent audit required before promotion.
