# ρ as a well-definedness question — no two-way object in the record fixes the Compton–Rindler ratio

Sandbox note (little Euler), 2026-11-18; follow-on item
of Jeremy's 2026-11-18 tasking. Producer:
`rho_well_definedness.py` (sympy + enumeration; all
checks PASS). Background: v15.883–v15.888 (Gravity,
sandbox-verified) fenced ρ: with L_R = ρλ̄_C every filed
identity survives for any ρ > 0, so the weld L_R = λ̄_C
(ρ = 1) is a postulate. The tasked question: is there
an object computable in two independent ways whose
*consistency* — a well-definedness predicate of the
species that has selected everything else in this
program — fixes ρ?

## The census: every candidate pays the rate exactly once

ρ is an exchange rate between the pair plane's two
readings: the mass shell's curvature radius (momentum
reading; λ̄_C, τ_C, the seat cycle) and a trajectory's
Rindler length (spacetime reading; a, T_U, the KMS
period). Each candidate two-way object was checked:

- **KMS period vs seat clock.** The Rindler thermal
  period in time units is 2πc/a = 2πρ·τ_C exactly: the
  ratio of the two periods *is* ρ, identically. At
  ρ = 1 they coincide; at any other ρ both are
  well-defined and simply different. A definition, not
  a constraint.
- **Unruh temperature.** T_U = mc²/(2πk_Bρ) — smooth,
  finite, nonzero for all ρ > 0.
- **Zitterbewegung weld.** a_ZB/a(ρ) = 2ρ identically
  (v15.1091's circle against the Rindler scale):
  again a ratio that names ρ, excludes nothing.
- **Seat cycle / Compton clock.** E_rest·τ_C = ħ and
  the π·τ_C ZB period carry ρ-weight 0 — the state
  sector never sees ρ at all.
- **The quantum bouncer** (v15.857/v15.869) — the one
  genuinely mixed spectrum in the record, with m, a
  and ħ in a single formula: E_n/(mc²)
  = |a_n|·2^{−1/3}·ρ^{−2/3}, a smooth power law,
  analytic for all ρ > 0. The mixed object exists and
  is consistent at every ρ.
- **Integer-valued wedge counts.** The one species
  that could bite discretely: a pair-lattice count in
  a horizon-bounded wedge is a *step function* of ρ
  (enumerated: constant on 278/300 sampled steps, jumps
  only at discrete ρ). Even an exact independent
  integer target would localize ρ to an interval
  between jumps — never to a value.

Formally: assign ρ-weights (a: −1, L_R: +1, T_U: −1;
λ̄_C, τ_C, ω_C, boost period: 0). Every identity in
the filed system is ρ-homogeneous — both sides scale
with the same power — so the system contains no
equation a wrong ρ can fail. Each mixed object pays
the exchange rate exactly once, as a definition; a
well-definedness failure needs an object that pays it
twice with independent determinations, and the record
contains none.

## The structural reason

ρ relates a system's mass to its acceleration.
Configurations at every ρ are ordinary, realized,
internally consistent physics — a particle of mass m
accelerating at any a ≠ mc³/ħ is an accelerator
commonplace. A framework-internal well-definedness
predicate cannot exclude configurations that are not
ill-defined. Fixing ρ would require a distinguished
system whose mass *and* acceleration are both
internally determined and linked. The seat is the
only candidate, and its "acceleration" is the
curvature of a momentum-space curve; identifying that
with a spacetime Rindler acceleration is the
dictionary move itself — the weld, restated. The
circle closes exactly where v15.886 left it.

## Verdict and reopening condition

**No: within the current record, ρ is not fixable by
well-definedness.** It remains a free positive real;
ρ = 1 remains a postulate (the seat hyperbola's
double reading), with the census above as its
negative support. Reopening condition, stated
exactly: an object that is (i) computable in both
readings with *independent* inputs, (ii) discretely
valued or otherwise rigid (not a step function with
intervals, not a smooth family), and (iii) ρ-dependent
in a way not removable by the one-time exchange-rate
definition. Nothing in the present machinery —
transports, dictionaries, conversions (v15.858) —
produces such an object, for the same corridor reason
as Door III: the machinery moves values between
sectors; it does not select them.

Flags: rho = FREE (rho > 0); well_definedness_fix =
NONE FOUND (census complete over the record's mixed
objects); rho_1 = POSTULATE (seat double reading);
selector = NONE; G_derived = false.
