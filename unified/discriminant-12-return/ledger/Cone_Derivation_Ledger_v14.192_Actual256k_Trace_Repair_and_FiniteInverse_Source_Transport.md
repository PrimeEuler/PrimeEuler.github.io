# Cone Derivation Ledger v14.192 — Actual-256k Exact Trace Repair and Finite-Inverse Source Transport

Date: 2026-10-09
Track: Lane A
Status: [D] Exact trace repair and conservative source-transport theorem; [V] actual frozen witnesses evaluated with exact rational arithmetic. No infinite capacity closure.
Parents: v14.173–176, v14.185–191.

## Exact constrained finite solution

Let L=(P*P)^-1 P*, W contain the six frozen graph trials, u the stored source trial, and t=T v the original fixed source trace. Compute d=(LW)^-1(Lu-t), and x=u-Wd. Then Lx=t exactly. Both parities' rational trace identities are checked directly from the full frozen snapshots.

Let Q be the orthogonal complement of the frozen six-plane. The physical finite minimizer x_star of the original affine source problem satisfies Q(A x_star-g)=0 and Lx_star=t. Thus e=x-x_star lies in Q. The audited uniform finite Q floor gamma gives

    ||e|| <= s_x/gamma,
    <e,A e> <= s_x^2/gamma,
    s_x <= s_u+f_W ||d||,
    ||u-x_star|| <= ||W||_F ||d||+s_x/gamma.

Here s_u and f_W are the physical outward residual bounds from the existing certificate, including scalar and assembly uncertainty. These inequalities follow from C_Q e=Q(Ax-g), C_Q>=gamma I. No unit floor is assigned to C_Q.

## Physical finite-to-infinite cross-block bound

Write the off-diagonal divided-difference kernel as

    (z_n m-n z_m)/(n^2-m^2)
      =1/2[(z_n-z_m)/(n-m)-(z_n+z_m)/(n+m)].

On either parity lattice, the discrete Hilbert kernel 1/(n-m), diagonal zero, has norm pi/2: rescale the integer-lattice Fourier multiplier whose magnitude is at most pi. The positive Hankel kernel 1/(n+m) has norm at most pi/2 (the odd lattice is one half the classical Hilbert matrix; the even lattice is bounded entrywise by it). With the audited physical |z|<=11 (finite bound 11; remote bound 8), each commutator/anticommutator term is bounded by 11*pi/2. Multiplication by c=2/pi bounds the whole divided-difference cross block by 22.

The pole contribution has magnitude factor 2 and |p(n)|<=2/n. The full-front pole norm squared is at most 8 by sum_{n>=1} n^-2<=2. For n>R=256000 on one parity, its squared norm is at most 4/R, by the decreasing integral comparison. Hence its cross norm is at most 2 sqrt(8*4/R)<1, checked by squaring (128<R). The physical diagonal has zero cross block. Therefore ||B_{>R,<=R}||<23. This argument covers the original physical kernel, including both denominator channels; no bulk-only J approximation is used.

Define the represented-trial physical infinite residual rho_u=g_tail-Bu. Then the exact constrained residual rho_star=g_tail-Bx_star satisfies

    ||rho_star-rho_u|| <= eta=23[||W||_F ||d||+s_x/gamma].

This is a certified transport charge; it does not yet construct an outward representation of rho_u on the near octave and infinite far region.

## Actual frozen-256k result

| Quantity | Even | Odd |
|---|---:|---:|
| trace repair norm upper | 2.213672e-17 | 7.781094e-20 |
| corrected projected residual upper | 4.262406e-18 | 5.644622e-19 |
| finite Q floor | 2.37e-13 | 4.15e-12 |
| stored-to-exact finite solution norm upper | 1.798484e-5 | 1.360151e-7 |
| source transport eta upper | 4.136512e-4 | 3.128345e-6 |
| corrected finite energy error upper | 7.665866e-23 | 7.677528e-26 |

Displayed bounds round upward. Exact rational bounds, repair coefficients, and full input hashes are in `research-notes/payloads/actual256-finite-trial-transport.json`. Reproducer: `research-notes/suzuki_finite_trial_transport.py --root <decoded actual-256k archive> --output <output.json>`; run with the other committed producer modules in the same directory. Two complete runs are byte-identical; input snapshot arrays are hash-checked during decoding and each exact trace-repair identity is checked.

## Gate implications

The finite energy errors are tiny, but the coercivity-only norm transport is much larger. These conservative eta bounds can be used honestly in v14.190's contract; they do not establish the 5e-9 gate. An upper bound being large is not a lower bound on the true error and is not an impossibility result. The next refinement should exploit the finite energy estimate in a directional B C_Q^-1 B* bound, or certify action on the actual correction, instead of treating the entire inverse error with the worst gamma direction. Near/far construction of rho_u and actual admissible remote trials y remain open. The remote Schur inverse norm remains <=1, separately from gamma.

HANDOFF
target: sandbox
type: audit
parent: v14.192
status: open
action: Independently check the exact constrained trace repair, finite Q energy/norm error inequalities, physical cross-block norm 23, and actual frozen transport output. Identify any correction; optionally derive a sharper energy-weighted directional transport inequality from the same residual without requiring a small unweighted J defect.
deliverable: audit-or-correction
constraints: This is a transport baseline, not an executed remote trial or infinite closure. Lane A retains near/far source and operator-action certification; preserve the actual physical kernel and original fixed source trace. Re-read latest ledger/audit and collision-check before writes.
