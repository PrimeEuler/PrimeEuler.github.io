# Cone Derivation Ledger v13.643 — j=3/2 Driven-Spin Analog Simulation of the Flattened Tetrahedral Orientation Carrier

Date: 2026-09-22

Status: exact analog-simulation/control result. Opens the separate gate proposed by External Audit Addendum v13.638; does not modify the closed LQG/D8 synthesis v13.636.

## 0. Live collision and relevance check

The live ledger was fetched before packaging this result. The live tip was v13.642, `Magnetic-Driver_Endpoint_e9_e10`, and v13.643 was free.

Relevant intervening entries were checked:

- v13.639: exact magnetic-driver Dyson-log g^10 extension;
- v13.640: chi_-4 source-normalization certification;
- v13.641: free Friedrichs continuum/box obstruction;
- v13.642: magnetic-driver endpoint epsilon^9/epsilon^10 coefficients.

The magnetic entries v13.639/v13.642 extend the separate perturbative Floquet program. They do not collide with the present control-theoretic question. In particular, their higher-order Zeeman/Floquet coefficients remain inside the spin su(2) dynamical algebra and therefore do not evade the no-go proved below.

A standalone body-of-work note has also been created:

`research-notes/Driven_Spin_Analog_Simulation_of_Flattened_Tetrahedral_Orientation_j3_2.md`

This ledger entry records the promoted exact results and guardrails.

## 1. Target carrier

For j=3/2,

[
L_Y=2J_x,
qquad
H=operatorname{diag}(1,-1,1,-1),
]

and

[
R_Y=H,operatorname{sgn}(2J_x).
]

In the ordered J_z basis,

[
R_Y=
egin{pmatrix}
0&rac{sqrt3}{2}&0&-rac12\
-rac{sqrt3}{2}&0&-rac12&0\
0&rac12&0&rac{sqrt3}{2}\
rac12&0&-rac{sqrt3}{2}&0
end{pmatrix},
]

with

[
R_Y^T=-R_Y,qquad R_Y^2=-I_4.
]

## 2. Zeeman-only no-go

Any Zeeman Hamiltonian

[
H_{m mag}(t)=h_x(t)J_x+h_y(t)J_y+h_z(t)J_z
]

has dynamical Lie algebra su(2), so its exact propagator lies in

[
D^{(3/2)}(SU(2)).
]

For a fundamental SU(2) matrix with parameters alpha,beta,

[
|D^{(3/2)}_{-3/2,-3/2}|=|alpha|^3,
qquad
|D^{(3/2)}_{-3/2,+3/2}|=|eta|^3.
]

The target has zero diagonal extremal element, forcing alpha=0 and |beta|=1, which would force the opposite extremal element to have magnitude 1. Instead R_Y has magnitude 1/2 there. Hence

[
oxed{R_Y
otin e^{iphi}D^{(3/2)}(SU(2)).}
]

Therefore no single-tone circular or linear Zeeman drive can realize R_Y at any stroboscopic time. More strongly, no arbitrary time-dependent Zeeman-only control can realize it.

The obstruction is representation-geometric, not spectral: R_Y has eigenvalues {+i,+i,-i,-i}, compatible with a pi rotation, but its matrix elements are incompatible with the symmetric-cube SU(2) image.

## 3. Exact quadratic-control synthesis

Define

[
X(	heta)=e^{-i	heta J_x},
quad
Z(	heta)=e^{-i	heta J_z},
quad
Q_x(kappa)=e^{-ikappa J_x^2}.
]

Exact evaluation on m_x=+-1/2,+-3/2 gives

[
oxed{
X(pi)Q_x(pi/2)
=
e^{-5ipi/8}operatorname{sgn}(2J_x).
}
]

Also

[
Z(-pi)=e^{ipi J_z}=iH.
]

Therefore

[
oxed{
R_Y=e^{ipi/8}Z(-pi)X(pi)Q_x(pi/2).
}
]

The raw pulse propagator is

[
oxed{
U_{m pulse}^{(Y)}
=
e^{-ipi/8}R_Y.
}
]

Because [J_x,J_x^2]=0, simultaneous linear/quadratic x control combines the first two primitive pulses:

[
oxed{
U_{xQ}
=
exp[-i(pi J_x+rac{pi}{2}J_x^2)],
}
]

followed by Z(-pi). Thus quadratic control is sufficient for an exact two-stage realization.

## 4. Explicit flattened-carrier intertwiner

For the tetrahedral carrier define

[
p=sqrt{rac{11+sqrt{105}}{30}},
qquad
q=sqrt{rac{19-sqrt{105}}{30}}.
]

Then

[
R_a=
egin{pmatrix}
0&-p&0&-q\
p&0&-q&0\
0&q&0&-p\
q&0&p&0
end{pmatrix}.
]

Fix the natural reference O(2) gauge by identifying the ordered even basis (e_0,e_2) in the two carriers. Set

[
c=rac{q-sqrt3p}{2},
qquad
d=rac{p+sqrt3q}{2}.
]

Then

[
oxed{
U_{aleftarrow Y}^{(0)}
=
egin{pmatrix}
1&0&0&0\
0&c&0&d\
0&0&1&0\
0&-d&0&c
end{pmatrix},
}
]

with

[
(U^{(0)})^TU^{(0)}=I,
qquad
U^{(0)}H=HU^{(0)},
qquad
U^{(0)}R_Y(U^{(0)})^T=R_a.
]

## 5. Transported control generator

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

The transported exact sequence is

[
oxed{
R_a=
e^{ipi/8}
Z(-pi)
exp[-i(pi K_a+rac{pi}{2}K_a^2)].
}
]

Hence

[
oxed{
U_{m pulse}^{(a)}
=
e^{-ipi/8}R_a
=
e^{-i5pi/8}operatorname{sgn}(Q_a).
}
]

The parity pulse is unchanged under transport because U commutes with H.

## 6. O(2) gauge optimization and intrinsic endpoint coupling

For j=3/2, N_j=2 and the intertwiner has O(2) multiplicity-space freedom. Parameterize the connected component by O(theta). For the corresponding transported generator K_a(theta),

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

The oscillatory amplitude is exactly 1/2:

[
left(rac{q-sqrt3p}{4}ight)^2+
left(rac{p+sqrt3q}{4}ight)^2
=
rac14.
]

Since

[
q=sqrt{rac{19-sqrt{105}}{30}}
approx0.540155818076>rac12,
]

the endpoint coupling cannot vanish in any gauge.

A minimizing angle is

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
	heta_{min}approx1.02368581342 {m rad}
approx58.6528767^circ.
]

At this gauge,

[
(K_a)_{03}^{m opt}=-q+rac12,
]

and over the full O(2), including det(O)=-1,

[
oxed{
min_{Oin O(2)}|(K_a)_{03}|
=
q-rac12
=
sqrt{rac{19-sqrt{105}}{30}}-rac12
approx0.040155818076>0.
}
]

Thus a nonzero transported endpoint coupling is intrinsic to every parity-adapted flattened-carrier intertwiner, although its magnitude is gauge-dependent.

## 7. Promoted result

For j=3/2:

[
oxed{
egin{aligned}
&	ext{Zeeman-only control cannot realize }R_Y;\
&J_x^2	ext{ control is sufficient for an exact two-stage synthesis};\
&R_Y=e^{ipi/8}Z(-pi)e^{-i(pi J_x+rac{pi}{2}J_x^2)};\
&R_a=U_{aleftarrow Y}R_YU_{aleftarrow Y}^T;\
&R_a=e^{ipi/8}Z(-pi)e^{-i(pi K_a+rac{pi}{2}K_a^2)};\
&min_{O(2)}|(K_a)_{03}|
=sqrt{rac{19-sqrt{105}}{30}}-rac12>0.
end{aligned}}
]

This supplies an exact analog-simulation protocol for the **flattened tetrahedral orientation carrier**, together with a sharp control obstruction.

## 8. Guardrails

1. The simulated object is R_a, equivalently sign(Q_a) up to the stated global phase, not the raw tetrahedral volume spectrum.
2. No physical equivalence between magnetic dynamics and tetrahedral volume dynamics is asserted.
3. The result is compatible with and depends on the raw spectral inequivalence of v13.624.
4. The no-go applies to spin-linear Zeeman Hamiltonians; nonlinear control changes the dynamical Lie algebra.
5. Quadratic J_x^2 is proved sufficient, not universally hardware-minimal or time-optimal.
6. The O(2)-optimized endpoint lower bound is intrinsic to the allowed parity-adapted intertwiner family.
7. No chi_-4/L-function consequence is asserted.
8. v13.639/v13.642 remain the separate higher-order magnetic Floquet lane; their higher-order coefficients do not evade the Zeeman-only su(2) closure.
9. No E8/golden-ratio spin-chain conclusion is asserted.


## 9. Post-publication audit correction

External Audit Round 68 (v13.646) independently reconstructed this entry and found that the displayed static matrix in Section 5 contained a transcription error: the coefficients 7 in the (1,2)/(2,1) and (2,3)/(3,2) entries must be 5. The matrix above has been corrected accordingly. The audit independently verified that the transported exponential identity, the full O(2) gauge family, and the promoted endpoint lower bound are unaffected. See v13.646 for the independent reconstruction. A later exact local-control refinement is promoted separately in v13.650.
