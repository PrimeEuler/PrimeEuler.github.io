"""A-sweep for the r-gate. Saves r_ratios_sweep.npz. Sandbox only."""
import numpy as np
import r_gate as rg

def run(A, N, q=8):
    o = rg.solve_moments(A, N, lam=-1.0, q=q, want_cond=(N <= 1600))
    return o

if __name__ == '__main__':
    import sys, json
    Agrid = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    results = []
    for A in Agrid:
        for N in [800, 1600]:
            print(f"A={A} N={N}", flush=True)
            o = run(A, N)
            rec = {k: (float(o[k]) if np.ndim(o[k]) == 0 else None)
                   for k in ['A', 'N', 'h', 'cond', 'res', 'par_one', 'par_x',
                             'cross_kx0_c1', 'cross_k0_cx',
                             'M00', 'M1x', 'M0e', 'M1e', 'd0', 'd1', 'r0', 'r1']}
            rec['q'] = 8
            results.append(rec)
            print(f"   r0={rec['r0']:.5f} r1={rec['r1']:.5f} d0={rec['d0']:.4f} "
                  f"d1={rec['d1']:.4f} cond={rec['cond']:.2f}", flush=True)
    # 4x refinement checks
    for A, N in [(1.0, 3200), (2.0, 3200)]:
        print(f"4x check: A={A} N={N}", flush=True)
        o = run(A, N, q=8)
        rec = {k: float(o[k]) for k in ['A', 'N', 'h', 'res',
                 'M00', 'M1x', 'M0e', 'M1e', 'd0', 'd1', 'r0', 'r1']}
        rec['q'] = 8
        results.append(rec)
        print(f"   r0={rec['r0']:.5f} r1={rec['r1']:.5f}", flush=True)
    # quadrature doubling at A=2, N=1600
    print("q-doubling: A=2.0 N=1600 q=16", flush=True)
    o = run(2.0, 1600, q=16)
    rec = {k: float(o[k]) for k in ['A', 'N', 'h', 'res',
             'M00', 'M1x', 'M0e', 'M1e', 'd0', 'd1', 'r0', 'r1']}
    rec['q'] = 16
    results.append(rec)
    print(f"   r0={rec['r0']:.5f} r1={rec['r1']:.5f}", flush=True)
    np.savez('r_ratios_sweep.npz', **{f'r{i}': np.array(
        [list(r.values()) for r in results]) for i, r in enumerate([0])},
        keys=np.array(list(results[0].keys())), nrec=len(results))
    # simpler: save as json-able
    import json
    with open('r_ratios_sweep.json', 'w') as f:
        json.dump(results, f)
    print("saved", len(results), "records")
