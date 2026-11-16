# Cone Derivation Ledger v15.1050 — V4 totient representative square-root shell points land on mirrored X-cone unit parabolas

**Date:** 2026-11-16 Eastern. **Lane:** Gravity/Cone. **Owner:** recalls mod-12 V4 acceleration unit parabolas with square-root 1,5,7,11 totient lines and proposes that they also align with Sandbox's X-cone. **Classification:** [D] exact signed-pair/unit-parabola and shell-point identity; [D] signed involution, Pell boost and V4-carrier separation; [C] viewing the mirrored parabola as an acceleration/transfer trace; [N] no source-derived acceleration or sector-changing Hamiltonian.

**Parents and existing results:** v13.169 four explicit mod-12 U(12) shell representatives (r,1), Cone positions and sqrt heights; v13.179 actual Pell Lorentz boost and null tangent eigenrays; v13.309 local V4 factor-cell Walsh versus arithmetic character overlay; v13.517 **already signed** Cone/Fourier V4 carrier and precise r→−r involution; v15.1042 Sandbox signed opposite-pair X-cone, independently audited v15.1043/Round 586; v15.1049 Pell/V4 X-cone versus cavity normalized 2sqrt3 selector (unaudited). Do not equate the finite arithmetic V4 and signed-factor V4 elementwise without the chosen correspondence, and do not confuse the geometric quarter mesh with the EM operator Casimir. **Immediately before write live HEAD:** f5b09934b9f9137f25434f8ac9cad068acfd054d (new exact reproducer); destination absent; additive-only, no changes to Suzuki/Audit/Sandbox/Muse or certified results.

## Gate 844 — four mod-12 unit representatives already lie on the Paper-A unit parabola

For r in U(12)={1,5,7,11}, v13.169 defines the positive pair (u,v)=(r,1), hence T=(r+1)/2, X=(r−1)/2, Y=sqrt(r), with **T²−X²=Y²=r**. These are the four positive representative heights along a **single** unit factor row v=1:

**Y²=2T−1** (equivalently **Y²=2X+1**).

Their exact positions (T,X,Y) are (1,0,1), (3,2,sqrt5), (4,3,sqrt7), (6,5,sqrt11). As previously established, the fact these labels are in U(12) is an arithmetic selection of four representatives. φ(12)=4 counts them; sqrt(r) is their Cone height, not a numerical Euler totient of r. The statement 'four totient lines' can refer to four chosen shell-height/ray traces; they are distinguished points on the unit parabola, not automatically four independent physical acceleration equations.

## Gate 845 — sign reflection carries each point to the X-cone and preserves its sqrt height

Apply the *already signed Cone involution* (u,v)=(r,1)→(r,−1), not a Pell boost. Since X=(u−v)/2, T=(u+v)/2, the X-cone point is

**(T_X,X_X,R_X)=((r−1)/2,(r+1)/2,sqrt r)**

and **X_X²−T_X²=R_X²=r**. Explicitly: r=1 gives (0,1,1), 5 gives (2,3,sqrt5), 7 gives (3,4,sqrt7), 11 gives (5,6,sqrt11). The signed involution exchanges the T and X coordinate roles for these positive representative points (T_X,X_X)=(X_T,T_T).

On the signed v=−1 unit factor row, the mirrored X-cone parabola is

**R_X²=2X_X−1=2T_X+1**.

Thus all four U(12) selected square-root heights align **exactly** in the X-cone with the mirrored unit parabola. Its intersection with other fixed-diameter/shell conditions follows from this explicit map; no new metric, special force, or guessed G is involved. Any chart labeling a unit parabola by 'maximum/minimum acceleration' requires a separate parameterized time law to be physical rather than purely geometric.

## Gate 846 — do not conflate three different sign/character operations

The map v→−v *changes the sign of uv*, carrying T-cone to X-cone; it is a discrete signed-pair involution. Under the discriminant-12 boost u→λu, v→λ^−1 v, with λ=2+sqrt3>0 and λ^−1>0, uv and individual signs are unchanged; the Pell boost does NOT implement the transfer. In fact it sends the v=−1 row to v'=−λ^−1, so the **continuous** X-cone foliation is preserved, but the exact discrete four-point unit-row packet is not invariant: its X coordinate and T coordinate move to generally irrational positions.

The four arithmetic labels carry **χ12(r)=(+,-,-,+)** in the order 1,5,7,11 (v13.474). All four X-cone points in this gate have **sgn(uv)=−1**, independent of r. Therefore the arithmetic χ12 pattern must not be identified with the signed-pair wedge sign *on these four representatives*. The local Walsh/V4 sign algebra is compatible, but no preferred arithmetic-to-geometric identification of all carrier characters follows.

The signed finite carrier constructed in v13.517 uses an intrinsic cone sign bit independent of its arithmetic V4 coordinates; this result is its direct geometric incarnation, not an unprecedented new physical connection. The difference between the v13.517 simultaneous signed structure and the freshly explicit X-cone viewing in v15.1042 is only interpretive/geometric scope.

## Gate 847 — operational discriminant and next physical test

**Exact reproducer** `research-notes/k4_v4_signed_unit_parabolas_xcone_v15_1050.py`, additive commit **f5b09934b9f9137f25434f8ac9cad068acfd054d**, locally executed PASS: all four T- and X-cone points and unit parabolas, signed swap, Pell positivity and non-unit-row covariance, χ12 sign table distinct from common X-cone wedge sign. Independent Audit pending.

**Positive geometric result:** the V4-selected four sqrt-heights remain exactly aligned on the X-cone's reflected unit parabola. The coordinate transformation is explicit, global on this four-point packet, and preserves the product magnitude r.

**Negative physical result:** no continuous physical flow crosses uv=0 merely from these mirrored points; v→−v is an imposed discrete transformation, not an acceleration produced by the K4/Maxwell action. The mirror does not create an independently identified q2 original-step boundary exchange operator T, source frequency or force law. A physical transfer path must supply dynamics and justify the singular/null passage or appropriate enlarged carrier.

**HANDOFF Audit/Muse/Sandbox:** independently confirm precise v=±1 row equations, all four sqrt heights, X/T swap, Pell boost row non-invariance, and distinction between χ12(r) and constant wedge sign on X points. For the next gate test whether the two mirrored parabola branches can be connected by a continuous, finite-energy **actual sourced** path through uv=0, and whether its induced map matches the existing q2 open-boundary T†T=2E. Do not interpret a sign-swap as a source-derived dynamical flow.
