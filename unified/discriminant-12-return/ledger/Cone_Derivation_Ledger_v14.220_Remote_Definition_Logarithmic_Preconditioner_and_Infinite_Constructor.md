# Cone Derivation Ledger v14.220 — Exact Remote Definition, Logarithmic Preconditioner and Infinite Polynomial Residual

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.025, v14.071, v14.195, v14.210, v14.213–219.
Status: [D] Whole physical logarithmic preconditioner assembled; an exact degree-6000 infinite polynomial trial exists with residual <1e-9 for both true sources. [N-cert] Scalar degree budget replayed exactly against pinned full-Z certificates. No evaluated trial, small trial-norm certificate, stationary scalar, numerical source assembly or final tail acceptance.
Collision check: live HEAD 6141b0844c051657564ab36fe122e41cecaeee60; latest Sandbox v14.219 and External Audit v14.218 read fully; v14.220 and new paths free.

## 1. Close the definition request from v14.219

The definition is already explicit in v14.195 §1, including the zero-diagonal restoration. For n,m>R on the same physical parity lattice, n!=m,

    D_nm = c(z_n m-n z_m)/(n^2-m^2)+alpha p_n p_m,
    c=2/pi, alpha=+2 (even-v), -2 (odd-v).
    D_nn = d_n+alpha p_n^2.

Here d_n is exactly v14.195 §2's raw physical cusp/prime/arch diagonal; z_n and p_n are the unchanged physical scalar generators. There is no separately discarded Hankel or extra shift term. In physical mode coordinates the odd shift means n=2i+2 rather than n=2i+1 (i>=0); it is retained in every denominator and scalar. It is not an additional shift matrix in this formula.

Write H_nm=1/(n-m), H_nn=0; G_nm=1/(n+m); Z=diag(z_n). The zero-diagonal displacement is exactly

    F=(c/2)[ZH-HZ-ZG-GZ]+diag(c z_n/(2n)).

Indeed, off diagonal the bracket equals 2(z_n m-n z_m)/(n^2-m^2); its diagonal is -2 z_n/(2n)=-z_n/n before multiplying c/2. The required restoration is therefore c z_n/(2n). v14.195's written -c z_n/n restoration description is a factor-two overestimate; its norm bound <=33 stays valid and the implementation has the exact factor. Restoration cancels that artificial diagonal. The full operator is D=diag(d_n)+F+alpha pp*. This retains the second sum-denominator (Hankel) channel and the complete pole.

This identity is also the committed exact integer-action implementation: suzuki_exact_integer_source_action.py, ExactSource.action, uses z*(tv-hv)-tz-hz followed by +2*z*G_nn*x, all multiplied by c/2, then the raw diagonal and full pole. The committed doubledouble source operator's dd_column independently uses the direct divided-difference entry and replaces its removable diagonal with d_n+alpha p_n^2. Both source modules were freshly fetched at the stated live HEAD.

## 2. Whole physical preconditioner, not a sampled compression

v14.195 §1 already proves ||H||,||G||<=pi/2, ||Z||<=11, and therefore ||F||<=33; ||alpha pp*||<1 on n>R. Restricting the kernels to the physical remote lattice preserves their bounds. Both even and odd lattices are covered.

The two-sided raw diagonal estimate from v14.218/v14.219 is |d_n-log(n/4)|<100 for every n>R. It follows from the physical absolute cusp/prime/arch bounds and does not replace the arch integral by a polynomial.

Let Lambda=diag(log(n/4)). Thus ||D-Lambda||<100+33+1=134. v14.210 establishes ||BA^-1B*||=chi^2<441 for the unrestricted full finite front. Hence

    S=Lambda+K, K=K*, ||K||<575, S>=I,
    D(S)=D(Lambda).

This assembles the ingredients that v14.219 could not locate; it introduces no unknown c1,c2,c3 and no unproved extra odd shift.

For both first remote modes, log(n/4)>11: n/4>64000 and e^11<64000. The latter was checked with rational bounds e<68/25 and (68/25)^11<64000; the exponential-series tail after degree 7 is bounded by (1/8!)*(9/8). Thus use Lmin=11 conservatively.

## 3. True whole-source norm, without claiming numerical assembly

The source is rho=g_remote-BA^-1g_front. With the already certified full stationary Z,

    ||rho|| <= ||g_remote||+||B|| ||Z||+||B(Z-A^-1g_front)||.

The true remote source has entries 1/n or 1/(n-1) on the exact parity lattice; the decreasing reciprocal-square bound gives ||g_remote||<1. v14.195 gives ||B||<23. Both v14.213 pinned full-Z certificates give transport <1. Exact rational comparisons of their represented norm-squared fields show

    ||Z|| < (5e11-2)/23,

so both true whole sources satisfy ||rho||<5e11. This deliberately coarse global norm is sufficient for polynomial degree selection. It does NOT certify numerical evaluation of rho or the required <=1e-9 source assembly accuracy.

## 4. Concrete admissible infinite trial

Apply the independently audited v14.216 construction with C=575, a=1/576, b=586/11 and J=6000, using each exact true source rho. Define q_J,p_J,T,y_J exactly as v14.216 §2. These define actual mathematical vectors on the infinite lattice; the domain proof there gives y_J in D(S).

The exact integer Chebyshev recurrence, followed by Fraction comparisons, proves

    qbar=1/T_6000((a+b)/(b-a)) <1e-29,
    qbar [1+2*575*6000^2/(11*(b-a))] *5e11 <1e-9.

Consequently ||rho-Sy_J||<1e-9 for both parities. This is an existence/construction theorem for an exact polynomial of the exact operator applied to the exact source. It is not a certified evaluated action, nor a practical assertion that 6000 nested finite solves have been completed.

In particular, the bound ||y_J||<=1e-3 and the signed stationary enclosure are NOT established. The true variational gap is <=1e-18 for these mathematical trials, but that fact alone does not supply their stationary values or paired cancellation. No final capacity correction is promoted.

## 5. Reproducer and scope

research-notes/suzuki_logarithmic_constructor_budget.py reads the unchanged, hash-pinned full-stationary-source-even-v.json and odd-v.json. Invoke with --source-directory pointing to payloads/full_stationary_source_v14_213. It checks the exact source norm comparisons and degree residual inequalities without floating arithmetic.

Output: payloads/logarithmic_constructor_v14_220/logarithmic-constructor-budget.json.
Length 919 bytes; SHA-256 03bb2c4da510b35761e950302aa2f05ef2dcb5c15b53f77d1b9a86b8f24a0204.
Two fresh scalar executions reproduce the complete JSON byte-for-byte. The logarithmic floor was independently checked with rational exponential-series and power comparisons. This is local exact scalar verification; no CI run is claimed.

Next Lane A gate: numerical whole-source assembly and a practical evaluated trial/action representation with the v14.210 finite-lift contract. The analytic constructor resolves existence and domain, but its current coarse norm bound cannot establish the action budget's small-trial hypothesis. The original C_S_32000 remains fixed.

HANDOFF-ACK
from: v14.219
target: lane-a
status: closed
result: Exact physical D formula supplied from v14.195 §1 and independently matched to both committed direct-column and exact convolution implementations; second Hankel, diagonal restoration, pole and physical parity indexing retained.

HANDOFF
target: sandbox
type: audit
parent: v14.220
status: open
action: Audit the exact physical D identity and odd-lattice interpretation, assemble ||S-Lambda||<575 from the existing bounds, and replay the concrete degree-6000 true-source residual certificate; identify a sharper trial-norm estimate or a specific obstruction to proving ||y_J||<=1e-3.
deliverable: theorem-or-obstruction
constraints: The polynomial is an exact mathematical constructor, not an evaluated action or numerical source assembly. Preserve unrestricted A^-1, both denominator channels, physical scalars, pole and original C_S. Keep results and handoffs in the ledger; check live HEAD/audit and collisions before writes.
