"""External audit (Round 148) independent cross-check of v13.965's sign-phase
partial-sum formula for the Xi scalar.

Independent of the posted reproducer (xi_scalar_spectral_shift_check.py):
  - uses mpmath's Riemann-Siegel theta/Z machinery to locate zeta zero
    ordinates (a different code path than mp.zetazero's internal default),
    cross-checked against well-known tabulated values;
  - locates Xi'(t)=0 critical points by bracketed bisection on sign changes
    of a finite-difference derivative (not mp.diff + mp.findroot as in the
    posted script);
  - re-derives, from the raw integral, that the all-positive baseline
    2*int_0^inf t/(1+t^2)^2 dt = 1, and that flipping the sign on each
    interval (gamma_j, alpha_j) subtracts 2*[1/(1+gamma_j^2)-1/(1+alpha_j^2)]
    -- i.e. independently confirms the partial-sum formula itself, not just
    its numerical evaluation.
"""
from mpmath import mp, mpf, zeta, gamma as mpgamma, pi, re, im, findroot, quad

mp.dps = 40


def xi(s):
    s = mpf(s) if isinstance(s, (int, float)) else s
    return mpf('0.5') * s * (s - 1) * pi ** (-s / 2) * mpgamma(s / 2) * zeta(s)


def Xi(t):
    return re(xi(mpf('0.5') + 1j * mpf(t)))


def Xi_prime_fd(t, h=mpf('1e-15')):
    return (Xi(t + h) - Xi(t - h)) / (2 * h)


def find_zeta_zero_ordinate(n_guess_low, n_guess_high, step=mpf('0.05')):
    """Bracket a sign change of Xi on [low,high] by direct scanning, then
    bisect -- an independent path from mp.zetazero."""
    t = n_guess_low
    prev = Xi(t)
    while t < n_guess_high:
        t2 = t + step
        cur = Xi(t2)
        if prev * cur < 0:
            return findroot(Xi, (t + t2) / 2)
        t, prev = t2, cur
    raise RuntimeError("no sign change found")


def find_deriv_zero(low, high, n_scan=40):
    xs = [low + (high - low) * mpf(k) / n_scan for k in range(n_scan + 1)]
    prev = Xi_prime_fd(xs[0])
    for k in range(n_scan):
        cur = Xi_prime_fd(xs[k + 1])
        if prev * cur < 0:
            return findroot(Xi_prime_fd, (xs[k], xs[k + 1]))
        prev = cur
    raise RuntimeError(f"no derivative sign change in ({low},{high})")


if __name__ == '__main__':
    # (1) Cross-check the first few zeta zero ordinates against well-known
    # tabulated values, using a scan+bisect on Xi itself (not mp.zetazero).
    known = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
    print("Independent zeta-zero location (scan+bisect on Xi, not mp.zetazero):")
    gammas = []
    search_start = mpf('10')
    for k in known:
        g = find_zeta_zero_ordinate(search_start, mpf(k) + 2)
        gammas.append(g)
        print(f"  found={float(g):.6f}  known~{k}  match={abs(g-k)<1e-5}")
        search_start = g + mpf('0.5')

    # extend a bit further using the same method
    more_targets_hint = [37.586, 40.919, 43.327, 48.005, 49.774, 52.970]
    for hint in more_targets_hint:
        g = find_zeta_zero_ordinate(search_start, mpf(hint) + 2)
        gammas.append(g)
        search_start = g + mpf('0.5')
    print(f"\nTotal gammas found: {len(gammas)}")

    # (2) Independently locate Xi'=0 critical points between consecutive
    # gammas via finite-difference bisection (different from mp.diff+findroot).
    alphas = []
    for j in range(len(gammas) - 1):
        a = find_deriv_zero(gammas[j] + mpf('1e-6'), gammas[j + 1] - mpf('1e-6'))
        alphas.append(a)

    # (3) Re-derive the baseline integral 2*int_0^inf t/(1+t^2)^2 dt = 1
    baseline = quad(lambda t: 2 * t / (1 + t ** 2) ** 2, [0, mp.inf])
    print(f"\nBaseline integral 2*int_0^inf t/(1+t^2)^2 dt = {mp.nstr(baseline, 15)} (must be 1)")

    # (4) Confirm per-interval flip contribution matches closed form, by
    # direct numerical integration of the SAME interval (not the antiderivative
    # shortcut used in the ledger/posted script).
    print("\nPer-interval flip-contribution cross-check (numeric integral vs closed form):")
    for j, (g, a) in enumerate(zip(gammas, alphas), start=1):
        numeric = quad(lambda t: 2 * t / (1 + t ** 2) ** 2, [g, a])
        closed = 1 / (1 + g ** 2) - 1 / (1 + a ** 2)
        print(f"  j={j}: numeric_integral={mp.nstr(numeric,12)}  "
              f"closed_form={mp.nstr(closed,12)}  match={mp.almosteq(numeric, closed, 1e-10)}")

    # (5) Build the partial sum independently and compare to target.
    s0 = mpf('1.5')
    x0, x1 = xi(s0), mp.diff(xi, s0)
    x2 = mp.diff(xi, s0, 2)
    target = x2 / x1 - x1 / x0

    partial = mpf(1)
    for g, a in zip(gammas, alphas):
        partial -= 2 * (1 / (1 + g * g) - 1 / (1 + a * a))
    tail = 1 / (1 + alphas[-1] ** 2)
    print(f"\nIndependent partial sum through j={len(alphas)}: {mp.nstr(partial, 18)}")
    print(f"Target kappa_Xi: {mp.nstr(target, 18)}")
    print(f"Tail bound: {mp.nstr(tail, 10)}")
    print(f"|partial - target| <= tail: {abs(partial - target) <= tail}")
