# Cone Derivation Ledger v13.756 — Finite-to-Infinite HB Determinant Convergence Gate

**Date:** 2026-09-24
**Status:** exact convergence criterion for the HB boundary determinant; operator convergence implications separated from the still-open Suzuki finite-edge asymptotics
**Parents:** v13.742–745, v13.753–755
**Synchronization:** live head before write was v13.755 (External Audit Round 91, \`d96413fa...\`). The audit independently passed v13.752–754's self-contained algebra and specifically named this finite-to-infinite gate as next. No collision was present.

## 1. Imported, now-audited architecture

Do not rederive:

1. v13.753: the derivative map is an exact screw–Weil form isometry; under positivity/completion it is unitary after null-space quotient.
2. v13.754: the derivative transport preserves the boundary Weyl function, and
\[
E(z)=i c_\infty\,\Xi(z)\,[m_\infty(z)-\tau_{\rm HB}],
\qquad
\tau_{\rm HB}=i/c_\infty.
\]
3. Hence the normalized infinite determinant is
\[
\Delta_{\infty}(z;z_*)
:=
\Delta_{{\rm HB}/\pi}(z;z_*)
=
\frac{\tau_{\rm HB}-m_\infty(z)}
{\tau_{\rm HB}-m_\infty(z_*)}
=
\frac{E(z)/\Xi(z)}{E(z_*)/\Xi(z_*)}.
\]
4. v13.742–745 corrected the finite deficiency equation. Therefore no finite paired-transfer identity from the retracted v13.740 is imported here.

## 2. Define the finite HB determinant without assuming edge convergence

For every finite \(A\), use the transported finite Weyl function \(m_A(z)\) and the **fixed infinite target boundary parameter**
\[
\boxed{\tau_{\rm HB}=i/c_\infty.}
\]
Choose a normalization point \(z_*\) in the common resolvent domain with
\[
\tau_{\rm HB}-m_\infty(z_*)\ne0.
\]
Define
\[
\boxed{
\Delta_A(z;z_*)
=
\frac{\tau_{\rm HB}-m_A(z)}
{\tau_{\rm HB}-m_A(z_*)}.
}
\]
This definition is boundary-triple intrinsic and does not require an unproved formula for the corrected finite deficiency pair.

## 3. Minimal scalar convergence theorem

Let \(K\) be a compact subset of a domain \(\Omega\) on which \(m_A,m_\infty\) are holomorphic. Assume
\[
\boxed{m_A\to m_\infty\quad\text{locally uniformly on }\Omega.}
\]
Then at the fixed \(z_*\),
\[
\tau_{\rm HB}-m_A(z_*)\to
\tau_{\rm HB}-m_\infty(z_*)\ne0.
\]
Hence for all sufficiently large \(A\), the finite denominator is nonzero and
\[
\boxed{
\Delta_A(\,\cdot\,;z_*)\to
\Delta_\infty(\,\cdot\,;z_*)
\quad\text{locally uniformly on }\Omega.
}
\]

Indeed, writing \(d_A=\tau_{\rm HB}-m_A(z_*)\), \(d_\infty=\tau_{\rm HB}-m_\infty(z_*)\),
\[
\Delta_A-\Delta_\infty
=
\frac{m_\infty-m_A}{d_A}
+
(\tau_{\rm HB}-m_\infty)
\left(\frac1{d_A}-\frac1{d_\infty}\right),
\]
and both terms tend uniformly to zero on compacta.

Thus **local uniform convergence of the scalar Weyl functions is sufficient for local uniform convergence of the normalized HB determinants.**

## 4. Logarithmic derivatives

On a compact \(K\Subset\Omega\) avoiding zeros of \(\tau_{\rm HB}-m_\infty\), local uniform holomorphic convergence implies derivative convergence by Cauchy's formula:
\[
m_A'\to m_\infty'
\]
locally uniformly. Therefore
\[
\boxed{
\partial_z\log\Delta_A(z;z_*)
=
-\frac{m_A'(z)}{\tau_{\rm HB}-m_A(z)}
\longrightarrow
-\frac{m_\infty'(z)}{\tau_{\rm HB}-m_\infty(z)}
=
\partial_z\log\Delta_\infty(z;z_*).
}
\]
Using v13.754,
\[
\boxed{
\partial_z\log\Delta_\infty
=
-\frac{T_{\rm pair}'}{T_{\rm pair}}.
}
\]
So the finite determinant logarithmic derivative converges to the paired infinite deficiency logarithmic derivative wherever the limiting denominator is nonzero.

This is a derivative/trace convergence target that avoids any normalization constant in \(T_{\rm pair}\).

## 5. Zero/pole stability

If \(m_A\to m_\infty\) locally uniformly and \(z_0\) is an isolated zero of
\[
\tau_{\rm HB}-m_\infty(z),
\]
then Hurwitz/Rouché theory implies that the zeros of
\[
\tau_{\rm HB}-m_A(z)
\]
inside a sufficiently small contour around \(z_0\) have the same total multiplicity for all sufficiently large \(A\).

Thus the finite HB boundary characteristic has locally stable divisor data under this convergence hypothesis.

This does **not** imply that all zeros lie on a real axis: \(\tau_{\rm HB}\) is complex and the HB extension is not self-adjoint.

## 6. Krein resolvent convergence: what extra input is required

The scalar determinant convergence needs only \(m_A\to m_\infty\). Operator resolvent convergence needs more.

After identifying the finite and infinite spaces through the derivative/helix transport, the rank-one Krein formula has schematic exact form
\[
R_{{\rm HB},A}(z)-R_{\pi,A}(z)
=
\gamma_A(z)
[\tau_{\rm HB}-m_A(z)]^{-1}
\gamma_A(\bar z)^*,
\]
and similarly at infinity.

A sufficient set of hypotheses for strong resolvent convergence on a common ambient realization is:

\[
\boxed{
R_{\pi,A}(z)\to R_{\pi,\infty}(z)\ \text{strongly},
}
\]
\[
\boxed{
\gamma_A(z)\to\gamma_\infty(z)\ \text{strongly},
\qquad
\gamma_A(\bar z)^*\to\gamma_\infty(\bar z)^*\ \text{strongly},
}
\]
together with
\[
\boxed{m_A(z)\to m_\infty(z)}
\]
and a uniform lower bound
\[
|\tau_{\rm HB}-m_A(z)|\ge c_K>0
\]
on compact subsets away from the limiting HB spectrum.

Under these hypotheses the rank-one correction converges strongly, hence
\[
\boxed{
R_{{\rm HB},A}(z)\to R_{{\rm HB},\infty}(z)
\quad\text{strongly}.
}
\]

If the reference resolvents and gamma fields converge in operator norm (with the corresponding adjoints), the same argument upgrades to norm-resolvent convergence.

## 7. Trace/determinant convergence

Because the boundary correction is rank one,
\[
\operatorname{Tr}\,[R_{{\rm HB},A}(z)-R_{\pi,A}(z)]
=
-\partial_z\log\Delta_A(z;z_*).
\]
Therefore the scalar local-uniform Weyl convergence already implies convergence of these **relative rank-one traces**:
\[
\boxed{
\operatorname{Tr}[R_{{\rm HB},A}-R_{\pi,A}]
\to
\operatorname{Tr}[R_{{\rm HB},\infty}-R_{\pi,\infty}]
=
\frac{T_{\rm pair}'}{T_{\rm pair}}.
}
\]
No convergence of the absolute resolvent traces is asserted.

## 8. Relation to the corrected finite Suzuki equation

The corrected v13.742–745 finite deficiency lane now has a precise target:

it does **not** need first to prove a finite identity of the form
\[
T_{{\rm pair},A}=C_A\,\Xi/E_A.
\]
It is enough to extract the finite Weyl data from Suzuki's correct equation (8.5) and prove
\[
\boxed{m_A\to m_\infty\ \text{locally uniformly}.}
\]

Once that is achieved, the HB determinant convergence follows automatically:
\[
\boxed{
\Delta_A
\to
\Delta_\infty
=
\frac{E/\Xi}{(E/\Xi)(z_*)}.
}
\]

Equivalently, after inversion,
\[
\boxed{
\Delta_A^{-1}
\to
\text{constant}\times\frac{\Xi}{E}
=
\text{constant}\times T_{\rm pair}.
}
\]

This gives a normalization-safe finite-to-infinite target for the Suzuki edge lane.

## 9. New helix relevance

The helix lane changes the interpretation but not the convergence theorem.

v13.753–754 show that the basepointed rapidity helix
\[
\Psi_u(t)=e^{itu}-1
\]
passes through the derivative unitary to the Weil carrier and transports the boundary triple without changing \(m_A\). Therefore the scalar convergence problem
\[
m_A\to m_\infty
\]
is invariant under the helix/screw–Weil transport.

So the new cone-helix structure supplies an exact common carrier:
\[
\boxed{
\text{basepointed rapidity helix}
\to
\text{screw space}
\overset{\bar D}{\simeq}
\text{Weil space}
\to
m_A
\to
\Delta_A,
}
\]
rather than introducing a second independent convergence problem.

## 10. Exact status

**PROVED here:** local-uniform \(m_A\to m_\infty\) implies local-uniform \(\Delta_A\to\Delta_\infty\), convergence of logarithmic derivatives away from the limiting divisor, and local stability of divisor multiplicities.

**PROVED here:** with convergent reference resolvents and gamma fields, Krein's rank-one formula promotes the scalar convergence to strong/norm resolvent convergence according to the topology of those inputs.

**OPEN:** prove \(m_A\to m_\infty\) from Suzuki's corrected finite equation (8.5).

**OPEN:** prove convergence of the transported gamma fields/reference resolvents in the required topology.

**OPEN:** identify the corrected finite paired deficiency expression directly with \(\Delta_A^{-1}\); this is not assumed.

**GUARDRAIL:** none of these convergence statements proves RH or self-adjointness of the complex HB extension.

## 11. Next nonredundant gate

Use the closed scalar moment system of v13.745 to express \(m_A(z)\) in terms of the corrected finite deficiency data, and isolate the smallest asymptotic estimates on those scalar moments that force locally uniform convergence to the audited infinite Weyl function
\[
m_\infty(z)
=
-i\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}.
\]
This reduces the remaining finite-to-infinite problem to explicit scalar asymptotics rather than operator-level guesswork.
