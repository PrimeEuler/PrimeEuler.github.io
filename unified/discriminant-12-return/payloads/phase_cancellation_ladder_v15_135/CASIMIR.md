# The Casimirs are different — correction and verification

Sandbox addendum, 2026-10-29. Jeremy's correction to Test 2 of FLIP.md.
Producer `casimir_test.py` (exact rationals, clean run). NOT ledgered.

## The correction
Test 2 reported the two EM copies as spectrally identical and concluded
"no EM-internal observable distinguishes the copies." That was an artifact
of the translation-invariant ring toy, which has no Casimir. On the cone
the claim is **false**: the Casimir C = j(j+1) (j = T) commutes with the
entire EM ladder algebra — it is as EM-internal as an observable gets —
and it separates the sectors completely. Superseded: the invisibility
sentence in FLIP.md Test 2 and in the 2026-10-29 daily note's operator-test
entry. What survives of Test 2: the grading algebra ([χ, H_EM] = 0,
{χ, U} = 0) and v14.770's specific statement about the Suzuki log
operator. The general "spectral invisibility" moral does not.

## Results [D]
1. **Sector Casimir classes are disjoint mod 1.** Even diagonals (EM):
   C mod 1 ∈ {0, 3/4} (j ∈ ½ℤ). Odd diagonals (gravity-only):
   C mod 1 ∈ {5/16, 13/16} (j in odd quarters) — sixteenths, a class the
   EM sector never takes. The gravity step flips diagonal class at every
   node, hence always changes the Casimir class; EM moves never cross.
2. **Within a shell, the cone's two landing families never share a
   Casimir.** Ladder (transition) circles: radius² = (j+½)². Casimir
   circles: radius² = j(j+1). Difference exactly 1/4 for every shell —
   the −1/4 of j(j+1) = (j+½)² − 1/4 (Paper C; Jeremy 2026-10-08: the
   actual states live on the Casimir circles).

## Consequence
The cone's selection of the EM sector is stronger than operator content:
the sectors carry different Casimir classes, so the phase-offset grading
is labeled by a conserved EM-internal quantity. The gravity-only nodes
are not a translated copy of EM — their Casimir spectrum (sixteenths)
does not occur anywhere in EM.
