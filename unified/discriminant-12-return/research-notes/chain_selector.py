import mpmath as mp
mp.mp.dps = 40

# Target: psi_D = (1/2) ln(Dirac), Dirac from v14.616 (30 dps).
Dirac = mp.mpf('2.26866143917643529e39')
psiD = mp.log(Dirac) / 2
# Dirac is meaningful to ~5 sig figs (rel. unc. 2.2e-5, all from G) -> psi window half-width:
halfwin = mp.mpf('1.1e-5')
print(f"psi_D = {mp.nstr(psiD, 14)}   hit window = +/-{halfwin}")

# Candidate uniform ratios, FIXED IN ADVANCE from the machine's native sets:
cands = {}
for n in range(1, 12):                       # consecutive ratios (the dictionary family (n+1)/n)
    cands[f"({n+1})/{n}"] = mp.mpf(n+1) / n
for p in (2, 3, 5, 7, 11):                   # prime pair steps (p,1)
    cands[f"{p}/1"] = mp.mpf(p)
cands["12/1"] = mp.mpf(12)                   # the diameter itself
cands["sqrt-step 2 (rapidity ln2)"] = mp.mpf(2)  # alias of 2/1 step counted once below

print("\nUniform chains  m * (1/2) ln r  vs psi_D:")
results = []
chance = mp.mpf(0)
for name, r in cands.items():
    step = mp.log(r) / 2
    m = int(mp.nint(psiD / step))
    if m < 1: continue
    resid = abs(m * step - psiD)
    chance += 2 * halfwin / step            # per-ratio chance of a hit somewhere along m
    results.append((resid, name, m, step))
    flag = "  <<< HIT" if resid < halfwin else ""
    print(f"  r={name:26s} step={mp.nstr(step,8)}  m={m:5d}  resid={mp.nstr(resid,4)}{flag}")
print(f"\nexpected chance hits over the whole scan ~ {mp.nstr(chance, 3)}")
best = min(results)
print(f"best: r={best[1]}, m={best[2]}, resid={mp.nstr(best[0],4)}  (window {halfwin})")
