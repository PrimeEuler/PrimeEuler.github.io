# Cone selection: EM ladder operators are the even diagonals

Sandbox addendum, 2026-10-29. Jeremy's claim: the cone selects the EM
sector; the EM ladder operators are the even diagonals of the
multiplication table. Producer `table_test.py` (exact rationals, clean
run). NOT ledgered.

Table = the (n1, n2) Schwinger multiplication table whose row/column lines
are the cone mesh (Paper C remark, 2026-10-08). At gravity resolution
h = 1/2: refined indices (p, q) ∈ ℤ², (n, k) = (p/2, q/2); node
X = (p−q)/4, T = (p+q)/4. A table diagonal is constant p−q (constant X).

## Results [D]
1. **Diagonal parity is the sector.** p−q even ⟺ X, T ∈ ½ℤ (EM); p−q odd
   ⟺ X, T odd quarters. 0 violations; 545 even / 544 odd in the window —
   the same partition as both previous tests, now in table coordinates.
2. **Vertices are diagonal offsets.** Smallest positive |X|: even
   diagonals → 1/2 (EM vertex ±1/2); odd diagonals → 1/4 (gravity vertex
   ±q_G). The weld's two vertex sets are the table's two diagonal classes.
3. **EM ladder moves never change diagonal parity.** In refined indices
   every EM move has even Δ(p−q): shell ladder (2,2) Δ=0; oscillator steps
   (2,0), (0,2) Δ=±2; J± (2,∓2) Δ=±4. The gravity single row/column steps
   (1,0), (0,1) have Δ=±1 and are the unique minimal sector-swaps.
4. **Shell lock (integer table).** At fixed shell s = n1+n2, every offset
   n1−n2 ≡ s (mod 2); the in-shell ladder step (+1,−1) changes the offset
   by exactly 2. Within a shell the ladder cannot land on the other
   parity's diagonals at all.

## Verdict
Jeremy's claim is exact in table coordinates. The cone selects the EM
sector at the level of **operator content**: the grading is not an added
potential — the table's integer indexing makes diagonal parity a conserved
label of the entire EM ladder algebra, and the EM ladder operators are
precisely the moves living on/between even diagonals. This retires the
"imported χ-lock" debt of Test 2 in its selection form. What it does not
supply: an energy splitting between the copies (still degenerate —
v14.770's spectral invisibility stands), Maxwell dynamics, or the value
of e. Selection of operators ≠ dynamics.
