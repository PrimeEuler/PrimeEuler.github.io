# Cone Derivation Ledger v13.378 — V4 Support Inversion and Unit-Residue Divisor Contacts

**Date:** 2026-09-09

## Audit reconciliation
External Audit Round 22 verified the local Casimir/V4 algebra but added a binding guardrail: equal numerical quarter terms at matched special parameter values must not be called a structural unification unless the bridge survives at generic parameter values. In particular, the standard SU(2) identity
\[
(j+\tfrac12)^2=j(j+1)+\tfrac14
\]
contains no free lattice-spacing parameter \(\delta\). Therefore prior language equating its \(1/4\) with \(\delta^2/4\) from factor-cell mixed differences is to be read only as a matched quarter-square form at unit spacing, not as a theorem identifying the carriers.

This checkpoint continues on an independent arithmetic path. Any factor \(1/4\) below comes solely from inversion of the four-character Hadamard matrix \(H_4\), since \(H_4^2=4I\).

## 1. Twisted support channels
For
\[
\delta_k(n)=\{n/k\},
\]
define
\[
\boxed{S_\chi(n)=\sum_{k\nmid n}\chi(k)}.
\]
Equivalently,
\[
\boxed{S_\chi(n)=\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)}.
\]

## 2. Unit-residue off-shell support
For \(r\in\{1,5,7,11\}\),
\[
\boxed{N_r^{\rm off}(n)=\#\{k\le n:k\nmid n,\ k\equiv r\pmod{12}\}}.
\]
With
\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I,
\]
we have
\[
\boxed{
\begin{pmatrix}
S_1^\times\\S_{-4}\\S_{-3}\\S_{12}
\end{pmatrix}
=H_4
\begin{pmatrix}
N_1^{\rm off}\\N_5^{\rm off}\\N_7^{\rm off}\\N_{11}^{\rm off}
\end{pmatrix}.
}
\]
Thus
\[
\boxed{
\begin{pmatrix}
N_1^{\rm off}\\N_5^{\rm off}\\N_7^{\rm off}\\N_{11}^{\rm off}
\end{pmatrix}
=rac14H_4
\begin{pmatrix}
S_1^\times\\S_{-4}\\S_{-3}\\S_{12}
\end{pmatrix}.
}
\]

**Guardrail:** this \(1/4\) is inverse-Hadamard normalization only. It is unrelated to the Casimir, null-diamond, or mixed-difference quarters.

## 3. Single-channel zeros versus full inversion
A nontrivial twisted channel may vanish through signed cancellation:
\[
S_\chi(n)=0
\]
does not imply disappearance of positive-defect support and is not a divisibility criterion.

The full four-channel vector is invertible:
\[
\boxed{
\mathbf S(n)=0
\iff
N_1^{\rm off}=N_5^{\rm off}=N_7^{\rm off}=N_{11}^{\rm off}=0.
}
\]
This states that every unit-residue column up to \(n\) is a divisor; it is not a generic primality condition.

## 4. Exact unit-residue divisor-contact reconstruction
Define
\[
U_r(n)=\#\{k\le n:k\equiv r\pmod{12}\},
\]
\[
C_r(n)=\#\{d\mid n:d\equiv r\pmod{12}\}.
\]
Then
\[
\boxed{C_r=U_r-N_r^{\rm off}}.
\]
Hence
\[
\boxed{
\mathbf C
=
\mathbf U-rac14H_4\mathbf S.
}
\]
So the complete V4 support vector plus known residue populations reconstructs the number of divisor-shell contacts in each unit residue class exactly.

## 5. Divisor-character complement identity
For each character,
\[
D_\chi(n):=\sum_{d\mid n}\chi(d),
\qquad
P_\chi(n):=\sum_{k=1}^n\chi(k).
\]
The divisor/off-shell partition gives
\[
\boxed{D_\chi(n)=P_\chi(n)-S_\chi(n)}.
\]
The four divisor-character channels satisfy
\[
\boxed{\mathbf D=H_4\mathbf C},
\qquad
\boxed{\mathbf C=\frac14H_4\mathbf D}.
\]

For the principal character modulo 12,
\[
D_1^\times(n)=\#\{d\mid n:\gcd(d,12)=1\}.
\]
If \(\gcd(n,6)=1\), all divisors are units modulo 12 and
\[
\boxed{D_1^\times(n)=\tau(n)=C_1+C_5+C_7+C_{11}}.
\]
Otherwise nonunit divisor contacts are omitted from this V4 unit-sector reconstruction.

## 6. Carrier split commutes with V4 inversion
Let
\[
B_r=\#\{q\in Q(n):q\nmid n,\ R_q\equiv r\pmod{12}\}
\]
count stable off-shell terminal endpoints in residue \(r\), and let
\[
I_r=\#\{k:\text{strict descent},\ k\equiv r\pmod{12}\}
\]
count strict-descent interior columns. Then
\[
N_r^{\rm off}=B_r+I_r.
\]
Their character transforms invert independently:
\[
\boxed{\mathbf B_\chi=H_4\mathbf B_r,\qquad \mathbf I_\chi=H_4\mathbf I_r},
\]
\[
\boxed{\mathbf B_r=\frac14H_4\mathbf B_\chi,\qquad \mathbf I_r=\frac14H_4\mathbf I_\chi}.
\]
Therefore the character projection commutes exactly with the boundary/interior support split.

## 7. Exact conclusion
The arithmetic V4 result is now sharper:

- individual nontrivial character channels measure signed residue imbalance and may vanish by cancellation;
- the complete four-character support vector reconstructs unit-residue off-shell counts exactly;
- complementing against known residue populations reconstructs unit-residue divisor-contact counts;
- the same reconstruction can be expressed through divisor-character sums;
- boundary and interior support carriers can be inverted separately;
- none of these statements uses or requires the Casimir-quarter analogy.

## 8. Guardrails
1. External Audit Round 22's generic-parameter test is binding: matched special-value quarters do not establish structural unification.
2. The \(1/4\) in this checkpoint is only the inverse normalization of \(H_4\).
3. Local factor-cell Walsh V4 and global mod-12 Dirichlet V4 are different carriers.
4. One twisted zero is cancellation, not divisibility.
5. The principal modulo-12 channel is unit-restricted, not the full untwisted channel.
6. Contact reconstruction is by residue counts, not individual divisor locations.
7. For \(\gcd(n,6)\ne1\), nonunit divisor contacts are outside the four-unit-residue V4 sector.
8. No new primality criterion or factoring algorithm is asserted.

## Companion note
`research-notes/V4_Support_Inversion_and_Unit_Residue_Divisor_Contact_Reconstruction.md`
