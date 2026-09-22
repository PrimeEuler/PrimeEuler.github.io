# Driven-Spin Analog Simulation of the Flattened Tetrahedral Orientation Carrier at j=3/2

## Standalone research note

**Status.** Exact finite-dimensional analog-simulation construction opened by the audit addendum v13.638. This note uses the closed flattened-D8 theorem of v13.624/v13.631/v13.636 as an input but is a separate investigation. It does not identify magnetic dynamics with the raw tetrahedral volume dynamics.

## 1. Target

For j=3/2, let

[
L_Y=2J_x
]

in the ordered J_z basis

[
(|-3/2angle,|-1/2angle,|1/2angle,|3/2angle).
]

Then

[
L_Y=
egin{pmatrix}
0&sqrt3&0&0\
sqrt3&0&2&0\
0&2&0&sqrt3\
0&0&sqrt3&0
end{pmatrix},
]

with spectrum {-3,-1,1,3}. Define

[
H=operatorname{diag}(1,-1,1,-1)
]

and

[
R_Y=H,operatorname{sgn}(2J_x).
]

Since sign(x) on x=+-1,+-3 is represented exactly by

[
operatorname{sgn}x=rac{13}{12}x-rac1{12}x^3,
]

one finds

[
operatorname{sgn}(2J_x)=
egin{pmatrix}
0&rac{sqrt3}{2}&0&-rac12\
rac{sqrt3}{2}&0&rac12&0\
0&rac12&0&rac{sqrt3}{2}\
-rac12&0&rac{sqrt3}{2}&0
end{pmatrix},
]

hence

[
R_Y=
egin{pmatrix}
0&rac{sqrt3}{2}&0&-rac12\
-rac{sqrt3}{2}&0&-rac12&0\
0&rac12&0&rac{sqrt3}{2}\
rac12&0&-rac{sqrt3}{2}&0
end{pmatrix}.
]

Exactly,

[
R_Y^T=-R_Y,qquad R_Y^2=-I_4.
]

The tetrahedral flattened carrier is

[
R_a=-i,operatorname{sgn}(Q_a).
]

The question is whether a driven spin can realize R_Y, and then whether the explicit flattened-carrier intertwiner can transport that control to R_a.

## 2. Zeeman-only no-go

Any purely magnetic Zeeman Hamiltonian has the form

[
H_{m mag}(t)=h_x(t)J_x+h_y(t)J_y+h_z(t)J_z.
]

Because

[
[J_a,J_b]=iepsilon_{abc}J_c,
]

the dynamical Lie algebra closes on su(2). Therefore, for arbitrary time dependence, including circular or linear single-tone driving and all exact time ordering,

[
U_{m mag}(t)in D^{(3/2)}(SU(2)).
]

The no-go is therefore stronger than a failure of a parameter search: R_Y would have to belong, up to scalar phase, to the spin-3/2 image of SU(2).

Write a fundamental SU(2) matrix as

[
g=egin{pmatrix}alpha&eta\-eta^*&alpha^*end{pmatrix},
qquad |alpha|^2+|eta|^2=1.
]

In the symmetric-cube spin-3/2 representation, the extremal matrix elements satisfy

[
|D^{(3/2)}_{-3/2,-3/2}(g)|=|alpha|^3,
]

[
|D^{(3/2)}_{-3/2,+3/2}(g)|=|eta|^3.
]

But the target R_Y has

[
(R_Y)_{-3/2,-3/2}=0,
]

forcing alpha=0 and therefore |beta|=1. A spin-3/2 rotation would then require

[
|D^{(3/2)}_{-3/2,+3/2}|=1,
]

whereas

[
|(R_Y)_{-3/2,+3/2}|=rac12.
]

Contradiction. Thus

[
oxed{R_Y
otin e^{iphi}D^{(3/2)}(SU(2)).}
]

Consequences:

[
oxed{	ext{single-tone circular Zeeman drive cannot realize }R_Y,}
]

[
oxed{	ext{single-tone linear Zeeman drive cannot realize }R_Y,}
]

and in fact

[
oxed{	ext{arbitrary time-dependent Zeeman-only control cannot realize }R_Y.}
]

Counter-rotating and Floquet corrections do not remove this obstruction: nested commutators of linear spin generators remain in su(2).

The obstruction is not spectral. R_Y has eigenvalues {+i,+i,-i,-i}, which are compatible with a pi spin rotation. The obstruction is the stronger matrix-element geometry of the spin-3/2 representation.

## 3. Minimal nonlinear extension and exact pulse

Introduce

[
X(	heta)=e^{-i	heta J_x},qquad
Z(	heta)=e^{-i	heta J_z},qquad
Q_x(kappa)=e^{-ikappa J_x^2}.
]

Since J_x commutes with J_x^2,

[
X(pi)Q_x(pi/2)
=
exp[-i(pi J_x+rac{pi}{2}J_x^2)].
]

For m_x=+-1/2,+-3/2, direct evaluation gives

[
exp[-i(pi m_x+rac{pi}{2}m_x^2)]
=
egin{cases}
e^{3ipi/8},&m_x<0,\
e^{-5ipi/8},&m_x>0.
end{cases}
]

Therefore

[
oxed{
X(pi)Q_x(pi/2)
=
e^{-5ipi/8}operatorname{sgn}(2J_x).
}
]

Also

[
e^{ipi J_z}=iH,
]

so

[
H=-iZ(-pi).
]

Combining the factors,

[
oxed{
R_Y=e^{ipi/8}Z(-pi)X(pi)Q_x(pi/2).
}
]

Thus the raw three-pulse propagator is

[
oxed{
U_{m pulse}^{(Y)}
=
Z(-pi)X(pi)Q_x(pi/2)
=
e^{-ipi/8}R_Y.
}
]

Because the two x-axis controls commute, simultaneous linear and quadratic x control reduces this to two stages:

[
U_{xQ}
=
exp[-i(pi J_x+rac{pi}{2}J_x^2)],
]

followed by

[
U_z=Z(-pi).
]

Then

[
oxed{U_zU_{xQ}=e^{-ipi/8}R_Y.}
]

A quadratic term is therefore sufficient to escape the Zeeman SU(2) subgroup and synthesize the flattened carrier exactly. This establishes sufficiency of a nonlinear quadratic control; it is not a general time-optimality theorem over every conceivable enlarged control algebra.

## 4. Explicit j=3/2 tetrahedral flattened carrier

For the volume carrier define

[
p=sqrt{rac{11+sqrt{105}}{30}},
qquad
q=sqrt{rac{19-sqrt{105}}{30}},
]

so p^2+q^2=1. The exact flattened tetrahedral quarter-turn is

[
R_a=
egin{pmatrix}
0&-p&0&-q\
p&0&-q&0\
0&q&0&-p\
q&0&p&0
end{pmatrix}.
]

It obeys

[
R_a^2=-I_4,qquad HR_aH=R_a^{-1}.
]

## 5. Natural O(2) gauge and explicit intertwiner

For j=3/2 the positive-parity multiplicity space has dimension N_j=2, so the parity-adapted intertwiner has O(2) freedom.

A natural reference gauge fixes the same ordered even basis (e_0,e_2) in both carriers and generates odd partners by R_Y and R_a.

Define

[
c=rac{q-sqrt3p}{2},
qquad
d=rac{p+sqrt3q}{2}.
]

Then c^2+d^2=1, and an explicit orthogonal intertwiner is

[
oxed{
U_{aleftarrow Y}^{(0)}
=
egin{pmatrix}
1&0&0&0\
0&c&0&d\
0&0&1&0\
0&-d&0&c
end{pmatrix}.
}
]

It satisfies

[
(U^{(0)})^TU^{(0)}=I,
qquad
U^{(0)}H=HU^{(0)},
]

and

[
oxed{U^{(0)}R_Y(U^{(0)})^T=R_a.}
]

## 6. Transported generator

Define

[
K_a^{(0)}=U^{(0)}J_x(U^{(0)})^T.
]

Then

[
oxed{
K_a^{(0)}
=
rac14
egin{pmatrix}
0&sqrt3q-3p&0&-sqrt3p-3q\
sqrt3q-3p&0&5q-sqrt3p&0\
0&5q-sqrt3p&0&-5p-sqrt3q\
-sqrt3p-3q&0&-5p-sqrt3q&0
end{pmatrix}.
}
]

As an orthogonal conjugate of J_x,

[
operatorname{spec}K_a^{(0)}
=
{-3/2,-1/2,1/2,3/2},
]

and

[
HK_a^{(0)}H=-K_a^{(0)}.
]

The transported exact protocol is

[
oxed{
R_a
=
e^{ipi/8}
Z(-pi)
exp[-i(pi K_a+rac{pi}{2}K_a^2)].
}
]

The parity pulse is unchanged because every allowed flattened-carrier intertwiner commutes with H and Z(-pi)=iH.

Thus

[
oxed{
U_{m pulse}^{(a)}
=
Z(-pi)
exp[-i(pi K_a+rac{pi}{2}K_a^2)]
=
e^{-ipi/8}R_a.
}
]

Since R_a=-i sign(Q_a),

[
oxed{
U_{m pulse}^{(a)}
=
e^{-i5pi/8}operatorname{sgn}(Q_a).
}
]

This implements the **orientation sign** of the tetrahedral volume, not its metric eigenvalue magnitudes.

## 7. O(2) gauge optimization

The reference intertwiner is not unique. Parameterize the connected SO(2) part of the multiplicity-space freedom by

[
O(	heta)=
egin{pmatrix}
cos	heta&-sin	heta\
sin	heta&cos	heta
end{pmatrix}.
]

Rotating the even parity basis by O(theta), and generating the corresponding odd partners by R_a, gives the full connected family U(theta). Let

[
K_a(	heta)=U(	heta)J_xU(	heta)^T.
]

The endpoint coupling is exactly

[
oxed{
(K_a(	heta))_{03}
=
-q+
rac{q-sqrt3p}{4}cos2	heta
+
rac{p+sqrt3q}{4}sin2	heta.
}
]

The oscillatory amplitude collapses to

[
left(rac{q-sqrt3p}{4}ight)^2+
left(rac{p+sqrt3q}{4}ight)^2
=
rac14.
]

Hence

[
(K_a(	heta))_{03}
=
-q+rac12cos(2	heta-delta),
]

where

[
cosdelta=rac{q-sqrt3p}{2},
qquad
sindelta=rac{p+sqrt3q}{2}.
]

Because

[
q=sqrt{rac{19-sqrt{105}}{30}}
approx0.540155818076>rac12,
]

no gauge can eliminate the endpoint coupling.

The optimum occurs at

[
oxed{
	heta_{min}
=
rac12operatorname{atan2}
(p+sqrt3q, q-sqrt3p)
pmod{pi},
}
]

numerically

[
	heta_{min}approx1.02368581342
	ext{ rad}
approx58.6528767^circ.
]

At the optimum,

[
oxed{
(K_a)_{03}^{m opt}
=
-q+rac12,
}
]

so

[
oxed{
min_{Oin O(2)}|(K_a)_{03}|
=
q-rac12
=
sqrt{rac{19-sqrt{105}}{30}}-rac12
approx0.040155818076.
}
]

The disconnected det(O)=-1 component gives the same lower bound. Therefore the result is over the full O(2), not merely SO(2).

The endpoint coupling is thus gauge-dependent in magnitude but cannot be gauged away. A nonzero 0<->3 term is intrinsic to every parity-adapted intertwiner that transports the magnetic flattened carrier to the tetrahedral one.

## 8. Result

For j=3/2:

[
oxed{
egin{aligned}
&	ext{Zeeman-only control cannot realize }R_Y;\
&	ext{this remains true for circular, linear, and arbitrary time-dependent Zeeman drives;}\
&J_x^2	ext{ control is sufficient for an exact two-stage synthesis;}\
&R_Y=e^{ipi/8}Z(-pi)e^{-i(pi J_x+rac{pi}{2}J_x^2)};\
&R_a=U_{aleftarrow Y}R_YU_{aleftarrow Y}^T;\
&R_a=e^{ipi/8}Z(-pi)e^{-i(pi K_a+rac{pi}{2}K_a^2)};\
&min_{O(2)}|(K_a)_{03}|
=sqrt{rac{19-sqrt{105}}{30}}-rac12>0.
end{aligned}}
]

The analog-simulation target is therefore exact at the flattened orientation level, while a residual nonlocal endpoint control survives every allowed O(2) gauge.

## 9. Guardrails

1. This protocol simulates the flattened orientation carrier R_a, equivalently sign(Q_a) up to a known global phase. It does not reproduce the raw tetrahedral volume spectrum.
2. It does not contradict the raw spectral inequivalence theorem of v13.624; it depends on flattening.
3. The no-go applies to Hamiltonians linear in the spin generators. Adding nonlinear control changes the dynamical Lie algebra.
4. Quadratic J_x^2 control is proved sufficient here; no universal hardware-minimal or time-optimal claim is made.
5. The transported generator K_a depends on O(2) gauge, but the optimized nonzero endpoint lower bound above is gauge-invariant over the allowed family.
6. This note does not establish a link to the chi_-4/L-function thread.
7. The separate high-order magnetic-driver Floquet expansion remains logically distinct. Its higher-order coefficients do not evade the Zeeman-only Lie-algebra obstruction.
8. No E8/golden-ratio spin-chain claim is derived here.

## 10. Provenance

The closed representation-theoretic input is v13.624/v13.631/v13.636 and the standalone companion `Three_Weighted_Paths_and_the_Flattened_D8_Skeleton.md`. The external audit addendum v13.638 proposed the present analog-simulation question. The calculations in this note constitute the first explicit control-theoretic answer to that new gate.


## 11. Exact local-control refinement: endpoint-free eight-pulse synthesis

The O(2) result above proves that a direct endpoint term is unavoidable inside the one-generator transported construction (K_a=U J_xU^T). It does **not** prove that such a term is unavoidable for time-ordered local quadratic control. The latter question admits an exact constructive answer.

Define

[
X(a)=e^{-iaJ_x},qquad
Y(a)=e^{-iaJ_y},qquad
Q(a)=e^{-iaJ_z^2}.
]

For (j=3/2),

[
J_z^2=operatorname{diag}(9/4,1/4,1/4,9/4),
]

so, up to the scalar phase (e^{-ia/4}),

[
Q(a)sim overline Q(z)=operatorname{diag}(z,1,1,z),
qquad z=e^{-2ia}.
]

Start from the structured nine-factor ansatz

[
U=
Q(alpha_9)Y(-pi/2)X(-pi/2)
Q(alpha_6)Y(alpha_5)X(-pi/2)
Q(alpha_3)Y(pi/2)X(alpha_1).
]

### 11.1 Exact elimination of the apparent fifth angle

Impose

[
oxed{alpha_5=alpha_1-pi.}
]

Exact multiplication shows that the complete projective (4	imes4) product is then independent of (alpha_1). Write

[
z_3=e^{-2ialpha_3},qquad
z_6=e^{-2ialpha_6},qquad
z_9=e^{-2ialpha_9}.
]

After removing the scalar phases of the three (Q) factors,

[
overline U=
rac18
egin{pmatrix}
0&
sqrt3z_9(z_3z_6-3z_3+z_6+1)&
0&
z_9(z_3z_6-3z_3-3z_6-3)
\
sqrt3(z_3z_6+z_3-3z_6+1)&
0&
3z_3z_6+3z_3+3z_6-1&
0
\
0&
-3z_3z_6-3z_3-3z_6+1&
0&
sqrt3(-z_3z_6-z_3+3z_6-1)
\
z_9(-z_3z_6+3z_3+3z_6+3)&
0&
sqrt3z_9(-z_3z_6+3z_3-z_6-1)&
0
end{pmatrix}.
]

Thus the checkerboard support of (R_a) is already exact.

### 11.2 Algebraic phase solution

Set

[
oxed{z_9=-z_3.}
]

The required sign relations reduce to the single equation

[
z_3^2z_6-3z_3^2+3z_6-1=0,
]

hence

[
oxed{
z_6=rac{3z_3^2+1}{z_3^2+3}.
}
]

Now set

[
r=rac qp=
sqrt{rac{19-sqrt{105}}{11+sqrt{105}}}.
]

The amplitude ratio (U_{03}/U_{01}=q/p) reduces exactly to

[
oxed{
-sqrt3(3z^2+2z+3)=3r(z-1)^2,
qquad z=z_3.
}
]

Choose the unit-modulus root

[
oxed{
z=
rac{
r-rac1{sqrt3}
-rac{2i}{3}sqrt{6(sqrt3r+1)}
}
{r+sqrt3}.
}
]

Then

[
|z|=1.
]

Define

[
oxed{
w=rac{3z^2+1}{z^2+3}.
}
]

The same unit-circle relation gives

[
|w|=1.
]

Thus one may choose real (A,B,C) satisfying

[
e^{-2iA}=z,qquad
e^{-2iB}=w,qquad
e^{-2iC}=-z.
]

### 11.3 Exact matrix certificate

After substituting (z_3=z), (z_6=w), (z_9=-z), the product reduces identically to

[
oxed{overline U=sR_a,}
]

where

[
oxed{
s=
rac{sqrt3,z(z-1)^2}{2p(z^2+3)}.
}
]

The defining quadratic equation for (z), together with (|z|=1), gives

[
|s|=1.
]

Equivalently,

[
oxed{R_a^daggeroverline U=sI_4,}
]

or componentwise,

[
egin{aligned}
U_{00}=U_{02}=U_{11}=U_{13}
=U_{20}=U_{22}=U_{31}=U_{33}&=0,\
U_{01}=U_{23}&=-sp,\
U_{10}=U_{32}&=sp,\
U_{03}=U_{12}&=-sq,\
U_{21}=U_{30}&=sq.
end{aligned}
]

These are exact algebraic identities, not numerical fit residuals.

Restoring the scalar phases of the physical (Q) pulses gives

[
U_{m phys}=e^{iPhi}R_a
]

with

[
e^{iPhi}
=
e^{-i(A+B+C)/4}s.
]

### 11.4 Eight-pulse gauge

Because (alpha_1) is redundant once (alpha_5=alpha_1-pi), choose (alpha_1=0). The first (X) pulse disappears and (alpha_5=-pi).

An exact eight-pulse local sequence is therefore

[
oxed{
U_{m loc}
=
Q(C),
Y(-pi/2),
X(-pi/2),
Q(B),
Y(-pi),
X(-pi/2),
Q(A),
Y(pi/2)
=
e^{iPhi}R_a.
}
]

Every instantaneous generator is one of

[
J_x,qquad J_y,qquad J_z^2.
]

Each is diagonal or nearest-neighbor in the tetrahedral (k)-basis, so the Hamiltonian has no direct (0leftrightarrow3) matrix element at any stage.

Therefore

[
oxed{
	ext{direct endpoint coupling is not fundamentally required to implement }R_a.
}
]

The nonzero lower bound

[
min_{O(2)}|(U J_xU^T)_{03}|=q-rac12
]

is an obstruction only to the single transported-(J_x) realization. Time ordering of strictly local quadratic controls generates the endpoint amplitude dynamically.

### 11.5 Audit correction incorporated

External Audit Round 68 (v13.646) independently reconstructed the earlier transported protocol and found a transcription error in Section 6. The correct entries are

[
(K_a^{(0)})_{12}=rac{5q-sqrt3p}{4},
qquad
(K_a^{(0)})_{23}=-rac{5p+sqrt3q}{4},
]

not the previously printed coefficients 7. The corrected matrix is now used above. The transported exponential identity and the O(2)-optimized endpoint bound were independently verified by the audit and are unaffected by this correction.

## 12. Refined control conclusion

The (j=3/2) control picture is now:

[
oxed{
egin{array}{c|c}
	ext{control class}&	ext{status}\
hline
	ext{Zeeman-only, arbitrary time dependence}&R_Y	ext{ impossible}\
	ext{single transported }K_a=UJ_xU^T&R_a	ext{ exact, endpoint term unavoidable}\
	ext{local time-ordered }J_x,J_y,J_z^2&R_a	ext{ exact, no direct endpoint term}
end{array}}
]

Thus the endpoint coupling found in the transported-generator construction is genuine but not fundamental: it characterizes that realization, not the target flattened tetrahedral orientation carrier itself.
