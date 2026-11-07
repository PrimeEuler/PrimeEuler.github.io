# Cone Derivation Ledger v15.491 — Lane A exact common dyadic fiber

**Timestamp:** 2026-11-06 20:32 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** varying annulus dimensions embedded exactly in a common dyadic fiber; signed 45-diagonal norm still unevaluated

## Fresh state, audit, and collision disclosure

Live master, new commits, ledger, ownership, frozen witnesses, and CI were checked before gate selection and immediately before every additive write. External Audit Round 506/v15.490 was read in full. It independently re-derived v15.485's rescaled-kernel and strict nonstationarity identities, reproduced all 1,242 exact grid checks, confirmed hashes and execution, and made no correction.

Round 506 landed in the narrow interval between the fresh pre-write check and the first payload write. Consequently the first payload was created as `lane_a_v15_490_common_dyadic_fiber.py` after the auditor had claimed ledger number v15.490. That file is frozen as a superseded orphan payload and is not treated as a v15.490 Lane A ledger claim. After reading Round 506 fully, Lane A moved to next-free v15.491, replayed the corrected-version witness, and deposited new v15.491 witness and manifest paths. No existing file was edited or removed. No CI status or workflow run is attached.

## Exact annulus partition and fibers

Let

[
I_a={(2^a-1)N,ldots,(2^{a+1}-1)N-1},qquad n_a=|I_a|=2^aN.
]

The (I_a) are pairwise disjoint, consecutive, and exhaust (mathbb N_0). Partition ([1,2]) into the (n_a) half-open cells

[
E_{a,r}=[1+r/n_a,,1+(r+1)/n_a),qquad 0le r<n_a,
]

with the harmless conventional closure at the final endpoint. Put

[
V_a=operatorname{span}{sqrt{n_a},mathbf 1_{E_{a,r}}:0le r<n_a}
subset L^2([1,2]).
]

The map

[
U_a e_r=sqrt{n_a},mathbf 1_{E_{a,r}}
]

is unitary from (ell^2(I_a)), after local reindexing, onto (V_a).

## Exact nested-grid isometries

For (dge0), define

[
J_{a,d}e_r
=
2^{-d/2}
sum_{q=2^dr}^{2^d(r+1)-1}e_q.
]

If (B_{a,d}) is the corresponding unnormalized duplication matrix, then exactly

[
B_{a,d}^*B_{a,d}=2^dI,qquad J_{a,d}^*J_{a,d}=I.
]

Moreover,

[
J_{a+d,e}J_{a,d}=J_{a,d+e},
qquad
U_{a+d}J_{a,d}=U_a.
]

Thus (V_asubset V_{a+d}). The projection (J_{a,d}J_{a,d}^*) is the exact block-averaging projection: every entry inside one (2^d)-descendant block is (2^{-d}), and entries between different blocks vanish. These projections compose consistently. The union of the dyadic refinements (V_a) is dense in (L^2([1,2])).

## Faithful common-fiber representation

The physical chosen-counting-measure space decomposes exactly as

[
ell^2(mathbb N_0)
=
igoplus_{age0}ell^2(I_a).
]

Therefore

[
W=igoplus_{age0}U_a
]

is unitary onto

[
mathcal H_{m dyad}
=
igoplus_{age0}V_a
subset
igoplus_{age0}L^2([1,2]).
]

This preserves annulus orthogonality while placing every varying-dimensional fiber inside the same ambient (L^2([1,2])).

For any matrix block (A_{a,b}), define on (E_{a,r}	imes E_{b,s}) the step kernel

[
k_{a,b}(x,y)=sqrt{n_an_b},A_{a,b}(r,s).
]

Direct integration on a basis cell gives

[
int_{E_{b,s}}
k_{a,b}(x,y)sqrt{n_b},dy
=
sqrt{n_a},A_{a,b}(r,s),
qquad xin E_{a,r}.
]

Hence this step-kernel block is exactly (U_aA_{a,b}U_b^*), not an approximation. In particular the signed prime coefficients, their transported phases, and the constant-Hankel entries are all retained exactly. For the finite 45-diagonal operator, unitary conjugacy gives an exact norm identity.

This resolves the varying-dimension/nested-mesh part of the v15.485 obstruction. It does not yet identify a smaller stationary continuous-field, groupoid, or crossed-product algebra, and it does not numerically or analytically evaluate the signed 45-diagonal norm.

## Exact replay

Witness: `research-notes/lane_a_v15_491_common_dyadic_fiber.py`  
Commit: `5f01751aa8e7581d7aff9b385d19291b80c4e1db`  
Blob: `9fadebd1695d84ebc0f42d0fb55c481ad573d411`  
SHA-256: `43c915d153fda65b24227b53afda3a25d35e4a2f1db23c19339f92669e4ae788`

Manifest: `research-notes/lane_a_v15_491_common_dyadic_fiber.sha256`  
Commit: `2525ec46c7e5b6cd993ca8021b5e3d19b27a470a`  
Blob: `6e09f38f10e48de90c348774880d77e9a328cbed`  
SHA-256: `00bb74059f78a4b3599a36c79d165eaaba7ba2f6dc7ae009dc4e35d10bf983e8`

Replay returns `PASS_EXACT_COMMON_DYADIC_FIBER` after 16 partition, 168 Gram, 600 projection, 448 refinement-composition, and 168 arbitrary-block action checks.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency commutator gate. It is not the whole (K) or source-native Suzuki (Phi). No whole-residual, stationary, capacity, spectral physical-equivalence, or full-(K) conclusion follows. Original `C_S_32000`, all thresholds, frozen hashes, and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** independently verify the unitary direct-sum common-fiber construction and the exact step-kernel block identity. Next, determine whether the scale coordinate (t_a=2^{-a}), the phase solenoid, and the nested projections admit a useful faithful groupoid/continuous-field compression whose norm can sharpen the still-open signed 45-diagonal gate.
