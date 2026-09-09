# Cone Derivation Ledger v13.370 — Carrier-Content 2x2 Triangular Defect Decomposition

**Date:** 2026-09-09

## Purpose
Synthesize the carrier split of v13.316--v13.319 with the remainder/curvature content split of v13.363 and the joint-zero geometry of v13.369.

## Two axes
For a quotient block \(B_q=[L_q,R_q]\),
\[
\Delta_k=s_q+q(R_q-k),
\qquad
s_q=n-qR_q.
\]

Carrier axis:
- boundary/terminal \(k=R_q\);
- interior \(k<R_q\).

Content axis:
- terminal remainder \(s_q\);
- curvature transport \(q(R_q-k)\).

## Exact first-moment 2x2 channels
For
\[
E_q=\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k},
\]
define
\[
\boxed{E_{BR,q}=\frac{s_q}{R_q}},
\]
\[
\boxed{E_{BC,q}=0},
\]
\[
\boxed{E_{IR,q}=s_q(H_{R_q-1}-H_{L_q-1})},
\]
\[
\boxed{
E_{IC,q}=q\sum_{k=L_q}^{R_q-1}\frac{R_q-k}{k}
=qR_q(H_{R_q-1}-H_{L_q-1})-q(m_q-1).
}
\]
Then
\[
\boxed{E_q=E_{BR,q}+E_{BC,q}+E_{IR,q}+E_{IC,q}}.
\]

## Triangular matrix
\[
\boxed{
\begin{array}{c|cc}
&\text{remainder}&\text{curvature}\\ \hline
\text{boundary}&E_{BR,q}&0\\
\text{interior}&E_{IR,q}&E_{IC,q}
\end{array}}
\]
The upper-right channel vanishes identically because transport distance is zero at the terminal endpoint.

## Recovery of previous decompositions
Carrier totals:
\[
E_{B,q}=E_{BR,q},
\qquad
E_{I,q}=E_{IR,q}+E_{IC,q}.
\]

Content totals:
\[
E_{R,q}=E_{BR,q}+E_{IR,q}=s_q(H_{R_q}-H_{L_q-1}),
\]
\[
E_{C,q}=E_{IC,q}=q\sum_{k=L_q}^{R_q}\frac{R_q-k}{k}.
\]
Thus the 2x2 table simultaneously reproduces the prior carrier and content splits.

## Integer moments
For integer \(m\ge1\), boundary remains pure remainder:
\[
\boxed{B_{m,q}=(s_q/R_q)^m.}
\]
Interior expands as
\[
\boxed{
I_{m,q}
=\sum_{r=0}^{m}{m\choose r}s_q^{m-r}q^r
\sum_{k=L_q}^{R_q-1}\frac{(R_q-k)^r}{k^m}.
}
\]
Here \(r=0\) is interior pure remainder, \(1\le r\le m-1\) are mixed remainder-curvature channels, and \(r=m\) is pure curvature.

Therefore all nonzero curvature powers are confined to the interior carrier.

## Quotient-block strata
- Contact endpoint: \(s_q=0\), transport \(=0\); all boundary channels vanish.
- Stable off-shell endpoint: \(s_q>0\), transport \(=0\); only boundary×remainder survives.
- Strict descent/interior: transport \(>0\); curvature channels become available.

## Global first moment
\[
\boxed{
E(n)=nH_n-D(n)=E_{BR}(n)+E_{IR}(n)+E_{IC}(n)
}
\]
with \(E_{BC}(n)=0\).

## Quarter-mode localization
Since
\[
q(R_q-k)=4\sum M_F^2
\]
over the endpoint strip, the curvature column is exactly accumulated local quarter-mode content. Its boundary entry vanishes because the strip collapses at \(k=R_q\).

## Guardrails
1. Carrier and content axes are distinct.
2. Zero boundary-curvature is terminality, not divisibility.
3. Stable off-shell terminals may carry positive boundary remainder.
4. Finite binomial channel expansions are asserted for integer moments only.
5. No new primality, asymptotic, or spectral theorem is claimed.

## Companion note
`research-notes/Carrier_Content_2x2_Triangular_Defect_Decomposition.md`
