# Cone Derivation Ledger v13.821 — \(\rho=0.02\) Parity-Tail Inertia Theorem

Date: 2026-09-26.

Lane: A.

Status: [C] exact sector-wise \(\rho=0.02\) tail endpoint inertias in both parities; [C] zero endpoint kernels; [C] exactly four compact-relative tail resonances in the sector-wise window \((-1.02,-0.98)\); [G] no parity-direct-sum multiplicity claim and no statement about the separate two-mode low-core Feshbach problem.

Parents: v13.818–820.

Research artifact:

- research-notes/suzuki_endpoint_M3999_rho002_inertia_certificate.py
  - theorem commit a63dfd1c7844297dc4b71faa6bd66ab31c4e9fe4
  - wording cleanup 36af688f554ba8d2c22b0b322879e988de6e8f99

Frozen inputs remain exactly those of v13.818. The widened caps remain exactly those of v13.820. No eigenspace, Cholesky factor, or audit threshold is regenerated here.

No GitHub workflow/status run is attached.

## 1. The two endpoint pencils

For each parity tail, define

\[
F^-_{0.02}
=
A-0.02B_{\rm sm},
\]

\[
F^+_{0.02}
=
A+0.02B_{\rm sm}.
\]

The remote parity tails begin at

\[
n=5,7,9,\ldots
\quad\text{for even-v},
\]

and

\[
n=6,8,10,\ldots
\quad\text{for odd-v}.
\]

The separate first two parity modes retained in the low-core Feshbach problem are not part of this theorem.

## 2. Frozen data and audit inheritance

The theorem wrapper begins by rerunning the v13.818 fail-closed immutable checks:

- exact SHA-256 hashes;
- exact rational rank minors for the minus four- and six-planes;
- exact triangular rank for the plus ten-core Cholesky factors;
- positive Cholesky diagonals.

It then consumes the v13.820 widened cap program unchanged.

The shared analytic assumptions are also rerun:

\[
|Z_n^{(\pm,0.02)}|<8
\qquad
(n\ge2{,}000{,}001),
\]

and the common remote cross-operator majorant

\[
\|F_{RF}\|<20.
\]

## 3. Minus endpoint: four strict negative directions

The hardened v13.820 finite graph-form certificates give

### even-v

\[
\boxed{
-Q_{{\rm neg},e}^{T}
S^-_{e,\rm exact}
Q_{{\rm neg},e}
>
0.00266179948027\,I.
}
\]

In frozen normalized coordinates,

\[
\boxed{
>
0.99999991429\,I.
}
\]

### odd-v

\[
\boxed{
-Q_{{\rm neg},o}^{T}
S^-_{o,\rm exact}
Q_{{\rm neg},o}
>
0.00398570593918\,I.
}
\]

Normalized,

\[
\boxed{
>
0.99999984934\,I.
}
\]

Hence each parity tail contains a four-dimensional strict negative graph subspace, and therefore

\[
\operatorname{ind}_{-}
(F^-_{0.02,\rm tail})
\ge4.
\]

## 4. Minus endpoint: codimension-four positive complement

The six frozen positive directions, after exact finite elimination and infinite remote correction, obey the following fail-closed terminal margins.

### even-v

\[
\boxed{
\gamma^-_e C^-_{e,6}-H^-_e
>
3.13191084098\,I.
}
\]

Equivalently, the remote-corrected normalized form satisfies

\[
\boxed{
C^-_{e,6}
-
(\gamma^-_e)^{-1}H^-_e
>
0.9848679786\,I.
}
\]

### odd-v

\[
\boxed{
\gamma^-_o C^-_{o,6}-H^-_o
>
3.17134400520\,I,
}
\]

and

\[
\boxed{
C^-_{o,6}
-
(\gamma^-_o)^{-1}H^-_o
>
0.9972258994\,I.
}
\]

Together with the positive eliminated finite buffer and positive remote tail, this constructs an infinite-dimensional positive subspace of codimension four. Hence

\[
\operatorname{ind}_{\le0}
(F^-_{0.02,\rm tail})
\le4.
\]

Combining with the four-dimensional strict negative graph space gives

\[
\boxed{
\operatorname{ind}_{-}
(F^-_{0.02,e,\rm tail})
=4,
}
\]

\[
\boxed{
\operatorname{ind}_{-}
(F^-_{0.02,o,\rm tail})
=4.
}
\]

Because the nonpositive index is already exhausted by four strict negative directions,

\[
\boxed{
\ker F^-_{0.02,e,\rm tail}
=
\ker F^-_{0.02,o,\rm tail}
=
\{0\}.
}
\]

## 5. Plus endpoint: strict positivity

For the plus endpoint, the standard ten-coordinate Schur core is positive after exact finite and infinite remote correction.

### even-v

\[
\boxed{
\gamma^+_e C^+_{e,10}-H^+_e
>
3.34990486435\,I.
}
\]

Normalized,

\[
\boxed{
C^+_{e,10}
-
(\gamma^+_e)^{-1}H^+_e
>
0.9871476699\,I.
}
\]

### odd-v

\[
\boxed{
\gamma^+_o C^+_{o,10}-H^+_o
>
3.35907757792\,I,
}
\]

with normalized lower bound

\[
\boxed{
C^+_{o,10}
-
(\gamma^+_o)^{-1}H^+_o
>
0.9898083969\,I.
}
\]

Since the finite buffer and remote tail are also strictly positive,

\[
\boxed{
F^+_{0.02,e,\rm tail}>0,
\qquad
F^+_{0.02,o,\rm tail}>0.
}
\]

Therefore

\[
\boxed{
\operatorname{ind}_{-}
(F^+_{0.02,e,\rm tail})
=
\operatorname{ind}_{-}
(F^+_{0.02,o,\rm tail})
=
0,
}
\]

and

\[
\boxed{
\ker F^+_{0.02,e,\rm tail}
=
\ker F^+_{0.02,o,\rm tail}
=
\{0\}.
}
\]

## 6. Exact inertia-difference count

Let \(\delta\) denote the generalized eigenvalue of the pair

\[
Aq=\delta B_{\rm sm}q.
\]

Because both endpoint pencils are nonsingular,

\[
N_{\rm tail}(\rho)
=
\#\{
\delta:\ |\delta|<\rho
\}
=
\operatorname{ind}_{-}(A-\rho B_{\rm sm})
-
\operatorname{ind}_{-}(A+\rho B_{\rm sm}).
\]

At

\[
\rho=0.02,
\]

the certified endpoint inertias give, sector by sector,

\[
\boxed{
N_{\rm tail}^{(e)}(0.02)
=
4-0
=
4,
}
\]

\[
\boxed{
N_{\rm tail}^{(o)}(0.02)
=
4-0
=
4.
}
\]

For the compact relative tail operator

\[
J=I+K,
\]

one has

\[
\delta=1+\mu,
\]

where \(\mu\) is an eigenvalue of \(K\). Therefore

\[
|\delta|<0.02
\]

is equivalent to

\[
-1.02<\mu<-0.98.
\]

Thus

\[
\boxed{
\operatorname{rank}
\mathbf 1_{(-1.02,-0.98)}
(K_{e,\rm tail})
=
4,
}
\]

\[
\boxed{
\operatorname{rank}
\mathbf 1_{(-1.02,-0.98)}
(K_{o,\rm tail})
=
4.
}
\]

These are sector-wise statements. No direct-sum multiplicity is asserted.

## 7. Relation to the \(\rho=0.10\) certificate

v13.816 gives

\[
N_{\rm tail}^{(e)}(0.10)
=
N_{\rm tail}^{(o)}(0.10)
=
4.
\]

The present theorem gives

\[
N_{\rm tail}^{(e)}(0.02)
=
N_{\rm tail}^{(o)}(0.02)
=
4.
\]

Therefore, in each parity tail separately, the same four resonances already lie inside the tighter window

\[
(-1.02,-0.98),
\]

and there is no fifth resonance in the larger window

\[
(-1.10,-0.90).
\]

This is the desired four-dimensional resonance-cluster certificate for the bulk-subtracted parity tail.

## 8. Exact public certificate margins

The fail-closed lower bounds used for theorem promotion are exactly the following decimal constants from the theorem wrapper:

\[
\boxed{
m^-_{{\rm neg},e}
=
0.00266179948027,
}
\]

\[
\boxed{
m^-_{{\rm neg},o}
=
0.00398570593918,
}
\]

\[
\boxed{
m^-_{{\rm pos},e}
=
3.13191084098,
}
\]

\[
\boxed{
m^-_{{\rm pos},o}
=
3.17134400520,
}
\]

\[
\boxed{
m^+_{e}
=
3.34990486435,
}
\]

\[
\boxed{
m^+_{o}
=
3.35907757792.
}
\]

The associated normalized lower bounds are

\[
\boxed{
0.99999991429,\quad
0.99999984934,\quad
0.9848679786,\quad
0.9972258994,\quad
0.9871476699,\quad
0.9898083969.
}
\]

These are deliberately the widened audited constants, not best-point estimates.

## 9. Guardrails

This theorem is scoped to the bulk-subtracted parity tails only.

It does not:

- combine the two parity counts into a direct-sum multiplicity claim;
- include the separate two-mode low-core Feshbach problem;
- promote any exact-zero, RH, or GRH statement;
- depend on the historical sign-incorrect odd/full-parity certificate lineage placed on HOLD at v13.799.

## Result

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.02,e,\rm tail})
=
\operatorname{ind}_{-}(F^-_{0.02,o,\rm tail})
=
4,
}
\]

\[
\boxed{
\operatorname{ind}_{-}(F^+_{0.02,e,\rm tail})
=
\operatorname{ind}_{-}(F^+_{0.02,o,\rm tail})
=
0,
}
\]

with zero kernel at all four endpoints, and hence

\[
\boxed{
N_{\rm tail}^{(e)}(0.02)
=
N_{\rm tail}^{(o)}(0.02)
=
4.
}
\]

Equivalently, each parity-tail compact relative operator has exactly four certified resonances in

\[
\boxed{
(-1.02,-0.98).
}
\]
