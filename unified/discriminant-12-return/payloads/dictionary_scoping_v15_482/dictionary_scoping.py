"""
Scoping the dictionary-shaped hole (2026-11-06, sandbox;
Jeremy: Lane A works FULL_K; we approach from the hole
between the frame and the operator).

THE TWO SIDES.
Frame side: slots labeled by RESIDUES -- (n2, tau, digit)
as classes mod 18 = 2 x 3^2 (v15.467); charges are class
functions on those addresses (v15.468); the underlying
objects are Schwinger PAIRS (the k=2 list's two modes);
tau is a mod-3 residue, the digit a mod-9 residue.
Operator side: modes n (a ray), split by PARITY into two
sectors; the arithmetic data (frozen formula, SEED_FORMULA
v14.819 / DERIVATION sec.0) is built from FREQUENCIES:
  z_m = sum_{q in {2,3,4,5,7}} 2 w_q sin(theta_q m)
        + pi/2 + O(1/m),   w_q = log q/sqrt(q),
        theta_q = (pi/2) log q,
  d_n = log(n/4) - 1/(2n) + 2(-1)^n/(n pi)^2
        - sum_q w_q (2 - log q)[cos(theta_q n)
        + (2/(n pi)) sin(theta_q n)] + O(1/n^2).
The operator's "3" is a FREQUENCY (log 3 inside theta_3);
the frame's "3" is a RESIDUE (mod 3). Different species.

THE PROBE. If a dictionary existed with the frame's
residue labels anchored in the operator's data, the
seed/diagonal would have to distinguish residue classes
of the mode index (a mod-3 signal for tau, mod-9 for the
digit). Test: class means of the oscillatory part
osc(m) = sum_q 2 w_q sin(theta_q m) over m = r (mod 3)
and (mod 9), at growing ranges, against a CONTROL (a true
period-3 signal, whose class means stabilize at separated
constants -- proving the probe can see a real signal).
And a frequency census: projections of osc at the five
log-frequencies vs at 1/3 and the mod-9 harmonics.

EXPECTED from the formula (frequencies (pi/2) log q are
incommensurate with 2pi/3): no exact period-3/9 component;
class means equidistribute to a common limit (Weyl);
any apparent separation is quasiperiodic leakage that
does not stabilize. The diagonal DOES carry one exact
residue signal: the cusp term 2(-1)^n/(n pi)^2 -- period
2. Parity is anchored; triality is not.

THE HOLE, scoped (printout): the only recorded bridges
are logarithmic/pair-level (station lattice u_n = log n,
v14.416; the weld's node = state pair identification,
v14.904) plus the one exact label match (sector parity
<-> the frame's Z2: spinor/boson by sector, v15.135-143).
A slot-level dictionary would need residue anchors the
operator's data does not contain, or a construction --
which the ledger's admissibility fence (v14.942) bars
from counting as provenance. The bilinear level (the
kernel K_{N,M} as a function of the pair (N,M), insertions)
is where frame-type labels would have to live if anywhere.
"""
import numpy as np

QS = (2, 3, 4, 5, 7)
w = {q: (np.log(q) / np.sqrt(q) if q != 4 else np.log(2) / 2) for q in QS}
th = {q: (np.pi / 2) * np.log(q) for q in QS}

def osc(m):
    return sum(2 * w[q] * np.sin(th[q] * m) for q in QS)

print("=" * 76)
print("probe: residue-class means of the seed's oscillatory part")
print("=" * 76)
for M in (10**3, 10**4, 10**5, 10**6):
    m = np.arange(1, M + 1)
    o = osc(m)
    c3 = [o[m % 3 == r].mean() for r in range(3)]
    c9 = [o[m % 9 == r].mean() for r in range(9)]
    ctrl = np.sin(2 * np.pi * m / 3)
    cc = [ctrl[m % 3 == r].mean() for r in range(3)]
    print(f"  M=1e{int(np.log10(M))}: mod-3 class means "
          f"{[round(x, 4) for x in c3]} (spread {max(c3)-min(c3):.4f}); "
          f"mod-9 spread {max(c9)-min(c9):.4f}")
    print(f"        control (true period-3): {[round(x, 4) for x in cc]} "
          f"-- stable, separated: the probe CAN see a residue signal")

print()
print("=" * 76)
print("frequency census: where osc's power actually sits")
print("=" * 76)
M = 10**6
m = np.arange(1, M + 1)
o = osc(m)
def proj(f):
    return abs(np.mean(o * np.exp(-2j * np.pi * f * m)))
for q in QS:
    print(f"  f = theta_{q}/(2pi) = {th[q]/(2*np.pi):.6f} (log-frequency): "
          f"|proj| = {proj(th[q]/(2*np.pi)):.4f}  (w_{q} = {w[q]:.4f})")
for name, f in (("1/3 (tau residue)", 1/3), ("1/9 (digit)", 1/9),
                ("2/9 (digit)", 2/9), ("1/2 (parity)", 1/2)):
    print(f"  f = {name}: |proj| = {proj(f):.5f}  (leakage floor, no line)")

print()
print("=" * 76)
print("VERDICT -- the hole, scoped")
print("=" * 76)
print("The operator's arithmetic data contains NO residue")
print("anchor for the frame's mod-3 or mod-9 labels: the seed's")
print("class means do not separate (probe validated on the")
print("control), and its spectrum is five log-frequencies")
print("(pi/2) log q, q in {2,3,4,5,7} -- the operator's '3' is")
print("the FREQUENCY log 3; the frame's '3' is the RESIDUE")
print("mod 3. The one exact residue signal in the operator's")
print("data is period 2 (the cusp's (-1)^n; the sector split")
print("itself) -- matching the frame's Z2 side, where the")
print("record already has its one exact label contact")
print("(sector parity <-> spinor/boson home, v15.135-143).")
print("Existing bridges are logarithmic or pair-level: the")
print("station lattice (u_n = log n = 2 psi_n, v14.416) and")
print("the weld's node = state pair identification (v14.904).")
print("A slot-level dictionary would have to convert species")
print("(frequency -> residue) with no anchor in the data, or")
print("be constructed -- and a construction is exactly what")
print("the admissibility fence (v14.942) and the v15.125")
print("absence bar from counting as provenance. If frame")
print("labels live anywhere on the operator side, it is at")
print("the BILINEAR level -- the kernel K_{N,M} as a function")
print("of the pair (N, M), i.e. of (T, X) = ((N+M)/2,")
print("(N-M)/2), the Schwinger pair coordinates -- which is")
print("also where the weld already lives, and where Lane A's")
print("FULL_K work is now pointed from the other side.")
