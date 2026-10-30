# Ledger v15.180 — Sandbox addendum: boundary staircase, boundary flux, phase relations

**Kind:** Sandbox return; addendum to v15.135 / v15.140 / v15.143.
**Origin:** Jeremy's prompts (2026-10-30): the cone within a cone,
with the null light cone as a boundary to measure against; the
resulting staircase figure; and the closing of the phase-relation
item flagged pending in v15.143 §5.
**Producers:** `cones_test.py`, `phase_relation_test.py` (exact
rationals / exact algebra; clean exits; shells audited to T = 5).
**Payload:** `payloads/boundary_staircase_phase_v15_180/` — CONES.md,
cones_test.py, cones_output.txt, PHASE.md, phase_relation_test.py,
phase_relation_output.txt, staircase.png, odd_diagonals_circle.png.
**Verification:** all identities closed-form or exhaustively audited
as stated; 0 violations.

## 1. The boundary measure and the flux theorem [D]
Per shell T: floor AM² = T², states C² = T(T+1), boundary (ladder)
R² = (T + 1/2)². The machinery's natural quantities are differences
against the boundary: transition amplitudes are boundary chords
(amp² = R² − X′², X′ the midpoint offset); **state depth is
constant**, R² − C² = 1/4 at every shell; the escape weight of
v15.143 is the boundary-to-floor gap, R² − AM² = T + 1/4.
**Flux theorem:** every shell T ≥ 1/4 has exactly **two open ends**
(even shells: the Casimir fragment's two; odd shells: one per
fragment), each leaking T + 1/4, so the **total escape per shell is
2T + 1/2**, carried entirely by the non-table chains; the closed
particle chain leaks nothing. (Open-end count: a chain class mod 1
contains ±T as in v15.143(i); per-end weight v15.143(ii).) Audited
T = 1/4 … 5.

## 2. The boundary staircase [D]
R(T) = T + 1/2 is the AM radius of shell T + 1/2: **each shell's null
boundary is the next shell's floor.** The next shell's state cone
protrudes past it by C(T + 1/2)² − R(T)² = T + 1/2 = R(T) (squared
radius). Containment is exact only within a shell (the 1/4 of §1);
across shells the cones form a regular staircase with no top —
v15.143(v)'s escape climb is a climb of this staircase. Figure:
`staircase.png` (floors at every quarter shell; boundary ticks ending
below the next floor's rim states).

## 3. Transitions live on the next cone; gravity's steps are null [D]
A transition landing point of shell T (midpoint X′ = m + 1/2, height
= amplitude √(nk) with n + k = 2T + 1) is a refined crossing of shell
T + 1/2 whose GM is the amplitude: the ladder circle of shell T is
the state circle of shell T + 1/2. In the (X, T) plane, step
intervals ΔT² − ΔX²: gravity's quarter steps (single row/column
steps) have interval **exactly 0 in both null directions**; EM's
shell ladder has +1 and the halfway step +1/4 (timelike); EM's
in-shell steps have −1 and −1/4 (spacelike). Null ⟺ odd change of
diagonal index ⟺ sector change. Figure: `odd_diagonals_circle.png`
(circle view: closed chain on the Casimir circle vs fragments
escaping to rim points of the ladder circle).

## 4. Phase relations (closes the v15.143 §5 flag) [D, finite model]
On the quarter ring of the v15.135 flip test: sector states (sites,
H_EM eigenstates) have ⟨U⟩ = 0 exactly — no inter-sector phase;
eigenstates of the quarter-step U have sector weights exactly
1/2 + 1/2 and ⟨U⟩ a pure phase (|⟨U⟩| = 1). A gravitational phase
relation is thereby a defined excitation type: a quantum of the
relative phase between the grid's two sectors, invisible to H_EM,
measured exactly by U; not a multiplet occupant (consistent with
v15.140). Recorded as a reinterpretation, not a displacement of the
QFT graviton (even-sector Fock state, j = 2); rhymes on record:
Misner patch phase (v14.731), monopole as pair phase, helicity-pair
relative phase (v15.062).

## 5. Diagonal grading and the ladder factor pairs [D]
Terminology (Jeremy): "the N diagonal" = the shell anti-diagonal
n1 + n2 = N = 2j of the table (5-diagonal: j = 5/2; 6-diagonal:
j = 3). The two diagonal families are locked by the shell lock
(offsets ≡ shell mod 2). Refined shell index S = p + q gives a
mod-4 grading: S ≡ 0 (mod 4) integer-spin shells, S ≡ 2 (mod 4)
half-integer-spin shells, S odd = quarter shells (no spin). Squared
ladder elements are factor products: (j−m)(j+m+1) = nk with
n + k = 2j + 1 — the amplitudes are the GM heights of the shell's
factor pairs on the ladder circle (j = 5/2: pairs summing to 6 give
5, 8, 9, 8, 5; j = 3: pairs summing to 7 give 6, 10, 12, 12, 10, 6);
half-integer j has a central transition of amplitude exactly R,
integer j has two central transitions of squared height j(j+1).

## 6. Scope and assessment for the gravity thread
Classification unchanged (v15.069; G_derived = false); production
files untouched. Two assessments recorded at Jeremy's question:
(a) the staircase is form-identical at every floor (1/4 depth, two
open ends, flux 2T + 1/2, linear growth), so no rung is
distinguished — the 2026-10-20 position-selector negative ("the
selector is not a staircase") is now a structural statement, not
only a scan result; (b) on the finite table, the quarter-step is
intrinsically selected as the unique null step (§3), narrowing
v14.865's operator item on the table side only — the Suzuki-side
analytic operator is still not exhibited and the physical weld
remains parked (v14.916). The boundary flux contains state data
(the shell T) and so would fail the v15.050/v15.069 checklist as a
derivation route; it is recorded as structure, not as a candidate
coupling.
