# Ledger v15.282 — Sandbox addendum to v15.278: spinors live only in the doublet channel

**Kind:** Sandbox addendum; representation fact [D] at the level
stated.
**Origin:** Jeremy (2026-11-01): "and spinors can only live
there too."
**Producer:** `spinor_home.py` (clean exit).
**Payload:** `payloads/spinor_home_v15_282/` — SPINOR_HOME.md,
spinor_home.py, spinor_home_output.txt.

## Result
A 2π rotation acts on spin-j states as (−1)^{2j} (computed
j = 0…3): integer j returns +1, half-integer j returns −1 — the
same −1 as the Kramers T² of v15.278's Shot 2. In the Pair-Split
grammar (v15.277) the spinor is the doublet channel's resident:
it carries no scalar exchange parity itself and lives in the
exchanged pair, on the double cover. The scalar channels receive
only its bilinears — the density ψ†ψ in the EVEN channel and
the current ψ†σψ as the ODD generators (verified explicitly).

By the shell lock (half-integer ⟺ odd diagonals, integer ⟺ even
diagonals), spinors reside only on the odd diagonals; an even
diagonal cannot host one, its exchange sign being +1 by the same
computation. This gives v15.140's boundary its resident: the odd
sector's conjugate pair of one-ended fragments is the doublet's
home — spinors appear as pairs, not as closed chains.

## Scope
Addendum to v15.278, completing its quantum piece: Shot 2 forced
the doublet's existence on the half-integer side; this entry
records that the doublet is also the spinor's ONLY possible
residence in the channel grading. No gate or classification
changes.
