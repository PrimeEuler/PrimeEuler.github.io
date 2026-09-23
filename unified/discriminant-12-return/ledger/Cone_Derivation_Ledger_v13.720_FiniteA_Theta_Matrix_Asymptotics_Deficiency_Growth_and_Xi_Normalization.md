# Cone Derivation Ledger v13.720 — Finite-A Theta Matrix Asymptotics, Deficiency Growth, and Xi Normalization

Date: 2026-09-23

Status: exact asymptotic continuation of v13.719. This entry determines the large-\(A\) behavior of the finite compressed theta-difference-kernel exponential matrix elements, including the overlap window and the \(e^{\pm x}\) deficiency-source growth, and states the exact normalizations under which the bilateral Xi transform is recovered or fails.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization

Immediately before this write the live head was v13.719, commit \`4d407e4986583bbc5544ad769f1536c4d0a04b95\`. No v13.720 collision was present.

Write
\[
K(r)=K_\theta(r),
\qquad
I(w)=I_\theta(w)=\int_{\mathbb R}K(r)e^{wr}\,dr.
\]

Because \(K\) is real, even, and super-exponentially decaying,
\[
I(w)
\]
is entire and every polynomial/exponential moment used below is finite on compact \(w\)-sets.

The finite exponential matrix element from v13.719 is
\[
M_A(a,b)
=
\int_{-2A}^{2A}
K(r)e^{i(a+b)r/2}
W_A(r;q)\,dr,
\qquad q=a-b,
\]
with
\[
W_A(r;q)
=
\frac{2\sin(q(A-|r|/2))}{q}
\]
for \(q\ne0\), and
\[
W_A(r;0)=2A-|r|.
\]

## 1. Diagonal asymptotics: the volume law [D]

For \(a=b\),
\[
M_A(a,a)
=
\int_{-2A}^{2A}
(2A-|r|)K(r)e^{iar}\,dr.
\]

Split:
\[
M_A(a,a)
=
2A\int_{-2A}^{2A}K(r)e^{iar}\,dr
-
\int_{-2A}^{2A}|r|K(r)e^{iar}\,dr.
\]

Define the first absolute-radius moment transform
\[
J_1(w)
=
\int_{\mathbb R}|r|K(r)e^{wr}\,dr.
\]

Super-exponential decay gives, uniformly for \(a\) in compact subsets of \(\mathbb C\),
\[
\boxed{
M_A(a,a)
=
2A\,I(ia)-J_1(ia)+o(1).
}
\]

In fact the remainder is super-exponentially small in \(A\) after multiplication by any fixed exponential \(e^{cA}\).

Therefore
\[
\boxed{
\frac{M_A(a,a)}{2A}
=
I(ia)-\frac{J_1(ia)}{2A}+o(A^{-1}).
}
\]

Hence
\[
\boxed{
\lim_{A\to\infty}\frac{1}{2A}M_A(a,a)=I(ia).
}
\]

This is the precise volume normalization.

If one wants \(I(w)\) for arbitrary \(w\in\mathbb C\), set
\[
\boxed{a=-iw.}
\]
Then
\[
\boxed{
\lim_{A\to\infty}
\frac1{2A}M_A(-iw,-iw)
=
I(w).
}
\]

Consequently
\[
\boxed{
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)
\lim_{A\to\infty}
\frac1{2A}M_A(-iw,-iw).
}
\]

This is an exact recovery of the v13.717 Xi integral from normalized diagonal compressed-convolution matrix elements.

## 2. General off-diagonal asymptotics for fixed q [D]

For fixed
\[
q=a-b\ne0,
\]
expand the overlap window:
\[
W_A(r;q)
=
\frac{e^{iqA}e^{-iq|r|/2}-e^{-iqA}e^{iq|r|/2}}{iq}.
\]

Define
\[
w_0=\frac{i(a+b)}2
\]
and the half-line folded transforms
\[
\boxed{
\mathcal J_\pm(w_0,q)
=
\int_{\mathbb R}
K(r)e^{w_0r}e^{\pm iq|r|/2}\,dr.
}
\]

Then truncation can be removed with super-exponentially small error:
\[
\boxed{
M_A(a,b)
=
\frac{
e^{iqA}\mathcal J_-(w_0,q)
-
e^{-iqA}\mathcal J_+(w_0,q)
}{iq}
+o(1)
}
\]
uniformly on compact parameter sets avoiding \(q=0\).

Because of \(|r|\), \(\mathcal J_\pm\) are not generally equal to the bilateral transform \(I(w)\). Explicitly, using evenness of \(K\),
\[
\mathcal J_\pm(w_0,q)
=
\int_0^\infty K(r)
\left[
e^{(w_0\pm iq/2)r}
+
e^{(-w_0\pm iq/2)r}
\right]dr.
\]

Thus fixed nonzero off-diagonal separation produces two folded half-line transforms, not one Xi transform.

If \(q\in\mathbb R\setminus\{0\}\), \(M_A(a,b)\) is bounded/oscillatory in \(A\), so
\[
\boxed{
\frac{M_A(a,b)}{2A}\to0.
}
\]

Hence volume normalization isolates the diagonal symbol and kills fixed real off-diagonal channels.

## 3. Complex q and deficiency-source growth [D]

Suzuki's deficiency channels have
\[
b=+i
\quad\text{or}\quad
b=-i.
\]

For a general complex \(z\), set \(a=z\).

### Plus deficiency channel

For \(b=+i\),
\[
q_+=z-i,
\qquad
w_{0,+}=\frac{i(z+i)}2.
\]

The exact asymptotic is
\[
\boxed{
M_{A,+}(z)
=
\frac{
e^{i(z-i)A}\mathcal J_-(w_{0,+},z-i)
-
e^{-i(z-i)A}\mathcal J_+(w_{0,+},z-i)
}{i(z-i)}
+o(1).
}
\]

Since
\[
e^{i(z-i)A}=e^{A}e^{izA},
\qquad
e^{-i(z-i)A}=e^{-A}e^{-izA},
\]
the first term is generically exponentially dominant:
\[
\boxed{
M_{A,+}(z)
\sim
\frac{e^{A}e^{izA}}
{i(z-i)}
\mathcal J_-(w_{0,+},z-i)
}
\]
provided the displayed coefficient is nonzero and \(z\) is kept in a fixed compact set.

Thus the natural deficiency normalization is
\[
\boxed{
e^{-A}e^{-izA}M_{A,+}(z)
\longrightarrow
\frac{\mathcal J_-(w_{0,+},z-i)}
{i(z-i)}.
}
\]

At \(z=i\) the formula is replaced by the removable diagonal case \(a=b=i\), where the growth is linear \(2A\), not exponential. Therefore the asymptotic above is not uniform through \(z=i\).

### Minus deficiency channel

For \(b=-i\),
\[
q_-=z+i,
\qquad
w_{0,-}=\frac{i(z-i)}2.
\]

Now
\[
e^{i(z+i)A}=e^{-A}e^{izA},
\qquad
e^{-i(z+i)A}=e^{A}e^{-izA}.
\]

The second term is generically dominant:
\[
\boxed{
M_{A,-}(z)
\sim
-
\frac{e^{A}e^{-izA}}
{i(z+i)}
\mathcal J_+(w_{0,-},z+i)
}
\]
provided the coefficient is nonzero.

The natural normalization is
\[
\boxed{
e^{-A}e^{izA}M_{A,-}(z)
\longrightarrow
-
\frac{\mathcal J_+(w_{0,-},z+i)}
{i(z+i)}.
}
\]

Again \(z=-i\) is a separate diagonal/linear-growth point.

## 4. The deficiency limits simplify, but not to I(w) [D]

For the plus channel,
\[
w_{0,+}-\frac{i(z-i)}2
=
-1,
\]
while
\[
-w_{0,+}-\frac{i(z-i)}2
=
-iz.
\]

Therefore
\[
\boxed{
\mathcal J_-(w_{0,+},z-i)
=
\int_0^\infty K(r)\left(e^{-r}+e^{-izr}\right)dr.
}
\]

For the minus channel,
\[
w_{0,-}+\frac{i(z+i)}2
=
-1,
\]
and
\[
-w_{0,-}+\frac{i(z+i)}2
=
iz.
\]

Hence
\[
\boxed{
\mathcal J_+(w_{0,-},z+i)
=
\int_0^\infty K(r)\left(e^{-r}+e^{izr}\right)dr.
}
\]

Thus the normalized deficiency limits are
\[
\boxed{
\lim_{A\to\infty}
e^{-A}e^{-izA}M_{A,+}(z)
=
\frac{1}{i(z-i)}
\int_0^\infty K(r)\left(e^{-r}+e^{-izr}\right)dr,
}
\]
and
\[
\boxed{
\lim_{A\to\infty}
e^{-A}e^{izA}M_{A,-}(z)
=
-\frac{1}{i(z+i)}
\int_0^\infty K(r)\left(e^{-r}+e^{izr}\right)dr.
}
\]

These are one-sided folded transforms plus a fixed \(e^{-r}\) contribution.

They are **not**
\[
I(w)=\int_{\mathbb R}K(r)e^{wr}dr
\]
for generic \(z,w\).

Because \(K\) is even,
\[
I(-iz)
=
\int_0^\infty K(r)\left(e^{-izr}+e^{izr}\right)dr.
\]

The two deficiency limits separately contain only one of these two oscillatory halves, plus the common term
\[
C_\theta:=\int_0^\infty K(r)e^{-r}dr.
\]

## 5. A symmetric combination reconstructs the bilateral transform [D]

Define the normalized channel limits
\[
L_+(z)
=
i(z-i)\lim_{A\to\infty}e^{-A}e^{-izA}M_{A,+}(z),
\]
\[
L_-(z)
=
-i(z+i)\lim_{A\to\infty}e^{-A}e^{izA}M_{A,-}(z).
\]

Then
\[
\boxed{
L_+(z)=C_\theta+\int_0^\infty K(r)e^{-izr}dr,
}
\]
\[
\boxed{
L_-(z)=C_\theta+\int_0^\infty K(r)e^{izr}dr.
}
\]

Add them:
\[
L_+(z)+L_-(z)
=
2C_\theta+I(-iz).
\]

Therefore
\[
\boxed{
I(-iz)
=
L_+(z)+L_-(z)-2C_\theta.
}
\]

Equivalently, set
\[
z=iw.
\]
Then
\[
\boxed{
I(w)
=
L_+(iw)+L_-(iw)-2C_\theta.
}
\]

This is a second exact recovery mechanism for the Xi transform: **not from either deficiency channel separately, but from the symmetrically renormalized pair after subtraction of a universal common term.**

Consequently
\[
\boxed{
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)
\left[
L_+(iw)+L_-(iw)-2C_\theta
\right].
}
\]

This is the strongest direct large-\(A\) deficiency-source bridge currently established for the raw exponential cores.

## 6. Interpretation of the common term [D/G]

The term
\[
\boxed{
C_\theta=\int_0^\infty K_\theta(r)e^{-r}dr
}
\]
is independent of \(z\) and appears identically in both deficiency channels.

It arises from the exponentially amplified boundary edge of the finite interval, not from the bilateral spectral transform.

Its cancellation in
\[
L_++L_--2C_\theta
\]
is therefore a genuine de-windowing/boundary-renormalization step.

This is structurally reminiscent of the common characteristic gauge sector discussed in v13.708, but no identity between \(C_\theta\) and Suzuki's characteristic common factor is asserted.

## 7. Precise hypotheses [D]

The asymptotics above hold under:

1. \(K\) is even and measurable;
2. for every compact spectral set used, the required weighted moments
   \[
   \int_{\mathbb R}|K(r)|e^{c|r|}(1+|r|)\,dr<\infty
   \]
   hold for a sufficiently large finite \(c\);
3. \(a,b,z\) are fixed as \(A\to\infty\);
4. off-diagonal formulas are taken away from \(a=b\), with diagonal points handled by the removable limit;
5. for the quoted leading deficiency asymptotic, the leading folded-transform coefficient is nonzero.

For \(K=K_\theta\), v13.717's super-exponential decay satisfies all weighted-moment hypotheses for arbitrary compact spectral sets.

## 8. Source-faithful Suzuki hypothesis [G/O]

The calculations above still concern the exponential cores
\[
e_z(x)=e^{-izx}.
\]

Suzuki's transported sources are
\[
d_z=\bar D e_z,
\]
and the actual defect responses are
\[
u_z=S_A^{-1}d_z.
\]

To transfer the large-\(A\) formulas literally to
\[
\langle d_{\bar z},H_\theta d_\pm\rangle
\quad\text{or}\quad
\langle u_{\bar z},H_\theta u_\pm\rangle,
\]
one needs asymptotic control of the \(A\)-dependent transport/resolvent factors:
\[
\bar D_A,\qquad S_A^{-1}.
\]

A sufficient hypothesis would be an intertwining/asymptotic-symbol statement showing that, after known scalar normalizations,
\[
\bar D_A e_z
\sim c_D(z,A)e_z,
\qquad
S_A^{-1}\bar D_Ae_{\pm i}
\sim c_\pm(A)e_{\pm i}
\]
in a norm strong enough to pass through the Hilbert--Schmidt pairing, with errors \(o(e^A)\) for deficiency normalization or \(o(A)\) for diagonal volume normalization.

No such theorem is currently proved.

Therefore:
\[
\boxed{
\text{the raw exponential-core Xi recovery is exact;}
}
\]
\[
\boxed{
\text{the full Suzuki defect-source Xi recovery remains conditional on transport/resolvent asymptotics.}
}
\]

## 9. Recovery/failure table [D/G]

### Exact recovery

Diagonal/full-line symbol:
\[
\boxed{
\frac1{2A}M_A(-iw,-iw)\to I(w).
}
\]

Paired deficiency cores:
\[
\boxed{
L_+(iw)+L_-(iw)-2C_\theta\to I(w)
}
\]
where \(L_\pm\) are the individually phase/exponential-renormalized channel limits defined above.

### Failure

No normalization by \(2A\) recovers \(I(w)\) from a fixed off-diagonal deficiency channel:
the channel grows generically as \(e^A\), not \(A\).

No scalar \(A\)-dependent normalization of a **single** deficiency channel removes its one-sided/folded transform and common \(C_\theta\) term to produce generic \(I(w)\).

Finite-\(A\) equality fails because of truncation and the overlap window.

### Conditional full-Suzuki recovery

The same conclusions extend to the actual transported/resolved defect sources only if the asymptotic action of \(\bar D_A\) and \(S_A^{-1}\) is controlled and shown not to introduce additional nontrivial \(r\)-dependent symbols.

## 10. Result [D/G]

The overlap window has two distinct asymptotic regimes:

- diagonal:
  \[
  W_A(r;0)=2A-|r|,
  \]
  producing a volume law and the exact normalized limit \(I(w)\);

- deficiency off-diagonal:
  complex separation \(q=z\mp i\) produces exponentially amplified boundary terms of order \(e^A\), whose normalized limits are folded half-line transforms.

For the raw exponential cores,
\[
\boxed{
\textbf{PASS: Xi is recovered by }(2A)^{-1}\textbf{ diagonal normalization.}
}
\]

More surprisingly,
\[
\boxed{
\textbf{PASS: Xi is also recovered from the paired deficiency channels after }e^{-A}
\textbf{ phase normalization and subtraction of }2C_\theta.
}
\]

But
\[
\boxed{
\textbf{FAIL: either deficiency channel alone is the Xi transform.}
}
\]

And
\[
\boxed{
\textbf{OPEN: source-faithful full Suzuki recovery including }\bar D_A,S_A^{-1}.
}
\]

## 11. Next gate [O]

The next decisive gate is now sharply defined: derive the explicit action of Suzuki's transport
\[
\bar D_A
\]
on the exponential sources \(e_z\), and determine the large-\(A\) asymptotics of
\[
u_\pm=S_A^{-1}\bar D_Ae_{\pm i}.
\]

The goal is to decide whether the paired deficiency-core identity survives with only scalar channel normalizations, or whether the transport/resolvent introduces a nontrivial multiplier that changes the theta symbol.

This is the exact missing step between the raw full-line convolution bridge and a genuine Suzuki-to-Xi operator bridge.
