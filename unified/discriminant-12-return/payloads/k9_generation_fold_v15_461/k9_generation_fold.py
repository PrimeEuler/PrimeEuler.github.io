"""
The k=9 generation fold (2026-11-06, sandbox). Door anatomy II
(v15.429) measured the generation door as one unbounded positive
integer: the replica tower c -> c + 3g, every output a function
of c mod 3 only. Proposal under test (Jeremy's question,
2026-11-06): the AM-GM family at higher k refines the grading.
A k-list's split phase has order k and grades a distinguished
mode's occupation c by c mod k; at k=9 the reduction Z9 -> Z3
has fibers of size 3, so IF the frame's third mode carries the
k=9 reading, the tower folds to exactly three classes per tau,
distinguished by a digit no gauge output reads.

Checks (exact arithmetic throughout):
 1. split grading at general k (phase order, AM coefficient 1/k
    from list length -- the k=3 argument of amgm_k3_triality,
    rerun at k = 2,3,4,6,9,12,18);
 2. the fold: frame tower classes at k=9 -- distinct for
    g = 0,1,2, repeating with period 3 in g; gauge outputs
    (tau, Y mod 2) identical across the folded classes;
 3. selectivity: fiber size over Z3 is k/3 -- 1,2,3,4,5,6 for
    k = 3,6,9,12,15,18; exactly 3 only at k = 9; k not divisible
    by 3 refines nothing;
 4. digit structure: c mod 9 <-> (tau, g mod 3) bijection;
    antimatter c -> -c negates both digits consistently;
 5. charge non-leakage: the Z6 congruence and the closed Y table
    see only the mod-3 shadow, for every replica.
NOT checked here (named as the hypothesis): the identification
of the frame's third mode with a k=9 distinguished mode, and
any sector (masses) that reads the fine digit. The family's
existence at k=9 is ledgered (v14.818: Hessian, signature
(1,8), seat -9 log 2, d_9 <-> zeta^9); no spacetime reading.
"""
from fractions import Fraction as F

print("=" * 76)
print("1. split grading at general k: phase order and AM coefficient")
print("=" * 76)
for k in (2, 3, 4, 6, 9, 12, 18):
    # split phase zeta_k = exp(2 pi i / k): order = k (exponent arithmetic)
    order = next(m for m in range(1, 4 * k + 1) if (F(m, k) % 1) == 0)
    refines = (k % 3 == 0)
    print(f"  k = {k:2d}: phase order {order}, AM coefficient 1/{k}, "
          f"grading c mod {k}" + (f", fiber over Z3 of size {k // 3}" if refines
                                  else ", does not refine Z3"))

print()
print("=" * 76)
print("2. the fold at k=9: frame tower classes (c = tau + 3g)")
print("=" * 76)
# frame entries: (name, tau, n2, Y closed value)
FRAME = [("L_L", 0, 1, F(-1)), ("Q_L", 1, 1, F(1, 3)), ("H", 0, 1, F(1)),
         ("e_R", 0, 0, F(-2)), ("u_R", 1, 0, F(4, 3)), ("d_R", 1, 0, F(-2, 3)),
         ("nu_R", 0, 0, F(0)), ("W", 0, 0, F(0))]
ok = True
for name, tau, n2, Y in FRAME:
    classes = [(tau + 3 * g) % 9 for g in range(6)]
    distinct3 = len(set(classes[:3])) == 3
    period3 = all(classes[g + 3] == classes[g] for g in range(3))
    ok &= distinct3 and period3
    print(f"  {name:5s} tau={tau}: classes g=0..5 -> {classes}  "
          f"distinct(g<3)={distinct3}, period-3 in g: {period3}")
print(f"  tower folds to exactly 3 classes per tau; a 4th replica")
print(f"  duplicates a class instead of extending the tower: {ok}")

print()
print("=" * 76)
print("3. selectivity: fiber size k/3 -- exactly 3 only at k=9")
print("=" * 76)
fib = {k: k // 3 for k in (3, 6, 9, 12, 15, 18)}
print(f"  fibers: {fib};  fiber == 3  <=>  k == 9: "
      f"{[k for k, v in fib.items() if v == 3] == [9]}")

print()
print("=" * 76)
print("4. digits and antimatter: c mod 9 <-> (tau, g mod 3)")
print("=" * 76)
bij = all(((c % 3) + 3 * (((c - (c % 3)) // 3) % 3)) == c for c in range(9))
print(f"  base-3 digit bijection on Z9: {bij}")
anti_ok = True
for c in range(9):
    cp = (-c) % 9
    tau, g = c % 3, ((c - (c % 3)) // 3) % 3
    taup, gp = cp % 3, ((cp - (cp % 3)) // 3) % 3
    # exact digit law: g' = (-g - [tau>0]) mod 3; and an involution
    anti_ok &= (taup == (-tau) % 3) and (gp == (-g - (1 if tau > 0 else 0)) % 3)
    cpp = (-cp) % 9
    anti_ok &= (cpp == c)
print(f"  conjugation on digits: tau -> -tau (mod 3), as filed at v15.388;")
print(f"  g -> -g - [tau>0] (mod 3) exactly on all 9 classes, and the map")
print(f"  is an involution -- antimatter stays inside the folded tower,")
print(f"  classes paired rather than digit-fixed: {anti_ok}")
print(f"  e.g. Q_L g=1 at c=4 (tau 1, digit 1) pairs with c=5 (tau 2,")
print(f"  digit 1); a tau=0 class at digit 1 pairs with digit 2.")

print()
print("=" * 76)
print("5. charge non-leakage: the Z6 congruence reads only the shadow")
print("=" * 76)
leak_ok = True
for name, tau, n2, Y in FRAME:
    for g in range(3):
        cls = (tau + 3 * g) % 9
        shadow = cls % 3
        leak_ok &= (shadow == tau) and ((Y / 2 + F(shadow, 3) + F(n2, 2)) % 1 == 0)
print(f"  congruence holds with tau = (c mod 9) mod 3 for all fields")
print(f"  and g = 0,1,2; closed Y values unchanged: {leak_ok}")
print(f"  the fine digit is gauge-invisible by the frame's own formulas.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("The refinement is real family arithmetic: at k=9 the split")
print("grading refines Z3 by a base-3 digit, the replica tower")
print("folds to exactly three classes per tau, no gauge output")
print("reads the digit, antimatter acts as an exact involution on")
print("the 9 classes (tau negated, digit paired), and among k <= 18")
print("only k=9 gives fiber 3.")
print("IF the frame's third mode is the k=9 list's distinguished")
print("mode (the identification -- a hypothesis, not derived here)")
print("and IF a sector exists that reads the fine digit (the mass")
print("sector is the phenomenological candidate: generations in")
print("nature differ ONLY there), then door II's integer is")
print("answered by a fiber cardinality: 3 = 9/3, the first count")
print("in this thread produced rather than assumed. Falsifiable")
print("shape retained: a fourth generation would have to duplicate")
print("an existing class in every digit-reading sector.")
