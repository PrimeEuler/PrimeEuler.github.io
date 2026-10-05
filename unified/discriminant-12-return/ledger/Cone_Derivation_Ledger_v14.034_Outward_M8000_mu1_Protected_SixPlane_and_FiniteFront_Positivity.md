# Cone Derivation Ledger v14.034 — Outward M8000 mu=1 Protected Six-Plane and Finite-Front Positivity

**Date:** 2026-10-05
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] graph-congruence/Feshbach reduction; [D] exact-source scalar-to-operator enclosure; [D] conservative LDDD primitive-chain rounding envelope; [N-cert] 420-digit all-mode scalar interval replay; [N-cert] pre-cancellation protected magnitude replay; [D] v14.031 complement floors consumed; **THEOREM:** finite shifted front F_p is strictly positive for both parities at mu=1; [O] v14.027 §6(b) four-channel Gram and §6(c) geometric remainder remain.
**Parents:** v14.027, v14.029, v14.031, v14.015, v14.025.
**Research/workflow commits:** 1f59353795fe07747f200f18051685cb773021c1; 768f5ef9073c7370bb31f44dca8d13dd7fc90a4a; 84413caa6ff8d970523c35a9eea21bfdab27140c; d2de8819aca0cef7eecc0d4b3762c31c305d5fbe; e77eb30092817466e012f00304365ab3707200cb; b42891d5d8f3d38befcd3dfbc9a6b73494208220; 461cb614d7ccbf8af3ac97f2629d6a88cb352c0a; e541fe91be838e194bca7524b10a91e8c6102ee5; 87a37946798fd66ecf4e523ddae11b2fd589ca52; 12b6c48194b94aac4590b5262da07e23769e4755.
**Collision check (original):** immediately before this write, live HEAD was 12b6c48194b94aac4590b5262da07e23769e4755 and no v14.032 ledger file or commit was present.
**Renumbering note (External Audit):** this entry's commit (`6f82afe`, 2026-10-05 09:52:09 -0400 = 13:52:09 UTC) collided with the External Audit Round 160 entry (`9790e1c`, 03:28:15 UTC), which landed first by several hours. Per the standing commit-timestamp precedence rule, Round 160 keeps v14.032 and this entry is renumbered to **v14.034**, with no change to its mathematical content. See External Audit Round 161 for the full writeup.

---

## 1. The finite-front obligation

v14.027 reduces the Euclidean coercivity theorem to three finite outward tasks. The first is positivity of the shifted finite front

\[
F_p=A_{p,\le8000}-\Pi_{4000<n\le8000}.
\]

v14.029/v14.031 already certify the large complement of the fixed six-plane. What remained was the protected six-dimensional Schur block.

Let P be the identical stored frozen six-column carrier used in v14.008, v14.024, v14.029 and v14.031, let Q be its Euclidean orthogonal complement, and write

\[
F_p=
\begin{pmatrix}
F_{PP}&F_{PQ}\\
F_{QP}&F_{QQ}
\end{pmatrix}.
\]

From v14.031, rigorously

\[
\boxed{
F_{QQ}^{(e)}\succeq\delta_e I,\qquad
\delta_e=7.795385618610192746\times10^{-6},
}
\]

\[
\boxed{
F_{QQ}^{(o)}\succeq\delta_o I,\qquad
\delta_o=3.262507025086259604\times10^{-5}.
}
\]

Thus only positivity of the exact protected Schur matrix remains.

---

## 2. Graph congruence identity [D]

Let W be any six-column graph trial whose protected-coordinate matrix

\[
B=(P^*P)^{-1}P^*W
\]

is invertible. Define the exact normalized graph

\[
\widehat W=WB^{-1}=P+X,\qquad X\in\operatorname{Ran}Q.
\]

Let

\[
R=QFW.
\]

Then the exact protected Schur matrix

\[
S=F_{PP}-F_{PQ}F_{QQ}^{-1}F_{QP}
\]

satisfies the congruence identity

\[
\boxed{
B^*SB
=
W^*FW-R^*F_{QQ}^{-1}R.
}
\tag{1}
\]

The proof is the graph completion-of-squares identity; equivalently normalize W by B^{-1} and use v14.031's graph-Schur formula. Therefore it is enough to show the right side of (1) is positive. Exact orthogonality of the numerically represented graph vectors is not required; invertibility of B suffices.

---

## 3. Protected-coordinate invertibility [N-cert/D]

The LDDD graph-coordinate replay gives

### even

\[
\max|P^*Y|
=
2.27606841636014\times10^{-41},
\]

\[
\sigma_{\min}(B)
=
0.99999999999999999999999999999999999999998779\ldots
\]

### odd

\[
\max|P^*Y|
=
5.54502399412988\times10^{-41},
\]

\[
\sigma_{\min}(B)
=
0.99999999999999999999999999999999999999996847\ldots
\]

The same LDDD primitive envelope used below is vastly smaller than even a public 10^{-12} invertibility allowance. Hence B is rigorously invertible in both sectors. No eigenvalue lower bound is transported through B; only positivity is transported by congruence.

---

## 4. Exact scalar producer intervals [N-cert]

The full 420-digit interval replay over all 4000 modes in each parity encloses the exact source-faithful scalar producer relative to the production LDDD payload.

### even

\[
\epsilon_z\le5.809110335412397\times10^{-39},
\]

\[
\epsilon_d\le3.0000001815446517\times10^{-32},
\]

\[
\epsilon_p\le7.365230177656668\times10^{-40},
\]

\[
\epsilon_c\le6.740593794183538\times10^{-42},
\qquad c=2/\pi.
\]

### odd

\[
\epsilon_z\le5.829046823471421\times10^{-39},
\]

\[
\epsilon_d\le7.500001658183785\times10^{-33},
\]

\[
\epsilon_p\le4.987119893996533\times10^{-41},
\]

with the same epsilon_c.

These intervals include the v14.015 archimedean truncation allowance and the omitted exponential z-correction tail.

**Guardrail.** The later split-precision replay is not used: its 100-digit digamma interval branch loses correlation and produces enormous z widths. The successful full 420-digit replay is the load-bearing source enclosure.

---

## 5. Scalar-to-operator enclosure [D]

For same-parity modes n_i,n_j,

\[
q_{ij}=\frac{z_i n_j-z_j n_i}{n_i^2-n_j^2}.
\]

If every z-coordinate is perturbed by at most epsilon_z, then

\[
|\Delta q_{ij}|
\le
\frac{\epsilon_z}{|n_i-n_j|}.
\]

Likewise, using the analytic all-finite-mode bound |z_n|<10 obtained from the same v14.025 digamma/prime/correction majorant,

\[
|q_{ij}|\le\frac{10}{|n_i-n_j|}.
\]

On a parity lattice of 4000 points,

\[
\sum_{j\ne i}\frac1{|n_i-n_j|}<H_{3999}<9.
\]

Hence the displacement-kernel representation error obeys the Schur row bound

\[
E_{\rm disp}
\le
9\left[(1+\epsilon_c)\epsilon_z+10\epsilon_c\right].
\tag{2}
\]

For the parity pole vector

\[
p_n=\frac{2k_ng}{k_n^2+1/4},
\]

one has

\[
\|p_e\|_2\le\sqrt2\cosh(1/2),
\]

\[
\|p_o\|_2\le\frac{4\sinh(1/2)}{\sqrt{24}}.
\]

With ||Delta p||_2 <= sqrt(4000) epsilon_p and |alpha|=2, the rank-one perturbation satisfies

\[
E_{\rm pole}
\le
2\left(2\|p\|_2\|\Delta p\|_2+\|\Delta p\|_2^2\right).
\tag{3}
\]

Combining (2), (3), and the diagonal error gives rigorous Euclidean operator radii

\[
\|\Delta F_e\|_2<3.01\times10^{-32},
\qquad
\|\Delta F_o\|_2<7.51\times10^{-33}.
\]

For the represented graph matrices,

\[
\|W_e\|_F^2=6.001323151827835,
\qquad
\|W_o\|_F^2=6.009267708281584.
\]

Therefore the exact-source protected-form charges used below are

\[
\boxed{
E_{\rm src,e}
=
1.8004180606546245\times10^{-31},
}
\]

\[
\boxed{
E_{\rm src,o}
=
4.5069868934512124\times10^{-32}.
}

---

## 6. LDDD arithmetic envelope [D]

On the audited x86 runner, long double has a 64-bit significand, so

\[
u=2^{-64}.
\]

The production engine uses Knuth two_sum and Dekker two_prod with splitter 2^{32}+1. Away from overflow/underflow, both are error-free transformations: the returned high+low pair equals the exact sum/product of the two input floating values.

Consequently first-order rounding is retained in the low component. The only discarded arithmetic appears when already-small low terms are themselves multiplied or summed. Under the maintained nonoverlap |x_lo|<=2u|x_hi|, direct triangle estimates give the conservative primitive bounds

\[
E_{\rm add}\le16u^2 M,\quad
E_{\rm mul_d}\le16u^2 M,
\]

\[
E_{\rm mul}\le32u^2 M,\quad
E_{\rm div_d}\le64u^2 M,
\]

where M is the positive pre-cancellation magnitude entering that primitive.

A source-faithful matrix entry uses fewer than sixteen such primitive stages. The row matvec and final protected dot each use one sequential two-component accumulation over N=4000 terms. Charging every primitive at its largest 64u^2 rate, charging both sequential accumulations by their full N-fold positive magnitude, and adding an eightfold safety factor yields

\[
\boxed{
E_{\rm DD}
\le
4096\,N\,u^2\,Q_{\rm comp}.
}
\tag{4}
\]

Here Q_comp is the positive contribution magnitude before cancellation, not |W^*FW| after cancellation.

The independent pre-cancellation replay gives

\[
Q_{\rm comp,e}^{\rm mid}=6.831468950718294,
\]

\[
Q_{\rm comp,o}^{\rm mid}=2.419996208244608.
\]

We use the public cap

\[
\boxed{Q_{\rm comp}\le32},
\]

which inflates these positive sums by factors 4.68 and 13.2. The scalar/source and long-double operation uncertainty needed to move the positive sum to the exact arithmetic object is many orders smaller than this inflation.

Thus

\[
\boxed{
E_{\rm DD}
\le
1.5407439555097887\times10^{-30}
}
\]

in either parity.

---

## 7. Exact graph residual correction [D]

The refined LDDD graph residuals are 10^{-28} to 10^{-27} class. For the final outward theorem we deliberately use the much looser public cap

\[
\boxed{\|R\|_2\le10^{-20}.}
\]

The scalar-to-operator enclosure above and the same LDDD primitive bound show that arithmetic/source uncertainty in the residual action is below 10^{-29}; hence this cap has more than eight orders of headroom over the computed residual.

Using the theorem-level v14.031 complement floors,

\[
R^*F_{QQ}^{-1}R
\preceq
\frac{\|R\|^2}{\delta}I.
\]

Therefore

\[
E_{R,e}
\le
1.2828101763338885\times10^{-35},
\]

\[
E_{R,o}
\le
3.0651274995294771\times10^{-36}.
\]

---

## 8. Protected outward lower bounds [D/N-cert]

The 180-digit protected midpoint minima are

\[
\lambda_{e,\rm mid}
=
5.6957561105269459079\times10^{-30},
\]

\[
\lambda_{o,\rm mid}
=
1.4356977652056780761\times10^{-26}.
\]

By Weyl plus the exact graph correction (1), subtract the source-form, LDDD, and residual charges:

\[
\lambda_{e,\rm out}
\ge
\lambda_{e,\rm mid}
-E_{\rm src,e}
-E_{\rm DD}
-E_{R,e}
\]

\[
\boxed{
\lambda_{e,\rm out}
>
3.9749575208499314\times10^{-30}>0.
}
\]

Likewise

\[
\boxed{
\lambda_{o,\rm out}
>
1.4355391835167209\times10^{-26}>0.
}

The even certificate retains about 69.79% of the midpoint pivot; the odd certificate retains 99.989%.

---

## 9. Finite-front theorem

Since

\[
F_{QQ}^{(p)}\succ0
\]

rigorously by v14.031 and the exact protected Schur matrix is positive by §8, the Schur-complement criterion gives

\[
\boxed{
F_e=A_{e,\le8000}-\Pi_{4000<n\le8000}\succ0,
}
\]

\[
\boxed{
F_o=A_{o,\le8000}-\Pi_{4000<n\le8000}\succ0.
}

Thus v14.027 §6(a), the finite shifted-front positivity obligation at mu=1, is closed.

Equivalently, the finite-shell Euclidean Schur complements satisfy

\[
S_{e,4000\to8000}\succ I,
\qquad
S_{o,4000\to8000}\succ I.
\]

---

## 10. Remaining Euclidean-gamma work

The only remaining inputs in v14.027 are now:

1. §6(b): outward correlated four-channel Gram upper bound for the far shifted-front Schur correction;
2. §6(c): outward K=10 geometric remainder, with enormous headroom.

Once these close, v14.027 immediately promotes

\[
S_{e,4000}\succeq I,
\qquad
S_{o,4000}\succeq I,
\]

so v14.016/v14.022 may consume the rigorous Euclidean constant gamma_E=1.

---

HANDOFF
target: sandbox
type: audit
parent: v14.034
status: open
action: Independently audit the outward M8000 mu=1 protected six-plane certificate and finite-front positivity theorem, focusing on the scalar-to-operator Schur row bound, the C_DD=4096 error-free-transformation envelope with pre-cancellation Qcomp<=32, the graph-coordinate/congruence interface, and the deliberately loose ||R||<=1e-20 residual cap. Confirm whether v14.027 §6(a) is rigorously closed.
deliverable: theorem-or-obstruction
constraints: Use the full 420-digit scalar interval replay, not the invalid split-precision z replay; consume the v14.031 complement floors exactly; do not infer the still-open far Gram or geometric-remainder obligations.
