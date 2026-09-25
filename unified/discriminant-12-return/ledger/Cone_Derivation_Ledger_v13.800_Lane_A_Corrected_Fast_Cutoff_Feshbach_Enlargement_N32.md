# Cone Derivation Ledger v13.800 — Lane A Corrected Fast-Cutoff Feshbach Enlargement Through N=32

Date: 2026-09-25

Lane: A.

Status: [N] corrected high-precision finite-section enlargement; [D] parity/sign convention inherited from v13.799; [G] protected dimension shown cutoff-dependent; [O] kappa_0 convergence and kappa_1 promotion remain open.

Parents: v13.797–799.

Research artifact:

- research-notes/suzuki_form_core_corrected_fast_cutoff.py
- commit 7d32cb07ad8400cb99f715e2198aeceaffd4fcad

No CI workflow or commit-status check is attached to that research commit; the calculations below were independently executed during this Lane A continuation using the same formulas.

## 0. Synchronization

Immediately before this ledger write, the live head was the research commit above, with v13.799 immediately below it. No competing v13.800+ ledger entry was present.

The purpose of this checkpoint is to continue the v13.798 protected-subspace source-resolvent gate after the v13.799 odd-pole correction, using compatible fast formulas in both parity channels.

## 1. Corrected parity builders

The even-v block uses odd Dirichlet indices and the source-faithful positive cosh pole channel

[
A_{m pole}^{(+)}=+2cc^T.
]

The odd-v block uses even Dirichlet indices and the corrected negative sinh pole channel

[
A_{m pole}^{(-)}=-2dd^T.
]

The odd non-pole Cauchy formulas are otherwise the archived source-faithful formulas. v13.799 established overlap with the current direct form to about (8.7	imes10^{-23}) entrywise through (N=16).

The source vector remains the analytic (lambda=0) Lane A source overlap used in v13.795–798.

## 2. First Schur parameter through N=32

At each even cutoff (N), define

[
E_{e,N}=f_e^T(A_N^{(+)})^{-1}f_e,
qquad
E_{o,N}=f_o^T(A_N^{(-)})^{-1}f_o,
]

and

[
kappa_{0,N}
=
rac{E_{e,N}-E_{o,N}}
{E_{e,N}+E_{o,N}}.
]

The corrected high-precision continuation gives

[
egin{array}{c|c}
N & kappa_{0,N}\
hline
18 & 0.9981634258231784889223\
20 & 0.9959431212804212882113\
22 & 0.9971160610440417681680\
24 & 0.9987372793730411261293\
26 & 0.9990349070278660678051\
28 & 0.9991646953989737916482\
30 & 0.9994186427865947104573\
32 & 0.9992230376149196805584
end{array}
]

For reference,

[
kappa_{0,infty}
approx
0.9968019520324009035289.
]

The (N=20) value happens to lie fairly near the target, but the subsequent sequence moves away again. Therefore there is still no monotone or numerically settled cutoff convergence.

The correct conclusion remains

[
oxed{
kappa_{0,N}	ext{ is not yet cutoff-stable through }N=32.
}
]

## 3. Lowest parity eigenvalues continue to collapse

At (N=32),

[
lambda_{min}(A_{32}^{(+)})
approx
7.1762110931	imes10^{-26},
]

[
lambda_{min}(A_{32}^{(-)})
approx
1.6285192018	imes10^{-23}.
]

The source-resolvent energies correspondingly reach roughly

[
E_{e,32}
approx
1.06931	imes10^{25},
qquad
E_{o,32}
approx
4.15569	imes10^{21}.
]

Thus the same source-coupled near-null mechanism identified in v13.798 persists and strengthens as the cutoff is increased.

## 4. Feshbach effective 10-core at N=32

To distinguish low protected geometry from the growing finite buffer, take a ten-dimensional low core in each parity sector and eliminate the remaining (N=32) modes by the exact finite Schur complement.

For the even-v effective core, the first levels are

[
egin{aligned}
&7.17621109312	imes10^{-26},\
&4.68282357060	imes10^{-20},\
&4.39883945855	imes10^{-15},\
&1.03931963248	imes10^{-10},\
&6.71959735666	imes10^{-7},\
&1.06872063732	imes10^{-3},\
&1.15999955256,ldots
end{aligned}
]

For the odd-v effective core,

[
egin{aligned}
&1.62851920175	imes10^{-23},\
&4.55540018216	imes10^{-18},\
&3.98939265910	imes10^{-13},\
&3.32725909787	imes10^{-9},\
&1.71474727214	imes10^{-5},\
&1.72676901707	imes10^{-2},\
&1.51646824479,ldots
end{aligned}
]

The Feshbach reduction therefore does exactly what is wanted structurally: the buffer is eliminated while the low near-null ladder remains visible in a fixed finite core.

## 5. The four-dimensional protected subspace is not cutoff-stable

At (N=16), v13.798 found a clear four-level near-null ladder followed by gaps of approximately

[
4.36	imes10^{-3}
quad	ext{(even-v)}
]

and

[
4.50	imes10^{-2}
quad	ext{(odd-v)}.
]

At (N=32), the effective-core spectra now contain a fifth very small level,

[
6.72	imes10^{-7}
quad	ext{(even-v)}
]

and

[
1.71	imes10^{-5}
quad	ext{(odd-v)},
]

before the next levels reach approximately

[
1.07	imes10^{-3}
quad	ext{and}quad
1.73	imes10^{-2}.
]

Therefore

[
oxed{
	ext{the protected dimension inferred at }N=16	ext{ is not invariant under cutoff enlargement.}
}
]

This is the central new numerical fact of the present gate.

The correct object to track is not a frozen list of four raw finite-section eigenvectors. It is the cutoff-dependent protected subspace of the Feshbach effective core, including the dressing produced by elimination of the growing buffer.

## 6. Consequence for the proposed strategy

The v13.798 plan to freeze four protected directions and simply enlarge the complement is too rigid.

The updated protected-subspace strategy is:

1. keep a fixed low Feshbach core of sufficient dimension, presently ten modes per parity;
2. enlarge only the buffer;
3. recompute the effective Schur matrix on that fixed core;
4. identify its low protected spectral cluster by a gap criterion rather than by a hard-coded dimension four;
5. transport source coordinates through the same Schur elimination;
6. evaluate (E_e,E_o,kappa_0) from the dressed effective system;
7. track the rank of the protected cluster as a function of cutoff.

This preserves the useful Feshbach architecture without assuming that the near-null rank is already asymptotically frozen.

## 7. kappa_1 remains blocked

The present calculation improves the fixed-cutoff linear algebra and exposes the moving protected cluster, but it does not establish cutoff convergence of (kappa_0).

Therefore the v13.797/v13.798 discipline remains in force:

[
oxed{
	ext{do not promote a new }kappa_{1,1}	ext{ value yet.}
}
]

Any second-stage moment solve would amplify a first-stage object that is still visibly changing with cutoff.

## 8. Next gate

The next Lane A computation should now be a genuine fixed-core / growing-buffer Feshbach study.

Recommended concrete target:

- core dimension: 10 per parity, as used above;
- buffer cutoffs: increase beyond 32 with the corrected fast builders;
- at each cutoff record:
  - effective-core eigenvalues;
  - spectral gap ratios defining the protected cluster;
  - source coordinates in the effective core;
  - complement positivity/gap;
  - (E_e,E_o,kappa_0);
  - principal angles between successive protected effective-core subspaces.

The key question is now whether the protected cluster dimension eventually stabilizes and whether the corresponding effective source quadratic forms converge.

Only after that occurs should weighted moments and (kappa_1) be revisited.

## Result

[
oxed{
kappa_{0,32}
approx
0.9992230376149196805584,
}
]

with no cutoff-convergence claim.

[
oxed{
	extbf{The N=16 four-direction protected picture is not cutoff-stable; at N=32 a fifth near-null effective-core direction has entered both parity ladders.}
}
]

[
oxed{
	extbf{The correct continuation is a fixed low Feshbach core with a growing buffer and a dynamically identified protected cluster.}
}
]
