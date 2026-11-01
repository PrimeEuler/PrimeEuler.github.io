# Ledger v15.235 — Sandbox addendum to v15.234: every crossing is an opposite-sign parabola pair; both families confocal at the apex

**Kind:** Sandbox addendum; exact (symbolic solve + patch check).
**Origin:** Jeremy (2026-10-31): "each point is also where 2
parabolas of opposite sign intersect."
**Producer:** `parabola_pairs.py` (clean exit).
**Payload:** `payloads/parabola_pairs_v15_235/` — PARABOLA_PAIRS.md,
parabola_pairs.py, parabola_pairs_output.txt.

## Result
In the projected canonical mesh the row and column parabolas
carry opposite signs — rows Y² = n² − 2nX (opening toward −X),
columns Y² = k² + 2kX (opening toward +X) — and:

1. **Every mesh crossing is a −/+ intersection**: the pair solves
   to X = (n−k)/2, Y² = nk for all (n, k) (64/64 patch verified
   exactly). This extends v15.234 §B(4): a crossing is a row, a
   column, a level boost hyperbola — and a meeting of the two
   oppositely-opening parabola families.
2. **Exactly two intersections per pair**: Y = ±√(nk). Each
   crossing has a mirror twin on the opposite nappe of the
   bicone, produced by the same two parabolas.
3. **Confocal at the apex**: both families have focus (0, 0) for
   every n, k (row vertex (n/2, 0), focal length −n/2; column
   vertex (−k/2, 0), focal length +k/2). The mesh is the classical
   confocal-parabola system defining parabolic coordinates — the
   geometric reason HJ separates there in both sectors on record
   (MIC v14.731; TN tn_sector.py) — and every parabola of the mesh
   is focused at the apex, the 0 entry of the v15.230 bookkeeping.

## Scope
Addendum to v15.234; grid geometry only. No gate, classification,
or selector statement changes.
