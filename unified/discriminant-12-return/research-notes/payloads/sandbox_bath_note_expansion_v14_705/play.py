# EFT PLAY: translate v3.4's hot-bath fixed point into cone coordinates, verify, simulate.
# Dictionary (from the corpus): epicycle radii A=sqrt(x), B=sqrt(y); x=T+X, y=T-X, Y=sqrt(xy).
# Ellipse semi-axes a=A+B, b=|A-B| -> e^2 = 4AB/(A+B)^2 = 2Y/(T+Y);  q^2 = 1-e^2 = (T-Y)/(T+Y).
import mpmath as mp, random
mp.mp.dps = 15
random.seed(7)
worst = 0
for _ in range(2000):
    A, B = sorted([random.uniform(0.05, 3), random.uniform(0.05, 3)], reverse=True)
    x, y = A*A, B*B; T, X, Y = (x+y)/2, (x-y)/2, mp.sqrt(x*y)
    a, b = A+B, A-B
    e_direct = mp.sqrt(1-(b/a)**2)
    e_cone = mp.sqrt(2*Y/(T+Y))
    worst = max(worst, abs(e_direct-e_cone))
print(f"dictionary check over 2000 random ellipses: max |e_direct - e_cone| = {mp.nstr(worst,3)}")
print(f"fixed point: q0^2=1/3 -> (T-Y)/(T+Y)=1/3 -> Y/T = 1/2 ; direction X:Y:T = sqrt(3) : 1 : 2")
print(f"null-coord ratio on attractor ray: (T+X)/(T-X) at (sqrt3,1,2) = {mp.nstr((2+mp.sqrt(3))/(2-mp.sqrt(3)),8)} = 7+4sqrt(3) = {mp.nstr(7+4*mp.sqrt(3),8)}")
# Reduced hot-limit shape flow: dq/dt = -C (3q^2-1)/q  (sign structure of v3.4 <Ls>, s=1-q, C>0)
def flow(q0, C=0.35, tmax=30, dt=0.005):
    q, t, out = q0, 0.0, []
    while t < tmax:
        out.append((t, mp.sqrt(1-q*q)))
        q += -C*(3*q*q-1)/q*dt; t += dt
    return out
for q0 in [0.08, 0.3, 0.577, 0.85, 0.99]:
    tr = flow(q0); print(f"  start e={mp.nstr(mp.sqrt(1-q0*q0),4)} -> end e={mp.nstr(tr[-1][1],6)} (target sqrt(2/3)={mp.nstr(mp.sqrt(2/3),6)})")
