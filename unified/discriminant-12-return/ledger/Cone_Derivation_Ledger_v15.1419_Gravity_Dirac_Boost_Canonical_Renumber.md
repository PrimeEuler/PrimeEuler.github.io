# Cone Derivation Ledger v15.1419 — The historical 45.310004305 G hierarchy as a boost on EM and q2 hyperboloids

**Date:** 2026-11-24 Eastern. **Canonical additive renumbering:** Audit Round 637 establishes earlier v15.1403 External Audit Round 636 had timestamp precedence. This v15.1419 is Gravity's canonical restatement of the historical Dirac-boost geometry; the original file, script v15_1403, results, and all prior commit SHAs remain unchanged. **Gravity/Cone.** **Status:** [D/N PASS] recover the user's historical "45.3 G hyperbolic boost point" as the *dimensionless Dirac-force-hierarchy rapidity* ψ_D=½ log(D) originally recorded v14.621, and lift the same boost onto the two distinct timelike representation-space observability hyperboloids, with exact Q invariance; [N NEGATIVE] measured D is the INPUT, so this does not compute G or independently select the rapidity; [D NEGATIVE] canonical divergence-free radial flux between hyperboloids requires a free normalization, and cannot select the 3:1 flat transverse annular partition without an independently specified current/measure. **Newest prior Audit:** Round 636 at 185e0ec14928f4823872c8b2ddf084b55bd7f4e4 independently verified v15.1401–1402. **Historical HEAD preceding original entry:** c4b9a9fec431683be89b0bea0a391920213dd1e4. Additive; all previous Gravity, Sandbox, Audit, Suzuki, Muse objects protected.

## Gate 1330 — recover what "45.3 G" actually meant

The historical Sandbox v14.621 `Cone_Derivation_Ledger_v14.621_Sandbox_Energy_AMGM_G_Ingredients.md` and `Energy_AM_GM_and_G_Ingredients_Addendum.md` defined

`D = e²/(4π ε0 G m_p m_e) = α(m_p/m_e)/α_G`, `α_G=Gm_p²/(ℏc)`,
`ψ_D=½ ln D = 45.3100043049815848428710843316`, with the historically archived D≈2.26866143917643529×10^39.

This is a dimensionless Lorentz-boost *parameter*. It is NOT 45.3 times terrestrial gravity, 45.3 units of proper acceleration, or a new force constant, and the old construction explicitly **did not derive G**: the empirical gravitational strength is inside D. A previous rapidity-chain scan identified many near-hits without a selector; none is promoted here.

On the null-cone factorization `U=T+X,V=T−X,Q=UV−Y²`, the boost `U→exp(η)U,V→exp(−η)V,Y→Y` preserves Q. For Y=0 the null cone is either U=0 or V=0, with no intrinsic rest vertex or unique finite "boost point": a boost simply rescales a null generator. For any chosen *timelike* sheet Q=r²>0 with Y=0, its intrinsic rest reference point (T,X)=(r,0) boosts to

`(T,X)=(r cosh η, r sinh η)`, `(U,V)=(r exp η,r exp(−η))`.

The correct archived surfaces are Q_EM=1/4 → r_EM=1/2 from the **ordinary EM transverse Jxy observability** (v15.1182), and Q_q2=1/16 → r_q2=1/4 from the **genuine closed refined nearest-step q2 carrier** (v15.1183). Neither is a physical relativistic particle mass shell or derived gravitational energy, and the projected original-unit-step q2 ladder has Q=1/4+E_i instead (boundary defect). At input η=ψ_D and Y=0:

| Sheet | Q | T (dimensionless) | U=T+X | V=T−X |
| --- | ---: | ---: | ---: | ---: |
| closed q2 | 1/16 | 5.9538084439400468×10^18 | 1.19076168878800936×10^19 | 5.248741254315484×10^(−21) |
| EM Jxy | 1/4 | 1.19076168878800936×10^19 | 2.38152337757601872×10^19 | 1.0497482508630968×10^(−20) |

The invariant products satisfy UV=Q exactly when computed at sufficient precision; naively evaluating T²−X² in ordinary float64 at these huge rapidities gives catastrophic cancellation, so tests use 70-digit mpmath and null factor coordinates. `exp(ψ_D)=4.76304675515203744×10^19`, and the formal corresponding relative boost speed is `tanh ψ_D=1−8.815771121521049×10^(−40)`; this is a **formal representation-space mapping**, not a derived physical velocity or dynamical acceleration. Neither boost sends a timelike Q>0 point to Q=0.

## Gate 1331 — the simplest covariantly conserved volume flux has an independent normalization

In ambient 2+1 Minkowski interior-cone hyperbolic coordinates `T=s coshχ, X=s sinhχ cosφ, Y=s sinhχ sinφ`, the invariant volume density is `s² sinhχ ds dχ dφ`. For a radial-vector current `J^s=C/s²`, the covariant divergence is identically zero: `∇_a J^a=[s² sinhχ]^(−1)∂s(s² sinhχ J^s)=0`. Its flux across any s=const sheet with a **common finite rapidity aperture** 0≤χ≤H,0≤φ<2π is

`Φ_s(H)=2π C(cosh H−1)`, independent of s.

This is an explicit conserved flux allowed by the ambient geometry, and it supplies **no** intrinsic EM/q2 transfer coefficient: C is arbitrary, and flux through each radial sheet is equal (no net source/debit between sheets). A nonzero change of flux would require a genuine source/sink in the interval, with a source law and action. Conservation does not choose the 3:1 fixed-T Euclidean annulus ratio or 7:1 proper-radius volume ratio from v15.1401. In addition, the rapidity cap H chooses an observer reference; the full noncompact hyperboloid area diverges.

**Reproducer:** locally executed Python `/mnt/data/cone_gate/k4_dirac_boost_nested_hyperboloids_v15_1403.py` checked 70-digit boost, Q products, numerical sheet lifts and exact SymPy divergence/flux. Additive GitHub source `research-notes/k4_dirac_boost_nested_hyperboloids_v15_1403.py`, SHA **b4d3f04268f6096c972bbc63647346780a005b86**; exact committed-byte external Audit replay pending.

**AUDIT:** check historical ψ and force-ratio identity, correct r/Q values (EM vs separate q2), null rays versus timelike rest points, numerically stable rapidity evaluations, divergence-free radial flux including proper measure and cutoff, and underdetermined physical normalization. Do not infer SI velocity, G, gravitation, new acceleration or physical mass shell from these representation coordinates.

**NEXT:** look for a null-congruence geometric transport which compares all three Q levels on a single affinely parametrized null line, and determine whether its relative spacings are Lorentz-covariant without a volume regulator. Then ask the action to select a physical null congruence, state measure and coupling, rather than impose them.
