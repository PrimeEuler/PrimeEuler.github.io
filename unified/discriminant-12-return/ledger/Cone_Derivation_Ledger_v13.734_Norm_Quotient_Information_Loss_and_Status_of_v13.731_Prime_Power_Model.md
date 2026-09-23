# Cone Derivation Ledger v13.734 — Norm-Quotient Information Loss and Status of the v13.731 Prime-Power Model

**Date:** 2026-09-23  
**Status:** exact group/test-function quotient identified; v13.731 Hilbert-space model is not yet a quotient representation  
**Parents:** v13.731, v13.733 (Weil-normalization lane)  
**Coordination note:** another thread independently used the label v13.733 after our Weil-normalization v13.733. No content collision is present; this lane advances to v13.734.

## 1. Exact norm quotient of the idele-class group

Let
\[
C_{\mathbb Q}=\mathbb A_{\mathbb Q}^{\times}/\mathbb Q^\times.
\]
The adelic norm
\[
|\cdot|_{\mathbb A}:C_{\mathbb Q}\to\mathbb R_{>0}^{\times}
\]
is well defined by the product formula. Define
\[
C_{\mathbb Q}^{1}=\ker|\cdot|_{\mathbb A}.
\]
Then
\[
\boxed{
1\to C_{\mathbb Q}^{1}
\to C_{\mathbb Q}
\xrightarrow{|\cdot|_{\mathbb A}}
\mathbb R_{>0}^{\times}
\to1.
}
\]
Therefore
\[
\boxed{
C_{\mathbb Q}/C_{\mathbb Q}^{1}\simeq\mathbb R_{>0}^{\times}.
}
\]
After
\[
r=\log|u|_{\mathbb A},
\]
this becomes the additive quotient
\[
\boxed{
C_{\mathbb Q}/C_{\mathbb Q}^{1}\simeq\mathbb R_r.
}
\]

Thus the logarithmic/rapidity coordinate used throughout the cone lane is genuinely the coordinate of the norm quotient. Idele inversion gives
\[
u\mapsto u^{-1}
\quad\Rightarrow\quad
r\mapsto-r.
\]

## 2. Information discarded by norm projection

Two idele classes have the same norm coordinate iff their ratio lies in \(C_{\mathbb Q}^{1}\). Hence the norm map forgets the entire norm-one fiber.

At the character level, a quasicharacter has the form
\[
\chi(u)|u|_{\mathbb A}^{s},
\]
with \(\chi\) unitary on the norm-one component. Projection to the norm quotient retains only the trivial-\(C_{\mathbb Q}^{1}\) sector:
\[
\boxed{
\chi(u)|u|^s\mapsto |u|^s
\quad\text{only when }\chi|_{C_{\mathbb Q}^{1}}=1.
}
\]

Therefore norm projection loses:
- nontrivial idele-class/Hecke characters;
- ramification and conductor data carried by those characters;
- local unit-group information;
- general twisted \(L(s,\chi)\) data.

It retains the trivial-character zeta lane exactly.

## 3. Local finite-place loss

Locally
\[
\mathbb Q_p^\times\simeq p^{\mathbb Z}\times\mathbb Z_p^\times.
\]
The valuation/norm projection is
\[
p^ku\mapsto k,\qquad u\in\mathbb Z_p^\times,
\]
so
\[
\boxed{
\mathbb Q_p^\times/\mathbb Z_p^\times\simeq\mathbb Z.
}
\]

The v13.731 local basis
\[
e_{p,k},\qquad H_pe_{p,k}=k\log p\,e_{p,k}
\]
uses precisely this valuation coordinate. It retains prime-power shell data and discards the unit coordinate \(u\in\mathbb Z_p^\times\).

This is sufficient for the unramified trivial local factor
\[
L_p(s)=(1-p^{-s})^{-1},
\]
but not for arbitrary ramified local Tate characters.

## 4. Important distinction: norm quotient vs v13.731 labels

The abstract norm quotient retains only the real number
\[
r=\log|u|_{\mathbb A}.
\]
The v13.731 space
\[
\mathcal H_{\rm fin}=\bigoplus_p\ell^2(\mathbb N_{\ge1})
\]
carries explicit labels \((p,k)\).

Thus the v13.731 realization is not literally the regular representation of the quotient group \(\mathbb R_{>0}^{\times}\). Its spectral support is the arithmetic subset
\[
\{k\log p:p\text{ prime},\ k\ge1\}
\]
with weights \(\log p\).

Unique factorization implies that \(k\log p=\ell\log q\) for positive integers and primes forces \(p=q\), \(k=\ell\), so the spectral value determines the prime power on this special support. But this arithmetic labeling is built into the chosen trace realization; it is not supplied by the abstract quotient map itself.

## 5. Exact status of the v13.731 model

Three levels must be distinguished.

### Group level — genuine quotient
\[
\boxed{
C_{\mathbb Q}/C_{\mathbb Q}^{1}\simeq\mathbb R_{>0}^{\times}.
}
\]

### Test-function/character level — genuine trivial-sector projection

Functions of norm only,
\[
h(u)=H(|u|),
\]
and quasicharacters \(|u|^s\) form the trivial-\(C_{\mathbb Q}^{1}\) sector. The Riemann-zeta scalar local factors and the v13.733 centered Weil arithmetic distribution descend exactly to this sector.

### v13.731 Hilbert-space level — auxiliary realization, not proven quotient

No representation
\[
\pi:C_{\mathbb Q}\to U(\mathcal H)
\]
and invariant quotient/subspace has been constructed whose descended operator is
\[
H_{\rm fin}=\bigoplus_p H_p
\]
with insertion
\[
A_{\rm fin}=\bigoplus_p(\log p)I.
\]

Therefore
\[
\boxed{
\text{v13.731 is NOT currently a quotient representation of }C_{\mathbb Q}.
}
\]

But it is stronger than an analogy:
\[
\boxed{
\text{its scalar trace distribution is the exact norm-sector arithmetic distribution.}
}
\]

The precise description is:

> v13.731 is an auxiliary Hilbert-space realization of the exact pushforward/trivial-character Weil distribution on the norm quotient, not a demonstrated quotient of the canonical adelic representation.

## 6. What is retained and lost

| Datum | Norm projection |
|---|---|
| \(|u|_{\mathbb A}\) | retained |
| \(r=\log|u|_{\mathbb A}\) | retained |
| trivial quasicharacters \(|u|^s\) | retained |
| inversion \(u\mapsto u^{-1}\) | retained as \(r\mapsto-r\) |
| trivial-character zeta Euler factors | retained |
| \(C_{\mathbb Q}^{1}\) position | lost |
| nontrivial Hecke characters | lost |
| \(\mathbb Z_p^\times\) unit coordinate | lost |
| ramification/conductor data | lost |
| general \(L(s,\chi)\) family | not recoverable from norm alone |

## 7. Cone interpretation

The exact statement supported by the present work is not
\[
\text{cone}\cong C_{\mathbb Q}.
\]
Rather, the logarithmic cone/rapidity line matches the rank-one norm quotient:
\[
\boxed{
r\leftrightarrow\log|u|_{\mathbb A}\in
\log(C_{\mathbb Q}/C_{\mathbb Q}^{1}).
}
\]
The common reflection
\[
r\mapsto-r
\]
is exactly the logarithmic image of idele inversion.

This is a genuine structural identification at the quotient-coordinate level. It does not geometrize the compact/norm-one idele-class fiber.

## 8. Commutative diagram and missing arrow

The current situation is
\[
\begin{array}{ccc}
C_{\mathbb Q}
&\longrightarrow&
\text{canonical idele-class/Weil representation}
\\
\downarrow |\cdot|_{\mathbb A}
&&\downarrow\text{trivial-character projection}
\\
\mathbb R_{>0}^{\times}
&\longrightarrow&
\text{v13.715/v13.733 arithmetic distribution}
\\
\downarrow\log
&&\downarrow
\\
\mathbb R_r
&\longrightarrow&
\text{v13.731 trace realization}.
\end{array}
\]

The left vertical quotient maps are canonical. The arithmetic distribution on the right is canonical. The bottom-right Hilbert-space realization is constructed.

The missing statement is a representation-theoretic descent from the upper-right canonical object to the v13.731 Hilbert space.

## 9. Next discriminating gate

Construct, where meaningful, the trivial-\(C_{\mathbb Q}^{1}\) isotypic/averaged sector of a canonical idele-class representation and determine its norm-direction operator.

Two outcomes are possible:

1. It yields a continuous regular representation on the norm line. Then its character may reproduce the centered Weil distribution, but the discrete prime-power \((p,k)\) decomposition of v13.731 is an auxiliary trace expansion rather than quotient-state spectrum.

2. It naturally yields the prime-power decomposition and insertion weights. Then v13.731 can be upgraded to a genuine representation-theoretic quotient.

No such upgrade is claimed before this computation.

## 10. Guardrail

The norm coordinate is a genuine quotient. The trivial-character arithmetic distribution descends exactly. The v13.731 prime-power Hilbert-space model is **not yet** a quotient representation; calling it merely an analogy is also too weak because its trace distribution is exactly the canonical norm-sector distribution.
