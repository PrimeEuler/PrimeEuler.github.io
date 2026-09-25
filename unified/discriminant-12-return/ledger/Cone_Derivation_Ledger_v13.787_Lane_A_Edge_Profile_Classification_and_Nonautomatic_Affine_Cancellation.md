# Cone Derivation Ledger v13.787 — Lane A Edge-Profile Classification and Nonautomatic Affine Cancellation

Date: 2026-09-25

Lane: A.

Status: [D] exact edge-profile classification from v13.785; [N] parity alone does not force affine contamination to vanish; [C] isolates the precise weighted edge moments and rates required for the pure compensated limit.

Parents: v13.743, v13.782, v13.785–786.

## 0. Synchronization

Immediately before this write the live ledger head is v13.786. No collision is present.

## 1. Imported exact quantities

From v13.785 define the dual responses
\[
\psi_{0,a}:=(T_a^{(+)})^{-1}q_{0,a},
\qquad
\psi_{1,a}:=(T_a^{(-)})^{-1}q_{1,a},
\]
and the right-edge Laplace moments
\[
\boxed{
L_{j,a}
:=
\int_0^{2a}e^{-\xi}\psi_{j,a}(a-\xi)\,d\xi
=
e^{-a}r_{j,a},
\qquad j=0,1.
}
\tag{1}
\]

The primitive affine contamination is exactly
\[
\boxed{
\alpha_a=-e^{-a}-L_{1,a},
}
\tag{2}
\]
\[
\boxed{
\beta_a=-(a+1)e^{-a}-aL_{1,a}-L_{0,a}.
}
\tag{3}
\]

No endpoint assumptions on the deficiency vectors enter.

## 2. Complete asymptotic classification [D]

### Case A: \(L_{1,a}\to \ell_1\neq0\)

Then
\[
\alpha_a\to-\ell_1,
\]
while
\[
\beta_a=-a\ell_1+o(a)
\]
and therefore the primitive constant contamination grows linearly.

Thus a nonzero limiting odd edge-Laplace moment is incompatible with the pure compensated edge model.

### Case B: \(L_{1,a}\to0\) but \(aL_{1,a}\to c_1\)

If also
\[
L_{0,a}\to \ell_0,
\]
then
\[
\boxed{
\alpha_a\to0,
\qquad
\beta_a\to-(c_1+\ell_0).
}
\tag{4}
\]

So the slope contamination disappears, but a finite constant edge remnant survives.

### Case C: \(aL_{1,a}\to0\), \(L_{0,a}\to\ell_0\)

Then
\[
\boxed{
\alpha_a\to0,
\qquad
\beta_a\to-\ell_0.
}
\tag{5}
\]

Only the even dual edge moment survives.

### Case D: pure compensated edge limit

The pure limit
\[
\alpha_a\to0,\qquad \beta_a\to0
\]
holds iff
\[
\boxed{
L_{0,a}\to0,
\qquad
aL_{1,a}\to0.
}
\tag{6}
\]

This is the sharp scalar criterion in the dual edge variables.

## 3. Weighted edge-profile convergence theorem [D]

Define shifted edge profiles
\[
\Psi_{j,a}(\xi)
:=
\psi_{j,a}(a-\xi),
\qquad
0\le\xi\le2a.
\]

Suppose, after extension by zero for \(\xi>2a\),
\[
\Psi_{j,a}\to\Psi_j^{\rm edge}
\]
in
\[
L^1((0,\infty),e^{-\xi}d\xi).
\]

Then
\[
\boxed{
L_{j,a}
\to
\mathcal L_j^{\rm edge}
:=
\int_0^\infty e^{-\xi}\Psi_j^{\rm edge}(\xi)\,d\xi.
}
\tag{7}
\]

Therefore:

- if
\[
\mathcal L_1^{\rm edge}\neq0,
\]
the constant contamination \(\beta_a\) diverges linearly;
- finite weighted edge-profile convergence by itself is **not enough** to obtain a finite primitive edge limit;
- the odd channel additionally requires cancellation of the limiting Laplace moment and a quantitative \(1/a\)-scale rate.

## 4. Parity does not force the edge moments to vanish [N]

Globally,
\[
\psi_{0,a}\text{ is even},
\qquad
\psi_{1,a}\text{ is odd}.
\]

But \(L_{j,a}\) is a **one-sided right-edge** functional:
\[
L_{j,a}
=
\int_0^{2a}e^{-\xi}\psi_{j,a}(a-\xi)\,d\xi.
\]

Evenness of \(\psi_{0,a}\) does not imply \(L_{0,a}=0\).

Oddness of \(\psi_{1,a}\) only relates the right and left edge profiles by sign; it does not force the right-edge Laplace moment to vanish.

Hence
\[
\boxed{
\text{reflection/parity symmetry does not automatically remove }
\alpha_a,\beta_a.
}
\tag{8}
\]

This closes another possible shortcut.

## 5. Minimal analytic targets [C]

The primitive-edge lane now requires exactly two estimates:
\[
\boxed{
\int_0^{2a}e^{-\xi}\psi_{0,a}(a-\xi)\,d\xi=o(1),
}
\tag{9}
\]
\[
\boxed{
\int_0^{2a}e^{-\xi}\psi_{1,a}(a-\xi)\,d\xi=o(a^{-1}).
}
\tag{10}
\]

These are strictly local-to-the-edge weighted estimates. No global \(L^2\) convergence of the whole deficiency vector is necessary.

## 6. Consequence for any future edge-limit theorem [G]

Any claimed limiting edge equation of the form
\[
S_{\rm edge}q
=
\text{pure compensated source}
\]
must establish (9)–(10), or an equivalent statement.

If instead only weighted profile convergence is available, the correct general limiting source must retain the residual constants determined by
\[
\mathcal L_0^{\rm edge}
\]
and the first nonzero asymptotic coefficient of
\[
L_{1,a}.
\]

Thus the edge correction is not an optional bookkeeping term; it is the exact output of the dual resolvent edge moments.

## Result

\[
\boxed{
\alpha_a=-e^{-a}-L_{1,a},
\qquad
\beta_a=-(a+1)e^{-a}-aL_{1,a}-L_{0,a}.
}
\]

The pure compensated edge limit is equivalent to
\[
\boxed{
L_{0,a}=o(1),
\qquad
L_{1,a}=o(a^{-1}).
}
\]

Parity alone does not imply either estimate.
