"""Numeric spot-check of the symbolic charge identities at random phase-space points."""
import random, math
import numpy as np

random.seed(20261022)
ok = True
for trial in range(200):
    l = random.uniform(0.3, 2.0)
    mm = random.uniform(-0.5, 1.5)   # background mass parameter (only enters f)
    r_plus = mm + math.sqrt(mm * mm + l * l)
    r = r_plus + random.uniform(1.0, 6.0)
    th = random.uniform(0.25, math.pi - 0.25)
    ph = random.uniform(0, 2 * math.pi)
    f = (r * r - 2 * mm * r - l * l) / (r * r + l * l)
    Sig = r * r + l * l
    g = np.zeros((4, 4))
    g[0, 0] = -f
    g[0, 3] = g[3, 0] = -2 * l * f * math.cos(th)
    g[3, 3] = -4 * l * l * f * math.cos(th) ** 2 + Sig * math.sin(th) ** 2
    g[1, 1] = 1 / f
    g[2, 2] = Sig
    # random timelike 4-velocity, normalized numerically
    u = np.array([random.uniform(1.2, 2.0), random.uniform(-0.05, 0.05),
                  random.uniform(-0.05, 0.05), random.uniform(-0.05, 0.05)])
    n2 = u @ g @ u
    u = u / math.sqrt(-n2)
    p = g @ u
    p_t, p_th, p_ph = p[0], p[2], p[3]
    eps = -p_t
    s, c = math.sin(th), math.cos(th)
    Qx = (2 * l * math.cos(ph) / s) * p_t - math.sin(ph) * p_th - math.cos(ph) * c / s * p_ph
    Qy = (2 * l * math.sin(ph) / s) * p_t + math.cos(ph) * p_th - math.sin(ph) * c / s * p_ph
    Qz = p_ph
    nvec = np.array([s * math.cos(ph), s * math.sin(ph), c])
    radial = nvec @ np.array([Qx, Qy, Qz])
    J2 = Qx * Qx + Qy * Qy + Qz * Qz
    J2_form = (Sig * u[2]) ** 2 + (p_ph + 2 * l * eps * c) ** 2 / s ** 2 + (2 * l * eps) ** 2
    if abs(radial - (-2 * l * eps)) > 1e-9 * max(1.0, abs(2 * l * eps)):
        ok = False; print("radial FAIL", trial, radial, -2 * l * eps)
    if abs(J2 - J2_form) > 1e-8 * max(1.0, J2):
        ok = False; print("J2 FAIL", trial, J2, J2_form)
print("numeric check (200 random points, incl. p_t-mixing):", "PASS" if ok else "FAIL")
