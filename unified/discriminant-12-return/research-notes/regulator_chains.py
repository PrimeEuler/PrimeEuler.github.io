import mpmath as mp
mp.mp.dps = 40
Dirac = mp.mpf('2.26866143917643529e39')
psiD = mp.log(Dirac)/2
halfwin = mp.mpf('1.1e-5')
print(f"psi_D = {mp.nstr(psiD, 12)}  window +/-{halfwin}\n")

# Fundamental units of the real quadratic fields behind the channel table (v14.612).
# (d, chi label): eps_d = minimal unit > 1 of Q(sqrt(d)); step = ln eps_d (the field's regulator).
fields = {
    5:  (mp.mpf(1)+mp.sqrt(5))/2,      # chi_5
    2:  1+mp.sqrt(2),                  # chi_8 (Q(sqrt2))
    3:  2+mp.sqrt(3),                  # chi_12 (Q(sqrt3)) -- the D12 field
    13: (mp.mpf(3)+mp.sqrt(13))/2,     # chi_13
    21: (mp.mpf(5)+mp.sqrt(21))/2,     # chi_21
    6:  5+2*mp.sqrt(6),                # chi_24 (Q(sqrt6))
}
steps = {d: mp.log(e) for d, e in fields.items()}
for d, s in steps.items():
    print(f"  Q(sqrt({d})): eps = {mp.nstr(fields[d], 10)}   regulator step = {mp.nstr(s, 10)}")

print("\nUniform regulator chains  m * ln(eps_d) vs psi_D:")
for d, s in steps.items():
    m = int(mp.nint(psiD/s)); resid = abs(m*s - psiD)
    print(f"  d={d:2d}: m={m:3d}  resid={mp.nstr(resid,4)}{'  <<< HIT' if resid < halfwin else ''}")

print("\nTwo-field mixes  a*ln(eps_d1) + b*ln(eps_d2), a,b in [0,300]:")
import itertools
hits = []
for (d1, s1), (d2, s2) in itertools.combinations(steps.items(), 2):
    amax = int(psiD/s1) + 1
    near = 0; total_near = 0
    best = (mp.inf, None)
    for a in range(amax + 1):
        rem = psiD - a*s1
        b = int(mp.nint(rem/s2))
        if b < 0 or b > 300: continue
        resid = abs(a*s1 + b*s2 - psiD)
        if resid < best[0]: best = (resid, (a, b))
        if resid < mp.mpf('0.01'): near += 1
    # chance: values a*s1+b*s2 have local density ~ (count within +-0.01)/(0.02) per unit;
    # expected hits in +-1.1e-5 ~ near * (2.2e-5/0.02) with 'near' measured on a +-0.01 band
    exp_hits = near * (2*halfwin/mp.mpf('0.02'))
    tag = ""
    if best[0] < halfwin:
        tag = "  <<< HIT"; hits.append((d1, d2, best))
    print(f"  d=({d1},{d2}): best resid={mp.nstr(best[0],4)} at (a,b)={best[1]}  "
          f"in-band(+-0.01)={near}  expected window hits by chance ~ {mp.nstr(exp_hits,3)}{tag}")
print("\nHITS:", hits if hits else "none")
