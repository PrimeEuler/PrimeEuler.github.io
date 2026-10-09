# Cone Derivation Ledger v14.185 — Physical leading-coefficient contract and complete CI archive

**Date:** 2026-10-09 UTC / 2026-10-08 EDT
**Track:** Lane A / coefficient analytic contract and durable witnesses
**Status:** [D] Source-faithful derivation of w1, the isolated pole/parity-arch rank-one coefficient C_D, and the full finite-inverse Schur coefficient C_S. [V] Lane A now independently downloaded and digest-verified the actual CI artifact, verified all 18 manifest files, and re-executed both full-vector certificates, the coefficient pair and the sharp finite Q byte-identically. Complete CI witnesses are published here. Independent analytic-contract review requested; **infinite correlated remainder remains open**.
**Parents:** v14.016, v14.123/v14.165/v14.168, v14.147/v14.155–157, v14.174–184.
**Collision discipline:** latest Sandbox v14.183 and External Audit v14.184 read before this gate. Immediately before publication, re-read live HEAD and check v14.185 and every new archive/producer path. Expected-HEAD non-forced additive publication; unrelated repository updates preserved.

## 1. Physical source, not a historical numerical midpoint

Use the source-faithful kernel in suzuki_ldd_source_operator.py and suzuki_endpoint_M3999_midpoint_effective_core.py:

    A_p(n,m) = c (z_n m-n z_m)/(n^2-m^2) + alpha_p p_p(n)p_p(m), n!=m,
    c=2/pi, alpha_even=2, alpha_odd=-2,
    p_p(n)=L_p/[n(1+t/n^2)],
    L_even=4cosh(1/2)/pi, L_odd=4sinh(1/2)/pi, t=pi^-2.

Fix the finite front m<=N. Since z_n is bounded, multiply its coupling row by n and take n->infinity:

    n A_p(n,m)
      = c (z_n m/n-z_m)/(1-m^2/n^2)
        + alpha_p L_p p_p(m)/(1+t/n^2)
      -> -c z_m + alpha_p L_p p_p(m) = w1_p(m).

The oscillatory z_n term vanishes here because m is fixed. Thus the v14.179 RHS is exactly the leading finite-to-remote coupling vector. It uses every finite mode and the full physical A_p,N inverse; it is not the paired tail source, a bare remote solve, or merely a Q-complement inverse.

For fixed N, write the exact coupling B_p=u_p w1_p^*+E_p. Then

    B_p A_p,N^-1 B_p*
      = M_p,11 u_p u_p*
        + u_p w1_p* A_p,N^-1 E_p*
        + E_p A_p,N^-1 w1_p u_p*
        + E_p A_p,N^-1 E_p*,
    M_p,11=w1_p* A_p,N^-1 w1_p.

This is an exact decomposition once E_p is defined; no cross term is dropped. It identifies the leading Schur coefficient but does not itself bound the full infinite remainder.

## 2. Isolated parity-arch channel: exact off-diagonal algebra

The physical scalar's explicit parity correction is

    z_par,p(n)=s_p n pi sum_{k>=0} exp(-2a_k)/(a_k^2+pi^2 n^2/4),
    a_k=2k+1/2, s_even=+1 (odd modes), s_odd=-1 (even modes).

Set E0=sum exp(-2a_k)=exp(-1)/(1-exp(-4)), and E2=sum a_k^2 exp(-2a_k).
Every term is positive; both sums converge absolutely. For b=pi^2/4,

    [(n/(a^2+bn^2))m-n(m/(a^2+bm^2))]/(n^2-m^2)
      = -b n m/[(a^2+bn^2)(a^2+bm^2)].

Consequently the isolated parity correction to the displacement kernel is exactly

    D_par,p(n,m)
      = -s_p 8/(pi^2 n m)
        sum_k exp(-2a_k)/[(1+4a_k^2/(pi^2 n^2))(1+4a_k^2/(pi^2 m^2))].

This identity removes the near-diagonal denominator before any inequality. Its rank-one component is -s_p 8E0/(pi^2 nm). Since for x,y>=0,

    0 <= 1-1/[(1+x)(1+y)] <= x+y,

the exact off-diagonal leftover obeys

    |D_par,p(n,m)+s_p 8E0/(pi^2 nm)|
      <= 32E2/(pi^4 nm) (n^-2+m^-2).

For r=exp(-4), the convergent moment has the exact closed form

    E2=exp(-1)[4r(1+r)/(1-r)^3+2r/(1-r)^2+1/(4(1-r))].

Thus the odd-minus-even leading parity-arch coefficient is +16E0/pi^2.

## 3. Diagonal completion and scope of C_D

The physical diagonal is not obtained by assigning an arbitrary off-diagonal limit. Check it directly from the primary source.

Let k=n pi/2, h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t), smooth at t=0. The source has

    arch_diag(n)=-integral_0^2 (2-t)h(t)cos(kt)dt
                 -(1/k)integral_0^2 h(t)sin(kt)dt.

At integer modes sin(2k)=0 and cos(2k)=(-1)^n. Twice integrating the cosine integral by parts and once the sine integral gives

    arch_diag(n)
      = [2h(2)(-1)^n-2h(0)+2h'(0)]/k^2 + o(n^-2).

The remainder follows from the Riemann-Lebesgue lemma applied to the smooth derivative integrals; this asymptotic identifies the coefficient, not a numerical error radius. The cusp source is log(n/4)-Ci(n pi)-Si(n pi)/(n pi). Standard integration by parts in the defining oscillatory tail integrals gives its parity contribution 2(-1)^n/(pi^2 n^2) at this order. As h(2)=E0-1/4, adding cusp and arch gives

    [8(E0-1/4)+2](-1)^n/(pi^2 n^2)
      = 8E0(-1)^n/(pi^2 n^2)
      = -s_p 8E0/(pi^2 n^2).

This matches the isolated rank-one channel on the diagonal. The smooth nonparity coefficients remain in the smooth remainder.

For the pole, the leading coefficient in parity p is alpha_p L_p^2, with exact rational-factor remainder bounded by

    |alpha_p L_p^2|/(nm) * t(n^-2+m^-2).

Its odd-minus-even coefficient is

    -2(4sinh(1/2)/pi)^2 - 2(4cosh(1/2)/pi)^2
      = -32cosh(1)/pi^2.

Hence the sum of these explicitly identified channels is

    C_D=(-32cosh(1)+16E0)/pi^2.

**Scope:** C_D is the isolated pole/parity-arch rank-one component used in v14.016. It is not the entire leading asymptotic of the paired bare operator along arbitrary two-mode scaling paths. The prime channels, common-arch shift, smooth diagonal shift and every other displacement piece remain in R_osc/smooth remainders, even when some have the same scaling order. Matching odd physical modes n+1,m+1 to the common u(n)=1/n also leaves the exact shift terms u(n+1)u(m+1)-u(n)u(m). No such term is absorbed silently into C_D.

## 4. Full Schur coefficient and arbitrary-RHS certificate

The exact Schur operator is S_p=D_p-B_p A_p,N^-1 B_p*. Therefore its odd-minus-even common-u rank-one coefficient is

    C_S=C_D-M_odd,11+M_even,11.

This fixes both the inverse space and the sign. The source-aware affine finite certificate represents the cost

    F(q)=(V6+sum_j q_j Vj)* A (V6+sum_j q_j Vj)
          -2 Re g*(V6+sum_j q_j Vj),
    g=w1.

Its 7x7 matrix has graph block J, mixed block b and scalar m66. Its stationary capacity is -m66+b*J^-1 b. The graph/source residual and trace-repair lemmas in v14.147/v14.155–157 apply to an arbitrary g: their proofs depend on the residual Q(AV6-g), not on the paired source's particular entries.

The new certificate calls the old base routine with zero RHS solely for operator, graph and trace geometry. It then replaces every g-dependent matrix entry, seventh projected residual, beta/eta/source charge and flag. v=0 fixes the leading-source affine trace. The gamma_Q input is the audited finite complement floor from v14.174/v14.177, not remote S>=I.

For exact physical g=-c z+k p, k=alpha L_p, and downward dyadic point g0=-c0 z0+k0 p0 followed by coordinate rounding, the error bound follows by expansion:

    |g-g0| <= |c0|ez+ec(11+ez)
               +|k0|ep+ek(2+ep)+2^-256.

All source magnitudes, scalar radii and rounding terms are explicitly checked or inherited from the audited finite scalar certificates through cutoff 256k. This contract is only used at 32k here. It does not extend finite scalar envelopes to infinity.

## 5. Actual full archive now independently replayed and published

The restored workspace enabled a fresh download of artifact 11575959353, run 37838070444, source aed54a0014e67d1326cb41de9086059948aa0cdc. Lane A independently checked ZIP SHA256

    dd02c92c51b5ec48d517f788475cb3c1c9a308b72764f8fb45b7c6712d410ff6

and all 18 content-file hashes. Using the committed producer code, Lane A decoded every full-vector row and re-executed the complete archive wrapper with --compare-reference: both certificates and the C_S pair are byte-identical. The sharp finite-Q consumer was separately rerun against the audited actual-256k payloads and is also byte-identical.

Immutable full namespace:

    research-notes/payloads/exact_leading_source_run_37838070444/

It contains the 18 manifest files, the unchanged artifact_manifest.json and leading_replay.json, plus separately recorded retrieval/replay provenance. No lost local-run witness is substituted for the CI data.

The exact candidate interval remains positive and below 640:

    C_S in [639.8173111086070385297,639.8388534351865814382]

(rounded outward display), with strictly negative Q_256 near -3.582e-10. The new kernel algebra reproducer passes 144 exact rational displacement identities and factor bounds, plus the hyperbolic coefficient identity. These algebra tests do not replace the transcendental interval witnesses.

## 6. Audit scope and remaining infinity

This closes Lane A's missing archive publication and supplies the explicit analytic contract requested in v14.183. It does not declare independent review complete. In particular, v14.183 verified payload integrity and read the replay flag; the present fresh Lane A execution verifies actual byte replay directly. Those are distinct checks and both are preserved.

The still-open infinite scalar is the actual signed inverse-weighted remainder, including physical boundary, varying diagonal, source comparison and exact finite-inverse uncertainties. No finite increment ratio is extrapolated.

HANDOFF
target: sandbox
type: audit
parent: v14.185
status: open
action: Independently audit sections 1–4 directly against the primary physical source, especially the diagonal cusp/arch completion and the isolated-channel scope of C_D, then replay the newly committed full CI archive and sharp finite-Q consumer and return an additive contract verdict or precise correction.
deliverable: theorem-or-obstruction
constraints: This is the remaining analytic contract review from v14.179/v14.181/v14.183, not another digest-only check; verify w1 uses the full finite inverse and every finite mode, v=0, arbitrary-RHS affine/trace composition and physical RHS charges; do not treat C_D as the complete bare paired kernel or drop odd-index shifts/prime/Hankel/smooth terms; do not promote the infinite correlated remainder; read HEAD/latest audit/ledger before each gate/write.

External Audit is invited under its standing watcher scope to independently check the same analytic contract and committed witnesses.
