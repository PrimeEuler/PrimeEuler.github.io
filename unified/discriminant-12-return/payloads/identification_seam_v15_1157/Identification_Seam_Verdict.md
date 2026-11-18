# The identification seam — broken at weld standard

Sandbox note (little Euler), 2026-11-18; item 2 of
Jeremy's 2026-11-18 gravity-thread tasking. Producer:
`identification_seam.py` (sympy, exact; all checks PASS).
Standard fixed in advance (2026-10-28 assessment): the
identification pair-side charge ↔ radial flux must be
*derived from the structure* at weld standard (v14.904 /
v14.914: integer counts, no fitted joint) — not
κC = 1-style matching. Weak form only: the strong form
(quantization fixes the strength, KK-style) was already
closed by v15.050.

## The two sides, as filed

Pair side — not one charge but three, from three actions:
the dressed momentum L = cosh(s)·p_s ∈ ℏℤ (v14.988, U(1)
single-valuedness at fixed ρ); the Hessian s-shift charge
Q_s (v14.946/v14.952), whose spectrum is **continuous**;
the spinor Noether charge q_χ = −ρṡ ∈ ℏℤ (v14.990).
Flux side (v14.944): conservation on the K4 FLRW slices
gives Ĵ = Φ(τ)/(4πR²) with Φ **not fixed by
conservation**; the point-source normalization is
external; the entry's own flags read
independent_factor_Noether_charge = NOT_DERIVED,
amplitude arbitrary.

## The obstruction, in three exact pieces

1. **The pair charges disagree with each other by
   state-dependent factors.** From the Hessian kinetic
   term (dℓ² = 2dρ² − 2ρ²ds²), p_s = −2ρ²ṡ, while
   q_χ = −ρṡ: ratio q_χ/p_s = 1/(2ρ). The two ℏℤ
   charges are related through the spinor square root by
   the flow factor −2cosh(s) (dθ/ds = −1/(2cosh s),
   verified from tanh s = cos 2θ) — again
   state-dependent, constant only at the seat s = 0.
   So at most one candidate could equal the flux, with a
   normalization that would have to vary with the state
   — not a dictionary constant.
2. **A static counterexample kills any functional
   identity.** At ṡ = 0 both pair charges vanish, while
   Φ ≠ 0 is admissible on the K4 side (v14.944's null
   current carries arbitrary N). A pair at rest with
   nonzero radial flux is a legal configuration of the
   combined record; charge = flux as functionals is
   false on it.
3. **The identification must cross actions, twice
   unforced.** The action that generates the radial/K4
   side is the Hessian action, whose charge is the
   continuous Q_s — the one candidate that is *not*
   ℏℤ-quantized. The ℏℤ charges live on pair-mechanical
   actions (fixed-ρ phase theory; spinor theory) that
   have no radial sector, no sphere, and no flux.
   Crossing requires selecting the pair kinetic metric —
   the choice v14.990 itself files as unforced ("Nothing
   yet forces the choice") — and separately fixing the
   flux amplitude v14.944 files as free. Two joints;
   weld standard allows zero.

## Verdict

**BROKEN at weld standard.** The identification is not
derivable from the structure; it survives only as a
postulated dictionary line (Φ := q_χ, or Φ := L) of
κC = 1 type — exactly the form the 2026-10-28 standard
excluded in advance. Downstream flag: any argument that
treats the radial flux as quantized *because* a pair
charge is ℏℤ is using the postulated form and should be
read as such. What does not break: each charge is a
correct conserved/quantized object on its own action;
the flux is a correct conserved-current construction
with a free amplitude; the weld (a different,
integer-count identification) is untouched.

Reopening condition: a coupled action in which the pair
kinetic metric is *selected dynamically* (so the charge
and the flux are charges of one theory), or a K4-side
derivation of a Noether charge from the factor product
with Φ fixed — either would give the identification a
single-action home. Absent one, the seam is settled:
the gravity dictionary's quiet dependence on it should
be treated as a postulate, not a derivation.

Flags: identification = BROKEN_AT_WELD_STANDARD;
pair_charges = 3 (2 × ℏℤ, state-dependently related;
1 continuous); flux_amplitude = FREE (v14.944);
joints_required = 2; G_derived = false;
psi_selected = false.
