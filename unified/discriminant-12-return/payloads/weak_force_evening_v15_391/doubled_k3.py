"""
"2 SU(3) glued together?" (2026-11-04, sandbox. Jeremy's joke, run
seriously -- the bicone was built by gluing two SU(2)s, so what does
gluing two k=3 systems give?)

Two 3-mode Schwinger systems, L and R, each carrying SU(3) (p,q)
irreps, with center gradings (tau_L, tau_R) in Z3 x Z3. "Gluing" =
restricting to the DIAGONAL SU(3) (the synchronous combination, the
analog of the bicone's L = J + K; the difference combination is the
axial side).

The construction has a textbook occupant: the chiral flavor symmetry
SU(3)_L x SU(3)_R of the three light quarks, spontaneously broken to
the diagonal SU(3)_V (the eightfold way). Verify its rep content in
the doubled-Schwinger language:

  q_L ~ (3, 1), q_R ~ (1, 3);  qbar_L ~ (3bar, 1), qbar_R ~ (1, 3bar).
  Meson sector qbar_L x q_R = (3bar, 3): diagonal restriction
      3bar x 3 = 8 + 1   (the pseudoscalar nonet's rep content),
      and the SINGLET component is the condensate channel:
      <qbar q> transforms as (3bar, 3), a VEV in its diagonal-singlet
      direction is exactly the glue -- a pairing of L-antiquanta with
      R-quanta that selects the diagonal subgroup.
  Baryon sector q_L^3: 3x3x3 = 10 + 8 + 8 + 1 under the diagonal.
  Diquark q_L^2 = 6 + 3bar: total triality 2, no diagonal singlet.
  Goldstone count: dim(SU(3)xSU(3)) - dim(SU(3)) = 16 - 8 = 8
      = the pseudoscalar octet (pi, K, eta).

SPECIES SEPARATION (the point of filing this carefully): this is
FLAVOR SU(3) acting on (u, d, s) -- global, approximate (explicitly
broken by quark masses). It is NOT the frame's color (p,q), NOT the
weak SU(2)_L chirality of the standing chiral door, and NOT the three
generations (u, d, s = generation 1 plus strangeness). The doubling
pattern has a k=3 occupant, but it lives in flavor space, adjacent to
the completed frame -- it opens none of the standing doors. One
structural difference from the bicone: there the doubling is unbroken
kinematics (Spin(4)); here the physical realization is BROKEN to the
diagonal, and the glue is dynamical (the condensate), not a shell
constraint.
"""

def dim(pq):
    p, q = pq
    return (p + 1) * (q + 1) * (p + q + 2) // 2
def tau(pq):
    return (pq[0] - pq[1]) % 3

# building blocks: ((p,q)_L, (p,q)_R)
BLOCKS = {
    "q_L":    ((1, 0), (0, 0)),
    "q_R":    ((0, 0), (1, 0)),
    "qbar_L": ((0, 1), (0, 0)),
    "qbar_R": ((0, 0), (0, 1)),
}
print("Building blocks under SU(3)_L x SU(3)_R, gradings (tau_L, tau_R):")
for name, (l, r) in BLOCKS.items():
    print(f"  {name:>7}: L{l} x R{r}, dim {dim(l)*dim(r)}, "
          f"gradings ({tau(l)}, {tau(r)})")

print()
print("Diagonal restriction (the gluing) -- composites:")
SECTORS = {
    "meson  qbar_L x q_R": (["qbar_L", "q_R"], [(1, 1), (0, 0)]),
    "baryon q_L x q_L x q_L": (["q_L"] * 3, [(3, 0), (1, 1), (1, 1), (0, 0)]),
    "diquark q_L x q_L": (["q_L"] * 2, [(2, 0), (0, 1)]),
}
for label, (parts, comps) in SECTORS.items():
    d_in = 1; g = [0, 0]
    for p in parts:
        l, r = BLOCKS[p]
        d_in *= dim(l) * dim(r)
        g[0] += tau(l); g[1] += tau(r)
    d_out = sum(dim(c) for c in comps)
    total_tau = (g[0] + g[1]) % 3
    uniform = all(tau(c) == total_tau for c in comps)
    print(f"  {label}: dim {d_in} = {d_out}: {d_in == d_out}; "
          f"(tau_L, tau_R) = ({g[0] % 3}, {g[1] % 3}), diagonal triality "
          f"{total_tau} uniform across components: {uniform}; "
          f"diagonal singlet present: {(0, 0) in comps}")

print()
print(f"Goldstone count: dim G - dim H = (8 + 8) - 8 = {16 - 8} "
      f"= pseudoscalar octet (pi, K, eta)")
print("Condensate channel: <qbar q> ~ (3bar, 3); its diagonal-singlet")
print("component (present above, meson sector) is the order parameter --")
print("the glue is a pairing of L-antiquanta with R-quanta, dynamical,")
print("where the bicone's glue was a shell constraint (j1 = j2).")
print()
print("VERDICT: the doubled k=3 has a real occupant -- chiral flavor")
print("SU(3)_L x SU(3)_R -> SU(3)_V, the eightfold way -- in flavor")
print("space. Adjacent to the frame, not inside it: not color, not the")
print("weak chiral door, not generations.")
