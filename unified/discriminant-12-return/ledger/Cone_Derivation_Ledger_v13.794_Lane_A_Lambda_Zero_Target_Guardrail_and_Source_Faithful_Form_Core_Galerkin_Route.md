# Cone Derivation Ledger v13.794 — Lane A Lambda-Zero Target Guardrail and Source-Faithful Form-Core Galerkin Route

Date: 2026-09-25

Lane: A.

Status: [P/D] direct Suzuki-v2 source qualification; [G] the \(\xi\)-target Schur hierarchy is a \(\lambda=0\) target, not universal in the auxiliary shift; [D] form-core Galerkin is the correct numerical realization of \(T_{a,\lambda}^{-1}e^x\); [C] identifies the admissible numerical branches.

Parents: v13.782, v13.786, v13.790–793.

## 0. Synchronization

Immediately before this write the live ledger head is v13.793. No collision is present.

Primary-source statements checked directly in Suzuki v2:

- Theorem 1.5 is built after choosing
\[
\lambda<\lambda_a,
\qquad
T_{a,\lambda}=A_a-\lambda I.
\]
- Section 7 explicitly assumes RH and then takes
\[
\lambda=0,
\qquad
T_{a,0}=A_a,
\]
because under RH \(A_a>0\) for all \(a\).
- The introduction states that the conjectural limit formula is formulated with this \(\lambda=0\) situation in mind.
- Suzuki remarks that, when \(A_a>0\), the Hilbert spaces for \(T_{a,\lambda}\) and \(A_a\) are isomorphic and the zeros of the characteristic are *expected* to be independent of the auxiliary \(\lambda\), but control of \(\lambda\) is itself part of the analytic difficulty.

## 1. Finite family is \(\lambda\)-dependent [D/G]

For every
\[
\lambda<\lambda_a,
\]
define
\[
T_{a,\lambda}=A_a-\lambda I.
\]

The canonical deficiency vector is
\[
\boxed{
v_{a,+i}^{(\lambda)}
=
T_{a,\lambda}^{-1}e^x.
}
\tag{1}
\]

Hence the one-function transform,
\[
F_{a,\lambda}(z)
=
\widehat{v_{a,+i}^{(\lambda)}}(z),
\]
the bounded quotient
\[
h_{a,\lambda}(z)
=
\frac{F_{a,\lambda}(z)}
{F_{a,\lambda}(-z)},
\]
the Weyl function
\[
m_{a,\lambda},
\]
and its Schur parameters
\[
\kappa_{n,a}^{(\lambda)}
\]
all depend on \(\lambda\) in general.

Therefore it is not source-faithful to compare an arbitrary shifted finite family directly to the Section-7 infinite \(\xi\)-target without controlling the shift.

## 2. The \(\xi\)-target hierarchy is the \(\lambda=0\) target [P/D]

Suzuki Section 7 proceeds under RH and explicitly replaces \(T_a\) by \(A_a\):
\[
\boxed{
T_{a,0}=A_a.
}
\tag{2}
\]

Accordingly the infinite functions in v13.790–793,
\[
m_\infty(z)
=
i\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)},
\]
\[
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1},
\]
and the scalar targets
\[
\kappa_{0,\infty},
\qquad
\kappa_{1,\infty},
\ldots
\]
must be interpreted as targets for the **unshifted**
\[
\boxed{
A_a^{-1}e^x
}
\]
family.

In particular,
\[
\boxed{
\kappa_{0,\infty}
\approx0.9968019520324009,
\qquad
\kappa_{1,\infty}
\approx-0.9954804115180577
}
\]
are not asserted as targets for a fixed \(\lambda\neq0\).

## 3. Unconditional versus target branches [G]

There are two distinct numerical/analytic branches.

### Branch U — unconditional finite operator study

Choose a rigorously admissible
\[
\lambda<\lambda_a.
\]
Then
\[
T_{a,\lambda}>0
\]
and all finite Schur/inner-function results of v13.790–793 hold for
\[
h_{a,\lambda}.
\]

This branch is source-faithful and unconditional at fixed \(a\), but it does **not** by itself test the Section-7 \(\xi\)-target.

### Branch X — \(\xi\)-target test

Use
\[
\lambda=0,
\qquad
T_{a,0}=A_a.
\]

This is the family relevant to Suzuki's Section-7 heuristic and to the targets \(\kappa_{n,\infty}\).

However, invertibility/positivity of \(A_a\) for every \(a\) is exactly tied to the global Weil-positivity/RH problem. Therefore any numerical use of \(A_a^{-1}\) is an experiment/diagnostic unless positivity and conditioning are separately certified for the tested finite \(a\).

The project must not turn successful finite-section inversion at \(\lambda=0\) into a proof of global positivity.

## 4. Why the Dirichlet form core is still the correct Galerkin route [P/D]

Suzuki proves that \(A_a\) is the Friedrichs extension of
\[
B_a=D^*G_aD
\]
with core domain
\[
H_0^1(-a,a),
\]
and that the infimum of the Rayleigh quotient may be taken over
\[
C_c^\infty(-a,a).
\]

Thus the fact that the true resolvent vector
\[
T_{a,\lambda}^{-1}e^x
\]
need not itself lie in \(H_0^1\) does **not** invalidate a form-core Galerkin method.

For \(\lambda<\lambda_a\), the coercive form
\[
\mathfrak t_{a,\lambda}[u,v]
=
Q_W^a(u,v)
-\lambda\langle u,v\rangle
\]
has \(C_c^\infty(-a,a)\) as a form core.

Therefore a nested Galerkin sequence
\[
V_N\subset H_0^1(-a,a)
\]
may solve the variational problem
\[
\boxed{
\mathfrak t_{a,\lambda}[v_N,\varphi]
=
\langle e^x,\varphi\rangle
\qquad
(\varphi\in V_N),
}
\tag{3}
\]
and, under the standard coercive Galerkin hypotheses,
\[
v_N\to T_{a,\lambda}^{-1}e^x
\]
in the \(T_{a,\lambda}\)-energy norm.

This is source-faithful even though each trial vector has Dirichlet traces and the limit need not.

## 5. Existing project matrices are compatible with this route [D/G]

The research-note matrices built from the direct Dirichlet basis
\[
\psi_n(x)
=
a^{-1/2}
\sin\!\left(
\frac{n\pi(x+a)}{2a}
\right)
\]
represent the source-level Weil quadratic form on a form core.

The basis is \(L^2\)-orthonormal, so the shifted finite Galerkin matrix is simply
\[
\boxed{
T_N^{(\lambda)}
=
A_N-\lambda I.
}
\tag{4}
\]

For the source
\[
e^x,
\]
define
\[
f_{N,n}
=
\langle\psi_n,e^x\rangle.
\]
Then the source-faithful finite solve is
\[
\boxed{
T_N^{(\lambda)}c_N=f_N.
}
\tag{5}
\]

The reconstructed trial function
\[
v_N=\sum_nc_{N,n}\psi_n
\]
may then be used to evaluate
\[
F_{N,a}(z)
=
\int_{-a}^{a}v_N(x)e^{izx}\,dx
\]
and the scalar Schur diagnostics.

The artificial endpoint rows of the deprecated first-kind Nyström code are not used.

## 6. Parity block reduction [D]

Odd basis index \(n\) gives an even primitive basis function; even \(n\) gives an odd one.

Because \(A_a\) commutes with reflection,
\[
A_N
=
A_N^{(+)}
\oplus
A_N^{(-)}.
\]

Likewise,
\[
e^x=\cosh x+\sinh x,
\]
so the Galerkin solve splits exactly:
\[
\boxed{
(A_N^{(+)}-\lambda I)c_{e,N}=f_{\cosh,N},
}
\tag{6E}
\]
\[
\boxed{
(A_N^{(-)}-\lambda I)c_{o,N}=f_{\sinh,N}.
}
\tag{6O}
\]

This produces the two energy components needed for the first scalar target:
\[
\kappa_{0,N}^{(\lambda)}
=
\frac{
\|v_{e,N}\|_{T_{N,\lambda}}^2
-
\|v_{o,N}\|_{T_{N,\lambda}}^2
}{
\|v_{e,N}\|_{T_{N,\lambda}}^2
+
\|v_{o,N}\|_{T_{N,\lambda}}^2
}.
\tag{7}
\]

At \(\lambda=0\), (7) is the finite-section diagnostic to compare with v13.792's \(\xi\)-target.

## 7. Conditioning guardrail [G]

The source-faithful project matrices already exhibit very small low modes in some large finite sections.

Therefore the unshifted solve
\[
A_Nc_N=f_N
\]
may be extremely ill-conditioned.

The near-extremal target Schur parameters
\[
|\kappa_{0,\infty}|\approx0.997,
\qquad
|\kappa_{1,\infty}|\approx0.995
\]
amplify this sensitivity further.

Any numerical experiment must therefore report at minimum:

- precision;
- cutoff/mode count;
- smallest eigenvalue of each parity block;
- condition number or inverse bound;
- residual of (5);
- \(\kappa_{0,N}\);
- \(\kappa_{1,N}\);
- stability under increasing cutoff and precision.

Binary64 agreement alone is not sufficient.

## 8. Correct next computational gate [C]

The safest next experiment is not a raw Fredholm solve.

At a value of \(a\) for which the direct source matrix is already well-audited, preferably \(a=1\):

1. assemble the source-faithful parity blocks of \(A_N\);
2. compute the exact/analytic source vectors for \(\cosh\) and \(\sinh\);
3. solve (6E)–(6O) at high precision;
4. compute
\[
\kappa_{0,N}^{(0)}
\]
and
\[
\kappa_{1,N}^{(0)}
\]
from the one-source moments;
5. study cutoff/precision stability;
6. treat the output as a finite-section diagnostic, not a positivity proof.

A separate shifted run with rigorously safe \(\lambda<\lambda_a\) can be used as an unconditional conditioning/control experiment, but its Schur parameters must not be compared directly with the \(\lambda=0\) \(\xi\)-targets.

## Result

The Lane-A Schur hierarchy now has a source-correct shift discipline:
\[
\boxed{
\text{finite }h_{a,\lambda}
\text{ exists for every }\lambda<\lambda_a,
}
\]
but
\[
\boxed{
h_\infty,\ \kappa_{n,\infty}
\text{ derived from Suzuki Section 7 are }\lambda=0\text{ targets}.
}
\]

The project already has the correct form-core matrices needed for a source-faithful Galerkin experiment. The next numerical gate is therefore feasible without resurrecting the invalid Fredholm endpoint closure.
