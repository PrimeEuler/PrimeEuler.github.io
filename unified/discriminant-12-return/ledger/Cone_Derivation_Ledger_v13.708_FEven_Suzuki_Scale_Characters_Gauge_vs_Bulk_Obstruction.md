# Cone Derivation Ledger v13.708 — F-Even Suzuki Scale Characters: Common Gauge versus Bulk Obstruction

Date: 2026-09-23

Status: exact character test following v13.706 and External Audit Round 81 (v13.707). This entry tests the two proposed F-even candidates for the remaining cone logarithmic directions \(\Re\tau\) and \(\Im\tau\): (i) a same-domain bulk relative determinant, and (ii) the common characteristic gauge multiplying Suzuki's deficiency characteristic.

## 0. Synchronization and correction gate

Immediately before this write the live head was v13.707, External Audit Round 81, commit \`30d25fc1468969099002462be72eb82bb5dcee0e\`. Round 81 independently verified v13.705–706 and the boost-character assignment. No v13.708 collision was present.

A mandatory source correction from v13.662 controls the present test:

\[
\boxed{
\text{No Suzuki same-domain bulk determinant against the local Dirichlet Laplacian has been established.}
}
\]

v13.662 re-read Suzuki's actual domains and showed that the earlier schematic decomposition
\[
H_A=H_{0,A}+V_A
\]
on a common operator domain was not derived and is generally incompatible with the source domain structure. Therefore the old candidate \(\Delta^{bulk}\) from that additive decomposition cannot be used as a proved Suzuki object.

The exact finite-\(A\) comparison supplied by Suzuki is instead the energy-space transfer
\[
\bar D:\mathcal H(T_A)\overset{\sim}{\longrightarrow}\mathcal H(S_A),
\]
with
\[
T_A=A_A-\lambda I,\qquad
S_A=G_A-\lambda(-\Delta_N)^{-1}.
\]

## 1. Candidate 1: same-domain bulk relative determinant

### 1.1 Existence test

The proposed scale-character assignment would require a genuine nonzero complex quantity
\[
\Delta_A^{bulk}(z)
\]
intrinsic to Suzuki's same-domain/full-vs-reference operator comparison.

But v13.662 proves that the particular \(\Delta^{bulk}\) previously used in v13.644 was only formal/hypothetical for Suzuki's operator.

Therefore:
\[
\boxed{
\Delta_A^{bulk}\text{ is presently NOT an established Suzuki quantity in the required sense.}
}
\]

Consequently neither
\[
\Re\log\Delta_A^{bulk}\stackrel?{\leftrightarrow}\Re\tau
\]
nor
\[
\Im\log\Delta_A^{bulk}\stackrel?{\leftrightarrow}\Im\tau
\]
can be promoted.

### 1.2 Conditional character law

If in the future a genuine same-domain relative determinant is constructed from an operator pair independent of the deficiency-channel labeling, then deficiency reflection would leave it unchanged:
\[
\mathscr R:\Delta^{bulk}\mapsto\Delta^{bulk}.
\]
Under a real-operator determinant symmetry
\[
\Delta^{bulk}(\bar z)=\overline{\Delta^{bulk}(z)},
\]
its local logarithm would satisfy
\[
\Re\log\Delta^{bulk}:(+,+),
\qquad
\Im\log\Delta^{bulk}:(+,-).
\]

This is exactly the desired scale pair, but at present it is only a **conditional template**, not a proved Suzuki correspondence.

## 2. Candidate 2: common characteristic gauge

Let a common nonzero characteristic gauge \(g(z)\) multiply every extension characteristic:
\[
\widetilde W_\theta(z)=g(z)W_\theta(z).
\]

Because deficiency reflection acts only by exchanging the two deficiency channels, the common factor is unchanged:
\[
\boxed{
\mathscr R:g\mapsto g.
}
\]

Thus any local logarithm
\[
L_g=\log g
\]
is F-even:
\[
\boxed{
\mathscr R:L_g\mapsto L_g.
}
\]

This is exact at the characteristic-gauge level.

If the gauge is chosen compatibly with the real structure,
\[
\boxed{
g(\bar z)=\overline{g(z)},
}
\]
then
\[
L_g(\bar z)=\overline{L_g(z)}
\]
locally modulo \(2\pi i\). Writing
\[
L_g=p+iq,
\]
gives
\[
p\mapsto p,\qquad q\mapsto-q.
\]

Therefore:
\[
\boxed{
\Re L_g:(F,C)=(+,+),
}
\]
\[
\boxed{
\Im L_g:(F,C)=(+,-).
}
\]

These are exactly the remaining cone characters:
\[
\boxed{
\Re\tau:(+,+),\qquad
\Im\tau:(+,-).
}
\]

Hence the common characteristic gauge realizes the **correct character representation** for the cone scale logarithm.

## 3. But the gauge is not intrinsic spectral data

The common gauge cancels from every normalized extension quotient:
\[
\frac{\widetilde W_{\theta_1}/\widetilde W_{\theta_2}}
{(\widetilde W_{\theta_1}/\widetilde W_{\theta_2})(z_*)}
=
\frac{W_{\theta_1}/W_{\theta_2}}
{(W_{\theta_1}/W_{\theta_2})(z_*)}.
\]

Therefore \(g\) is not determined by the ordered extension pair or its Kreĭn resolvent difference.

Indeed Suzuki's heuristic permits a common entire factor of the form
\[
e^{\varphi(A,z)}
\]
in the finite-to-infinite comparison. Its logarithm is precisely a common additive characteristic term.

Thus:
\[
\boxed{
\text{the common gauge carries the desired }(+,+)\oplus(+,-)\text{ character pair,}
}
\]
but
\[
\boxed{
\text{it is gauge freedom, not yet a canonical physical/spectral scale coordinate.}
}
\]

This distinction is essential.

## 4. Exact factorization of the characteristic into gauge and boundary pieces

Using the v13.647 form,
\[
W_A(\theta;z)
=
G_A(z)\,[1-e^{i\theta}s_A(z)]
\]
where in the printed Suzuki normalization one may take
\[
G_A(z)=(z-i)F_{A,+}(z)
\]
and
\[
s_A^{Suz}(z)
=
-\frac{(z+i)F_{A,-}(z)}
{(z-i)F_{A,+}(z)}.
\]

At the purely algebraic characteristic level:
\[
\boxed{
\log W_A
=
\log G_A
+
\log(1-e^{i\theta}s_A).
}
\]

The second term contains the F-odd boost/boundary data resolved in v13.706. The first term is the natural F-even common term.

However, \(G_A\) itself depends on the chosen normalization of the deficiency basis/characteristic. Multiplying all \(W_\theta\) by any nonvanishing entire \(h(z)\) changes
\[
G_A\mapsto hG_A
\]
without changing the extension quotient.

Therefore \(G_A\) supplies a **representative** of the scale-character sector, not yet a canonical scale coordinate.

## 5. Character completion versus canonical completion

The four cone characters can now all be represented on Suzuki characteristic data:

\[
\begin{array}{c|c|c|c}
\text{cone direction}&(F,C)&\text{Suzuki representative}&\text{status}\\ \hline
\Re\tau&(+,+)&\Re\log g\ \text{or }\Re\log G_A&
\text{character proved; gauge-dependent}\\
\Im\tau&(+,-)&\Im\log g\ \text{or }\Im\log G_A&
\text{character proved; gauge-dependent}\\
\Re\ell&(-,+)&\Re\log s&
\text{intrinsic Cayley equivariance proved}\\
\Im\ell&(-,-)&\Im\log s,\ \theta&
\text{intrinsic character/equivariance proved}
\end{array}
\]

Thus:
\[
\boxed{
\textbf{the four-character representation is complete,}
}
\]
but
\[
\boxed{
\textbf{the four-coordinate canonical identification is not complete.}
}
\]

The boost pair is tied to the intrinsic Weyl/Cayley boundary data. The scale pair currently lives in common characteristic gauge freedom.

## 6. Why the normalized cross-ratio loses the scale sector too

v13.706 showed the normalized \(0/\pi\) cross-ratio loses the reflection sign:
\[
m\mapsto-m
\quad\Longrightarrow\quad
\frac{m(z)}{m(z_*)}\mapsto\frac{m(z)}{m(z_*)}.
\]

It also cancels any common characteristic gauge \(g(z)\) already at the unnormalized quotient \(W_0/W_\pi\).

Therefore the extension cross-ratio forgets **both**:

1. the common F-even gauge/scale sector;
2. the absolute F-odd sign of the Weyl coordinate.

What it retains is the relative \(z\)-dependence of the ordered extension pair.

This clarifies why the cross-ratio is robust for convergence yet insufficient for reconstructing the full four-character torus.

## 7. Relation to the v13.689 Friedrichs-vs-Zeeman discrepancy

The large stable mismatch found in v13.689 cannot be repaired by inserting the old local-Dirichlet \(\Delta^{bulk}\), because v13.662 already removed that factor from proved Suzuki status.

The present analysis does show that a common F-even normalization sector exists algebraically in \(W\). Therefore an even/odd relative-normalization issue can in principle live there.

But:
\[
\boxed{
\text{no specific }g(z)\text{ has been proved to explain the v13.689 discrepancy.}
}
\]

That remains a diagnostic direction only.

## 8. What would promote the scale pair from gauge to intrinsic

Any one of the following would suffice in principle:

1. derive a canonical same-domain relative determinant directly from Suzuki's actual energy-space pair \(T_A,S_A\);
2. impose a canonical de Branges/Cartwright normalization fixing the common entire factor;
3. derive \(G_A\) uniquely from the continuous-kernel defect equations plus a fixed asymptotic/base-point normalization;
4. show that a canonical Fredholm determinant in the \(S_A\) representation equals the common factor up to a real positive constant.

Until one of these is proved, the scale pair is a character-sector representative rather than intrinsic spectral data.

## 9. Result

\[
\boxed{
\textbf{FAIL / NOT AVAILABLE: }
\text{the previously proposed same-domain bulk determinant is not an established Suzuki object.}
}
\]

\[
\boxed{
\textbf{PROVED: }
\text{a common characteristic gauge is deficiency-reflection even.}
}
\]

Under a real-compatible gauge:
\[
\boxed{
\Re\log g:(+,+),\qquad
\Im\log g:(+,-).
}
\]

Therefore:
\[
\boxed{
\textbf{PROVED CHARACTER MATCH: }
(\Re\log g,\Im\log g)
\leftrightarrow
(\Re\tau,\Im\tau).
}
\]

But:
\[
\boxed{
\textbf{OPEN: }
\text{canonical/intrinsic identification of }g\text{ with the cone scale coordinate }\tau.
}
\]

Combined with v13.706:
\[
\boxed{
\begin{array}{c|c}
(+,+)&\Re\log g\quad\text{(gauge-dependent)}\\
(+,-)&\Im\log g\quad\text{(gauge-dependent)}\\
(-,+)&\Re\log s\quad\text{(intrinsic Cayley)}\\
(-,-)&\Im\log s,\theta\quad\text{(intrinsic boundary phase)}
\end{array}
}
\]

The full \(C_2^2\) character representation is therefore realized on Suzuki characteristic data, but only the boost half is presently canonical.

## 10. Next gate

The next non-artificial route is to use Suzuki's actual exact energy-space transfer
\[
\bar D:\mathcal H(T_A)\to\mathcal H(S_A)
\]
and ask whether the \(S_A\) continuous-kernel problem has a canonical Fredholm determinant or base-point-normalized characteristic that fixes the common gauge.

That is the correct place to search for an intrinsic \(\tau\)-coordinate. Do not revive the invalid local Dirichlet-Laplacian bulk determinant.
