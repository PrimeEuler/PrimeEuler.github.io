# Cone Derivation Ledger v13.719 — Theta Difference-Kernel Exponential Matrix Elements and the Xi Bridge Obstruction

Date: 2026-09-23

Status: exact finite-\(A\) transform test following v13.718. This entry tests whether the candidate pullback
\[
h_\theta(x,y)=K_\theta(x-y)
\]
turns Suzuki's exponential defect-source pairings into the bilateral theta/Mellin integral of v13.717.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization

Immediately before this write the live head was v13.718, commit \`92233d20f8f782fbe69f4305a18432f4bcd22816\`. No v13.719 collision was present.

Use
\[
K_\theta(r)
=
e^{|r|/2}\sum_{n\ge1}e^{-\pi n^2e^{2|r|}}
\]
from v13.717. It is real, even, continuous, and super-exponentially decaying.

Define on \([-A,A]\)
\[
(H_\theta f)(x)
=
\int_{-A}^{A}K_\theta(x-y)f(y)\,dy.
\]

Because the square is compact and the kernel is continuous,
\[
H_\theta\in\mathfrak S_2.
\]
It is self-adjoint and commutes with reflection.

## 1. General exponential matrix element [D]

Let
\[
e_a(x)=e^{-iax}.
\]
Consider the raw exponential matrix element
\[
M_A(a,b)
=
\langle e_{\bar a},H_\theta e_b\rangle_{L^2(-A,A)}.
\]

With the standard inner product this is
\[
M_A(a,b)
=
\int_{-A}^{A}\int_{-A}^{A}
e^{iax}K_\theta(x-y)e^{-iby}\,dy\,dx.
\]

Introduce
\[
r=x-y,\qquad c=\frac{x+y}{2}.
\]
Then
\[
x=c+\frac r2,\qquad y=c-\frac r2,\qquad dx\,dy=dc\,dr.
\]

The square maps to
\[
-2A\le r\le2A,
\qquad
-A+\frac{|r|}{2}
\le c\le
A-\frac{|r|}{2}.
\]

The exponential factor separates:
\[
e^{iax}e^{-iby}
=
e^{i(a-b)c}e^{i(a+b)r/2}.
\]

Therefore
\[
\boxed{
M_A(a,b)
=
\int_{-2A}^{2A}
K_\theta(r)
e^{i(a+b)r/2}
W_A(r;a-b)\,dr,
}
\]
where
\[
\boxed{
W_A(r;q)
=
\int_{-A+|r|/2}^{A-|r|/2}e^{iqc}\,dc
=
\frac{2\sin(q(A-|r|/2))}{q}
}
\]
for \(q\ne0\), with the removable limit
\[
\boxed{
W_A(r;0)=2A-|r|.
}
\]

Thus the exact finite-interval matrix element is a **windowed truncated bilateral transform** of the theta kernel.

## 2. Suzuki deficiency exponentials [D]

The canonical exponential deficiency points are
\[
e_{+i}(y)=e^y,\qquad
e_{-i}(y)=e^{-y}.
\]

Taking \(a=z\), \(b=+i\) gives
\[
\boxed{
M_{A,+}(z)
=
\int_{-2A}^{2A}
K_\theta(r)
e^{i(z+i)r/2}
\frac{2\sin((z-i)(A-|r|/2))}{z-i}\,dr.
}
\]

Taking \(a=z\), \(b=-i\) gives
\[
\boxed{
M_{A,-}(z)
=
\int_{-2A}^{2A}
K_\theta(r)
e^{i(z-i)r/2}
\frac{2\sin((z+i)(A-|r|/2))}{z+i}\,dr.
}
\]

At the removable special points \(z=\pm i\), the corresponding sine quotient is replaced by
\[
2A-|r|.
\]

These formulas are exact for the exponential cores.

## 3. Comparison with the Xi bilateral Mellin transform [D]

v13.717 defines
\[
I_\theta(w)
=
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr
\]
and
\[
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)I_\theta(w).
\]

The Suzuki finite-\(A\) matrix elements differ in three exact ways:

1. **support truncation**
   \[
   r\in[-2A,2A]
   \quad\text{instead of}\quad
   r\in\mathbb R;
   \]

2. **center/window factor**
   \[
   W_A(r;z\mp i)
   =
   \frac{2\sin((z\mp i)(A-|r|/2))}{z\mp i},
   \]
   which depends on \(|r|\) and cannot be absorbed into a constant normalization;

3. **spectral-variable map**
   \[
   w_+(z)=\frac{i(z+i)}2,
   \qquad
   w_-(z)=\frac{i(z-i)}2
   \]
   for the two deficiency channels, rather than one common \(w\).

Therefore
\[
\boxed{
M_{A,\pm}(z)\ne I_\theta(w)
}
\]
for finite \(A\) in general.

Consequently they do not reproduce
\[
\boxed{
\Xi(w)
=
\frac12+\left(w^2-\frac14\right)I_\theta(w)
}
\]
by a scalar prefactor or a single affine spectral reparameterization.

## 4. The diagonal channel exposes the geometric obstruction [D]

If \(a=b\), then
\[
\boxed{
M_A(a,a)
=
\int_{-2A}^{2A}
(2A-|r|)K_\theta(r)e^{iar}\,dr.
}
\]

Even in the channel where the center oscillation disappears, the finite square produces the triangular overlap factor
\[
\boxed{2A-|r|}.
\]

This factor is purely geometric: it is the length of the intersection
\[
[-A,A]\cap([-A,A]-r).
\]

Thus the obstruction is not a normalization accident. It comes from compressing a translation-invariant convolution kernel to a finite interval.

## 5. Source-faithful Suzuki guardrail [G]

Suzuki's actual continuous-kernel source is
\[
d_z=\bar D e_z,
\]
and v13.685 uses
\[
F_{A,\pm}(z)
=
\overline{
\langle d_{\bar z},S_A^{-1}d_\pm\rangle
}.
\]

The genuine kernel variation in v13.718 contains
\[
\langle u_{\bar z},H_\theta u_\pm\rangle,
\qquad
u_\pm=S_A^{-1}d_\pm.
\]

The formulas in Sections 1–4 are therefore the exact matrix elements of \(H_\theta\) against the **exponential cores** \(e_{\bar z},e_{\pm i}\). They become literal matrix elements against \(d_z=\bar D e_z\) only after transporting \(\bar D\) through the kernel or supplying its explicit action on these exponentials.

No such commutation/intertwining identity has yet been proved in the ledger.

Hence:
\[
\boxed{
\text{the raw exponential test already fails to equal the Xi transform,}
}
\]
and inserting the nontrivial \(\bar D\) and \(S_A^{-1}\) factors cannot be silently discarded.

## 6. Bilateral-transform reduction [D]

The strongest exact reduction is to a finite-window bilateral transform. Define
\[
\mathcal B_{\theta,A}[W](w)
=
\int_{-2A}^{2A}K_\theta(r)W(r)e^{wr}\,dr.
\]

Then
\[
\boxed{
M_{A,+}(z)
=
\mathcal B_{\theta,A}
\left[
\frac{2\sin((z-i)(A-|r|/2))}{z-i}
\right]
\left(\frac{i(z+i)}2\right),
}
\]
and
\[
\boxed{
M_{A,-}(z)
=
\mathcal B_{\theta,A}
\left[
\frac{2\sin((z+i)(A-|r|/2))}{z+i}
\right]
\left(\frac{i(z-i)}2\right).
}
\]

By contrast,
\[
\boxed{
I_\theta(w)=\mathcal B_{\theta,\infty}[1](w).
}
\]

This notation isolates exactly what would have to disappear in a successful limit/intertwiner:
\[
\boxed{
\text{finite support}+\text{overlap window}+\text{channel split}.
}
\]

## 7. Does the naive map r=x-y reproduce Xi? [D]

No.

The candidate
\[
r=x-y,\qquad h_\theta(x,y)=K_\theta(x-y)
\]
is admissible and structurally natural, but finite-\(A\) compression changes the bilateral Mellin transform into the windowed transform above.

Therefore:
\[
\boxed{
\textbf{FAIL: the naive difference-kernel pullback does not reproduce the v13.717 Xi integral.}
}
\]

This is a useful obstruction, not a failure of the broader bridge program. It identifies the missing ingredient precisely.

## 8. What would be needed for equality [O]

A direct equality with
\[
I_\theta(w)=\int_{\mathbb R}K_\theta(r)e^{wr}\,dr
\]
would require an operator realization on the full line, or a finite-\(A\) de-windowing/normalization whose limit can be justified.

The diagonal normalized overlap suggests
\[
\frac1{2A}M_A(a,a)
=
\int_{-2A}^{2A}
\left(1-\frac{|r|}{2A}\right)
K_\theta(r)e^{iar}\,dr.
\]

Because \(K_\theta\) decays super-exponentially,
\[
\boxed{
\lim_{A\to\infty}
\frac1{2A}M_A(a,a)
=
\int_{\mathbb R}K_\theta(r)e^{iar}\,dr
=
I_\theta(ia)
}
\]
for fixed \(a\), by dominated convergence.

Thus the bilateral theta transform **does emerge canonically as a volume-normalized infinite-window limit of the diagonal convolution matrix element.**

This is the first exact positive bridge statement.

But Suzuki's deficiency channels are off-diagonal \(b=\pm i\), not \(a=b\). Their center factors do not reduce to the triangular overlap weight, and no corresponding scalar volume normalization has yet been proved to yield \(I_\theta\).

## 9. Consequence for the cross-lane program [D/O]

We now have:

- exact finite-\(A\) admissibility of \(K_\theta(x-y)\);
- exact reduction of its exponential matrix elements to windowed bilateral transforms;
- exact obstruction to identifying finite-\(A\) deficiency-channel matrix elements with the Xi current;
- exact recovery of the Xi bilateral transform in the normalized diagonal \(A\to\infty\) convolution limit.

Therefore the promising bridge is not
\[
\boxed{\text{finite Suzuki deficiency matrix element}=\Xi}
\]
but rather
\[
\boxed{
\text{thermodynamic/full-line convolution symbol of }K_\theta
=
I_\theta.
}
\]

This points toward a Fourier/Laplace multiplier or full-line convolution-operator bridge rather than a literal finite-\(A\) characteristic identity.

## 10. Result

For raw exponentials,
\[
\boxed{
\langle e_{\bar a},H_\theta e_b\rangle
=
\int_{-2A}^{2A}
K_\theta(r)e^{i(a+b)r/2}
\frac{2\sin((a-b)(A-|r|/2))}{a-b}\,dr.
}
\]

For Suzuki's deficiency exponentials \(b=\pm i\), the two exact formulas are those in Section 2.

They are windowed/truncated bilateral transforms and **do not** reproduce the Xi integral at finite \(A\).

However,
\[
\boxed{
\lim_{A\to\infty}
\frac1{2A}
\langle e_{\bar a},H_\theta e_a\rangle
=
I_\theta(ia).
}
\]

So:
\[
\boxed{
\textbf{finite deficiency-channel equality: FAIL;}
}
\]
\[
\boxed{
\textbf{normalized diagonal full-line symbol equality: PASS.}
}
\]

## 11. Next gate [O]

The next high-value gate is to abandon the naive finite-deficiency equality and construct the full-line convolution operator
\[
(\mathcal K_\theta f)(x)
=
\int_{\mathbb R}K_\theta(x-y)f(y)\,dy.
\]

Then:

1. compute its Fourier/Laplace symbol exactly:
   \[
   \widehat K_\theta(\zeta)
   =
   \int_{\mathbb R}K_\theta(r)e^{\zeta r}\,dr
   =
   I_\theta(\zeta);
   \]
2. rewrite
   \[
   \Xi(w)
   =
   \frac12+
   \left(w^2-\frac14\right)\widehat K_\theta(w);
   \]
3. determine whether this can be realized as a determinant, characteristic, or boundary symbol of a canonical full-line operator;
4. only then compare that full-line operator with the finite-\(A\) Suzuki compressions.

That route preserves the exact positive bridge just found and avoids forcing an equality that the finite-window geometry forbids.
