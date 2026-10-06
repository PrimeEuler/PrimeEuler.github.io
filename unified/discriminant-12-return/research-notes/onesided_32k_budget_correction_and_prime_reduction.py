#!/usr/bin/env python3
"""v14.092/093 correction and prime-channel structural target.

This producer does two independent things.

(A) Correct the one-sided 32k oscillatory bookkeeping:
    * use the actual N=32000 amplitude A_e=1200.458705... rather than the
      inherited 804 constant;
    * keep the J=300 product ||w_o||||w_e||=3.7281e-9 explicitly labelled
      as a finite-window diagnostic, not a theorem input;
    * recompute the resulting diagnostic break-even joint constant.

(B) Freeze the exact leading-prime structural constant obtained by combining
    each q-channel's leading off-diagonal Toeplitz piece with its matching
    prime-diagonal cosine piece BEFORE taking norms.

For q=3,4,5,7 the full-line frequency shift is a nilpotent partial isometry
of order 2, giving channel norm <= C_q/2.
For q=2, pi/3 < phi_2 < pi/2, so the shift is nilpotent of order 3, giving
channel norm <= C_2/sqrt(2).
The half-line/finite near block is a compression, so the same bounds hold.

This is not a closure theorem: second-identity/Hankel pieces, smooth terms,
the finite-Schur oscillatory remainder, and most importantly a rigorous
full-near-block quadratic-form/localization bound remain.
"""
from __future__ import annotations
import math

N=32000
A_E=1200.4587051950723326859704612197054
A_O=1184.9475540161082531811400666425518
A_MAX=max(A_E,A_O)
M_PRIMARY=1.8869797018800170e-5
WPROD_J300=3.7281e-9
SMOOTH_RESERVE=2.0e-8

QS=(2,3,4,5,7)
WS=(
    math.log(2)/math.sqrt(2),
    math.log(3)/math.sqrt(3),
    math.log(2)/2,
    math.log(5)/math.sqrt(5),
    math.log(7)/math.sqrt(7),
)

def k10():
    scale=(8000.0/64000.0)**22.5
    R10=1.21e-10*1e20*scale
    u_norm=1.0/math.sqrt(2*N)
    cross=2*math.sqrt(A_MAX)*u_norm*R10
    sub=R10*R10
    return R10,cross+sub

def main():
    du=2*A_MAX/(math.sqrt(12)*N*N)
    R10,k10tot=k10()
    fixed=du+k10tot+SMOOTH_RESERVE
    unit=A_E*WPROD_J300
    break_even=(M_PRIMARY-fixed)/unit

    print("=== corrected N=32000 one-sided bookkeeping ===")
    print("A_e_32k =",repr(A_E))
    print("A_o_32k =",repr(A_O))
    print("A_max_32k =",repr(A_MAX))
    print("delta_u_corrected =",repr(du))
    print("K10_R10 =",repr(R10))
    print("K10_total_corrected =",repr(k10tot))
    print("smooth_reserve =",repr(SMOOTH_RESERVE))
    print("M_primary =",repr(M_PRIMARY))
    print("wprod_J300_DIAGNOSTIC_ONLY =",repr(WPROD_J300))
    print("unit_cost_using_J300_DIAGNOSTIC =",repr(unit))
    print("break_even_joint_using_J300_DIAGNOSTIC =",repr(break_even))
    print("GUARDRAIL: J=300 w-product is not a full-near-block theorem input.")

    print("\n=== leading prime channel combination ===")
    total=0.0
    for q,w in zip(QS,WS):
        phi=math.pi*math.log(q)/2
        Cq=4*w*abs(math.sin(phi/2))
        if q==2:
            fac=1/math.sqrt(2)
            nilpotency=3
            assert math.pi/3 < phi < math.pi/2
        else:
            fac=0.5
            nilpotency=2
            assert phi > math.pi/2
        b=Cq*fac
        total+=b
        print(f"q={q} phi={phi:.15g} Cq={Cq:.15g} "
              f"nilpotency={nilpotency} factor={fac:.15g} bound={b:.15g}")
    print("combined_leading_plus_diagcos_constant =",repr(total))
    print("GUARDRAIL: does not include second-identity/Hankel, smooth, or Schur oscillatory remainder.")

if __name__=="__main__":
    main()
