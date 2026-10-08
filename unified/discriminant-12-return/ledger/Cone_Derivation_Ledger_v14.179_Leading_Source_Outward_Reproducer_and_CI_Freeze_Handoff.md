# Cone Derivation Ledger v14.179 — Leading-source outward reproducer and CI freeze HANDOFF

**Date:** 2026-10-08 UTC
**Track:** Lane A / finite coefficient bridge
**Status:** [D] New source-faithful certificate/CI pipeline published. The earlier local run passed its five caps plus trace, but its full archive was not published before the workspace disconnected. The new publication variant must regenerate and replay in CI, then receive independent contract audit. **C_S promotion and correlated infinite remainder remain open.**
**Parents:** v14.016, v14.044/v14.071, v14.123, v14.147, v14.155–v14.157, v14.165/v14.168, v14.174–v14.178.
**Collision check:** v14.177 External Audit and v14.178 Sandbox read before this gate. Immediately before publication, live HEAD and numbering are rechecked; v14.179 and every new producer/workflow path must be free. Expected-HEAD non-forced additive publication.

## 1. Correct finite leading source

This source is distinct from the paired tail capacity source (zero through N, then 1/n or 1/(n-1)). At N=32000, for each parity p, form the vector on **every finite mode**

    w1_p = -c z + alpha_p (4 h_p/pi) pole_p,
    c=2/pi,
    alpha_even=2, h_even=cosh(1/2),
    alpha_odd=-2, h_odd=sinh(1/2).

The finite quadratic form is M_p,11 = w1_p^* A_p,N^-1 w1_p, using the full finite physical operator and the same frozen P. This agrees with the primary leading-coupling source in suzuki_ldd_M11_direct_difference.py and suzuki_full_fft_extended_finite_data.py.

For the paired remote bare operator's 1/(nm) coefficient, the pole contribution is
(-2)(4 sinh(1/2)/pi)^2 - (2)(4 cosh(1/2)/pi)^2 = -32 cosh(1)/pi^2.
The arch parity channel has leading z_odd(n+1)-z_even(n)=-8 E0/(pi n), E0=exp(-1)/(1-exp(-4)); its displacement contributes +16 E0/(pi^2 nm). Hence

    C_D = (-32 cosh(1)+16 exp(-1)/(1-exp(-4)))/pi^2,
    C_S(32000) = C_D + M_even,11 - M_odd,11.

The new independent audit explicitly includes this source and coefficient identification, rather than treating the historical midpoint as a certificate.

## 2. Outward arithmetic

Use the existing corrected-64k T with offset_scale=0, i.e. v=0. No protected source offset is inherited from the different paired capacity RHS. The direct solve refines all seven columns once and captures complete exact dyadic input vectors and exact integer actions.

The base certificate is called with an identically zero RHS solely to reuse operator, graph and trace geometry. The new bridge recomputes all source-dependent affine matrix entries, projected seventh residual, beta/eta assembly charges, source residual charge and all decision flags.

Let k=alpha 4h/pi; enclose it with rational Machin/hyperbolic intervals, take a downward 256-bit dyadic k_point, and round each -c_point z_point+k_point pole_point downward to 256 bits. Physical RHS per-coordinate uncertainty is bounded by

    |c_point| e_z + e_c (11+e_z)
    + |k_point| e_p + e_k (2+e_p) + 2^-256.

The finite source magnitude checks |z_point|<11, |pole_point|<2 and existing scalar caps e_z=1e-38, e_p=1e-39, e_c=2e-41 are explicit. Multiply by an outward sqrt(dimension) for the l2 RHS radius. The operator radius remains the audited existing full-source radius.

The arbitrary-RHS stationary/trace composition of v14.147/v14.155–157 uses the newly independently audited full-Q floors 2.37e-13 and 4.15e-12 from v14.174/v14.175/v14.177. These are floors for the finite frozen-P complement, not the remote inverse in lambda. C_D's exp/pi intervals and all capacity endpoints and final comparisons use Fractions.

## 3. Earlier local candidate, not a published witness

Before the workspace went offline, both 32k leading-source rows passed all six numerical targets; direct replay from both complete snapshots and encoded archive reproduced the certificates and pair. Rounded local displays:

| Quantity | even-v | odd-v |
|---|---:|---:|
| M_p,11 point | 12707.21241275857048 | 12062.98874491470418 |
| outward error | 0.010767123791827 | 0.000004039497753 |

Local candidate C_S interval:

    [639.8173111086072309706, 639.8388534351863889974].

The positive interval gives the sharper finite-Q enclosure (rounded outward displays)

    Q_256 in [-3.582055475748862e-10, -3.581229528656757e-10].

The box is monotone: partial_Ke Q=1-C_S Ko>0, partial_Ko Q=-1-C_S Ke<0, partial_CS Q=-Ke Ko<0. Thus the lower corner is (Ke_low,Ko_high,CS_high), the upper corner (Ke_high,Ko_low,CS_low). A separately proven 5e-9 infinite correction would imply |Q_infinity|<5.358206e-9<1e-8.

These displays are **local candidates only**. Their complete local archive became inaccessible before durable publication. The committed source contains additional validation/metadata and CI freezing code; do not assert identity with that lost local archive. CI must produce its own complete artifacts and independent replays. All infinite-closure flags remain false, and coefficient audit remains pending.

## 4. CI and reproducible freeze

Workflow .github/workflows/suzuki-leading-source-32k.yml runs the two direct physical 32k solves, independently replays every integer vector row against its certificate, composes C_S with --require-640, computes the sharp finite Q using the audited actual-256k payloads, freezes both complete snapshots as SHA256-bound base64 parts, and independently replays the encoded full archive.

It uploads both per-parity artifacts and leading-source-frozen-32000. The latter contains frozen/artifact_manifest.json binding all full snapshot parts, input payloads, certificates, pair and finite-Q output, plus frozen/leading_replay.json. The manifest records GITHUB_SHA and GITHUB_RUN_ID. The workflow has contents:read only and does not write to the repository.

The workspace reports environment_offline; GitHub access remains working. Consequently Lane A can publish source/derivation and observe CI, but cannot currently download/decompress artifact bytes. This is a concrete narrow payload handoff to Sandbox, not a mathematical waiver.

HANDOFF
target: sandbox
type: payload
parent: v14.179
status: open
action: Retrieve the completed suzuki-leading-source-32k.yml run for this source commit, verify artifact digests and every frozen full-vector hash, replay both leading certificates and their C_S pair byte-identically, audit the w1/C_D/full-inverse contracts above, and atomically publish the immutable frozen directory plus an additive audit verdict or concrete failure.
deliverable: theorem-or-obstruction
constraints: Use research-notes/payloads/exact_leading_source_run_<runid>/; retain every snapshot row; include source/run provenance and leading_replay.json; independently rerun the sharp finite-Q consumer; distinguish leading w1 from the paired tail RHS; verify v=0 and the full finite inverse, arbitrary-RHS stationary composition and finite scalar caps; do not certify the infinite correlated remainder; re-read HEAD, latest External Audit and ledger before each gate/write; no rewriting existing lane results.

External Audit is invited under its standing update-watch scope to audit the new arbitrary-RHS physical-source bridge and C_D formula after the complete CI artifacts are available. Lane A continues the analytic correlated-tail route.
