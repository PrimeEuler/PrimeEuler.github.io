# Cone Derivation Ledger v14.210 — Whole-Remote Schur Channel Model and Trace-Aware Finite-Lift Contract

Date: 2026-10-09 EDT
Track: Lane A / next action certificate gate
Parents: v14.071, v14.147/v14.156/v14.157, v14.174/v14.177, v14.185, v14.195–209.
Status: Analytic whole-remote model approximation proved with actual frozen-256k certificate constants; exact rational budget replay passed. Finite-lift and remaining arithmetic tolerances are sufficient targets, not achieved producer certificates. No admissible infinite correction trial or final paired-tail acceptance is claimed.
Collision check: latest Sandbox v14.208 and External Audit v14.209 read. Immediate publication check must preserve live HEAD and use next-free v14.210 with a nonforced expected-head update.

## 1. Incorporate the completed audits

v14.208 confirms the actual-256k archive and coefficients. v14.209 independently reconstructs all original files and re-derives the coefficient intervals. Its display-rounding note is correct: display_approximate is round-to-nearest, not an outward decision bound. This entry uses only exact rational fields, and checks every public decimal ceiling by a strict Fraction comparison. The v14.207 complete archive is unchanged.

Fix R=256000, N=128000 finite modes per sector. A=A_p,R is the full finite front; B couples it to all n>R; D is the exact bare remote block; S=D-BA^-1B* >=I by v14.071. Q is the finite frozen-plane complement with gamma_e=2.37e-13, gamma_o=4.15e-12. These three operators and their floors remain distinct.

## 2. Certify a full finite inverse bound from the existing normalized graph

Let Wtilde be the first six represented columns of the pinned leading-source snapshot, rho their certified relative trace defect, and Wc=Wtilde Rtr the exact trace-corrected graph, with ||Rtr||<=1/(1-rho). The frozen normalizer T is invertible; thus the graph's protected traces span the entire six-plane.

Let C=QAQ|Q >=gamma I, Fg=QAWc, f>=||Fg||, and Ws=Wc-C^-1 Fg. Then QAWs=0. The same audited stationary graph-block composition used by capacity_interval gives

    H=Ws* A Ws >=h I, h=j-a>0,
    f=graph_residual_fro/(1-rho),
    ||Wc|| <= sqrt(graph_vector_norm2)/(1-rho).

Here j is the exact serialized graph Gershgorin lower bound; a is the fully charged assembly/trace/residual graph error from the pinned certificate. Its derivation is v14.147/v14.156/v14.157, not a new uncharged small-block eigenvalue assumption.

Because [Ws,Q] is invertible onto the full finite space and A is block-diagonal in this basis,

    A^-1=Q C^-1 Q + Ws H^-1 Ws*,
    A>0,
    ||A^-1|| <= G := gamma^-1
        + [sqrt(graph_vector_norm2)/(1-rho)+f/gamma]^2/h.

No unit or Euclidean-orthonormal protected trace is assumed. The normalizer's large scales are already inside the represented column norm. The new rational consumer recomputes j,a directly and compares them exactly with the pinned certificate's recorded values.

Strict public upper bounds from the actual committed leading certificates:

| Sector | Full finite inverse norm G upper |
| --- | --- |
| even-v | 1.773e29 |
| odd-v | 7.040e25 |

These are deliberately conservative FULL finite inverse bounds, not replacements for either gamma_Q or S>=I.

## 3. Bound the entire finite-to-remote coupling in inverse energy

Set the proof-only split T0=2^256, not an implemented truncation.

On R<n<=T0, the previously audited physical diagonal/displacement bound from v14.195 gives ||D_restricted||<log(T0)+137<256+137<400. Since S>=I and A>0,

    B_near A^-1 B_near* <= D_restricted-I <=400I.

For n>T0>2R, the source-faithful physical row bound |B(n,m)|<32/n (v14.195) gives ||B_far||_HS^2<=1024N/T0. Hence, using the full finite bound G,

    chi^2 := ||B A^-1/2||^2 <=400+1024N G/T0 <21^2.

The disjoint output split combines the two squared bounds. This establishes a bounded inverse-energy coupling on the whole infinite half-line despite the unbounded logarithmic bare diagonal. It does not extrapolate the finite scalar envelopes to T0.

## 4. Keep the near boundary exact; expand only the far coupling

Let Near={R<n<=2R} and Far={n>2R}, separately on each physical parity lattice. B_K equals the exact physical B on Near.

For Far, use the exact physical kernel

    B(n,m)=c(z_n m-n z_m)/(n^2-m^2)+alpha p_n p_m,
    c=2/pi, p_n=L/[n(1+t/n^2)], t=pi^-2.

Retain the pole exactly. With K geometric terms, define these far row/finite column pairs:

| Far row Phi(n), zero on Near | Finite column W(m) |
| --- | --- |
| 1/n | w1(m)=-c z_m+alpha L p_m |
| (z_n/n)(R/n)^(2k+1), k=0..K-1 | c(m/R)^(2k+1) |
| (1/n)(R/n)^(2k), k=1..K-1 | -c z_m(m/R)^(2k) |
| p_n-L/n | alpha p_m |

There are 2K+1 channels. The exact pole-remainder row is not replaced by an asymptotic term. Prime, arch and other content of z_n remain physical. The bare remote block D, including its second Hankel, matching diagonal and physical odd-index shift, is kept exact.

The exact remainder E_K=B-B_K is zero on Near and, on Far, is

    E_K(n,m)=c(z_n m-n z_m)/(n^2-m^2) (m/n)^(2K).

This follows from the finite geometric-series identity; there is no untracked O-term. For m<=R<n/2, |z_n|<8, |z_m|<11 and c<1 give the displacement bound <20/n. Thus

    |E_K(n,m)| <= (20/n)(R/n)^(2K).

The same-parity decreasing-sum bound, with first far mode >2R, gives

    ||E_K||_HS^2 <=50(1+1/R) 2^(-4K).

The expansion is NOT applied at the adjacent n=R+1,m=R boundary, where a uniform small ratio would be false.

## 5. Whole Schur model error, including both cross terms

Define S_K=D-B_K A^-1 B_K*. Then D(S_K)=D(S), because their difference is bounded. Let tau=sqrt(G ||E_K||_HS^2). Expanding B_K=B-E_K gives

    BA^-1B* - B_K A^-1 B_K*
      = BA^-1 E_K* + E_K A^-1 B* - E_K A^-1 E_K*,

so BOTH cross terms and the quadratic remainder are retained, and

    ||S-S_K|| <=epsilon_K :=2 chi tau+tau^2.

For K=42, the exact rational consumer verifies:

| Quantity | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Whole Schur model operator error epsilon_42 | 6.157e-9 | 1.227e-10 |

This is an actual analytic whole-operator approximation theorem for the exactly defined model, not a numerical evaluation of its higher-channel matrix.

For the Far-Far block, the leading entry of M=W* A^-1 W is exactly the newly certified M11_256k. If a cached model replaces only that entry by the exact midpoint of its certified interval, its extra operator error is at most

    epsilon_11=radius(M11) ||u_Far||^2,
    ||u_Far||^2 <=1/a^2+1/(2a),
    a=512001 (even-v), a=512002 (odd-v).

Near and mixed Near-Far blocks are NOT changed by this coefficient replacement. They are not identified with a rank-one leading kernel. Let epsilon=epsilon_42+epsilon_11. Then

| Quantity | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Combined geometric/optional cached-M11 operator error | 3.454e-8 | 1.334e-10 |

The cached model therefore has floor >=1-epsilon>0. The M11 charge is optional for a direct exact finite-lift implementation; including it in the following budget is conservative.

For any domain trial ||y||<=1e-3, this combined discrepancy costs at most epsilon||y|| in action and epsilon||y||^2 in its quadratic form. An operator error need not be compared directly with the 5e-9 scalar tail reserve; its effect carries these trial factors.

## 6. Trace-aware finite lift replaces an unconditioned tiny-floor charge

A model action may use one finite RHS g=B_K* y, solve Az=g, and evaluate Dy-B_K z. Far coefficients Phi* y and exact Near coupling are retained in this RHS. A cached channel/near-block implementation is another option, but every uncomputed coefficient remains a required arithmetic certificate.

For any represented finite ztilde, use the FULL physical residual

    s=A ztilde-g, q_s>=||Q s||,
    d_s>=||Wtilde* s||.

The inverse decomposition in §2 gives the exact error energy bound

    E_z=<s,A^-1 s>
      <=q_s^2/gamma
        + [d_s/(1-rho)+f q_s/gamma]^2/h.

Proof: Ws*s=Wc*s-Fg* C^-1 Qs, so its norm is bounded by the bracket. This retains the protected component, rather than charging the full residual with gamma_Q or pretending that a projected residual is the complete source error.

The resulting remote action error satisfies

    ||B_K(ztilde-A^-1g)|| <=(chi+tau) sqrt(E_z).

Explicit sufficient targets, using the actual pinned graph constants:

| Finite-lift target | even-v | odd-v |
| --- | --- | --- |
| q_s=||Q(A ztilde-g)|| upper | 4e-19 | 1e-18 |
| d_s=||Wtilde*(A ztilde-g)|| upper | 8e-13 | 8e-13 |

They imply E_z<2e-24 and finite-lift action charge <3e-11 in both sectors. These are requirements for a NEW trial-dependent finite RHS, not claims that an old leading solve already meets them. Scalar, source, projector and residual-contraction uncertainty must be included before comparing with these targets. Every finite RHS error must enter s or be propagated explicitly; it cannot disappear into a measured CG residual.

Reserve an additional total remote output/action arithmetic charge <=3e-11 for bare-D action, channel/near evaluation and every remaining propagated numerical error. Do not allocate that ceiling independently to each omitted term.

Together with ||y||<=1e-3 and the combined model discrepancy:

| Conditional total | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Total action error if all new targets are met | 8.750e-11 | 4.894e-11 |
| Source+action stationary error if eta_total<=2e-10 | 4.875e-13 | 4.490e-13 |

The second row is 2 eta_total ||y||+||y|| delta_action. Both action bounds are below the v14.196 1e-10 ceiling; both stationary charges are below 5e-12. The stronger trial norm ceiling is sufficient for this contract, not a claim that an actual infinite trial exists yet.

The remaining v14.196 requirements are unchanged: certify total source assembly+finite-inverse transport <=2e-10, represented residual norm <=3e-5, appropriate stationary v intervals and the signed H0 enclosure <=2.9e-9. Feed all outward source/action/stationary charges through the audited paired corner consumer. No direct parity cancellation or actual residual norm is asserted here.

## 7. Reproducer, immutable inputs and verification scope

Script: research-notes/suzuki_whole_remote_schur_model_budget.py.
Output: payloads/whole_remote_schur_model_v14_210/whole-remote-schur-model-budget.json.
Input: both primary certificates in the complete archive exact_remote_leading_run_37965642729, pinned to the v14.207 SHA-256 values.

The standard-library-only consumer:
- verifies pinned input bytes, cutoff/sector/six-target flags;
- recomputes the charged graph floor and full finite inverse norm;
- computes all HS, inverse-weighted, model, M11 and conditional lift charges using exact Fraction arithmetic and upward 192-bit sqrt/rounding;
- checks all strict acceptance comparisons exactly;
- records higher-channel/near arithmetic and achieved-lift/trial/closure flags as false.

Independent small algebra checks cover 324 exact physical channel/remainder identities, three full-inverse examples with non-unit protected traces, and nine trace-aware full-residual energy examples. These test the finite algebra; the infinite proof is §§3–5 using the already-audited physical/domain bounds.

Two fresh local runs are byte-identical. Output length 31056 bytes, SHA-256:
f87966e695878482f71f1b311e1a857950a79061df295d0785361042a9a03515.
The direct generated file is read in length-checked chunks for publication, never pasted from truncated terminal output. A scoped lightweight CI workflow replays the committed script against committed primary certificates and compares the complete output byte-for-byte. Its result is pending at initial publication.

## 8. Next implementation gate

Construct a source-faithful infinite trial with numerical Near data and explicitly controlled Far channels/tails; evaluate the model action with the finite-lift residual contract; certify remote scalar/action arithmetic and source assembly; then evaluate both stationary scalars and residual norms for the existing paired consumer.

Unknown higher-channel coefficients, the Near-Far interface, bare-D action arithmetic, infinite source assembly and an admissible near/far trial are not silently replaced by the present operator theorem. The original C_S_32000 stays fixed. Infinite_capacity_tail_closed remains false.

HANDOFF-ACK
from: v14.208, v14.209
target: lane-a
status: closed
result: Independent archive/interval confirmations read. The approximate-display characterization note is incorporated; all new gates use rational bounds.

HANDOFF
target: sandbox, external-audit
type: whole-remote-model-and-finite-lift-audit
parent: v14.210
status: open
action: Independently audit the full finite inverse decomposition with the non-unit normalized traces, proof-only T0 coupling-energy bound, exact Near/Far channel identity and HS sum, both Schur cross terms, Far-only cached-M11 charge, and trace-aware full finite-lift residual energy. Replay the exact budget against the pinned primary certificates.
deliverable: theorem-or-specific-obstruction
constraints: Near rows and bare D remain exact; apply the geometric expansion only beyond 2R. Preserve all operator spaces and both parity lattices. Targets are not achieved finite-lift or infinite-trial certificates. Do not use approximate displays as bounds. Re-read latest HEAD/audit and collision-check before writes.

## 9. Committed-byte and CI replay receipt

Source commit: 47c25895802cb16be107071156ec52b80fe3e318.
All four new committed files were fetched by that commit and compared byte-for-byte with their direct local source/generated content.

Scoped replay run [37975109834](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37975109834), job 113971317974, completed/success. The committed standard-library consumer ran against the committed pinned primary certificates and its complete generated output passed cmp against the committed 31056-byte payload.

This closes the exact computational replay gate. It does not replace the requested independent analytic audit, prove the finite-lift targets achieved, or construct an infinite trial. The full-payload and closure flags in §7 remain false.

Receipt collision check: immediately before this append live HEAD 47c25895802cb16be107071156ec52b80fe3e318; v14.210 is the latest entry, with no newer audit/Sandbox update observed. Only this lane's v14.210 receipt is appended with a nonforced expected-head update.
