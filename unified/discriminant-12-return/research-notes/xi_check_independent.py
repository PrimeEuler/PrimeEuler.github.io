"""Independent re-check of v13.917's Phi(tau) cosine-transform zero claim.
Fresh code, hardcoded reference zeta-zero ordinates (not pulled from the
ledger or its script), independent series/quadrature implementation.
"""
import mpmath as mp
mp.mp.dps = 40

def Phi(tau):
    t = abs(mp.mpf(tau))
    s = mp.mpf(0)
    m = 1
    while True:
        a = mp.e**(2*t)
        term = (4*mp.pi**2*m**4*mp.e**(mp.mpf(9)/2*t) - 6*mp.pi*m**2*mp.e**(mp.mpf(5)/2*t)) * mp.e**(-mp.pi*m*m*a)
        s += term
        if m > 2 and abs(term) < mp.mpf('1e-50'):
            break
        m += 1
    return s

def cosine_transform(gamma):
    f = lambda t: Phi(t) * mp.cos(gamma*t)
    return 2*mp.quad(f, [0, 0.3, 0.6, 1.0, 1.5, 2.2, 3.0])

# standard reference values for the first 5 nontrivial zeta zero ordinates
# (well-known tabulated constants, not computed from the ledger's own machinery)
known_gammas = [
    mp.mpf('14.134725141734693790'),
    mp.mpf('21.022039638771554993'),
    mp.mpf('25.010857580145688763'),
    mp.mpf('30.424876125859513210'),
    mp.mpf('32.935061587739189691'),
]

print("Independent check: cosine transform of Phi at known zeta zero ordinates")
for k, g in enumerate(known_gammas, 1):
    r = cosine_transform(g)
    print(k, float(g), mp.nstr(r, 6))

# also check it's NOT zero at a generic non-zero point, as a negative control
print("\nNegative control (should NOT be ~0):")
for g in [mp.mpf('10'), mp.mpf('20'), mp.mpf('17.5')]:
    r = cosine_transform(g)
    print(float(g), mp.nstr(r, 6))
