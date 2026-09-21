# Cone Derivation Ledger v13.611 — chi_-4 Zeeman Characteristic Zero-Branch Test

Date: 2026-09-21

Status: first falsifiable zero-comparison experiment; current naive Zeeman nodal characteristic FAILS the interval-scale robustness gate. No zero-convergence or GRH claim.

## 0. Mandatory pre-commit collision/relevance check

The live ledger was re-fetched immediately before this write. Highest entry is v13.610; v13.611 is free.

External Audit Round 64 (v13.609) is newly relevant and was read before proceeding. It independently executed and verified both chi_-4 scripts through v13.610, including the reflection deficiency residual at approximately 1.29e-15. It also confirms the intended next gate is exactly the zero-branch experiment performed here.

No collision with the magnetic-driver lane affects this calculation.

## 1. Independent target zeros

For
[
L(s,chi_{-4})=eta(s),
]
compute the real critical-line completed function
[
Lambda_{-4}(1/2+it)
=
(4/pi)^{(3/2+it)/2}
Gamma(3/4+it/2),
eta(1/2+it).
]

Independent high-precision sign bracketing/root refinement gives the first ten positive ordinates

[
egin{aligned}
gamma_1&=6.020948904698,\
gamma_2&=10.243770304167,\
gamma_3&=12.988098012312,\
gamma_4&=16.342607104587,\
gamma_5&=18.291993196124,\
gamma_6&=21.450611343983,\
gamma_7&=23.278376520460,\
gamma_8&=25.728756425089,\
gamma_9&=28.359634343025,\
gamma_{10}&=29.656384014593.
end{aligned}
]

These are target data only; they are not inserted into the finite operator.

## 2. Real finite characteristic

The v13.610 reflection relation makes
[
W_j^{(-4)}(pi;z)
]
purely imaginary on real z in the chosen gauge, up to roundoff. Therefore its real-axis zeros can be located by sign changes of
[
operatorname{Im}W_j^{(-4)}(pi;z).
]

The experiment tracks the ordered finite roots themselves. It does **not** rematch each root to the nearest beta zero at each j.

## 3. Ordered root data

Representative first roots are:

### A=1.5

j=6:
[
2.209687, 4.387323, 6.231743, 8.562094, 10.453459, 12.589319,ldots
]

j=20:
[
2.167772, 4.365377, 6.148568, 8.588508, 10.387908, 12.929322,ldots
]

### A=2.0

j=6:
[
1.664735, 3.248150, 4.932630, 6.172837, 8.105189, 9.483816, 10.833436, 12.725666,ldots
]

j=20:
[
1.618012, 3.237590, 4.926037, 6.127822, 7.971235, 9.942480, 10.884942, 12.894358,ldots
]

### A=2.5

j=6:
[
1.323505, 2.587228, 3.882115, 5.063274, 6.174114, 7.576635, 8.944351, 10.121314,ldots
]

j=20:
[
1.284712, 2.570572, 3.872739, 5.214987, 6.109931, 7.625684, 8.857293, 10.214727,ldots
]

## 4. A tempting local signal and why it is not enough

Every tested A has a finite root near the first beta ordinate 6.0209489, and increasing j moves that nearby root somewhat toward the target:

- A=1.5: ordered branch 3, 6.231743 -> 6.148568;
- A=2.0: ordered branch 4, 6.172837 -> 6.127822;
- A=2.5: ordered branch 5, 6.174114 -> 6.109931.

Likewise some higher finite roots can lie near higher beta zeros.

But the **ordered branch number changes with A**. The near-6 root is branch 3, 4, and 5 for A=1.5,2.0,2.5 respectively. This is already incompatible with interpreting a fixed ordered finite branch as an A-independent zero index.

## 5. Interval-scale robustness gate fails

The low finite roots scale strongly with the box length:

[
r_1(A=1.5,j=20)=2.167772,
]
[
r_1(A=2.0,j=20)=1.618012,
]
[
r_1(A=2.5,j=20)=1.284712.
]

The approximate (1/A) movement and the increasing number of finite roots below a fixed physical ordinate show a strong finite-interval/Fourier-box spectrum.

Thus the requested fail-closed criterion triggers:

[
oxed{	ext{the current naive Zeeman nodal characteristic does not pass the A-robust zero-indexing test.}}
]

The isolated approach of a root near (gamma_1) cannot yet be interpreted as L-zero convergence because which ordered root supplies that match changes as A changes.

## 6. Interpretation

This is a useful negative result, not a failure of the chi_-4 arithmetic kernel itself.

The experiment distinguishes two layers:

1. the chi_-4 Suzuki screw kernel and finite deficiency construction remain internally consistent;
2. the present direct Jz-node quadrature compression retains strong box modes, so its raw theta=pi finite characteristic has not yet isolated an A-independent L-zero branch.

This is exactly why v13.610 required multiple A values rather than a single visually favorable comparison.

## 7. Reproducer

Added
`research-notes/suzuki_chi4_zeeman_zero_branch_test.py`.

It independently computes the beta critical-line target zeros, locates all finite real characteristic roots in a fixed window, and prints the ordered roots for

[
A=1.5,2.0,2.5,qquad
j=6,10,15,20.
]

## 8. Next mathematical gate

Do not tune A to force matches.

The next useful question is whether Suzuki's **actual finite self-adjoint extension geometry** supplies an A-dependent phase/normalization or carrier map that removes these box branches before the infinite limit. Concretely:

1. reconstruct the finite boundary phase from the deficiency vectors instead of freezing theta=pi at every finite A;
2. compare scalar-normalized characteristics (W(A,	heta(A);z)/W(A,	heta(A);z_*));
3. test whether a canonical phase-covariant branch survives across A;
4. separately compare the Zeeman nodal compression against a source-faithful breakpoint-aware continuous/Galerkin discretization at the same A.

Only if one of those removes the observed (1/A) branch drift should the L-zero convergence test be resumed.
