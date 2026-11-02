# Second test round on the pair structure: three confirmations

Producer: `structure_tests.py` / `structure_tests_output.txt`.

**Test A — apex pair, gravity sector.** On the refined mesh, the
triple balance of v15.280 holds at the quarter scale: innermost
vertices ±1/4, innermost crossing (0, 1/2), curvatures ∓2/+2
cancelling; vertex midpoint = X_cross/2 for all tested (p, q).
The apex-pair structure is sector-general.

**Test D — Wigner holonomy channel.** Pair-Split (v15.277) places
the v15.271 spin-transport gauge in the odd channel and the shell
in the even. Composing boosts both ways: the resulting γ_w is
exchange-EVEN and the Wigner angle θ_W exchange-ODD, both exact
to 6 digits on four random pairs (residual verified a pure
rotation). Note on method: a first extraction using the wrong
(R·B vs B·R) decomposition gave approximate antisymmetry and was
rejected; the deposited producer uses the corrected B·R form —
the near-miss is recorded here because the test was only passed
after the extraction was fixed.

**Test G — rest-gap census.** ψ_min(N) = min over factor pairs
of |½ ln(n/k)| on uv = N: ZERO iff N is a perfect square
(squares 1, 4, 9, 16 in range; verified through the census),
strictly positive otherwise. Primes are worst-case:
ψ_min(p) = ½ ln p exactly (p = 499: 3.1063). Near-square
N = m² − 1: ψ_min = ½ ln((m+1)/(m−1)) exactly (m = 3, 5, 10),
decaying ~1/√N. Content: the lattice holds a state exactly at
rest only on square shells; on every other shell its nearest
state is forcibly boosted by ψ_min(N). This quantifies the
v15.274 seam.
