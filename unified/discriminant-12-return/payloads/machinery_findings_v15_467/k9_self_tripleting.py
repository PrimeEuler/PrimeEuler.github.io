"""
Could k=9 be a self-tripleting of k=3? (2026-11-06, sandbox;
Jeremy's question.) Two faces, two different answers:

DIRICHLET FACE: yes, trivially -- the triple self-convolution
of d_3 is d_9: (zeta^3)^3 = zeta^9, exactly as squaring d_2
gave d_4 and squaring d_3 gave d_6 (v15.466). Self-multiplying
the k=3 member m times lands on k = 3m... here 3*3 = 9 either
way: three factors of zeta^3.

GRADING FACE: no -- and the discriminator is element order.
The fold (v15.461) needs the CYCLIC group Z9: the tower step
c -> c + 3 must cycle through 3 distinct classes, which needs
an element (the class 4 = tau 1, g 1) of order 9. A tripled
k=3 -- three 3-lists, or one list read through three mod-3
channels -- has grading group Z3 x Z3 (x Z3): every element
has order dividing 3, the step c -> c + 3 is 0 in every mod-3
channel, and generations are exactly as invisible as they are
at k=3 alone. Z9 is the center of the FLAT 9-list's U(9);
tripling systems never manufactures an order-9 phase.
What tripling WOULD give: a relative-grading plane Z3^2 --
two independent triality differences among three sectors.
And the fold's own generalization runs along flat lists
k = 3^m: each adds one base-3 digit (k=27: fiber 9 over Z3,
or a second fold over Z9).
"""
from fractions import Fraction as F

NMAX = 40
def d_k(k, n):
    cur = [0] + [1] * n
    for _ in range(k - 1):
        nxt = [0] * (n + 1)
        for a in range(1, n + 1):
            if cur[a]:
                for b in range(1, n // a + 1):
                    nxt[a * b] += cur[a]
        cur = nxt
    return cur

def conv(a, b, n):
    out = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            out[i * j] += a[i] * b[j]
    return out

def order_mod(a, m):
    x, t = a % m, 1
    while x != 0:
        x = (x + a) % m; t += 1
    return t

print("=" * 76)
print("Dirichlet face: triple self-convolution of d_3")
print("=" * 76)
d3, d9 = d_k(3, NMAX), d_k(9, NMAX)
trip = conv(conv(d3, d3, NMAX), d3, NMAX)
print(f"  d_3 * d_3 * d_3 == d_9 (N <= {NMAX}): {trip == d9}")
print("  on the zeta face k=9 IS (k=3) self-tripled -- same sense")
print("  in which the bicone's square of k=2 is k=4 (v15.466).")

print()
print("=" * 76)
print("Grading face: Z9 (flat 9-list) vs Z3 x Z3 (tripled k=3)")
print("=" * 76)
ords9 = sorted({order_mod(a, 9) for a in range(9)})
print(f"  element orders in Z9: {ords9} -- order-9 elements exist")
print(f"  (e.g. class 4 = (tau 1, g 1) has order {order_mod(4, 9)})")
print(f"  element orders in Z3 x Z3: [1, 3] -- maximum order 3")
step = [((c + 3) % 9) != (c % 9) for c in range(9)]
print(f"  tower step c -> c+3 changes the Z9 class: {all(step)}")
print(f"  tower step in ANY mod-3 channel: c mod 3 -> (c+3) mod 3,")
print(f"  unchanged for every c: {all((c + 3) % 3 == c % 3 for c in range(30))}")
print("  a tripled k=3 reads only mod-3 channels (per factor, or")
print("  relatives among factors): the generation step is 0 in all")
print("  of them. The fold's digit is a genuinely order-9 datum.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("As a Dirichlet object, yes: k=9 = (k=3) tripled, (z^3)^3.")
print("As the fold's carrier, no: tripling three k=3 systems gives")
print("grading group Z3^2 (relatives) with exponent 3 -- it cannot")
print("hold the cyclic Z9 class the fold spends. The fold's 9 is")
print("the flat 9-list (one list, AM in ninths, U(9) center Z9);")
print("its base-3 digits are a READING of that flat class, not a")
print("tripling of systems. Tripling instead buys a relative-")
print("grading plane Z3^2 among three sectors -- a different")
print("instrument, should three-sector trialities ever be wanted.")
print("The fold generalizes along flat 3^m lists: k=27 adds a")
print("third base-3 digit (fiber 9 over Z3; a fold over the fold).")
