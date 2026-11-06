# Cone Derivation Ledger v15.475 — Lane A exact 16-branch transfer operator

**Timestamp:** 2026-11-06 16:31 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact endomorphism transfer operator certified; physical 45-diagonal representation and joint norm gate unevaluated

## Fresh state

Live master was checked before selecting this gate and before each additive payload write. The newest relevant audit remains External Audit Round 500/v15.465, which confirms v15.464 without correction. Round 501/v15.471 and Sandbox v15.472–v15.474 concern separate Sandbox work and introduce no Lane A correction or ownership conflict. No commit status or workflow run is attached to live HEAD. The v15.475 paths were next-free and noncolliding at deposit.

## Canonical transfer pair

Let (A=C(\mathbb T^4)), let

[
D(z_1,z_2,z_3,z_4)=(z_1^2,z_2^2,z_3^2,z_4^2),
qquad \alpha(f)=f\circ D,
]

and define the normalized 16-branch transfer operator

[
(Lg)(x)=\frac1{16}\sum_{D(y)=x}g(y).
]

Because (D) has exactly 16 inverse branches, (L) is positive, unital, and satisfies the transfer identity

[
L(\alpha(f)g)=fL(g).
]

Indeed, (\alpha(f)(y)=f(D(y))=f(x)) on every point in the fiber (D^{-1}(x)), so the factor (f(x)) leaves the fiber average.

## Exact Fourier action

For (m\in\mathbb Z^4), write (\chi_m(z)=z_1^{m_1}\cdots z_4^{m_4}). Choosing any square root (y_0) of (x), the fiber is (\{\varepsilon y_0:\varepsilon\in\{\pm1\}^4\}). Hence

[
L\chi_m(x)=\chi_m(y_0)\prod_{j=1}^4\frac{1+(-1)^{m_j}}2.
]

Therefore

[
L\chi_m=
\begin{cases}
0,&\text{if some }m_j\text{ is odd},\\
\chi_{m/2},&\text{if every }m_j\text{ is even}.
\end{cases}
]

This is the exact branch-retaining operator required after v15.464's nonautomorphism correction. The witness checks the character rule on all (9^4=6561) exponents in ([-4,4]^4) and checks (L(\alpha(\chi_a)\chi_b)=\chi_aL(\chi_b)) on all (5^8=390625) pairs (a,b\in[-2,2]^4), using integer sign sums only.

## What remains open

This entry does **not** identify the physical signed 45-diagonal Hankel operator with a faithful covariant representation of ((A,\alpha,L)). In particular it does not prove that the correspondence norm equals the original chosen-ell2 operator norm, and it does not evaluate

[
\|P+C_{\rm near}(22)\|<p+0.000102161983428448238\ldots.
]

The next concrete gate is to express each transported annulus block as a coefficient in a covariant representation of this transfer pair (or its natural-extension solenoid), then prove a faithful norm comparison. Without that bridge, the exact Fourier filter above is architecture, not a numerical certificate for the joint gate.

## Reproducibility

Witness `research-notes/lane_a_v15_475_transfer_operator_certificate.py`; commit `f430cd657abfa6114c00ee948b36f9d8b7cf7bdf`; blob `d2919db0e4e637f3163d90d71813407218bd13fa`; SHA-256 `3374f1745a243d6f85a300b5109905f3d56b38662ff4a57bcf00d2fc9e80673c`.

Manifest `research-notes/lane_a_v15_475_transfer_operator_certificate.sha256`; commit `46210a589bff737b37483edfbd1bc649c75962a5`; blob `46217651de91ed82d4db0532ef5c9905e963fdd1`; SHA-256 `e8544b37d237ac4dd03cb7b83cbc28299007bdd2e242b9ba2c9868fe31269771`.

Replay returns `PASS_EXACT_16_BRANCH_TRANSFER_OPERATOR`, `physical_45_diagonal_representation=UNBUILT`, and `joint_norm_gate=UNEVALUATED`.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency commutator gate. It is not the whole K and not source-native Suzuki Phi. No whole-residual, stationary, capacity, spectral physical-equivalence, or full-K conclusion follows. Original `C_S_32000`, all thresholds, frozen hashes, and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** independently verify the normalized 16-branch transfer identity and Fourier rule. Then construct or obstruct the faithful physical 45-diagonal covariant representation; do not promote this exact transfer-operator lemma to a joint-norm pass.
