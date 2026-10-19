#!/usr/bin/env python3
"""Dictionary-candidate closure probe (sandbox, 2026-10-18, LIttle Euler).

Tests the v14.592 dictionary candidate (cone coordinate as action /
segment area) against the staged 2026-09-28 dictionary obligation
(embedding.md sec.18; archimedean_report_2.md sec.2): dictionary
x(t): [0,inf) -> [0,L], L = 12/11, x(0)=L, x(inf)=0, envelope
A~(t) = 6 sqrt(1 - e^{-2t}); staged dual signature (6pi/w) J1(12w/11).

  Test 1a: FT of the semicircle envelope A~(x) = 6 sqrt(1-(x/L)^2)
           equals (6pi/w) J1(L w) exactly (mpmath, dps=30).
           The semicircle in x exists iff x = L e^{-t} (D_exp), since
           A~(t) = 6 sqrt(1 - e^{-2t}) and e^{-2t} = (x/L)^2 iff D_exp.
  Test 1b: under D_tanh the x-profile is not the semicircle and its
           FT misses the J1 form by 14-26%.
  Test 2:  the deficit-area dictionary x_S(t) = L(1 - S(t)/S(inf)),
           S(t) = int_0^t (6 - A~(s)) ds, is well-defined
           (S(inf) = 1.84111691664) with correct endpoints, but is not
           D_exp: x_S/x_Dexp runs 0.70 -> 0.0055 on t in [0.25, 5],
           log-rate log(L/x_S)/t -> 2 (e^{-2t} tail, not e^{-t}).
  Test 3:  (from archimedean_report_2, 30-digit verified there) the
           channel asymptotics are t*log t (A12 small-t), sqrt(t)
           (envelope small-t), linear (large-t); J1 zeros arithmetic
           pi(s+1/4) (airy_powers_probe.py). No 2/3 foothold.

Verdict recorded in conversation 2026-10-18: candidate dissolved;
J1 signature <=> D_exp is one claim, not two.
"""
import mpmath as mp
mp.mp.dps = 30
L = mp.mpf(12) / 11
f = float

print("== Test 1a ==")
env = lambda x: 6 * mp.sqrt(1 - (x / L) ** 2)
for w in [mp.mpf('0.7'), mp.mpf('2.3'), mp.mpf('5.0'), mp.mpf('9.4')]:
    ft = mp.quad(lambda x: env(x) * mp.cos(w * x), [-L, L])
    pred = 6 * mp.pi / w * mp.besselj(1, L * w)
    print(f"  w={f(w)}: rel.diff={f(abs(ft - pred) / abs(pred)):.2e}")

print("== Test 1b ==")
def env_tanh(x):
    t = mp.atanh(1 - x / L)
    return 6 * mp.sqrt(1 - mp.e ** (-2 * t))
for w in [mp.mpf('2.3'), mp.mpf('5.0')]:
    ft = mp.quad(lambda x: env_tanh(x) * mp.cos(w * x), [-L, L])
    pred = 6 * mp.pi / w * mp.besselj(1, L * w)
    print(f"  w={f(w)}: rel.diff={f(abs(ft - pred) / abs(pred)) * 100:.1f}%")

print("== Test 2 ==")
env_t = lambda s: 6 * mp.sqrt(1 - mp.e ** (-2 * s))
Sinf = mp.quad(lambda s: 6 - env_t(s), [0, mp.inf])
print(f"  S(inf) = {mp.nstr(Sinf, 12)}")
S = lambda t: mp.quad(lambda s: 6 - env_t(s), [0, t])
for t in [mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('3'), mp.mpf('5')]:
    xS, xD = L * (1 - S(t) / Sinf), L * mp.e ** (-t)
    print(f"  t={f(t)}: ratio={mp.nstr(xS / xD, 6)}  log(L/x_S)/t={mp.nstr(mp.log(L / xS) / t, 6)}")
print("DONE")
