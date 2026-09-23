# Cone Derivation Ledger v13.721 — Suzuki Transport Multiplier and Conditional Xi Identification

Date: 2026-09-23

Status: source-faithful continuation of v13.720. This entry isolates what is exact about Suzuki's transport on exponential defects, derives the natural full-line multiplier form of the Section-8 operator, and states the strongest currently justified Suzuki–Xi identification.

Status labels: **[D]** exact derived, **[C]** conditional theorem, **[O]** open, **[G]** guardrail.

## 0. Synchronization

Immediately before this write the live head was v13.720, commit \`74da501f6d97ebbc9a91f7c7faa871ae7192226a\`. No v13.721 collision was present.

The source-faithful finite-\(A\) transport is v13.667:
\[
D=i\frac d{dx},
\qquad
\bar D:\mathcal H(T_A)\to\mathcal H(S_A),
\]
\[
S_Au_z=\bar D e_z,
\qquad
e_z(x)=e^{-izx}.
\]

## 1. The transport factor on exponentials [D]

On the exponential defect core,
\[
D e_z
=
i\frac d{dx}e^{-izx}
=
z e^{-izx}.
\]

Therefore, wherever the Section-8 extension \(\bar D\) is evaluated on Suzuki's exponential defect vector,
\[
\boxed{
\bar D e_z=z e_z
}
\]
in the transported energy-space sense.

Thus the transport itself introduces only the scalar spectral multiplier
\[
\boxed{z.}
\]

At the deficiency points,
\[
\boxed{
\bar D e_{+i}=i e^x,
\qquad
\bar D e_{-i}=-i e^{-x}.
}
\]

Hence the source side of the defect equation is
\[
\boxed{
S_Au_z=z e_z.
}
\]

This removes one of the two unknown factors left in v13.720: \(\bar D\) does not create an \(r\)-dependent theta-kernel multiplier on exponentials.

## 2. Exact simplification of the Neumann inverse on mean-zero data [D]

Suzuki's Section-8 kernel is
\[
S_A=G_A-\lambda K_A,
\qquad
K_A=(-\Delta_N)^{-1},
\]
with
\[
N_A(x,y)
=
\frac{x^2+y^2}{4A}
-\frac{|x-y|}{2}
+\frac A6.
\]

For \(f\in L_0^2(-A,A)\),
\[
\int_{-A}^{A}f(y)\,dy=0.
\]

Therefore the terms depending only on \(x\) and the constant term vanish under \(y\)-integration:
\[
\int\left(\frac{x^2}{4A}+\frac A6\right)f(y)\,dy=0.
\]

The remaining \(y^2/(4A)\) term is independent of \(x\), so it is a rank-one/constant-output correction. In pairings against another mean-zero function it also vanishes.

Thus on the mean-zero quadratic-form level,
\[
\boxed{
\langle f,K_Ag\rangle
=
-\frac12
\int_{-A}^{A}\int_{-A}^{A}
\overline{f(x)}\,|x-y|\,g(y)\,dy\,dx.
}
\]

Hence the bulk part of \(K_A\) is exactly the compressed translation-invariant kernel
\[
\boxed{k_\infty(r)=-\frac{|r|}{2}.}
\]

This is the Green kernel of \(-d^2/dx^2\) on the line, modulo the zero-frequency ambiguity expected from the mean-zero condition.

## 3. Natural full-line bulk symbol [D/G]

The \(G_A\) part already has difference form
\[
g_A(x-y).
\]

Ignoring only finite-boundary compression and the constant-output Neumann correction, the bulk Section-8 operator therefore has the translation-invariant form
\[
\boxed{
S_\infty
=
\mathcal G-\lambda\mathcal K,
}
\]
with kernels
\[
g(r),\qquad -\frac{|r|}{2}.
\]

For an exponential mode \(e_z(x)=e^{-izx}\), any full-line convolution realization diagonalizes:
\[
\mathcal G e_z=\widehat g(z)e_z,
\]
and formally/away from zero frequency
\[
\mathcal K e_z=\frac1{z^2}e_z,
\]
since
\[
-\frac{d^2}{dx^2}e_z=z^2e_z.
\]

Thus the natural bulk symbol is
\[
\boxed{
\sigma_S(z)
=
\widehat g(z)-\frac{\lambda}{z^2}.
}
\]

This formula is exact for the corresponding full-line convolution operator when the transforms exist in the chosen distributional sense. Its identification as the strong \(A\to\infty\) limit of the finite Suzuki \(S_A\) on deficiency modes still requires a boundary-layer theorem.

## 4. Conditional asymptotic defect multiplier [C]

Assume the following finite-to-full-line hypothesis for a fixed spectral \(z\):

**H1.** There is a bulk region whose distance from both endpoints tends to infinity with \(A\).

**H2.** On the exponential mode,
\[
S_A e_z
=
\sigma_S(z)e_z+\rho_{A,z},
\]
where the remainder is negligible in the pairing/normalization used in v13.720.

**H3.**
\[
\sigma_S(z)\ne0.
\]

Then from
\[
S_Au_z=z e_z
\]
one obtains
\[
\boxed{
u_z
=
\frac{z}{\sigma_S(z)}e_z
+
o_{\rm bulk}(1).
}
\]

Define
\[
\boxed{
c_S(z)=\frac{z}{\sigma_S(z)}.
}
\]

Therefore the full Suzuki defect response is asymptotically the raw exponential core times a scalar channel multiplier.

This is exactly the favorable scenario isolated as the missing condition in v13.720.

## 5. Consequence for theta-kernel defect pairings [C]

Under H1–H3 strongly enough to pass through the Hilbert--Schmidt theta pairing,
\[
\langle u_{\bar z},H_\theta u_{\pm i}\rangle
\sim
\overline{c_S(\bar z)}\,c_S(\pm i)
\langle e_{\bar z},H_\theta e_{\pm i}\rangle.
\]

Thus the nontrivial \(r\)-dependence remains entirely in the theta matrix element already analyzed in v13.719–720; Suzuki's transport/resolvent contributes scalar channel factors only.

Define renormalized Suzuki channel quantities by dividing those known multipliers:
\[
\boxed{
\widetilde M_{A,\pm}^{Suz}(z)
=
\frac{
\langle u_{\bar z},H_\theta u_{\pm i}\rangle
}{
\overline{c_S(\bar z)}\,c_S(\pm i)
}.
}
\]

Then
\[
\widetilde M_{A,\pm}^{Suz}(z)
=
M_{A,\pm}(z)+o(e^A)
\]
in the deficiency normalization regime.

Consequently all paired-channel asymptotics of v13.720 survive.

## 6. Conditional paired Suzuki–Xi identity [C]

Let
\[
C_\theta=\int_0^\infty K_\theta(r)e^{-r}\,dr.
\]

Define
\[
\mathcal L_+^{Suz}(z)
=
i(z-i)
\lim_{A\to\infty}
e^{-A}e^{-izA}
\widetilde M_{A,+}^{Suz}(z),
\]
\[
\mathcal L_-^{Suz}(z)
=
-i(z+i)
\lim_{A\to\infty}
e^{-A}e^{izA}
\widetilde M_{A,-}^{Suz}(z).
\]

Under H1–H3 and the pairing-error hypothesis,
\[
\boxed{
\mathcal L_+^{Suz}(z)
=
C_\theta+\int_0^\infty K_\theta(r)e^{-izr}\,dr,
}
\]
\[
\boxed{
\mathcal L_-^{Suz}(z)
=
C_\theta+\int_0^\infty K_\theta(r)e^{izr}\,dr.
}
\]

Therefore
\[
\boxed{
I_\theta(-iz)
=
\mathcal L_+^{Suz}(z)
+
\mathcal L_-^{Suz}(z)
-
2C_\theta.
}
\]

Putting
\[
z=iw
\]
gives the conditional source-faithful identity
\[
\boxed{
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)
\left[
\mathcal L_+^{Suz}(iw)
+
\mathcal L_-^{Suz}(iw)
-
2C_\theta
\right].
}
\]

This is the precise form a Suzuki–Xi identification would take if the full-line multiplier hypothesis is proved.

## 7. What has actually been proved versus what has not [D/G]

### Exact now

1. Suzuki's transport acts on the exponential defects by
   \[
   \boxed{\bar D e_z=z e_z.}
   \]

2. The mean-zero Neumann inverse has bulk difference kernel
   \[
   \boxed{-|x-y|/2.}
   \]

3. The natural full-line Section-8 bulk symbol is
   \[
   \boxed{\sigma_S(z)=\widehat g(z)-\lambda/z^2}
   \]
   for the corresponding convolution realization.

4. v13.720 exactly reconstructs \(I_\theta\) from the paired normalized raw deficiency exponentials.

### Not yet exact for finite Suzuki

We have not proved
\[
S_A^{-1}e_z
\sim
\sigma_S(z)^{-1}e_z
\]
with the boundary-error control needed for the exponentially growing deficiency channels.

This matters because \(e^{\pm x}\) concentrate their norm near an endpoint as \(A\to\infty\). A bulk strong-limit theorem alone is insufficient: the deficiency normalization is explicitly boundary-sensitive.

Therefore the strongest status is
\[
\boxed{
\textbf{Suzuki--Xi identification: CONDITIONAL, not yet promoted to theorem.}
}
\]

## 8. Critical boundary-layer obstruction [D/G]

The deficiency sources
\[
e^x,\qquad e^{-x}
\]
have
\[
\|e^x\|_{L^2(-A,A)}^2
=
\|e^{-x}\|_{L^2(-A,A)}^2
=
\sinh(2A),
\]
so their normalized mass concentrates at \(+A\) and \(-A\), respectively.

Thus the exact asymptotic needed is not merely the interior/full-line symbol of \(S_A\), but the **edge symbol / boundary-layer response** of
\[
S_A^{-1}
\]
on these exponentially localized deficiency sources.

This explains why the finite-\(A\) edge term \(C_\theta\) appeared in v13.720.

Any proof that ignores this concentration is insufficient.

## 9. Decisive next test [O]

Introduce edge coordinates
\[
\xi=A-x
\quad\text{for }u_+,
\qquad
\xi=A+x
\quad\text{for }u_-.
\]

Then
\[
e^x=e^A e^{-\xi},
\qquad
e^{-x}=e^A e^{-\xi}.
\]

After factoring out \(e^A\), derive the half-line limit of the Section-8 equation
\[
S_Au_\pm=\pm i\,e^{\pm x}
\]
in the edge coordinate.

The correct limiting object should be a Wiener--Hopf/half-line operator obtained from the difference kernel \(g(r)-\lambda(-|r|/2)\), plus any surviving Neumann boundary correction.

If the half-line resolvent sends \(e^{-\xi}\) to a scalar multiple of \(e^{-\xi}\), then the conditional identity in Section 6 becomes exact after scalar channel normalization.

If it produces a nontrivial profile \(q(\xi)\), then the theta transform is modified by the Laplace transform of that edge profile, and the naive Suzuki–Xi identification fails in a precisely computable way.

This edge-resolvent gate is now the decisive missing theorem.
