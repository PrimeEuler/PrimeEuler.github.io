# Cone Derivation Ledger v13.497 — Semilinear Residue–Tangent Cohomology Audit

## Purpose

Resolve the category subtlety left open in the prime-2 affine-frame branch. The issue is that the arithmetic involution \(\tau=\bar\sigma_5\) acts differently on the residue-field coordinate and on the square-zero tangent coefficient in
\[
R_2\cong \mathbf F_4[\eta]/(\eta^2).
\]
Earlier residue calculations used pure Frobenius \(x\mapsto x^2\), whereas the tangent coefficient transforms by a twisted Frobenius. This entry separates the two modules exactly, recomputes the relevant cohomology, and qualifies the frame interpretation in v13.466/v13.468/v13.469 and descendants.

This audit does not alter the exact A3/S4 character-coordinate results v13.478–v13.495 as abstract/chosen-coordinate representation theory.

---

## 1. Prime-2 ring coordinates

Let
\[
R_2=\mathcal O_K/2\mathcal O_K\cong \mathbf F_4[\eta]/(\eta^2),
\qquad \mathbf F_4=\mathbf F_2(w),\quad w^2+w+1=0.
\]
Use
\[
u=w+\eta,
\qquad \eta=u^2+u+1,
\qquad \eta^2=0.
\]
The arithmetic involution is
\[
\tau=\bar\sigma_5,
\qquad \tau(u)=u^5.
\]
From the established prime-2 identities,
\[
\boxed{\tau(w)=w^2,\qquad \tau(\eta)=w\eta.}
\]
Therefore for every \(x,t\in\mathbf F_4\),
\[
\boxed{\tau(x+t\eta)=x^2+w t^2\eta.}
\]
This is the basic semilinear formula required for the audit.

---

## 2. Residue and tangent are different C2-modules

As an additive \(\mathbf F_2\)-space,
\[
R_{2,+}=M_{\rm res}\oplus I,
\]
where
\[
M_{\rm res}\cong(\mathbf F_4,+),
\qquad I=\eta\mathbf F_4\cong(\mathbf F_4,+).
\]

On the residue summand,
\[
\boxed{F(x)=x^2.}
\]
On tangent coefficients,
\[
\boxed{L(t)=w t^2.}
\]
Thus the two actions are not the same module action.

This is the category distinction that must be respected whenever residue discrepancies are compared with tangent affine frames.

---

## 3. Residue-module cohomology

For \(F(x)=x^2\), the fixed set is
\[
M_{\rm res}^{C_2}=\{0,1\}.
\]
The characteristic-two norm/coboundary operator is
\[
N_F(x)=x+F(x)=x+x^2.
\]
Explicitly,
\[
N_F(0)=0,\quad N_F(1)=0,
\]
\[
N_F(w)=w+w^2=1,
\quad N_F(w^2)=w^2+w=1.
\]
Hence
\[
\operatorname{im}N_F=\{0,1\}=M_{\rm res}^{C_2}.
\]
Therefore
\[
\boxed{H^1(C_2,M_{\rm res})=0.}
\]
The nonzero residue cocycle value \(1\) has exactly two trivializations:
\[
\boxed{b=w\quad\text{or}\quad b=w^2.}
\]
This validates the pure-residue computation in v13.466.

---

## 4. Tangent-module cohomology

For the tangent coefficient action
\[
L(t)=wt^2,
\]
first verify
\[
L^2(t)=w(wt^2)^2=w\,w^2t^4=t,
\]
so this is indeed a \(C_2\)-action.

The fixed equation is
\[
t=wt^2.
\]
Its solutions in \(\mathbf F_4\) are
\[
\boxed{I^{C_2}=\{0,w^2\}.}
\]

Now compute
\[
N_L(t)=t+L(t)=t+wt^2.
\]
The four values are
\[
N_L(0)=0,
\]
\[
N_L(1)=1+w=w^2,
\]
\[
N_L(w)=w+w w^2=w+1=w^2,
\]
\[
N_L(w^2)=w^2+w(w^2)^2=w^2+w\,w=w^2+w^2=0.
\]
Thus
\[
\operatorname{im}N_L=\{0,w^2\}=I^{C_2}.
\]
Therefore
\[
\boxed{H^1(C_2,I)=0.}
\]
The nonzero tangent cocycle value \(w^2\) has exactly two trivializations:
\[
\boxed{b=1\quad\text{or}\quad b=w.}
\]
They differ by the nonzero invariant tangent vector \(w^2\).

This is not the residue pair \(\{w,w^2\}\).

---

## 5. Full additive ring cohomology

Since
\[
R_{2,+}=M_{\rm res}\oplus I
\]
as \(C_2\)-modules,
\[
H^1(C_2,R_{2,+})
\cong H^1(C_2,M_{\rm res})\oplus H^1(C_2,I).
\]
Hence
\[
\boxed{H^1(C_2,R_{2,+})=0.}
\]

Moreover in both summands the invariant subspace equals the norm image. Therefore the same direct calculation gives
\[
\boxed{H^2(C_2,M_{\rm res})=H^2(C_2,I)=H^2(C_2,R_{2,+})=0.}
\]
Here \(H^2(C_2,M)=M^{C_2}/N(M)\) for the additive module.

So there is no cohomological obstruction in either summand or in the full additive ring. The distinction is instead which semilinear module and which trivialization torsor is being used.

---

## 6. Exact action on the derivation value

From v13.458,
\[
D_7(u)=u=w+\eta.
\]
Applying the full arithmetic involution gives
\[
\tau(D_7(u))=\tau(u)=u^5.
\]
Using the semilinear decomposition,
\[
\boxed{(w,1)\longmapsto(w^2,w),}
\]
i.e.
\[
\boxed{\tau(w+\eta)=w^2+w\eta.}
\]
Thus the residue component transforms by pure Frobenius, while the tangent coefficient transforms by \(L(t)=wt^2\).

This explicitly demonstrates why reducing \(D_7(u)\) modulo \(\eta\) and then treating that residue value as a tangent coefficient is not equivariant.

---

## 7. Full-ring norm identity

Compute
\[
(1+\tau)u=u+u^5.
\]
Using
\[
u=w+\eta,\qquad \tau(u)=w^2+w\eta,
\]
we obtain
\[
u+\tau(u)
=(w+w^2)+(1+w)\eta
=1+w^2\eta.
\]
But the established tangent state is
\[
h=u^3=1+w^2\eta.
\]
Therefore
\[
\boxed{(1+\tau)u=h=u^3.}
\]
Also \(h\) is \(\tau\)-fixed, hence
\[
\boxed{(1+\tau)h=0.}
\]

Important category distinction:
\[
h=1+w^2\eta
\]
is a multiplicative tangent state in \(1+\eta\mathbf F_4\), whereas
\[
h-1=w^2\eta
\]
is the corresponding additive tangent vector. They should not be conflated.

The full-ring norm identity is the clean object that packages the residue and tangent contributions simultaneously.

---

## 8. Qualification of v13.466

The v13.466 statement
\[
w+w^2=1
\]
and the residue cocycle
\[
c(\tau)=1
\]
are exact in the pure residue Frobenius module. Its two trivializations are exactly
\[
\{w,w^2\}.
\]

However, that pair is not the trivialization pair for the tangent coefficient module. In the tangent module the nonzero fixed/coboundary value is \(w^2\), and the two trivializations are
\[
\boxed{\{1,w\}.}
\]

Therefore v13.466 remains correct as residue cohomology, but any wording identifying its \(\{w,w^2\}\) torsor directly with the tangent affine-frame torsor must be qualified.

---

## 9. Qualification of v13.468 and v13.469

The prime-3 Pell phase statements remain exact:
\[
j([\lambda])=1,
\qquad
j([\lambda^{-1}])=-1=2,
\]
and under the two-prime phase carrier
\[
\Psi(j)=w^j,
\]
\[
\boxed{\Psi([\lambda])=w,\qquad \Psi([\lambda^{-1}])=w^2.}
\]

Likewise the Galois time-orientation law remains exact:
\[
\boxed{\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}},
\]
so
\[
\boxed{n\mapsto\chi_{12}(r)n.}
\]

What does not follow is that the two Pell orientations \(w,w^2\) are the two tangent affine-frame trivializations. Under the correct tangent action those trivializations are \(1,w\).

Thus the safe statement is:

- \(w,w^2\) are the two oriented residue/Pell phase values;
- \(1,w\) are the two trivializations of the nonzero tangent cocycle;
- the positive Pell phase \(w\) belongs to both sets, but the inverse phase \(w^2\) does not;
- no canonical bijection between these two two-element torsors has yet been established.

---

## 10. Status of v13.474 and v13.476 onward

The exact character decomposition
\[
\chi_{-4}=\chi_{12}\chi_{-3}
\]
and bit relation
\[
\ell=p\oplus f
\]
remain unchanged.

The chosen affine coordinate model
\[
1\mapsto0,\quad5\mapsto1,\quad7\mapsto w^2,\quad11\mapsto w
\]
and the resulting
\[
V_4\rtimes S_3\cong S_4
\]
matrices, character tables, tetrahedral geometry, A3 roots, root/weight lattices, and \(P/Q\) classifier remain exact as a chosen oriented coordinate realization.

What is not currently certified is the stronger arithmetic claim that Pell orientation alone canonically selects that pointwise identification
\[
U(12)\longrightarrow T_2.
\]

Accordingly, v13.476–v13.495 should be read as exact representation/lattice theory after a chosen oriented identification, except for those portions (such as the character-value tetrahedron itself) that are intrinsic directly from the three quadratic characters and do not use the tangent identification.

In particular, the A3 tetrahedral construction
\[
v_r=(\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r))
\]
is intrinsic and unaffected by this audit.

---

## 11. Corrected structural picture

The audited prime-2 structure is
\[
\boxed{
\begin{array}{ccc}
\text{residue module}&:&x\mapsto x^2,\\
&&H^1=0,\quad c=1,\quad\text{trivializers }\{w,w^2\};\\[1mm]
\text{tangent module}&:&t\mapsto wt^2,\\
&&H^1=0,\quad c=w^2,\quad\text{trivializers }\{1,w\};\\[1mm]
\text{full ring}&:&\tau(x+t\eta)=x^2+wt^2\eta,\\
&&(1+\tau)u=h=u^3.
\end{array}}
\]

The common element \(w\) is noteworthy, but by itself does not supply a canonical equivalence of the residue and tangent torsors.

---

## 12. Conclusion

The semilinear audit resolves the outstanding category issue:
\[
\boxed{\text{residue Frobenius}\neq\text{tangent coefficient action}.}
\]
Both modules have trivial first cohomology, but their nonzero invariant cocycles and their trivialization pairs differ.

The strongest exact bridge currently available across the full prime-2 ring is
\[
\boxed{(1+\tau)u=h=u^3,}
\]
not an identification of the residue trivializer pair \(\{w,w^2\}\) with the tangent-frame pair \(\{1,w\}\).

This preserves the exact Pell-time law, the exact residue-phase law, and all intrinsic/chosen-coordinate S4/A3 results, while withdrawing the unsupported step that Pell orientation by itself canonically fixes the tangent affine frame.