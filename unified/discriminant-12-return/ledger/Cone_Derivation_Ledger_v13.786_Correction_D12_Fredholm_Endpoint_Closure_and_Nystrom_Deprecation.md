# Cone Derivation Ledger v13.786 — Correction of the D12 Fredholm Endpoint Closure and Deprecation of the Existing Nyström Prototype

Date: 2026-09-25

Lane: A / D12 computational interface.

Status: [R] correction of v13.283 §8/§12; [G] computational deprecation notice for \`research-notes/suzuki_d12_fredholm_nystrom.py\`; [D] parity/reflection reduction retained; [C] corrected numerical routes identified.

Parents: v13.283, v13.782–785.

## 0. Synchronization

Immediately before this write the live ledger head is v13.785. No collision is present.

The source correction in v13.784 forces a dependency cleanup of the older D12 Fredholm numerical route.

## 1. The invalid step in v13.283 [R]

v13.283 §8 asserted that
\[
q_+=T_{K,a}^{-1}e^x
\]
lies in the operator domain of the Friedrichs realization and therefore in the form domain inherited from \(H_0^1(-a,a)\), concluding
\[
q_+(\pm a)=0.
\]

The implication
\[
\mathfrak D(A_a)\subset H_0^1(-a,a)
\]
is false.

Suzuki explicitly states that
\[
\mathfrak D(A_a)\supsetneq \mathfrak D(B_a)=H_0^1(-a,a)
\]
and that \(\mathfrak D(A_a)\) contains constants.

Moreover, Section 6.3 gives
\[
v_z=T_a^{-1}e_z\in\mathfrak D(T_a)=\mathfrak D(A_a),
\]
but does not place \(v_z\) in \(H_0^1(-a,a)\).

Therefore the endpoint conditions
\[
\boxed{
q_e(a)=0,\qquad q_o(a)=0
}
\]
used in v13.283 are not source-established for the actual deficiency vectors.

## 2. What survives from v13.283 [D]

The following are unaffected:

- \(T_{K,a}\) commutes with reflection;
- the canonical resolvent normalization
\[
q_+=T_{K,a}^{-1}e^x,\qquad q_-=Rq_+;
\]
- the phase-free real basis with \(C_+=C_-=1\);
- the parity decomposition
\[
q_+=q_e+q_o;
\]
- the raw first-kind parity equations
\[
-\mathcal K_a^{(+)}q_e=\cosh x+B_a,
\]
\[
-\mathcal K_a^{(-)}q_o=\sinh x+A_ax;
\]
- reflection laws
\[
A_-=-A_+,\qquad B_-=B_+;
\]
- normalized characteristic ratios eliminate the common deficiency scale.

Only the endpoint closure is retracted.

## 3. Consequence for the existing Nyström prototype [G]

The file
\[
\texttt{research-notes/suzuki\_d12\_fredholm\_nystrom.py}
\]
explicitly states and imposes
\[
q_e(a)=0,\qquad q_o(a)=0.
\]

Those constraints are used to make the augmented first-kind systems square.

Accordingly:
\[
\boxed{
\texttt{suzuki\_d12\_fredholm\_nystrom.py}
\text{ is not source-faithful for Suzuki's actual deficiency vectors.}
}
\]

Its current outputs must be treated as structural/toy Fredholm experiments only. They may not be used as evidence for:

- the actual finite deficiency vectors;
- \(A_a,B_a\);
- finite Suzuki characteristics;
- finite-to-infinite Weyl/HB limits.

No numerical result depending on those endpoint rows should be promoted.

## 4. Why the first-kind system becomes underdetermined without the false endpoints [D/N]

After parity reduction, the raw equation has one additional affine scalar in each channel:
\[
-\mathcal K_a^{(+)}q_e=\cosh+B_a,
\]
\[
-\mathcal K_a^{(-)}q_o=\sinh+A_ax.
\]

The local trace identities defining \(A_a,B_a\) are tautological when substituted back into the same first-kind equation, as established in v13.773/v13.781.

Therefore deleting the false endpoint condition does **not** reveal another simple algebraic row that makes the old Nyström system square.

This is exactly the primitive-affine nonclosure theorem in computational form.

## 5. Correct numerical routes [C]

There are now two source-faithful options.

### Route I — discretize the source-level operator
Compute
\[
q_e=(T_a^{(+)})^{-1}\cosh,
\qquad
q_o=(T_a^{(-)})^{-1}\sinh
\]
using a Galerkin/form discretization of
\[
T_a=A_a-\lambda I.
\]

Then evaluate the raw first-kind observables afterward:
\[
B_a=-1-r_{0,a},
\qquad
A_a=-1-r_{1,a},
\]
with
\[
r_{0,a}=\ell_{0,a}(q_e),
\qquad
r_{1,a}=\ell_{1,a}(q_o).
\]

This is the preferred route because uniqueness is inherited directly from \(T_a\)-invertibility.

### Route II — use the exact transported operator
Solve
\[
S_au_\pm=C_\pm\bar D e_{\pm i}
\]
in the projected energy-space realization and recover the finite Weyl data there.

This route is valid for spectral/Weyl quantities but does not by itself give the raw first-kind affine constants unless one subsequently reconstructs the Level-III primitive observables.

## 6. Correct role of the raw Fredholm equation [G]

Suzuki's equation (8.5) remains useful as:

- a continuous-kernel representation;
- a posteriori validation of a source-level solution;
- a way to evaluate the affine observables;
- a possible regularized numerical formulation if the missing domain realization is built explicitly.

It is **not** currently a closed standalone numerical system when the false endpoint conditions are removed.

Thus the correct computational hierarchy is
\[
\boxed{
T_a\text{ solve}
\;\longrightarrow\;
q_e,q_o
\;\longrightarrow\;
(A_a,B_a)
\;\longrightarrow\;
\text{raw Fredholm residual check}.
}
\]

## 7. Replacement of the v13.283 next target [R/C]

The old next target
\[
\text{Nyström solve of (8.5) + }q_e(a)=q_o(a)=0
\]
is retracted.

The replacement target is:

1. construct a parity-adapted Galerkin approximation of \(T_a\);
2. solve the two source equations
\[
T_a^{(+)}q_e=\cosh,\qquad T_a^{(-)}q_o=\sinh;
\]
3. evaluate
\[
r_{0,a},r_{1,a}
\]
and the dual edge-Laplace quantities from v13.785;
4. only then check (8.5) numerically without imposing artificial endpoint traces.

## Result

\[
\boxed{
q_e(a)=q_o(a)=0
\text{ is not a valid deficiency-vector boundary condition.}
}
\]

The D12 parity reduction survives, but the existing Fredholm Nyström prototype is computationally deprecated for the true Suzuki deficiency problem until its endpoint closure is replaced by a source-faithful \(T_a\) or energy-space realization.
