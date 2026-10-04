# Cone Derivation Ledger v13.995 — Sandbox: Infinite-Dimensional Relative Determinant Framework for the Pre-Elimination Projective Border Ratio

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), parallel analytic task
**Status:** [D] determinant-category lineage audit; [D] relative rank-one Fredholm determinant identity for the border ratio; [D] finite-section theorem with pre-limit complement cancellation; [I] exact-D invertibility and bordered invertibility as the remaining hard hypotheses; [O] scalar-separation fallback and resolvent-winding alternative.
**Parents:** v13.661, v13.708–709, v13.991, v13.993–994
**Authorization:** Jeremy, 2026-10-04 ("yes ledger it")
**Collision check:** Live HEAD immediately before this write was v13.994
(Rank-One Source-Capacity, Lane A); no v13.995 entry was present.

---

## 0. Purpose

v13.993 proves, for finite sections, that the Xi-scalar projective ratio

\[
\frac{F(i)}{F(-i)}
=
\frac{\det\mathfrak B_{\rm full}(p_{+i})}
     {\det\mathfrak B_{\rm full}(p_{-i})}
\]

is exact, with the complement determinant cancelling algebraically.
v13.993 §11 flags the guardrail: the identities are finite-dimensional;
the infinite-dimensional promotion needs a relative/Fredholm
determinant or a finite-section tail theorem.

This entry supplies that framework without rebuilding the v13.982/v13.988
KKT inverse payload, per the tasking. No 6×6 inverse appears.

---

## 1. Determinant-category lineage [D]

Source-faithfully available:

* **v13.661 — Relative rank-one Krein determinant.**
  \(\Delta^{\rm bdry}_{A,\theta/\pi}(z;z_*)
  =(\tau_\theta-m_A(z))/(\tau_\theta-m_A(z_*))\).
  A *ratio*; well-defined for rank-one boundary perturbations as an
  ordinary 1×1 determinant. The operative category for what follows.

* **v13.709 — Regularized Fredholm \(\det_2\).**
  \(D_A(z)=\det_2(I-zS_A)\) with \(S_A\in\mathfrak S_2\) (Hilbert–Schmidt)
  from the continuous kernel. Canonical. *Not* ordinary det:
  trace class (\(\mathfrak S_1\)) is unproven, so \(\det(I-zS_A)\) must
  not be asserted.

* **Ordinary finite-dimensional det.** Used in v13.991/993 for sections
  and reduced blocks.

Not available (v13.708, negative): no same-domain bulk determinant vs
the local Dirichlet Laplacian. Do not use.

## 2. The two pre-elimination borders [D]

With \(\mathcal A=\bigl(\begin{smallmatrix}A_R&E^*\\E&D\end{smallmatrix}\bigr)\),
\(b=\binom{b_R}{b_Q}\), \(p_j^*=(p_{R,j}^*,p_{Q,j}^*)\), \(j\in\{+i,-i\}\):

\[
\mathfrak B_{\rm full}(p_j)
=
\begin{pmatrix}
A_R & b_R & E^*\\
-p_{R,j}^* & 0 & -p_{Q,j}^*\\
E & b_Q & D
\end{pmatrix}.
\]

The two borders differ *only* in the middle row. Hence

\[
\boxed{
\mathfrak B_{\rm full}(p_{+i})-\mathfrak B_{\rm full}(p_{-i})
\text{ is rank-one, hence trace-class.}
}
\]

## 3. Relative determinant identity [D]

Assume (H1) \(D\) invertible with bounded inverse (exact);
(H2) \(E,E^*\) bounded; (H3) \(b,p_j\) in the correct form domains so
\(F_j=p_j^*\mathcal A^{-1}b\) exist; (H4) \(\mathfrak B_{\rm full}(p_{-i})\)
invertible with bounded inverse. Then

\[
\boxed{
\frac{F(i)}{F(-i)}
=
\det\nolimits_{\rm Fredholm}
\!\Bigl(I+\mathfrak B_{-}^{-1}
(\mathfrak B_{+}-\mathfrak B_{-})\Bigr),
}
\]

a Fredholm determinant of a rank-one (hence \(\mathfrak S_1\))
perturbation. No individual \(\det\mathfrak B_\pm\), no \(\det D\),
no \(\det\mathcal A\) is ever formed. Moreover this equals
\(\det\mathfrak B_{\rm red}(p_{+i})/\det\mathfrak B_{\rm red}(p_{-i})\)
with \(\mathfrak B_{\rm red}\) the *finite-dimensional* Schur-reduced
borders — the complement factor cancels algebraically.

This places the ratio in the v13.661 relative rank-one category, not
the unavailable bulk category.

## 4. Finite-section theorem with pre-limit cancellation [D]

If (H4) is unavailable, let \(\mathfrak B_{N,\pm}\) be N-mode sections.
Exactly at finite N,

\[
\boxed{
R_N
:=
\frac{\det\mathfrak B_{N,+}}{\det\mathfrak B_{N,-}}
=
\frac{\det\mathfrak B_{{\rm red},N}(p_{+})}
     {\det\mathfrak B_{{\rm red},N}(p_{-})},
}
\]

with \(\det D_N\) cancelled *before* \(N\to\infty\) — no lower bound on
any complement determinant is ever needed. With tails
\(\tau_N\to0\) for \(D_N^{-1},E_N,b_{Q,N},p_{Q,N}\),

\[
|R_N-F(i)/F(-i)|
\le
C\,\tau_N/{\rm dist},
\qquad
{\rm dist}=|\det\mathfrak B_{\rm red}(p_{-i})|>0,
\]

a *scalar* separation, strictly weaker than any bordered
\(\sigma_{\min}\) gate (v13.991/v13.993 diagnostics).

## 5. Tail strength [I]

The ratio needs \(D^{-1}\) only on the *fixed* vectors (columns of
\(E\), \(b_Q\)) and functionals (rows \(p_Q^*\)), not a uniform
carrier-residual bound as in v13.989–992. The difference
\(p_{Q,+}^*-p_{Q,-}^*\) may enjoy faster remote decay than either term
alone (the leading \(1/n\) moment is \(\theta\)-dependent and partially
cancels). Verifying this from the explicit \(p^{(\pm i)}\) asymptotics
is a concrete next computation.

## 6. Obstructions [D]

* **(H4) failure:** if \(\mathfrak B_{\rm full}(p_{-i})\) is not
  invertibly bounded, the direct Fredholm relative determinant does not
  exist; fall back to §4 (finite-section scalar separation).
* **(H1) for exact \(D\):** v13.979 certifies the *numerical*
  complement (\(\|\widehat D^{-1}\|<10.2\)); exact-\(D\) invertibility
  needs \(\|D-\widehat D\|<1/10.2\) in the gap metric — open.
* **Weaker fallback:** track \(\det\mathfrak B_{{\rm red},N}(p(z))\) by
  argument principle along a contour (topological nonvanishing, no
  quantitative lower bound).

---

*Strictly projective/relative throughout. The v13.987-closed absolute
\(6\times6\) inverse route is not revived.*
