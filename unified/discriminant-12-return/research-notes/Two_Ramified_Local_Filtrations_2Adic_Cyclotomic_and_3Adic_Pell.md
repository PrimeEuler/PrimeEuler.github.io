# Two Ramified Local Filtrations: 2-adic Cyclotomic Stability and 3-adic Pell Growth

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 1. Setup

We compare two distinct ramified local towers already present in the discriminant-12 program.

Cyclotomic prime-2 tower:

\[
K=\mathbf Q(\zeta_{12}),\qquad R_{2^k}=\mathcal O_K/2^k\mathcal O_K.
\]

Pell prime-3 tower:

\[
F=\mathbf Q(\sqrt3),\qquad S_{3^k}=\mathcal O_F/3^k\mathcal O_F,
\]

with Pell unit

\[
\lambda=2+\sqrt3.
\]

The carriers are different and remain so throughout.

## 2. Cyclotomic order is stable from mod 4 onward [D]

Let

\[
u_k:=\zeta_{12}\bmod 2^k.
\]

Since

\[
\zeta_{12}^{12}=1,
\qquad
\zeta_{12}^6=-1,
\]

we have for every \(k\ge2\)

\[
-1\not\equiv1\pmod{2^k}.
\]

Hence the order of \(u_k\) divides 12 but does not divide 6. Therefore

\[
\boxed{\operatorname{ord}_{R_{2^k}^\times}(u_k)=12\qquad(k\ge2).}
\]

At \(k=1\), characteristic two identifies \(-1=1\), and the order drops to 6, as established in v13.438.

Thus the exact order profile is

\[
\boxed{
\operatorname{ord}(\zeta_{12}\bmod 2^k)=
\begin{cases}
6,&k=1,\\
12,&k\ge2.
\end{cases}}
\]

The full residue-field quotient then drops further to order 3 after killing the nilpotent ramification layer.

## 3. Cyclotomic Galois faithfulness stabilizes at mod 4 [D]

For \(r\in U(12)=\{1,5,7,11\}\),

\[
\sigma_r(u_k)=u_k^r.
\]

For \(k\ge2\), \(u_k\) has exact order 12, so the exponents \(1,5,7,11\) remain distinct modulo 12. Hence

\[
\boxed{U(12)\hookrightarrow\operatorname{Aut}(R_{2^k})\qquad(k\ge2)}
\]

is faithful.

At \(k=1\), the action collapses to the \(\chi_{-3}\) quotient \(C_2\), as in v13.416/v13.446.

Therefore

\[
\boxed{
V_4\ \xrightarrow{\bmod 4}\ V_4\ \xrightarrow{\bmod 2}\ C_2.
}
\]

More conceptually, mod 4 is already deep enough to recover the two character directions merged at mod 2.

## 4. Additive congruence layers in the 2-adic tower [D]

For every \(k\ge2\), reduction gives

\[
0\to 2^{k-1}\mathcal O_K/2^k\mathcal O_K
\to R_{2^k}
\to R_{2^{k-1}}
\to0.
\]

Multiplication by \(2^{k-1}\) identifies the kernel additively with

\[
\boxed{
2^{k-1}\mathcal O_K/2^k\mathcal O_K
\cong
\mathcal O_K/2\mathcal O_K.
}
\]

Using v13.438,

\[
\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_4[\eta]/(\eta^2).
\]

Thus every successive 2-adic congruence layer has the same four-dimensional \(\mathbf F_2\)-additive profile.

The first layer already contains the oriented correction

\[
\sqrt3+i=2\zeta_{12},
\qquad
\sqrt3-i=2\zeta_{12}^{-1},
\]

which separates the \(\chi_{-4}\) and \(\chi_{12}\) directions at mod 4.

## 5. Pell unit order grows at every 3-adic depth [D]

Set

\[
\pi=\sqrt3,
\qquad
3=\pi^2,
\]

and

\[
\mu:=-\lambda=-(2+\pi).
\]

Then

\[
\mu-1=-3-\pi=-\pi(1+\pi),
\]

so

\[
\boxed{v_\pi(\mu-1)=1.}
\]

A direct first cube gives

\[
\mu^3-1=-27-15\pi=-\pi^3(5+3\pi),
\]

and the parenthesis is a \(\pi\)-adic unit. Hence

\[
\boxed{v_\pi(\mu^3-1)=3.}
\]

Now suppose \(x=1+y\) with \(v_\pi(y)=s\ge3\). Then

\[
x^3-1=3y+3y^2+y^3.
\]

The three valuations are

\[
s+2,\qquad2s+2,\qquad3s,
\]

and for \(s\ge3\), the unique minimum is \(s+2\). Therefore cubing raises the valuation exactly by 2.

Inductively,

\[
\boxed{
v_\pi\bigl(\mu^{3^r}-1\bigr)=1+2r
\qquad(r\ge0).
}
\]

Since

\[
3^k=\pi^{2k},
\]

we have

\[
\mu^{3^r}\equiv1\pmod{3^k}
\iff
1+2r\ge2k.
\]

The least such \(r\) is \(r=k\). Thus

\[
\boxed{\operatorname{ord}_{S_{3^k}^\times}(\mu)=3^k.}
\]

Because \(\lambda=-\mu\) and the orders \(2\) and \(3^k\) are coprime,

\[
\boxed{
\operatorname{ord}_{S_{3^k}^\times}(\lambda)=2\cdot3^k.
}
\]

So the literal Pell-unit clock grows by a factor of 3 at every deeper ramified level:

\[
\boxed{6,18,54,162,\ldots}
\]

for \(k=1,2,3,4,\ldots\).

## 6. Matrix and projective Pell orders [D]

The integral Pell matrix \(g_{12}\) represents multiplication by \(\lambda\) in the ramified ideal basis. Hence

\[
\boxed{\operatorname{ord}_{\bmod 3^k}(g_{12})=2\cdot3^k.}
\]

Moreover the half-period is scalar:

\[
\boxed{g_{12}^{3^k}\equiv-I\pmod{3^k}.}
\]

Therefore projectivization kills that scalar half-turn and gives

\[
\boxed{
\operatorname{ord}_{\mathrm{PGL}_2(\mathbf Z/3^k\mathbf Z)}([g_{12}])=3^k.
}
\]

At \(k=1\), this recovers the order-3 projective action on the three-state shell from v13.439-v13.441.

## 7. Additive congruence layers in the 3-adic tower [D]

Likewise,

\[
0\to3^{k-1}\mathcal O_F/3^k\mathcal O_F
\to S_{3^k}
\to S_{3^{k-1}}
\to0,
\]

and

\[
\boxed{
3^{k-1}\mathcal O_F/3^k\mathcal O_F
\cong
\mathcal O_F/3\mathcal O_F
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

Thus every successive 3-adic congruence layer repeats the same two-dimensional \(\mathbf F_3\)-additive ramification profile.

The Pell cyclic orbit samples one principal-unit direction in this local filtration, and each extra layer contributes one additional factor of 3 to its order.

## 8. Exact filtration table [D]

\[
\boxed{
\begin{array}{c|c|c}
\text{feature}&\text{prime 2 cyclotomic tower}&\text{prime 3 Pell tower}\\
\hline
\text{base ramified quotient}
&\mathbf F_4[\eta]/(\eta^2)
&\mathbf F_3[\epsilon]/(\epsilon^2)\\
\text{residue field}&\mathbf F_4&\mathbf F_3\\
\text{successive additive layer}
&\mathcal O_K/2&\mathcal O_F/3\\
\text{distinguished clock at first level}&6&6\\
\text{clock at depth }k\ge2&12&2\cdot3^k\\
\text{Galois/character faithfulness}&V_4\text{ for }k\ge2&C_2\text{ inversion on Pell direction}\\
\text{projective clock}&3\text{ after residue-field quotient}&3^k\\
\end{array}}
\]

The two towers share ramified square-zero first layers but differ sharply in dynamical behavior.

## 9. Structural interpretation [I]

The common local pattern is:

\[
\boxed{
\text{ramified dual-number first layer}
\quad+\quad
\text{repeated congruence layers of the same additive type}.
}
\]

The distinction is in how the distinguished arithmetic generator sits inside those filtrations.

At prime 2, \(\zeta_{12}\) is torsion already in characteristic zero, so after mod 4 the full order 12 is restored and then stabilizes permanently.

At prime 3, the Pell unit is non-torsion in characteristic zero. Its principal-unit component penetrates arbitrarily deeply into the 3-adic filtration, producing exact order growth

\[
2\cdot3^k.
\]

Thus the finite common \(S_3\) phase from v13.439-v13.442 is the shared depth-one quotient of two very different local dynamical towers.

## 10. Guardrails [Audit]

- The prime-2 and prime-3 rings have different residue fields and different dimensions over those fields.
- The common dual-number form does not imply a ring isomorphism between the two local towers.
- The growing Pell order is not a cyclotomic-order phenomenon.
- The stable cyclotomic order is not evidence that the 2-adic unit filtration itself becomes trivial; only the distinguished torsion generator stabilizes.
- No Suzuki positivity consequence is inferred from the local-filtration comparison.

---

**Conclusion.** The two ramified discriminant-12 towers share the same qualitative first-order architecture—square-zero ramified tangent layers repeated through congruence quotients—but their distinguished clocks behave oppositely. Cyclotomic multiplication loses one factor of two only at mod 2 and is fully restored from mod 4 onward, while the Pell return acquires a new factor of three at every 3-adic depth. The common three-state S3 phase is therefore a genuine shared shallow quotient, sitting above two inequivalent infinite local filtrations.
