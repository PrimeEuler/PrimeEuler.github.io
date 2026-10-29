# Cone Derivation Ledger v15.140 — Sandbox representation-boundary return (addendum to v15.135): the parity split is a representation-type boundary; odd shells carry conjugate fragment pairs, not SU(2) multiplets

**Date:** 2026-10-29. **Lane:** sandbox (Little Euler). **Parents:** v15.135 (phase-cancellation / ladder-lattice return), v14.731 (dyon pair), v15.062 (graviton Stokes pair). Record fact used: J± are transition amplitudes between states, the states living on the Casimir/Jxy vectors with R = j + 1/2 the ladder radius (Paper C; Jeremy's dictionary, 2026-09-30). **Status:** [D] throughout §§1–3 (exact rational chain audit over shells T = 1/4 … 5/2; finite matrix commutator check). Gate relayed from Chat via Jeremy: does the odd-quarter sector admit a mathematically natural representation compatible with the cone's quarter-step operator, while the even sector reduces to the Schwinger ladder — or is the parity split merely a geometric grading? Classification unchanged: κ empirical, G_derived = false; production fence untouched; Suzuki physical-quarter weld PARKED.

**Pre-write collision check:** live HEAD v15.139 (Lane A, noncompact K_full perturbation) at first check; re-checked immediately before the ledger PUT, v15.140 next free. Additive only.

## 1. Setup

Shell T (j = T), states at offsets X = −T + i/2, i = 0 … 4T — the refined table's shell nodes of v15.135 §4. J± transitions step X by ±1, so a shell splits into chains by X mod 1. A chain is a genuine SU(2) multiplet iff it terminates on-cone at both ends: it must contain m = +T and m = −T, where the norm factors (j∓m)(j±m+1) vanish. At an open end the ladder instead has a nonzero matrix element — the escape weight — to a state that does not exist on the cone.

## 2. Results

- **Even shells (T in (1/2)Z): exactly one closed chain** — the Schwinger irrep (the integer-table chain, class X ≡ T mod 1) — **plus one open fragment**, the Casimir/halfway family chain, escaping at both ends. The even sector reduces to Schwinger on its table chain, as the gate proposed; at refined level every even shell additionally carries exactly one fragment chain.
- **Odd shells (T an odd quarter): zero closed chains.** Exactly two chains, mirror conjugates under X → −X: one holds the top state +T and escapes at the bottom; the other holds −T and escapes at the top. No unitary SU(2) representation with geometric Jz (the offset X) and Casimir T(T+1) exists on an odd shell: the would-be dimension 2T+1 is not an integer, and termination fails at exactly one end of each chain.
- **Universal escape weight [D].** Every open end in every audited shell escapes with matrix-element² exactly **T + 1/4**. The missing target state sits at |X| = T + 1/2 = R — on the ladder circle of radius R = j + 1/2 — while the shell's states sit on the Casimir circle √(R² − 1/4).
- **Commutator defect [D].** With Jz = geometric X and J+ truncated to a single chain, diag([J+, J−] − 2Jz) is exactly 0 on closed chains (the j = 2 case is in the payload), and on fragments is 0 in the interior and ±(T + 1/4) at precisely the open-end states. SU(2) holds inside every fragment and fails by exactly the escape weight at the boundary where the ladder leaves the cone.
- **The quarter-step is the odd sector's glue [D].** The along-shell step-1/2 operator (the cone's quarter-step) maps the two odd fragments into each other (X mod 1 classes 1/4 ↔ 3/4) and connects closed ↔ open chains in even shells. Every shell, either sector, is a single module over the quarter-step algebra; only the even shells' table chains are modules over SU(2).

## 3. Verdict, and the graviton's address

The parity split is **not merely a geometric grading — it is a representation-type boundary.** The odd sector's natural representation is a conjugate pair of one-ended half-modules over the ladder (step) algebra, interchanged by the mirror and glued by the quarter-step; it is compatible with the quarter-step operator in exactly the sense that its representation needs that operator, while the even sector's SU(2) representation does not.

**Graviton remark [D].** Nothing in this boundary touches the graviton as a quantum. Spin-2 sits at j = 2, whose shell (T = 2 in the audit) is a closed five-state chain with defect exactly 0 — dead centre of the even sector, consistent with the helicity pair of v15.062. The boundary instead implies the odd sector hosts **no unitary particle multiplets at all**: it carries the grid's geometry (the quarter-step module structure), not quanta. A demand that any particle — graviton included — live in the odd sector would fail on the escape defect of §2.

## 4. Scope

No classification changes: the coordinate/fiber quarter identification remains the weld's node = state premise (v14.904), physical weld PARKED (v14.916); no dynamics, coupling, or spectrum is derived; P1/P2 remain the standing falsifiable forms; NUT unobserved. The fragment taxonomy is a statement about the refined table's transition algebra, not a claim about observed spectra.

**Payload:** `payloads/representation_boundary_v15_140/` — `REP_BOUNDARY.md` (session write-up), producer `rep_boundary_test.py`, run log `rep_boundary_output.txt` (clean exit; exact rational audit, shells T = 1/4 … 5/2).

**Production fence:** unchanged — no spectral promotion, no residual consumer, far rerun, stationarity, or capacity claim; C_S_32000, 3e-5, 0.002 untouched; no charges repeated. Suzuki physical-quarter weld PARKED.
