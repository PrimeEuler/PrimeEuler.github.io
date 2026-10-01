"""External audit (Round 139): ngrid-sensitivity probe of fem_screw.py's
build_G2 + assemble_Q pipeline, used to check v13.926's claimed converged
positive lambda_1 for the full Lambda-weighted screw form at a=2.

Finding: lambda_1 is NOT converged with respect to ngrid (the G2 quadrature
grid resolution) at the N values v13.926 tested -- it was held fixed at
fem_screw.py's hardcoded default (ngrid=40001) throughout their N-sweep.
Refining ngrid alone (N fixed) or jointly with N shows lambda_1 shrinking
by 3-4x per doubling of ngrid with no plateau, consistent with an O(delta^2)
quadrature-error floor (delta = G2 grid spacing) being amplified by the
1/h^2 division in assemble_Q, not a genuine converged continuum eigenvalue.
"""
import sys, time
sys.path.insert(0, '.')
import fem_screw as fs
from scipy.linalg import eigh

a = 2.0


def lambda123(N, ngrid, g=None):
    g = g or fs.make_g('lambda', 2.0 * a)
    G2 = fs.build_G2(g, a, ngrid=ngrid)
    Q = fs.assemble_Q(a, N, G2)
    M = fs.assemble_M(a, N)
    return eigh(Q, M, eigvals_only=True, subset_by_index=[0, 2])


if __name__ == '__main__':
    g = fs.make_g('lambda', 2.0 * a)

    print("Reproduce v13.926's table exactly at their (implicit) ngrid=40001:")
    for N in [400, 800, 1600, 3200, 6400]:
        w = lambda123(N, 40001, g)
        print(f"  N={N:5d}  lam1={w[0]:.6e}  lam2={w[1]:.6e}  lam3={w[2]:.6e}")

    print("\nFixed N=800, refine ngrid (the actual convergence check they skipped):")
    for ngrid in [40001, 80001, 160001, 320001, 640001, 1280001, 2560001]:
        w = lambda123(800, ngrid, g)
        print(f"  ngrid={ngrid:8d}  lam1={w[0]:.6e}  lam2={w[1]:.6e}  lam3={w[2]:.6e}")

    print("\nJoint refinement (ngrid=200*N+1):")
    for N in [400, 800, 1600, 3200]:
        w = lambda123(N, 200 * N + 1, g)
        print(f"  N={N:5d} ngrid={200*N+1:8d}  lam1={w[0]:.6e}  lam2={w[1]:.6e}  lam3={w[2]:.6e}")

    print("\nScale-dependence of the instability (small N is fine; larger N drifts):")
    for N in [20, 100, 200]:
        print(f" N={N}:")
        for ngrid in [40001, 320001, 2560001]:
            w = lambda123(N, ngrid, g)
            print(f"    ngrid={ngrid:8d}  lam1={w[0]:.6e}")
