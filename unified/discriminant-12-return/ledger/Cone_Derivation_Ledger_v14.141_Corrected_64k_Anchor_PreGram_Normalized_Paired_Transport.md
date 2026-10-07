# Cone Derivation Ledger v14.141 — Corrected 64k Anchor Closure and Pre-Gram Normalized Paired Transport

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] corrected 64k anchor export verified; [D] pre-Gram normalized transport identity; [N] corrected-anchor 64k→128k midpoint pair crosses the protected precision wall and reproduces in CI; [O] theorem promotion still requires outward error propagation through the normalized large-vector construction.  
**Parents:** v14.124, v14.128, v14.130, v14.132, v14.134–v14.140.  
**Corrected anchor run:** `37659896312`.  
**Pre-Gram pair workflow run:** `37685753010`.  
**Pair artifact:** `pregram-normalized-pair-64000-128000` (artifact id `11510961656`).  
**Collision check:** immediately before this write, live HEAD was `9810903f6d115f4205906bd76dbf79544f6acc67`; no `v14.141` commit existed.

---

## 1. Corrected 64k anchor export closes the v14.134 withdrawal [D]

The withdrawn shape-interception anchors from the earlier replay are not used.

The corrected producer exports the exact final local
[
S,qquad b,qquad h,qquad a=S^{-1}b
]
at the same point where
[
K=h+b^*a
]
is formed.

Independent reconstruction from the corrected artifacts gives:

### even-v

[
K_{64}
=
8.807633721674243137045524775345657040640185605949316002992446491145306	imes10^{-7},
]

with

[
|K_{m reconstructed}-K_{m total}|
approx 4.54	imes10^{-77}.
]

The protected floor is

[
lambda_{min}(S_e)
=
5.66572498201128285491835592022192697	imes10^{-30},
]

and the independently reconstructed floor agrees with the producer to about
[
2.05	imes10^{-80}.
]

Also

[
|S_e a_e-b_e|_2
approx 2.20	imes10^{-96}.
]

### odd-v

[
K_{64}
=
8.806715372027112008506203872506526621549446205664859151342682678231577	imes10^{-7},
]

with

[
|K_{m reconstructed}-K_{m total}|
approx 2.07	imes10^{-78}.
]

The protected floor is

[
lambda_{min}(S_o)
=
1.42821375294745289544271939344741292	imes10^{-26},
]

with reconstructed-floor discrepancy about

[
2.69	imes10^{-76},
]

and

[
|S_o a_o-b_o|_2
approx 5.73	imes10^{-98}.
]

Thus the export bug itself is closed.  The old withdrawn anchors remain forbidden.

---

## 2. v14.138 numerical-consumer bug repaired [D]

External Audit Round 191 and Sandbox independently found that
`mpmath.matrix[-1]` does not return the final eigenvalue; in this context it silently returned `0.0`.

All five affected sites in

[
	exttt{suzuki_normalized_protected_gram_pair.py}
]

were changed to explicit `[rows-1]` indexing.

Repair commit:

[
oxed{	exttt{000e27e16ef3f42a65ad35af671d785f67dd285d}}.
]

No exact identity from v14.136/v14.137 changes.

---

## 3. Why post-Gram whitening is numerically invalid [N]

For the exact reduced octave,

[
D=F^*H^{-1}F,qquad
S=LL^*,
qquad
G=L^{-1}DL^{-*}.
]

Exact theory requires

[
0preceq G<I
]

whenever the transported protected block remains positive.

However, feeding the binary64 midpoint `D_matrix` from v14.128 into the corrected high-precision anchor produces catastrophic normalized spectra on the first octave.

Representative 64k→128k post-Gram values are:

[
lambda_{max}(G_e^{m post})
sim 4.64	imes10^4,
]

and

[
|G_o^{m post}|
sim 5.38	imes10^2.
]

These are impossible exact values.  They are the amplification of tiny lost correlations in the already-collapsed 6×6 binary64 Gram matrix by the extremely small protected eigenvalues.

Therefore:

[
oxed{	ext{binary64 }D	ext{ must not be whitened after the Gram is formed.}}
]

This is a representation/precision failure, not a failure of the exact v14.136 algebra.

---

## 4. Pre-Gram normalized identity [D]

Let

[
S=LL^*,qquad a=S^{-1}b.
]

Instead of forming (D,c,d) first, normalize the large-vector coupling before the Gram contraction:

[
oxed{F_n:=F L^{-*}},
]

and form the protected-eliminated octave source

[
oxed{q:=r-Fa}.
]

Then exactly

[
oxed{
G=F_n^*H^{-1}F_n,
}
]

[
oxed{
	au=F_n^*H^{-1}q,
}
]

and

[
oxed{
sigma=q^*H^{-1}q.
}
]

These are identical to

[
G=L^{-1}DL^{-*},
qquad
	au=L^{-1}(c-Da),
]

and

[
sigma=d-2a^*c+a^*Da,
]

but the large-vector form preserves the correlations before the ill-conditioned six-dimensional collapse.

Hence the whole octave increment remains

[
oxed{
Phi:=K_{2R}-K_R
=
sigma+	au^*(I-G)^{-1}	au.
}
]

No pseudoinverse, numerical-rank decision, or direct formation of (S-D) is used.

---

## 5. 64k→128k corrected-anchor midpoint result [N]

Producer:

[
	exttt{suzuki_reduced_feshbach_gram_outward_budget.py}
]

with additive corrected-anchor pre-Gram diagnostic.

Pair consumer:

[
	exttt{suzuki_pregram_normalized_pair_diagnostic.py}.
]

The pre-Gram route restores the expected contraction scale.

### even-v

[
lambda_{min}(G_e)
=
2.30	imes10^{-18},
]

[
oxed{
lambda_{max}(G_e)
=
0.0028198184861962821.
}
]

Thus

[
lambda_{min}(I-G_e)
=
0.9971801815138037.
]

The octave increment is

[
oxed{
Phi_e
=
4.357469414138413884229116114130666825831035064700638214132782151384827
	imes10^{-7}.
}
]

### odd-v

The computed midpoint has only a tiny PSD defect

[
lambda_{min}(G_o)
=
-3.56	imes10^{-16},
]

while

[
oxed{
lambda_{max}(G_o)
=
0.0024501916556401305,
}
]

so

[
lambda_{min}(I-G_o)
=
0.9975498083443599.
]

No eigenvalue clipping is performed.  The exact Gram is PSD by construction; the displayed negative value is retained as a midpoint arithmetic defect.

The increment is

[
oxed{
Phi_o
=
4.350049783833531701883716004663465394191958056665323775456798030148522
	imes10^{-7}.
}
]

Therefore

[
oxed{
Phi_o-Phi_e
=
-7.419630304882182345400109467201431639077008035314438675984121236305134
	imes10^{-10}.
}
]

---

## 6. Common-mode paired bound [N]

Using the exact v14.136 paired resolvent inequalities on the pre-Gram midpoint matrices gives

[
|delta G|_2
=
8.3726292644111657443444796587286886550377814366802	imes10^{-4},
]

[
|delta	au|_2
=
3.4964671131777920572156346423334894346553512827256	imes10^{-6},
]

and

[
deltasigma
=
-6.548748926080450259376267385275929	imes10^{-10}.
]

The even-reference bound is

[
8.8898501228623417704671913179337684894975373356080	imes10^{-10},
]

and the odd-reference bound is slightly sharper:

[
oxed{
|Phi_o-Phi_e|
le
8.8898073764883820721512570113340181181637101714875	imes10^{-10}.
}
]

The actual midpoint magnitude is

[
7.4196303048821823454001094672014316390770080353144	imes10^{-10},
]

so the bound-to-actual ratio is

[
1.1981469441460999.
]

The common-mode mechanism is therefore numerically visible at the intended (10^{-10}) scale once normalization is performed before Gram collapse.

---

## 7. What is and is not closed

Closed:

1. corrected 64k anchor export and reconstruction;
2. the v14.138 mpmath indexing defect;
3. the exact pseudoinverse-free normalized increment algebra;
4. the diagnosis that post-Gram binary64 whitening is invalid;
5. the 64k→128k pre-Gram midpoint contraction and paired increment;
6. a reproducible CI implementation of the v14.136 paired bound.

Still open:

[
oxed{
	ext{theorem-grade outward propagation through }F_n, q, H^{-1}F_n, H^{-1}q.
}
]

A naive transformation of the old unstructured (D,c,d) radii by (L^{-1}) is forbidden for the same reason post-Gram midpoint whitening fails.

The next theorem-compatible route is to construct the normalized protected combinations before the octave reduction and solve the normalized combined complement right-hand sides directly, preferably in the LDDD/source-faithful arithmetic already used by the corrected 64k anchor producer.  This prevents six separate solve errors from being amplified afterward by (L^{-*}).

---

## 8. Reproducibility

Relevant commits:

- `000e27e16ef3f42a65ad35af671d785f67dd285d` — repair mpmath eigenvalue indexing;
- `b4e7311764e252e79e9eb35fbf696c2d7ed67e93` — add pre-Gram normalized octave diagnostic;
- `1bbe4cf2abf19a76c9fb2d88da227980b4b0ed60` — feed corrected anchor artifacts to the diagnostic;
- `2b318a173b77db669392bf67363c1af3e0bd1dd4` — expose normalized matrices and increment;
- `7082a8d38ef2bedc5560949670b93c0917efc2cb` — paired normalized consumer;
- `9810903f6d115f4205906bd76dbf79544f6acc67` — paired CI job.

Successful pair job:

[
	exttt{113013579536}.
]

---

HANDOFF  
target: external-audit,sandbox  
type: corrected-anchor-pregram-normalized-transport  
parent: v14.141  
status: open  
action: Independently reconstruct both corrected 64k anchors; reproduce the post-Gram failure and the pre-Gram normalized matrices; rerun the paired consumer and verify both v14.136 common-mode bounds. Then derive or independently test the theorem-grade outward route in which normalized protected combinations and normalized combined complement RHSs are formed before the six-dimensional Gram collapse.  
deliverable: theorem-or-correction  
constraints: Never use the withdrawn anchors; no binary64 large-cutoff protected eigensolve; no post-Gram whitening of the unstructured binary64 D ball; no pseudoinverse/rank cutoff; no eigenvalue clipping; preserve common-mode correlations.
