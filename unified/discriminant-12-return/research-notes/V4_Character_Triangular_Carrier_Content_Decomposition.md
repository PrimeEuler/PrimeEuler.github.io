# V4 Character Triangular Carrier-Content Decomposition

## Status
Exact continuation of the boundary/interior carrier split, the remainder/curvature content split, and the mod-12 V4 character decomposition.

Let
\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
B_q=[L_q,R_q],
\qquad
s_q=n-qR_q=n\bmod q.
\]
For every \(k\in B_q\),
\[
\Delta_k=n-kq=s_q+q(R_q-k).
\]
Define
\[
C_{k,q}:=q(R_q-k).
\]
Then \(\Delta_k=s_q+C_{k,q}\).

For an arithmetic weight \(\chi(k)\), define the twisted first defect moment
\[
E_\chi(n)=\sum_{k=1}^n\chi(k)\frac{\Delta_k}{k}.
\]

## 1. Exact blockwise triangular decomposition
On one quotient block,
\[
E_{\chi,q}
=\sum_{k=L_q}^{R_q}\chi(k)\frac{s_q+C_{k,q}}{k}.
\]
Separate the terminal endpoint \(k=R_q\) from the interior \(L_q\le k\le R_q-1\).

### Boundary x remainder
\[
\boxed{
E_{BR,\chi,q}
=\chi(R_q)\frac{s_q}{R_q}.
}
\]

### Boundary x curvature
Since \(C_{R_q,q}=0\),
\[
\boxed{E_{BC,\chi,q}=0.}
\]

### Interior x remainder
\[
\boxed{
E_{IR,\chi,q}
=s_q\sum_{k=L_q}^{R_q-1}\frac{\chi(k)}{k}.
}
\]

### Interior x curvature
\[
\boxed{
E_{IC,\chi,q}
=q\sum_{k=L_q}^{R_q-1}\chi(k)\frac{R_q-k}{k}.
}
\]
Therefore
\[
\boxed{
E_{\chi,q}
=E_{BR,\chi,q}+E_{IR,\chi,q}+E_{IC,\chi,q},
\qquad E_{BC,\chi,q}=0.
}
\]
The carrier/content matrix remains triangular after twisting.

## 2. Finite character-sum closure
Define
\[
H_\chi(N)=\sum_{k\le N}\frac{\chi(k)}{k},
\qquad
C_\chi(N)=\sum_{k\le N}\chi(k).
\]
Then
\[
\boxed{
E_{IR,\chi,q}
=s_q\bigl[H_\chi(R_q-1)-H_\chi(L_q-1)\bigr].
}
\]
Also
\[
\sum_{k=L_q}^{R_q-1}\chi(k)\frac{R_q-k}{k}
=R_q\bigl[H_\chi(R_q-1)-H_\chi(L_q-1)\bigr]
-\bigl[C_\chi(R_q-1)-C_\chi(L_q-1)\bigr].
\]
Hence
\[
\boxed{
E_{IC,\chi,q}
=qR_q\Delta H_{\chi,q}^{\rm int}
-q\Delta C_{\chi,q}^{\rm int}.
}
\]
Together with \(s_q+qR_q=n\), this recombines to the earlier twisted block formula
\[
\boxed{
E_{\chi,q}
=n\bigl[H_\chi(R_q)-H_\chi(L_q-1)\bigr]
-q\bigl[C_\chi(R_q)-C_\chi(L_q-1)\bigr].
}
\]
The new content is the exact triangular resolution of that formula.

## 3. Higher integer moments
For \(m\ge1\),
\[
\mathcal S_{m,\chi,q}
=\sum_{k=L_q}^{R_q}\chi(k)\left(\frac{s_q+q(R_q-k)}{k}\right)^m.
\]
The boundary term is pure remainder:
\[
\boxed{
B_{m,\chi,q}
=\chi(R_q)\left(\frac{s_q}{R_q}\right)^m.
}
\]
The interior is
\[
\boxed{
I_{m,\chi,q}
=\sum_{r=0}^m{m\choose r}s_q^{m-r}q^r
\sum_{k=L_q}^{R_q-1}\chi(k)\frac{(R_q-k)^r}{k^m}.
}
\]
Thus all mixed remainder-curvature powers and pure curvature powers live strictly in the interior.

Define twisted interior curvature-distance moments
\[
\mathcal K^{\rm int}_{m,r,\chi,q}
:=q^r\sum_{k=L_q}^{R_q-1}\chi(k)\frac{(R_q-k)^r}{k^m}.
\]
Then
\[
\boxed{
I_{m,\chi,q}
=\sum_{r=0}^m{m\choose r}s_q^{m-r}\mathcal K^{\rm int}_{m,r,\chi,q}.
}
\]

## 4. Generalized twisted harmonic closure
Expanding \((R_q-k)^r\),
\[
\boxed{
\mathcal K^{\rm int}_{m,r,\chi,q}
=q^r\sum_{j=0}^r{r\choose j}R_q^{r-j}(-1)^j
\left[
H_\chi^{(m-j)}(R_q-1)-H_\chi^{(m-j)}(L_q-1)
\right].
}
\]
So the three axes
\[
\boxed{
\text{carrier}\times\text{content}\times\text{character}
}
\]
remain finite and exact for positive integer moments.

## 5. V4 mod-12 channels
For the four real characters modulo 12,
\[
1,\chi_{-4},\chi_{-3},\chi_{12},
\]
character projection is linear and therefore commutes separately with each nonzero carrier/content channel.

For unit residues \(r\in\{1,5,7,11\}\), define residue-resolved channel totals, e.g.
\[
E_{BR,r}(n)
=\sum_{\substack{q\in Q(n)\\R_q\equiv r\ (12)}}\frac{s_q}{R_q},
\]
with analogous definitions for \(IR\) and \(IC\) using the original carrier index \(k\) for interior sums.

Then each channel independently obeys the Hadamard transform
\[
\boxed{
\begin{pmatrix}
E_{*,1}^{\times}\\E_{*,-4}\\E_{*,-3}\\E_{*,12}
\end{pmatrix}
=H_4
\begin{pmatrix}
E_{*,1}\\E_{*,5}\\E_{*,7}\\E_{*,11}
\end{pmatrix},
\qquad *=BR,IR,IC.
}
\]
The inverse is \(\frac14H_4\).

Critical carrier rule: the character always acts on the original staircase column \(k\). For the boundary channel that column is \(R_q\); it is never replaced by the quotient label \(q\).

## 6. Zeroth-support limit
For \(\alpha\to0^+\), the twisted boundary and interior support channels become
\[
\boxed{
B_{0^+,\chi}(n)
=\sum_{\substack{q\in Q(n)\\q\nmid n}}\chi(R_q),
}
\]
which measures signed stable off-shell endpoint support, and
\[
\boxed{
I_{0^+,\chi}(n)
=\sum_q\sum_{k=L_q}^{R_q-1}\chi(k),
}
\]
which measures signed strict-descent support.

Their sum is
\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=\sum_{k\nmid n}\chi(k).
}
\]
For \(\chi=1\), this reduces to
\[
(Q_n-\tau(n))+(n-Q_n)=n-\tau(n).
\]
Thus the earlier support split itself admits V4-residue resolution.

## 7. Structural conclusion
The exact organization is now
\[
\boxed{
\text{carrier axis}:\ \partial\oplus\mathrm{int},
}
\]
\[
\boxed{
\text{content axis}:\ \mathrm{remainder}\oplus\mathrm{curvature},
}
\]
\[
\boxed{
\text{character axis}:\ 1\oplus\chi_{-4}\oplus\chi_{-3}\oplus\chi_{12}.
}
\]
The carrier/content matrix is triangular because the boundary-curvature entry vanishes identically. The character transform commutes with this triangular decomposition by linearity.

## Guardrails
- Character acts on original column \(k\), not quotient label \(q\).
- Principal Dirichlet channel is restricted to units modulo 12; it is not the full untwisted sum.
- Signed character cancellations are not shell contacts; true shell contact remains \(s_q=0\) and \(C_{k,q}=0\).
- Local four-position V4/Walsh labels and global mod-12 Dirichlet characters remain distinct carriers sharing the same abstract V4 algebra.
- No prime criterion beyond the untwisted support statement, and no asymptotic or spectral claim, follows here.
