# Associated-Graded Ramified Towers and Repeating S3 Phases

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 1. Prime-2 cyclotomic associated graded [D]

Let
\[
K=\mathbf Q(\zeta_{12}),
\qquad
\mathfrak P_2=(1+i)\subset\mathcal O_K,
\qquad
\kappa_2:=\mathcal O_K/\mathfrak P_2\cong\mathbf F_4.
\]
Since the prime above 2 has ramification index 2 and residue degree 2, each additive associated-graded piece is one-dimensional over the residue field:
\[
\operatorname{gr}_{\mathfrak P_2}^n(\mathcal O_K)
:=\mathfrak P_2^n/\mathfrak P_2^{n+1}
\cong\mathbf F_4
\qquad(n\ge0).
\]
Write \(\omega=\zeta_{12}\bmod\mathfrak P_2\), so \(\omega^2+\omega+1=0\).

Multiplication by \(\zeta_{12}\) preserves every power of \(\mathfrak P_2\), and on each graded quotient acts by the residue scalar:
\[
\boxed{
M_{\zeta_{12}}|_{\operatorname{gr}^n}=M_\omega.
}
\]
Thus on the nonzero points of every graded piece it gives the order-3 cycle of \(\mathbf F_4^\times\).

For \(r\in U(12)\), the Galois action on the residue field is controlled by \(\chi_{-3}\):
\[
\sigma_r|_{\kappa_2}
=
\begin{cases}
\mathrm{id},&\chi_{-3}(r)=+1,\\
\mathrm{Fr},&\chi_{-3}(r)=-1,
\end{cases}
\qquad \mathrm{Fr}(a)=a^2.
\]
Choose the uniformizer \(\pi_2=1+i\). If \(r=1,5\), \(\sigma_r(\pi_2)=\pi_2\). If \(r=7,11\), then
\[
\sigma_r(\pi_2)=1-i=(-i)(1+i),
\]
and \(-i\equiv1\pmod{\mathfrak P_2}\). Hence the uniformizer contributes no extra scalar on the associated graded. Therefore for every \(n\),
\[
\boxed{
\sigma_r(a\pi_2^n)\equiv
\begin{cases}
a\pi_2^n,&\chi_{-3}(r)=+1,\\
a^2\pi_2^n,&\chi_{-3}(r)=-1
\end{cases}
\pmod{\mathfrak P_2^{n+1}}.
}
\]
Thus every nonzero graded shell carries the same semilinear group
\[
\boxed{
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong C_3\rtimes C_2\cong S_3.
}
\]

### Consequence [D/I]
The full \(V_4\) Galois action recovered modulo 4 is not visible on any single associated-graded layer. Each layer sees only the \(\chi_{-3}\) quotient. The additional mod-4 information is therefore extension data linking successive ramified layers.

## 2. Prime-2 principal-unit torsion chain [D]

Let
\[
w:=\zeta_{12}^4,
\]
so \(w\) has order 3 and reduces to \(\omega\). Then
\[
h:=\zeta_{12}w^{-1}=\zeta_{12}^{-3}=-i.
\]
The element \(h\) is the principal-unit component of the cyclotomic generator. With \(\pi_2=1+i\),
\[
\boxed{h=1-\pi_2.}
\]
Hence
\[
v_{\mathfrak P_2}(h-1)=1.
\]
Also
\[
h^2=-1,
\qquad
h^2-1=-2,
\]
and since \(v_{\mathfrak P_2}(2)=2\),
\[
\boxed{v_{\mathfrak P_2}(h^2-1)=2.}
\]
Finally \(h^4=1\). Thus the 2-primary torsion part has the finite depth pattern
\[
\boxed{1\longrightarrow2\longrightarrow\infty}
\]
under successive squaring: first graded layer, second graded layer, then termination.

## 3. Prime-3 Pell associated unit graded [D]

Let
\[
F=\mathbf Q(\sqrt3),
\qquad
\pi_3=\sqrt3,
\qquad
\mathfrak p_3=(\pi_3),
\qquad
\kappa_3=\mathbf F_3.
\]
Define the principal-unit filtration
\[
U_3^n:=1+\mathfrak p_3^n.
\]
For every \(n\ge1\), multiplication of principal units gives
\[
\boxed{
U_3^n/U_3^{n+1}\cong(\mathbf F_3,+),
}
\]
via
\[
1+a\pi_3^n\longmapsto a\bmod\mathfrak p_3.
\]

Quadratic conjugation sends \(\pi_3\mapsto-\pi_3\), hence on the nth graded unit quotient,
\[
\boxed{
c_n:a\longmapsto(-1)^n a.
}
\]
So even graded pieces have trivial conjugation action, while odd graded pieces carry inversion.

## 4. Pell principal unit visits exactly the odd grades [D]

Let
\[
\lambda=2+\sqrt3,
\qquad
\mu:=-\lambda.
\]
Then \(\mu\equiv1\pmod{\mathfrak p_3}\), and the previously established valuation law is
\[
\boxed{
v_{\pi_3}(\mu^{3^r}-1)=1+2r.}
\]
Therefore
\[
\mu^{3^r}\in U_3^{1+2r}\setminus U_3^{2+2r}.
\]
Thus the distinguished Pell phase lands successively in the odd associated-graded pieces
\[
\boxed{1,3,5,7,\ldots.}
\]
Its class in each active quotient generates the additive \(C_3\). Since conjugation acts by minus sign on every odd grade, the corresponding phase action is
\[
\boxed{
j\mapsto j+1,\qquad j\mapsto-j,}
\]
and therefore each Pell-active odd graded layer carries
\[
\boxed{C_3\rtimes C_2\cong S_3.}
\]
The even principal-unit grades are not hit by the sequence \(\mu^{3^r}\), and conjugation acts trivially on them.

## 5. Associated-graded comparison [D/I]

The two ramified towers therefore have the following exact graded behavior.

### Prime 2 cyclotomic tower
- every additive graded layer is \(\mathbf F_4\);
- multiplication by \(\zeta_{12}\) acts by the same residue scalar \(\omega\) on every layer;
- Galois acts through the same \(\chi_{-3}\) identity/Frobenius quotient on every layer;
- every nonzero graded shell therefore carries the same \(S_3\) phase;
- the missing \(V_4\) information recovered at modulus 4 is extension data between layers, not extra character data within an individual graded piece.

### Prime 3 Pell tower
- every principal-unit graded layer is \(\mathbf F_3\) additively;
- conjugation alternates by parity, acting as \((-1)^n\);
- the distinguished Pell principal unit reaches precisely the odd layers \(1+2r\);
- each active odd layer therefore carries the same \(S_3\) affine phase;
- the growing 3-adic order comes from continuing to deeper odd layers rather than from changing the local phase group on a fixed layer.

Hence
\[
\boxed{
\text{prime 2: repeated }S_3\text{ on every graded shell},
}
\]
while
\[
\boxed{
\text{prime 3: repeated }S_3\text{ on the odd Pell-active graded shells}.
}
\]

## 6. Why the deep towers differ despite the same graded phase [I]

The shared \(S_3\) phase does not force the deep local clocks to agree.

At prime 2, the cyclotomic generator is torsion. Its residue order-3 part repeats on each graded quotient, while its principal-unit part is finite 4-torsion with depth chain
\[
1\to2\to\infty.
\]
This is why the total cyclotomic order stabilizes at 12 from modulus 4 onward.

At prime 3, the Pell unit is non-torsion. The principal-unit part repeatedly reappears two ramification degrees deeper under cubing:
\[
1\to3\to5\to7\to\cdots.
\]
This is why the finite Pell order grows as \(2\cdot3^k\).

Thus the common \(S_3\) is genuinely a graded local phase, while the difference between the infinite towers is encoded in how the distinguished arithmetic generator moves between graded layers.

## 7. Relation to the intrinsic discriminant-12 quotient [D/I]

The intrinsic \(S_3\) of v13.454 is now seen as the first instance of a repeated associated-graded pattern:

- at prime 2, the first residue/tangent layer is one of an infinite sequence of \(\mathbf F_4\) graded shells with the same semilinear \(S_3\);
- at prime 3, the first tangent phase is the first of the odd-grade principal-unit shells successively reached by the Pell generator.

Accordingly, the maximal common phase quotient from v13.450 is terminal as a finite quotient but recurrent as a local graded symmetry.

## 8. Guardrails [Audit]

- The two associated-graded rings are over different residue fields and are not identified as rings.
- The repeated \(S_3\) actions are isomorphic phase actions, not a single global operator acting simultaneously on both towers.
- The full mod-4 \(V_4\) recovery on the cyclotomic side is extension data and must not be attributed to any single \(\mathbf F_4\) graded quotient.
- On the Pell side, even unit grades exist but are not visited by the distinguished sequence \(\mu^{3^r}\); they should not be discarded from the local ring itself.
- No Suzuki terminal direction is identified with either graded tower by this calculation.

---

**Conclusion.** The discriminant-12 ramified towers share a repeated local \(S_3\) phase at the associated-graded level. The prime-2 cyclotomic tower realizes it on every nonzero \(\mathbf F_4\) graded shell, while the prime-3 Pell tower realizes it on every odd principal-unit grade reached by successive cubing of the normalized Pell unit. Their deep arithmetic divergence is therefore not a difference in the local phase symmetry itself, but in the inter-grade dynamics: finite torsion termination at 2 versus unbounded principal-unit penetration at 3.
