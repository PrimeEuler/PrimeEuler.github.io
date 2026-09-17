# Cone Derivation Ledger v13.568 — M16001 Remote-Row and Pre-Gram Certificate Specification

Date: 2026-09-17

## Scope

This entry freezes the next outward-certification interface downstream of the exact/replay basis handoff in the M16001 seven-plane audit. It is a specification checkpoint, not a numerical closure and not an inertia promotion.

The live source-faithful midpoint replay remains `research-notes/suzuki_M16001_even_index3_anisotropic_tail_split.py`, with explicit odd remote rows n=16003,16005,...,1999999 (991999 rows) and KEXP=8. The source implementation currently evaluates `tail_Z(n)` numerically; that evaluation remains an open outward source leaf.

## 1. Certified finite-moment input

The remote-row certificate consumes one immutable hashed replay handoff

    (W_hat, rho_W),   shape(W)=8001 x 10,

with finite odd modes

    j_r = 2r+1,  r=0,...,8000.

It then produces certified midpoint/radius pairs

    (p_hat, rho_p),           shape 10,
    (a_hat, rho_a),           shape 8 x 10,
    (b_hat, rho_b),           shape 8 x 10,

for

    p_i = sum_r c_r W_{ri},
    a_{q,i} = sum_r j_r^(2q+1) W_{ri},
    b_{q,i} = sum_r Z_r j_r^(2q) W_{ri},    q=0,...,7.

Integer powers are generated exactly by recurrences

    J_a(r,0)=j_r,
    J_a(r,q+1)=J_a(r,q) j_r^2,

    J_b(r,0)=1,
    J_b(r,q+1)=J_b(r,q) j_r^2.

The authoritative reduction certificate is exact dyadic/rational recomputation of the nominal sum followed by exact comparison with the stored replay midpoint. gamma_8001 is retained only as an independent arithmetic cross-check.

Finite Z and c payload conversion is already zero-radius under the earlier binary64-to-longdouble conversion certificates. Exact-source-versus-nominal uncertainty is a separate leaf and must either be supplied entrywise or explicitly remain OPEN; it must not be silently identified with conversion error.

## 2. Basis-independent remote scalar intervals

For every odd n in 16003..1999999, certify intervals for

    pi,
    alpha = 2/pi,
    Z_n^tail,
    d_{q,n} = n^(-(2q+2)),
    e_{q,n} = n^(-(2q+1)),
    h = cosh(1/2),
    k_n = n*pi/2,
    c_n = 2 k_n h / (k_n^2 + 1/4).

The integer n and all integer exponents are exact. Reciprocal powers, pi, cosh(1/2), and the complete tail_Z evaluation require directed/outward enclosures. The certificate must store the source identity and method used for each nonexact scalar family; ordinary `tail_Z(ns)` midpoint evaluation is not a certificate.

## 3. Remote-row recurrence

For coordinate i=0,...,9 and q=0,...,7 define

    U_{q,n,i} = Z_n^tail * a_{q,i} * d_{q,n},
    V_{q,n,i} = b_{q,i} * e_{q,n},

    T_{n,i} = alpha * sum_{q=0}^7 (U_{q,n,i} - V_{q,n,i}),
    H_{n,i} = 2 c_n p_i,
    R_{n,i} = T_{n,i} + H_{n,i}.

Every operation is evaluated as midpoint plus a nonnegative absolute radius. For two uncertain factors x,y,

    rho_xy >= |x_hat| rho_y + |y_hat| rho_x + rho_x rho_y + rho_mul.

For three uncertain factors x,y,z,

    rho_xyz >=
      |y_hat z_hat| rho_x + |x_hat z_hat| rho_y + |x_hat y_hat| rho_z
      + |z_hat| rho_x rho_y + |y_hat| rho_x rho_z + |x_hat| rho_y rho_z
      + rho_x rho_y rho_z + rho_arith.

The implementation may instead use exact dyadic recomputation of the nominal arithmetic discrepancy whenever all midpoint operands are dyadic; in that case the exact discrepancy is authoritative and gamma bounds are diagnostic only.

Required row endpoint:

    R_exact[n,i] in [R_hat[n,i]-rho_R[n,i], R_hat[n,i]+rho_R[n,i]].

The row artifact therefore has shape

    R_hat, rho_R : 991999 x 10.

Because this is large, chunked canonical payloads are permitted, but the manifest must bind the ordered chunk list, row ranges, dimensions, and SHA-256 of every midpoint/radius chunk.

## 4. Machine-checkable remote-row transcript fields

At minimum the transcript records:

- upstream SHA-256 for W_hat, rho_W, p/a/b midpoint and radius payloads;
- remote odd-row count = 991999;
- coordinate count = 10;
- q count = 8;
- first/last n = 16003/1999999;
- exact-source status for finite Z,c;
- interval-source/method identity for pi, cosh(1/2), and tail_Z;
- maximum radius and its (n,i) location for alpha, tail_Z, inverse powers, c_n, T, H, and R;
- all radii finite/nonnegative;
- all row interval checks PASS;
- ordered chunk hashes all MATCH;
- ARITHMETIC CERTIFICATE PASS/FAIL;
- EXACT-SOURCE CERTIFICATE PASS/OPEN/FAIL.

No PASS boolean is evidence by itself: the checker recomputes every relation from the hashed payloads.

## 5. Missing pre-Gram contribution

Let

    R_{ni} = R_hat_{ni} + delta_{ni},
    |delta_{ni}| <= rho_{ni}.

For the exact remote Gram G=R^T R, the operand/row-formation uncertainty satisfies entrywise

    E_preGram[i,j] = sum_n (
        |R_hat[n,i]| rho[n,j]
      + |R_hat[n,j]| rho[n,i]
      + rho[n,i] rho[n,j]
    ).

Equivalently,

    E_preGram = |R_hat|^T rho_R
              + rho_R^T |R_hat|
              + rho_R^T rho_R.

This is the missing term identified in the earlier M16001 DAG. It is distinct from the already-transcripted nominal Gram reduction rounding and chunk-addition rounding.

The final remote Gram entry radius is

    E_G[i,j] = E_preGram[i,j]
             + E_gramRnd[i,j]
             + E_chunkAdd[i,j].

All three are nonnegative 10 x 10 matrices. The certificate must accumulate E_preGram outward. Blind BLAS evaluation is not accepted as a proof step: use exact dyadic accumulation, explicit directed scalar loops, or a separately transcripted gamma enclosure for each matrix-product reduction.

## 6. Pre-Gram machine-checkable fields

Required fields:

    shape = [10,10]
    remote_row_count = 991999
    E1 = |R_hat|^T rho_R
    E2 = rho_R^T |R_hat|
    E3 = rho_R^T rho_R
    E_preGram = E1+E2+E3
    E_gramRnd = imported v13.512-compatible transcript
    E_chunkAdd = imported v13.512-compatible transcript
    E_G = E_preGram+E_gramRnd+E_chunkAdd

For each matrix store a canonical outward payload SHA-256, maximum entry with index, Frobenius upper bound, symmetry check where applicable, and the upstream row-payload manifest hash. E1 and E2 need not individually be symmetric, but the checker must verify E2=E1^T under the same certified accumulation convention or safely enclose both independently. E3, E_preGram, and E_G must be symmetric up to the chosen outward representation.

## 7. Separation from the far branch

This explicit-row certificate is independent of the far branch n>=2000001 once the shared finite basis/moment inputs are frozen. The far branch continues separately through S_Z, S_J, S_J2Z, then L,B,C and adverse f_Q^U,f_N^U,f_X^U endpoints. It does not require the million-row tail_Z payload.

## 8. Certification status after this entry

CLOSED/FROZEN BY SPECIFICATION:

- dimensions and recurrence for p,a_q,b_q;
- dimensions and recurrence for each explicit remote row;
- required separation of arithmetic conversion error from exact-source uncertainty;
- exact entrywise pre-Gram formula;
- separation of E_preGram from existing Gram/chunk rounding;
- canonical hash/manfiest dependency chain required for replay.

STILL OPEN NUMERICALLY:

- exact rational P/N/B construction and its replay handoff;
- finite exact-source Z,c entrywise treatment if needed;
- outward pi and cosh(1/2) endpoints;
- outward tail_Z(n) source/evaluation enclosure for all 991999 rows;
- directed inverse-power evaluation;
- numerical rho_R payload;
- numerical E_preGram and final E_G;
- far-tail adverse endpoints;
- finite Q/N block endpoint certification;
- final Schur lower endpoint.

Therefore no stronger inertia theorem is promoted here. The final gate remains

    a_N^L - (||B_QN||_2^U)^2 / lambda_Q^L > 0.

## Next concrete breakpoint

The next meaningful ledger entry should be numerical rather than architectural: either (i) exact P/N/B construction with a machine-checked nonzero det[B] and hashed payloads, or (ii) an outward tail_Z source/evaluation certificate strong enough to close the explicit remote-row source leaf. The exact P/N/B gate is the preferred upstream target because both the explicit-remote and far branches depend on it.
