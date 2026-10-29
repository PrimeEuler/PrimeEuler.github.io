# Cone Derivation Ledger v15.135 — Sandbox phase-cancellation / ladder-lattice return: EM-first fails at the fiber, the flip is selected by the cone's table, and the Casimirs separate the sectors

**Date:** 2026-10-29. **Lane:** sandbox (Little Euler). **Parents:** v14.731, v14.735 (dyon pair; angular unification), v14.904, v14.913, v14.914 (weld and framing corrections), v14.770 (grid-offset spectral invisibility, scoped), v15.069, v15.073 (classification audit, R394-verified). Record fact used: the mesh is the (n1, n2) Schwinger multiplication table's row/column lines (Paper C remark, 2026-10-08). **Status:** [D] all lattice, operator, table, and Casimir statements in §§2–5 (exact rational / symbolic / finite-operator checks, payload replayable); [I] the two origin readings in §6. Classification unchanged: κ empirical, C matched, G_derived = false; Suzuki physical-quarter weld PARKED (v14.916); production fence untouched. Jeremy-directed session (the two hypotheses and the cone-selection claim are his; the Casimir correction in §5 is his, caught against this lane's own operator test).

**Pre-write collision check:** live HEAD v15.134 (Audit liveness) at first check; re-checked immediately before the ledger PUT, v15.135 next free. Additive only.

## 1. Setup — the two directions, three levels kept separate

Two origin hypotheses for the quarter lattice were tested against each other. **EM-first (Jeremy):** EM created the 1/4 lattice and gravity is the residue of a phase cancellation. **The flip (Jeremy):** gravity creates the grid and a phase offset creates EM. A third claim, also Jeremy's, is tested in §4: the cone itself selects the EM sector, the EM ladder operators being the even diagonals of the multiplication table.

Throughout, ħ = 1 and three levels are never conflated: **P** pair product (EM: eg in (1/2)Z; TN: εl in (1/4)Z, v14.731); **S** HJ twist (s_EM = eg; s_TN = 2εl — both in (1/2)Z); **R** parabolic seat roots r± = (k ∓ s)/2.

## 2. EM-first — a coordinate quarter, conditionally; no fiber quarter

- **The ladder is s-blind [D].** MIC parabolic separation holds with symbolic s (sympy residual exactly 0), and TN − MIC is purely radial at s = 2εl (v14.734 machinery, re-run). The parabolic ladder creates no lattice; the twist's quantization is imported from fiber single-valuedness (Dirac for EM, Misner for TN).
- **EM pairs generate a coordinate quarter lattice [D].** For A = p/2, B = q/2, the pair coordinates C = (A+B)/2, X = (A−B)/2 lie in (1/4)Z on a checkerboard: 4C ≡ 4X (mod 2), exhaustive, 0 violations. Opposite parity gives genuine odd quarters (A = 1/2, B = 0 → C = X = 1/4).
- **The cancellation condition [D].** Odd-quarter offsets survive iff the centre is itself an odd quarter mod 1 (C ≡ 1/4, 3/4 → X ∈ {1/4, 3/4}; C ≡ 0, 1/2 → X ∈ {0, 1/2}). Exact cancellation C = 0 forces X = A in (1/2)Z: cancel the common mode completely and the odd quarters die with it. An EM origin for quarter offsets therefore requires the "cancelled" mode to leave an odd-quarter holonomy; bare cancellation does not select one.
- **No twist-level route to the dyon quarter [D].** (1/2)Z is a group: s1 ± s2 stays in (1/2)Z. The only combination reaching (1/4)Z, the offset coordinate (s1−s2)/2 used as a twist, produces seat-root offsets in (1/8)Z — an eighth lattice not in the record (combination rule falsified). At minimal twist the sectors are seat-identical: EM (s = 1/2) and TN (εl = 1/4, s = 2εl = 1/2) give the same seat charges for k = 0..4. The quarter is invisible in the twist and in the seats; it lives in the factorisation s = 2εl (state ε × coupling l), i.e. in the Misner fiber spectrum ε_n·l = n/4, which EM does not possess.

**Verdict (EM-first):** the mesh/coordinate quarter is EM-generable, conditionally (opposite-parity pair + odd-quarter centre holonomy, origin open). The dyon product quarter is NOT EM-generable by phase combination. Identifying the coordinate quarter with the fiber-product quarter is exactly the weld's node = state premise (v14.904), not a consequence of EM phase algebra.

## 3. The flip — lattice and operator levels

- **Lattice level [D].** On gravity's quarter checkerboard (1,089 points in the test window), a staggered phase offset — a second channel translated by half a period, character χ = (−1)^(4C) — interferes as (1+χ)/2 and leaves exactly the EM sublattice: 545 survivors, all in (1/2)Z × (1/2)Z; the 544 cancelled points are exactly the odd quarters. Quotient (1/4 Z)/(1/2 Z) ≅ Z2. (Same partition as §2's parity split, read from the other end.)
- **Operator level [D, finite model].** 24 quarter sites on a ring, U = quarter step, H_EM = U² + U⁻², χ = (−1)ⁿ: [χ, H_EM] = 0 and {χ, U} = 0 exactly, PUP = 0 with P = (1+χ)/2 — EM dynamics preserves the sectors, every gravity step flips sector. U² has exactly two orbits (12 + 12), each with H_EM spectrum equal to the half-lattice ring's (max deviation 0.00e+00); the odd copy sits at 1/4, 3/4, 5/4, … — the EM lattice translated by half an EM period, a π phase offset in EM's own phase variable. A χ-potential −λχ splits the copies rigidly by 2λ and does nothing else: that term is the phase lock a "creation" dynamics would have to supply (see §4 for its selection-form retirement, and §5 for the correction to this test's invisibility remark).
- **Priority [I].** The two directions are one operator fact (U vs the orbits of U²); the lattice cannot decide priority. The record can: U has a derivation (Misner period 8πl, v14.731); no EM-side derivation of the U² dynamics exists. Kaluza–Klein is the precedent for fiber phase → charge; the grid version avoids KK's radius problem because the fiber is the universal mesh, not one TN solution's l.

## 4. Cone selection — Jeremy's even diagonals [D]

Table coordinates: refined indices (p, q) in Z², (n, k) = (p/2, q/2); node X = (p−q)/4, T = (p+q)/4; a diagonal is constant p−q (constant X).

- **Diagonal parity is the sector.** p−q even ⟺ X, T in (1/2)Z (EM); p−q odd ⟺ X, T odd quarters. 0 violations; 545 even / 544 odd — the same partition a third time.
- **The weld's vertices are the diagonal classes.** Smallest positive |X|: even diagonals → 1/2 (EM vertex); odd diagonals → 1/4 (gravity vertex ±q_G).
- **EM ladder moves never change diagonal parity.** Refined Δ(p−q): shell ladder (2,2) → 0; oscillator steps (2,0), (0,2) → ±2; J± (2,∓2) → ±4. The gravity single row/column steps (1,0), (0,1) have Δ = ±1 and are the unique minimal sector-swaps. Shell lock (integer table): at fixed shell s = n1+n2, every offset n1−n2 ≡ s (mod 2), and the in-shell ladder step changes the offset by exactly 2 — within a shell the ladder cannot land on the other parity's diagonals at all.

**Verdict:** the cone selects the EM sector at the level of operator content. Diagonal parity is a conserved label of the EM ladder algebra by the table's integer indexing alone; no imported χ-lock is needed for selection. (This retires the selection form of §3's lock debt. It supplies no energy splitting and no dynamics — §6.)

## 5. The Casimirs are different — correction, and the sector label [D]

This lane's §3 operator test reported the two copies as spectrally identical and stated that no EM-internal observable distinguishes them. **Jeremy's correction: the Casimirs are different. He is right; the sentence is superseded.** It was an artifact of the translation-invariant ring toy, which has no Casimir. On the cone, with j = T and C = j(j+1):

- **Casimir classes mod 1 are disjoint between sectors.** Even diagonals (EM): C ∈ {0, 3/4}. Odd diagonals (gravity-only): C ∈ {5/16, 13/16} — sixteenths, a class the EM sector never takes. The Casimir commutes with the entire EM ladder algebra, so the grading is labeled by a conserved EM-internal quantity. The gravity step flips diagonal class at every node, hence always changes Casimir class; EM moves never cross.
- **Within a shell, the cone's two landing families never share a Casimir.** Ladder (transition) circles: radius² = (j+½)². Casimir circles: radius² = j(j+1). Difference exactly 1/4 for every shell (Paper C; the actual states live on the Casimir circles).

What survives of §3's operator test: the grading algebra and the orbit decomposition. What does not: any general spectral-invisibility moral beyond v14.770's specific log-operator statement (H_G = H_EM − (log 4)I), which is untouched.

**Detection remark [I].** A "gravitational Casimir" would be an observed angular spectrum whose Casimir values land in the sixteenth classes — equivalently quarter-j shells on a gravitational (TN-class) background. No channel is claimed here; the standing falsifiable forms remain P1 (h = 1/2 gravity at every k) and P2 (W₂ cutoff 4n), both untested, and NUT remains unobserved.

## 6. Scope and classification

This entry changes no classification: the coordinate quarter is derived algebra; the fiber quarter remains the Misner/Killing derivation of v14.731; the identification of the two remains the weld's node = state premise (v14.904), with the physical weld PARKED (v14.916). Neither direction derives Maxwell dynamics, Einstein dynamics, the value of e (α remains empirical/selector class), or an energy splitting between the sectors. κ empirical, C matched, G_derived = false. The dyadic pattern of the session is noted without claim: state lattice (1/2)¹, pair product and Casimir offset (1/2)², and the single appearance of (1/2)³ was the falsified eighth lattice of §2 — a third halving exists algebraically but the cone's table does not populate it as a twist.

**Payload:** `payloads/phase_cancellation_ladder_v15_135/` — `RESULTS.md`, `FLIP.md`, `TABLE.md`, `CASIMIR.md` (session write-ups incl. the §5 correction), producers `ladder_test.py`, `flip_test.py`, `flip_operator_test.py`, `table_test.py`, `casimir_test.py`, and run logs `output.txt`, `flip_operator_output.txt`, `table_output.txt`, `casimir_output.txt` (all clean exits; exact rational arithmetic throughout, sympy for §2's separation checks).

**Production fence:** unchanged — no spectral promotion, no residual consumer, far rerun, stationarity, or capacity claim; C_S_32000, 3e-5, 0.002 untouched; no charges repeated. Suzuki physical-quarter weld PARKED.
