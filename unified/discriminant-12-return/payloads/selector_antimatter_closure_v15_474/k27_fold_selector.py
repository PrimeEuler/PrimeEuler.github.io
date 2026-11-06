"""
The k=27 rung + the selector for the reading level
(2026-11-06, sandbox; the open frontier after v15.473:
why is the tower read at k=9 -- H1's level -- and what
lives one rung up?)

The frame is antimatter-complete by its own construction
(v15.388): every slot's conjugate is a slot. At the address
level that is a sharp predicate on any proposed reading
level 3^m: the observed tower's class set
    S_m = { (tau + 3g) mod 3^m : tau in -1,0,1; g = 0,1,2 }
must be closed under negation (the conjugate's address
must be an occupied address). Together with refinement
(the level must see more than the tau shadow, capacity
per tau > 1) this SELECTS the level:

    m   level  capacity/tau  occupied  antimatter-closed?
    1      3        1           3       yes (collapse: no
                                        generation structure)
    2      9        3           9       YES -- by exhaustion
                                        (9 slots = 9 classes)
    3     27        9           9       NO (conjugates land on
                                        empty addresses)
    4     81       27           9       NO

m = 2 is the UNIQUE refining level at which the observed,
antimatter-complete tower closes. Going up (the k=27 rung)
does not deepen the fold; it breaks the frame's own
completion -- the conjugates of occupied slots fall on the
18 empty classes. The ladder's capacity grows as 3^(m-1)
per tau, but occupancy stays 9 slots: above m = 2 the
machinery and the world disagree about antimatter.

What this does to H1: the hypothesis was "the frame's
third mode IS a k=9 list's distinguished mode," with the
level looking like a free choice (the selector question).
Within flat readings the level is not free: it is forced
to 9 by closure + refinement, given the observed tower
(3 generations, antimatter-complete -- both empirical).
What remains of H1 is flatness itself (v15.467: the 9
cannot be assembled by tripling k=3; it must be a genuine
flat list) -- the identification, with its level now
selected rather than stipulated. The count is still not
derived from nothing: the tower's observed 3 is an input
to the closure test. But the explanation's direction
sharpens -- an antimatter-complete tower that exactly
EXHAUSTS its reading level has #slots = level, and the
observed 9 slots (3 tau x 3 g) force level 9.

Also verified: the negation digit rule at 27 (mixed-radix
borrow rule, the v15.461 rule one digit deeper), and the
address remark: at reading 27 the frame address would be
mod 54 = 2 x 27; closure fails already in the 27
component, so the standing address remains Z18 (v15.467).
"""
print("=" * 76)
print("the ladder: capacity, occupancy, antimatter closure by level")
print("=" * 76)
TAUS = (-1, 0, 1)
GS = (0, 1, 2)
for m in (1, 2, 3, 4):
    L = 3 ** m
    S = sorted({(t + 3 * g) % L for t in TAUS for g in GS})
    capacity = 3 ** (m - 1)
    closed = all((-c) % L in S for c in S)
    refines = capacity > 1
    print(f"  m={m} level={L:3d}: capacity/tau={capacity:2d}, occupied "
          f"classes={len(S):2d} of {L:3d}, closed={closed}, "
          f"refines={refines}  -> {'SELECTED' if closed and refines else 'no'}")

print()
print("=" * 76)
print("the k=27 rung in detail: occupied classes and their conjugates")
print("=" * 76)
L = 27
def digits(c):
    t0 = c % 3
    d1 = ((c - t0) // 3) % 3
    d2 = ((c - t0 - 3 * d1) // 9) % 3
    return t0, d1, d2
S = sorted({(t + 3 * g) % L for t in TAUS for g in GS})
print("  slot (tau, g) -> class (tau0, d1, d2) | conjugate class, in S?")
for t in TAUS:
    for g in GS:
        c = (t + 3 * g) % L
        cc = (-c) % L
        print(f"    ({t:+d}, {g}) -> {c:2d} {digits(c)} | {-c % L:2d} "
              f"{digits(cc)} {'YES' if cc in S else 'NO -- empty address'}")

print()
print("=" * 76)
print("negation digit rule at 27 (borrow rule, verified on all 27 classes)")
print("=" * 76)
def neg_digits(t0, d1, d2):
    t0n = (-t0) % 3
    b1 = 1 if t0 != 0 else 0
    d1n = (-d1 - b1) % 3
    b2 = 1 if (d1 + b1) != 0 else 0
    return t0n, d1n, (-d2 - b2) % 3
ok = all(digits((-c) % 27) == neg_digits(*digits(c)) for c in range(27))
print(f"  (t0,d1,d2) -> ((-t0)%3, (-d1-b1)%3, (-d2-b2)%3), b1 = [t0>0 in")
print(f"  canonical reps: t0 != 0], b2 = [d1 + b1 != 0]: verified = {ok}")
print("  this is v15.461's rule (digit -> -digit - [tau>0]) one digit")
print("  deeper: each digit's flip borrows from the digit below.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("The selector exists and is internal: within flat")
print("readings, antimatter closure (the frame's own completion,")
print("v15.388) plus refinement select the level UNIQUELY --")
print("k=9. One rung down collapses the generations; one rung")
print("up (k=27) breaks the completion, stranding conjugates")
print("on 18 empty addresses. H1 is thereby upgraded: its")
print("level is no longer stipulated but forced, given the")
print("observed tower; its remaining content is flatness (a")
print("genuine flat 9-list, per v15.467's no-tripling verdict).")
print("The generation count is still not derived from nothing")
print("-- the observed 3-generation, antimatter-complete tower")
print("is an input -- but the machinery now explains why, IF")
print("the tower is read flatly at all, it is read at 9: it is")
print("the only level where the frame and its antimatter")
print("completion describe the same world. The k=27 rung is")
print("closed as a reading level (capacity 9/tau, occupancy 3,")
print("closure fails); the standing address remains Z18.")
