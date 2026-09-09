# Cone Derivation Ledger v13.371 — V4 Character Triangular Carrier-Content Decomposition

**Date:** 2026-09-09

## Purpose
Combine the exact carrier split (boundary/interior), content split (terminal remainder/curvature transport), and mod-12 V4 character decomposition into one commuting three-axis framework.

## Block setup
For quotient block \(B_q=[L_q,R_q]\), let
\[
s_q=n-qR_q=n\bmod q,
\qquad
C_{k,q}=q(R_q-k).
\]
Then
\[
\boxed{\Delta_k=s_q+C_{k,q}}.
\]
For arithmetic weight \(\chi(k)\),
\[
E_{\chi,q}=\sum_{k=L_q}^{R_q}\chi(k)\frac{\Delta_k}{k}.
\]

## Exact triangular split
\[
\boxed{E_{BR,\chi,q}=\chi(R_q)\frac{s_q}{R_q}}
\]
\[
\boxed{E_{BC,\chi,q}=0}
\]
\[
\boxed{E_{IR,\chi,q}=s_q\sum_{k=L_q}^{R_q-1}\frac{\chi(k)}{k}}
\]
\[
\boxed{E_{IC,\chi,q}=q\sum_{k=L_q}^{R_q-1}\chi(k)\frac{R_q-k}{k}}
\]
and therefore
\[
\boxed{
E_{\chi,q}=E_{BR,\chi,q}+E_{IR,\chi,q}+E_{IC,\chi,q}.
}
\]
The boundary-curvature channel vanishes identically even after twisting.

## Character-sum closure
With
\[
H_\chi(N)=\sum_{k\le N}\chi(k)/k,
\qquad
C_\chi(N)=\sum_{k\le N}\chi(k),
\]
we have
\[
E_{IR,\chi,q}=s_q[H_\chi(R_q-1)-H_\chi(L_q-1)],
\]
\[
E_{IC,\chi,q}=qR_q[H_\chi(R_q-1)-H_\chi(L_q-1)]
-q[C_\chi(R_q-1)-C_\chi(L_q-1)].
\]
Recombining with \(s_q+qR_q=n\) recovers the prior twisted block formula
\[
\boxed{
E_{\chi,q}=n[H_\chi(R_q)-H_\chi(L_q-1)]
-q[C_\chi(R_q)-C_\chi(L_q-1)].
}
\]

## Higher integer moments
For \(m\ge1\), boundary remains pure remainder:
\[
\boxed{
B_{m,\chi,q}=\chi(R_q)(s_q/R_q)^m.
}
\]
Interior decomposes as
\[
\boxed{
I_{m,\chi,q}
=\sum_{r=0}^m{m\choose r}s_q^{m-r}q^r
\sum_{k=L_q}^{R_q-1}\chi(k)\frac{(R_q-k)^r}{k^m}.
}
\]
Thus mixed and pure-curvature powers occur only in the interior.

Define
\[
\mathcal K^{\rm int}_{m,r,\chi,q}
=q^r\sum_{k=L_q}^{R_q-1}\chi(k)\frac{(R_q-k)^r}{k^m}.
\]
Then generalized twisted harmonic closure is
\[
\boxed{
\mathcal K^{\rm int}_{m,r,\chi,q}
=q^r\sum_{j=0}^r{r\choose j}R_q^{r-j}(-1)^j
[H_\chi^{(m-j)}(R_q-1)-H_\chi^{(m-j)}(L_q-1)].
}
\]

## V4 mod-12 transform
For \(1,\chi_{-4},\chi_{-3},\chi_{12}\), each nonzero carrier/content channel transforms independently by the same Hadamard matrix \(H_4\), with inverse \(\frac14H_4\).

Therefore character projection commutes with the triangular carrier/content decomposition.

Critical carrier rule:
\[
\boxed{\chi\text{ acts on original column }k.}
\]
At the terminal boundary this means \(\chi(R_q)\), never \(\chi(q)\).

## Zeroth-support limit
Boundary support:
\[
\boxed{
B_{0^+,\chi}(n)=\sum_{q\nmid n}\chi(R_q).
}
\]
This is the signed stable off-shell endpoint count.

Interior support:
\[
\boxed{
I_{0^+,\chi}(n)=\sum_q\sum_{k=L_q}^{R_q-1}\chi(k).
}
\]
This is the signed strict-descent support count.

Global:
\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=\sum_{k\nmid n}\chi(k).
}
\]
For \(\chi=1\),
\[
(Q_n-\tau(n))+(n-Q_n)=n-\tau(n).
\]

## Three-axis framework
\[
\boxed{
\text{carrier}:\ \partial\oplus\mathrm{int}
}
\]
\[
\boxed{
\text{content}:\ \mathrm{remainder}\oplus\mathrm{curvature}
}
\]
\[
\boxed{
\text{character}:\ 1\oplus\chi_{-4}\oplus\chi_{-3}\oplus\chi_{12}.
}
\]
The carrier/content matrix is triangular; the V4 character transform acts independently on every surviving entry.

## Guardrails
1. Character carrier is \(k\), not \(q\).
2. Principal Dirichlet channel covers only unit residues modulo 12, not the full untwisted sum.
3. Character cancellation is not geometric shell contact.
4. Local cell V4/Walsh and global mod-12 V4 are distinct carriers with common abstract character algebra.
5. No new prime criterion, asymptotic, RH/GRH, or spectral conclusion is claimed.

## Companion note
`research-notes/V4_Character_Triangular_Carrier_Content_Decomposition.md`
