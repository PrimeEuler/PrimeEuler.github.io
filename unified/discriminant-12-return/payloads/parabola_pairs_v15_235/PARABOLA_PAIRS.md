# Every crossing is an opposite-sign parabola pair — verification note

Producer: `parabola_pairs.py` / `parabola_pairs_output.txt`
(symbolic solve + 64-crossing patch check).

In the projected (T-view) canonical mesh, the two parabola
families carry opposite signs:

    row n:    Y² = n² − 2nX   (opens toward −X)
    column k: Y² = k² + 2kX   (opens toward +X)

1. **Every mesh crossing is a −/+ intersection.** Solving the pair
   gives X = (n−k)/2, Y² = nk — the crossing — for every (n, k)
   (64/64 patch verified exactly).
2. **Exactly two intersections per pair:** Y = ±√(nk) — the
   crossing and its mirror across the axis, i.e. one point on each
   nappe of the bicone. Every mesh point has a mirror twin
   produced by the same two parabolas.
3. **Both families are confocal at the origin.** Row: vertex
   (n/2, 0), focal length −n/2 → focus (0, 0). Column: vertex
   (−k/2, 0), focal length +k/2 → focus (0, 0). For all n, k. The
   mesh is the classical confocal-parabola system defining
   parabolic coordinates — the geometric reason the HJ equation
   separates there in both sectors on record (MIC v14.731; TN,
   tn_sector.py). Every parabola of the mesh is focused at the
   apex — the 0 of the v15.230 apex bookkeeping.
