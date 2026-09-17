# Cone Derivation Ledger v13.566 — Cyclic-order orientation selects sigma_B

## Question
For the two J-compatible V4 automorphisms from v13.563,

\[
\sigma_A=(7\ 11),\qquad \sigma_B=(5\ 11\ 7),
\]

compute their action on the six oriented cyclic orders from v13.560 and determine which preserves the chosen orientation.

## Six oriented cyclic orders
Using the established labeling

\[
\begin{array}{c|c}
a&[1,5,11,7]\\
b&[1,7,11,5]\\
c&[1,11,5,7]\\
d&[1,7,5,11]\\
e&[1,5,7,11]\\
f&[1,11,7,5]
\end{array}
\]

with reversal \(\rho=(a\ b)(c\ d)(e\ f)\).

## Action of sigma_A
Apply \(\sigma_A:5\mapsto5,7\leftrightarrow11\) entrywise. One obtains

\[
a\leftrightarrow e,\qquad b\leftrightarrow f,\qquad c\leftrightarrow d,
\]

hence

\[
\boxed{\sigma_A|_{\mathcal C_6}=(a\ e)(b\ f)(c\ d).}
\]

As a permutation of the four carrier labels \(\{1,5,7,11\}\), \(\sigma_A\) is one transposition and therefore has sign \(-1\). Relative to the chosen ordered carrier orientation represented by \([1,5,7,11]\), it reverses orientation.

## Action of sigma_B
Apply \(\sigma_B:5\mapsto11,11\mapsto7,7\mapsto5\) entrywise. Then

\[
a\mapsto f\mapsto d\mapsto a,
\]

and

\[
b\mapsto e\mapsto c\mapsto b.
\]

Thus

\[
\boxed{\sigma_B|_{\mathcal C_6}=(a\ f\ d)(b\ e\ c).}
\]

This is exactly the already-verified ray permutation \(s\) from the S4 construction, because the corresponding carrier permutation is exactly the chosen generator

\[
S=(5\ 11\ 7),\qquad S(1)=1.
\]

It is a 3-cycle, hence even, so it preserves the chosen carrier orientation.

## Orientation selection
The two J-compatible automorphisms are distinguished by the sign homomorphism on the four-label S4 realization:

\[
\operatorname{sgn}(\sigma_A)=-1,\qquad
\operatorname{sgn}(\sigma_B)=+1.
\]

Therefore, once the v13.560 ordered carrier orientation is retained,

\[
\boxed{\sigma_B=(5\ 11\ 7)}
\]

is the unique one of the two J-compatible relabelings that preserves that chosen orientation. Moreover it is not a newly invented relabeling: it is literally the previously verified S generator whose six-ray action is \(s=(a\ f\ d)(b\ e\ c)\).

Combining with v13.563, the orientation-preserving J-compatible representative can be taken as

\[
\boxed{Q=J}
\]

(up to the commuting scale family \(\operatorname{diag}(a,a,c)\)).

## Guardrail
"Orientation-preserving" here refers to the orientation of the chosen ordered four-label carrier realization \([1,5,7,11]\), equivalently the sign of the corresponding permutation in S4. It is not a claim that the bare six-element coset set \(S_4/C_4\) carries a canonical orientation independent of that choice. The v13.560 cyclic-order identification itself was chosen/equivariant rather than canonical.
