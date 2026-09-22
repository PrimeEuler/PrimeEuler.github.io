# Cone Derivation Ledger v13.676 — Audit of v13.673: Finite Hermite-Biehler Theorem Confirmed, with Explicit Normalization Hypothesis

Date: 2026-09-22

Status: independent re-derivation of v13.673 after the convention stabilization v13.675. Result: PASS, subject to one explicitly stated normalization hypothesis that was implicit in v13.673.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.675. No collision. v13.674 specifically requested a careful audit of v13.673 after stabilizing the W/raw-boundary-form sign. v13.675 confirms v13.672's sign, so that prerequisite is now satisfied.

## 1. Hypothesis that must be explicit

Assume the finite deficiency basis is chosen in the canonical real/reflection normalization
\[
\boxed{v_-(x)=v_+(-x),\qquad v_+(x)\in\mathbb R.}
\]
This is stronger than equal norm alone. Equal norm determines only the modulus of the relative phase; the sharp identities below require the reflection phase to be fixed to zero.

This canonical phase is compatible with the real reflection-symmetric finite problem and with the project's earlier phase audit, but the HB theorem should state it as a hypothesis unless it is derived afresh from the chosen T_a^{-1}e^{\pm x} normalization.

## 2. Sharp identities

Let
\[
F(z)=\int_{-a}^a v_+(x)e^{izx}\,dx.
\]
Under the hypothesis,
\[
\widehat v_-(z)=F(-z)=F^\sharp(z).
\]
Therefore
\[
W_0=(z-i)F+(z+i)F^\sharp,
\]
\[
W_\pi=(z-i)F-(z+i)F^\sharp.
\]
Direct sharp conjugation gives
\[
\boxed{W_0^\sharp=W_0,\qquad W_\pi^\sharp=-W_\pi.}
\]
This part of v13.673 is exact.

## 3. Correct HB function

With
\[
c=c_\infty=\xi'(3/2)/\xi(3/2)>0,
\]
define
\[
E_a=W_\pi-cW_0.
\]
Then
\[
\boxed{
E_a^\sharp=-W_\pi-cW_0.
}
\]
From v13.661/v13.675,
\[
W_0/W_\pi=i m_a.
\]
Hence
\[
\boxed{
-\frac{E_a^\sharp}{E_a}
=
\frac{1+icm_a}{1-icm_a}.
}
\]

## 4. Hermite-Biehler inequality

For z in C_+, the scalar Weyl function of an ordinary boundary triple is Nevanlinna:
\[
m_a(z)=x+iy,\qquad y>0
\]
for the simple deficiency-(1,1) operator. Then
\[
|1+icm|^2=(1-cy)^2+c^2x^2,
\]
\[
|1-icm|^2=(1+cy)^2+c^2x^2.
\]
Thus
\[
|1+icm|<|1-icm|
\]
and therefore
\[
\boxed{|E_a^\sharp(z)|<|E_a(z)|\quad(\operatorname{Im}z>0).}
\]
So
\[
\boxed{E_a\text{ is Hermite-Biehler}.}
\]

This confirms the central theorem of v13.673.

## 5. A/B decomposition

Using
\[
E_a=A_a-iB_a,
\]
with
\[
A_a=(E_a+E_a^\sharp)/2,\qquad
B_a=(E_a^\sharp-E_a)/(2i),
\]
one gets
\[
\boxed{A_a=-cW_0,\qquad B_a=iW_\pi.}
\]
Both are real entire by the sharp identities.

Thus the theta=0 and theta=pi self-adjoint characteristics are exactly the real A/B components of the finite de Branges generator, up to fixed real factors.

## 6. Interlacing qualification

For a simple symmetric operator with deficiency indices (1,1), spectra of distinct self-adjoint extensions interlace on intervals where the scalar Weyl function is strictly monotone, and common eigenvalues can only arise from a self-adjoint reducing part.

Suzuki's defect-vector construction is intended to describe the simple part. Therefore the safe statement is:
\[
\boxed{\text{zeros of }W_0\text{ and }W_\pi\text{ interlace on the simple scalar boundary-triple sector}.}
\]
This is slightly more precise than an unconditional blanket "all zeros simple and interlace" if simplicity of the entire symmetric operator has not separately been proved.

Suzuki does state that every eigenvalue of each finite self-adjoint extension has multiplicity one, which supports the simple-spectrum side.

## 7. Verdict on v13.673

PASS:
- sharp identities: exact under canonical real/reflection phase;
- corrected sign inherited from v13.672: confirmed by v13.675;
- HB inequality: exact;
- Schur transform: exact;
- A/B decomposition: exact.

Qualification:
- explicitly state the real/reflection phase normalization;
- phrase interlacing on the simple scalar sector unless a separate irreducibility/simplicity theorem for the minimal operator is cited.

## 8. Next gate

Now that the source and sign issues are stabilized, proceed to the convergence problem without further manipulating raw signs:
1. define the finite de Branges kernel
\[
K_a(w,z)=\frac{E_a(z)\overline{E_a(w)}-E_a^\sharp(z)\overline{E_a^\sharp(w)}}{2\pi i(\bar w-z)};
\]
2. express it purely through W_pi and the Weyl function m_a;
3. compare it to the abstract gamma-field kernel
\[
\frac{m_a(z)-\overline{m_a(w)}}{z-\bar w};
\]
4. determine the exact positive scalar/gauge relating the two RKHSs.

This will tell us whether the finite energy space itself is already a de Branges space after the canonical defect transform, rather than merely producing one HB function.
