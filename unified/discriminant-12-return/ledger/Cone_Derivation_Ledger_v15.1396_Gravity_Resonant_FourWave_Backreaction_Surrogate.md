# Cone Derivation Ledger v15.1396 — Conserved resonant four-mode backreaction surrogate with explicit pump depletion

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [N PASS] deliberately selected finite-mode Hamiltonian permits nonzero EM growth while the internal pair loses equal occupation and the TT partner gains one; the full stipulated Hamiltonian and all four Manley–Rowe invariants remain constant to <1.5e-11; [NEGATIVE] not derived by projecting the covariant Weyl–Maxwell–H² action, so it **does not establish physical backreaction of the actual field theory**, the coupling coefficient remains assumed, and total Einstein–Maxwell–sigma energy transfer is not yet verified; [OPEN] actual covariant 4-point overlap, normalization, positive sigma energy, finite-packet backreaction, metric variation, physical quarter selector. Additive, no original scripts modified. External Audit Round 634 (SHA b2d0cd2adeb42cefb44c6c122ce7030d15825691) replayed v15.1391–1393, confirmed all physical tests, and identified a v15.1391 Ledger namespace collision. The prior packet ledger was restated canonically in v15.1395; its historical script and record remain untouched.

## Gate 1316 — isolate the energy-accounting question in a transparent resonant truncation

The phase-matched on-shell test v15.1389 admits kinematic four-wave mixing with two independent H² modes and a TT wave. A **consistent but not yet action-projected model** is the classical resonant Hamiltonian

`H=omega_A|A|²+omega_G|G|²+omega_U|U|²+omega_V|V|²+κ(A*G*UV+AGU*V*)`,

where A is EM, G is TT, and U,V are independent hyperboloid excitations. The interaction conserves total unperturbed occupation because it converts **one U and one V excitation into one A and one G excitation**. At the chosen unit-frequency exact resonance, all four omega=1, and in the co-rotating interaction picture the equations are

`i Adot=κ G*UV`, `i Gdot=κ A*UV`, `i Udot=κ AGV*`, `i Vdot=κ AGU*`.

Direct canonical variation of the stated real Hamiltonian yields these equations; they preserve the full Hamiltonian as well as

`N_A+N_U, N_A+N_V, N_G+N_U, N_G+N_V`.

Only three of the four Manley–Rowe invariants are algebraically independent. The physical magnitude and even presence of κ remain **independent free choices** here: an overlap of a specific normalized finite packet with the original Weyl–F–H² area operator has NOT been used to derive κ. We have not evolved the full Einstein/Matter system.

## Gate 1317 — actual independent numerical population transfer and controls

Using 4-component complex DOP853 solve_ivp, rtol 5e−12, atol 1e−13, initial complex amplitudes (A,G,U,V)=(0,1,1,1), κ=.05, the actually executed local source `/mnt/data/cone_gate/four_wave_backreaction_v15_1396.py` reported:

| Model t | κ | EM occupation | TT occupation | U occupation | V occupation | max Hamiltonian/Manley–Rowe error |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | .05 | .9932398486605482 | 1.993239848660652 | .006760151339487009 | .006760151339487009 | 1.3855139258112104e−11 |
| 15 | .05 | .44682685234591646 | 1.4468268523460448 | .5531731476538951 | .5531731476538951 | 1.3945733456921516e−11 |
| 30 | .025 | .44682685234594954 | 1.4468268523460721 | .5531731476538236 | .5531731476538236 | 1.4759748978576687e−11 |

At t=50, the unperturbed total occupation/energy remains 3.000000000000174; full conserved H differs by the same tiny numerical drift. Halving κ and doubling t reproduces population transfer at machine precision. With κ=0 the photon remains zero; with initial G=0 (and EM=0) it also remains exactly zero. Thus this **stipulated reduced interacting model** incorporates the opposite internal energy debit missing from v15.1392's one-way forced Maxwell mode and is numerically well-behaved on the tested finite interval.

Caution: a freely propagating TT physical field's occupation and a classical sigma field's finite-energy mode normalization require different actual action coefficients and Einstein constraints. They have not been matched to these unit-normalized toy amplitudes. The positive four-wave Hamiltonian evolution is a **consistency example**, not a derivation or certification of a physical gravitational backreaction term; nor does it establish an intrinsic quarter-dependent κ.

## Gate 1318 — executable and next genuinely physical test

**Additive committed reproducer:** `research-notes/k4_quarter_four_mode_backreaction_v15_1396.py`, SHA **759169cd50a72940a79d2d4653bec0864ee87001**; mathematical-equivalent compact version of the locally executed full script, exact committed-byte replay pending Audit. Actual local source above is separately verified in the container. The evolved ODE has four invariants, three independent, not a full stress-tensor divergence test.

**AUDIT:** independently derive the Hamilton equations and signs, assess invariant independence, run exact committed script and reproduce table, check free-mode phase convention, and distinguish physical TT energy from unit-normalized action-angle occupation. If a coefficient normalization inconsistent with the four-mode canonical action emerges, do not label this a physical spin/quarter prediction.

**NEXT:** derive the on-shell four-field coupling amplitude directly by spatial integration of the v15.1381 Weyl–F–H² area Lagrangian over **fully normalized** periodic/free packets, with the sigma f² kinetic and actual TT metric's EH quadratic normalization, then compare the overlap to this chosen κ. Only after fixing that coupling and determining full 4D variational stress, evolve a coupled finite-packet Maxwell+sigma+TT system and independently check total energy. The coefficient remains free under the exact radius/f reparameterization of v15.1387. A new physical Cone-only interaction is **not** established.
