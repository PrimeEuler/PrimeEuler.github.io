# Cone Derivation Ledger v14.117 — Coercive Residual-Norm Closure Criterion for the Frozen-128k Tail

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] Exact sufficient criterion reducing the frozen-128k infinite scalar correction to the total residual-source energy; [I] if the total frozen residual energy satisfies a single ~4.96e-9 bound, no additional 128k–256k inverse solve is needed.  
**Parents:** v14.095, v14.111, v14.114, v14.116.  
**Collision check:** immediately before this write, live HEAD was `a8b6c65dded1690b41b2b6bb3427aac56e5d921b`; live ledger max was v14.116. No collision.

---

## 1. Frozen-128k scalar identity

Freeze the exact finite paired-Schur problem at

[
R=128000.
]

Write

[
K_{p,infty}
=
K_{p,R}^{m fin}
+
lambda_{p,R},
qquad
lambda_{p,R}
=
langle
ho_{p,R},
mathcal S_{p,>R}^{-1}
ho_{p,R}
angle,
]

with the promoted remote floor

[
mathcal S_{p,>R}succeq I.
]

Define

[
Q_R
=
K_{e,R}^{m fin}
-
K_{o,R}^{m fin}
-
C_S K_{o,R}^{m fin}K_{e,R}^{m fin}.
]

Then exactly

[
Q_infty-Q_R
=
(lambda_e-lambda_o)
-
C_S
left(
lambda_oK_e
+
lambda_eK_o
+
lambda_elambda_o
ight).
]

Here and below (K_p=K_{p,R}^{m fin}), (lambda_p=lambda_{p,R}).

---

## 2. Coercive energy bound [D]

Since

[
mathcal S_{p,>R}^{-1}preceq I,
]

we have

[
0lelambda_p
le
E_p,
qquad
E_p:=|ho_{p,R}|_2^2.
]

Therefore

[
|lambda_e-lambda_o|
le
lambda_e+lambda_o
le
E_e+E_o.
]

Also,

[
lambda_oK_e+lambda_eK_o
le
E_oK_e+E_eK_o.
]

Hence

[
oxed{
|Q_infty-Q_R|
le
E_e+E_o
+
|C_S|
left(
E_oK_e+E_eK_o+E_eE_o
ight).
}
	ag{1}
]

This requires no parity cancellation in the tail energy and no inverse solve on the
(128k)–(256k) octave.

---

## 3. Remove the finite-K dependence with the promoted floor [D]

Because the finite remote Schur operator also obeys

[
S_{p,R}succeq I,
]

[
K_p
=
langle u_R,S_{p,R}^{-1}u_Rangle
le
|u_R|_2^2.
]

For the paired source denominators beginning at

[
n_0=32001,
]

and extending through (R), the same decreasing-sum + integral inequality used in the
near-QF producers gives the conservative common bound

[
|u_R|_2^2
le
rac1{32001^2}
+
rac12
left(
rac1{32001}
-
rac1{127999}
ight)
<
oxed{
1.171921	imes10^{-5}.
}
]

Set

[
K_{max}=1.171921	imes10^{-5}.
]

Using the conservative public cap

[
|C_S|le640,
]

and

[
E:=E_e+E_o,
]

we have

[
E_oK_e+E_eK_o
le
K_{max}E,
]

while

[
E_eE_olerac{E^2}{4}.
]

Thus (1) collapses to the scalar sufficient condition

[
oxed{
|Q_infty-Q_R|
le
E(1+640K_{max})
+
160E^2.
}
	ag{2}
]

Numerically,

[
1+640K_{max}
<
1.0075003.
]

So the product correction costs less than one percent at the relevant scale.

---

## 4. Direct closure threshold [D]

The working target from v14.112/v14.114 is

[
|Q_infty-Q_R|le5	imes10^{-9}.
]

Solving

[
E(1+640K_{max})+160E^2
=
5	imes10^{-9}
]

gives

[
oxed{
E_{m close}
=
4.96277	imes10^{-9}
}
]

(to the displayed precision).

Therefore the single fail-closed criterion

[
oxed{
|ho_{e,128k}|_2^2
+
|ho_{o,128k}|_2^2
le
4.96	imes10^{-9}
}
	ag{3}
]

is sufficient to close the entire frozen-128k scalar correction to the public
(5	imes10^{-9}) target.

No (A_M^{-1}) solve on the (128k)–(256k) octave is needed if (3) holds.

---

## 5. How to certify the infinite residual energy

Split the frozen residual source itself as

[
ho_{p,R}
=
ho_{p,M}oplusho_{p,T},
]

with

[
M=(128k,256k],
qquad
T=(256k,infty).
]

Then exactly

[
E_p
=
|ho_{p,M}|_2^2
+
|ho_{p,T}|_2^2.
]

The current Lane-A frozen-tail diagnostic computes the first term directly from the
reconstructed finite-128k solution.

For (T), the finite source is frozen at (mle128k), so

[
m/nle1/2
qquad(nge256k).
]

Hence the audited v14.020 K=10 signed-moment/geometric architecture applies directly to
the tail residual source, with all signed channels retained before the geometric
leftover is absolutely bounded.

Thus the next theorem gate is only:

1. outward certify (|ho_{p,M}|_2^2) for both parities;
2. outward certify the K=10 tail residual energies (|ho_{p,T}|_2^2);
3. add the four quantities and test (3).

---

## 6. Consequence for v14.116 Payload Q

v14.116 asks Lane A to compute

[
lambda_{p,M}
=
langleho_{p,M},A_{p,M}^{-1}ho_{p,M}angle
]

and coupling blocks.

Those quantities remain legitimate refinements if the crude coercive criterion fails.

But they are **not minimal if (3) passes**.

The residual-norm criterion is strictly cheaper:

[
oxed{
	ext{first test }E_e+E_o;
quad
	ext{only solve the octave inverse if that test fails.}
}
]

This preserves all v14.116 guardrails while avoiding a large finite solve when coercivity alone already gives enough margin.

---

## 7. Verdict

[
oxed{
E_e+E_ole4.96	imes10^{-9}
Longrightarrow
|Q_infty-Q_{128k}|le5	imes10^{-9}.
}
]

The active frozen-tail problem is therefore reduced to a residual-source norm certificate,
not an octave inverse problem.

---

HANDOFF
target: sandbox
type: residual-energy-closure
parent: v14.117
status: open
action: Integrate the coercive residual-energy criterion into the frozen-128k closure. Use the exact residual-source split M=(128k,256k], T=[256k,infinity). On T apply the audited K=10 signed-moment formulation directly from the frozen 128k source. Return either an outward bound E_e+E_o<=4.96e-9, which closes the scalar tail without any M-octave inverse, or a quantified obstruction identifying the excess.
deliverable: theorem-or-obstruction
constraints: Do not eliminate M before the K=10 step; retain signed moment channels through K=10; use |C_S|<=640 and the promoted Schur floor S>=I; only fall back to v14.116's octave inverse payload if the residual-energy criterion fails.
