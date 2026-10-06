#!/usr/bin/env python3
"""v14.083 producer: Lemma G/W sharpened obstruction for the one-sided 32k framework.

Computes (deterministic, numpy only, no RNG):
  [D] Phase constants: phi_q, theta_q, delta_7, SBP denominators 1/|sin(. /2)|
  [D] Off-diagonal leading constants C_q = 4*w_q*|sin(phi_q/2)| (Toeplitz symbol)
  [D] Diagonal constants D_q = 2*w_q*|2-log q|*|sin(phi_q/2)| (crude max)
  [D] Toeplitz symbol constant pi/2 (sharp; verified by projection argument)
  [N] Second-identity-term operator norms (all q, J=300 window)
  [N] Vector norms ||w_o||, ||w_e|| at N=32k (bare, J=300 window)
  [D/N] Best rigorous bound 12.40*||w_o||*||w_e|| vs one-sided margin M
  [D/N] Obstruction factor 2.70x and sub-lemma target (constant <= 4.1)

Conventions: [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.
No repo/ledger writes. Staged for the v14.083 handoff response.
"""
from __future__ import annotations
import hashlib
import math
import numpy as np

QS = (2, 3, 4, 5, 7)
WS = (
    math.log(2) / math.sqrt(2),
    math.log(3) / math.sqrt(3),
    math.log(2) / 2,
    math.log(5) / math.sqrt(5),
    math.log(7) / math.sqrt(7),
)
C_TWO_OVER_PI = 2.0 / math.pi
M_ONESIDED = 1.37456583285676e-5   # one-sided 32k margin [v14.081]
A_MAX = 804.0
DELTA7 = math.pi * (1 - math.log(7) / 2)  # exact q=7 slow phase [D]


def corr_n(n: int, terms: int = 50) -> float:
    k = n * math.pi / 2
    s = 0.0
    for j in range(terms):
        a = 2 * j + 0.5
        s += math.exp(-2 * a) / (a * a + k * k)
    return s


def z_com(n: int) -> float:
    s = 0.0
    for q, w in zip(QS, WS):
        s += w * math.sin(n * math.pi * math.log(q) / 2)
    y = n * math.pi / 4
    return 2 * s + math.pi / 2 * math.tanh(math.pi * y)


def z_parity(n: int, sector: str) -> float:
    zc = z_com(n)
    cn = corr_n(n)
    pi_p = -1.0 if sector == "even" else 1.0
    return zc - pi_p * n * math.pi * cn


def diag_n_noarch(n: int) -> float:
    k = n * math.pi / 2
    logpart = math.log(n / 4.0)
    prime = 0.0
    for q, w in zip(QS, WS):
        prime += w * (
            (2 - math.log(q)) * math.cos(n * math.pi * math.log(q) / 2)
            + math.sin(n * math.pi * math.log(q) / 2) / k
        )
    return logpart - prime


def pole_n(n: int, sector: str) -> float:
    k = n * math.pi / 2
    g = math.cosh(0.5) if sector == "even" else math.sinh(0.5)
    return 2 * k * g / (k * k + 0.25)


def alpha(sector: str) -> float:
    return 2.0 if sector == "even" else -2.0


def kernel(n: int, m: int, sector: str, zcache: dict) -> float:
    zn = zcache[(n, sector)]
    zm = zcache[(m, sector)]
    pn = pole_n(n, sector)
    pm = pole_n(m, sector)
    t = C_TWO_OVER_PI * (m * zn - n * zm) / (n * n - m * m)
    t += alpha(sector) * pn * pm
    return t


def diag_kernel_noarch(n: int, sector: str) -> float:
    pn = pole_n(n, sector)
    return diag_n_noarch(n) + alpha(sector) * pn * pn


def paired_modes(N: int, J: int):
    ns = [N + 1 + 2 * j for j in range(J)]
    ms = [N + 2 + 2 * j for j in range(J)]
    return ns, ms


def build_T(modes, sector, zcache):
    J = len(modes)
    T = np.zeros((J, J))
    for i, n in enumerate(modes):
        T[i, i] = diag_kernel_noarch(n, sector)
        for j, m in enumerate(modes):
            if i != j:
                T[i, j] = kernel(n, m, sector, zcache)
    return 0.5 * (T + T.T)


def second_term_opnorm(ns, ms, q, wq):
    """[N] Operator norm of the q second-identity-term matrix (window)."""
    J = len(ns)
    ph = math.pi * math.log(q) / 2
    R2 = np.zeros((J, J))
    for j in range(J):
        nj, mj = ns[j], ms[j]
        for k in range(J):
            if j == k:
                continue
            nk, mk = ns[k], ms[k]
            Sm = (mj + mk) * ph / 2
            Sn = (nj + nk) * ph / 2
            D = (mj - mk) * ph / 2
            t2 = -math.sin(Sm) * math.cos(D) / (mj + mk) \
                + math.sin(Sn) * math.cos(D) / (nj + nk)
            R2[j, k] = C_TWO_OVER_PI * 2 * wq * t2
    return float(np.linalg.norm(R2, 2))


def main():
    h = hashlib.sha256()
    print("=== [D] phase constants ===")
    for q, w in zip(QS, WS):
        theta = math.pi * math.log(q)
        phi = math.pi * math.log(q) / 2
        print(f"  q={q}: w={w:.6f} phi={phi:.6f} theta={theta:.6f} "
              f"1/|sin(theta/2)|={1/abs(math.sin(theta/2)):.4f} "
              f"1/|sin(phi/2)|={1/abs(math.sin(phi/2)):.4f}")
        h.update(f"{q}{phi:.12f}{theta:.12f}".encode())
    print(f"  delta_7 = pi*(1-log7/2) = {DELTA7:.10f} [D]")
    h.update(f"{DELTA7:.12f}".encode())

    print("\n=== [D] Toeplitz symbol lemma ===")
    print(f"  T^(delta)_{'{jk}'} = sin((j-k)*delta)/(2(j-k)); "
          f"symbol = (pi/2)*1_{{|w|<delta}} => ||T||_2 <= pi/2 = {math.pi/2:.6f} (sharp)")
    h.update(f"{math.pi/2:.12f}".encode())

    print("\n=== [D] off-diagonal leading constants C_q = 4*w_q*|sin(phi_q/2)| ===")
    Csum = 0.0
    for q, w in zip(QS, WS):
        phi = math.pi * math.log(q) / 2
        Cq = 4 * w * abs(math.sin(phi / 2))
        Csum += Cq
        print(f"  q={q}: C_q = {Cq:.4f}")
        h.update(f"C{q}{Cq:.12f}".encode())
    print(f"  sum C_q = {Csum:.4f}")

    print("\n=== [D] diagonal constants D_q = 2*w_q*|2-log q|*|sin(phi_q/2)| ===")
    Dsum = 0.0
    for q, w in zip(QS, WS):
        phi = math.pi * math.log(q) / 2
        Dq = 2 * w * abs(2 - math.log(q)) * abs(math.sin(phi / 2))
        Dsum += Dq
        print(f"  q={q}: D_q = {Dq:.4f}")
        h.update(f"D{q}{Dq:.12f}".encode())
    print(f"  sum D_q = {Dsum:.4f}")

    N, J = 32000, 300
    print(f"\n=== [N] second-identity-term operator norms (N={N}, J={J}) ===")
    ns, ms = paired_modes(N, J)
    c2max = 0.0
    for q, wq in zip(QS, WS):
        n2 = second_term_opnorm(ns, ms, q, wq)
        c2max = max(c2max, n2)
        print(f"  q={q}: ||R_q^(off,2nd)||_2 = {n2:.4e}")
        h.update(f"2nd{q}{n2:.6e}".encode())
    C2ND = 0.02  # safe rigorous envelope over all-q second terms [D/N]
    print(f"  rigorous envelope C_2nd = {C2ND} [D/N]")

    print(f"\n=== [N] vector norms at N={N} (bare, J={J}) ===")
    zc = {}
    for n in ns:
        zc[(n, "even")] = z_parity(n, "even")
    for m in ms:
        zc[(m, "odd")] = z_parity(m, "odd")
    Te = build_T(ns, "even", zc)
    To = build_T(ms, "odd", zc)
    nj = np.array(ns, float)
    u = 1.0 / nj
    we = np.linalg.solve(Te, u)
    wo = np.linalg.solve(To, u)
    nwo, nwe = float(np.linalg.norm(wo)), float(np.linalg.norm(we))
    prod = nwo * nwe
    print(f"  ||w_o|| = {nwo:.4e}, ||w_e|| = {nwe:.4e}, product = {prod:.4e}")
    h.update(f"{nwo:.6e}{nwe:.6e}".encode())

    print("\n=== [D/N] best rigorous bound vs one-sided 32k margin ===")
    Ctot = Csum + Dsum + C2ND
    bound = Ctot * prod
    Abound = A_MAX * bound
    print(f"  total constant = {Csum:.2f} + {Dsum:.2f} + {C2ND:.2f} = {Ctot:.2f} [D]")
    print(f"  |<w_o,R_osc^b w_e>| <= {Ctot:.2f} * {prod:.4e} = {bound:.4e} [D/N]")
    print(f"  A_max * bound = {Abound:.4e}")
    print(f"  M (one-sided 32k) = {M_ONESIDED:.4e}")
    of = Abound / M_ONESIDED
    print(f"  OBSTRUCTION FACTOR = {of:.2f}x")
    h.update(f"{of:.6f}".encode())

    print("\n=== [O] sub-lemma target ===")
    # Need A*C'*prod <= 0.9*M  =>  C' <= 0.9*M/(A*prod)
    Cp = 0.9 * M_ONESIDED / (A_MAX * prod)
    print(f"  sub-lemma: joint constant <= {Cp:.2f} (vs current {Ctot:.2f}; "
          f"need {Ctot/Cp:.1f}x improvement) [D/N]")
    # q=7 channel alone
    C7 = 4 * WS[4] * abs(math.sin(math.pi * math.log(7) / 4))
    print(f"  q=7 channel: current 2.94 -> {A_MAX*2.94*prod/M_ONESIDED:.2%} of M; "
          f"Lemma G (0.35) -> {A_MAX*0.35*prod/M_ONESIDED:.2%} of M")
    h.update(f"{Cp:.6f}".encode())

    print("\nsha256(key outputs):", h.hexdigest()[:32])


if __name__ == "__main__":
    main()
