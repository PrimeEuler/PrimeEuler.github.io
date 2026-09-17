# Cone Derivation Ledger v13.540 — Null Six-Orbit and the S4 Edge Action

## Status
Exact finite-group computation / correction of the proposed four-null-direction test. Exploratory bridge only; no main theorem promotion.

## Pre-write synchronization
Immediately before this write, the latest ledger-numbered commits visible were v13.539 (External Audit Round 45) and a concurrent v13.537 Suzuki entry. Therefore this entry uses v13.540.

The audit also corrected two nearby points: the earlier v13.536 split-quaternion determinant framing had a sign/axis error, while the later split-matrix model below has the correct determinant; and the literal statement `D^2=H` in the prior split-matrix entry was imprecise although the induced relation A^2=R_Y remains correct. This entry uses only the verified 3x3 action and the correct split-matrix cone.

## Correct split-matrix cone
Use

\[
Q(X,Y,T)=\begin{pmatrix}T+X&Y\\Y&T-X\end{pmatrix},
\qquad
\det Q=T^2-X^2-Y^2.
\]

Hence the complexified projective null cone is

\[
X^2+Y^2=T^2.
\]

The previously verified generators on `(X,Y,T)` are

\[
A=\begin{pmatrix}0&0&-1\\0&i&0\\-1&0&0\end{pmatrix},\quad
R_X=\operatorname{diag}(-1,1,1),\quad
R_Y=\operatorname{diag}(1,-1,1),\quad
J=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}.
\]

Their closure has order 96, and its determinant-one kernel `H` has order 24 and is isomorphic to S4 (as independently audited in Round 45).

## No invariant four-point null orbit
The natural request was to find four distinguished null projective directions permuted by H as the tetrahedral four-set. Direct orbit closure shows that a coordinate null ray such as

\[
a=[1:0:1]
\]

has orbit of size **six**, not four. The complete orbit is

\[
\boxed{
\mathcal N_6=
\{[1:0:1],[1:0:-1],[0:1:1],[0:1:-1],[1:i:0],[1:-i:0]\}.
}
\]

Every representative satisfies `X^2+Y^2=T^2` exactly.

Thus the determinant-one S4 does **not** realize its natural degree-four tetrahedral permutation action on this null orbit. Instead it realizes the natural degree-six action of S4 on the six unordered pairs / six edges of a tetrahedron.

This is an important structural correction: the A3 tetrahedral vertices should not be identified directly with four null rays of this 3-dimensional cone representation.

## Explicit permutation generators on the six null rays
Label

\[
a=[1:0:1],\quad b=[1:0:-1],\quad c=[0:1:1],\quad d=[0:1:-1],\quad e=[1:i:0],\quad f=[1:-i:0].
\]

Choose the determinant-one order-four element

\[
r=J=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}
\]

and the determinant-one order-three element

\[
s=\begin{pmatrix}0&0&i\\1&0&0\\0&-i&0\end{pmatrix}.
\]

They generate all 24 elements of H. Their projective actions on `N_6` are

\[
\boxed{r=(a\ c\ b\ d),\qquad e,f\text{ fixed},}
\]

and

\[
\boxed{s=(a\ f\ d)(b\ e\ c).}
\]

Therefore the action is faithful and transitive on six points. Since H has order 24, this is exactly an S4 degree-six permutation representation.

## Tetrahedral-edge interpretation
S4 acts naturally on the six two-element subsets of a four-element set. The cycle types above match that edge action: an order-four vertex permutation induces a four-cycle on four edges while fixing the two opposite-edge directions; an order-three vertex permutation induces two disjoint three-cycles on the six edges.

Hence

\[
\boxed{\mathcal N_6\ \text{is naturally of tetrahedral-edge type, not tetrahedral-vertex type}.}
\]

This supplies a cleaner cone–A3 bridge than the attempted four-null-ray identification:

\[
\text{A3 tetrahedron: 4 vertices}\quad\leadsto\quad6\text{ edges}
\quad\longleftrightarrow\quad
\mathcal N_6\subset\mathbb P(\text{null cone}).
\]

The next exact task is to solve an explicit labeling of `a,...,f` by the six unordered pairs of `{1,5,7,11}` so that the already-known U(12)/A3 S4 generators have exactly the above permutations. That would give a concrete equivariant edge/null-ray intertwiner.

## Guardrails
1. There is no four-element null orbit established here; the directly computed distinguished orbit has six rays.
2. Do not identify A3 tetrahedral vertices themselves with these null rays.
3. The correct comparison is presently between the six tetrahedral edges (equivalently A3 positive-root directions up to sign) and the six projective null directions.
4. This is a finite representation-theoretic bridge, not yet a Pell-to-cone dynamical theorem.
5. Use the correct determinant `det Q=T^2-X^2-Y^2`; do not propagate the earlier v13.536 sign error.
