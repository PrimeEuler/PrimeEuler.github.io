# Weld test — is the /4 in Suzuki's log(n/4) the dyon pair quantum?

Run 2026-10-26, sandbox (little Euler), on Jeremy's line.
Conjecture (Jeremy, 2026-10-26): "the (k/4)^2 dyon is the reason
the 4 exists" — the operator's counting start (log(n/4), unit
point at n = 4) is the dyon pair product's denominator.

## Objects (all [D] in the ledger)

- Factor grid (v14.768): members x = h a, y = h b (a, b in Z+),
  shell n = a b, radial coordinate r_h(n) = log(h^2 n) =
  2 psi_{n,c} with c = h^{-2}, boost beta = (1/2) log(a/b),
  vertices +-h/2. Observed: EM dictionary h = 1 (r = log n);
  Suzuki diagonal (D_log)_nn = log(n/4) (v13.301) = r_{1/2}(n).
- Mesh crossings: row x, column y cross at X = (x - y)/2
  (offset), Y = sqrt(xy) (GM), T = (x + y)/2 (AM) — the
  diameter-secant triple (v14.550). Crossing offsets are
  h(a - b)/2: the grid's offset values form the lattice
  (h/2) Z, exactly.
- The offset slot's physical occupant is the pair product
  (v14.731 sec.3 [D identity]). Its quantisation is derived:
  EM eg/hbarc in (1/2) Z (Dirac single-valuedness);
  gravity mu c l / hbar in (1/4) Z (Killing-triad closure and
  Misner periodicity, two routes, G cancels) (v14.731 sec.1/4).
  Write q for the pair-product quantum: q_EM = 1/2, q_G = 1/4.
  Dyon seats sit on crossings: centre k/2 = T, offset s/2 = X
  (v14.731 sec.2).

## The weld

Premise (dictionary consistency): the dictionary grid's nodes
are the states. Its crossings must therefore sit at physically
allowed offsets — no finer (nodes with no states: the
dictionary overcounts) and no coarser (states with no nodes).
The allowed offsets are q Z (the pair-product lattice). The
grid's offsets are (h/2) Z. Hence

  h/2 = q,   i.e.   h = 2q,   c = (2q)^{-2},   vertex = +-q.

Check (exact rationals, weld_check.py, DONE):
  EM: q = 1/2 -> h = 1,   c = 1, r = log n,     vertices +-1/2.
  G:  q = 1/4 -> h = 1/2, c = 4, r = log(n/4), vertices +-1/4.
Both observed grids are reproduced from the derived pair
quanta with no free choice. r = 0 sits at shell n = c in both
sectors, and that shell is the one carrying the unit raw pair
(1, 1) (diagonal pair a = b = 1/h, raw members h a = 1): the
counting starts where the first complete pair fits, literally.

The vertex statement closes v14.865's flag in dictionary form:
vertices are +-q — the ladder parabolas (u = 1) sit at
+-q_EM = +-1/2, the gravity dictionary's at the u = 2 q_G
dilation, +-1/4. quarter_grid_operator_selection is answered
by offset-lattice matching: the sector's grid is the one whose
offset lattice equals its pair-product lattice.

The rival quarter has the wrong type: the Maslov/Langer
quarter of v14.592 is an additive action shift ((n - 1/4) in
the bouncer's Bohr-Sommerfeld rule), not a lattice
denominator; the /4 in log(n/4) is multiplicative (a grid
scale), and the pair-product lattice is the only quarter in
the record with denominator structure.

## Verdict and boundaries

Jeremy's conjecture is CONFIRMED at dictionary level: the 4 in
log(n/4) is (2 q_G)^{-2} with q_G = 1/4 the derived dyon pair
quantum — the /4 exists because the gravity pair quantum is
1/4, via h = 2q. Steps 1-2 and the arithmetic are [D]. The one
non-[D] step is the premise: node = state consistency of the
dictionary. A skeptic can still call the grid a chosen
parametrisation (v14.865's "u is coordinate choice"); the weld
shows the choice is forced once the dictionary is required to
count exactly the physical pair states — which is the
project's standing use of the dictionary (v14.768's
shared-normalisation condition, now supplied with a reason:
the operator's rows are the dictionary's states, and its
diagonal's /4 is the pair quantum of the gravity sector).

Not touched: G and alpha_G are not derived; psi (the hierarchy)
is untouched; NUT charge remains unobserved; the dyon's
selector slot (which pair is realised) is unchanged. This
welds the pair dictionary to the operator dictionary; it does
not derive a coupling.
