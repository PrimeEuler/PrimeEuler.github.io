# Cone Derivation Ledger v13.264 — Squared First-Order Operator and Rigged Resolvent Target

Date: 2026-09-05
Status: EXACT OPERATOR-THEORETIC REFINEMENT + NO-GO FOR ORDINARY VECTOR RESOLVENT — RH/GRH NOT PROVED

## 0. Synchronization and purpose

Immediately before this write, the authoritative project README, current `master` tip, and v13.263 were re-fetched. The tip remained

`4947aec0ec4100d50b8d9259202e0f87c201a4ed`,

with v13.263 the highest ledger checkpoint. No newer external-audit entry had landed at the synchronization point.

The purpose of this entry is to test the operator target proposed at the end of v13.263:

\[
\mathcal S_K(w)\stackrel{?}{=}\langle v,(A_K+w)^{-1}v\rangle,
\qquad A_K\ge0,
\]

and to compare it with Suzuki's 2026 first-order self-adjoint-extension framework.

The outcome is both positive and corrective:

1. the squared coordinate `w=z^2` is exactly what one expects from squaring a self-adjoint first-order spectral operator;
2. however, the exact D12 Stieltjes function cannot be an ordinary Hilbert-space vector resolvent because its spectral measure has infinite total mass;
3. the correct target is a **rigged-Hilbert-space / boundary-functional resolvent** for the square of a self-adjoint first-order operator.

This substantially sharpens the Hilbert–Pólya target.

## 1. Source-established Suzuki operator facts

Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), constructs for each finite interval `[-a,a]` a self-adjoint operator associated with the restricted Weil quadratic form. In the paper's notation:

- `B_a=D^*G_aD` is symmetric but not self-adjoint;
- the associated self-adjoint `A_a` is the Friedrichs extension of `B_a`;
- after shifting below the lower spectral bound, the form defines a Hilbert space `H(T_a)`;
- the minimal first-order operator
  \[
  \mathscr D_a=i\,d/dx
  \]
  on that Hilbert space has deficiency indices `(1,1)`;
- it therefore has a one-parameter family of self-adjoint extensions;
- the zeros of an associated entire boundary function `W(a,theta;z)` are precisely the eigenvalues of those self-adjoint extensions, hence are real;
- in the infinite-volume RH picture Suzuki identifies a self-adjoint extension whose spectrum is the set of zero ordinates and formulates approximation by the finite-interval extensions in strong resolvent sense.

Suzuki explicitly presents the limiting self-adjoint spectral operator as conjectural in the unconditional finite-to-infinite passage. The present ledger does not upgrade that conjecture to a theorem and does not claim Suzuki treats the D12 Dedekind field specifically.

The structural point relevant here is exact:

\[
\boxed{
\text{first-order self-adjoint spectral operator}
\quad\Longrightarrow\quad
\text{real spectral parameter }\gamma.
}
\]

The D12 squared coordinate from v13.263 is therefore naturally associated with the square of such an operator.

## 2. Squaring the first-order operator

Let `D` be any self-adjoint operator. Then

\[
\boxed{A:=D^2\ge0}
\]

is positive self-adjoint by the spectral theorem.

If

\[
D e_j=\gamma_j e_j,
\]

then

\[
\boxed{A e_j=\gamma_j^2 e_j.}
\]

Thus the transformation

\[
z\mapsto w=z^2
\]

that appeared arithmetically in v13.263 is exactly the spectral transformation

\[
\boxed{D\mapsto D^2.}
\]

This is not merely a visual analogy. It is the unique elementary functional-calculus operation that converts a real first-order spectrum `gamma_j` into the nonnegative support `gamma_j^2` of the Stieltjes measure.

Hence, if a D12 Hilbert–Pólya operator `D_K` exists with spectrum equal to the centered zero ordinates, the natural positive operator is

\[
\boxed{A_K=D_K^2.}
\]

Its resolvent has poles at

\[
w=-\gamma_j^2,
\]

exactly matching v13.263.

## 3. The naive ordinary-vector resolvent target

For a positive self-adjoint operator `A` and a Hilbert-space vector `v`, the scalar resolvent is

\[
R_v(w):=\langle v,(A+w)^{-1}v\rangle,
\qquad w>0.
\]

By the spectral theorem,

\[
\boxed{
R_v(w)=\int_{[0,\infty)}\frac{d\sigma_v(t)}{w+t},
}
\]

where

\[
\sigma_v(E)=\langle v,P_A(E)v\rangle
\]

is a finite positive measure with

\[
\boxed{\sigma_v([0,\infty))=\|v\|^2<\infty.}
\]

Consequently

\[
\boxed{
\lim_{w\to\infty}wR_v(w)=\|v\|^2.
}
\]

This follows from monotone/dominated convergence applied to

\[
\frac{w}{w+t}\uparrow1.
\]

Therefore every ordinary vector resolvent has finite total Stieltjes mass.

## 4. D12 spectral measure has infinite total mass

Under the v13.263 GRH/Stieltjes representation,

\[
\mathcal S_K(w)
=\sum_j\frac{2m_j}{w+\gamma_j^2}
=\int\frac{d\nu_K(t)}{w+t},
\]

with

\[
\boxed{
\nu_K=2\sum_jm_j\delta_{\gamma_j^2}.
}
\]

There are infinitely many nontrivial zeros of `zeta_K`, so

\[
\boxed{
\nu_K([0,\infty))=2\sum_jm_j=\infty.
}
\]

Moreover, for `w>0`,

\[
w\mathcal S_K(w)
=\sum_j2m_j\frac{w}{w+\gamma_j^2}.
\]

Each summand increases to `2m_j` as `w` tends to infinity. Hence monotone convergence gives

\[
\boxed{
\lim_{w\to\infty}w\mathcal S_K(w)=+\infty.
}
\]

Therefore:

\[
\boxed{
\mathcal S_K(w)
\neq
\langle v,(A+w)^{-1}v\rangle
}
\]

for every positive self-adjoint `A` and every genuine vector `v` in its Hilbert space.

This is an exact no-go theorem for the ordinary-vector ansatz proposed at the end of v13.263.

It does **not** obstruct a self-adjoint spectral realization. It tells us that the probing object cannot be a finite-norm vector.

## 5. Why the Stieltjes transform still converges

Infinite total mass is compatible with a Stieltjes transform provided the measure has the standard weighted integrability

\[
\int_{[0,\infty)}\frac{d\nu_K(t)}{1+t}<\infty.
\]

For the zero measure this becomes

\[
2\sum_j\frac{m_j}{1+\gamma_j^2}<\infty.
\]

This convergence follows from the standard zero-counting growth for completed degree-two Dedekind zeta functions; equivalently it is encoded in the convergence of the paired canonical product used in v13.263.

Thus

\[
\boxed{
\nu_K([0,\infty))=\infty,
\qquad
\int\frac{d\nu_K(t)}{1+t}<\infty.
}
\]

This is exactly the regime of an infinite-mass Stieltjes measure and points naturally to a boundary functional or negative Sobolev-scale vector.

## 6. Rigged Hilbert-space realization

Let `A>=0` be self-adjoint on a Hilbert space `H`. Introduce the scale

\[
H_{+1}=\mathfrak D((I+A)^{1/2}),
\qquad
H\subset H_{-1}=H_{+1}^*.
\]

A generalized vector `phi` may lie in `H_{-1}` without lying in `H`.

In a pure-point model with orthonormal eigenbasis `e_j`, suppose

\[
A e_j=\gamma_j^2e_j.
\]

Formally define

\[
\boxed{
\phi=\sum_j\sqrt{2m_j}\,e_j.
}
\]

Then

\[
\|\phi\|_H^2=2\sum_jm_j=\infty,
\]

so `phi` is not a Hilbert vector. But

\[
\boxed{
\|\phi\|_{H_{-1}}^2
=2\sum_j\frac{m_j}{1+\gamma_j^2}<\infty.
}
\]

Hence `phi` is a legitimate generalized vector in the negative scale.

The dual resolvent pairing is then

\[
\boxed{
\langle\phi,(A+w)^{-1}\phi\rangle_{-1,+1}
=\sum_j\frac{2m_j}{w+\gamma_j^2}
=\mathcal S_K(w).
}
\]

Thus the exact operator target is not

\[
\langle v,(A+w)^{-1}v\rangle,
\quad v\in H,
\]

but rather

\[
\boxed{
\mathcal S_K(w)
=\langle\phi,(A_K+w)^{-1}\phi\rangle_{-1,+1},
\qquad
A_K=D_K^2\ge0,
\quad
\phi\in H_{-1}\setminus H.
}
\]

This is the correct mass class.

## 7. Boundary-functional interpretation

The previous generalized vector should be interpreted as a boundary probe rather than a normalizable state.

This aligns structurally with Suzuki's finite-interval theory:

- the first-order minimal operator has deficiency indices `(1,1)`;
- its self-adjoint extensions are selected by one boundary parameter;
- an entire function built from deficiency vectors/boundary data has zeros exactly at the extension eigenvalues.

Therefore the D12 Stieltjes function is more naturally sought as a **Weyl/Titchmarsh-type boundary resolvent function** for a self-adjoint extension than as an ordinary state expectation of a resolvent.

This distinction is load-bearing.

A Weyl function can encode an infinite spectral measure because the boundary functional need not be represented by a vector of finite Hilbert norm.

The operator program should therefore be reformulated as

\[
\boxed{
\text{construct a D12 symmetric first-order operator with deficiency }(1,1),
}
\]

identify its canonical boundary functional `phi`, and prove that the associated squared-operator Weyl function is

\[
\boxed{
\mathcal S_K(w).
}
\]

If this can be done unconditionally with a self-adjoint extension, the support of its squared spectral measure is automatically nonnegative.

## 8. Conditional exact model under GRH

Under GRH, the abstract model is immediate.

Take

\[
H_K^{\rm spec}=\ell^2(\{(j,r):1\le r\le m_j\}),
\]

and define the self-adjoint diagonal operator

\[
D_K e_{j,r}=\gamma_j e_{j,r}.
\]

Then

\[
A_K=D_K^2,
\qquad
A_Ke_{j,r}=\gamma_j^2e_{j,r}.
\]

Define the generalized boundary vector

\[
\phi_K
=\sqrt2\sum_{j,r}e_{j,r}.
\]

It is not in `H_K^spec`, but belongs to the corresponding `H_{-1}` scale. Then

\[
\boxed{
\mathcal S_K(w)
=\langle\phi_K,(A_K+w)^{-1}\phi_K\rangle_{-1,+1}.
}
\]

This model is tautological and therefore is **not** a proof of GRH. Its value is diagnostic: it identifies exactly the operator class and boundary mass normalization an unconditional construction must reproduce.

## 9. Multiplicity normalization is fixed

The residue of `mathcal S_K` at `w=-gamma_j^2` is

\[
2m_j.
\]

Therefore any boundary spectral realization must satisfy

\[
\boxed{
\|P_{\gamma_j^2}\phi_K\|_{\rm generalized}^2=2m_j.
}
\]

The factor `2` is not arbitrary. It comes from folding the centered pair

\[
+i\gamma_j,
\qquad
-i\gamma_j
\]

through the square map.

Thus the squared operator naturally forgets the sign of the first-order eigenvalue while doubling the spectral mass of each positive squared height.

This gives a precise bridge between the even functional equation and the operator square.

## 10. D12 factorization and direct-sum operator target

The completed Dedekind function factors into the Riemann and quadratic channels:

\[
\xi_K=C\,\xi_0\xi_{12}.
\]

Hence

\[
\mathcal S_K=\mathcal S_0+\mathcal S_{12}.
\]

Under the critical-line spectral picture, this suggests the direct sum

\[
\boxed{
D_K=D_0\oplus D_{12},
}
\]

and therefore

\[
\boxed{
A_K=D_K^2=D_0^2\oplus D_{12}^2.
}
\]

The generalized boundary functional decomposes accordingly:

\[
\phi_K=\phi_0\oplus\phi_{12},
\]

so that

\[
\boxed{
\mathcal S_K(w)
=
\langle\phi_0,(D_0^2+w)^{-1}\phi_0\rangle
+
\langle\phi_{12},(D_{12}^2+w)^{-1}\phi_{12}\rangle.
}
\]

This is the operator counterpart of the audited H4/D12 block decomposition.

Guardrail: no unconditional construction of `D_12` with the required spectrum is claimed here.

## 11. Relation to the split/inert self-sector

From v13.262,

\[
Q_K=2Q_{SS}=2Q_{II}.
\]

Therefore the same first-order/squared-operator target belongs to either D12 diagonal self-sector.

The chain is now

\[
\boxed{
Q_{SS}
\longrightarrow
Q_K
\longrightarrow
\mathscr D_K
\longrightarrow
D_K\text{ self-adjoint extension}
\longrightarrow
A_K=D_K^2
\longrightarrow
\mathcal S_K(w)\text{ as boundary resolvent}.
}
\]

The unresolved step is the unconditional construction/identification of the middle operator from the D12 screw kernel.

## 12. Finite-interval approximation target

Suzuki's 2026 framework suggests a concrete finite-interval route.

For each `a>0`, the restricted Weil form gives a Hilbert space and a minimal first-order operator with deficiency `(1,1)`. Let

\[
D_{K,a,\theta}
\]

denote the D12/Dedekind analogue, if constructed, of the relevant self-adjoint extension, and define

\[
A_{K,a,\theta}=D_{K,a,\theta}^2\ge0.
\]

The correct approximation problem is then not merely eigenvalue convergence. It is simultaneous convergence of the **boundary Weyl functions**:

\[
\boxed{
m_{K,a}(w)\longrightarrow\mathcal S_K(w)}
\]

locally uniformly on the Stieltjes domain, or in an equivalent resolvent sense compatible with the generalized boundary vectors.

If each finite `m_{K,a}` is a Stieltjes function because `A_{K,a,theta}>=0`, and if the convergence is strong enough to preserve the Stieltjes class and identify the limit with the arithmetic `mathcal S_K`, then the limit would inherit nonpositive-real pole support.

That is the precise place where a GRH proof would have to enter.

The hard part is therefore no longer vague “operator positivity.” It is:

\[
\boxed{
\text{unconditional identification of the arithmetic }\mathcal S_K
\text{ with the limit of positive squared boundary resolvents.}
}
\]

## 13. Why squaring is especially natural here

Three independent structures now select the same square:

1. **Functional equation:** `Xi_K(z)` is even, so its logarithmic derivative divided by `z` is a function of `z^2`.
2. **Critical line:** centered critical zeros are `z=i gamma`; squaring sends them to `-gamma^2`.
3. **Operator theory:** a self-adjoint first-order operator has real spectrum `gamma`; its square is positive with spectrum `gamma^2`.

Thus

\[
\boxed{
\text{evenness}
\leftrightarrow
z^2
\leftrightarrow
D^2
\leftrightarrow
\text{positive Stieltjes support}.
}
\]

This four-way match is exact at the level of spectral geometry.

## 14. New no-go and corrected target

The main theorem of this entry can be summarized as follows.

### Theorem — mass obstruction to an ordinary vector resolvent

Let `mathcal S_K` be the D12 squared critical logarithmic derivative of v13.263. Under its GRH Stieltjes representation,

\[
\nu_K=2\sum_jm_j\delta_{\gamma_j^2}
\]

has infinite total mass. Therefore there is no Hilbert-space vector `v` and positive self-adjoint operator `A` such that

\[
\mathcal S_K(w)=\langle v,(A+w)^{-1}v\rangle
\]

for all `w>0`.

### Corrected target

The exact spectral class is instead

\[
\boxed{
\mathcal S_K(w)
=\langle\phi,(D_K^2+w)^{-1}\phi\rangle_{-1,+1},
}
\]

where `D_K` is self-adjoint and `phi` is a generalized boundary vector with

\[
\phi\in H_{-1}\setminus H.
\]

This target has exactly the required infinite spectral mass and finite Stieltjes weighted mass.

## 15. What is exact, conditional, and open

### Exact/unconditional operator facts

- If `D` is self-adjoint, `D^2>=0`.
- Ordinary vector resolvents have finite total spectral mass.
- The D12 zero-counting Stieltjes measure has infinite total mass but finite `(1+t)^{-1}` weighted mass under the critical-line representation.
- Therefore the ordinary-vector resolvent ansatz is too small.
- A generalized `H_{-1}` boundary vector is the correct abstract mass class.
- Suzuki's finite-interval first-order operators have deficiency indices `(1,1)` and self-adjoint extensions with real spectra; this is source-established for his Riemann-zeta framework.

### Conditional on GRH / spectral input

- The diagonal model with eigenvalues `gamma_j`.
- The positive measure `nu_K` supported on squared zero heights.
- The explicit rigged resolvent realization using those ordinates.

### Open

- Constructing the D12/Dedekind first-order operator directly from the audited D12 screw/Weil self-sector without assuming GRH.
- Identifying its canonical boundary functional.
- Proving its squared Weyl function equals the arithmetic `mathcal S_K`.
- Establishing the finite-interval to infinite-volume convergence needed to transfer positivity and pole support.

No RH or GRH statement is proved in this entry.

## 16. Strategic consequence

The previous target

\[
\mathcal S_K(w)=\langle v,(A_K+w)^{-1}v\rangle
\]

was close but technically impossible because `v` would need infinite norm.

The corrected frontier is sharper:

\[
\boxed{
\text{D12 screw self-sector}
\to
\text{deficiency-(1,1) first-order operator}
\to
\text{self-adjoint }D_K
\to
D_K^2\ge0
\to
\text{boundary Weyl/Stieltjes function}
\stackrel{?}{=}
\mathcal S_K.
}
\]

The most valuable next derivation is therefore to write the D12 restricted screw kernel in the same finite-interval operator language used by Suzuki, identify the analogue of the form operator `G_a`, and determine whether the D12 two-sector compression commutes with the derivative/Friedrichs-extension construction.

If it does, the H4/D12 decomposition may descend all the way to the finite-interval deficiency spaces and boundary Weyl functions. That would turn the existing character/residue transform into an operator-level decomposition of the exact objects whose limits are conjectured to encode zero ordinates.