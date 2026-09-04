# Cone Derivation Ledger v13.202 — Paper B Initial Orbit Audit

Status: **[Audit] first-pass dependency and theorem audit**

Source audited:

`unified/discriminant-12-return/foundations/PaperB_EigenCoordinates.tex`

## 1. Role of Paper B

Paper B is structurally the Lorentz-dynamics companion to Paper A. Its intended chain is:

\[
\text{Paper A plane section}
\longrightarrow
\mathfrak{so}(2,1)\text{ generator}
\longrightarrow
\text{one-parameter orbit}
\longrightarrow
\text{eigen-coordinate / power map}.
\]

The natural decomposition for the unified project is:

- **Paper-A dependency:** cone coordinates and the line-plane equation
  \[
  (a-b)X+(a+b)T=c.
  \]
- **Paper-B-specific:** the Lorentz generator attached to that plane, its spectral type, orbit parametrization, and eigen-coordinate constructions.
- **Discriminant-12 bridge:** the special hyperbolic boost representation should be connected later to the audited Pell return, but Paper B should not depend on discriminant-12 arithmetic for its basic proofs.
- **Area branch:** no area theorem is needed for the orbit classification.

## 2. [Audit] Paper A theorem restatement is now stale

Paper B currently restates Paper A as:

> ellipse if `ab>0`, parabola if `ab=0`, hyperbola if `ab<0`.

The audited Paper A theorem now requires the degenerate exception:

\[
ab<0,\ c\ne0 \Rightarrow \text{nondegenerate hyperbola},
\]

while

\[
ab<0,\ c=0
\]

gives a degenerate generator section of the full cone (and a single positive-factor ray on the upper cone).

Paper B must inherit this corrected hypothesis before publication.

## 3. [D] Generator and spectrum survive the first algebra check

Paper B defines

\[
G_{a,b}=(a+b)L+(a-b)B_Y.
\]

In the basis `(X,Y,T)`, writing

\[
A=a+b,\qquad D=a-b,
\]

gives

\[
G_{a,b}=
\begin{pmatrix}
0&-A&0\\
A&0&D\\
0&D&0
\end{pmatrix}.
\]

For

\[
m=(D,0,-A),
\]

direct multiplication gives

\[
G_{a,b}m=0.
\]

The characteristic polynomial is

\[
\lambda\bigl(\lambda^2+4ab\bigr),
\]

so the stated spectral trichotomy is correct:

\[
ab>0:\quad 0,\ \pm2i\sqrt{ab},
\]

\[
ab<0:\quad 0,\ \pm2\sqrt{-ab}.
\]

The Minkowski norm of the plane normal is likewise

\[
(a-b)^2-(a+b)^2=-4ab.
\]

Thus the exact identification

\[
\boxed{\text{conic sign }ab\ \leftrightarrow\ \text{Lorentz causal/spectral type}}
\]

survives the first audit.

## 4. [Audit] Proof text in Theorem 3.1(a) is internally garbled

The current proof says that for `G=alpha L+gamma B_Y`, the equation `Gm=0` forces conditions including

\[
\gamma m_3=0,\qquad \gamma m_1=0,
\]

and then says this "forces the `B_X`-component to vanish," although no `B_X` component appears in that displayed `G`.

That prose is not the correct direct multiplication. The clean calculation is simply

\[
G_{a,b}(a-b,0,-(a+b))^T=0.
\]

The theorem itself survives; the proof should be rewritten.

## 5. [Audit] "complete orbit" currently overstates the positive-factor trace

This is the largest first-pass issue.

Paper A's factor map uses

\[
Y=\sqrt{xy}\ge0,
\]

so the multiplication-table image occupies the **upper** cone / upper half of each fixed-`T` circle.

But the one-parameter Lorentz subgroup acts on the full cone. For example, when `a=b`,

\[
G_{a,a}=2aL,
\]

and the full `L`-orbit is a complete circle in the `(X,Y)` plane, including `Y<0`. The actual positive-factor trace is only the `Y\ge0` semicircle.

Therefore the current global wording

> "the full curve that `ax+by=c` traces on the cone is a single orbit"

is not publication-safe if "traces" means the Paper-A positive-factor image.

A safer structure is:

1. the full algebraic plane-cone section is an orbit or union of orbit components of the corresponding one-parameter subgroup;
2. the positive-factor trace is the portion of that orbit lying in
   \[
   T>0,\qquad Y\ge0,
   \]
   with any additional connected-component restriction made explicit.

For hyperbolic sections, connected-component/branch issues must also be checked before claiming a single full orbit.

## 6. [Audit] Dimension argument in Theorem 3.1(c) is insufficient

The proof currently argues that because the non-kernel eigenspace is two-dimensional and the conic is one-dimensional, the one-parameter orbit equals the whole conic.

This does not establish global orbit equality. A one-parameter orbit is one-dimensional regardless of the dimension of the nonzero eigenspace, and containment in a one-dimensional invariant curve gives at most a local/open-orbit statement without a connectedness/completeness argument.

The repair should proceed by explicit canonical conjugacy:

- timelike axis (`ab>0`) -> conjugate to a rotation `L`;
- spacelike axis (`ab<0`) -> conjugate to a boost;
- null axis (`ab=0`) -> parabolic generator.

Then determine exactly which connected component of the plane-cone section each orbit covers and intersect with the positive-factor chamber.

## 7. [Audit] Abstract spectral wording should be normalized

The abstract says the nonzero eigenvalues are "equal to `±2 sqrt(-ab)` up to sign." This obscures the elliptic case. Publication-safe wording is

\[
\lambda^2=-4ab,
\]

or explicitly

\[
ab>0:\ \lambda=\pm2i\sqrt{ab},\qquad
ab<0:\ \lambda=\pm2\sqrt{-ab}.
\]

## 8. [D] Strongest result currently retained

The strongest theorem-level statement supported by the initial audit is:

> For the plane `(a-b)X+(a+b)T=c`, the Lorentz generator
> \[
> G_{a,b}=(a+b)L+(a-b)B_Y
> \]
> preserves the plane, and its nonzero spectral square
> \[
> \lambda^2=-4ab
> \]
> is exactly the Minkowski norm of the plane normal. Hence the Paper-A ellipse/parabola/hyperbola sign invariant is the same invariant that classifies the corresponding Lorentz generator as elliptic/parabolic/hyperbolic, subject to the degenerate `c=0` edge case and to explicit orbit-component/chamber restrictions.

## Next audit pass

Before editing Paper B, inspect Sections 4–8 in full, with special attention to:

- normalization of the complex/split-complex eigen-coordinate;
- whether `|zeta|=c` should be `|c|` or requires `c>0` normalization;
- whether raising the eigen-coordinate to the `n`th power really lands on `ax+by=c^n` without hidden scaling factors or branch restrictions;
- the constant-product power map;
- the claim that no power map exists for `ab=0`;
- compatibility with Paper A's now-fixed `X=(x-y)/2` convention;
- the exact bridge, if any, from Paper B's `B_X` boost to the discriminant-12 Pell return.
