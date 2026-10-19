import mpmath as mp
mp.mp.dps = 50

def lerch_singular_C(a):
    # zeta(2,a) - Phi(e^{-w},2,a) = w*log(1/w) + C*w + o(w).
    # Chat(w) = (Z - Phi - w log(1/w))/w = C + w*(alpha*log(1/w) + beta) + O(w^2 log w):
    # least-squares fit of C, alpha, beta on w = 10^-2 .. 10^-6 (dps 50).
    a = mp.mpf(a); Z = mp.zeta(2, a)
    def Chat(w):
        return (Z - mp.lerchphi(mp.e**(-w), 2, a) - w*mp.log(1/w)) / w
    ws = [mp.mpf(10)**(-k) for k in (2, 3, 4)]   # Phi(e^-w) at dps 50 gets very slow for w <= 1e-5
    rows = []
    for w in ws:
        lw = mp.log(1/w)
        rows.append([mp.mpf(1), w*lw, w])
    M = mp.matrix(rows)
    y = mp.matrix([Chat(w) for w in ws])
    sol = mp.lu_solve(M.T*M, M.T*y)
    C, alpha, beta = sol[0], sol[1], sol[2]
    resid = max(abs((M*sol - y)[i]) for i in range(len(ws)))
    return C, resid

for a in ('0.25', '0.75'):
    c, resid = lerch_singular_C(a)
    print(f"a={a}: C_LERCH = {mp.nstr(c, 14)}   (fit resid {mp.nstr(resid, 3)})")
print("  (control: run-2 exact value for a=1/4 is 0.35090557984795486267)")

def channel(q, parity):
    a = mp.mpf(1)/4 if parity == 'even' else mp.mpf(3)/4
    C1 = mp.digamma(a) + mp.log(mp.mpf(q)/mp.pi)
    Z = mp.zeta(2, a)
    s = -C1 / q                      # s = -C1/(2R), R = q/2
    def A(t):
        t = mp.mpf(t)
        return (t/2)*C1 + mp.mpf(1)/4 * (Z - mp.e**(-2*a*t) * mp.lerchphi(mp.e**(-2*t), 2, a))
    t0 = None; bump = None
    if C1 < 0:  # negative linear tail -> exactly one zero crossing (scan for sign change)
        prev_t, prev_v = mp.mpf('0.01'), A(mp.mpf('0.01'))
        tt = mp.mpf('0.02')
        while tt < 60:
            v = A(tt)
            if prev_v > 0 and v < 0:
                lo, hi = prev_t, tt
                for _ in range(60):
                    mid = (lo+hi)/2
                    if A(mid) > 0: lo = mid
                    else: hi = mid
                t0 = (lo+hi)/2
                break
            prev_t, prev_v = tt, v
            tt *= mp.mpf('1.3')
        if t0:
            lo2, hi2 = mp.mpf('0.0001'), t0     # ternary search for the bump max
            for _ in range(80):
                m1 = lo2 + (hi2-lo2)/3; m2 = hi2 - (hi2-lo2)/3
                if A(m1) < A(m2): lo2 = m1
                else: hi2 = m2
            tb = (lo2+hi2)/2
            bump = (A(tb), tb)
    print(f"q={q:3d} {parity:4s} a={mp.nstr(a,3)}: C1={mp.nstr(C1, 10)}  s={mp.nstr(s, 10)}  "
          f"t0={mp.nstr(t0, 10) if t0 else '--'}  bump={mp.nstr(bump[0], 8) if bump else '--'}"
          f"{' at t='+mp.nstr(bump[1], 6) if bump else ''}  L=q/(q-1)={q/(q-1):.6f}  R={q/2}")
    return C1, s

print()
channel(12, 'even')   # control: expect s = 0.24060639745313878, t0 = 1.9120492808650985
for q in (5, 8, 13, 21, 24):
    channel(q, 'even')
for q in (3, 4, 7, 8):
    channel(q, 'odd')
channel(11, 'odd')    # beyond the odd threshold q < pi*e^{-psi(3/4)} ~ 9.31: C1 > 0 expected
print()
print(f"thresholds: even q < pi*e^{{-psi(1/4)}} = {mp.nstr(mp.pi*mp.e**(-mp.digamma(mp.mpf(1)/4)), 8)}; "
      f"odd q < pi*e^{{-psi(3/4)}} = {mp.nstr(mp.pi*mp.e**(-mp.digamma(mp.mpf(3)/4)), 8)}")
