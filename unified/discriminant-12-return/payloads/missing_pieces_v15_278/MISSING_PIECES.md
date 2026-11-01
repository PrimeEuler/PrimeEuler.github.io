# Two missing pieces: the denominator 8 (closed by parity); the quantum doublet (Kramers)

Producer: `missing_pieces.py` / `missing_pieces_output.txt`.

**Shot 1 — the missing 8, closed.** Flagged 2026-10-29: Casimir
classes mod 1 have denominators 4 = 2² (EM) and 16 = 2⁴ (gravity);
2³ = 8 occurs nowhere. Scan over the quarter lattice: j(j+1) and
(j+½)² give denominators {1, 4, 16}; pair-product and seat squares
give {1, 4, 16, 64} — always 2^even. Mechanism (proof, not search):
at j = a/4, j(j+1) = a(a+4)/16 with a and a+4 in the same parity
class, so v2(a(a+4)) ∈ {0, 2, ≥4} — never 1, and v2 = 1 is the
unique valuation producing a reduced denominator of 8. Quadratic
forms on the dyadic lattice skip 8 by parity. Eighths live one
degree up: j³ = 1/8 exactly at j = ½.

**Shot 2 — the quantum doublet.** v15.277's phase-doublet clause
was classical. Quantum mechanically it is Kramers' theorem,
verified directly: with T = exp(−iπJ_y)K, T² = (−1)^{2j} — computed
−1 at j = ½, +1 at j = 1, −1 at j = 3/2. A T-invariant spin-3/2
Hamiltonian (zero-field form) has spectrum two exact doublets
(±1.1269); the same form at spin 1 gives three distinct levels.
On the half-integer side the doublet is forced by the exchange
algebra itself — exactly the cone's odd diagonals; on the
integer side it is optional — the even diagonals.

Standing pieces NOT touched: the apex dynamics (v15.230); the
rest-point gaps on non-square lattice hyperbolas; the selector.
