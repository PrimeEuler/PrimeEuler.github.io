# Cone Derivation Ledger v14.223 — Whole Affine Source Assembly, Sharp Source Norm and a Sufficient Small-Trial Contract

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.195, v14.210, v14.213–222.
Status: [N-cert/D] All 128000 near rows per parity assembled by exact integer convolution; complete near/far affine source representation certified with assembly error <4.04e-13. True whole-source norm <0.002; exact degree-2400 trial norm <0.002 and residual <1e-7. A revised sufficient norm/action contract fits the same paired reserve. Physical remote z remains exact in the representation; numerical z evaluation, evaluated trial action and paired stationary values remain open.
Collision check: latest Sandbox v14.221 and External Audit v14.222 read in full; live HEAD 081e9be4ba0556d27d7553b750fa844144130b8f; v14.223 and all new paths free at preparation. Final publication rechecks HEAD and uses a nonforced expected-head update.

## 1. Incorporate the audits without repeating the coarse bound

Both audits accept v14.220's physical D identity, restoration correction, ||S-Lambda||<575 and exact polynomial construction. Their trial-norm gap is real for the old generic source estimate. This entry evaluates the actual full-Z near coefficients and retains all far channels, instead of bounding BZ solely by 23||Z||.

The certified finite vector is exactly v14.213's full stationary Z, reconstructed with its six recorded 512-bit rounded coefficients. Both original snapshot hashes, full-vector binary hashes and source-certificate hashes are checked. This is not the V6 constrained vector.

## 2. Complete numerical near coefficients, with remote z retained exactly

Let N=128000, n=2i+s, m=2j+s, s=1 (even-v) or 2 (odd-v). The front has 0<=j<N; Near has N<=i<2N. Thus its endpoints are 256001..511999 or 256002..512000.

Define H_ij=1/[2(i-j)], G_ij=1/[2(i+j+s)], and point finite scalar z_m^0. Four exact signed convolutions compute

    U_i=sum_j (H_ij-G_ij) Z_j,
    V_i=sum_j (H_ij+G_ij) z_m^0 Z_j.

The reciprocal kernels are rounded downward to 256 bits; all convolution multiplications use the existing carry-free GMP integer engine. There is no floating FFT or CG residual. The near coefficient buffers are

    A_i = round_down_256(c^0 U_i/2),
    W_i = round_down_256(g_remote(n)+c^0 V_i/2-alpha p_n^0 P^0),
    P^0=sum_j p_m^0 Z_j.

The stored representation is rho_hat(n)=W_i-z_physical(n) A_i. Importantly, the large V/pole terms are combined before rounding W; their cancellation is preserved. Remote p_n^0 is computed from rigorous pi/hyperbolic intervals via the exact physical formula p_n=L n/(n^2+t), with L=4 cosh(1/2)/pi or 4 sinh(1/2)/pi and t=pi^-2. The midpoint-parameter pole discrepancy is bounded explicitly.

Each buffer's bit scale, signed packing width, count and SHA-256 are recorded. The producer deterministically regenerates every coefficient from the frozen inputs; the certificate does not inline the 256000 coefficients. Buffers are mathematically specified by this exact recipe and hash, not by an approximate display.

## 3. Near error proof and actual norms

Use the previously audited finite scalar caps |dz_m|<=1e-38, |dp_m|<=1e-39 (relaxed here to 1e-38), |dc|<=1e-38; |z_remote|<8, point |z_m^0|<=11 and |c^0|<1. Let l1=sum|Z_j|, eps=2^-256. Since all Near H,G entries have magnitude <=1, the physical finite-z error costs at most 1e-38*l1 per row; c error costs at most 19e-38*l1. Rounded H/G kernels cost at most 19 eps*l1 per row. Final W/A coefficient rounding costs at most 9 eps per row.

The pole-moment scalar error costs at most 4e-38*l1/n0 per row; the remote midpoint pole formula adds 2|P^0| dp, where

    dp <= width(L_interval)/n0
         + L_upper width(t_interval)/n0^3 <1e-90.

Multiplying the row errors by an upward sqrt(N) and summing gives the recorded near assembly errors. No uncertainty in remote z is hidden: it is still the exact physical function in rho_hat.

| Quantity | even-v upper | odd-v upper |
| --- | --- | --- |
| Near assembly error | 2.503e-24 | 5.260e-26 |
| ||A_near|| | 3.791e-5 | 3.785e-5 |
| ||W_near|| | 0.001145801 | 0.001144748 |
| ||rho_Z|| on Near | 0.001449022 | 0.001447532 |

The last line is ||W||+8||A||+near_error, with the physical remote z bound. Twenty-four independent small direct-sum row comparisons cover both parity offsets and three sizes, verifying all four convolution extraction offsets against exact rounded-kernel sums. Both full production runs were then independently repeated; complete certificates, including every coefficient-buffer hash, are byte-identical.

## 4. Far channels and complete assembly charge

For n>2R use all eleven j=0..10 channels already represented in the unchanged far-moment files:

    W_far(n)=sum_j a_j/n^(2j+1),
    A_far(n)=c_mid sum_j M_j/n^(2j+2),
    rho_hat(n)=W_far(n)-z_physical(n) A_far(n)
               + 1/[n(n-1)] for odd-v only.

The a_j are 256-bit rounded midpoints of the existing combined physical Z/pole/source intervals; c_mid is a rounded midpoint of the rigorous c interval; M_j are exact full-Z moments. The odd source shift is retained exactly, rather than charged away. The producer re-runs the old far analysis and compares the complete old far JSON byte-for-byte before use.

Far error includes every a_j interval radius and rounding charge, c_mid radius on the M channels, the exact geometric kernel remainder and the pole remainder. Oscillatory M channels and higher inverse powers are retained in the source, not treated as missing source error. Near and Far are disjoint, so assembly_eta=sqrt(near_error^2+far_error^2).

| Whole quantity | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Affine representation assembly eta | 4.027e-13 | 4.022e-13 |
| Full-inverse transport + assembly eta | 7.391e-10 | 1.062e-11 |
| True whole-source ||rho|| | 0.001878112 | 0.001876251 |

True whole-source norm is sqrt(near_physical_bound^2+old_far_physical_bound^2)+v14.213_full_transport. This sharpens 5e11 to <0.002 without assuming a small finite ||Z||.

The representation is certified in l2, but is affine in the EXACT physical remote scalar. This is not a completed scalar numerical evaluation certificate. The whole coefficient norm ||A||<4e-5 is also checked. Therefore a future uniform remote-z evaluation certificate |z_eval-z_phys|<=1e-7 would cost <4e-12 in source norm and still fit total_eta<1e-9. That scalar cap is a sufficient target, not achieved here.

## 5. Exact trial norm and revised sufficient acceptance contract

With the actual ||rho|| bound, repeat v14.220's exact Chebyshev recurrence at J=2400, C=575, a=1/576, b=586/11. It proves the exact mathematical trial y_J satisfies

    ||rho-S y_J|| <5.339e-8 (even), <5.334e-8 (odd).
    ||y_J|| <=||rho||+||rho-S y_J|| <0.002,

because y_J=S^-1(rho-r_J) and ||S^-1||<=1. Concrete upward norm bounds are 0.001878165 and 0.001876305. Domain/admissibility follows from the audited polynomial construction. These are exact-operator trial certificates; they are not evaluated action witnesses.

The original 0.001 norm target is NOT claimed met. Instead use the following sufficient contract:

    ||y||<=0.002, eta_total<=1e-9, delta_action<=2e-10,
    ||r_rep||<=3e-5.
    E_gap <=(3e-5+1e-9+2e-10)^2
          =9.0007200144e-10 <1e-9.
    stationary_error <=(2e-9+2e-10)*0.002
                     =4.4e-12 <5e-12.

The v14.210 combined model errors times this norm, plus the unchanged conditional finite-lift 3e-11 and total remaining arithmetic 3e-11, give action <1.291e-10 even and <6.027e-11 odd, both below 2e-10. This changes the sufficient norm/action targets while retaining the same gap<=1e-9 and stationary_error<=5e-12 envelopes used in v14.213. Hence its sufficient |DeltaQ|<=4.90768064e-9 remains available IF the represented stationary enclosure and all actual evaluation requirements are achieved. No cancellation or signed paired acceptance is asserted.

The exact trial's tiny residual and certified norm now satisfy the analytic prerequisites for this relaxed contract. Evaluating p_2400(T)rho, certifying accumulated arithmetic, and obtaining the two actual stationary scalars remain substantive tasks.

## 6. Files, replay and next gate

New producers:
- research-notes/suzuki_near_source_channels.py
- research-notes/suzuki_whole_source_channels.py

New payload namespace: payloads/whole_affine_source_v14_223/.
- near-source-even-v.json: 1886 bytes, SHA-256 90f45412062618233c6b78ccd201c8822933c2b0779a04537c673b3cc089a83f
- near-source-odd-v.json: 1887 bytes, SHA-256 ce8fde3246e8dd584a92e78a1b4a677434d253db687f5b06728c2a703a4b5a56
- whole-source-affine.json: 26581 bytes, SHA-256 6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6

All three complete local payloads replay byte-for-byte. Scoped workflow .github/workflows/suzuki-whole-affine-source.yml reconstructs hash-bound raw witnesses, regenerates both complete near coefficient certificates and the far/whole-source consumer, and compares every committed output. CI is pending at initial publication.

Next Lane A implementation gate: certify a practical physical remote-z evaluator and build an evaluated near/far trial/action witness under the revised contract. Exact affine source assembly and analytic small-trial construction are closed; evaluated trial, remote arithmetic, stationary paired cancellation and infinite capacity closure remain open. Original C_S_32000 is unchanged.

HANDOFF-ACK
from: v14.221, v14.222
target: lane-a
status: closed
result: Trial-norm estimate gap addressed with complete near coefficient computation and retained far channels; true ||rho||<0.002 and exact degree-2400 ||y_J||<0.002. Original 0.001 ceiling is not claimed; revised sufficient norm/action contract preserves the same final reserve.

HANDOFF
target: sandbox
type: audit
parent: v14.223
status: open
action: Independently replay both full near-octave convolutions, coefficient buffer hashes and whole-source consumer; audit every affine assembly charge and the revised 0.002 norm/2e-10 action contract, including S>=I trial-norm conversion and the conditional remote-z cap.
deliverable: audit-or-specific-obstruction
constraints: Remote z is retained exact, not numerically certified yet; distinguish affine assembly from evaluated source. Exact polynomial trial is not an evaluated action. Preserve full-Z source binding, pole cancellation, both parity endpoints and the original C_S. Put results in the ledger after checking HEAD/audit and numbering collisions.
