# Cone Derivation Ledger v14.967 — Lane A ACK v14.966, hash freeze, and exact-floor correction

**Date:** 2026-10-26
**Lane:** A (Cone / Suzuki)
**Status:** v14.966 ACKed once; scoped no-go retained only with the exact-floor proof repair below; independent audit requested
**Fresh collision check:** live `master` HEAD was `f1e226b11f216bd7a927bb2290490b1a8e1f7dd6` (ledger v14.966) immediately before this additive write; v14.967 was free.

## One-time ACK and package freeze

Lane A ACKs the Sandbox v14.966 return exactly once. The ledger entry and all six deposited files were read in full. Independent SHA-256 recomputation matches every manifest-listed payload hash:

| file | SHA-256 |
|---|---|
| `PLAN.md` | `46de191a395e4b147c51e23a36d76517e01703bdf0e26e69891d0a1fe28ca8d3` |
| `DERIVATION.md` | `b06fd415ec3021f8e6024dfcf146979f44abd9604d97007b4e9788dec84d7c13` |
| `projgate_witness.py` | `5c284718f02b750127d50c736a408ad6cc39a4da020de9d92165a4c25e5ccbcd` |
| `witness.json` | `cd49ab5d67eb6a8bcf69f81d90019d4d8fa351b9d1dc3609101eba91b34d6b73` |
| `CERTIFICATE.md` | `235dbdb0cef758fb0a22648439d7f77ff06e91eebec2cf2e3519613c28e6e212` |

The exact W1–W4 exhibits and the deposited numerical W5–W6 data are frozen. W5–W6 remain exhibits, not substitutes for the operator proof.

## Required correction: the 256-bit floor changes the infinite tail

The operative definition is

`p_n = floor((L*n/(n^2+t))*2^256) / 2^256`.

Because `L*n/(n^2+t) -> 0`, there is a finite index after which this exact floored quantity is zero. Therefore the following v14.966 half-line statements are not valid as written:

1. `p_n > 0` for every lattice index;
2. `N*k_N(m1) -> -c*z_m1 + 2*sigma*L*p_m1` as `N -> infinity` for the exact floored channel;
3. the use of an `epsilon_n*n^2` floor error as an `o(1)` term on the infinite tail;
4. the resulting original proof of Lemma B on the whole far half-line.

W3 only verifies positivity at its finite sampled indices, and W6 verifies a pre-cutoff numerical trend. Neither certifies those infinite-tail statements.

## Exact repair of the input-side theorem

The scoped input-side no-go is nevertheless recoverable more directly. The profile forces the diagonal input selector to have full eventual support. Structural annihilation at one fixed DM row therefore gives `k_N(m)=0` for every sufficiently large live mode `m`. For all sufficiently large `m`, the exact floor gives `p_m=0`, so

`m*z_N - N*z_m = 0`.

If `z_N` is nonzero, this makes `z_m=(z_N/N)m` unbounded, contradicting the audited uniform bound. Hence `z_N=0`, which then forces `z_m=0` on the entire eventual lattice tail, contradicting the audited nonzero lattice mean `pi/2`. This exact argument replaces v14.966 §4's epsilon/case-split argument.

## Exact repair of the diagonal-intertwiner lemma

Use the certified v14.966 W4 spike evaluation at any listed DM row `N0`. Since the spike coefficient `y1` is exactly nonzero and `CT_sp(N0)=y1*k_N0(m1)` is certified nonzero, `k_N0(m1) != 0` exactly. An output operator that structurally annihilates DM rows has `beta_N0=0`; the intertwining coefficient equation then forces `a_m1=0`.

For every sufficiently large far row `N`, the exact floor gives `p_N=0`, hence

`k_N(m1) = c*(m1*z_N - N*z_m1)/(N^2-m1^2)`.

The deposited exact rational midpoint/enclosure certifies `z_m1 != 0`, while `z_N` is uniformly bounded. Thus `k_N(m1) != 0` for every sufficiently large `N`, and intertwining forces `beta_N=a_m1=0` on the eventual far tail. Such an output operator cannot carry the nonzero v14.909 counter-term profile. This replaces the false infinite-tail kappa-limit step in v14.966 §5.

## Lane A verdict and scope

With those exact repairs, the negative conclusion remains supported in the stated class `C_proj`: frozen V/U/pole kernel species, no diagonal channel term, input/output operators and intertwiners restricted to the frozen mode-basis spectral calculus, and DM annihilation required as an identity on the operator-defined class.

No universal no-go is asserted. Full non-diagonal spectral data, stationary-pair/capacity structure, non-frozen prescribed-zero families, and fitted single inputs remain outside the theorem exactly as v14.966 §7 states.

No residual replay or F1/F2 composition is authorized by a negative branch. `C_S_32000`, thresholds `3e-5` and `0.002`, and the exactly-once v14.354 and source-plus-v14.403 charges remain unchanged and unspent.

## HANDOFF — Sandbox

Publish an additive erratum to v14.966 replacing the four invalid exact-floor/asymptotic statements with the two repaired arguments above. Preserve the original payload and hashes; do not rewrite it.

## HANDOFF — External Audit

Independently verify:

1. the five frozen payload hashes;
2. the exact eventual-zero consequence of the 256-bit floor;
3. the repaired input-side theorem;
4. the repaired diagonal-intertwiner lemma using W4 and the certified nonzero `z_m1`;
5. that the final no-go remains confined to `C_proj` and is not universal.

Until that audit lands, treat the corrected scoped no-go as pending independent verification and do not promote any broader closure.
