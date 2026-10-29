"""
Representation-boundary test (sandbox, 2026-10-29; gate relayed from Chat).

Question: does the odd-quarter sector admit a mathematically natural
representation compatible with the cone's quarter-step operator, the way
the even sector reduces to the Schwinger ladder? Or is the parity split
merely a geometric grading?

Setup: shell T (j = T), states at offsets X = -T + i/2 (i = 0..4T) --
the refined table's shell nodes. J+-type transitions step X by +-1, so a
shell splits into chains by X mod 1. A chain is a genuine SU(2) multiplet
iff it terminates on-cone at BOTH ends (contains m = +T and m = -T, where
the norm factors (j-+m)(j+-m+1) vanish). At an open end, the ladder has a
nonzero matrix element to a state that does not exist on the cone: the
escape weight a^2. Audit over shells T in (1/4)Z:
  - closed chains: count per shell, and T range;
  - escape weights at every open end: universal formula?
Then the operator check: build Jz, J+ (truncated to a chain) and measure
the SU(2) defect diag([J+, J-] - 2 Jz): zero for a true representation,
boundary-localised otherwise.
"""
from fractions import Fraction as F
from collections import defaultdict
import numpy as np

print("PART A -- chain termination audit (exact rationals)")
escapes = set()
for t4 in range(1, 11):
    T = F(t4, 4)
    nodes = [-T + F(i, 2) for i in range(int(4 * T) + 1)]
    chains = defaultdict(list)
    for X in nodes:
        chains[X % 1].append(X)
    nclosed = 0
    desc = []
    for c in sorted(chains):
        ch = sorted(chains[c])
        has_top, has_bot = (ch[-1] == T), (ch[0] == -T)
        if has_top and has_bot:
            nclosed += 1
            desc.append(f"X={c}: CLOSED ({len(ch)} states)")
        else:
            esc = []
            if not has_top:
                e = (T - ch[-1]) * (T + ch[-1] + 1)
                esc.append(f"top escape^2={e}"); escapes.add(e - (T + F(1, 4)))
            if not has_bot:
                e = (T + ch[0]) * (T - ch[0] + 1)
                esc.append(f"bottom escape^2={e}"); escapes.add(e - (T + F(1, 4)))
            kind = "one-ended fragment" if (has_top or has_bot) else "open fragment"
            desc.append(f"X={c}: {kind} ({len(ch)} states; {', '.join(esc)})")
    sector = "EVEN (T in (1/2)Z)" if T.denominator <= 2 else "ODD  (T odd quarter)"
    print(f" T={str(T):>5} [{sector}] closed chains: {nclosed}")
    for d in desc:
        print(f"      chain mod 1 = {d}")
print(" escape weights minus (T + 1/4), all open ends, all shells:", escapes,
      " -> every open end escapes with weight exactly T + 1/4" if escapes == {0} else " MISMATCH")

print()
print("PART B -- SU(2) commutator defect on single chains (Jz = geometric X)")
def defect(T, chain):
    ch = sorted(chain)
    idx = {m: i for i, m in enumerate(ch)}
    n = len(ch)
    Jz = np.diag([float(m) for m in ch])
    Jp = np.zeros((n, n))
    for m in ch:
        if m + 1 in idx:  # transition target exists in this chain
            a = np.sqrt(float((T - m) * (T + m + 1)))
            Jp[idx[m + 1], idx[m]] = a
    Jm = Jp.T
    D = (Jp @ Jm - Jm @ Jp) - 2 * Jz
    return ch, np.diag(D)

cases = [
    (F(2), [F(i) for i in range(-2, 3)], "T=2, integer chain (Schwinger j=2)"),
    (F(1), [F(-1, 2), F(1, 2)], "T=1, halfway chain (Casimir family)"),
    (F(5, 4), [F(5, 4), F(1, 4), F(-3, 4)], "T=5/4, odd chain X=1/4 mod 1"),
    (F(5, 4), [F(3, 4), F(-1, 4), F(-5, 4)], "T=5/4, odd chain X=3/4 mod 1"),
]
for T, chain, name in cases:
    ch, d = defect(T, chain)
    print(f" {name}")
    print(f"   states X = {[str(x) for x in ch]}")
    print(f"   defect diag([J+,J-] - 2Jz) = {np.round(d, 10)}   (T + 1/4 = {float(T + F(1,4))})")
print()
print("Reading: closed chain -> defect 0 (true SU(2) representation).")
print("Fragment -> defect = +(T+1/4) at an open top, -(T+1/4) at an open")
print("bottom, 0 in the interior: SU(2) holds inside the fragment and fails")
print("by exactly the escape weight at the end where the ladder leaves the cone.")
print("ALL CHECKS DONE")
