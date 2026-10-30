"""
Cone within a cone -- exploration (sandbox, 2026-10-30).
The null (ladder) boundary as the thing everything is measured against.
All exact rationals.

(1) Squared radii per shell and their gaps: AM^2 = T^2, C^2 = T(T+1),
    R^2 = (T+1/2)^2. State depth below the boundary R^2 - C^2 = 1/4;
    escape weight = R^2 - AM^2 = T + 1/4 (the boundary-to-floor gap).
(2) Every shell has exactly TWO open ends; total escape per shell
    = 2T + 1/2, all of it in the non-table chains.
(3) Nesting: the ladder boundary of shell T IS the AM floor of shell
    T + 1/2; the next shell's Casimir circle protrudes past it by
    C(T+1/2)^2 - R(T)^2 = T + 1/2 = R(T) (squared-radius units).
(4) Step intervals in the (X, T) plane, interval = dT^2 - dX^2:
    gravity's quarter steps (single row/column steps) are NULL;
    EM's steps are timelike (shell ladder) or spacelike (in-shell).
"""
from fractions import Fraction as F
from collections import defaultdict

print("(1) squared radii and gaps")
for T in [F(1, 4), F(1, 2), F(5, 4), F(5, 2), F(3)]:
    AM2, C2, R2 = T * T, T * (T + 1), (T + F(1, 2)) ** 2
    print(f"  T={str(T):>4}: AM^2={AM2}  C^2={C2}  R^2={R2}   "
          f"depth R^2-C^2={R2 - C2}   escape R^2-AM^2={R2 - AM2}   C^2-AM^2={C2 - AM2}")
    assert R2 - C2 == F(1, 4) and R2 - AM2 == T + F(1, 4)

print("(2) open ends and total escape per shell, T = 1/4 .. 5")
for t4 in range(1, 21):
    T = F(t4, 4)
    nodes = [-T + F(i, 2) for i in range(int(4 * T) + 1)]
    ch = defaultdict(list)
    for X in nodes:
        ch[X % 1].append(X)
    ends, total = 0, F(0)
    for c, members in ch.items():
        members = sorted(members)
        for side, has in (('top', members[-1] == T), ('bottom', members[0] == -T)):
            if not has:
                ends += 1
                total += T + F(1, 4)
    status = "OK" if (ends == 2 and total == 2 * T + F(1, 2)) else "VIOLATION"
    print(f"  T={str(T):>5}: open ends={ends}  total escape={total}  (2T+1/2={2 * T + F(1, 2)})  {status}")
    assert ends == 2 and total == 2 * T + F(1, 2)

print("(3) nesting across shells")
for T in [F(1, 4), F(1, 2), F(5, 4), F(5, 2), F(3)]:
    R2 = (T + F(1, 2)) ** 2
    Cn2 = (T + F(1, 2)) * (T + F(3, 2))
    print(f"  R(T={T})^2={R2} = AM(T+1/2)^2   C(T+1/2)^2 - R(T)^2 = {Cn2 - R2} = R(T)={T + F(1, 2)}")
    assert Cn2 - R2 == T + F(1, 2)

print("(4) step intervals dT^2 - dX^2 in the (X, T) plane (refined steps dp, dq;"
      " dX=(dp-dq)/4, dT=(dp+dq)/4)")
steps = {
    "gravity row step (1,0)": (1, 0), "gravity column step (0,1)": (0, 1),
    "EM shell ladder (2,2)": (2, 2), "EM oscillator / J step (2,-2)": (2, -2),
    "halfway step (1,1)": (1, 1), "diagonal step (1,-1)": (1, -1),
}
for name, (dp, dq) in steps.items():
    dX, dT = F(dp - dq, 4), F(dp + dq, 4)
    iv = dT * dT - dX * dX
    kind = "NULL" if iv == 0 else ("timelike" if iv > 0 else "spacelike")
    print(f"  {name:32s} dX={dX}  dT={dT}  interval={iv}  {kind}")
print("ALL CHECKS DONE")
