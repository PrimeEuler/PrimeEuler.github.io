import mpmath as mp
mp.mp.dps = 40
Dirac = mp.mpf('2.26866143917643529e39')
psiD = mp.log(Dirac)/2
halfwin = mp.mpf('1.1e-5')
alpha = 1/mp.mpf('137.035999084')
lna = -mp.log(alpha)                      # ln(1/alpha) = 4.9202437...
print(f"psi_D = {mp.nstr(psiD, 12)}   ln(1/alpha) = {mp.nstr(lna, 10)}")

print("\nEM-step uniform chains  m * step  vs psi_D:")
for name, step in [("-ln alpha", lna), ("-(1/2) ln alpha", lna/2), ("-ln alpha / (2pi)", lna/(2*mp.pi))]:
    m = int(mp.nint(psiD/step)); resid = abs(m*step - psiD)
    print(f"  step={name:22s} = {mp.nstr(step,8)}  m={m:4d}  resid={mp.nstr(resid,4)}"
          f"{'  <<< HIT' if resid < halfwin else ''}")

print("\nBest uniform chain (4/3)^315 corrected by k EM steps  k*(-ln alpha), k=-3..3:")
base = 315 * mp.log(mp.mpf(4)/3)/2
for k in range(-3, 4):
    resid = abs(base + k*lna - psiD)
    print(f"  k={k:+d}: resid={mp.nstr(resid,4)}{'  <<< HIT' if resid < halfwin else ''}")

print("\nPure alpha-power reading: ln(alpha_G)/ln(alpha) should be an integer if alpha_G = alpha^m:")
alphaG = mp.mpf('5.906e-39')
print(f"  ln(alpha_G)/ln(alpha) = {mp.nstr(mp.log(alphaG)/mp.log(alpha), 8)}   (integer would be a hit; Eddington zone)")

print("\nTotient-restricted consecutive ladder (units of 12), per-12-block sum:")
blk = sum(mp.log(mp.mpf(n+1)/n)/2 for n in (1, 5, 7, 11))
nb = int(mp.nint(psiD/blk))
print(f"  block step = {mp.nstr(blk,8)}   blocks={nb}  resid={mp.nstr(abs(nb*blk-psiD),4)}")
