# Ledger v15.277 — Sandbox synthesis: the Pair-Split principle, tested and refined

**Kind:** Sandbox synthesis note over v15.228–v15.275; instances
exact, cross-system unity [I]; deposited only after out-of-sample
testing at Jeremy's direction.
**Origin:** Jeremy (2026-11-01): "there seems to be a
generalization theorem emerging" — then "lets test it" before
any deposit.
**Producers:** `pair_split.py`, `pair_split_test.py` (clean
exits).
**Payload:** `payloads/pair_split_v15_277/` — PAIR_SPLIT.md,
pair_split.py, pair_split_output.txt, pair_split_test.py,
pair_split_test_output.txt.

## The principle (refined form)
Each opposed pair on record carries its own exchange involution
(grid swap u ↔ v; seat swap A ↔ B; retarded ↔ advanced; Rindler
wedge swap). The involution Z₂-grades the observable algebra:
the **odd channel** holds the generators and the irreversible
forces (momentum/offset, angular momentum, rapidity, the paired
charge as seat half-split s/2, net curvature = drive − reaction,
radiation reaction (ret − adv)/2, damping); the **even channel**
holds the invariants as even functions of those generators —
Casimirs and labels (uv = m², L², A²; Wigner: (m², J²)) — plus
energy and equilibrium data. The **phase** is the exchanged
doublet (e^{±iφ}): the state is the pair. The **fixed locus** is
balance, read sector-wise as rest, drive = reaction, detailed
balance, and the vacuum (exchange-symmetric two-wedge state;
one-sided reduction exactly thermal — verified geometric
spectrum, mean t²/(1−t²)).

## What the tests changed
1. **Grading is algebraic, not cosmetic** (out of sample,
   Schwinger SO(4)): under A ↔ B, all 24 generator commutators
   respect parity multiplication ([e,e]⊂e, [e,o]⊂o, [o,o]⊂e) —
   a Cartan-type automorphism.
2. **The naive form failed and was replaced.** "Labels are even"
   is false: L is conserved (Kepler orbit drift 3.6e-14) and
   exchange-odd. The surviving form: labels are even *functions*
   (Casimirs) of odd generators — verified by A² = 1 + 2EL² to
   4.4e-16 along the orbit, so eccentricity is fixed by even
   data alone.
3. **Scope verified at force level** (exact damped oscillator):
   the even force's work is a state function (−ΔU); all
   dissipation passes through the odd force (work = ΔE_mech;
   closure 1.8e-11). Product-level quantities (powers, fluxes)
   are even as odd×odd and are outside the claim.

**Standing failure condition:** an irreversible force, or a
Casimir-grade label in generator form, found in the wrong
channel in a system on record.

## Scope
Synthesis over the v15.228–v15.275 chain and the earlier
pair record (v14.550, v14.731, v15.135, v15.180). No gate,
classification, or selector statement changes; G_derived and
the occupants question untouched.
