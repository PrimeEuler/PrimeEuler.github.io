# Cone Derivation Ledger v13.770 — Lane A Divisor-Shell Rapidity Sampling Test and Arithmetic-Carrier Obstruction

Date: 2026-09-24

Lane: A — exploratory cross-check against the established divisor-shell cone geometry.

Status: [D] exact rapidity sampling measure and parity decomposition; [D] exact boundary-scale identification \(n=e^{2A}\), \(\sqrt n=e^A\); [N] direct identification with the Lane-A trace functionals fails; [I] divisor geometry remains a useful renormalization/asymptotic template.

Parents: v13.315, v13.409, v13.691, v13.744–746, v13.761, v13.766, v13.768–769.

## 0. Synchronization

The controlling checkpoint v13.769 and External Audit Round 95 v13.768 were read before starting. Live ledger checked immediately before write: v13.769 remains head; no numbering collision.

## 1. Exact shell matching [D]

Take an integer shell
\[
n=e^{2A},
\qquad
A=\frac12\log n.
\]
For \(k=1,\dots,n\), the divisor-shell sampling point is
\[
(x_k,y_k)=\left(k,\frac nk\right).
\]
Its rapidity is
\[
\boxed{s_k=\log k-A,}
\]
because
\[
k=e^{A+s_k},
\qquad
\frac nk=e^{A-s_k}.
\]
As \(k\) ranges from \(1\) to \(n\),
\[
s_k\in[-A,A].
\]

Thus the divisor shell and Suzuki's finite interval have exactly the same rapidity window after \(n=e^{2A}\).

## 2. Exact weighted sampling measure [D]

Since
\[
y_k=\frac nk=e^{A-s_k},
\]
define the atomic measure
\[
\boxed{
\mu_A^{\rm div}
:=
\sum_{k=1}^{n}
\frac nk\,\delta_{s_k}.
}
\]

Then for any test function \(\phi\),
\[
\boxed{
\langle\mu_A^{\rm div},\phi\rangle
=
\sum_{k=1}^{n}\frac nk\,
\phi(\log k-A).
}
\]

The continuous shell relation is
\[
x=e^{A+s},\qquad dx=e^{A+s}ds,
\]
and
\[
y=e^{A-s}.
\]
Hence
\[
\boxed{y\,dx=e^{2A}ds=n\,ds.}
\]

Therefore the exact continuous carrier corresponding to the weighted divisor sampling is
\[
\boxed{
\mu_A^{\rm bulk}=n\,1_{[-A,A]}(s)\,ds.
}
\]

Define the rapidity sampling discrepancy
\[
\boxed{
\nu_A^{\rm div}
=
\mu_A^{\rm div}
-
n\,1_{[-A,A]}ds.
}
\]

For \(\phi\equiv1\),
\[
\boxed{
\langle\nu_A^{\rm div},1\rangle
=
nH_n-n\log n.
}
\]

This is the exact linear sampling-minus-integral discrepancy on the shell.

## 3. Parity decomposition [D]

Let reflection act by
\[
(R\phi)(s)=\phi(-s).
\]
For any distribution \(\nu\), define
\[
\nu^{(+)}=\frac12(\nu+R_*\nu),
\qquad
\nu^{(-)}=\frac12(\nu-R_*\nu).
\]

Since the bulk measure \(n\,ds\) is even,
\[
\boxed{
(\nu_A^{\rm div})^{(+)}
=
\frac12(\mu_A^{\rm div}+R_*\mu_A^{\rm div})
-
n\,ds,
}
\]
\[
\boxed{
(\nu_A^{\rm div})^{(-)}
=
\frac12(\mu_A^{\rm div}-R_*\mu_A^{\rm div}).
}
\]

For even \(\phi_+\),
\[
\langle\nu_A^{\rm div},\phi_+\rangle
=
\langle(\nu_A^{\rm div})^{(+)},\phi_+\rangle,
\]
and for odd \(\phi_-\),
\[
\langle\nu_A^{\rm div},\phi_-\rangle
=
\langle(\nu_A^{\rm div})^{(-)},\phi_-\rangle.
\]

This is an exact even/odd shell-discrepancy decomposition on the same interval \([-A,A]\) used by Lane A.

## 4. The \(e^A\) boundary scale is exact [D]

v13.315 establishes that the divisor staircase's terminal hyperbola boundary has
\[
Q_n=O(\sqrt n).
\]
Under \(n=e^{2A}\),
\[
\boxed{
Q_{e^{2A}}=O(e^A).
}
\]

Thus Lane A's edge normalization \(e^A\) is exactly the square-root hyperbola boundary scale after the shell/rapidity identification. This is a genuine geometric scale match, not a heuristic exponent substitution.

## 5. First obstruction: the raw linear discrepancy is too large [N]

Using
\[
H_n=\log n+\gamma+\frac1{2n}+O(n^{-2}),
\]
the constant-test discrepancy is
\[
nH_n-n\log n
=
\gamma n+\frac12+O(n^{-1}).
\]
With \(n=e^{2A}\),
\[
\boxed{
\langle\nu_A^{\rm div},1\rangle
=
\gamma e^{2A}+\frac12+O(e^{-2A}).
}
\]

Therefore the raw sampling-minus-integral measure is not an \(O(e^A)\) boundary remainder. It contains an \(O(e^{2A})\) smooth/contact contribution that must be subtracted first.

This mirrors the classical need to remove the full smooth main term
\[
n\log n+(2\gamma-1)n
\]
before the divisor error \(\Delta(n)\) appears.

## 6. Second obstruction: flooring is nonlinear [N]

The divisor summatory function is
\[
D(n)=\sum_{k\le n}\left\lfloor\frac nk\right\rfloor.
\]
Its staircase correction is
\[
nH_n-D(n)
=
\sum_{k\le n}\left\{\frac nk\right\}.
\]

The floor/fractional-part operation is nonlinear in the shell height. Consequently \(D(n)\) and its remainder are not obtained simply by pairing the linear distribution \(\nu_A^{\rm div}\) against a fixed test function.

Thus the exact divisor error cannot be identified with either Lane-A linear trace functional merely from the common rapidity carrier.

## 7. Third obstruction: arithmetic carrier mismatch [N]

Lane A's common Suzuki-Weil current has finite-place arithmetic carrier
\[
\mu_{\rm Weil}^{\rm fin}
=
\sum_{p,m\ge1}(\log p)p^{-m/2}
(\delta_{m\log p}+\delta_{-m\log p}),
\]
equivalently the logarithmic-derivative/von-Mangoldt carrier associated with \(-\zeta'/\zeta\).

By contrast, the divisor summatory function has Dirichlet series
\[
\sum_{n\ge1}\frac{d(n)}{n^s}=\zeta(s)^2.
\]

Therefore the two arithmetic objects are categorically different:
\[
\boxed{
\text{Lane A: logarithmic derivative / prime-power current}
}
\]
versus
\[
\boxed{
\text{divisor summatory: multiplicative convolution }1*1.
}
\]

No exact identity
\[
\ell_{0,A}\ \text{or}\ \ell_{1,A}
=
\text{divisor-discrepancy functional}
\]
follows from the cone geometry, and none is claimed.

## 8. Comparison with Lane-A trace functionals [D/N]

Lane A has
\[
\ell_{0,A}(v)
=
\int_{-A}^{A}k(0,s)v(s)\,ds,
\]
\[
\ell_{1,A}(v)
=
\int_{-A}^{A}k_x(0,s)v(s)\,ds.
\]

These are absolutely continuous kernel functionals on the finite interval.

The divisor shell discrepancy is instead an atomic-minus-continuous distribution:
\[
\nu_A^{\rm div}
=
\sum_{k\le n}\frac nk\delta_{\log k-A}
-
n\,ds.
\]

Hence the proposed direct identification fails already at the measure class:
\[
\boxed{
\nu_A^{\rm div}\ne
k(0,s)\,ds,
\qquad
\nu_A^{\rm div}\ne
k_x(0,s)\,ds.
}
\]

The parity match is exact, but it does not remove this carrier mismatch.

## 9. What survives and is useful [I]

Three pieces survive the test exactly:

1. **Same finite rapidity window**
\[
\boxed{[-A,A]\leftrightarrow n=e^{2A}.}
\]

2. **Same mirror/parity structure**
\[
s\mapsto-s
\]
gives exact even/odd discrepancy channels, matching Lane A's parity split structurally.

3. **Same natural boundary scale**
\[
\boxed{\sqrt n=e^A.}
\]

Therefore divisor-shell asymptotics remain a useful model for how a large smooth \(e^{2A}\)-scale bulk can be renormalized before an \(e^A\)-scale hyperbola boundary becomes visible.

The correct lesson is not that the divisor error equals the Suzuki feedback moment. It is:
\[
\boxed{
\text{extract the full smooth/contact bulk before estimating the finite-}A\text{ feedback remainder.}
}
\]

This suggests that crude separate norm bounds on \(k\) and \(R_Af\) may miss cancellation in exactly the same way that bounding \(nH_n\) directly misses the divisor-error scale.

## 10. New quantitative target [I/C]

Instead of immediately estimating
\[
M_{00}=\ell_{0,A}(R_A^{(+)}1),
\qquad
M_{1x}=\ell_{1,A}(R_A^{(-)}x)
\]
as undifferentiated products of norms, first seek decompositions
\[
M_{00}=M_{00}^{\rm bulk}+M_{00}^{\rm bdry},
\]
\[
M_{1x}=M_{1x}^{\rm bulk}+M_{1x}^{\rm bdry},
\]
where the bulk pieces are explicitly computable from the full-line/translation-invariant response and the residual pieces are supported or concentrated at the finite endpoints/basepoint correction.

The divisor-shell test predicts the scale hierarchy
\[
\text{bulk}\sim e^{2A},
\qquad
\text{geometric boundary}\sim e^A,
\]
but this hierarchy is only a guide until derived for the Suzuki moments themselves.

The immediate analytic gate is therefore:

\[
\boxed{
\text{derive a finite-interval minus full-line decomposition of }
R_A^{(\pm)}
\text{ and of the two trace moments.}
}
\]

If that decomposition yields cancellation of the leading smooth/contact contribution, the residual can then be tested against the required
\[
r_{0,A}=o(e^A),
\qquad
r_{1,A}=o(e^A/A)
\]
edge scales.

## Result

The divisor-cone idea passes a strong structural test but fails as a literal functional identity.

Exact:
\[
\boxed{n=e^{2A},\quad s_k=\log k-A,\quad \sqrt n=e^A,}
\]
and the divisor shell admits exact parity-resolved rapidity discrepancy measures on the same \([-A,A]\) interval.

Not exact:
\[
\boxed{
\text{divisor discrepancy}\ne
\text{Suzuki basepoint trace functional}.
}
\]

The useful new strategy is the renormalization principle exposed by the comparison: subtract the full smooth/full-line contribution before applying quantitative bounds to the finite-\(A\) feedback moments.
