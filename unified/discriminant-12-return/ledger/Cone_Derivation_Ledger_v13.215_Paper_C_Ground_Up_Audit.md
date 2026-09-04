# Cone Derivation Ledger v13.215 — Paper C Ground-Up Audit

Date: 2026-09-04

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [I] interpretation, [O] open.

## Scope

This checkpoint audits

`foundations/PaperC_QuantumRealizations.tex`

against the now-audited continuous foundation

`foundations/PaperB_EigenCoordinates_v2.1.tex`

and against the source-status / two-mode guardrails already established in

`foundations/Casimir_Null_Diamond_Standalone_v2.1.tex`.

Paper C is not promoted by this checkpoint. The purpose is to determine which mathematical statements survive, which require correction, and which claims must be weakened before a corrected next version is created.

## Overall result

**Core operator algebra: PASS with corrections.**

The Schwinger `SU(2)` realization, the two-mode `SU(1,1)` commutators and Casimir, the exact coherent-state occupation formulas, the exact mean-field residual formula after correcting its parameter notation, the generic-ellipse selection rule, and the generic-ellipse revival operator identity all survive direct audit.

The current manuscript nevertheless cannot be treated as publication-authoritative because several framing and theorem-strength statements are stale or too strong.

## 1. [Audit] Opening power-map premise is obsolete after Paper B v2.1

The abstract currently says that the companion paper attaches to **every** cone-symmetry generator an exact power map that sends one orbit to a larger one of the same shape. The introduction repeats the same universal framing.

This is no longer the audited Paper-B theorem.

Paper B v2.1 distinguishes:

1. nonparabolic intrinsic normalized orbit coordinates
   \[
   |z|=1,
   \qquad
   \xi_+\xi_-=1,
   \]
   with intrinsic power self-maps
   \[
   z\mapsto z^n,
   \qquad
   (\xi_+,\xi_-)\mapsto(\xi_+^n,\xi_-^n);
   \]
2. exact but **chosen-equation-dependent** level-raising lifts built from the unnormalized eigen-coordinates;
3. the parabolic boundary, where the diagonal eigen-coordinate construction fails, although coordinatewise factor powers still exist.

Paper C must be rewritten around this hierarchy. It must not say that every generator carries one canonical exact orbit-enlarging power map.

## 2. [D] `SU(2)` Schwinger realization survives

With
\[
J_+=a_1^\dagger a_2,
\qquad
J_-=a_2^\dagger a_1,
\qquad
J_z=\frac{n_1-n_2}{2},
\]
the standard relations
\[
[J_z,J_\pm]=\pm J_\pm,
\qquad
[J_+,J_-]=2J_z
\]
are correct.

For total number
\[
N=n_1+n_2,
\]
the Schwinger representation has
\[
j=\frac N2,
\qquad
J^2=j(j+1).
\]
Under the Paper-C state dictionary
\[
x=n_1+1,
\qquad
y=n_2,
\]
we have
\[
T=\frac{N+1}{2}=j+\frac12,
\qquad
J_z=X-\frac12.
\]

The centrality no-go inside a fixed `SU(2)` action is sound: `SU(2)` rotations cannot change the spin sector.

### [Audit] strengthen the proof of `T` conservation

The present manuscript infers conservation of `T` from conservation of the Casimir expectation. For arbitrary superpositions of spin sectors, the cleaner exact operator statement is
\[
[N,J_x]=[N,J_y]=[N,J_z]=0,
\]
so
\[
[T,J_i]=0,
\qquad
T=\frac{N+1}{2}.
\]

This proves directly, for every state, that any unitary generated inside the Schwinger `su(2)` algebra preserves the complete `T` distribution, not merely the expectation of `J^2`.

The publication rewrite should use this direct statement while retaining Casimir centrality as the representation-theoretic explanation.

## 3. [Audit] global positive-discrete-series Bargmann index is incorrect

The manuscript currently states
\[
k=\frac{n_1-n_2+1}{2}=X
\]
as the positive-discrete-series Bargmann index for **every** Fock state.

The computed Casimir is correctly
\[
C=\frac{(n_1-n_2)^2-1}{4}.
\]
But the standard positive-discrete-series parameter is
\[
\boxed{
k=\frac{|n_1-n_2|+1}{2}.
}
\]

Let
\[
d=n_1-n_2.
\]
Then:

- in the oriented sector `d>=0`,
  \[
  k=\frac{d+1}{2}=X;
  \]
- in the opposite sector `d<0`, `X=(d+1)/2` is not the positive Bargmann index.

The exact conserved operator is the number difference
\[
D=n_1-n_2,
\]
or equivalently the oriented coordinate
\[
X=\frac{D+1}{2}.
\]
The positive-discrete-series label is a sector function of `|D|`, not globally identical to `X`.

This is the same correction already recorded during the null-diamond audit and must now be applied directly to Paper C.

## 4. [Audit] superpositions across number-difference sectors

The current text says that `X` is “the Bargmann index, a bona fide quantum number” under arbitrary `SU(1,1)` evolution for every state.

Correct statement:

\[
[D,K_z]=[D,K_+]=[D,K_-]=0.
\]

Therefore the Hilbert space decomposes into invariant fixed-`d` sectors. Each fixed-`d` sector carries a positive discrete series with
\[
k=\frac{|d|+1}{2}.
\]

A superposition of different `d` sectors remains a superposition of sectors; it does not possess one single Bargmann index. The signed coordinate `X=(D+1)/2` is nevertheless an exactly conserved operator.

Publication language must distinguish these two facts.

## 5. [D] coherent-state occupation formulas survive

For two-mode squeezing
\[
S(r)=\exp[r(K_+-K_-)],
\]
the manuscript's exact formulas
\[
\langle n_1(r)\rangle
=(\alpha_1\cosh r+\alpha_2\sinh r)^2+\sinh^2r,
\]
\[
\langle n_2(r)\rangle
=(\alpha_2\cosh r+\alpha_1\sinh r)^2+\sinh^2r
\]
for real coherent amplitudes are correct.

Their difference is exactly conserved:
\[
\langle n_1(r)-n_2(r)\rangle
=\alpha_1^2-\alpha_2^2.
\]

This is the mean-value consequence of the exact operator conservation of `D=n1-n2`.

## 6. [Audit] mean-field residual has an argument-label error

The manuscript defines
\[
T_q(r)
=\frac{\langle n_1(r)\rangle+\langle n_2(r)\rangle+1}{2},
\]
and the classical flow parameter `phi` is related to squeezing by
\[
\phi=2r.
\]

Direct expansion gives
\[
T_q(r)
=T_0\cosh(2r)+\alpha_1\alpha_2\sinh(2r).
\]
Therefore the exact comparison is
\[
\boxed{
T_q(r)-T_{\rm cl}(2r)
=Y_0\sinh(2r)
\left(\sqrt{1-\frac1{x_0}}-1\right).
}
\]

The current theorem instead writes `T_q(2r)-T_cl(2r)` while the proof still uses the squeezing parameter `r`. The table likewise labels `T_q(0.6)` while its caption says `r=0.3`, `phi=0.6`.

This is a notation/argument error, not a failure of the residual formula itself. The corrected next version should consistently write either:

- `T_q(r)` versus `T_cl(2r)`, or
- reparameterize the quantum trajectory as `\widetilde T_q(phi):=T_q(phi/2)` and compare both at `phi`.

The latter is probably cleaner for publication.

## 7. [Audit] asymptotic error language needs the scaling variable stated carefully

The factor
\[
\sqrt{1-1/x_0}-1
=-\frac1{2x_0}+O(x_0^{-2}).
\]

Thus the residual itself is
\[
-\frac{Y_0}{2x_0}\sinh(2r)+O\!\left(\frac{Y_0}{x_0^2}\right).
\]

Calling the **absolute residual** simply `O(1/x_0)` is only correct when the scaling of `Y_0` is controlled. The table appears to scale both coherent amplitudes together, in which case the **relative error** is `O(1/x_0)` while the absolute residual can remain order one depending on the path in parameter space.

The next version should state explicitly whether the asymptotic claim concerns the bracket factor, absolute residual, or relative error under a specified joint scaling of `(x0,y0)`.

## 8. [Audit] the `B_X` Gaussian no-go is not yet proved at theorem strength

The manuscript argues that all two-mode quadratic Hermitian generators are either passive or active, then claims:

- passive transformations fail because they conserve total number;
- active transformations necessarily introduce vacuum-fluctuation additive terms;
- therefore no quadratic/Gaussian unitary can reproduce the exact classical `B_X` flow.

The passive half is clear.

The active half is plausible and consistent with general Bogoliubov structure, but the manuscript does not prove the required universal statement for an arbitrary two-mode symplectic/Bogoliubov generator and arbitrary coherent input. In particular, it does not derive a general normal form showing that no allowed `U,V` Bogoliubov blocks can satisfy simultaneously, for all inputs and all flow parameters,
\[
x(\phi)=e^\phi x_0,
\qquad
y(\phi)=e^{-\phi}y_0
\]
under the shifted dictionary `x=n1+1`, `y=n2`.

Accordingly:

**Current status: strong structural evidence / partial no-go, not yet a proved universal Gaussian no-go theorem.**

The next version should either:

1. downgrade the section to a carefully scoped obstruction argument; or
2. supply a full symplectic/Bogoliubov proof.

No claim about non-Gaussian realizations is justified.

## 9. [D] generic-ellipse selection rule survives

For the quantum mixed generator
\[
\mathcal G^{(q)}_{a,b}
=(a+b)(-iJ_y)
+\frac{a-b}{2}(K_+-K_-),
\]
the `J_y` term changes total number by `0` and the `K_\pm` terms change total number by `\pm2`.

Therefore the full exponential preserves total-number parity, and a state beginning in spin sector `j0` can occupy only sectors satisfying
\[
j-j_0\in\mathbb Z.
\]

This selection rule is exact.

### [Audit] notation collision with Paper B v2.1

Paper B v2.1 now reserves
\[
\widehat G_{a,b}=\frac{G_{a,b}}{2\sqrt{|ab|}}
\]
for the normalized **classical Lorentz generator**.

Paper C currently uses `\hat G_{a,b}` for the quantum anti-Hermitian generator. This is now unnecessarily ambiguous.

The corrected Paper C should rename the quantum generator, for example
\[
\mathcal G^{(q)}_{a,b}.
\]

## 10. [D] generic-ellipse revival identity survives and can be strengthened algebraically

For `ab>0`, the Heisenberg matrix written in the manuscript is
\[
A=
\begin{pmatrix}
0&-p&0&m\\
p&0&m&0\\
0&m&0&-p\\
m&0&p&0
\end{pmatrix},
\qquad
p=\frac{a+b}{2},
\quad
m=\frac{a-b}{2}.
\]

Direct multiplication gives the stronger exact identity
\[
\boxed{A^2=-ab\,I_4.}
\]

Hence, with
\[
T_{\rm cl}=\frac{\pi}{\sqrt{ab}},
\]
we obtain immediately
\[
e^{T_{\rm cl}A}=-I_4,
\qquad
e^{2T_{\rm cl}A}=I_4.
\]

Therefore, for the corresponding Fock-space unitary `U`,
\[
U(T_{\rm cl})
=e^{i\alpha}(-1)^{N},
\]
up to a scalar phase, and
\[
U(2T_{\rm cl})
=e^{2i\alpha}I.
\]

This operator theorem is sound. The next version should use `A^2=-ab I` rather than relying on a statement that symbolic exponentiation was checked.

## 11. [Audit] “precisely” / minimal-period language is too strong

The operator identity proves that:

- every total-parity eigenstate revives **at** one classical period, up to phase;
- every state revives **by** two classical periods, up to phase.

It does **not** prove that these are the minimal revival times for every individual state. Some special states can have shorter periods.

Therefore words such as “precisely one period,” “precisely twice the period,” or “exactly periodic at period `2T_cl`” should be replaced by statements about guaranteed revivals at those times unless minimality is separately proved.

## 12. [Audit] discussion currently contradicts the revival theorem

The discussion says that the generic elliptic generator “reproduces its classical period exactly, for every state.”

But the theorem itself gives
\[
U(T_{\rm cl})=e^{i\alpha}(-1)^N,
\]
which is not a scalar on an arbitrary superposition of even and odd total-number sectors.

Thus an arbitrary state need not revive at one classical period. The correct statement is:

- the **Heisenberg canonical variables** acquire a sign after one classical period;
- definite parity / definite total-number states revive up to phase at one classical period;
- arbitrary states are guaranteed to revive up to phase at two classical periods.

This distinction must be made consistently in the abstract, theorem discussion, table, and conclusion.

## 13. [Audit] Paper-C state dictionary versus four-corner transition cell

The state dictionary
\[
x=n_1+1,
\qquad
y=n_2
\]
is useful and should be retained.

However, the audited null-diamond foundation now establishes the four-corner transition cell
\[
[p,p+1]\times[q,q+1]
\]
and shows that the Paper-C state point corresponds to one transition vertex of that cell, not literally to the cell center.

Paper C need not import the full null-diamond construction, but its next version should add a short guardrail so later readers do not identify its state point with the centered factor cell used in the Casimir-completion theorem.

## 14. [Audit] source architecture and bibliography

The bibliography entry for the eigen-coordinate companion still uses the older title

> *Every Cut Is an Orbit: Eigen-Coordinates and a Power-Map Companion to the Cutting-Plane Theorem*.

The authoritative Paper B source is now

`PaperB_EigenCoordinates_v2.1.tex`

with title

> *Signed Cone Cuts as Lorentz Orbits: Eigen-Coordinates and Power Maps*.

Paper C should cite the current title and theorem hierarchy.

## Publication classification after audit

### PASS / retain

- Schwinger `SU(2)` commutators and spin decomposition;
- `SU(2)` fixed-sector / total-number conservation;
- two-mode `SU(1,1)` commutators;
- Casimir value `((n1-n2)^2-1)/4`;
- exact conservation of number difference;
- exact coherent-state occupation formulas;
- exact quantum/classical residual formula after parameter relabeling;
- generic-ellipse total-parity selection rule;
- generic-ellipse Heisenberg revival identity, strengthened by `A^2=-ab I`;
- scope guardrail that no “cone is secretly quantum” claim is established.

### CORRECT / rewrite

- obsolete universal Paper-B power-map premise;
- global `k=X` positive-discrete-series statement;
- Bargmann-index language for superpositions;
- `T_q(2r)` argument error;
- asymptotic `O(1/x0)` wording;
- collision between classical `\widehat G` and quantum `\hat G` notation;
- minimal-period / “precisely” language;
- claim that every state reproduces the classical period at one period;
- current Paper-B bibliography/title.

### DOWNGRADE OR PROVE

- universal two-mode Gaussian no-go for `B_X`.

## Foundation status

Paper C remains:

**ACTIVE FOUNDATION MATERIAL / NEEDS RECONCILIATION**.

It should not yet be treated as an audited publication baseline.

## Next task

Create a corrected next Paper-C version only after applying all of the above at once. The rewrite should preserve the exact operator results while reorganizing the narrative around the audited Paper-B distinction:

\[
\text{intrinsic projective orbit dynamics}
\quad\text{vs.}\quad
\text{chosen-equation level-raising lift}.
\]

The build/CI policy should then be applied in the same change set: settle the corrected Paper-C filename first, add a foundation-local build script if none exists, and only then add/update a matching workflow and compiled publication output.
