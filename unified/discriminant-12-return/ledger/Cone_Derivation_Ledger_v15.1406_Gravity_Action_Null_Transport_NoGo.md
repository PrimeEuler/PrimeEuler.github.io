# Cone Derivation Ledger v15.1406 — A unitary null-line action conserves probability but does not turn 3:1 geometry into a fixed transition law

**Date:** 2026-11-24 Eastern. **Gravity/Cone.** **Status:** [EXACT PASS, auxiliary toy theory] a first-order Hermitian two-state transport action on the previously derived invariant Q-coordinate yields a conserved total U(1) probability and transition probabilities that **are not 3:1**; [EXACT NEGATIVE] uniform path connection is flat/pure gauge, its coefficient is arbitrary, and a scalar operator linking genuine finite EM and q2 SU(2) carriers is forbidden by their distinct central Casimirs; [OPEN] physical action-selected curvature/holonomy, local gauge and EM charge, sector Hilbert map, and observational normalization. This is NOT yet an action derived from frozen Einstein–Maxwell+K4 or Cone arithmetic. Historical v15.1403–1405 3:1 null-affine geometry remains unchanged. **Preledger script commit:** 2fc166caef83c2b135a3e3d87ba97fc6603e0e96. Additive only.

## Gate 1337 — explicit first-order null-Q transport action and U(1) conserved norm

On the fixed U,Y ambient null line from v15.1404, the Lorentz scalar `Q=UV−Y²` is a coordinate increasing from the null sheet Q=0, through closed refined q2 Q=1/16, to EM transverse observability Q=1/4. Let an **auxiliary two-component complex column** `Ψ(Q)` represent two putative sectors. Postulate the simple real first-order action

`S=∫dQ{(i/2)[Ψ†∂QΨ−(∂QΨ†)Ψ]−κ Ψ†σ_x Ψ}`,

with real arbitrary κ and the ordinary Pauli σ_x. Variation gives `i∂QΨ=κσ_x Ψ`; since generator is Hermitian, `∂Q(Ψ†Ψ)=0`. This is an exact **one-dimensional U(1) Noether norm**, not a physical Maxwell/Einstein flux or automatically a photon transition current. κ has dimensions reciprocal to the representation-space Q coordinate (Q is dimensionless here, so κ is formally dimensionless), and is not fixed by the q2 geometric radius.

For an initial pure sector Ψ(0)=(1,0), direct evolution over ΔQ is `Ψ(ΔQ)=exp(−iκΔQσ_x)Ψ(0)`; the probability of finding the second sector is

`P(ΔQ)=sin²(κ ΔQ)`.

The two null-affine intervals are `ΔQ_inner=1/16` and `ΔQ_outer=3/16`, ratio precisely 3. But their *individual segment transition probabilities* satisfy

`P_outer/P_inner=sin²(3κ/16)/sin²(κ/16)`.

The limit κ→0 is **9**, not 3: probability is quadratic in transition amplitude; the amplitudes have first-order magnitude ratio 3. At κ=8π/3 the probabilities are P_inner=1/4 and P_outer=1, ratio 4. The ratio varies with κ and can be undefined when the inner probability vanishes. Sequential propagation through both segments is a product of unitary propagators, not an independent pair of fresh transitions; the segment-specific ratios only compare separate initially identical pure-sector preparations, not a literal decomposition of one final transition probability into segments. The global U1 norm remains 1 across the entire path.

Actual local executed SciPy/SymPy proof: `/mnt/data/cone_gate/k4_null_transport_action_v15_1406.py` checked exact propagators, weak-ratio 9, finite κ ratio 4, and numerical unitary time evolution for κ=.1,1,4,8π/3, with norm error <1e−13. **Additive GitHub reproducer:** `research-notes/k4_null_transport_action_v15_1406.py`, commit SHA **2fc166caef83c2b135a3e3d87ba97fc6603e0e96**, equivalent independently authored; exact committed-byte Audit replay pending.

## Gate 1337b — a flat 1D connection does not supply an intrinsic force

The connection one-form `\mathcal A=κσ_x dQ` has vanishing curvature: `d\mathcal A+\mathcal A∧\mathcal A=0` for this single-coordinate constant matrix. On an interval it is locally pure gauge under `Ψ↦e^{iκQσ_x}Ψ`. When the sector basis is only a conventional internal gauge label, this change of basis removes the apparent mixing; there is no physical new force. If sectors have independently fixed physical measurement bases/endpoints, comparing those bases can retain a boundary rotation. **Either way**, a physical choice of boundary basis, coupling κ and sector map is additional data: it cannot be read off 3:1 affine geometry alone.

## Gate 1337c — physical finite-SU2 scalar intersector mixing is actually prohibited

The archived genuine closed EM and q2 carriers at a common D≥2 have ordinary SU2 spins `j_E=(D−1)/2` and `J_q=(2D−1)/2`. Their central Casimirs differ by the exact amount

`J_q(J_q+1)−j_E(j_E+1)=3D²/4≠0`.

If an intersector map M were a **shared SU2-invariant scalar intertwiner**, it must satisfy `J_q^a M=M J_E^a` for all generators, implying `[C,M]=[J_q(J_q+1)−j_E(j_E+1)]M=0`. Therefore **M=0**. The auxiliary σ_x mixing just postulated is NOT such a scalar map between those actual distinct-spin Hilbert spaces; treating it as a physical SU2 singlet would violate the conditional common-SU2 symmetry. More general tensor couplings may be possible only with the rank/center conditions derived v15.1397 and independent dynamical reduced matrix elements.

**Verdict:** A natural-looking unitary transport along the invariant Q variable is easy to **postulate**, but neither its free coefficient nor its endpoint/sector basis is action-selected. Its probability ratio differs sharply from 3 even with globally conserved U1 norm. The missing physical object is a nontrivial, symmetry-consistent connection or operator, not another geometric partition.

**AUDIT HANDOFF:** independently replay exact committed source, check the symmetrized first-order action and signs, P segment controls and their preparation qualification, flat-connection gauge argument, and central Casimir no-intertwiner proof without conflating the physical closed q2 carrier with the continuous H² target.

**NEXT:** test the nonflat intrinsic Levi-Civita connection on H², where the metric DOES choose a canonical geometric transport, and ask if the exact ln2 intersheet boost difference enforces a closed loop/physical carrier rather than merely suggesting one.
