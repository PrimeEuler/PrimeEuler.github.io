"""
No-self-standing-gravity theorem -- computational proof components
(sandbox, 2026-10-29).

Standing wave := a shell chain terminated at both ends (a finite unitary
SU(2) multiplet). Uses the chain audit of rep_boundary_test.py and adds
the two new components:
  (C) Closure is impossible from inside: adjoining the missing state
      X* (one J-step past an open end) gives it a NEGATIVE outward norm
      factor with the shell's own Casimir -- a ghost. Truncating instead
      leaves the commutator defect of v15.140. The only consistent
      closure supplies X* from a different shell (its own Casimir),
      where it is a genuine endpoint.
  (D) The escape never terminates: following the missing end from shell
      to shell (T -> T + 1/2) stays in odd shells forever, escape
      weights T + 1/4 growing without bound -- the unbounded ladder
      has no standing waves at any stage.
"""
from fractions import Fraction as F
from collections import defaultdict

def chains_of(T):
    nodes = [-T + F(i, 2) for i in range(int(4 * T) + 1)]
    ch = defaultdict(list)
    for X in nodes:
        ch[X % 1].append(X)
    return {c: sorted(v) for c, v in ch.items()}

def outward_factor(T, X, side):
    # squared J matrix element from state X one step OUTWARD (beyond the end)
    if side == 'top':
        return (T - X) * (T + X + 1)
    return (T + X) * (T - X + 1)

print("(C) closure obstruction at every open end, shells T = 1/4 .. 5/2")
bad = 0
for t4 in range(1, 11):
    T = F(t4, 4)
    for c, ch in chains_of(T).items():
        ends = []
        if ch[-1] != T:
            ends.append(('top', ch[-1] + 1))
        if ch[0] != -T:
            ends.append(('bottom', ch[0] - 1))
        for side, Xs in ends:
            ghost = outward_factor(T, Xs, side)
            # Xs as endpoint of its own shell T' = |Xs|: outward factor there
            Tp = abs(Xs)
            own = outward_factor(Tp, Xs, side)
            if ghost != -(T + F(3, 4)) or own != 0:
                bad += 1
            print(f"  T={str(T):>4} class {c}: missing state X*={Xs}  "
                  f"ghost factor in shell T: {ghost}   outward factor in own shell {Tp}: {own}")
print("  violations of [ghost = -(T + 3/4), own-shell factor = 0]:", bad)

print()
print("(D) escape iteration: follow the missing end upward")
T, Xs = F(1, 4), F(1, 4)   # start: T=1/4, the state X=1/4 itself
seen = []
for step in range(10):
    Tp = abs(Xs)
    ch = chains_of(Tp)[Xs % 1]
    assert Xs in ch and (ch[0] == Xs or ch[-1] == Xs), "X* must be an endpoint of its shell"
    closed = (ch[0] == -Tp and ch[-1] == Tp)
    if ch[-1] == Tp and ch[0] != -Tp:
        side, nxt = 'bottom', ch[0] - 1
    elif ch[0] == -Tp and ch[-1] != Tp:
        side, nxt = 'top', ch[-1] + 1
    else:
        side, nxt = 'BOTH/NEITHER', None
    esc = outward_factor(Tp, ch[-1] if side == 'top' else ch[0], side) if side in ('top', 'bottom') else None
    # escape weight = inward element at the fragment's open end:
    escw = (Tp + F(1, 4))
    seen.append((Tp, closed))
    print(f"  step {step}: shell T={Tp} chain class {Xs % 1} ({len(ch)} states), closed={closed}, "
          f"escapes at {side} with weight {escw}, missing state {nxt}")
    if nxt is None:
        break
    Xs = nxt
print("  all visited shells odd quarters:", all(T.denominator == 4 for (T, _) in seen),
      " none closed:", all(not c for (_, c) in seen))
print("ALL CHECKS DONE")
