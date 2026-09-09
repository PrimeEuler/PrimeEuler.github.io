# Carrier-Content 2x2 Triangular Defect Decomposition

## Status
Exact synthesis of the carrier decomposition from v13.316--v13.319 with the remainder/curvature content decomposition from v13.363 and the joint-zero geometry of v13.369.

## 1. Two independent axes
For a quotient block
\[
B_q=[L_q,R_q],
\qquad
s_q=n-qR_q,
\]
write
\[
\Delta_k=s_q+q(R_q-k).
\]
There are two conceptually distinct decompositions.

### Carrier axis
Where the contribution sits:
- boundary/terminal carrier: \(k=R_q\);
- interior/strict-descent carriers: \(L_q\le k<R_q\).

### Content axis
What the defect contains:
- terminal remainder content: \(s_q\);
- curvature/transport content: \(q(R_q-k)\).

These axes are transverse.

## 2. First-moment 2x2 decomposition
The block first moment is
\[
E_q=\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k}.
\]
Split first by carrier and then by content.

### Boundary × remainder
At \(k=R_q\),
\[
\boxed{E_{BR,q}=\frac{s_q}{R_q}}.
\]

### Boundary × curvature
Because \(R_q-k=0\) at the terminal endpoint,
\[
\boxed{E_{BC,q}=0}.
\]

### Interior × remainder
\[
\boxed{
E_{IR,q}=s_q\sum_{k=L_q}^{R_q-1}\frac1k
=s_q\left(H_{R_q-1}-H_{L_q-1}\right).
}
\]

### Interior × curvature
\[
\boxed{
E_{IC,q}=q\sum_{k=L_q}^{R_q-1}\frac{R_q-k}{k}.
}
\]
Since
\[
\sum_{k=L_q}^{R_q-1}\frac{R_q-k}{k}
=R_q\left(H_{R_q-1}-H_{L_q-1}\right)-(m_q-1),
\]
we have
\[
\boxed{
E_{IC,q}
=qR_q\left(H_{R_q-1}-H_{L_q-1}\right)-q(m_q-1).
}
\]

Therefore
\[
\boxed{
E_q
=E_{BR,q}+E_{BC,q}+E_{IR,q}+E_{IC,q}
}
\]
with
\[
\boxed{E_{BC,q}=0}.
\]

## 3. Triangular channel matrix
It is useful to display the two axes as
\[
\boxed{
\begin{array}{c|cc}
&\text{remainder content}&\text{curvature content}\\ \hline
\text{boundary carrier}&E_{BR,q}&0\\
\text{interior carrier}&E_{IR,q}&E_{IC,q}
\end{array}}
\]
The vanishing upper-right entry is exact, not approximate.

Interpretation: curvature transport has no terminal carrier because transport distance is zero at the endpoint.

## 4. Recovery of earlier formulas
Boundary total:
\[
E_{B,q}=E_{BR,q}=\frac{s_q}{R_q}.
\]
Interior total:
\[
E_{I,q}=E_{IR,q}+E_{IC,q}.
\]
Thus the v13.316 carrier split is recovered.

Content total:
\[
E_{R,q}=E_{BR,q}+E_{IR,q}=s_q(H_{R_q}-H_{L_q-1}),
\]
\[
E_{C,q}=E_{IC,q}=q\sum_{k=L_q}^{R_q}\frac{R_q-k}{k},
\]
where including \(k=R_q\) does not change the curvature sum. Thus the v13.363 content split is recovered.

## 5. Integer moments
For integer \(m\ge1\),
\[
\mathcal S_{m,q}
=\sum_{k=L_q}^{R_q}\left(\frac{s_q+q(R_q-k)}{k}\right)^m.
\]
Boundary:
\[
\boxed{B_{m,q}=\left(\frac{s_q}{R_q}\right)^m.}
\]
This is pure remainder content only.

Interior:
\[
I_{m,q}
=\sum_{k=L_q}^{R_q-1}rac{(s_q+q(R_q-k))^m}{k^m}
\]
expands as
\[
\boxed{
I_{m,q}
=\sum_{r=0}^{m}{m\choose r}s_q^{m-r}q^r
\sum_{k=L_q}^{R_q-1}\frac{(R_q-k)^r}{k^m}.
}
\]
The \(r=0\) term is interior pure-remainder content. Terms \(1\le r\le m-1\) are mixed remainder-curvature channels. The \(r=m\) term is pure curvature content.

Thus all nontrivial curvature powers are confined to the interior carrier.

## 6. Second moment example
For \(m=2\),
\[
B_{2,q}=\frac{s_q^2}{R_q^2},
\]
while
\[
I_{2,q}
=\underbrace{s_q^2\sum_{k=L}^{R-1}\frac1{k^2}}_{\text{interior pure remainder}}
+\underbrace{2s_qq\sum_{k=L}^{R-1}\frac{R-k}{k^2}}_{\text{interior mixed}}
+\underbrace{q^2\sum_{k=L}^{R-1}\frac{(R-k)^2}{k^2}}_{\text{interior pure curvature}}.
\]
There is no boundary mixed or boundary curvature channel.

## 7. Joint-zero interpretation
At a shell-contact endpoint,
\[
s_q=0,
\qquad
R_q-k=0.
\]
Therefore every channel at that boundary vanishes.

For a stable off-shell terminal endpoint,
\[
s_q>0,
\qquad
R_q-k=0,
\]
so only the boundary×remainder channel survives.

For strict-descent interior points, curvature channels are available because \(R_q-k>0\).

This makes the three quotient-block strata visible directly in the triangular carrier-content decomposition.

## 8. Global first moment
Summing over quotient blocks gives
\[
\boxed{
E(n)=nH_n-D(n)
=E_{BR}(n)+E_{IR}(n)+E_{IC}(n),
}
\]
with
\[
E_{BC}(n)=0.
\]
Here
\[
E_{BR}=\sum_q\frac{s_q}{R_q},
\]
\[
E_{IR}=\sum_q s_q(H_{R_q-1}-H_{L_q-1}),
\]
\[
E_{IC}=\sum_q q\sum_{k=L_q}^{R_q-1}\frac{R_q-k}{k}.
\]

## 9. Quarter-mode interpretation
Because
\[
q(R_q-k)=4\sum_{C\subset\mathcal R_{k,q}}M_F^2,
\]
the entire curvature-content column of the decomposition is built from accumulated local quarter modes. The boundary curvature entry vanishes because the endpoint strip collapses to zero width.

Thus the triangular matrix is simultaneously:
- a carrier decomposition,
- a Euclidean remainder/transport decomposition,
- a quarter-mode localization statement.

## 10. Guardrails
- Carrier and content axes must not be conflated.
- The zero boundary-curvature channel is a consequence of zero transport distance, not divisibility.
- Boundary remainder can be positive at stable off-shell endpoints.
- Higher-moment finite binomial channel decompositions are asserted only for integer moments.
- No new prime test, asymptotic, or spectral theorem is claimed.
