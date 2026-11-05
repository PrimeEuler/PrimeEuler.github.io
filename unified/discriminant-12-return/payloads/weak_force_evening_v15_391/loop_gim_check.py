"""
Loop anatomy check (2026-11-04, sandbox): the B_d -> mu+mu- loop,
taken apart. Amplitude ~ sum over the internal up-type quarks
i in {u, c, t} of lambda_i * Y(x_i), lambda_i = V_id V_ib*, with the
Inami-Lim function Y(x), x_i = (m_i / M_W)^2. The three internal
lines run over the frame's GENERATION direction (the c -> c+3
replicas): this is the first place in the thread where that
direction is SUMMED, not just labeled.

What is structural (cone-native species): the cancellation. CKM
unitarity sum_i lambda_i = 0 is a completeness identity over the
generation direction, and it forces the amplitude into
mass-DIFFERENCE form; degenerate internal masses give exactly zero
(GIM). What is imported: the weights -- masses (top dominance) and
the lambda_i themselves (CKM: the generation door), and the overall
coupling prefactors (dynamics door).
"""
import sympy as sp

# 1. exact reduction under sum lambda = 0
lu, lc, lt, Yu, Yc, Yt = sp.symbols('lambda_u lambda_c lambda_t Y_u Y_c Y_t')
A = lu * Yu + lc * Yc + lt * Yt
A_red = sp.expand(A.subs(lu, -lc - lt))
print(f"A with unitarity substituted: {A_red}")
print("  = lambda_c (Y_c - Y_u) + lambda_t (Y_t - Y_u): mass differences only.")
print(f"  degenerate masses Y_u=Y_c=Y_t -> A = {sp.expand(A_red.subs({Yc: Yu, Yt: Yu}))}  (GIM: exact zero)")

# 2. numerics: Inami-Lim Y and the actual weights
import mpmath as mp
def Y(x):
    if x == 0: return mp.mpf('0')
    return x / 8 * ((x - 4) / (x - 1) + 3 * x * mp.log(x) / (x - 1) ** 2)
MW = mp.mpf('80.4')
xs = {'u': (mp.mpf('0.0022') / MW) ** 2, 'c': (mp.mpf('1.27') / MW) ** 2,
      't': (mp.mpf('172.7') / MW) ** 2}
lam = {'u': mp.mpf('-0.0004'), 'c': mp.mpf('0.0090'), 't': mp.mpf('-0.0086')}  # ~V_id V_ib*, sums ~0
print(f"  sum lambda_i = {float(sum(lam.values())):.2e} (unitarity, ~0)")
tot = mp.mpf('0')
for k in 'uct':
    term = lam[k] * Y(xs[k]); tot += term
    print(f"  {k}: x={float(xs[k]):.3e}, Y(x)={float(Y(xs[k])):.4f}, "
          f"lambda*Y = {float(term):+.3e}")
print(f"  amplitude ~ {float(tot):+.3e}: the top term is "
      f"{abs(float(lam['t'] * Y(xs['t']) / tot)) * 100:.0f}% of it --")
print("  dominance is a MASS fact (imported); the cancellation that")
print("  leaves only mass differences is the completeness sum over")
print("  the generation direction (structural).")
