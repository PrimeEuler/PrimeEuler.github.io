# Representation boundary between the Casimir sectors

Sandbox addendum, 2026-10-29. Gate relayed from Chat: determine whether
the odd-quarter sector admits a mathematically natural representation
compatible with the cone's quarter-step operator, while the even sector
reduces to the Schwinger ladder — i.e. whether the parity split is merely
a geometric grading or deeper operator structure. Producer
`rep_boundary_test.py` (exact rationals + finite matrix check; run log
`rep_boundary_output.txt`, clean exit). NOT ledgered.

Setup: shell T (j = T), states at offsets X = −T + i/2 (the refined
table's shell nodes). J± transitions step X by ±1, so a shell splits into
chains by X mod 1. A chain is a genuine SU(2) multiplet iff it terminates
on-cone at both ends (contains m = ±T, where the norm factors vanish).

## Results [D]
1. **Even shells (T ∈ ½ℤ): exactly one closed chain** — the Schwinger
   irrep (the integer-table chain, class X ≡ T mod 1) — **plus one open
   fragment** (the Casimir/halfway family chain), escaping at *both*
   ends. So even the EM sector is not purely Schwinger at refined level:
   every shell carries exactly one fragment chain beside its irrep.
2. **Odd shells (T an odd quarter): zero closed chains.** Exactly two
   chains, mirror conjugates: one holds the top (+T) and escapes at the
   bottom, the other holds the bottom (−T) and escapes at the top. No
   unitary SU(2) representation with geometric Jz and Casimir T(T+1)
   exists on an odd shell — the would-be dimension 2T+1 is not an
   integer, and the ladder has a nonzero matrix element to a state that
   is not on the cone.
3. **Universal escape weight.** Every open end in every shell (T = 1/4 …
   5/2 audited) escapes with matrix-element² exactly **T + 1/4**. The
   missing target state sits at |X| = T + 1/2 = R — on the ladder circle
   of radius R = j + ½, while the shell's states sit on the Casimir
   circle √(R² − 1/4).
4. **Commutator defect (operator check).** With Jz = geometric X and J+
   truncated to a chain, diag([J+, J−] − 2Jz) is exactly 0 on the closed
   chain (Schwinger j = 2 case checked), and on fragments is 0 in the
   interior and ±(T + 1/4) at precisely the open-end states. SU(2) holds
   inside every fragment and fails by exactly the escape weight at the
   boundary where the ladder leaves the cone.
5. **The quarter-step glues what SU(2) cannot.** The shell's step-½
   operator (the quarter-step, along-shell) maps the two odd fragments
   into each other (X mod 1 classes 1/4 ↔ 3/4) and connects closed ↔ open
   chains in even shells. The full shell — either sector — is a single
   module over the quarter-step algebra; only the even shells' table
   chains are modules over SU(2).

## Verdict
The parity split is **not merely a geometric grading — it is a
representation-type boundary.** Even sector: closed unitary SU(2)
multiplets (Schwinger), one per shell. Odd sector: no SU(2)
representation; instead a conjugate pair of one-ended half-modules,
interchanged by the mirror X → −X and glued into a single module by the
cone's quarter-step operator, with the SU(2) relations failing by a
universal boundary term T + 1/4. The natural representation the odd
sector admits is this graded fragment pair — a module over the ladder
(step) algebra, not over SU(2). Compatible with the quarter-step
operator: yes, and the quarter-step is exactly what the odd sector's
representation needs and the even sector's does not.
