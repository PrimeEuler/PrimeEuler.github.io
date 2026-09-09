# V4 Support Inversion and Unit-Residue Divisor-Contact Reconstruction

## Status
Exact arithmetic continuation of the V4 defect-support thread after External Audit Round 22. This note deliberately does **not** identify any arithmetic quarter with the SU(2) Casimir quarter. The only factor `1/4` below is the inverse normalization of the four-character Hadamard transform on `U(12)`.

## 1. Setup
For
\[
\delta_k(n)=\left\{\frac nk\right\}=\frac{n\bmod k}{k},
\]
the positive-defect support is
\[
\{k\le n:\delta_k(n)>0\}=\{k\le n:k\nmid n\}.
\]
For a Dirichlet character \(\chi\) modulo 12 define the twisted support channel
\[
\boxed{
S_\chi(n):=\sum_{k\nmid n}\chi(k).
}
\]
Equivalently, from the defect moment family,
\[
\boxed{
S_\chi(n)=\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n).
}
\]

The four real characters on the unit group
\[
U(12)=\{1,5,7,11\}\cong V_4
\]
are
\[
1,\qquad \chi_{-4},\qquad \chi_{-3},\qquad \chi_{12}=\chi_{-4}\chi_{-3}.
\]

## 2. Unit-residue off-shell counts
For \(r\in\{1,5,7,11\}\), define
\[
\boxed{
N_r^{\rm off}(n)
:=\#\{k\le n:k\nmid n,\ k\equiv r\pmod{12}\}.
}
\]
Let
\[
\mathbf N^{\rm off}
=
\begin{pmatrix}
N_1^{\rm off}\\
N_5^{\rm off}\\
N_7^{\rm off}\\
N_{11}^{\rm off}
\end{pmatrix}.
\]
Using the character table
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
we have the exact transform
\[
\boxed{
\begin{pmatrix}
S_1^\times\\
S_{-4}\\
S_{-3}\\
S_{12}
\end{pmatrix}
=
H_4\mathbf N^{\rm off}.
}
\]
Here \(S_1^\times\) is the principal Dirichlet-character channel, hence restricted to columns coprime to 12; it is not the full untwisted support \(n-\tau(n)\).

Therefore
\[
\boxed{
\mathbf N^{\rm off}
=\frac14H_4
\begin{pmatrix}
S_1^\times\\
S_{-4}\\
S_{-3}\\
S_{12}
\end{pmatrix}.
}
\]

### Normalization guardrail
The factor \(1/4\) here is **only** the inverse-Hadamard normalization following from \(H_4^2=4I\). It is unrelated to the Casimir completion constant, null-diamond midpoint norm, or normalized mixed second difference.

## 3. Why one twisted zero is not a shell-contact criterion
For any nontrivial character, cancellation can produce
\[
S_\chi(n)=0
\]
while many positive-defect columns remain. Therefore
\[
\boxed{S_\chi(n)=0\not\Rightarrow k\mid n\text{ for the contributing columns}.}
\]
A vanishing single character channel records signed residue balance, not disappearance of support.

The full four-channel vector is different: because the Hadamard transform is invertible, it reconstructs all four unit-residue off-shell counts exactly.

Thus the correct zero-locus statement is:
\[
\boxed{
\mathbf S(n)=0
\iff
N_1^{\rm off}=N_5^{\rm off}=N_7^{\rm off}=N_{11}^{\rm off}=0,
}
\]
where \(\mathbf S=(S_1^\times,S_{-4},S_{-3},S_{12})^T\).
This means every unit-residue column up to \(n\) is a divisor of \(n\), an extremely restrictive condition; it is not a generic primality test.

## 4. Reconstructing divisor-contact counts by residue
Define the total number of columns in each unit residue class:
\[
\boxed{
U_r(n):=\#\{k\le n:k\equiv r\pmod{12}\}.
}
\]
Define unit-residue divisor-contact counts
\[
\boxed{
C_r(n):=\#\{d\mid n:d\equiv r\pmod{12}\}.
}
\]
Since every unit-residue column is either a divisor contact or off shell,
\[
\boxed{
C_r(n)=U_r(n)-N_r^{\rm off}(n).
}
\]
Hence the four twisted support channels, together with the deterministic totals \(U_r(n)\), reconstruct the unit-residue divisor-contact counts exactly.

In vector form,
\[
\boxed{
\mathbf C
=
\mathbf U
-\frac14H_4\mathbf S.
}
\]
Again the \(1/4\) is inverse-Hadamard normalization only.

## 5. Equivalent divisor-character sums
Define
\[
D_\chi(n):=\sum_{d\mid n}\chi(d).
\]
Also define the complete character prefix sum
\[
P_\chi(n):=\sum_{k=1}^{n}\chi(k).
\]
Because the support/complement partition is exact,
\[
P_\chi(n)
=
\sum_{d\mid n}\chi(d)
+
\sum_{k\nmid n}\chi(k),
\]
so
\[
\boxed{
D_\chi(n)=P_\chi(n)-S_\chi(n).
}
\]
This holds for all four Dirichlet characters, including the principal character modulo 12.

The divisor-character vector
\[
\mathbf D
=
(D_1^\times,D_{-4},D_{-3},D_{12})^T
\]
is the Hadamard transform of the residue-contact vector:
\[
\boxed{\mathbf D=H_4\mathbf C},
\qquad
\boxed{\mathbf C=\frac14H_4\mathbf D}.
\]
Thus the unit-residue contact reconstruction can be viewed either from off-shell support or directly from divisor-character sums.

## 6. Relation to the ordinary divisor count
The principal modulo-12 divisor sum
\[
D_1^\times(n)
=\#\{d\mid n:\gcd(d,12)=1\}
\]
counts only unit-residue divisors.

If
\[
\gcd(n,6)=1,
\]
then every divisor of \(n\) is coprime to 12, and therefore
\[
\boxed{D_1^\times(n)=\tau(n)}.
\]
In this coprime-to-6 sector,
\[
\boxed{	au(n)=C_1+C_5+C_7+C_{11}}.
\]
Outside that sector, nonunit residue classes contain additional divisor contacts and must be treated separately.

## 7. Carrier split can be inverted independently
From the boundary/interior support decomposition, define for each unit residue \(r\):
\[
B_r(n):=\#\{q\in Q(n):q\nmid n,\ R_q\equiv r\pmod{12}\},
\]
\[
I_r(n):=\#\{k:\ k\text{ is strict-descent and }k\equiv r\pmod{12}\}.
\]
Then
\[
N_r^{\rm off}=B_r+I_r.
\]
The V4 transform acts independently on each carrier:
\[
\boxed{\mathbf B_\chi=H_4\mathbf B_r},
\qquad
\boxed{\mathbf I_\chi=H_4\mathbf I_r}.
\]
Hence
\[
\boxed{
\mathbf B_r=\frac14H_4\mathbf B_\chi,
\qquad
\mathbf I_r=\frac14H_4\mathbf I_\chi.
}
\]
Character projection therefore commutes with the boundary/interior carrier split at the support level.

## 8. Structural conclusion
The exact arithmetic statement is not that a single twisted channel detects divisibility. Rather:

1. each character channel is a signed projection of unit-residue off-shell support;
2. individual channels can vanish by cancellation;
3. the complete four-character vector is invertible and reconstructs the four unit-residue off-shell counts;
4. subtracting those counts from the known total residue populations reconstructs the unit-residue divisor-contact counts;
5. this reconstruction is independent of the Casimir/null-diamond quarter discussion.

## 9. Guardrails
- Local factor-cell V4/Walsh labels and global mod-12 Dirichlet characters are distinct carriers.
- A zero in one twisted character channel is a cancellation statement, not a divisor-contact statement.
- The principal Dirichlet character modulo 12 vanishes on nonunits; its support channel is not the full untwisted support.
- The inverse-transform factor \(1/4\) is group-Fourier normalization only and has no asserted relation to any other quarter appearing elsewhere in the project.
- Unit-residue contact reconstruction gives counts by residue class, not the individual divisor positions unless additional data are retained.
- For \(\gcd(n,6)\ne1\), unit-residue contact counts do not exhaust \(\tau(n)\).
- No new primality criterion or factoring algorithm is claimed.
