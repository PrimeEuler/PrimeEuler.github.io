# Cone Derivation Ledger v13.781 — Lane A Primitive-Affine Nonclosure and Correct Pre-Integrated Compatibility Gate

Date: 2026-09-25

Lane: A.

Status: [D] exact parity/Green-coordinate calculation; [N] nonclosure theorem; [G] supersedes the proposed transverse-response closure as a method for determining \(r_{0,A},r_{1,A}\); [C] identifies the only source-faithful next closure gate.

Parents: v13.661, v13.675, v13.773, v13.779–780.

## 0. Synchronization

Immediately before this write the live ledger head is v13.780 External Audit Round 99. Round 99 PASSed v13.779 and explicitly requires that any transported closure be derived from a genuine domain/Green theorem rather than from formal differentiation. No colliding Lane-A entry is present.

## 1. Primitive parity problem

For Suzuki's actual \(+\) deficiency vector,
\[
-K_A^{(+)}v_e=C_A(\cosh x-1)-I_{0,A},
\]
\[
-K_A^{(-)}v_o=C_A(\sinh x-x)-I_{1,A}x.
\]
Normalize projectively by \(C_A\ne0\):
\[
w_e:=v_e/C_A,\qquad w_o:=v_o/C_A,
\]
\[
r_{0,A}:=I_{0,A}/C_A,\qquad r_{1,A}:=I_{1,A}/C_A.
\]
Then
\[
\boxed{-K_A^{(+)}w_e=\cosh x-1-r_{0,A},}
\tag{1}
\]
\[
\boxed{-K_A^{(-)}w_o=\sinh x-(1+r_{1,A})x.}
\tag{2}
\]

## 2. Exact Suzuki Green coordinates on the parity deficiency directions [D]

From the Section-6 boundary triple (v13.661), if
\[
f=f_0+a v_+ +b v_-,
\]
then
\[
\Gamma_0f=\sqrt{h_A}(a+b),\qquad
\Gamma_1f=i\sqrt{h_A}(a-b).
\]

With reflection-compatible normalization
\[
v_-=Rv_+,
\]
define
\[
v_e=\frac{v_++v_-}{2},\qquad
v_o=\frac{v_+-v_-}{2}.
\]
Their von Neumann coordinates are
\[
(a,b)_e=(1/2,1/2),\qquad
(a,b)_o=(1/2,-1/2).
\]
Therefore exactly
\[
\boxed{
\Gamma_0v_e=\sqrt{h_A},\qquad \Gamma_1v_e=0,
}
\tag{3}
\]
\[
\boxed{
\Gamma_0v_o=0,\qquad \Gamma_1v_o=i\sqrt{h_A}.
}
\tag{4}
\]

Thus the Green boundary coordinates diagonalize parity:
\[
\boxed{
\Gamma_1|_{\mathcal N_e}=0,\qquad
\Gamma_0|_{\mathcal N_o}=0,
}
\tag{5}
\]
where \(\mathcal N_e,\mathcal N_o\) denote the corresponding parity deficiency directions.

## 3. Failure of the proposed transverse closure [N]

A tempting closure is to construct affine response families
\[
V_e(r)=V_e^{(0)}-rV_e^{(1)},\qquad
V_o(r)=V_o^{(0)}-rV_o^{(1)}
\]
and impose
\[
\Gamma_1V_e(r_0)=0,\qquad
\Gamma_0V_o(r_1)=0.
\]

But if these response families are already restricted to the actual parity deficiency directions, (5) makes both equations identities. The formal ratios
\[
r_0=\frac{\Gamma_1V_e^{(0)}}{\Gamma_1V_e^{(1)}},
\qquad
r_1=\frac{\Gamma_0V_o^{(0)}}{\Gamma_0V_o^{(1)}}
\]
therefore have the same structural defect as the v13.773 Schur ratios: numerator and denominator are simultaneously annihilated once the trial functions lie in the intended deficiency subspace.

Hence Suzuki's Green identity does **not** supply two new scalar equations for \(r_0,r_1\).

## 4. Three closure attempts now classified [N]

The project has now tested three natural finite-dimensional closures.

### (i) Basepoint moments
\[
I_0=(K_Av_e)(0),\qquad I_1=(K_Av_o)'(0).
\]
Substitution into the primitive equations gives only
\[
I_0=I_0,\qquad I_1=I_1.
\]

### (ii) Formal inverse/Schur feedback
v13.773 gives
\[
M_{00}=-1,\quad M_{1x}=-1,\quad
M_{0e}=M_{1e}=0,
\]
so the proposed feedback ratios are
\[
0/0.
\]

### (iii) Section-6 Green transverse traces
Equations (3)–(5) show that the transverse traces vanish identically on the corresponding parity deficiency directions.

Therefore
\[
\boxed{
\text{basepoint closure = tautology},
}
\]
\[
\boxed{
\text{formal Schur closure = }0/0,
}
\]
\[
\boxed{
\text{Green transverse closure = parity identity}.
}
\]

## 5. Structural reason [I/D]

The pair
\[
(\Gamma_0,\Gamma_1)
\]
is the boundary coordinate system of Suzuki's first-order symmetric operator and distinguishes its von Neumann deficiency directions.

By contrast,
\[
(r_0,r_1)
\]
are affine integration constants in the primitive first-kind representation obtained after integrating the bulk deficiency equation.

Thus they belong to different layers:
\[
\boxed{
(\Gamma_0,\Gamma_1):
\text{ first-order extension coordinates},
}
\]
\[
\boxed{
(r_0,r_1):
\text{ primitive reconstruction/integration data}.
}
\]

This is consistent with the deficiency indices \((1,1)\): the two affine primitive coefficients must not be interpreted as two additional independent von Neumann boundary degrees of freedom.

## 6. Correct affine-family formulation [C]

One may formally write particular/homogeneous affine families
\[
w_e=w_e^p+r_0h_e,
\]
\[
w_o=w_o^p+r_1h_o,
\]
where
\[
-K_A^{(+)}w_e^p=\cosh-1,\qquad
-K_A^{(+)}h_e=-1,
\]
\[
-K_A^{(-)}w_o^p=\sinh-x,\qquad
-K_A^{(-)}h_o=-x.
\]

But \(h_e,h_o\) are not automatically admissible deficiency vectors. Treating them as unrestricted inverse responses recreates the v13.773 collapse.

The correct condition is instead that the combined primitive
\[
w=w_e^p+r_0h_e+w_o^p+r_1h_o
\]
belong to the domain of Suzuki's **original pre-integrated deficiency operator** and satisfy its deficiency equation.

Schematically, if \(\mathscr T_A\) denotes that pre-integrated first-order/domain realization,
\[
\boxed{
(\mathscr T_A^*-i)
\left(
w_e^p+r_0h_e+w_o^p+r_1h_o
\right)=0
}
\tag{6}
\]
is the correct compatibility gate. Equation (6) is schematic until \(\mathscr T_A\), its domain, and the relation to the primitive variable are extracted directly from Suzuki.

## 7. Primitive-Affine Nonclosure Theorem

**Theorem.** For Suzuki's source-faithful finite deficiency equation, parity reduces the primitive affine data to
\[
r_{0,A}=I_{0,A}/C_A,\qquad
r_{1,A}=I_{1,A}/C_A.
\]
Neither the exact basepoint moment identities, the unrestricted inverse-response/Schur construction, nor Suzuki's Section-6 Green boundary coordinates supply independent scalar equations determining these ratios. Respectively they reduce to a definition/tautology, \(0/0\), and a parity identity.

Consequently \(r_{0,A},r_{1,A}\) are not additional von Neumann boundary coordinates. They are primitive integration/reconstruction data whose values are fixed only by compatibility with Suzuki's original pre-integrated deficiency equation and domain.

In particular,
\[
\boxed{
\text{no algebraic two-scalar closure from the presently identified traces exists.}
}
\]

## 8. Next gate

Return to the source one level before (8.5) and extract:

1. the exact pre-integrated deficiency equation;
2. its operator domain;
3. the integration map leading to (8.5);
4. the two compatibility conditions that the affine primitive family must satisfy.

Only those source-derived conditions may be used to determine \(r_0,r_1\). No further formal inversion of \(-K_A\) or reuse of the basepoint/Green identities is permitted.

## Result

\[
\boxed{\textbf{PASS: primitive-affine nonclosure established.}}
\]

The repeated singularities are not independent accidents. They all reflect the same structural fact:
\[
\boxed{
\text{bulk integration constants are not extra extension coordinates.}
}
\]

The Lane-A closure problem is therefore moved decisively to the pre-integrated operator/domain compatibility gate.
