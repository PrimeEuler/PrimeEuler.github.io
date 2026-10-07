# Cone Derivation Ledger v14.136 — Pseudoinverse-Free Cholesky-Normalized Paired Octave Increment

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] Exact Cholesky-normalized formula for the full finite-octave increment and an exact common-mode-preserving paired-parity bound, requiring neither (D^+) nor the subtraction/inversion of (S-D). [O] Numerical evaluation awaits the corrected explicit M64000 anchor from replay `37659896312`; no theorem promotion from midpoint Gram data is made here.  
**Parents:** v14.124, v14.130, v14.132, v14.134–v14.135.  
**Research consumer:** `unified/discriminant-12-return/research-notes/suzuki_normalized_protected_gram_pair.py`, current implementation commits `1ab3362`, `07904d5`.  
**Collision check:** immediately before this write, live HEAD was `07904d5ed479c76b3a026363a176fa153d54befa`; live ledger max was v14.135. No v14.136 collision was present.

---

## 1. Starting point

For one octave (R\to 2R), v14.124 gives

[
K_{2R}-K_R
=
\sigma+t^*(S-D)^{-1}t,
]

where

[
a=S^{-1}b,
qquad
\sigma=d-2a^*c+a^*Da,
qquad
t=c-Da.
]

The obstruction is that (S) has extremely small protected eigenvalues, so explicitly forming or inverting (S-D) is the wrong numerical architecture.

Take the certified protected Cholesky factor

[
S=LL^*,
]

and define, exactly as in v14.130,

[
G=L^{-1}DL^{-*}.
]

Then

[
S-D=L(I-G)L^*.
]

Define the normalized residual coordinate

[
\boxed{\tau:=L^{-1}t=L^{-1}(c-Da).}
]

Therefore

[
t^*(S-D)^{-1}t
=
\tau^*(I-G)^{-1}\tau,
]

and hence

[
\boxed{
K_{2R}-K_R
=
\sigma+\tau^*(I-G)^{-1}\tau.
}
\tag{1}
]

Equation (1) is exact. It requires no pseudoinverse, no rank decision for (D), and no explicit (S-D).

---

## 2. Factor-preserving anchor transport

Since the exact reduced block is positive,

[
0\preceq G\prec I.
]

Let

[
I-G=CC^*
]

be its Cholesky factorization. Then

[
S_{2R}=S-D
=
L(I-G)L^*
=
(LC)(LC)^*.
]

Thus the next protected factor can be transported as

[
\boxed{L_{2R}=LC}
\tag{2}
]

together with the exact reduced updates

[
b_{2R}=b-c,
qquad
h_{2R}=h+d.
]

This never materializes the near-singular difference (S-D).

---

## 3. Paired parity identity

For parity (p\in\{e,o\}), write

[
\Phi_p
:=
\sigma_p+\tau_p^*R_p\tau_p,
qquad
R_p:=(I-G_p)^{-1}.
]

Then

[
\Phi_p=K_{2R,p}-K_{R,p}.
]

Set

[
\delta G:=G_o-G_e,
qquad
\delta\tau:=\tau_o-\tau_e,
qquad
\delta\sigma:=\sigma_o-\sigma_e.
]

The resolvent identity gives

[
R_o-R_e
=
R_o\,\delta G\,R_e.
]

Using even parity as the reference,

[
\begin{aligned}
\Phi_o-\Phi_e
&=
\delta\sigma
+
\tau_o^*(R_o-R_e)\tau_o
+
\left(\tau_o^*R_e\tau_o-\tau_e^*R_e\tau_e\right) \\
&=
\delta\sigma
+
(R_o\tau_o)^*\delta G(R_e\tau_o)
+
(\delta\tau)^*R_e\tau_o
+
\tau_e^*R_e\delta\tau.
\end{aligned}
\tag{3}
]

Therefore

[
\boxed{
\begin{aligned}
|\Phi_o-\Phi_e|
&\le
|\delta\sigma|
+
\|\delta G\|_2
\|R_o\tau_o\|
\|R_e\tau_o\| \\
&\quad+
\|\delta\tau\|
\left(
\|R_e\tau_o\|
+
\|R_e\tau_e\|
\right).
\end{aligned}}
\tag{4e}
]

Using odd parity as the reference instead gives the equally exact companion bound

[
\boxed{
\begin{aligned}
|\Phi_o-\Phi_e|
&\le
|\delta\sigma|
+
\|\delta G\|_2
\|R_o\tau_e\|
\|R_e\tau_e\| \\
&\quad+
\|\delta\tau\|
\left(
\|R_o\tau_o\|
+
\|R_o\tau_e\|
\right).
\end{aligned}}
\tag{4o}
]

Hence the valid paired bound is the minimum of the two right-hand sides.

---

## 4. Why this is a useful gate

The bound has four properties needed by the present certification problem:

1. **Exact common-mode preservation.** If
   [
   (G_o,\tau_o,\sigma_o)=(G_e,\tau_e,\sigma_e),
   ]
   then the bound vanishes identically.

2. **No pseudoinverse/rank decision.** Unlike the (v=D^+c) representation of the protected-only split, (1)–(4) remain valid without deciding whether the near-rank-one midpoint (D) is numerically full rank.

3. **No protected-matrix subtraction.** Neither evaluation nor transport forms (S-D); only (I-G) is factored/inverted.

4. **At most six dimensions after the octave solves.** All paired load-bearing algebra is confined to the protected coordinates.

This gives an independent route to certify the parity difference of the **whole finite-octave increment**. It does not invalidate v14.128 or v14.132; rather, it provides a rank-independent fallback if the protected-only (D^+) split is numerically ambiguous.

---

## 5. Independent algebra test

The identity and both paired bounds were checked on independent random SPD test systems in multiprecision:

- direct Schur transport versus (1): agreement at approximately (2\times10^{-81});
- factor transport (L_{2R}=L\operatorname{chol}(I-G)): residual at approximately (2\times10^{-80});
- both (4e) and (4o) bounded the directly evaluated paired increment.

These tests are sanity checks only; the derivation above is exact and load-bearing.

---

## 6. Numerical guardrail

The current reduced octave (D) midpoint is known to be nearly rank one. For example, on the previously audited (128k\to256k) replay the binary64 symmetric eigensolves contained tiny negative near-null eigenvalues (approximately (-3.7\times10^{-24}) even and (-1.37\times10^{-22}) odd), while the dominant eigenvalues were (3.5081\times10^{-8}) and (1.1156\times10^{-6}).

Therefore:

- no arbitrary pseudoinverse cutoff is introduced;
- the normalized consumer emits the v14.132 protected-only quantity only when midpoint (D\succ0);
- the pseudoinverse-free whole-increment route (1)–(4) is the preferred rank-independent diagnostic;
- theorem-grade use still requires propagation of the certified outward Gram uncertainties into the normalized variables.

---

## 7. Current dependency

The old 64k anchor artifacts and transport run `37658776275` remain withdrawn under v14.134.

The only admissible anchor is the producer's explicit final payload from corrected replay

[
\boxed{`37659896312`}.
]

At write time that replay remains in progress in both parity sectors. No numerical value from the withdrawn anchor is used here.

---

## 8. Verdict

[
\boxed{
K_{2R}-K_R
=
\sigma+\tau^*(I-G)^{-1}\tau,
qquad
\tau=L^{-1}(c-Da).
}
]

Together with (4e)/(4o), this closes the analytic rank-dependence gap in the paired finite-octave consumer. Numerical certification remains open only on the corrected anchor and normalized outward-error propagation.

---

HANDOFF  
target: external-audit, sandbox  
type: normalized-whole-increment-paired-bound  
parent: v14.136  
status: open  
action: Independently derive (1), (4e), and (4o). When corrected replay 37659896312 completes, evaluate the normalized whole-increment pair on the explicit final anchors and compare with the v14.132 protected-only route where the midpoint rank is resolvable.  
deliverable: verification-or-obstruction  
constraints: Do not use withdrawn M64000 anchors; do not form S-D; do not introduce an arbitrary pseudoinverse cutoff; theorem-grade numerics must propagate the outward Gram uncertainty.
