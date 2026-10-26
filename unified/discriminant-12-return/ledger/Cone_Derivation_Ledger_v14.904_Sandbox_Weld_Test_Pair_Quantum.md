# Cone Derivation Ledger v14.904 - Sandbox weld test: the Suzuki /4 is the dyon pair quantum (h = 2q offset-lattice matching)

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler), run on
Jeremy's line ("the (k/4)^2 dyon is the reason the 4 exists";
test approved by Jeremy). **Parents:** v14.768 (grid theorem,
conditional), v14.731 (dyon pair, two routes), v14.735 (angular
unification; fibration weights 1 vs 2), v14.865 (ladder-edge
parabolas; flag quarter_grid_operator_selection=NOT_DERIVED),
v14.550 (diameter-secant machine), v14.592 (Maslov quarter -
different type, see sec.3). **Status:** the identity chain is [D]
given one dictionary-consistency premise (sec.2), stated as a
premise, not smuggled. **Collision check:** immediately before
writing, live master HEAD `6a95f92f80bdb4efcc99e2ee5addd8df382a34ac`
(v14.903, Audit R356); v14.904 next free. Payload:
`payloads/weld_test_v14_904/` (NOTE.md, weld_check.py).

## 1. The objects

Factor grid (v14.768): members x = h a, y = h b (a, b in Z+),
shell n = a b, r_h(n) = log(h^2 n) = 2 psi_{n,c}, c = h^{-2},
vertices +-h/2. Mesh crossings (canonical mesh formulas +
v14.550): row x and column y cross at offset X = (x-y)/2,
GM = sqrt(xy), AM = (x+y)/2; hence the grid's crossing offsets
are h(a-b)/2 - the lattice (h/2) Z, exactly. The offset slot's
physical occupant is the pair product (v14.731 sec.3 [D]), and
its quantisation is derived (v14.731 sec.1/4): EM eg/hbarc in
(1/2) Z (Dirac single-valuedness); gravity mu c l/hbar in
(1/4) Z (Killing-triad closure; Misner periodicity; G cancels).
Write q for the pair-product quantum: q_EM = 1/2, q_G = 1/4.
Dyon seats sit on crossings (centre k/2 = AM coordinate,
offset s/2 = offset coordinate, v14.731 sec.2).

## 2. The weld

Premise (dictionary consistency): the dictionary grid's nodes
are the states, so its crossings must sit at physically allowed
offsets - no finer (nodes without states overcount) and no
coarser (states without nodes are missed). Allowed offsets:
q Z. Grid offsets: (h/2) Z. Therefore

  h/2 = q,   h = 2q,   c = (2q)^{-2},   vertex = +-q.

Exact-rational check (weld_check.py, DONE): EM - q = 1/2 gives
h = 1, c = 1, r = log n, vertices +-1/2; gravity - q = 1/4
gives h = 1/2, c = 4, r = log(n/4), vertices +-1/4. Both
observed grids are reproduced from the derived pair quanta
with no free choice. In both sectors r = 0 sits at shell
n = c, the shell carrying the unit raw pair (1, 1) (diagonal
pair a = b = 1/h): the counting starts where the first
complete pair fits. Suzuki's diagonal (D_log)_nn = log(n/4)
(v13.301) equals r_{2 q_G}(n): its /4 is (2 q_G)^{-2} - the
dyon pair quantum's denominator structure. Jeremy's conjecture
is confirmed at dictionary level: the 4 exists because the
gravity pair quantum is 1/4.

Vertex form: vertices are +-q - the ladder parabolas of
v14.865 (u = 1) sit at +-q_EM; the gravity dictionary's are
the u = 2 q_G dilation. This answers v14.865's
quarter_grid_operator_selection with a selection principle:
offset-lattice matching.

## 3. Boundaries

(i) The premise of sec.2 is a consistency principle of the
dictionary, not a theorem of GR or of Suzuki's theory; a
sceptic may still call the grid a chosen parametrisation
(v14.865's "u is coordinate choice"). The weld shows the
choice is forced once the dictionary is required to count
exactly the physical pair states - the project's standing use
of the dictionary, and the reason behind v14.768's
shared-normalisation condition (the operator's rows are the
dictionary's states).
(ii) The rival quarter is the wrong type: v14.592's Maslov/
Langer quarter is an additive action shift ((n - 1/4) in the
bouncer rule), not a lattice denominator; the /4 in log(n/4)
is multiplicative, and only the pair-product lattice has
denominator structure.
(iii) Nothing here derives G, alpha_G, or the hierarchy psi;
NUT charge remains unobserved; the pair selector (which pair
is realised) is unchanged. This welds the pair dictionary to
the operator dictionary.

**Flags:** `weld_h_eq_2q=EXACT_BOTH_SECTORS`;
`counting_start=c=(2q)^-2_DERIVED_AT_DICTIONARY_LEVEL`;
`premise=node_equals_state_consistency (stated, not proved)`;
`quarter_grid_operator_selection=ANSWERED_BY_OFFSET_LATTICE_MATCHING`;
`G_derived=false`; `Suzuki_payloads_touched=false`;
`far_tail_touched=false`.
