# Cone Derivation Ledger v13.737 — Analytic Screw Current, Paired Deficiency Channel, and Xi/E Gate

Date: 2026-09-23

Status: continuation of the Suzuki edge lane after v13.733 (the Wiener–Hopf edge equation, renumbered from v13.732). Several gates are advanced: analytic regularization of the screw current, centered-variable symmetry, integration from logarithmic derivative to Xi, and comparison with Suzuki's exact Section-7 paired deficiency identity. The result isolates the de Branges factor \(E\), not the raw edge transfer, as the remaining normalization/scattering object.

Synchronization: live head before this write was v13.734, commit \`ccf4c2096638c4bd671eb6f889ca43a2beebc533\`. That entry (originally labeled v13.734, now renumbered v13.736 — see its own renumbering note) is an adelic norm-quotient correction and does not collide with this lane. External Audit Round 86 independently verified v13.724--731, including the compensated edge source and scalar-profile obstruction.

**Renumbering note (External Audit Round 87):** this entry was originally committed as v13.735 (commit `8d9b3a0`, 2026-09-23T21:40:35Z), the latest of a chain of near-simultaneous collisions among four other entries at v13.732/v13.733/v13.734 that day. Once those four are resolved to v13.733/v13.734/v13.735/v13.736 (see each entry's own renumbering note), this entry is pushed to v13.737 to remain the last and collision-free in the sequence. No mathematical content was changed.

## Gate 1. Analytic regularization of the screw current [D]

The raw differentiated Suzuki screw kernel
\[
\mathcal K=-g''
\]
is a tempered Weil explicit-formula distribution, so its raw Fourier transform is not an ordinary scalar Wiener--Hopf symbol.

The correct analytic object is obtained by pairing the corresponding signed logarithmic current against compensated exponentials. With
\[
L(s):=\frac{\xi'}{\xi}(s),
\]
the already-established exact current identity is
\[
\boxed{
L(s)-L(2)
=
\int_0^\infty(e^{-sr}-e^{-2r})\,d\nu_\xi(r),
\qquad \Re s>1.
}
\]

Thus the source-faithful analytic regularization of the screw current is, up to the fixed subtraction at \(s=2\),
\[
\boxed{\mathscr C(s)=L(s)-L(2).}
\]

The subtraction is the analytic counterpart of the compensation/gauge needed to pair a nondecaying/distributional screw current with exponentials.

## Gate 2. Centered variable and reflection parity [D]

Set
\[
s=\frac12+w.
\]
Since
\[
\xi(s)=\xi(1-s),
\]
differentiation gives
\[
L(s)=-L(1-s).
\]

Therefore
\[
\boxed{
L\!\left(\frac12+w\right)
=
-L\!\left(\frac12-w\right).
}
\]

Define
\[
\ell(w):=L\!\left(\frac12+w\right).
\]
Then
\[
\boxed{\ell(-w)=-\ell(w).}
\]

So the analytically regularized screw current lives naturally in the **odd reflection character**, whereas
\[
\Xi(w):=\xi\!\left(\frac12+w\right)
\]
is even:
\[
\boxed{\Xi(-w)=\Xi(w).}
\]

This exactly matches the derivative relation
\[
\boxed{
\ell(w)=\frac{\Xi'(w)}{\Xi(w)}.
}
\]

## Gate 3. Exact integration back to Xi [D]

Away from zeros of \(\Xi\),
\[
\frac{d}{dw}\log\Xi(w)=\ell(w).
\]

Hence for any path avoiding zeros,
\[
\boxed{
\frac{\Xi(w)}{\Xi(w_0)}
=
\exp\left(\int_{w_0}^{w}\ell(u)\,du\right).
}
\]

Taking \(w_0=0\), where
\[
\Xi(0)=\xi(1/2)\ne0,
\]
gives locally and by analytic continuation through the canonical entire function,
\[
\boxed{
\Xi(w)
=
\Xi(0)\exp\left(\int_0^w
\frac{\Xi'(u)}{\Xi(u)}\,du\right),
}
\]
with the usual zero/winding bookkeeping for logarithms.

Because \(\ell\) is odd, its integral from \(0\) to \(w\) is even, recovering the Xi reflection parity automatically.

Thus the screw and theta currents are not competing realizations. They are related by:
\[
\boxed{
\text{screw current}
\;\xrightarrow{\rm analytic\ regularization}\;
\Xi'/\Xi
\;\xrightarrow{\rm integrate+normalize}\;
\Xi
\;\xleftarrow{\rm bilateral\ transform}\;
\Phi_\theta.
}
\]

This is an exact bridge at the level of scalar analytic functions.

## Gate 4. What the Green subtraction does analytically [D/C]

The Section-8 edge operator is
\[
S_{\rm edge}=G_{\rm edge}-\lambda K_{\rm edge}.
\]

After two derivatives, the Green part contributes the scalar \(-\lambda\) in the formal differentiated symbol
\[
\mathcal D=\widehat{-g''}-\lambda.
\]

Thus the analytic regularization of the differentiated edge current is naturally of the form
\[
\boxed{
\mathscr D_\lambda(s)
=
\mathscr C_{\rm screw}(s)-\lambda\,\mathscr C_{\rm Green}(s),
}
\]
where the Green term is elementary but the precise normalization depends on the chosen compensated Cauchy/Laplace transform and on the rank-one boundary moment \(M=Q(0)\).

It is therefore not source-faithful to identify the edge denominator simply with
\[
L(s)-\lambda.
\]

The rank-one boundary datum remains essential. This prevents an unjustified promotion of the scalar regularization to an operator identity.

## Gate 5. Suzuki's exact infinite-volume paired identity [D/source]

Suzuki Section 7 gives the exact boundary combination
\[
\boxed{
(z-i)\widehat f_{+i}(z)
-
(z+i)\widehat f_{-i}(z)
=
C_\xi
\frac{\xi(1/2-iz)}{E(z)},
}
\]
where
\[
C_\xi=\frac{2\xi'(3/2)}{\pi^2 i}.
\]

Introduce
\[
w=-iz.
\]
Then
\[
\boxed{
(z-i)\widehat f_{+i}(z)
-
(z+i)\widehat f_{-i}(z)
=
C_\xi\frac{\Xi(w)}{E(z)}.
}
\]

This is the exact source-side target that the Section-8 edge limit must reproduce if the finite-volume/edge theory converges to Suzuki's infinite-volume de Branges model in the relevant sense.

## Gate 6. Paired transfer rather than single transfer [D/C]

Let the normalized right/left edge profiles have analytic transforms
\[
Q_+(z),\qquad Q_-(z),
\]
and define channel transfers relative to their raw exponential source factors:
\[
\mathcal T_+(z):=(z-i)Q_+(z),
\qquad
\mathcal T_-(z):=(z+i)Q_-(z),
\]
with convention-dependent factors of \(i\) suppressed only at this schematic normalization step.

v13.727 proves neither channel can be a constant scalar multiple of its raw exponential profile.

The Section-7 identity shows that the correct invariant is instead the paired combination
\[
\boxed{
\mathcal T_{\rm pair}(z)
:=
\mathcal T_+(z)-\mathcal T_-(z).
}
\]

If the edge limit matches Suzuki's infinite-volume normalization, then necessarily
\[
\boxed{
\mathcal T_{\rm pair}(z)
=
C_\xi\frac{\Xi(-iz)}{E(z)}.
}
\]

This is not yet an edge-limit theorem; it is the exact matching condition supplied by Suzuki's already-proven infinite-volume theory.

## Gate 7. Logarithmic derivative of the paired target [D]

Take a logarithmic derivative of the exact target:
\[
\frac{d}{dz}
\log\frac{\Xi(-iz)}{E(z)}
=
-i\,\frac{\Xi'(-iz)}{\Xi(-iz)}
-\frac{E'(z)}{E(z)}.
\]

Therefore
\[
\boxed{
\frac{\mathcal T_{\rm pair}'(z)}
{\mathcal T_{\rm pair}(z)}
=
-i\,L\!\left(\frac12-iz\right)
-\frac{E'(z)}{E(z)}
}
\]
where the identity is understood away from zeros/poles and after the constant \(C_\xi\) drops out.

This is the key analytic comparison:

- the screw current supplies the first term,
  \[
  -i\,L(1/2-iz);
  \]
- the discrepancy between the raw screw primitive and the paired deficiency transfer is exactly the de Branges normalization/scattering term
  \[
  \boxed{-E'/E.}
  \]

Thus the remaining transfer is not mysterious: at the scalar analytic level it is encoded by \(E\).

## Gate 8. Exact quotient that removes the Xi part [D]

Define
\[
\boxed{
\mathcal R(z)
:=
\frac{E(z)\mathcal T_{\rm pair}(z)}
{\Xi(-iz)}.
}
\]

Suzuki's Section-7 identity gives
\[
\boxed{
\mathcal R(z)=C_\xi
}
\]
identically in the infinite-volume model.

Equivalently,
\[
\boxed{
\frac{d}{dz}\log\mathcal R(z)=0.
}
\]

This is a much sharper target for the Section-8 edge limit than asking whether a single \(\mathcal T_{\rm edge}\) equals Xi.

The finite/edge convergence test should therefore be:
\[
\boxed{
\mathcal R_A(z)
:=
\frac{E(z)\mathcal T_{{\rm pair},A}(z)}
{\Xi(-iz)}
\stackrel{A\to\infty}{\longrightarrow}
C_\xi.
}
\]

If this convergence holds locally uniformly away from zeros, the Suzuki--Xi identification is recovered in the precise paired-channel/de Branges-normalized sense.

## Gate 9. Comparison with theta representation [D]

From v13.722,
\[
\Xi(w)=\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
\]

Therefore the exact infinite-volume paired target can be written
\[
\boxed{
\mathcal T_{\rm pair}(z)
=
\frac{C_\xi}{E(z)}
\int_{\mathbb R}\Phi(r)e^{-izr}\,dr.
}
\]

This is the cleanest current synthesis so far:

\[
\boxed{
E(z)\mathcal T_{\rm pair}(z)
=
C_\xi\,\widehat{\Phi}(z)
}
\]
with the bilateral/Fourier convention inherited from \(w=-iz\).

So after multiplication by the de Branges factor \(E(z)\), the **paired Suzuki deficiency transfer is exactly the theta/Xi transform** in the infinite-volume model.

This is an exact identity from combining two already-established formulas; it is not an RH statement and does not identify a self-adjoint spectrum with the zeros.

## Gate 10. What remains open [O]

The missing finite-to-edge theorem is now sharply isolated:

1. construct the limiting edge form/domain from \(H(S_A)\);
2. prove the compensated source convergence in that topology;
3. prove the two edge deficiency transforms converge to Suzuki's Section-7 \(f_{\pm i}\);
4. show
   \[
   \mathcal T_{{\rm pair},A}\to\mathcal T_{\rm pair};
   \]
5. consequently verify
   \[
   \frac{E(z)\mathcal T_{{\rm pair},A}(z)}{\Xi(-iz)}
   \to C_\xi.
   \]

No raw scalar Wiener--Hopf factorization of the explicit-formula distribution is needed for this target.

## Result

\[
\boxed{\textbf{PASS: screw current analytically regularizes to }\Xi'/\Xi.}
\]

\[
\boxed{\textbf{PASS: integration + normalization reconstructs }\Xi.}
\]

\[
\boxed{\textbf{PASS: Suzuki's infinite-volume paired transfer fits the theta/Xi structure exactly after }E\textbf{-normalization}.}
\]

Specifically,
\[
\boxed{
E(z)\mathcal T_{\rm pair}(z)
=
C_\xi\,\Xi(-iz)
=
C_\xi\int_{\mathbb R}\Phi(r)e^{-izr}\,dr.
}
\]

\[
\boxed{\textbf{OPEN: prove the Section-8 finite/edge paired channel converges to this Section-7 target.}}
\]

This replaces the failed single-channel scalar identification by a precise, source-faithful paired-channel Xi identification.
