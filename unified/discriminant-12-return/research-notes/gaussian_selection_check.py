import mpmath as mp
mp.mp.dps = 30

# Check 1: g_a(Y) = e^{-pi a Y^2} + a^{-1/2} e^{-pi Y^2/a} is Fourier self-dual, a != 1
def g(Y, a):
    Y = mp.mpf(Y); a = mp.mpf(a)
    return mp.e**(-mp.pi*a*Y**2) + a**mp.mpf('-0.5')*mp.e**(-mp.pi*Y**2/a)

def fourier(f, xi, a, R=12):
    # numeric FT with convention fhat(xi)=int f(Y) e^{-2pi i Y xi} dY
    re = mp.quad(lambda Y: f(Y,a)*mp.cos(2*mp.pi*Y*xi), [-R,0,R])
    im = mp.quad(lambda Y: -f(Y,a)*mp.sin(2*mp.pi*Y*xi), [-R,0,R])
    return re, im

a = mp.mpf('2.0')
for xi in [0, 0.3, 0.7, 1.5]:
    re, im = fourier(g, xi, a)
    direct = g(xi, a)
    print(f"xi={xi}: FT(g)={mp.nstr(re,10)}+{mp.nstr(im,6)}i   g(xi)={mp.nstr(direct,10)}  match={abs(re-direct)<1e-8}")

print()
# Check 2: Theta_c(x) = sum e^{-c x m^2}; test exact self-duality at c=pi vs c=1
def Theta(x, c, M=40):
    x = mp.mpf(x); c = mp.mpf(c)
    return mp.nsum(lambda m: mp.e**(-c*x*m**2), [-M, M])

for c in [mp.pi, mp.mpf(1)]:
    x = mp.mpf('0.7')
    lhs = Theta(x, c)
    rhs = x**mp.mpf('-0.5') * Theta(1/x, c)
    print(f"c={mp.nstr(c,6)}: Theta(x)={mp.nstr(lhs,10)}  x^-1/2 Theta(1/x)={mp.nstr(rhs,10)}  equal={abs(lhs-rhs)<1e-10}")
