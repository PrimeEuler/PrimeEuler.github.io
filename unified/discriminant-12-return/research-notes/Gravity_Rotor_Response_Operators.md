# Gravity lane — rank-1/rank-2 rotor response operators and the first G-free null test

*Dedicated Cone gravity lane, 2026-10-22. Separate from the Suzuki far-tail certification. Parents: v14.550, v14.620–632, v14.680, v14.696–699. Producer: \`gravity_rotor_response.py\`.*

Labels: **[D]** exact derivation; **[N]** reproducible numerical observation; **[I]** interpretation/correspondence; **[P]** physical prediction/null test.

Nothing here derives the numerical value of Newton's \(G\). The separatrix-logarithm and apex/initial-seat constructions of v14.696 are not used in this gate; they remain separate hypotheses whose gravitational/cosmological identifications require independent physical justification.

## 1. Model-separation correction to the rank-1 note [D/N]

v14.626 uses the matrix element
\[
\langle j+1,0|\cos\theta|j,0\rangle
=\frac{j+1}{\sqrt{(2j+1)(2j+3)}}.
\]
That is the standard **3-D spherical rigid-rotor** result in the \(|j,m=0\rangle\) basis, whose free spectrum is
\[
E_j/B=j(j+1),\qquad B=\hbar^2/(2I_{\rm kin}).
\]

But v14.626 §4 diagonalized
\[
-\partial_\theta^2-\beta\cos\theta
\]
on a circle. That is the **planar rotor / Mathieu** model, with free spectrum \(n^2\) and the \(\pm n\) doublets
\(0,1,1,4,4,9,\ldots\).

Both are legitimate models, but they are not the same Hilbert space or free Hamiltonian. The Wigner/Legendre weights of v14.626 §2 and v14.630 therefore cannot be combined with the numerical Mathieu spectrum of v14.626 §4 as one single rotor calculation.

The producer reproduces the quoted planar \(\beta=1\) values
\(-0.37848922,0.91805818,1.29316628,\ldots\), and separately the consistent spherical-\(m=0\) values
\(-0.15766348,2.09076065,6.02403165,\ldots\). In the deep well the planar first spacing tends to \(\sqrt{2\beta}\), while the fixed-\(m=0\) spherical spacing tends to \(2\sqrt{2\beta}\). [N]

**Disposition:** the already-audited Wigner/rank-2 identities remain correct. The correction is only that the planar spectrum is a separate model.

## 2. One consistent 3-D rotor: rank-1 and rank-2 operators [D]

Define
\[
C=\cos\theta,\qquad P_2(C)=\frac{3C^2-1}{2}.
\]

In a fixed-\(m\) sector,
\[
C|j,m\rangle=a^+_{jm}|j+1,m\rangle+a^-_{jm}|j-1,m\rangle,
\]
with
\[
(a^+_{jm})^2=\frac{(j+1)^2-m^2}{(2j+1)(2j+3)},\qquad
(a^-_{jm})^2=\frac{j^2-m^2}{(2j-1)(2j+1)}.
\]

For \(m=0\), \(a^+_{j0}=w_j\) of v14.626. Since \(P_2=(3C^2-1)/2\),
\[
v_j=\langle j+2,0|P_2|j,0\rangle
=\frac32\,w_jw_{j+1},
\]
exactly the v14.630 identity. It is therefore ordinary angular-momentum algebra, not an additional Cone dynamical law.

The diagonal rank-2 element is
\[
d_{jm}:=\langle j,m|P_2|j,m\rangle
=\frac{j(j+1)-3m^2}{(2j-1)(2j+3)}
\]
for \(j>0\), with \(d_{00}=0\).

This is the standard Wigner-Eckart / spherical-harmonic product structure. DLMF §34.3(vii) expresses the same product and Gaunt-integral algebra with 3j symbols; standard multipole theory gives the corresponding rank-1/rank-2 selection rules. The Cone rotor sector reproduces that structure rather than modifying it.

## 3. Static response operators: exact cross-rank identity [D]

Use the dimensionless spherical Hamiltonian
\[
h=J^2/\hbar^2-\beta_1 C-\beta_2P_2(C).
\]

For \(j>0\), define the rank-1 second-order static response
\[
S_{jm}
=\langle jm|C\,Q(\epsilon_j-h_0)^{-1}Q\,C|jm\rangle,
\qquad \epsilon_j=j(j+1).
\]
Only \(j\pm1\) contribute:
\[
S_{jm}
=\frac{(a^-_{jm})^2}{2j}
-\frac{(a^+_{jm})^2}{2(j+1)}
=\frac{j(j+1)-3m^2}
{2j(j+1)(2j-1)(2j+3)}.
\]

Hence
\[
\boxed{d_{jm}=2j(j+1)S_{jm}}\qquad(j>0).
\]

Equivalently,
\[
\epsilon_{jm}(\beta_1,\beta_2)
=j(j+1)+\beta_1^2S_{jm}-\beta_2d_{jm}+\cdots,
\]
so
\[
\boxed{
-\left.\frac{\partial\epsilon_{jm}}{\partial\beta_2}\right|_0
=
j(j+1)
\left.\frac{\partial^2\epsilon_{jm}}{\partial\beta_1^2}\right|_0
}
\qquad(j>0).
\]

The \(j=0\) state is the expected exception: \(d_{00}=0\), while \(S_{00}=-1/6\).

This is a clean dimensionless response identity and could be measured as an internal rotor calibration/null relation. But it follows completely from the standard rigid-rotor spectrum and standard rank-1/rank-2 operators. It is **not a new gravitational prediction of the Cone**.

## 4. Physical rank-1/rank-2 ratio: a real G-free observable [D/P]

Now separate rotor algebra from the external field.

Let the rotor pivot be at radius \(R\) in a radial potential \(\Phi(R)\). Let:
- \(I_{\rm kin}\): kinetic moment of inertia;
- \(Ml\): pivot-to-centre-of-mass dipole moment;
- \(q\): axial quadrupole second-moment coefficient.

To quadrupole order, up to orientation-independent terms,
\[
U_1=Ml\,\Phi'(R)\cos\theta,
\]
\[
U_2=\frac{q}{3}
\left(\Phi''(R)-\frac{\Phi'(R)}{R}\right)P_2(\cos\theta).
\]

With positive \(\beta_1,\beta_2\) denoting the magnitudes of the Newtonian aligning terms,
\[
\beta_1=\frac{2I_{\rm kin}}{\hbar^2}Ml\,\Phi'(R),
\]
\[
\beta_2=\frac{2I_{\rm kin}}{\hbar^2}\frac{q}{3}
\left(\frac{\Phi'(R)}{R}-\Phi''(R)\right).
\]

Therefore
\[
\boxed{
\Xi(R)
=
\frac{MlR}{q}\frac{\beta_2}{\beta_1}
=
\frac{1-R\Phi''(R)/\Phi'(R)}{3}
=
\frac{1-d\ln g/d\ln R}{3}
}
\]
with \(g=\Phi'(R)\).

For a Newtonian point source, \(\Phi=-A/R\),
\[
\boxed{\Xi=1}
\]
exactly, independent of the amplitude \(A\). If \(A=GM_s\), both \(G\) and the source mass cancel.

More generally, for \(\Phi=-A/R^p\),
\[
\Xi=(p+2)/3.
\]

So \(\Xi\) is genuinely dimensionless, G-free, and experimentally distinguishable: it tests the **shape** of the radial field rather than its strength.

But this is the standard gravity-gradient/acceleration logarithmic-slope ratio written in rotor-spectroscopy variables. The Cone supplies a natural single-device representation through rank-1 and rank-2 channels, but **the observable is not theoretically new to the Cone framework**.

## 5. Geometry normalization: v14.630's \(I^2\) form is model-specific [D]

v14.630 wrote
\[
U_{\rm tidal}=-(GM_sI/R^3)P_2,\qquad
\beta_2=2GM_sI^2/(\hbar^2R^3).
\]

This is exact for an ideal slender axial dumbbell where the relevant quadrupole second moment equals the kinetic perpendicular moment. It is not universal for a finite double-paraboloid body.

For an axisymmetric body,
\[
A=\int z'^2\,dm,\qquad
B=\int x'^2\,dm=\int y'^2\,dm,
\]
so
\[
I_{\rm kin,\perp}=A+B,\qquad q=A-B.
\]
Only in the slender limit \(B=0\) does \(q=I_{\rm kin}\). Any real double-paraboloid implementation must calibrate \(q\) and \(I_{\rm kin}\) separately.

## 6. Research-objective verdict at this gate

**Mathematical identities [D].**
Rank-1/rank-2 weights are standard SO(3) algebra; \(v_j=\tfrac32w_jw_{j+1}\) is just \(P_2=(3C^2-1)/2\); the cross-rank response identity is exact; and \(\Xi=[1-R\Phi''/\Phi']/3\) is exact at dipole+quadrupole order.

**Numerical observations [N].**
The v14.626 Mathieu spectrum is reproduced by the planar rotor. The consistent spherical rotor has a different spectrum and a factor-of-two different deep-well fixed-\(m=0\) spacing.

**Interpretive correspondences [I].**
The paraboloid/fibre picture organizes the channels usefully, but their rank structure is ordinary angular momentum. The response identity can serve as a calibration/null check.

**Physical prediction [P].**
A single rotor carrying both calibrated dipole and quadrupole moments can measure \(\Xi\) without inserting \(G\). Newtonian \(1/R\) gives \(\Xi=1\); another radial law gives another value.

**Novelty verdict: negative.**
The first G-free observable produced by the rank-1/rank-2 rotor channel is experimentally meaningful, but it is equivalent to standard gradiometry. No Cone-specific dimensionless gravitational number or new tidal law has yet survived comparison with established angular-momentum and multipole theory.

## 7. Separate hypotheses preserved

The v14.696 **separatrix logarithm** remains mathematically valid as an elliptic-integral asymptotic, but its identification with a gravitational/cosmological hierarchy is a separate physical hypothesis. This gate neither uses nor strengthens that identification.

The v14.696 **apex/initial-seat construction** remains an interpretive initial-condition hypothesis. No rotor-response calculation here derives the seat, fixes its value, or turns it into \(G\).

## 8. Next gates

The next mathematical gravity gate should construct the response from the **actual cone phase-integral dynamics** of v14.680 rather than assume the ordinary rigid-rotor Hamiltonian, and ask whether any correction survives reduction to standard Wigner-Eckart/multipole theory.

The parallel experimental gate should test whether one physical rotor can resolve both \(\beta_1\) and \(\beta_2\) precisely enough for \(\Xi\) to compete with ordinary gradiometry, including uncertainty in \(l,q,I_{\rm kin},R\), source geometry, and Earth-gradient background.
