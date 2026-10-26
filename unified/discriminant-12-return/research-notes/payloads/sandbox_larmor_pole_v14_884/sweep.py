#!/usr/bin/env python3
"""Pole continuation sweep for the finite-Larmor seat kernel (kernel5).

For each beta in {0.5, 1, 2}: continue the v14.874 pole
z0 = 0.4108337143730426 - 0.1700926343728676i from alpha=0 upward in steps,
secant-polished at each declared alpha in {0.05,0.1,0.2,0.35,0.5} (alpha*beta<=0.7).
Also: UHP scan for extra zeros near the path, and Dhat values on a real-axis
grid for the time-domain cross-check. Results -> sweep.json.
Kernels cached to kernel_cache_{beta}.npz.
"""
import numpy as np, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kernel5 import Kernel5, _Hnum

Z0 = 0.4108337143730426 - 0.1700926343728676j

def load_kernel(beta):
    fn = f"kernel_cache_{beta}.npz"
    if os.path.exists(fn):
        d = np.load(fn)
        K = Kernel5.__new__(Kernel5)
        K.beta = beta; K.N = int(d["N"]); K.p = d["p"]; K.wp = d["wp"]
        K.xm = d["xm"]; K.wm = d["wm"]; K.phi = d["phi"]; K.wphi = float(d["wphi"])
        K.H0, K.H1, K.H2 = d["H0"], d["H1"], d["H2"]
        K.ns = d["ns"]; K.W = d["W"]
        return K
    K = Kernel5(beta)
    np.savez(fn, N=K.N, p=K.p, wp=K.wp, xm=K.xm, wm=K.wm, phi=K.phi,
             wphi=K.wphi, H0=K.H0, H1=K.H1, H2=K.H2, ns=K.ns, W=K.W)
    return K

def secant(K, alpha, za, zb, tol=1e-12, maxit=60):
    fa, fb = K.Dhat(za, alpha), K.Dhat(zb, alpha)
    for _ in range(maxit):
        if abs(fb) < tol:
            return zb, fb
        if fb == fa:
            break
        zc = zb - fb*(zb-za)/(fb-fa)
        za, fa, zb, fb = zb, fb, zc, K.Dhat(zc, alpha)
    return zb, fb

def main():
    out = {}
    alphas_declared = [0.05, 0.1, 0.2, 0.35, 0.5]
    for beta in (0.5, 1.0, 2.0):
        K = load_kernel(beta)
        print(f"beta={beta} kernel ready N={K.N}", flush=True)
        zprev, zprev2 = Z0, Z0*(1+1e-6)
        results = {}
        amax = 0.7/beta
        targets = [a for a in alphas_declared if a <= amax + 1e-12]
        a = 0.0
        for at in targets:
            while a < at - 1e-12:
                an = min(a + 0.025, at)
                znew, res = secant(K, an, zprev2, zprev)
                zprev2, zprev, a = zprev, znew, an
            results[str(at)] = {"z": [zprev.real, zprev.imag], "residual": abs(K.Dhat(zprev, at))}
            print(f"  beta={beta} alpha={at}: z={zprev:.12f} res={results[str(at)]['residual']:.2e}", flush=True)
        # UHP scan at largest alpha: grid search for |Dhat| minima with Im z>0
        at = targets[-1]
        best = []
        for re in np.linspace(-1.2, 1.2, 25):
            for im in np.linspace(0.02, 1.0, 20):
                v = abs(K.Dhat(re+1j*im, at))
                best.append((v, re, im))
        best.sort()
        results["uhp_scan_min"] = [{"abs": v, "re": re, "im": im} for v, re, im in best[:3]]
        # near-axis values (Im z = 0.02, resolvable) for time-domain cross-check
        results["real_axis"] = {str(w): [K.Dhat(w+0.02j, at).real, K.Dhat(w+0.02j, at).imag]
                                for w in (0.25, 0.35, 0.45, 0.55)}
        results["alpha_max"] = at
        out[str(beta)] = results
    with open("sweep.json", "w") as f:
        json.dump(out, f, indent=1)
    print("SWEEP_DONE")

if __name__ == "__main__":
    main()
