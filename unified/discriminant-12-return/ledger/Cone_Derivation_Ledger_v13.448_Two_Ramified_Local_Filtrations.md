# Cone Derivation Ledger v13.448 — Two Ramified Local Filtrations

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked before this work and again immediately before this numbered write. The newest numbered ledger entry remained `v13.447` (`Mod-4 Character Recovery and First 2-adic Separation`), so `v13.448` was free at creation time.

A concurrent Suzuki commit landed during this derivation: an independent frozen-8D normalized midpoint replay. That affects the positivity/theorem-promotion thread but does not alter the local arithmetic derivation below.

This checkpoint compares the two ramified local towers that have emerged from the Pell and cyclotomic threads.

## 1. Prime-2 cyclotomic tower [D]

Let

\[
K=\mathbf Q(\zeta_{12}),
\qquad
R_{2^k}=\mathcal O_K/2^k\mathcal O_K,
\]

and write

\[
u_k=\zeta_{12}\bmod 2^k.
\]

Because

\[
\zeta_{12}^{12}=1,
\qquad
\zeta_{12}^6=-1,
\]

we have

\[
\operatorname{ord}(u_1)=6
\]

at mod 2, since \(-1=1\) in characteristic two.

For every \(k\ge2\), however,

\[
-1\not\equiv1\pmod{2^k},
\]

so the order divides 12 but cannot divide 6. Therefore

\[
\boxed{
\operatorname{ord}_{R_{2^k}^\times}(u_k)=12
\qquad(k\ge2).
}
\]

Hence the exact cyclotomic-order profile is

\[
\boxed{6,12,12,12,\ldots}
\]

for mod \(2,4,8,16,\ldots\).

## 2. Prime-2 Galois faithfulness [D]

For \(r\in U(12)=\{1,5,7,11\}\),

\[
\sigma_r(u_k)=u_k^r.
\]

When \(k\ge2\), the element \(u_k\) has exact order 12, so the four exponents \(1,5,7,11\) remain distinct modulo 12. Therefore the full Galois action is faithful:

\[
\boxed{
U(12)\hookrightarrow\operatorname{Aut}(R_{2^k})
\qquad(k\ge2).
}
\]

At mod 2, the action collapses to the \(\chi_{-3}\) quotient \(C_2\), as established in v13.416/v13.446.

Thus

\[
\boxed{
V_4\text{ at characteristic zero/mod }4\text{ and deeper}
\quad\longrightarrow\quad
C_2\text{ at mod }2.
}
\]

The mod-2 collapse is therefore exceptional and does not persist in the deeper 2-adic tower.

## 3. Repeated prime-2 congruence layers [D]

For every \(k\ge2\), reduction yields

\[
0\to2^{k-1}\mathcal O_K/2^k\mathcal O_K
\to R_{2^k}
\to R_{2^{k-1}}
\to0.
\]

Multiplication by \(2^{k-1}\) gives the additive identification

\[
\boxed{
2^{k-1}\mathcal O_K/2^k\mathcal O_K
\cong
\mathcal O_K/2\mathcal O_K.
}
\]

From v13.438,

\[
\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_4[\eta]/(\eta^2).
\]

Hence every successive 2-adic congruence layer repeats the same four-dimensional \(\mathbf F_2\)-additive ramified profile.

The first deeper layer already restores the directions merged at mod 2 through

\[
\sqrt3+i=2\zeta_{12},
\qquad
\sqrt3-i=2\zeta_{12}^{-1}.
\]

## 4. Prime-3 Pell tower [D]

Let

\[
F=\mathbf Q(\sqrt3),
\qquad
\pi=\sqrt3,
\qquad
3=\pi^2,
\]

and

\[
\lambda=2+\pi,
\qquad
\mu:=-\lambda.
\]

Then

\[
\mu-1=-3-\pi=-\pi(1+\pi),
\]

so

\[
\boxed{v_\pi(\mu-1)=1.}
\]

A direct cube gives

\[
\mu^3-1=-27-15\pi=-\pi^3(5+3\pi),
\]

with \(5+3\pi\) a \(\pi\)-adic unit. Therefore

\[
\boxed{v_\pi(\mu^3-1)=3.}
\]

If \(x=1+y\) and \(v_\pi(y)=s\ge3\), then

\[
x^3-1=3y+3y^2+y^3.
\]

The term valuations are

\[
s+2,\quad2s+2,\quad3s,
\]

and the unique minimum is \(s+2\). Thus cubing raises the \(\pi\)-adic valuation exactly by 2.

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

the least \(r\) for which \(\mu^{3^r}\equiv1\pmod{3^k}\) is \(r=k\). Hence

\[
\boxed{
\operatorname{ord}(\mu\bmod3^k)=3^k.
}
\]

Because \(\lambda=-\mu\),

\[
\boxed{
\operatorname{ord}(\lambda\bmod3^k)=2\cdot3^k.
}
\]

So the literal Pell-unit order profile is

\[
\boxed{6,18,54,162,\ldots}
\]

for mod \(3,9,27,81,\ldots\).

## 5. Pell matrix and projective order [D]

The integral return matrix \(g_{12}\) represents multiplication by \(\lambda\) in the ramified ideal basis. Therefore

\[
\boxed{
\operatorname{ord}_{\bmod3^k}(g_{12})=2\cdot3^k.
}
\]

At the half-period,

\[
\boxed{
g_{12}^{3^k}\equiv-I\pmod{3^k}.
}
\]

After projectivization the scalar \(-I\) disappears, giving

\[
\boxed{
\operatorname{ord}_{\mathrm{PGL}_2(\mathbf Z/3^k\mathbf Z)}([g_{12}])=3^k.
}
\]

For \(k=1\), this is the order-3 phase cycle on the anisotropic shell from v13.439-v13.441.

## 6. Repeated prime-3 congruence layers [D]

Similarly,

\[
0\to3^{k-1}\mathcal O_F/3^k\mathcal O_F
\to\mathcal O_F/3^k\mathcal O_F
\to\mathcal O_F/3^{k-1}\mathcal O_F
\to0,
\]

with

\[
\boxed{
3^{k-1}\mathcal O_F/3^k\mathcal O_F
\cong
\mathcal O_F/3\mathcal O_F
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

Thus every deeper 3-adic layer repeats the same two-dimensional \(\mathbf F_3\)-additive ramified profile.

The Pell unit's principal-unit component penetrates one layer deeper every time its exponent is multiplied by 3, which is exactly why its order grows by a factor of 3 at each depth.

## 7. Exact comparison table [D]

\[
\boxed{
\begin{array}{c|c|c}
\text{feature}&\text{prime 2 cyclotomic}&\text{prime 3 Pell}\\
\hline
\text{first ramified ring}&\mathbf F_4[\eta]/(\eta^2)&\mathbf F_3[\epsilon]/(\epsilon^2)\\
\text{residue field}&\mathbf F_4&\mathbf F_3\\
\text{successive additive layer}&\mathcal O_K/2&\mathcal O_F/3\\
\text{distinguished order at depth 1}&6&6\\
\text{depth }k\ge2&12&2\cdot3^k\\
\text{Galois/character behavior}&V_4\text{ faithful for }k\ge2&C_2\text{ inversion on Pell direction}\\
\text{projective/terminal phase}&C_3\text{ after residue quotient}&C_{3^k}
\end{array}}
\]

## 8. Structural synthesis [I]

The shared local architecture is the existence of ramified square-zero first layers and repeated congruence quotients of the same additive type.

The distinguished generators behave very differently:

- cyclotomic multiplication is torsion already in characteristic zero, so after the exceptional mod-2 collapse its full order 12 is restored at mod 4 and remains stable;
- the Pell unit is non-torsion in characteristic zero, and its principal-unit component moves deeper into the 3-adic filtration, producing unbounded order growth \(2\cdot3^k\).

Therefore the common three-state \(S_3\) phase found in v13.439-v13.442 is a genuine shared shallow quotient of two inequivalent infinite local towers.

## 9. Suzuki-thread synchronization [Audit]

During this derivation an independent midpoint replay for the normalized frozen odd 8D subspace was committed. Together with v13.434/v13.443 and the v13.445 audit, the Suzuki theorem thread has now reduced its remaining obstacle set to the outward certification of the normalized frozen-8D bounds. No implication from the present local-arithmetic comparison to those analytic bounds is claimed.

## 10. Guardrails [Audit]

- The prime-2 and prime-3 local rings are not isomorphic.
- The common dual-number first-order form does not identify their residue fields or unit groups.
- Stable cyclotomic order does not mean the full 2-adic unit filtration is trivial.
- Growing Pell order is a principal-unit phenomenon and not a cyclotomic torsion phenomenon.
- The shared depth-one \(S_3\) phase is a quotient-level equivalence, not an equality of carriers.

---

**Checkpoint conclusion.** The discriminant-12 ramified towers share a common first-order architecture but diverge dynamically. The 2-adic cyclotomic clock is exceptional only at mod 2 and stabilizes at order 12 from mod 4 onward, with full V4 Galois faithfulness recovered immediately. The 3-adic Pell clock instead grows exactly as \(2\cdot3^k\), with projective order \(3^k\). Their common finite S3 phase is therefore the shallow intersection of a stable torsion tower and a genuinely expanding principal-unit tower.
