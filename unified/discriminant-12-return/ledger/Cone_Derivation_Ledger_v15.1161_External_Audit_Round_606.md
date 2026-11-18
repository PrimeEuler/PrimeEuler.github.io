# Cone Derivation Ledger v15.1161 — External Audit Round 606

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Four new Sandbox entries landed since Round 605/v15.1156 (`87c19d2`):

- v15.1157 (`...Sandbox_Identification_Seam_Broken.md`, `ea4a6d8`,
  payload `payloads/identification_seam_v15_1157/`)
- v15.1158 (`...Sandbox_Nonlinear_Veto_Closure.md`, `85d49ff`,
  payload `payloads/nonlinear_veto_closure_v15_1158/`)
- v15.1159 (`...Sandbox_SVT_Constraint_Completion.md`, `747a645`,
  payload `payloads/svt_constraint_completion_v15_1159/`)
- v15.1160 (`...Sandbox_ET_Dynamics.md`, `d8ae436`,
  payload `payloads/et_dynamics_v15_1160/`)

No filename or version-number collisions found; all four version numbers
and payload directories were free at gate selection.

Each of these entries builds on prior (pre-session, frozen) Gravity/Sandbox
results — v14.9xx charge/flux constructions, v15.1057/1058's K4 veto
machinery, v15.1083/1085's TT-jet and Ward-jet results, v15.1110-1112's
ellipse-shape energetics — which this audit treats as given background,
consistent with practice throughout this session: the audit's job here is
to verify that the *new* algebra built on those quoted inputs is itself
correct, not to re-derive the cited prior physics from first principles.

## v15.1157 — independent verification

Hand-derived from the stated Lagrangian/charge definitions (not just
re-reading the script's asserts):
- L_H=ρ̇²−ρ²ṡ² ⇒ p_s=∂L_H/∂ṡ=−2ρ²ṡ (direct calculus).
- ratio q_χ/p_s=(−ρṡ)/(−2ρ²ṡ)=1/(2ρ), confirmed state-dependent.
- With θ=arccos(tanh s)/2: dθ/ds=(1/2)·(−1/√(1−tanh²s))·sech²s=
  (1/2)(−1/sech s)·sech²s=−sech(s)/2=−1/(2cosh s), matching exactly.
- At ṡ=0: q_χ=p_s=0 trivially, while the cited flux amplitude Φ is
  external/unfixed per the quoted v14.944 result — confirming the
  counterexample logic (no universal functional identity charge=flux can
  hold, since forcing it at this state would also force Φ=0, contradicting
  the cited external-amplitude freedom).
- SHA-256 of both payload files matched; script re-executed: exit 0, 5/5
  PASS.
- The entry's own epistemic scope (identification "BROKEN at weld
  standard", reopening condition stated) is consistent with what the
  derivation actually shows.

## v15.1158 — independent verification

- **H1 (filed J series through r⁶).** By hand, with r²=b²+c²,
  J=(8/9)r²−(8/9)r⁴+(112/135)r⁶: computed ∂²J/∂b∂c directly via the chain
  rule and got bc[−64/9+(896/45)(b²+c²)] exactly, matching the ledger
  (and confirmed it vanishes at c=0 and is odd under c→−c, both
  immediate from the bc prefactor).
- **H2 (general case).** For any analytic f(r²), ∂²f/∂b∂c=4bc·f''(r²) by
  direct chain-rule differentiation (∂f/∂b=2b f', then ∂/∂c gives
  2b·2c·f''=4bc f'') — a fully general identity, not merely true for the
  tested quartic polynomial.
- **H3 (TT block).** For M=[[b,c],[c,−b]]: trace=0 by inspection; det=
  −b²−c²=−r²; characteristic polynomial λ²−r² by direct 2×2 expansion —
  all confirmed exactly by hand.
- **H4/H5.** The y-parity convention and the odd-source/even-square
  identity (V(−U)²=V(U)² for any odd V) are elementary and confirmed by
  inspection.
- SHA-256 of both payload files matched; script re-executed: exit 0, 9/9
  PASS.

## v15.1159 — independent verification

This entry carries the most new quantitative content. Hand-verified every
step from the stated stress tensor T=diag(P,−P,R):
- trace=R; scalar STF S_L=T_zz−trace/3=2R/3 (independent of P).
- Decomposition T=iso(R/3,R/3,R/3)+scalar-STF(−R/3,−R/3,2R/3)+TT(P,−P,0)
  sums back to diag(P,−P,R) exactly — checked component-by-component.
- Ward jet: from the stated first-order system R'=−iqS_z, S_z'=−iqT_zz
  with S_z(0)=0, T_zz(0)=R: R'(0)=0, S_z'(0)=−iqR, and
  R''(0)=−iq·S_z'(0)=−iq(−iqR)=−q²R — all three confirmed by direct
  substitution.
- Constraint solve: Π^S=(3/2)S_L=R; Φ−Ψ=−κa₀⁻²R/q²; with the stated
  Ψ=−κa₀⁻²R/(2q²), Φ=Ψ+(Φ−Ψ)=−(3/2)κa₀⁻²R/q²=3Ψ exactly; Φ+Ψ=4Ψ=
  −2κa₀⁻²R/q² — all confirmed by direct arithmetic.
- Scalar electric Weyl: with the stated Fourier substitution
  ∂ᵢ∂ⱼ→−qᵢqⱼ, ∇²→−q² for q=(0,0,q): E_zz=−(1/(2a₀²))(−q²+q²/3)(Φ+Ψ)=
  (q²/(3a₀²))(Φ+Ψ)=−2κR/(3a₀⁴); E_xx=−(1/(2a₀²))(q²/3)(Φ+Ψ)=κR/(3a₀⁴) —
  both confirmed exactly by hand, and 2E_xx+E_zz=0 (traceless) checked.
- At P=3R/5 (a:b=1:2): E_xx,total=κP/(2a₀⁴)+κR/(3a₀⁴)=(3/10+1/3)κR/a₀⁴=
  (19/30)κR/a₀⁴ exactly, matching the ledger. At P=0: the TT jet vanishes
  while E_zz=−2κR/(3a₀⁴)≠0 — confirmed.
- SHA-256 of both payload files matched; script re-executed: exit 0,
  11/11 PASS.

## v15.1160 — independent verification

- **U_B'(e).** By hand, for U_B=(K/2)(2−e²)(1−e²)^(−1/2): differentiating
  gives (K/2)·e³(1−e²)^(−3/2) after simplification — matches exactly.
- **I_plus'(e).** Similarly, for I_plus=−Ke²(1−e²)^(−1/2): differentiating
  gives −Ke(2−e²)(1−e²)^(−3/2) exactly, matching the ledger.
- **Quartic rest state.** Expanded (1−e²)^(−1/2) via the binomial series
  (1+e²/2+3e⁴/8+...) by hand and multiplied through (2−e²)(...): the e²
  terms cancel exactly, leaving U_B−U_B(0)=(K/8)e⁴+O(e⁶) — confirming no
  quadratic term and the stated e⁴ coefficient K/8 exactly.
- I_plus'(0)=0 trivially from the −Ke(...) prefactor.
- The 1/A period-scaling claim for a pure quartic potential is dimensionally
  standard (energy~A⁴, velocity~A², time~1/A) and consistent with the
  script's numerics.
- SHA-256 of both payload files matched; script re-executed: exit 0,
  all PASS, with every printed number matching the ledger exactly
  (periods 71.360/37.936 vs stated 71.36/37.94; energy residual 2.77e-03
  vs stated 2.8e-3; lag +0.00252 vs stated +0.0025; zero crossings
  0.25937→0.26189 matching exactly).

## Verdict

All four new Sandbox entries PASS independent verification. No
mathematical, numerical, or reproducibility error found in any of them.
All four entries are carefully scoped (explicitly flagging what is
imported/standard vs. newly derived, and not overclaiming a Cone-specific
selector or new physics), consistent with the pattern established
throughout this session's audit.

`git fetch origin master` immediately before this commit returns
`d8ae436`, unchanged since the pushes verified above. Gravity/Sandbox/
Lane A should continue.
