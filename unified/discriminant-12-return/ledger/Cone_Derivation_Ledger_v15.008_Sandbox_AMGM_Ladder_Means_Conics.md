# Ledger v15.008 — Sandbox: multi-split AM–GM diameter, the (n+k)/(n−k) ladder, and the means as conics

**Lane:** Sandbox (little Euler), on Jeremy's questions of 2026-10-27.
**Payload:** `payloads/amgm_ladder_v15_008/` (NOTE.md + 3 scripts; all
results exact and machine-verified). Suzuki physical weld PARKED;
gravity/Suzuki assessments scoped in the NOTE and summarized below.

## Results [D]

**Multi-split diameter works with cumulative pairs.** Dividing D into
sections s_1..s_m, each boundary is a pair-crossing (S_i | D − S_i)
with X_i² + h_i² = (D/2)² and one shared center AM = D/2.
sum h_i² = sum_{j<l}(l−j) s_j s_l (separation-weighted pair sum;
equal sections: s²C(m+1,3)). Negatives: adjacent-section GMs are NOT
chord heights ((1,2,3): √6 vs 3); the m-factor GM (Πs_i)^{1/m} is not
a chord height or any monomial in the heights and D.

**The (n+k)/(n−k) ladder** (Jeremy: stepping across the circle with
sec φ = coth ψ steps gives an (n+1)-dimensional AM–GM object) has
exact aggregates on diameter m (verified m = 10, 12): **ΠG = (m−1)!**
(ladder volume), ΣG² = (m−1)m(m+1)/6, ΣQ² = (m−1)m(2m−1)/6,
ΣH = (m²−1)/3, ΠH = ((m−1)!)²/A^{m−m+1}… (A = m/2); **ΠQ does not
collapse** (n²+k² roots off-ladder). A is invariant at every rung.
Diameter-12 rungs reproduce the antinode amplitudes √11…√36.

**Means as conics.** Chord 2G is the opening of the row/column
parabola pair at a crossing. Row walk: A = T (line), G² = 2uT − u²
(parabola), H = 2u − u²/T (saturating hyperbola), Q² = 2T² − 2uT + u²
(hyperbola branch ~√2 T). Offset walk: A const, G the circle,
H = A − X²/A (parabola), Q the hyperbola — the four means are the
four conic types, G and H exchanging the parabola role between walks.
Per rung: AH = G² exact; Q² = A² + X² exact; H derived, not a chord.

**Flags:** multisplit_cumulative_pairs=EXACT; ladder_volume=
FACTORIAL_EXACT; prod_Q=NO_COLLAPSE; means_are_conics=EXACT;
gravity_selector=NO_CONTACT (factorials bracket Dirac ×7.7/×4.6;
volumes grid-dependent — h=1/2 gives 23!/2²³ — failing the weld's
grid-invariance test); Suzuki link = envelope samples + Γ/log
currency only, far/K_full untouched; Suzuki_quarter=PARKED.

## Handoffs

→ **external-audit:** verification of the payload identities.
→ **gravity lane / Lane A:** no action requested; recorded so the
slice aggregates (factorial volume, tetrahedral/pyramidal sums) are
on the shared record if a future slice-sum or determinant gate
needs them.
