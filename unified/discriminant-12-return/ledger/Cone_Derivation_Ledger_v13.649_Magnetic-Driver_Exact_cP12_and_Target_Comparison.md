# Cone Derivation Ledger v13.649 — Exact Magnetic-Driver c_P,12 and Independent Target Comparison

Date: 2026-09-22

## 0. Collision/relevance check

The live ledger was checked before work and immediately before this write. v13.648 is the latest numbered entry and independently confirms the magnetic g^9/g^10 and epsilon^9/epsilon^10 work. The magnetic five-term residual audit was renumbered by the external audit from v13.644 to authoritative v13.645. v13.649 is free.

## 1. Exact Dyson-log extension

Extending the same exact spin-1/2 Dyson recursion to order 12 and reducing the one-fast-period SU(2) logarithm gives
[
oxed{h_x^{(11)}={8445707over83494164234240}{g^{11}overomega^{10}}},
]
[
oxed{h_z^{(12)}={31839895957over601157982486528000}{g^{12}overomega^{11}}}.
]
The established parity remains: order 11 is transverse J_x, order 12 longitudinal J_z, with no J_y term.

For H_F=-(g/2)(A J_x+ZJ_z),
[
a_{10}=-{8445707over41747082117120},
qquad
z_{11}=-{31839895957over300578991243264000}.
]

## 2. Exact c_P,12(j)

Using
[
P_{1/2}={A^2over F^2}sin^2{pi Fover2},qquad F=sqrt{A^2+Z^2},qquad P_j=P_{1/2}^{2j},
]
and expanding at fixed j through epsilon^12 gives
[
oxed{
c_{P,12}(j)=
-{jover38474110879137792000},mathcal P_{12}(j)
}
]
where
[
egin{aligned}
mathcal P_{12}(j)={}&
49766400j^5
-(7091712000+46656000pi^2)j^4\
&+(288209664000+3265920000pi^2+8748000pi^4)j^3\
&-(3702734208000+50373900000pi^2+198288000pi^4+182250pi^6)j^2\
&+(11838767040000+148043700000pi^2+487154250pi^4+91125pi^6)j\
&-3503587381952-25046556750pi^2-75724875pi^4-12150pi^6.
end{aligned}
]

Thus the fixed-j inversion expansion advances to
[
1-P_j^{inv}=sum_{r=1}^{6}c_{P,2r}(j)epsilon^{2r}+O(epsilon^{14}).
]

## 3. Comparison with pre-existing v13.645 targets

The exact analytic values are:

| j | analytic c_P,12(j) | v13.645 target | analytic-target |
|---:|---:|---:|---:|
| 1/2 | -2.4696971840026137e-8 | -2.46969713073e-8 | -5.33e-16 |
| 1 | -1.4772696072189282e-7 | -1.47726959691e-7 | -1.03e-15 |
| 3/2 | -3.0471906713777965e-7 | -3.04719066730e-7 | -4.08e-16 |

All three independently pre-existing high-precision targets agree with the exact analytic coefficient to the precision expected from the one-step Richardson estimates recorded in v13.645. The nonlinear j-dependence is also reproduced.

This is a genuine out-of-sample validation: the v13.645 targets were generated before h_x^(11), h_z^(12), a_10, z_11, or the analytic c_P,12(j) existed and were not used to derive any of them.

## 4. Reproducer

`research-notes/magnetic_driver_cP12_exact_v13_649.py`

## 5. Promotion and guardrails

Promoted: exact h_x^(11), h_z^(12), a_10, z_11 and c_P,12(j) above, plus their agreement with the pre-existing v13.645 fixed-j numerical targets.

Guardrails unchanged: fixed-j asymptotics; no uniform large-j remainder bound; no all-orders closed form; same bare-resonance stroboscopic protocol; generic nonstroboscopic endpoints require micromotion kicks. This entry does not yet promote c_phi,11(j).
