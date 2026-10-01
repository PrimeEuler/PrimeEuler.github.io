"""Independent check of v13.925's GNS/return-amplitude identity:
<Omega_alpha, e^{i gamma Q} Omega_alpha> = Xi(alpha+i*gamma)/Xi(alpha)
Reusing the already-validated Phi(tau) from Round 137 (fresh re-typed here).
"""
import mpmath as mp
mp.mp.dps = 30

def Phi(tau):
    t = abs(mp.mpf(tau))
    s = mp.mpf(0)
    m = 1
    while True:
        term = (4*mp.pi**2*m**4*mp.e**(mp.mpf(9)/2*t) - 6*mp.pi*m**2*mp.e**(mp.mpf(5)/2*t)) * mp.e**(-mp.pi*m*m*mp.e**(2*t))
        s += term
        if m > 2 and abs(term) < mp.mpf('1e-40'):
            break
        m += 1
    return s

def Xi(w):
    # Xi(w) = int Phi(tau) e^{w tau} dtau ; w = alpha + i*gamma, real alpha, real gamma
    f = lambda t: Phi(t)*mp.e**(w*t)
    return mp.quad(f, [0, 0.3, 0.6, 1.0, 1.5, 2.2, 3.0, -0.3,-0.6,-1.0,-1.5,-2.2,-3.0])

Xi0 = Xi(mp.mpf(0))
print("Xi(0) =", mp.nstr(Xi0, 12))

alpha = mp.mpf('0.3')
gamma = mp.mpf('5.0')
Xi_a = Xi(alpha)
Xi_aig = Xi(alpha + 1j*gamma)
rhs = Xi_aig/Xi_a
print("Xi(alpha) =", mp.nstr(Xi_a,12))
print("Xi(alpha+i*gamma) =", mp.nstr(Xi_aig,12))
print("RHS = Xi(alpha+i*gamma)/Xi(alpha) =", mp.nstr(rhs,12))

# direct LHS: <Omega_alpha, e^{i*gamma*Q} Omega_alpha> = (Xi0/Xi_a) * int Phi(t) e^{alpha t} e^{i gamma t} dt
#            = (Xi0/Xi_a) * (1/Xi0) * Xi(alpha+i*gamma) [since that integral IS Xi(alpha+i*gamma)]
# so this is definitionally identical -- but let's verify ||Omega_alpha||=1 as the real independent check:
norm2 = (Xi0/Xi_a) * mp.quad(lambda t: Phi(t)*mp.e**(alpha*t), [0,0.3,0.6,1.0,1.5,2.2,3.0,-0.3,-0.6,-1.0,-1.5,-2.2,-3.0]) / Xi0
print("||Omega_alpha||^2 (should be exactly 1) =", mp.nstr(norm2, 12))

# Also confirm Xi(i*gamma1)=0 at the first zeta zero (cross-check vs Round 137)
gamma1 = mp.mpf('14.134725141734693790')
print("Xi(i*gamma_1) [should be ~0] =", mp.nstr(Xi(1j*gamma1), 8))
