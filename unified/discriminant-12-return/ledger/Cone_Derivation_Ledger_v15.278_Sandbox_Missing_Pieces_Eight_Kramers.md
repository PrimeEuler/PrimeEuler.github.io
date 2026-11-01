# Ledger v15.278 — Sandbox addendum to v15.277: two missing pieces — the denominator 8 closed by parity; the quantum doublet (Kramers)

**Kind:** Sandbox addendum; exact (scan + parity argument;
operator computation).
**Origin:** Jeremy (2026-11-01): "lets take a shot at the
missing pieces."
**Producer:** `missing_pieces.py` (clean exit).
**Payload:** `payloads/missing_pieces_v15_278/` —
MISSING_PIECES.md, missing_pieces.py, missing_pieces_output.txt.

## Shot 1 — the missing denominator 8 is closed
Open since 2026-10-29 (Casimir denominators 4 = 2² EM, 16 = 2⁴
gravity, 8 occurring nowhere; the one-line addendum then offered
was not taken up). Scan over the quarter lattice: j(j+1) and
(j+½)² have mod-1 denominators {1, 4, 16} only; the pair-product
(k/4)² and seat-root squares have {1, 4, 16, 64} — dyadic depths,
always 2^even. The reason is a parity lock, not an unsearched
sector: at j = a/4 the Casimir is a(a+4)/16, the factors a and
a+4 share a parity class, and v2(a(a+4)) ∈ {0, 2, ≥4} — never 1,
the unique valuation a denominator 8 requires. Quadratic forms
on the dyadic lattice skip 8 structurally (this is the mechanism
under the 2026-10-29 exponent-doubling observation and the
Casimir paper's dyadic quadratic normalisation). Eighths exist
at odd degree: j³ = 1/8 exactly at j = ½.

## Shot 2 — the quantum doublet
v15.277's phase doublet was established classically. Its quantum
form is Kramers' theorem, verified directly: T = exp(−iπJ_y)K
gives T² = (−1)^{2j} (computed: −1 at j = ½, +1 at j = 1, −1 at
j = 3/2). A T-invariant spin-3/2 Hamiltonian (zero-field
splitting form) has two exact doublet levels (±1.1269); the same
form at spin 1 has three distinct levels. The doublet is forced
by the exchange algebra on the half-integer side — the cone's
odd diagonals — and optional on the integer side, completing
the doublet clause of v15.277 sector-by-sector as the sector
split predicts.

## Scope
Addendum to v15.277. Untouched standing pieces: the apex
dynamics (v15.230), rest-point gaps on non-square lattice
hyperbolas (seat sampled only for square N), and the selector.
No gate or classification changes.
