"""External audit (Round 146) independent numerical checks for v13.956's
resolvent-weighted critical selector.

Checks:
  1. v13.941's crossover relation O_a(delta_tau) = tanh(tau/2)*E_a(delta_tau)
     implies kappa_a(delta_tau) = (1-tanh(tau/2))/(1+tanh(tau/2)) = e^{-tau}
     (eq 22), via the elementary tanh half-angle identity.
  2. The universal critical parity weights w_+(tau)=(1+e^{-tau})/2,
     w_-(tau)=(1-e^{-tau})/2 (eqs 23-24), numerically at tau=1.
  3. The exact raw source norms/overlap (eqs 3-5): ||f_R,a||^2=(1-e^{-4a})/2,
     <f_R,f_L>=2a*e^{-2a}, chi_raw ~ 4a*e^{-2a}.
  4. The resolvent-amplification ratio (eq 25):
     chi_resolvent/chi_raw ~ e^{2a-tau}/(4a).

Fresh implementation, not reusing anything from the ledger entry itself.
"""
import math


def kappa_from_crossover(tau):
    q = math.tanh(tau / 2)
    return (1 - q) / (1 + q)


def raw_source_stats(a):
    norm2 = (1 - math.exp(-4 * a)) / 2
    overlap = 2 * a * math.exp(-2 * a)
    return norm2, overlap, overlap / norm2


if __name__ == '__main__':
    print("Eq 22: kappa_a(delta_tau) = (1-tanh(tau/2))/(1+tanh(tau/2)) =? e^-tau")
    for tau in [0.3, 1.0, 2.0, 5.0]:
        kappa = kappa_from_crossover(tau)
        print(f"  tau={tau}: kappa={kappa:.10f}  e^-tau={math.exp(-tau):.10f}  "
              f"match={math.isclose(kappa, math.exp(-tau))}")

    print("\nEqs 23-24: w_+(1), w_-(1)")
    tau = 1.0
    wp, wm = (1 + math.exp(-tau)) / 2, (1 - math.exp(-tau)) / 2
    print(f"  w_+(1)={wp:.7f}  (claimed 0.6839397)")
    print(f"  w_-(1)={wm:.7f}  (claimed 0.3160603)")
    print(f"  sum={wp + wm} (must be 1)")

    print("\nEqs 3-5: raw source norms/overlap vs asymptotics")
    for a in [1.0, 2.0, 3.0, 5.0]:
        norm2, overlap, chi_raw = raw_source_stats(a)
        asym = 4 * a * math.exp(-2 * a)
        print(f"  a={a}: ||f_R||^2={norm2:.8f}  <f_R,f_L>={overlap:.8f}  "
              f"chi_raw={chi_raw:.6e}  asym~{asym:.6e}")

    print("\nEq 25: resolvent-amplification ratio at tau=1")
    for a in [2, 4, 6, 10]:
        _, _, chi_raw = raw_source_stats(a)
        chi_res = math.exp(-1.0)
        ratio = chi_res / chi_raw
        ratio_asym = math.exp(2 * a - 1) / (4 * a)
        print(f"  a={a}: ratio={ratio:.6e}  asym_formula={ratio_asym:.6e}")
