# Cone Derivation Ledger v13.798 — Lane A Protected-Subspace/Feshbach Source-Resolvent Evaluation at a=1, lambda=0

Date: 2026-09-25

Lane: A.

Status: [N] protected numerical gate completed through N=16; [D] exact finite-dimensional Feshbach identity used; [G] source/domain guardrails from v13.784–797 preserved; [C] next gate identified.

Parents: v13.795–797, especially v13.797 §13.

Research artifact:

- research-notes/suzuki_form_core_protected_resolvent.py
- commit da767855076603870705d65f4795fe9e2fadf81a

## 0. Collision/provenance check

Before writing new code, the live head was checked and remained v13.797.  The protected-subspace machinery named by the handoff was inspected first.

The following older artifacts contain reusable algebra but are **not** directly reusable as numerical payloads for the present source-resolvent problem:

- suzuki_active_core_feshbach_basis.py
- suzuki_feshbach_buffer_anatomy.py
- suzuki_hybrid_finite_feshbach_low_core.py
- suzuki_rank4_streaming_inverse_residual_contract.py
- suzuki_residual_certified_schur_solve.py
- suzuki_two_sided_inverse_factor_bound.py
- suzuki_rational_77x6_full_tail_protected_subspace.py

Compatibility result:

1. The Schur/Feshbach elimination identity and residual-to-Schur-error logic are reusable.
2. The old active-core and fixed 77x6 protected bases are tied to the earlier **even-v / odd-mode** sector and different truncation/certificate targets.
3. The rank-four streaming inverse work is tied to a shifted high-complement problem, including the 0.22 shift, and is not the present lambda=0 source solve.
4. The current gate needs **both** parity blocks and the analytic source vectors from the source-faithful form-core Galerkin problem.

Therefore no old protected basis was imported blindly.

## 1. Current source-faithful finite problem

At

[
a=1,qquad lambda=0,
]

use the audited direct Dirichlet form matrix from

[
	exttt{suzuki_componentwise_high_precision_audit.py}
]

and the analytic source overlaps from

[
	exttt{suzuki_form_core_schur_parameter_diagnostic.py}.
]

For each parity block (B),

[
E=f^T B^{-1}f
]

is evaluated.

No endpoint condition is imposed on the deficiency vector.  No raw first-kind Fredholm operator is inverted.  No identification (ar Dv=iv') is used.

The lambda=0 results remain finite-a diagnostics only.

## 2. Frozen numerical payload

A maximum cutoff

[
N=16
]

was assembled at 70 decimal digits.  A canonical row-major serialization at 60 significant decimal digits was frozen by SHA-256.

Full matrix:

[
oxed{
mathrm{SHA256}(A_{16})
=
	exttt{d48c064ba483dc79225764be0be7ba4aa6102640e9a05eedd0c9f5549a8b9839}.
}
]

Full source:

[
oxed{
mathrm{SHA256}(f_{16})
=
	exttt{1be3f5f7ed32a38e26028dafed44e25cae920f0f983a335ea50671544203f03d}.
}
]

Even-v parity block/source:

[
oxed{
mathrm{SHA256}(A_{16}^{(+)})
=
	exttt{de2bde77f9359b7221beb52d46b1c1ef66dc52b80b938bb269bb45a66c0157d2},
}
]

[
oxed{
mathrm{SHA256}(f_{16}^{(+)})
=
	exttt{65acc73c73598a62f98e8ba036fe9e3a84d68359e913f572fe5fe2d8334e50df}.
}
]

Odd-v parity block/source:

[
oxed{
mathrm{SHA256}(A_{16}^{(-)})
=
	exttt{f870cfca7b37583c65d4f70cb057735eb8ae6fb5daa35af6772041910e7a390b},
}
]

[
oxed{
mathrm{SHA256}(f_{16}^{(-)})
=
	exttt{e2b3afe3303ca1386e96c6aea18c0db9151cecbbcab18c64267d5e8788527e38}.
}
]

These hashes freeze the numerical payload actually used; they are not a claim that the underlying transcendental matrix entries are exact rationals.

An independent 80-digit N=12 assembly and the upper-left N=12 block of the 70-digit N=16 assembly agreed entrywise to

[
oxed{
max_{i,j}|A_{12}^{(80)}-A_{16}^{(70)}[1{:}12,1{:}12]|
approx 2.04	imes10^{-71}.
}
]

Thus the reported N<=12 values are not an assembly-precision artifact.

## 3. Protected spectral anatomy

At N=16 the parity spectra begin:

Even-v:

[
egin{aligned}
&8.3157917492	imes10^{-19},\
&1.2130768789	imes10^{-13},\
&2.5193725310	imes10^{-9},\
&6.9480962277	imes10^{-6},\
&4.3565736619	imes10^{-3},\
&1.0066201058,ldots
end{aligned}
]

Odd-v:

[
egin{aligned}
&1.2111203833	imes10^{-16},\
&7.3737588303	imes10^{-12},\
&4.7080022325	imes10^{-8},\
&6.6577758335	imes10^{-5},\
&4.4992024471	imes10^{-2},\
&1.5499893330,ldots
end{aligned}
]

Therefore both parity blocks display a clear **four-level near-null ladder** before the first substantial gap.

This is compatible with the earlier even-sector Feshbach anatomy, which also isolated a four-dimensional active near-null core, but the present result is independently reconstructed from the current source-faithful form matrix and now occurs in both parity channels.

## 4. Exact finite-dimensional Feshbach evaluation

Let (P) be the span of the first (r) eigenvectors of the N=12 parity block, embedded in the N=16 parity block.  Let (Q) span its orthogonal complement.

Define

[
S
=
P^TBP
-
P^TBQ,(Q^TBQ)^{-1}Q^TBP,
]

and

[
g
=
P^Tf
-
P^TBQ,(Q^TBQ)^{-1}Q^Tf.
]

Then exactly in finite dimension,

[
oxed{
f^TB^{-1}f
=
f_Q^T(Q^TBQ)^{-1}f_Q
+
g^TS^{-1}g.
}
]

The protected-dimension scan shows why (r=4) is the first natural protected size.

For the even-v block, the complement gap is approximately

[
egin{array}{c|ccccc}
r & 1 & 2 & 3 & 4 & 5\
hline
gamma_C &
1.21	imes10^{-13} &
2.50	imes10^{-9} &
6.82	imes10^{-6} &
3.93	imes10^{-3} &
9.79	imes10^{-1}
end{array}
]

For the odd-v block,

[
egin{array}{c|ccccc}
r & 1 & 2 & 3 & 4 & 5\
hline
gamma_C &
7.36	imes10^{-12} &
4.69	imes10^{-8} &
6.44	imes10^{-5} &
4.20	imes10^{-2} &
1.40
end{array}
]

Thus protecting four directions removes the entire visible near-null ladder and leaves a genuinely stiff complement.

At (r=4), the N=12-to-N=16 embedded protected basis has nonzero coupling to the new complement,

[
|A_{PC}|_Fapprox 2.60	imes10^{-2}
]

in the even channel and

[
|A_{PC}|_Fapprox 3.19	imes10^{-2}
]

in the odd channel, so this is a nontrivial Feshbach reduction rather than merely diagonalizing N=16 and declaring the cross block zero.

The protected/Feshbach and full spectral quadratic forms agree relatively to approximately

[
oxed{
1.5	imes10^{-65}quad	ext{(even)}
}
]

and

[
oxed{
1.8	imes10^{-67}quad	ext{(odd)}.
}
]

## 5. Source-resolvent quadratic forms and first Schur parameter

At N=16,

[
oxed{
E_{e,16}
approx
9.88105202101156878	imes10^{17},
}
]

[
oxed{
E_{o,16}
approx
6.64502527901586881	imes10^{14}.
}
]

The lowest protected mode contributes

[
oxed{
99.999567% 	ext{of }E_{e,16}
}
]

and

[
oxed{
99.997165% 	ext{of }E_{o,16}.
}
]

Therefore the source vector couples strongly to the lowest near-null directions.  The large quadratic forms are not produced by an unstable dense inverse; they are the resolved consequence of that coupling.

The resulting first Schur parameter is

[
oxed{
kappa_{0,16}
=
0.9986559003076436730382ldots
}
]

The cutoff sequence is

[
egin{array}{c|c}
N & kappa_{0,N}\
hline
4 & 0.99820062872003903161\
6 & 0.99954753083354612292\
8 & 0.99734803602012615745\
10 & 0.96783862780471321268\
12 & 0.99389585322145076917\
14 & 0.99769745662762483588\
16 & 0.99865590030764367304
end{array}
]

This is **not monotone** and is not yet a convergence certificate.

Relative to the infinite target

[
kappa_{0,infty}
approx
0.99680195203240090353,
]

the last three finite differences are

[
kappa_{0,12}-kappa_{0,infty}
approx
-2.90610	imes10^{-3},
]

[
kappa_{0,14}-kappa_{0,infty}
approx
+8.95505	imes10^{-4},
]

[
kappa_{0,16}-kappa_{0,infty}
approx
+1.85395	imes10^{-3}.
]

No convergence claim is made from these three values.

## 6. Precision dependence

The frozen N=16 payload was rounded to different significant-digit levels before repeating the spectral quadratic-form evaluation.

For (kappa_{0,16}):

[
egin{array}{c|c}
	ext{payload digits} & kappa_{0,16}\
hline
20 & 0.99865589163353554375\
25 & 0.99865590030746531912\
30 & 0.99865590030764367274\
35 & 0.99865590030764367304\
40+ & 0.99865590030764367304
end{array}
]

Thus the fixed-cutoff N=16 value is numerically stable once the matrix/source payload is carried at adequate precision, despite

[
kappa(A_{16}^{(+)})approx2.55	imes10^{18},
qquad
kappa(A_{16}^{(-)})approx2.07	imes10^{16}.
]

The high-precision reconstructed solve residuals remain around the (10^{-65}) scale at N=16.

Therefore the present obstacle is **cutoff evolution of the near-null protected spectrum**, not failure to solve a fixed finite section.

## 7. Consequence for kappa_1

v13.797 required that (kappa_{1,a}) be trusted only after the first protected solve is stable.

The first protected solve is now stable with respect to:

- algebraic method (full spectral vs. Feshbach),
- arithmetic precision,
- matrix-assembly precision through N=12,
- residual size.

But (kappa_{0,N}) is still visibly cutoff-sensitive.

Therefore the disciplined conclusion is:

[
oxed{
	ext{do not promote a new } kappa_{1,1}	ext{ value yet.}
}
]

Computing a higher Schur stage before controlling the cutoff motion of the protected near-null ladder would amplify exactly the unstable quantity the protected calculation has now isolated.

## 8. Updated diagnosis

The v13.795/v13.797 phrase “near-null conditioning barrier” can now be sharpened.

At fixed cutoff, sufficiently high precision resolves the inverse action cleanly.

The actual active issue is

[
oxed{
	ext{a cutoff-dependent four-dimensional near-null ladder carrying essentially all source-resolvent energy.}
}
]

This is a stronger and more specific statement than merely saying that the matrices are ill-conditioned.

## 9. Next gate

The next nonredundant computation should preserve the protected four-dimensional geometry while increasing the cutoff without returning to a naive dense high-precision inverse.

Recommended route:

1. Use the existing fast a=1 Feshbach/buffer assembly only after explicitly proving numerical equivalence with the current source-faithful form matrix on overlapping finite blocks.
2. Freeze a four-dimensional protected basis at a controlled cutoff.
3. Increase the finite buffer and evaluate the protected Schur complement plus source vector under that same basis.
4. Track:
   - the four protected eigenvalues,
   - the complement gap,
   - the protected source coordinates,
   - (E_e,E_o),
   - (kappa_0).
5. Only after (kappa_0) stabilizes under this cutoff enlargement should the weighted moments and (kappa_1) be promoted.
6. Keep any shifted lambda<lambda_a control separate from the lambda=0 xi-target branch.

## Result

The protected-subspace gate requested by v13.797 has landed.

[
oxed{
	extbf{Four protected directions are sufficient to isolate a stiff complement in both parity channels at N=16.}
}
]

[
oxed{
	extbf{The Feshbach and full spectral source-resolvent energies agree to about 65 decimal orders.}
}
]

[
oxed{
	extbf{The unresolved issue is cutoff motion of the near-null ladder, not fixed-cutoff linear-algebra instability.}
}
]
