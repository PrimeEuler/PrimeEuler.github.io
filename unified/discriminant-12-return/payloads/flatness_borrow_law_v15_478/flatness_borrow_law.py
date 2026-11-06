"""
Flatness: the borrow is the signature (2026-11-06, sandbox;
door II digging -- H1's residue after the v15.474 selector
forced the level).

H1 said: the frame's third mode IS a flat k=9 list's
distinguished mode. Two sub-questions were bundled in it:
(a) FLATNESS -- is the fine digit a second base-3 digit of
    the ONE occupation integer c (flat Z9, cyclic, order-9
    classes), or an independent second Z3 (nested Z3 x Z3,
    exponent 3, v15.467's alternative)?
(b) REALITY -- is the digit read by anything (= H2)?

This build settles (a) as a property of the frame's
construction, by the conjugation law. The two candidates
give different conjugations on the 9 classes (canonical
digits (tau0, d): class = tau0 + 3d):
  FLAT:   p(c) = -c mod 9; digit law d -> -d - [tau0 > 0]
          (the BORROW: negating the integer carries).
  NESTED: p(tau0, d) = (-tau0, -d) componentwise; digit
          law d -> -d (borrow-free).
Pairings differ on 6 of the 8 non-fixed classes.
The frame's conjugation is c -> -c on the split-grading
integer (the b-sector completion, v15.388), and v15.461
machine-verified the BORROW law against it on all classes.
A borrow-free law would require the digit to be a second
independent grading -- a second distinguished mode. The
frame has exactly one: the digit is a digit OF c, and its
step is the integer's +1 step, carries included (period 9
on classes; order-9 elements exist). Flatness is therefore
not an added hypothesis but the frame's own arithmetic.
(Notation check, done in the build: in signed (tau, gamma)
coordinates the two pairings coincide -- the invariant
discriminator is the step/carry structure, and it is the
borrow in canonical digits that exhibits it.)

Consequence: H1 collapses. Its content was flatness
(construction arithmetic -- here) + level (forced by
closure + refinement, v15.474) + reality of the digit.
The first two are settled; the third IS H2, verbatim.
Door II's two hypotheses merge into the single empirical
question: does anything read the second digit? (Locus
narrowed at v15.472: the charged-lepton mass sector.)
Scope: flatness is settled as a property of THIS frame's
construction; the standing identification of the frame
with nature's labels is v15.388's, untouched. If nothing
reads the digit, the operative modulus is 3 and the fold
is bookkeeping -- which is H2's question, not H1's.
"""
print("=" * 76)
print("the two conjugation pairings on the 9 classes")
print("=" * 76)
def digits(c):
    return c % 3, ((c - (c % 3)) // 3) % 3
def from_digits(t0, d):
    return (t0 + 3 * d) % 9
def pairs(p):
    seen, out = set(), []
    for c in range(9):
        if c in seen:
            continue
        q = p(c)
        seen |= {c, q}
        out.append((c, q))
    return out
flat = pairs(lambda c: (-c) % 9)
def nest(c):
    t0, d = digits(c)
    return from_digits((-t0) % 3, (-d) % 3)
nested = pairs(nest)
print(f"  FLAT   (one integer, -c mod 9):      {flat}")
print(f"  NESTED (two digits, componentwise):  {nested}")
diff = [c for c in range(9)
        if ((-c) % 9) != nest(c)]
print(f"  pairings differ on classes: {diff} (6 of 8 non-fixed)")

print()
print("=" * 76)
print("the digit laws: the borrow is the carry of the one integer")
print("=" * 76)
flat_law_ok = all(
    digits((-c) % 9) == ((-digits(c)[0]) % 3,
                         (-digits(c)[1] - (1 if digits(c)[0] > 0 else 0)) % 3)
    for c in range(9))
nest_law_ok = all(
    digits(nest(c)) == ((-digits(c)[0]) % 3, (-digits(c)[1]) % 3)
    for c in range(9))
print(f"  flat law  d -> -d - [tau0>0], tau0 -> -tau0: exact = {flat_law_ok}")
print(f"  nested law d -> -d (borrow-free):            exact = {nest_law_ok}")
print("  (both are exact as maps -- on DIFFERENT pairings. The")
print("  frame's conjugation is c -> -c on the grading integer")
print("  (v15.388 b-sector), and v15.461 verified the BORROW law")
print("  against it: the frame follows the flat pairing.)")

print()
print("=" * 76)
print("step structure: one integer (carries, period 9) vs two digits")
print("=" * 76)
x, seq = 0, []
for _ in range(9):
    seq.append(x)
    x = (x + 1) % 9
print(f"  flat +1 step orbit from 0: {seq} -- one 9-cycle (order-9")
print("  elements exist; Z9). A nested digit pair has two")
print("  independent +1 steps and exponent 3: no 9-cycle exists.")
print("  The frame's tower is a ray over ONE occupation integer")
print("  (base + order, door II anatomy v15.429): its step is")
print("  the integer's step, carries included.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("Flatness is the frame's own arithmetic, not an added")
print("hypothesis: the digit is the second base-3 digit of the")
print("one occupation integer, its conjugation carries the")
print("borrow, and a borrow-free (nested) digit would need a")
print("second distinguished mode the frame does not have.")
print("H1 thereby collapses: flatness (here) + level (forced,")
print("v15.474) + reality of the digit. The first two are")
print("settled; the third is H2 itself. Door II's hypotheses")
print("merge into ONE empirical question -- does anything")
print("read the second digit? -- with its locus already")
print("narrowed to the charged-lepton mass sector (v15.472).")
