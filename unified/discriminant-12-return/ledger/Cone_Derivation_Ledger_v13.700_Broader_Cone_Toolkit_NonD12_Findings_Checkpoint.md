# Cone Derivation Ledger v13.700 — Broader Cone Toolkit / Non-D12 Findings Checkpoint

Date: 2026-09-23

Status: cross-thread consolidation and research-spine checkpoint. This entry deliberately steps back from the D12-return specialization and records the broader tools that are already exact, audited, or sharply open.

Status labels: **[A]** independently audited/exact, **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization

Immediately before this write the live head was v13.699, commit \`c7b788f65ea14f16f6650ac71319c5dd21c412b1\`. No v13.700 collision was present.

This checkpoint incorporates the audited cone-complexification handoff v13.656, the earlier complexification audits v13.539/v13.542/v13.544, the HM/GM/AM/QM revival v13.690–695, and the reflection analysis v13.696–699.

## 1. Research hierarchy: D12 is a specialization, not the ambient theory

The current evidence supports the following hierarchy:

\[
\boxed{
\text{additive log coordinate}
\to
\text{positive multiplicative flow}
\to
\text{complex multiplicative/phase extension}
\to
\text{finite torsion/reflection groups}
\to
\text{arithmetic specializations such as D12}.
}
\]

The D12 carrier is therefore to be treated as one arithmetic discretization/selection mechanism inside a larger geometric/operator toolkit.

[G] No result below should be retroactively described as “caused by D12” unless the arithmetic specialization is explicitly used in its proof.

## 2. Real exponential/logarithmic spine [D]

For positive factor/null coordinates
\[
x=T+X,\qquad y=T-X,\qquad xy=G^2>0,
\]
define
\[
s=\frac12\log\frac{x}{y}.
\]
Then
\[
x=Ge^s,\qquad y=Ge^{-s},
\]
and
\[
\boxed{
T=G\cosh s,\qquad X=G\sinh s.
}
\]

Thus the fixed-product hyperbola is the exponential image of the additive rapidity line:
\[
\boxed{
(\mathbb R,+)\xrightarrow{\exp}(\mathbb R_{>0},\times).
}
\]

Factor exchange is inversion:
\[
x\leftrightarrow y
\iff
e^s\leftrightarrow e^{-s}
\iff
s\mapsto-s
\iff
X\mapsto-X.
\]

This structure is continuous and independent of D12.

### Export value

- **Suzuki/operator threads:** additive generator \(\leftrightarrow\) multiplicative evolution, with \(\log\) as the linearizing coordinate.
- **Hilbert–Pólya exploration:** useful representation template for comparing self-adjoint generators, exponentials, Cayley transforms, and unitary/positive flows; not itself an HP construction.
- **Magnetic/Floquet thread:** same additive-generator/exponential-evolution architecture appears in propagators; comparison is structural only until an explicit intertwiner is proved.

## 3. Two distinct circle bridges from rapidity [D/G]

The real normalized cone gives
\[
u=\frac XT=\tanh s,\qquad
g=\frac GT=\operatorname{sech}s,
\qquad
u^2+g^2=1.
\]
Writing
\[
u=\sin\theta,\qquad g=\cos\theta
\]
gives
\[
\boxed{
\sin\theta=\tanh s,\quad
\cos\theta=\operatorname{sech}s,\quad
\tan\theta=\sinh s,
}
\]
and
\[
\boxed{d\theta=\operatorname{sech}s\,ds.}
\]

Separately, analytic complexification of the exponential coordinate gives
\[
e^s\rightsquigarrow e^{i\phi}.
\]

[G] These are not the same map. The first is a real nonlinear compactification of hyperbolic coordinates onto a circle; the second is analytic continuation/complex phase. Their coexistence is potentially useful and must not be collapsed into one “complexification.”

## 4. Candidate ambient multiplicative group C* [D/O]

Every nonzero complex number has polar form
\[
w=\rho e^{i\phi},
\qquad
\rho>0,
\]
so
\[
\mathbb C^\times\cong\mathbb R_{>0}\times U(1)
\]
as real Lie groups.

The cone already supplies a natural positive multiplicative coordinate
\[
\rho=e^s,
\]
while the complexified fixed-shell geometry supplies phase rotations \(e^{i\phi}\).

Therefore the natural candidate combined coordinate is
\[
\boxed{
w=e^{s+i\phi}.
}
\]

[D] Algebraically,
\[
w_1w_2=e^{(s_1+s_2)+i(\phi_1+\phi_2)},
\]
so \((s,\phi)\) linearize the universal-cover group law.

[O] What is **not yet proved** is that the project's concrete cone operators realize a faithful/global \(\mathbb C^\times\)-action on one common representation preserving the required cone/operator structures. That is now a primary non-D12 gate.

## 5. Audited finite complexification structures [A]

The dormant complexification branch v13.534–549, consolidated at v13.656, established:

1. A complexified arithmetic-negation lift \(A\) of order four with
   \[
   A^2=R_Y.
   \]
   The generated group \(G_{\rm lift}=\langle A,R_X\rangle\) has order 16 and
   \[
   G_{\rm lift}/\langle-I_3\rangle\cong D_8.
   \]

2. Three abstractly \(D_8\) actions exist but their natural generator labels are not simultaneously intertwineable. In particular,
   \[
   A^2=R_Y
   \]
   while for the intrinsic complex-plane quarter-turn \(J\),
   \[
   J^2=-I\ne C.
   \]
   This is an exact obstruction.

3. Adjoining the intrinsic quarter-turn gives
   \[
   \boxed{
   G_{\rm lin}\cong C_4\times S_4,\qquad |G_{\rm lin}|=96,
   }
   \]
   with scalar center
   \[
   \mu_4=\{I,iI,-I,-iI\}.
   \]

4. The determinant-one \(S_4\) has a natural six-null-ray orbit \(N_6\). This is **not** the tetrahedral-edge action. Exact cycle-type comparison disproved that identification.

5. Instead,
   \[
   \boxed{N_6\cong S_4/C_4}
   \]
   equivariantly, realized as oriented cyclic orderings of \(\{1,5,7,11\}\) modulo rotation.

6. Orientation reversal of that cyclic order requires a semilinear/antilinear operator; no complex-linear operator realizes it.

7. The full semilinear closure is
   \[
   \boxed{
   \widetilde G\cong S_4\times D_8,\qquad |\widetilde G|=192.
   }
   \]
   The \(D_8\) factor is generated by central \(iI\) and semilinear reversal \(\mathcal R\), with
   \[
   \mathcal R(iI)\mathcal R^{-1}=-iI.
   \]

These are broad complex/operator results and should not be filed mentally as D12-only.

## 6. The central C4 / cyclotomic-i question [O]

The most repeated open question in v13.534–549 remains:
\[
\boxed{
\langle iI\rangle\stackrel{?}{=}\text{the existing cyclotomic }Z^3=\times i
}
\]
in a shared representation.

Recent work sharpens why this matters. The project now has the audited intrinsic leg
\[
\chi_{-4}\leftrightarrow R_Y
\]
coming from
\[
\sigma_r(i)=\chi_{-4}(r)i.
\]

If the central \(C_4\) really is the same cyclotomic \(i\)-rotation, then
\[
\langle i,\text{conjugation}\rangle
\]
naturally produces the dihedral relation
\[
CiC^{-1}=i^{-1},
\]
giving a conceptually clean source for a \(D_8\) factor.

This is now the highest-priority exact gate in the complexification lane.

## 7. Primitive reflection toolkit [A/D]

The current reflection triangle is exact:
\[
\boxed{
(5,\chi_{-3},R_X)\,
(7,\chi_{-4},R_Y)
=
(11,\chi_{12},R_XR_Y).
}
\]

The operations have independent continuous meanings:

- \(R_X\): factor exchange \(x\leftrightarrow y\), rapidity reversal \(s\mapsto-s\);
- \(R_Y\): complex conjugation \(z=X+iY\mapsto\bar z\);
- \(R_XR_Y\): fixed-\(T\) half-turn \(z\mapsto-z\).

This is useful beyond D12 because \(R_X,R_Y\) are intrinsic cone symmetries; D12 supplies distinguished arithmetic labels for them.

## 8. Mean/Casimir identities as a continuous algebraic toolkit [A/D]

For positive \(x,y\):
\[
A=\frac{x+y}{2},\quad
D=\frac{x-y}{2},\quad
G=\sqrt{xy},\quad
H=\frac{2xy}{x+y},\quad
Q=\sqrt{\frac{x^2+y^2}{2}},\quad
C=\frac{x^2+y^2}{x+y}.
\]

Exact identities:
\[
\boxed{A^2=G^2+D^2},
\]
\[
\boxed{AH=G^2},
\]
\[
\boxed{Q^2=A^2+D^2},
\]
\[
\boxed{AC=Q^2},
\]
\[
\boxed{H+C=2A},
\]
\[
\boxed{2A^2=G^2+Q^2}.
\]

At fixed \(A\),
\[
H=A-\frac{D^2}{A},
\qquad
C=A+\frac{D^2}{A},
\]
giving a mirror-parabola pair.

At fixed \(G\), rapidity gives
\[
Q^2=G^2\cosh 2s.
\]

These identities are continuous; their arithmetic residues are secondary specializations.

## 9. Divisor-summatory / fractional-part bridge [A]

The project has an exact non-D12 identity
\[
D(n)=\sum_{k\le n}\left\lfloor\frac nk\right\rfloor
=nH_n-\sum_{k\le n}\left\{\frac nk\right\}.
\]

For the centered difference coordinate
\[
X_k=\frac{k^2-n}{2k},
\]
the old geometric coordinate \(v_k=-X_k\) satisfies
\[
\boxed{
2\bigl((-X_k)\bmod\tfrac12\bigr)=\left\{\frac nk\right\}.
}
\]

Thus the mod-\(1/2\) quotient is native to the centered cone/factor geometry and directly encodes divisor fractional parts.

This is potentially relevant to analytic-number-theory threads independently of D12 characters.

## 10. Operator-theoretic export lane: Suzuki [O]

A promising reusable architecture is
\[
\boxed{
\text{operator/contraction}
\to
\text{Cayley coordinate}
\to
\log
\to
\text{additive spectral/rapidity variable}.
}
\]

The cone side independently has
\[
\boxed{
\text{positive multiplicative coordinate}
\xleftrightarrow{\log/\exp}
\text{additive rapidity}.
}
\]

The research question is therefore not merely whether D12 residues appear in Suzuki, but whether an explicit operator variable in the Suzuki/Friedrichs/Kreĭn framework is intertwined with the cone's logarithmic coordinate.

[O] No such intertwiner is yet proved here. This is an export target, not a theorem.

## 11. Hilbert–Pólya/RH relevance: disciplined scope [G/O]

The broader toolkit contains ingredients common in spectral formulations:

- additive generators and exponential flows;
- real/complex multiplicative coordinates;
- reflections and semilinear conjugations;
- finite unitary/torsion subgroups;
- Cayley/log linearization candidates;
- determinant and boundary-operator structures in the Suzuki lane.

[G] None of this proves RH, constructs the required Hilbert–Pólya operator, or establishes a spectral determinant equal to \(\xi\).

A genuine HP result would still require, at minimum, a specified positive Hilbert space, a closed self-adjoint operator, an exact spectral/determinant relation to the zeta/xi zeros, and completeness/no spurious spectrum.

The value of the current work is as a **toolkit for posing and testing such constructions**, not as evidence that the conjecture is solved.

## 12. Cross-thread export matrix

| Tool/result | D12 return | Suzuki/L-function | HP/RH | Magnetic/Floquet | Complexification |
|---|---|---|---|---|---|
| \(\log/\exp\) rapidity | useful | high priority | structural | structural | fundamental |
| real circle compactification | useful | possible kernel coordinate | structural | phase comparison | fundamental |
| \(C^\times\) candidate | optional | high-interest | structural | high-interest | primary |
| \(R_X,R_Y\) reflections | arithmetic labels | symmetry test | structural | parity test | fundamental |
| \(C_4,\ D_8\) finite lifts | arithmetic specialization | representation test | structural | symmetry analogy | established |
| \(S_4/C_4\) six-ray carrier | open | low/unknown | low/unknown | low/unknown | established |
| divisor mod-\(1/2\) bridge | useful | high-interest | analytic-number-theory | low | independent |
| RMS/Casimir mean algebra | useful | possible coordinate transform | structural | quadratic comparison | independent |

## 13. Prioritized non-D12 gates

1. **Resolve central \(C_4\) versus cyclotomic \(Z^3=\times i\).**
2. **Construct/test a genuine \(\mathbb C^\times\) action** combining \(e^s\) and \(e^{i\phi}\) in one representation, and identify its kernel/stabilizers.
3. **Map the cone log coordinate into the Suzuki Cayley/log machinery** by explicit formulas, not analogy.
4. **Revisit the divisor fractional-part bridge** as an analytic-number-theory tool without imposing \(\chi_{12}\).
5. **Only then ask whether the larger structure yields new D12/Pell, Suzuki positivity, or HP consequences.**

## 14. Guardrail summary

- D12 is a specialization, not the ambient continuous theory.
- Real circle compactification and analytic phase complexification are distinct.
- The \(C^\times\) organization is a candidate ambient group until an explicit common action is proved.
- The old tetrahedral-edge identification of the six-ray orbit is false and closed.
- The v13.536 determinant-sign error is known and superseded; use the corrected later model.
- No HP/RH or Suzuki spectral consequence is promoted without an explicit operator-level bridge.

## 15. Immediate continuation

Proceed first with Gate 1: place the old central \(iI\) operator and the existing cyclotomic \(Z^3\) operator into a common representation, compare their matrices/actions exactly, and determine whether equality, conjugacy, projective equality, or obstruction holds.
