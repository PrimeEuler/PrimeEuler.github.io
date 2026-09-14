# Cone Derivation Ledger v13.431 — Cyclotomic Zeta Intertwiner Graph

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger currently contains two independent entries carrying the label `v13.430`; this checkpoint therefore skips to `v13.431` rather than reusing `v13.430`.

This entry continues `v13.421`, where the cyclotomic field was decomposed over `Q` into the four one-dimensional `V4=U(12)` character lines.

## 1. Character-line basis [D]

Use the ordered rational basis

\[
B_\chi=(1,\ i,\ i\sqrt3,\ \sqrt3),
\]

corresponding respectively to the characters

\[
\mathbf1,\qquad \chi_{-4},\qquad \chi_{-3},\qquad \chi_{12}.
\]

Thus

\[
\mathbf Q(\zeta_{12})
=
\mathbf Q\cdot1
\oplus
\mathbf Q\cdot i
\oplus
\mathbf Q\cdot i\sqrt3
\oplus
\mathbf Q\cdot\sqrt3.
\]

Let

\[
\zeta=\zeta_{12}=\frac{\sqrt3+i}{2},
\qquad
\mathcal Z=\times\zeta.
\]

## 2. Exact action of multiplication by zeta [D]

Direct multiplication gives

\[
\mathcal Z(1)=\frac12 i+\frac12\sqrt3,
\]

\[
\mathcal Z(i)=-\frac12+\frac12 i\sqrt3,
\]

\[
\mathcal Z(i\sqrt3)=\frac32 i-\frac12\sqrt3,
\]

\[
\mathcal Z(\sqrt3)=\frac32+\frac12 i\sqrt3.
\]

Therefore in the ordered basis `B_chi`,

\[
\boxed{
[\mathcal Z]_{B_\chi}
=
\begin{pmatrix}
0&-\frac12&0&\frac32\\
\frac12&0&\frac32&0\\
0&\frac12&0&\frac12\\
\frac12&0&-\frac12&0
\end{pmatrix}.
}
\]

## 3. Character-theoretic intertwiner rule [D]

Since

\[
\zeta=\frac12\sqrt3+\frac12 i,
\]

and `sqrt3` lies in the `chi_12` character line while `i` lies in the `chi_-4` line, multiplication by `zeta` sends any character line `L_chi` into

\[
\boxed{
\mathcal Z(L_\chi)
\subset
L_{\chi\chi_{12}}
\oplus
L_{\chi\chi_{-4}}.
}
\]

Because

\[
\chi_{12}=\chi_{-4}\chi_{-3},
\]

both target characters differ from `chi` by a character with `chi_-3` parity opposite to that of `chi`.

Thus the four character lines split into two parity classes

\[
\{\mathbf1,\chi_{-3}\}
\qquad\text{and}\qquad
\{\chi_{-4},\chi_{12}\},
\]

and `mathcal Z` exchanges these two classes.

## 4. Bipartite intertwiner graph [D/I]

Ignoring coefficients and retaining only nonzero character-line couplings, the graph is

\[
\{\mathbf1,\chi_{-3}\}
\longleftrightarrow
\{\chi_{-4},\chi_{12}\}.
\]

More precisely each source line has two outgoing character edges:

- multiplication by the `i` component toggles by `chi_-4`;
- multiplication by the `sqrt3` component toggles by `chi_12`.

Hence the support graph is the complete bipartite graph `K_{2,2}`, equivalently a square whose edge labels are `chi_-4` and `chi_12`.

This is an operator-level realization of the `V4` character multiplication law, but it is not the same as the geometric mod-12 shell drawing.

## 5. Powers of the intertwiner [D]

Since

\[
\zeta^2=\frac{1+i\sqrt3}{2},
\]

`mathcal Z^2` has only the trivial and `chi_-3` character components. Therefore

\[
\boxed{
\mathcal Z^2(L_\chi)
\subset
L_\chi\oplus L_{\chi\chi_{-3}},
}
\]

so `mathcal Z^2` preserves each `chi_-3` parity half.

Since

\[
\zeta^3=i,
\]

one has

\[
\boxed{\mathcal Z^3=\times i,}
\]

which acts as the signed permutation

\[
1\mapsto i,
\qquad
i\mapsto-1,
\qquad
i\sqrt3\mapsto-\sqrt3,
\qquad
\sqrt3\mapsto i\sqrt3.
\]

Thus at the level of character labels, `mathcal Z^3` toggles exactly by `chi_-4`.

Further,

\[
\boxed{\mathcal Z^6=-I,}
\qquad
\boxed{\mathcal Z^{12}=I.}
\]

The order-12 cyclotomic multiplication therefore alternates between the two `chi_-3` parity halves at odd powers, stays within a parity half at even powers, becomes a signed character permutation at the cubic step, and reaches scalar `-I` at the half-period.

## 6. Relation to the prior finite-field reduction [D/I]

`v13.416` showed that the ramified residue-field Galois action is controlled by `chi_-3`, while Pell-time orientation is controlled by `chi_12`.

The present calculation explains why `chi_-3` naturally appears as a parity partition for `mathcal Z`: the primitive cyclotomic generator itself contains exactly the two character components `chi_-4` and `chi_12`, whose quotient/product is `chi_-3`.

So the parity split

\[
\{\mathbf1,\chi_{-3}\}
\sqcup
\{\chi_{-4},\chi_{12}\}
\]

is intrinsic to multiplication by `zeta_12`, not imposed externally.

## 7. Guardrails [Audit]

- The character-line decomposition is over `Q`; it is not an integral direct-sum decomposition of `O_{K_12}`.
- The factors `1/2` and `3/2` in `[mathcal Z]_{B_chi}` are coordinate effects relative to the rational character basis.
- The correct integral carrier remains the ideal `P_2` used in the principal paper, where multiplication by `zeta_12` has an integral companion-type matrix.
- The `K_{2,2}` character support graph is not the geometric placement of the four cone shells `1,5,7,11`.
- No claim is made that shell adjacency implements cyclotomic multiplication.

## 8. Structural conclusion

The full `V4` character decomposition and the cyclotomic generator now fit together exactly:

\[
\boxed{
\mathbf Q(\zeta_{12})
=\bigoplus_{\chi\in\widehat{V_4}}L_\chi,
\qquad
\mathcal Z(L_\chi)
\subset
L_{\chi\chi_{-4}}
\oplus
L_{\chi\chi_{12}}.
}
\]

Hence multiplication by the primitive twelfth root is a two-channel intertwiner on the four character lines, with an intrinsic `chi_-3` bipartition. Its powers recover the expected cyclotomic hierarchy

\[
\mathcal Z^2=\times\zeta_{12}^2,
\qquad
\mathcal Z^3=\times i,
\qquad
\mathcal Z^6=-I,
\qquad
\mathcal Z^{12}=I.
\]

This supplies the operator-level `V4` intertwiner graph sought after `v13.421` while preserving the project's carrier-separation guardrails.
