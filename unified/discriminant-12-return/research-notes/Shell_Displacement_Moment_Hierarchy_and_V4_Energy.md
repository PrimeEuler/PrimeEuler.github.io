# Shell-Displacement Moment Hierarchy and V4 Energy

Date: 2026-09-13

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 1. Exact shell-to-skeleton displacement

Fix an integer `n>=1`. For each `1<=k<=n`, define

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
r_k=n-kq_k,
\qquad
\delta_k(n)=\left\{\frac nk\right\}=\frac{r_k}{k}.
\]

On the Paper-A shell `Y=sqrt(n)`, with

\[
u=k,\qquad v=\frac nk,
\]

the exact shell coordinate is

\[
X_k=\frac12\left(k-\frac nk\right).
\]

Define the quotient-skeleton coordinate by replacing `n/k` with its integer quotient:

\[
X_k^{(0)}=\frac{k-q_k}{2}.
\]

Then

\[
\boxed{
\Delta X_k:=X_k-X_k^{(0)}
=-\frac12\delta_k(n)
=-\frac{r_k}{2k}.
}
\]

Hence

\[
\boxed{
\delta_k(n)=-2\Delta X_k,
\qquad
r_k=-2k\Delta X_k.
}
\]

Because `0<=delta_k<1`,

\[
-\frac12<\Delta X_k\le0.
\]

And the divisor/contact criterion becomes

\[
\boxed{
\Delta X_k=0
\iff
\delta_k(n)=0
\iff
r_k=0
\iff
k\mid n.
}
\]

This is an exact geometric realization of the fractional divisor defect as horizontal displacement of the real shell sample from the quotient half-lattice skeleton.

## 2. Full displacement moment hierarchy

For `alpha>0`, define the untwisted defect moment

\[
\mathcal S_\alpha(n)
=
\sum_{k\nmid n}\delta_k(n)^\alpha.
\]

Using `delta_k=-2 Delta X_k`,

\[
\boxed{
\mathcal S_\alpha(n)
=
2^\alpha\sum_{k\nmid n}(-\Delta X_k)^\alpha.
}
\]

Thus the existing defect-moment family is exactly the positive moment hierarchy of shell-to-skeleton displacement magnitudes.

In particular,

\[
\boxed{
\mathcal S_1(n)=nH_n-D(n)
=-2\sum_{k=1}^n\Delta X_k.
}
\]

The quadratic moment is

\[
\boxed{
\mathcal S_2(n)
=4\sum_{k=1}^n(\Delta X_k)^2.
}
\]

Define the shell-displacement energy

\[
\boxed{
\mathcal E_X(n)
:=\sum_{k=1}^n(\Delta X_k)^2
=\frac14\mathcal S_2(n).
}
\]

This is sign-free: it measures geometric spread from the quotient skeleton, whereas `S_1` measures total one-sided displacement.

Since `0<=delta_k<1`, for `alpha>beta>=0`,

\[
\mathcal S_\alpha(n)\le \mathcal S_\beta(n),
\]

with the `alpha->0+` endpoint

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_\alpha(n)=n-\tau(n).
}
\]

Therefore

\[
\boxed{
4\mathcal E_X(n)=\mathcal S_2(n)
\le \mathcal S_1(n)
\le n-\tau(n).
}
\]

Equivalently,

\[
\boxed{
\mathcal E_X(n)
\le \frac14\bigl(nH_n-D(n)\bigr)
\le \frac14\bigl(n-\tau(n)\bigr).
}
\]

## 3. Character-weighted shell displacement moments

For an arithmetic character/weight `chi`, define

\[
\mathcal S_{\alpha,\chi}(n)
=
\sum_{k\nmid n}\chi(k)\delta_k(n)^\alpha.
\]

Then

\[
\boxed{
\mathcal S_{\alpha,\chi}(n)
=
2^\alpha\sum_{k\nmid n}\chi(k)(-\Delta X_k)^\alpha.
}
\]

At first order,

\[
\boxed{
E_\chi(n):=\mathcal S_{1,\chi}(n)
=-2\sum_{k=1}^n\chi(k)\Delta X_k.
}
\]

At second order define

\[
\boxed{
Q_\chi(n):=\mathcal S_{2,\chi}(n)
=4\sum_{k=1}^n\chi(k)(\Delta X_k)^2.
}
\]

The untwisted quadratic channel is positive:

\[
Q_1(n)=4\mathcal E_X(n)\ge0.
\]

For nonprincipal real characters, `Q_chi` is a signed residue-sector imbalance of quadratic displacement energy; it need not be nonnegative.

## 4. V4 residue-energy decomposition

Assume the mod-12 unit-sector characters

\[
1,\chi_{-4},\chi_{-3},\chi_{12}
\]

and residue classes `r in {1,5,7,11}`. Define residue quadratic energies

\[
\mathcal E_r(n)
:=
\sum_{\substack{k\le n\\k\equiv r\ (12)}}(\Delta X_k)^2.
\]

Then the character quadratic channels satisfy the exact Hadamard transform

\[
\boxed{
\frac14
\begin{pmatrix}
Q_1^\times\\Q_{-4}\\Q_{-3}\\Q_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
\mathcal E_1\\\mathcal E_5\\\mathcal E_7\\\mathcal E_{11}
\end{pmatrix},
}
\]

where `Q_1^times` denotes the principal mod-12 channel, i.e. the quadratic energy restricted to unit residue columns. Equivalently,

\[
\boxed{
\begin{pmatrix}
\mathcal E_1\\\mathcal E_5\\\mathcal E_7\\\mathcal E_{11}
\end{pmatrix}
=
\frac1{16}H_4
\begin{pmatrix}
Q_1^\times\\Q_{-4}\\Q_{-3}\\Q_{12}
\end{pmatrix}.
}
\]

The factor `1/16` here is simply the combination of (i) `Q_chi=4` times the displacement-square transform and (ii) the inverse Hadamard factor `1/4`.

**[Audit]** It has no Casimir/null-diamond interpretation.

A cleaner convention is to define the normalized quadratic character energy directly as

\[
\widetilde Q_\chi(n)
:=\sum_k\chi(k)(\Delta X_k)^2
=\frac14Q_\chi(n).
\]

Then

\[
\boxed{
\begin{pmatrix}
\widetilde Q_1^\times\\\widetilde Q_{-4}\\\widetilde Q_{-3}\\\widetilde Q_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
\mathcal E_1\\\mathcal E_5\\\mathcal E_7\\\mathcal E_{11}
\end{pmatrix},
}
\]

and inversion is the ordinary

\[
\boxed{
\mathbf E_r=\frac14H_4\widetilde{\mathbf Q}_\chi.
}
\]

## 5. Contact spectrum versus displacement-amplitude spectrum

The prime factorization

\[
n=\prod_p p^{e_p}
\]

determines the zero-displacement set exactly:

\[
\Delta X_k=0
\iff
k\mid n.
\]

For `gcd(n,6)=1`, the zero-set/contact character spectrum is

\[
D_\chi(n)=\sum_{d\mid n}\chi(d)
=\prod_{p^{e_p}\parallel n}\bigl(1+\chi(p)+\cdots+\chi(p)^{e_p}\bigr).
\]

Thus

\[
D_\chi(n)=0
\iff
\exists p^{e_p}\parallel n:\ \chi(p)=-1,\ e_p\text{ odd}.
\]

By contrast, `E_chi` and `Q_chi` depend on the nonzero amplitudes

\[
\Delta X_k=-\frac{n\bmod k}{2k},
\]

so they do not in general admit an Euler product in the prime exponents of `n`.

This yields a three-layer hierarchy:

1. **support/contact (`alpha=0+`)**: prime exponents determine exactly which shell samples have zero displacement;
2. **first displacement (`alpha=1`)**: Euclidean remainder amplitudes produce signed/weighted shell displacement;
3. **quadratic energy (`alpha=2`)**: Euclidean remainder amplitudes produce sign-free geometric spread, with V4 characters resolving residue-sector energy imbalance.

## 6. Exact support limit and complement

For each character,

\[
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=
\sum_{k\nmid n}\chi(k).
\]

Writing

\[
P_\chi(n)=\sum_{k=1}^n\chi(k),
\qquad
D_\chi(n)=\sum_{d\mid n}\chi(d),
\]

gives

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=P_\chi(n)-D_\chi(n).
}
\]

So the complete shell-displacement moment family connects continuously (in the `alpha->0+` support sense) to the prime-exponent-controlled contact spectrum, while positive moments retain genuinely Euclidean remainder information.

## 7. Guardrails

- `X_k` is on the exact continuous shell; `X_k^(0)` is the quotient skeleton. Calling `Delta X_k` an off-shell displacement would be misleading: it is an off-skeleton displacement within the shell coordinate comparison.
- `D_chi=0` does not imply `E_chi=0` or `Q_chi=0`.
- Prime exponents control the zero set multiplicatively, not the nonzero displacement amplitudes.
- Hadamard normalization factors are group-Fourier normalization only and are not identified with Casimir or null-diamond quarters.
