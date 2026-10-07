#!/usr/bin/env python3
"""
Cusp catastrophe dynamics for Paper D.
Equilibrium surface: V'(t) = t^3 - 3t + q = 0
Stable/unstable branches, fold bifurcations at q = ±2,
with quasistatic hysteresis paths overlaid.
"""
import numpy as np
import matplotlib.pyplot as plt

# Equilibrium: t^3 - 3t + q = 0  =>  q = 3t - t^3
t = np.linspace(-2.2, 2.2, 2000)
q = 3*t - t**3

# Stability: V''(t) = 3t^2 - 3; stable where V'' > 0 (|t| > 1)
stable = np.abs(t) > 1

fig, ax = plt.subplots(figsize=(8, 5))

# Unstable branch (dashed)
ax.plot(q[~stable], t[~stable], 'r--', lw=1.5, label='Unstable', zorder=2)
# Stable branches (solid)
ax.plot(q[stable], t[stable], 'b-', lw=2, label='Stable', zorder=3)

# Fold points at q = ±2, t = ∓1
ax.plot([2, -2], [-1, 1], 'ko', ms=8, zorder=4)
ax.annotate('Fold', xy=(2, -1), xytext=(2.6, -1.5),
            arrowprops=dict(arrowstyle='->', color='k'), fontsize=10)
ax.annotate('Fold', xy=(-2, 1), xytext=(-2.6, 1.5),
            arrowprops=dict(arrowstyle='->', color='k'), fontsize=10)

# Hysteresis: quasistatic sweep up (q: -3 -> 3) then down (q: 3 -> -3)
# Up-sweep: follow lower stable branch until fold at q=2, jump to upper
q_up = np.linspace(-3, 3, 500)
t_up = np.zeros_like(q_up)
for i, qi in enumerate(q_up):
    # roots of t^3 - 3t + qi = 0; pick the one continuing from below
    roots = np.roots([1, 0, -3, qi])
    real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-8])
    if qi < 2:
        # on lower branch (most negative stable root)
        t_up[i] = min([r for r in real_roots if r < -1] or [min(real_roots)])
    else:
        # jumped to upper branch
        t_up[i] = max([r for r in real_roots if r > 1] or [max(real_roots)])

q_dn = np.linspace(3, -3, 500)
t_dn = np.zeros_like(q_dn)
for i, qi in enumerate(q_dn):
    roots = np.roots([1, 0, -3, qi])
    real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-8])
    if qi > -2:
        t_dn[i] = max([r for r in real_roots if r > 1] or [max(real_roots)])
    else:
        t_dn[i] = min([r for r in real_roots if r < -1] or [min(real_roots)])

ax.plot(q_up, t_up, 'g-', lw=1, alpha=0.7, label='Up-sweep')
ax.plot(q_dn, t_dn, 'm-', lw=1, alpha=0.7, label='Down-sweep')

ax.set_xlabel('$q$ (unfolding parameter)', fontsize=12)
ax.set_ylabel('$t$ (state)', fontsize=12)
ax.set_title("Cusp catastrophe: $V'(t) = t^3 - 3t + q = 0$", fontsize=13)
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-2.4, 2.4)

plt.tight_layout()
plt.savefig('fig_cusp_dynamics.pdf')
plt.savefig('fig_cusp_dynamics.png', dpi=150)
print("wrote fig_cusp_dynamics.pdf / .png")
