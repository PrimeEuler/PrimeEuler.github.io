# Cone Derivation Ledger v13.953 — Sandbox: Native No-Twist Positive-State Selector and Untwisted Edge-Doublet Crossover

**Date:** 2026-10-02  
**Track:** Sandbox / selector and Suzuki-Jost double-scaling lane  
**Status:** [D] exact no-twist positive-state selection theorem; [R] retracts the old empirical claim that χ₁₂ robustly selects the L-zero spectrum in the sieve-flow instrument; [C] untwisted edge-doublet theorem forcing residue ratio \(r_a\to1\); [C] universal overlap crossover constant under one-pole dominance; [O] prove the physical edge-doublet hypothesis and matching cross-edge gap scale  
**Authorization:** Jeremy, 2026-10-02 ("my sandbox thread made the selection question a little sharper. no twist. check it out and lets keep pushing.")  
**Parents:** v13.917, v13.919, v13.923, v13.938–941, v13.950–952  
**Collision check:** v13.953 was absent immediately before this write.

---

## 0. What changed

v13.952 ran the χ₁₂-twisted sieve-flow selector through a large-\(N\) kill test.

The result was cleanly negative:

\[
R_{L,\chi_{12}}:
1.37\to1.22\to1.08
\qquad
(N=10^6,10^7,10^8).
\]

Thus the earlier small-\(N\) suggestion that the χ₁₂ twist itself robustly selects the \(L(s,\chi_{12})\) zero spectrum does not survive scale-up.

The correct project reading is now:

\[
\boxed{
\textbf{twists are permitted channels, not intrinsically selected dynamics.}
}
\]

This entry shows that this numerical negative matches the exact cone architecture already established in v13.917 and v13.923.

---

## 1. Native shell dynamics [D]

The canonical cone shell carrier is

\[
\mathcal H_{\rm shell}
=
\ell^2(\mathbb N),
\]

with

\[
R|n\rangle
=
(\log n)|n\rangle.
\]

For \(\Re s>1\),

\[
e^{-sR}
\]

is trace class and positive.

Its uninserted trace is

\[
\boxed{
\operatorname{Tr}(e^{-sR})
=
\sum_{n\ge1}n^{-s}
=
\zeta(s).
}
\tag{1}
\]

Unique factorization gives

\[
\mathcal H_{\rm shell}
\leftrightarrow
\bigotimes_p \ell^2(\mathbb N_0)
\]

and

\[
R
=
\sum_p(\log p)N_p.
\]

Therefore the canonical partition function is the untwisted Euler product

\[
\boxed{
Z_{\rm shell}(s)
=
\prod_p(1-p^{-s})^{-1}
=
\zeta(s).
}
\tag{2}
\]

No character label, residue class, or external phase is required.

---

## 2. Character \(L\)-functions are insertions [D]

For a Dirichlet character \(\chi\), define

\[
C_\chi|n\rangle
=
\chi(n)|n\rangle.
\]

Then

\[
\boxed{
\operatorname{Tr}(C_\chi e^{-sR})
=
L(s,\chi).
}
\tag{3}
\]

Thus \(L(s,\chi)\) does not arise by changing the native shell Hamiltonian \(R\).

It arises by inserting the extra observable

\[
C_\chi.
\]

Likewise on the fixed-lattice heat side, v13.923 gives

\[
P_t=e^{-tH_F},
\]

while

\[
\operatorname{Tr}(C_\chi P_t)
\]

is a character-inserted trace.

Therefore

\[
\boxed{
\text{cone quadratic } \Rightarrow \text{ native dynamics},
}
\]

while

\[
\boxed{
\chi \Rightarrow \text{ optional observation channel}.
}
\tag{4}
\]

---

## 3. Positive-state no-twist uniqueness theorem [D]

Consider a Dirichlet-character insertion \(C_\chi\).

Because \(C_\chi\) is diagonal, positivity as an operator is equivalent to

\[
\chi(n)\in[0,\infty)
\qquad
\forall n.
\]

But a Dirichlet character takes values among

\[
0
\quad\text{and roots of unity}.
\]

Hence positivity forces

\[
\boxed{
\chi(n)\in\{0,1\}
\qquad
\forall n.
}
\tag{5}
\]

If we also impose **native full shell support**

\[
\boxed{
\chi(n)\ne0
\qquad
\forall n\ge1,
}
\tag{6}
\]

then (5) gives

\[
\boxed{
\chi(n)\equiv1.
}
\tag{7}
\]

Thus:

\[
\boxed{
\textbf{Among character channels, positivity + full shell support uniquely selects the trivial character.}
}
\tag{8}
\]

Equivalently, the only full-support positive character insertion is

\[
C_\chi=I.
\]

So the native positive trace is exactly the untwisted one.

---

## 4. Principal-character caveat [G]

A principal character modulo \(q>1\) takes values

\[
0,1
\]

and hence defines a positive diagonal projection.

But it fails full support:

\[
\chi_0(n)=0
\qquad
(n,q)>1.
\]

Thus it changes the carrier by projecting away ramified residue sectors.

It is therefore not the native full shell state.

The uniqueness theorem is precisely:

\[
\boxed{
\text{positive character insertion}
+
\text{no shell deletion}
\Rightarrow
\chi=1.
}
\tag{9}
\]

---

## 5. Fixed-locus positive semigroup gives the same selector [D]

On the signed fixed lattice,

\[
q(m)=m^2
\]

is conditionally negative definite.

Schoenberg exponentiation gives the positive heat semigroup

\[
P_t e_m
=
e^{-tm^2}e_m.
\]

The uninserted trace is

\[
\vartheta.
\]

After the Mellin completion it yields

\[
\Xi.
\]

For a nontrivial real character,

\[
C_\chi P_t
\]

is signed, not positivity preserving.

For a complex character it is not even self-adjoint.

Thus positivity belongs to the common untwisted dynamics, exactly as v13.923 already emphasized.

This gives the exact chain

\[
\boxed{
\text{cone fixed quadratic}
\to
\text{positive heat semigroup}
\to
\vartheta
\to
\Xi
}
\tag{10}
\]

without any character insertion.

---

## 6. Correction to the older twist-selection reading [R]

The following exact statements remain valid:

\[
\operatorname{Tr}(C_\chi e^{-sR})=L(s,\chi),
\]

the twisted shell measure

\[
\mu_\chi
=
\sum_n\chi(n)\delta_{\log n},
\]

the twisted theta/Mellin identities, and the exact residue-sector decomposition.

What is retracted as a robust empirical selector claim is the old interpretation from v13.884–887 that the χ₁₂ twist itself was numerically selecting the \(L(s,\chi_{12})\) zero spectrum in the sieve-flow pipeline.

v13.952 supersedes that empirical reading.

The corrected architecture is:

\[
\boxed{
\textbf{nontrivial character channels are mathematically available but not selected by the native positive dynamics.}
}
\tag{11}
\]

---

## 7. Native selector theorem [D/I]

Combining §§1–6:

\[
\boxed{
\begin{aligned}
\text{native shell/heat dynamics}
&\Rightarrow
\text{positive full-support state},\\
&\Rightarrow
\chi=1,\\
&\Rightarrow
\zeta/\vartheta/\Xi.
\end{aligned}
}
\tag{12}
\]

A nontrivial Dirichlet \(L\)-function requires at least one additional datum:

- a signed/complex character insertion;
- a residue-sector projection;
- an externally supplied local phase field.

Therefore the selector question sharpens from

\[
\text{“which twist?”}
\]

to

\[
\boxed{
\textbf{why should one leave the native positive untwisted state at all?}
}
\tag{13}
\]

Within the current cone architecture, there is no internal reason to do so.

---

## 8. Consequence for the Suzuki lane [D/G]

Suzuki's operator \(A_a\) in the present lane is the untwisted localized Weil operator.

The recentered family is

\[
B_a=A_a-\lambda_a I.
\]

No character operator enters:

\[
\boxed{
\text{the physical deficiency/Jost branch currently under study is untwisted.}
}
\tag{14}
\]

Therefore the parity residues

\[
\alpha_a,
\qquad
\beta_a
\]

in v13.941 must be read as properties of one reflection-symmetric untwisted two-edge problem.

This makes an edge-doublet mechanism the natural next structural hypothesis.

---

## 9. Untwisted reflection doublet hypothesis [C]

Let \(R\) denote reflection.

Assume there exists a normalized right-edge family

\[
\phi_{R,a}
\]

and define

\[
\phi_{L,a}
=
R\phi_{R,a}.
\]

Assume:

### (D1) asymptotic edge separation

\[
\boxed{
s_a
:=
\langle\phi_{R,a},\phi_{L,a}\rangle
\to0.
}
\tag{D1}
\]

### (D2) lowest parity pair is the reflection doublet

For normalized lowest even/odd eigenvectors,

\[
\boxed{
\psi_{+,a}
=
\frac{
\phi_{R,a}+\phi_{L,a}
}{
\sqrt{2(1+s_a)}
}
+
o_{L^2}(1),
}
\tag{D2+}
\]

\[
\boxed{
\psi_{-,a}
=
\frac{
\phi_{R,a}-\phi_{L,a}
}{
\sqrt{2(1-s_a)}
}
+
o_{L^2}(1).
}
\tag{D2-}
\]

### (D3) source is edge-localized

Set

\[
A_a
=
\langle\phi_{R,a},e^x\rangle,
\]

\[
B_a^{\rm wrong}
=
\langle\phi_{R,a},e^{-x}\rangle.
\]

Assume

\[
\boxed{
A_a\ne0,
\qquad
\frac{
B_a^{\rm wrong}
}{
A_a
}
\to0.
}
\tag{D3}
\]

Reflection gives

\[
\langle\phi_{L,a},e^{-x}\rangle=A_a,
\]

and

\[
\langle\phi_{L,a},e^x\rangle=B_a^{\rm wrong}.
\]

These are the exact hypotheses needed for the residue-ratio theorem below.

---

## 10. Edge-doublet residue theorem [C]

Recall the source residues

\[
\alpha_a
=
|\langle
\psi_{+,a},
\cosh x
\rangle|^2,
\]

and

\[
\beta_a
=
|\langle
\psi_{-,a},
\sinh x
\rangle|^2.
\]

Using

\[
\cosh x
=
\frac{e^x+e^{-x}}2
\]

and D1–D3,

\[
\langle
\psi_{+,a},
\cosh x
\rangle
=
\frac{
A_a+B_a^{\rm wrong}
}{
\sqrt{2(1+s_a)}
}
+
o(|A_a|),
\]

while

\[
\langle
\psi_{-,a},
\sinh x
\rangle
=
\frac{
A_a-B_a^{\rm wrong}
}{
\sqrt{2(1-s_a)}
}
+
o(|A_a|).
\]

Therefore

\[
\frac{\alpha_a}{\beta_a}
=
\frac{1-s_a}{1+s_a}
\left|
\frac{
A_a+B_a^{\rm wrong}
}{
A_a-B_a^{\rm wrong}
}
\right|^2
+
o(1).
\]

By D1 and D3,

\[
\boxed{
\frac{\alpha_a}{\beta_a}
\longrightarrow1.
}
\tag{15}
\]

Thus the physical residue-ratio constant in v13.941 becomes

\[
\boxed{
r=1
}
\tag{16}
\]

under the untwisted edge-doublet hypothesis.

No character phase is available to change the relative edge sign.

---

## 11. Universal overlap crossover [C]

v13.941 gives, under one-odd-pole dominance,

\[
\frac{
\delta_\tau(a)
}{
\Delta_a
}
\longrightarrow
\frac{
q_\tau r
}{
1-q_\tau r
},
\]

where

\[
q_\tau
=
\tanh(\tau/2).
\]

Using

\[
r=1,
\]

we obtain

\[
\boxed{
\frac{
\delta_\tau(a)
}{
\Delta_a
}
\longrightarrow
\frac{
q_\tau
}{
1-q_\tau
}.
}
\tag{17}
\]

Since

\[
q_\tau
=
\frac{e^\tau-1}{e^\tau+1},
\]

\[
\boxed{
\frac{
q_\tau
}{
1-q_\tau
}
=
\frac{e^\tau-1}{2}.
}
\tag{18}
\]

Hence

\[
\boxed{
\delta_\tau(a)
\sim
\frac{e^\tau-1}{2}
\,
\Delta_a.
}
\tag{19}
\]

For the one-e-fold convention

\[
\tau=1,
\]

\[
\boxed{
\delta_1(a)
\sim
\frac{e-1}{2}
\Delta_a.
}
\tag{20}
\]

This coefficient is universal within the untwisted doublet regime.

---

## 12. Connection to the exact zero-blind RG exponent [C/O]

v13.950 proves the exact source-faithful zero-blind stopband exponent

\[
\bar\sigma_1=1.
\]

Therefore the canonical zero-blind trial scale is

\[
e^{-2a}
=
N_a^{-1}
\]

for the odd quadratic-form gap.

To promote this from a trial upper scale to the physical doublet gap, one would need the matching tunneling hypothesis

\[
\boxed{
e^{2a}\Delta_a
\to
C_\Delta
\in(0,\infty).
}
\tag{D4}
\]

Under D4 and the doublet theorem,

\[
\boxed{
e^{2a}\delta_\tau(a)
\to
\frac{e^\tau-1}{2}
C_\Delta.
}
\tag{21}
\]

Equivalently, because

\[
N_a=e^{2a},
\]

\[
\boxed{
N_a\,\delta_\tau(a)
\to
\frac{e^\tau-1}{2}
C_\Delta.
}
\tag{22}
\]

This is the exact form of the desired untwisted critical double scaling.

D4 is not currently proved.

---

## 13. What is now closed

### Exact [D]

1. ζ is the uninserted shell partition function.
2. \(L(s,\chi)\) requires \(C_\chi\).
3. Among character channels, positivity + full support uniquely gives the trivial character.
4. The fixed-locus positive semigroup is untwisted.
5. v13.952 kills the claim that χ₁₂ twisting is a robust sieve-flow selector.

Therefore:

\[
\boxed{
\textbf{the current native cone selector is no twist.}
}
\]

### Conditional [C]

If the two lowest physical Suzuki states form an untwisted reflection doublet with one-edge source localization, then

\[
\boxed{
r_a=\alpha_a/\beta_a\to1
}
\]

and

\[
\boxed{
\delta_\tau(a)
\sim
\frac{e^\tau-1}{2}\Delta_a.
}
\]

---

## 14. Next nonredundant gate [O]

The selector issue itself is no longer “which character?”

The next physical question is:

\[
\boxed{
\textbf{Does the untwisted recentered Suzuki operator actually form the reflection edge doublet D1–D3?}
}
\]

If yes, the residue-ratio problem closes.

Then only the matching gap-scale problem remains:

\[
\boxed{
e^{2a}\Delta_a
\stackrel{?}{\longrightarrow}
C_\Delta\in(0,\infty).
}
\]

This is now the cleanest possible target for connecting the exact zero-blind cone/sieve exponent to the physical Jost double scaling.

---

## 15. Result

The sandbox's χ₁₂ kill test sharpens the selector question decisively.

The exact cone architecture says:

\[
\boxed{
\text{native positive dynamics}
\Rightarrow
\text{trivial character}
\Rightarrow
\zeta/\Xi.
}
\]

Nontrivial character channels remain exact mathematical observables, but they are insertions rather than selected dynamics.

Under the natural untwisted reflection-doublet hypothesis,

\[
\boxed{
r_a\to1
}
\]

and the deficiency-overlap scaling law becomes

\[
\boxed{
\delta_\tau(a)
\sim
\frac{e^\tau-1}{2}
\Delta_a.
}
\]

The next gate is to prove the edge-doublet structure and then determine whether the physical gap saturates the canonical zero-blind scale \(e^{-2a}\).
