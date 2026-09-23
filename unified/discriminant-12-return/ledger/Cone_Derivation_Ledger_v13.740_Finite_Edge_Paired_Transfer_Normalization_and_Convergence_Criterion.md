# Cone Derivation Ledger v13.740 — Finite-Edge Paired Transfer Normalization and Convergence Criterion

Date: 2026-09-23

Status: nonredundant continuation of the Suzuki edge lane after the Round-87 renumbering/provenance cleanup. This entry imports the established v13.739 registry rather than rederiving the screw/Xi bridge.

Synchronization: live head before write was v13.739, commit \`54f8b5addf58852fdedf9c22b54208f62b243699\`. External Audit Round 87 renumbered the relevant source entries and independently verified the Section-7 paired identity and the screw-current decomposition. Canonical references below use the post-audit numbering.

## 1. Imported established facts [S/C/X]

From v13.739:

\[
T_{\rm pair}(z)
=
C_\xi\frac{\Xi(-iz)}{E(z)}
=
\frac{C_\xi}{1+L(s)},
\qquad
s=\frac12-iz,
\]
where
\[
L(s)=\frac{\xi'(s)}{\xi(s)},
\qquad
E(z)=\xi(s)+\xi'(s)=\xi(s)[1+L(s)],
\]
and
\[
C_\xi=\frac{2\xi'(3/2)}{\pi^2 i}.
\]

Also
\[
E(z)T_{\rm pair}(z)
=
C_\xi\Xi(-iz)
=
C_\xi\widehat\Phi(z).
\]

These are ESTABLISHED and are not rederived here.

## 2. Finite Section-8 characteristic channels [S]

For the finite interval, use the established continuous-kernel defect pair
\[
S_Au_z=\bar D e_z,
\qquad
S_Au_\pm=\bar D e_{\pm i}
\]
up to the fixed deficiency normalizations.

Define
\[
F_{A,\pm}(z)
=
\overline{
\left\langle
\bar D e_{\bar z},
S_A^{-1}\bar D e_{\pm i}
\right\rangle
}.
\]

The finite characteristic decomposes into the two channels
\[
A_A(z):=(z-i)F_{A,+}(z),
\qquad
B_A(z):=(z+i)F_{A,-}(z).
\]

The boundary-triple/Weyl ratio is
\[
m_A(z)
=
-i\frac{A_A(z)+B_A(z)}
{A_A(z)-B_A(z)}.
\]

Therefore the finite paired-difference channel is canonically
\[
\boxed{
P_A(z):=A_A(z)-B_A(z)
=
(z-i)F_{A,+}(z)-(z+i)F_{A,-}(z).
}
\]

This is the finite Section-8 object with the same algebraic \(+\)/\(-\) pairing as Suzuki's Section-7 identity.

## 3. The finite paired channel is the Weyl denominator [X]

The previous formula gives
\[
A_A+B_A=i\,m_A\,P_A.
\]

Hence
\[
\boxed{
A_A=\frac{1+i m_A}{2}P_A,
\qquad
B_A=\frac{i m_A-1}{2}P_A.
}
\]

Thus the finite deficiency data split exactly into

1. a common amplitude \(P_A\);
2. the Weyl ratio \(m_A\).

This is useful because the boundary characteristic alone determines only projective channel data. The Xi comparison requires the missing common amplitude \(P_A\), not merely \(m_A\).

## 4. Boundary-layer scaling required by the deficiency sources [S/X]

The established finite-\(A\) raw exponential analysis showed that the \(+i\) source is concentrated at the right edge with scale \(e^A\), while the \(-i\) source is concentrated at the left edge with the same scale.

The source-faithful transported profiles are compensated:
\[
e^{-A}\mathcal E_A(\bar D e_{+i})
\rightsquigarrow
i(e^{-\xi}-\delta_0),
\]
and by reflection
\[
e^{-A}\mathcal E_A^L(\bar D e_{-i})
\rightsquigarrow
-i(e^{-\xi}-\delta_0),
\]
at the established distributional level.

Therefore each finite deficiency channel carries one \(e^A\)-scale source normalization. The paired scalar \(P_A\), being a pairing of a general defect source with a deficiency source, must be normalized using the same edge scaling before any Section-7 comparison.

For fixed \(z\), define the edge-normalized channel
\[
\boxed{
\widetilde P_A(z)
:=
N_A(z)P_A(z),
}
\]
where \(N_A(z)\) is chosen from the already-established finite-\(A\) exponential boundary factor so that the right/left edge sources have finite nonzero limits.

The exact \(N_A(z)\) is convention-sensitive because \(F_{A,\pm}\) contains \(\bar D\), not the raw exponentials. It is therefore **not** promoted here as \(e^{-A}e^{\mp izA}\) until the limiting \(H(S_{\rm edge})\) source theorem is proved.

This prevents reintroducing the v13.724 transport error.

## 5. A normalization-free finite convergence invariant [X]

Although the absolute amplitude normalization is still open, ratios at two spectral points cancel any \(z\)-independent deficiency-source normalization.

Choose a reference point \(z_*\) with
\[
P_A(z_*),\quad
T_{\rm pair}(z_*)\ne0.
\]

Define
\[
\boxed{
\mathscr R_A(z;z_*)
:=
\frac{P_A(z)}{P_A(z_*)}
\frac{T_{\rm pair}(z_*)}{T_{\rm pair}(z)}.
}
\]

Using the established infinite target,
\[
\frac{T_{\rm pair}(z_*)}{T_{\rm pair}(z)}
=
\frac{\Xi(-iz_*)E(z)}
{\Xi(-iz)E(z_*)}.
\]

Hence
\[
\boxed{
\mathscr R_A(z;z_*)
=
\frac{P_A(z)}{P_A(z_*)}
\frac{\Xi(-iz_*)E(z)}
{\Xi(-iz)E(z_*)}.
}
\]

If the finite Section-8 paired channel converges to the Section-7 channel up to a single \(A\)-dependent scalar \(c_A\),
\[
P_A(z)=c_A T_{\rm pair}(z)(1+o(1))
\]
locally uniformly, then necessarily
\[
\boxed{
\mathscr R_A(z;z_*)\to1.
}
\]

Conversely, local-uniform convergence
\[
\mathscr R_A(z;z_*)\to1
\]
on a connected zero-free domain implies that \(P_A\) approaches the Section-7 target projectively; the remaining ambiguity is exactly one scalar \(c_A=P_A(z_*)/T_{\rm pair}(z_*)\).

Thus this ratio test separates the **shape problem** from the **absolute normalization problem**.

## 6. Log-derivative form removes the scalar normalization completely [X]

Define
\[
\boxed{
\Delta_A(z)
:=
\frac{P_A'(z)}{P_A(z)}
-
\frac{T_{\rm pair}'(z)}{T_{\rm pair}(z)}.
}
\]

From v13.739,
\[
\frac{T_{\rm pair}'}{T_{\rm pair}}
=
i\frac{L'(s)}{1+L(s)},
\qquad
s=\frac12-iz.
\]

Therefore
\[
\boxed{
\Delta_A(z)
=
\frac{P_A'(z)}{P_A(z)}
-
i\frac{L'(1/2-iz)}
{1+L(1/2-iz)}.
}
\]

This is a particularly sharp finite-edge test:
\[
\boxed{
\Delta_A(z)\to0
}
\]
locally uniformly away from divisors is necessary for projective finite-edge convergence, and integrating \(\Delta_A\) along paths gives the ratio invariant:
\[
\log\mathscr R_A(z;z_*)
=
\int_{z_*}^{z}\Delta_A(\zeta)d\zeta.
\]

So no absolute source normalization is needed to test the spectral shape.

## 7. Equivalent theta-kernel test [X]

Because
\[
E(z)T_{\rm pair}(z)=C_\xi\widehat\Phi(z),
\]
the same ratio invariant can be written
\[
\boxed{
\mathscr R_A(z;z_*)
=
\frac{E(z)P_A(z)}
{E(z_*)P_A(z_*)}
\frac{\widehat\Phi(z_*)}{\widehat\Phi(z)}.
}
\]

Thus finite Section-8 data can be compared directly against the theta/Casimir kernel without first reconstructing \(\xi'/\xi\).

The logarithmic derivative target is
\[
\boxed{
\frac{d}{dz}\log[E(z)P_A(z)]
\stackrel{A\to\infty}{\longrightarrow}
\frac{d}{dz}\log\widehat\Phi(z)
=
-iL(1/2-iz).
}
\]

Using
\[
\frac{E'}E
=
-iL-i\frac{L'}{1+L},
\]
this is algebraically equivalent to the \(\Delta_A\to0\) criterion.

## 8. Divisor test [X]

Projective convergence also predicts the limiting zero/pole pattern.

Since
\[
T_{\rm pair}(z)=\frac{C_\xi}{1+L(s)}
=
C_\xi\frac{\xi(s)}{\xi(s)+\xi'(s)},
\]
the finite paired channel should, after projective convergence, inherit zeros from \(\xi(s)\) with the divisor allocation already recorded in v13.739.

At a simple zero of \(\xi(s)\),
\[
E(z)=\xi'(s)\ne0,
\]
so
\[
T_{\rm pair}(z)=0
\]
simply.

Therefore a necessary local convergence signature is:
\[
\boxed{
\text{zeros of }P_A
\text{ should approach the simple Xi zeros of the target channel,}
}
\]
subject to the usual caveat that this statement concerns convergence of analytic functions and is not a Hilbert--Pólya or RH assertion.

Off the critical line, the corresponding \(z\) is complex; no real-spectrum claim is implied.

## 9. What finite Section-8 data are actually needed [O]

The next computational/analytic gate is now smaller than a full edge resolvent construction.

It suffices to obtain \(P_A(z)\), or its logarithmic derivative, from the finite continuous-kernel problem:
\[
P_A(z)
=
(z-i)
\overline{\langle\bar D e_{\bar z},S_A^{-1}\bar D e_{+i}\rangle}
-
(z+i)
\overline{\langle\bar D e_{\bar z},S_A^{-1}\bar D e_{-i}\rangle}.
\]

Then evaluate either

\[
\boxed{
\mathscr R_A(z;z_*)
}
\]
or
\[
\boxed{
\Delta_A(z).
}
\]

This avoids the unresolved absolute edge-source normalization entirely.

## 10. Relation to the Weyl function and a limitation [X]

Because
\[
m_A=-i\frac{A_A+B_A}{P_A},
\]
knowledge of \(m_A\) alone does **not** determine \(P_A\): multiplying both \(A_A\) and \(B_A\) by the same nonzero analytic factor leaves \(m_A\) unchanged.

Therefore the already-established Weyl convergence, if available, would not by itself prove the Xi amplitude identification.

This is precisely why the finite paired amplitude \(P_A\) is the correct remaining object.

The determinant/boundary characteristic may fix this amplitude only after a normalization at one spectral point.

## Result

\[
\boxed{\textbf{PASS: exact finite paired channel isolated}}
\]
\[
\boxed{
P_A(z)=(z-i)F_{A,+}(z)-(z+i)F_{A,-}(z).
}
\]

\[
\boxed{\textbf{PASS: normalization-free Xi/theta convergence criterion}}
\]
\[
\boxed{
\mathscr R_A(z;z_*)
=
\frac{P_A(z)}{P_A(z_*)}
\frac{\Xi(-iz_*)E(z)}
{\Xi(-iz)E(z_*)}
\to1.
}
\]

Equivalent local criterion:
\[
\boxed{
\Delta_A(z)
=
\frac{P_A'}{P_A}
-
i\frac{L'(1/2-iz)}{1+L(1/2-iz)}
\to0.
}
\]

Equivalent theta criterion:
\[
\boxed{
\frac{d}{dz}\log[E(z)P_A(z)]
\to
\frac{d}{dz}\log\widehat\Phi(z).
}
\]

\[
\boxed{\textbf{OPEN: compute/estimate }P_A(z)\textbf{ from the finite Section-8 continuous-kernel problem and test these criteria.}}
\]

This is the next nonredundant finite-edge gate under the v13.739 provenance registry.
